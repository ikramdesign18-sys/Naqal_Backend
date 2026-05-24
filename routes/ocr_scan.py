from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.ocr_service import extract_text_from_image, extract_barcode_from_image
from app.services.product_analyzer import ProductAnalyzer

router = APIRouter()
product_analyzer = ProductAnalyzer()

@router.post("/scan-label")
async def scan_product_label(image: UploadFile = File(...)):
    """Scan a product label image - extracts ingredients and barcode"""
    try:
        image_bytes = await image.read()
        
        # Extract text using OCR
        ocr_result = extract_text_from_image(image_bytes)
        
        # Try to extract barcode
        barcode_result = extract_barcode_from_image(image_bytes)
        
        # Analyze ingredients if found
        ingredient_analysis = None
        if ocr_result.get("ingredients"):
            ingredients_text = ', '.join(ocr_result["ingredients"])
            ingredient_analysis = product_analyzer.analyze_ingredients(ingredients_text)
        
        # Look up barcode if found
        product_info = None
        if barcode_result.get("found"):
            product_info = await product_analyzer.lookup_barcode(barcode_result["barcode"])
        
        return {
            "status": "success",
            "ocr_result": ocr_result,
            "barcode": barcode_result,
            "product_info": product_info,
            "ingredient_analysis": ingredient_analysis
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))