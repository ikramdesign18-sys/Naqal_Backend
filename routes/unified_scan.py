from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from typing import Optional
from app.services.product_analyzer import ProductAnalyzer
from app.services.barcode_scanner import BarcodeScanner
from app.services.ingredient_ocr import IngredientOCR
from PIL import Image
import io

router = APIRouter()
product_analyzer = ProductAnalyzer()
barcode_scanner = BarcodeScanner()
ingredient_ocr = IngredientOCR()

@router.post("/quick-scan")
async def quick_scan(
    image: UploadFile = File(None),
    barcode: Optional[str] = Form(None),
    product_name: Optional[str] = Form(None),
    price_pkr: Optional[float] = Form(None),
):
    """
    Unified quick scan - camera or manual
    Returns ingredient safety + fake detection in one call
    """
    try:
        result = {
            "status": "success",
            "barcode_info": None,
            "ingredient_analysis": None,
            "fake_check": None,
            "warnings": [],
            "overall_verdict": "unknown"
        }
        
        # 1. Barcode processing
        if barcode:
            barcode_info = barcode_scanner.validate_barcode(barcode)
            result["barcode_info"] = barcode_info
            
            # Try to lookup product by barcode
            product = await product_analyzer.lookup_barcode(barcode)
            if "error" not in product:
                if not product_name:
                    product_name = product.get("name", "")
                
                # Analyze ingredients from barcode lookup
                ingredients = product.get("ingredients", "")
                if ingredients:
                    result["ingredient_analysis"] = product_analyzer.analyze_ingredients(ingredients)
        
        # 2. Product name / fake detection
        if product_name:
            fake_check = product_analyzer.check_fake_product(
                product_name,
                barcode=barcode,
                price=price_pkr
            )
            result["fake_check"] = fake_check
            
            if fake_check.get("verdict") == "likely_fake":
                result["warnings"].append({
                    "type": "fake_product",
                    "severity": "high",
                    "message": f"⚠️ {product_name} is likely FAKE!",
                    "details": fake_check.get("warnings", []),
                    "health_risks": fake_check.get("health_risks", "")
                })
        
        # 3. Ingredient safety verdict
        if result["ingredient_analysis"]:
            ing_analysis = result["ingredient_analysis"]
            if ing_analysis.get("verdict") == "avoid":
                result["warnings"].append({
                    "type": "harmful_ingredients",
                    "severity": "high",
                    "message": "This product contains harmful ingredients for your skin",
                    "irritants": ing_analysis.get("irritants", []),
                    "comedogenic": ing_analysis.get("comedogenic_ingredients", [])
                })
            elif ing_analysis.get("verdict") == "caution":
                result["warnings"].append({
                    "type": "caution",
                    "severity": "medium",
                    "message": "Some ingredients may cause irritation",
                })
        
        # 4. Overall verdict
        if result["fake_check"] and result["fake_check"].get("verdict") == "likely_fake":
            result["overall_verdict"] = "danger"
        elif result["ingredient_analysis"] and result["ingredient_analysis"].get("verdict") == "avoid":
            result["overall_verdict"] = "avoid"
        elif result["ingredient_analysis"] and result["ingredient_analysis"].get("verdict") == "caution":
            result["overall_verdict"] = "caution"
        else:
            result["overall_verdict"] = "safe"
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ocr-ingredients")
async def ocr_ingredients(image: UploadFile = File(...)):
    """Extract ingredients from product label photo using OCR"""
    try:
        image_bytes = await image.read()
        
        # For now, return placeholder - real OCR integration next
        # We'll use Tesseract or Google ML Kit in production
        text = "Ingredients extracted from image will appear here"
        
        parsed = ingredient_ocr.parse_ingredients_text(text)
        
        # If ingredients found, analyze them
        analysis = None
        if parsed.get("ingredients_text") and len(parsed.get("ingredients", [])) > 0:
            analysis = product_analyzer.analyze_ingredients(parsed["ingredients_text"])
        
        return {
            "status": "success",
            "ocr_result": parsed,
            "ingredient_analysis": analysis,
            "message": "OCR ready for integration with device-level ML Kit"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))