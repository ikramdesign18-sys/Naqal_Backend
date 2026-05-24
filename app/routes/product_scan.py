from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.product_analyzer import ProductAnalyzer

router = APIRouter()
product_analyzer = ProductAnalyzer()

class BarcodeRequest(BaseModel):
    barcode: str
    product_type: str = "skincare"
    price_pkr: Optional[float] = None

class IngredientsRequest(BaseModel):
    ingredients: str
    product_type: str = "skincare"
    product_name: Optional[str] = None
    price_pkr: Optional[float] = None

class SearchRequest(BaseModel):
    query: str
    price_pkr: Optional[float] = None

@router.post("/scan-barcode")
async def scan_barcode(request: BarcodeRequest):
    """Scan product by barcode with fake detection + GS1 verification"""
    try:
        product = await product_analyzer.lookup_barcode(request.barcode)
        
        if "error" in product:
            raise HTTPException(status_code=404, detail=product["error"])
        
        # Analyze ingredients
        analysis = product_analyzer.analyze_ingredients(
            product.get("ingredients", ""),
            request.product_type
        )
        
        # Check if fake product (with GS1 verification)
        product_name = product.get("name", "")
        brand = product.get("brand", "")
        search_name = f"{product_name} {brand}"
        fake_check = await product_analyzer.check_fake_product(
            search_name,
            barcode=request.barcode,
            price=request.price_pkr
        )
        
        return {
            "status": "success",
            "product": product,
            "ingredient_analysis": analysis,
            "fake_check": fake_check
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/scan-ingredients")
async def scan_ingredients(request: IngredientsRequest):
    """Scan by pasting ingredients list with fake detection"""
    try:
        analysis = product_analyzer.analyze_ingredients(
            request.ingredients,
            request.product_type
        )
        
        fake_check = None
        if request.product_name:
            fake_check = await product_analyzer.check_fake_product(
                request.product_name,
                price=request.price_pkr
            )
        
        return {
            "status": "success",
            "ingredient_analysis": analysis,
            "fake_check": fake_check
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/search")
async def search_product(request: SearchRequest):
    """Search product by name with fake detection + GS1 verification"""
    try:
        product = await product_analyzer.search_product(request.query)
        
        if "error" in product:
            raise HTTPException(status_code=404, detail=product["error"])
        
        analysis = product_analyzer.analyze_ingredients(
            product.get("ingredients", "")
        )
        
        product_name = product.get("name", "")
        brand = product.get("brand", "")
        search_name = f"{product_name} {brand}"
        fake_check = await product_analyzer.check_fake_product(
            search_name,
            price=request.price_pkr
        )
        
        return {
            "status": "success",
            "product": product,
            "ingredient_analysis": analysis,
            "fake_check": fake_check
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/report-fake")
async def report_fake(product_name: str, issue: str, location: str = "Pakistan"):
    """Report a fake product"""
    from app.services.fake_products_db import add_fake_report
    
    success = add_fake_report(product_name, issue, location)
    
    return {
        "status": "success" if success else "not_found",
        "message": "Report recorded. Thank you for keeping Pakistan safe!" if success else "Product not found in database"
    }