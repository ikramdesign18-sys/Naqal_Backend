import httpx
from typing import Dict, List, Optional
from app.services.fake_products_db import search_fake_db
from app.services.ingredient_knowledge import (
    analyze_ingredient_knowledge, 
    get_safety_label, 
    get_comedogenic_label, 
    get_irritant_label, 
    get_ewg_label
)
from app.services.gs1_service import verify_barcode_gs1, get_country_from_barcode

# Try to load Groq service
groq_explain = None
groq_fake = None
try:
    from app.services.groq_service import explain_product_safety, analyze_fake_risk
    groq_explain = explain_product_safety
    groq_fake = analyze_fake_risk
    print("✅ Groq Product Analysis service loaded")
except Exception as e:
    print(f"⚠️ Groq Product Analysis not loaded: {e}")

class ProductAnalyzer:
    """
    Naqal Product Safety Engine v3.0 + Groq AI + GS1 Verification
    Uses Open Beauty Facts API + 250+ ingredient knowledge base
    Includes Pakistan fake product detection + GS1 barcode verification
    Works for skincare AND haircare products
    """
    
    async def lookup_barcode(self, barcode: str) -> dict:
        """Look up product by barcode"""
        urls = [
            f"https://world.openbeautyfacts.org/api/v2/product/{barcode}.json",
            f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json",
        ]
        
        async with httpx.AsyncClient() as client:
            for url in urls:
                try:
                    response = await client.get(url)
                    data = response.json()
                    if data.get("status") == 1:
                        product = data.get("product", {})
                        return {
                            "name": product.get("product_name", "Unknown"),
                            "brand": product.get("brands", "Unknown"),
                            "ingredients": product.get("ingredients_text", ""),
                            "image": product.get("image_url", ""),
                            "categories": product.get("categories", ""),
                        }
                except:
                    continue
        return {"error": "Product not found"}
    
    async def search_product(self, query: str) -> dict:
        """Search product by name"""
        url = f"https://world.openbeautyfacts.org/cgi/search.pl?search_terms={query}&search_simple=1&json=1"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                data = response.json()
                products = data.get("products", [])
                for p in products:
                    if p.get("ingredients_text"):
                        return {
                            "name": p.get("product_name", "Unknown"),
                            "brand": p.get("brands", "Unknown"),
                            "ingredients": p.get("ingredients_text", ""),
                            "image": p.get("image_url", ""),
                            "categories": p.get("categories", ""),
                        }
                return {"error": "No products with ingredients found"}
            except:
                return {"error": "Search failed"}
    
    def advanced_ingredient_analysis(self, ingredients_text: str) -> dict:
        """Deep ingredient analysis using 250+ ingredient knowledge base"""
        if not ingredients_text:
            return {"error": "No ingredients found"}
        
        ingredients_list = [i.strip() for i in ingredients_text.lower().split(',') if len(i.strip()) > 2]
        
        analyzed = []
        total_safety = 0
        total_comedogenic = 0
        total_irritant = 0
        acne_triggers = 0
        allergens = 0
        toxic_found = []
        banned_found = []
        pregnancy_unsafe = 0
        fungal_unsafe = 0
        ewg_high_hazard = 0
        
        for ing in ingredients_list:
            knowledge = analyze_ingredient_knowledge(ing)
            
            total_safety += knowledge.get("safety", 3)
            total_comedogenic += knowledge.get("comedogenic", 0)
            total_irritant += knowledge.get("irritant", 0)
            
            if knowledge.get("acne_trigger", 0) >= 3:
                acne_triggers += 1
            if knowledge.get("allergen", False):
                allergens += 1
            if knowledge.get("toxic", False):
                toxic_found.append(ing)
            if knowledge.get("banned"):
                banned_found.append({"ingredient": ing, "banned_in": knowledge["banned"]})
            if not knowledge.get("pregnancy_safe", True):
                pregnancy_unsafe += 1
            if not knowledge.get("fungal_safe", True):
                fungal_unsafe += 1
            if knowledge.get("ewg_score", 0) >= 7:
                ewg_high_hazard += 1
            
            analyzed.append({
                "ingredient": ing,
                "safety_score": knowledge.get("safety", 3),
                "safety_label": get_safety_label(knowledge.get("safety", 3)),
                "comedogenic_score": knowledge.get("comedogenic", 0),
                "comedogenic_label": get_comedogenic_label(knowledge.get("comedogenic", 0)),
                "irritant_score": knowledge.get("irritant", 0),
                "irritant_label": get_irritant_label(knowledge.get("irritant", 0)),
                "ewg_score": knowledge.get("ewg_score", 3),
                "ewg_label": get_ewg_label(knowledge.get("ewg_score", 3)),
                "acne_trigger": knowledge.get("acne_trigger", 0) >= 3,
                "fungal_safe": knowledge.get("fungal_safe", True),
                "pregnancy_safe": knowledge.get("pregnancy_safe", True),
                "is_toxic": knowledge.get("toxic", False),
                "source": knowledge.get("source", "unknown"),
            })
        
        count = len(ingredients_list) if ingredients_list else 1
        
        avg_safety = total_safety / count
        avg_comedogenic = total_comedogenic / count
        avg_irritant = total_irritant / count
        
        if toxic_found or banned_found:
            overall_verdict = "avoid"
        elif avg_safety < 2 or avg_irritant > 3:
            overall_verdict = "avoid"
        elif avg_safety < 3 or avg_comedogenic > 2:
            overall_verdict = "caution"
        else:
            overall_verdict = "safe"
        
        return {
            "total_ingredients": count,
            "analyzed_ingredients": analyzed,
            "summary": {
                "average_safety": round(avg_safety, 1),
                "average_comedogenic": round(avg_comedogenic, 1),
                "average_irritant": round(avg_irritant, 1),
                "acne_triggers": acne_triggers,
                "allergens": allergens,
                "ewg_high_hazard_count": ewg_high_hazard,
                "pregnancy_unsafe_count": pregnancy_unsafe,
                "fungal_unsafe_count": fungal_unsafe,
            },
            "alerts": {
                "toxic_ingredients": toxic_found,
                "banned_ingredients": banned_found,
            },
            "overall_verdict": overall_verdict,
            "data_sources": ["INCI Decoder", "CosDNA", "EWG Skin Deep", "SkinCarisma", "Pakistan DRAP"],
        }
    
    def analyze_ingredients(self, ingredients_text: str, skin_type: str = "normal") -> dict:
        """Quick ingredient analysis (legacy + new)"""
        if not ingredients_text:
            return {"error": "No ingredients found"}
        
        advanced = self.advanced_ingredient_analysis(ingredients_text)
        
        result = {
            "verdict": advanced.get("overall_verdict", "unknown"),
            "summary": advanced.get("summary", {}),
            "alerts": advanced.get("alerts", {}),
            "analyzed_count": advanced.get("total_ingredients", 0),
            "data_sources": advanced.get("data_sources", []),
        }
        
        # Add Groq AI explanation if available
        if groq_explain:
            try:
                ai_explanation = groq_explain(ingredients_text, skin_type)
                if ai_explanation:
                    result["ai_explanation"] = ai_explanation
            except Exception as e:
                print(f"Groq explanation skipped: {e}")
        
        return result
    
    async def check_fake_product(self, product_name: str, barcode: str = None, price: float = None) -> dict:
        """Check if product is potentially fake using Pakistan database + GS1 + Groq AI"""
        fake_data = search_fake_db(product_name)
        
        # GS1 verification (strongest check - runs regardless)
        gs1_result = None
        country_origin = None
        if barcode:
            gs1_result = await verify_barcode_gs1(barcode)
            country_origin = get_country_from_barcode(barcode)
        
        if not fake_data:
            return {
                "is_known_fake_risk": False,
                "message": "Not in fake database",
                "gs1_verified": gs1_result.get("valid", False) if gs1_result else None,
                "country_origin": country_origin
            }
        
        warnings = []
        fake_score = 0
        
        # GS1 check (most reliable - 95%+ accurate)
        if gs1_result:
            if gs1_result.get("valid"):
                warnings.append(f"✅ GS1 verified barcode from {country_origin}")
                fake_score -= 10
            else:
                warnings.append(f"⚠️ Barcode not found in GS1 global database")
                fake_score += 15
        
        if barcode and fake_data.get("real_barcode_prefix"):
            barcode_prefix = barcode[:3]
            if barcode_prefix not in fake_data["real_barcode_prefix"]:
                warnings.append(f"Barcode prefix {barcode_prefix} doesn't match authentic {fake_data['brand']}")
                fake_score += 40
        
        if price and fake_data.get("real_price_range_pkr"):
            min_price, max_price = fake_data["real_price_range_pkr"]
            if price < min_price * 0.5:
                warnings.append(f"Price too low: {price} PKR (normal: {min_price}-{max_price} PKR)")
                fake_score += 30
        
        if fake_data.get("fake_indicators"):
            indicators = fake_data['fake_indicators'][:3]
            warnings.append(f"Common fake signs: {indicators}")
            fake_score += 20
        
        if fake_score >= 50:
            verdict = "likely_fake"
        elif fake_score >= 25:
            verdict = "suspicious"
        else:
            verdict = "probably_genuine"
        
        result = {
            "is_known_fake_risk": True,
            "brand": fake_data["brand"],
            "category": fake_data["category"],
            "fake_score": fake_score,
            "verdict": verdict,
            "warnings": warnings,
            "health_risks": fake_data.get("health_risks", ""),
            "toxic_additives_in_fakes": fake_data.get("fake_toxic_additives", []),
            "community_reports": fake_data.get("report_count", 0),
            "gs1_verified": gs1_result.get("valid", False) if gs1_result else None,
            "country_origin": country_origin,
        }
        
        # Add Groq AI fake analysis if available
        if groq_fake and (price or barcode):
            try:
                ai_analysis = groq_fake(
                    product_name, 
                    price or 0, 
                    barcode or "", 
                    fake_data.get("fake_indicators", [])[:3]
                )
                if ai_analysis:
                    result["ai_fake_analysis"] = ai_analysis
            except Exception as e:
                print(f"Groq fake analysis skipped: {e}")
        
        return result