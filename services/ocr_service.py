"""
Naqal Free OCR Service
Uses EasyOCR - 100% free, no credit card, works offline
Supports English + Urdu text extraction
"""

import re
import io

# Lazy load EasyOCR (loads on first use)
_reader = None

def get_reader():
    global _reader
    if _reader is None:
        try:
            import easyocr
            print("Loading EasyOCR... (one-time setup)")
            _reader = easyocr.Reader(['en', 'ur'])  # English + Urdu
            print("✅ EasyOCR ready!")
        except Exception as e:
            print(f"⚠️ EasyOCR not available: {e}")
            return None
    return _reader

def extract_text_from_image(image_bytes: bytes) -> dict:
    """
    Extract text from product label image using EasyOCR
    100% free, no credit card needed
    """
    try:
        reader = get_reader()
        
        if reader is None:
            return {
                "text": "OCR not available. Please type ingredients manually.",
                "ingredients": [],
                "source": "none"
            }
        
        # Convert bytes to image array
        import numpy as np
        from PIL import Image
        
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image_np = np.array(image)
        
        # Run OCR
        results = reader.readtext(image_np)
        
        # Combine all detected text
        full_text = ' '.join([text for _, text, confidence in results])
        
        # Parse ingredients
        ingredients = _parse_ingredients_from_text(full_text)
        
        # Calculate average confidence
        if results:
            avg_confidence = sum(conf for _, _, conf in results) / len(results)
        else:
            avg_confidence = 0
        
        return {
            "text": full_text,
            "ingredients": ingredients,
            "confidence": round(avg_confidence, 2),
            "source": "easyocr"
        }
        
    except Exception as e:
        print(f"OCR error: {e}")
        return {
            "text": "",
            "ingredients": [],
            "confidence": 0,
            "source": "error",
            "error": str(e)
        }

def _parse_ingredients_from_text(text: str) -> list:
    """Extract ingredients list from OCR text"""
    text_lower = text.lower()
    
    # Look for ingredients section
    ingredients_start = -1
    for header in ["ingredients:", "ingredients", "inci:", "composition:", "contains:"]:
        idx = text_lower.find(header)
        if idx != -1:
            ingredients_start = idx + len(header)
            break
    
    if ingredients_start == -1:
        ingredients_text = text
    else:
        ingredients_text = text[ingredients_start:]
    
    # Split by commas
    ingredients = [i.strip() for i in ingredients_text.split(',') if len(i.strip()) > 2]
    
    # Clean up
    cleaned = []
    for ing in ingredients:
        ing = re.sub(r'[\(\[].*?[\)\]]', '', ing)
        ing = re.sub(r'[^a-zA-Z0-9\s\-\.]', '', ing)
        ing = ing.strip()
        if len(ing) > 2:
            cleaned.append(ing)
    
    return cleaned[:50]

def extract_barcode_from_image(image_bytes: bytes) -> dict:
    """
    Extract barcode from product image
    """
    try:
        from PIL import Image
        from pyzbar.pyzbar import decode
        
        image = Image.open(io.BytesIO(image_bytes))
        barcodes = decode(image)
        
        if barcodes:
            return {
                "barcode": barcodes[0].data.decode('utf-8'),
                "type": barcodes[0].type,
                "found": True
            }
        
        return {"found": False, "barcode": None}
        
    except ImportError:
        return {"found": False, "note": "Install pyzbar: pip install pyzbar"}
    except Exception as e:
        return {"found": False, "error": str(e)}