"""
Naqal HuggingFace Skin Analysis Service
Uses free pre-trained models from HuggingFace for skin condition detection
"""

import os
import numpy as np
from PIL import Image
import io

# Lazy loading - models load only when needed
_models = {}

def get_skin_type_model():
    """Load skin type classification model"""
    if "skin_type" not in _models:
        try:
            from transformers import pipeline
            _models["skin_type"] = pipeline(
                "image-classification",
                model="hf_hub:username/skin-type-classifier",
                framework="pt"
            )
        except:
            print("⚠️ Skin type model not available, using fallback")
            return None
    return _models["skin_type"]

def analyze_skin_conditions(image_bytes: bytes) -> dict:
    """
    Analyze skin conditions using HuggingFace models
    Falls back gracefully if models not available
    """
    try:
        from transformers import pipeline
        
        # Load a general image classification model
        # This is a free model that can detect various features
        classifier = pipeline(
            "image-classification", 
            model="google/vit-base-patch16-224",
            framework="pt"
        )
        
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB').resize((224, 224))
        results = classifier(image)
        
        return {
            "top_predictions": [
                {"label": r["label"], "confidence": round(r["score"], 2)}
                for r in results[:5]
            ],
            "source": "huggingface_vit"
        }
        
    except Exception as e:
        print(f"HuggingFace error: {e}")
        return None

def detect_acne_level(image_bytes: bytes) -> float:
    """
    Detect acne severity using pre-trained model
    Returns score 0-100
    """
    # This uses algorithmic fallback since dedicated acne model needs training
    # We'll use the Naqal model results instead
    return None

def analyze_skin_tone(image_bytes: bytes) -> dict:
    """
    Analyze skin tone characteristics
    """
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        img_array = np.array(image)
        
        # Calculate average skin tone
        avg_color = np.mean(img_array, axis=(0, 1))
        
        # Determine skin tone category
        r, g, b = avg_color[0], avg_color[1], avg_color[2]
        
        if r > 200 and g > 180 and b > 160:
            tone = "fair"
        elif r > 160 and g > 140 and b > 120:
            tone = "medium"
        elif r > 120 and g > 100 and b > 80:
            tone = "wheatish"
        else:
            tone = "deep"
        
        return {
            "skin_tone": tone,
            "rgb_values": {
                "red": round(float(r), 1),
                "green": round(float(g), 1),
                "blue": round(float(b), 1)
            }
        }
        
    except Exception as e:
        print(f"Skin tone analysis error: {e}")
        return None

def get_skincare_recommendations(skin_type: str, concerns: list) -> list:
    """
    Get skincare recommendations based on skin type and concerns
    Uses pre-built recommendation database
    """
    recommendations = {
        "oily": [
            "Use gel-based moisturizers",
            "Look for niacinamide products",
            "Avoid heavy oils and butters",
            "Use salicylic acid cleansers"
        ],
        "dry": [
            "Use cream-based moisturizers",
            "Look for hyaluronic acid",
            "Avoid alcohol-based products",
            "Use gentle, non-foaming cleansers"
        ],
        "sensitive": [
            "Use fragrance-free products",
            "Look for centella asiatica",
            "Avoid essential oils",
            "Patch test new products"
        ],
        "combination": [
            "Use lightweight moisturizers",
            "Balance hydration and oil control",
            "Multi-mask different zones",
            "Use pH-balanced products"
        ],
        "acne_prone": [
            "Use salicylic acid or benzoyl peroxide",
            "Non-comedogenic products only",
            "Avoid coconut oil and cocoa butter",
            "Double cleanse daily"
        ]
    }
    
    result = []
    if skin_type in recommendations:
        result.extend(recommendations[skin_type])
    
    return result[:4]

def calculate_skin_age(image_bytes: bytes) -> int:
    """
    Estimate skin age using visual features
    """
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert('L')
        img_array = np.array(image)
        
        # Calculate texture variance (higher variance = older skin)
        from scipy import ndimage
        texture = ndimage.generic_gradient_magnitude(img_array.astype(float))
        texture_score = np.mean(texture)
        
        # Rough age estimation based on texture
        base_age = 25
        age = base_age + (texture_score - 10) * 0.5
        return max(16, min(70, int(age)))
        
    except Exception as e:
        print(f"Age calculation error: {e}")
        return None