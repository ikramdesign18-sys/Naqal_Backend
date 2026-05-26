"""
Naqal Groq AI Service
Uses Groq LLaMA 3 for face analysis and product explanations
"""

import os
import random
import json
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEYS = os.getenv("GROQ_API_KEYS", "").split(",")
GROQ_API_KEYS = [k.strip() for k in GROQ_API_KEYS if k.strip()]

if not GROQ_API_KEYS:
    print("⚠️ No Groq API keys found in .env")
else:
    print(f"✅ Loaded {len(GROQ_API_KEYS)} Groq API keys")

response_cache = {}

def get_client():
    from groq import Groq
    key = random.choice(GROQ_API_KEYS)
    return Groq(api_key=key)

def explain_product_safety(ingredients: str, skin_type: str) -> str:
    if not GROQ_API_KEYS:
        return None
    try:
        from groq import Groq
        client = get_client()
        prompt = f"Explain if this product is safe for {skin_type} skin. Ingredients: {ingredients}. Reply in 2-3 simple sentences."
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5, max_tokens=200,
        )
        result = response.choices[0].message.content
        if result and len(result) > 5:
            return result
        return None
    except Exception as e:
        return None

def analyze_fake_risk(product_name: str, price: float, barcode: str, indicators: list) -> str:
    if not GROQ_API_KEYS:
        return None
    try:
        from groq import Groq
        client = get_client()
        prompt = f"Product: {product_name}, Price: {price} PKR, Signs: {indicators}. Is this likely fake? Reply in 1-2 sentences."
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3, max_tokens=150,
        )
        result = response.choices[0].message.content
        if result and len(result) > 5:
            return result
        return None
    except Exception as e:
        return None

def analyze_face_with_ai(image_description: str, user_skin_profile: dict = None) -> dict:
    if not GROQ_API_KEYS:
        return None
    cache_key = str(image_description)[:100]
    if cache_key in response_cache:
        return response_cache[cache_key]
    try:
        from groq import Groq
        client = get_client()
        prompt = f'Analyze this face: {image_description}. Return JSON: {{"acne_score":50,"redness_score":50,"dark_circles_score":50,"texture_score":50,"hydration_score":50,"sensitivity_score":50,"estimated_age":30,"overall_health":60,"summary":"ok"}}. Return ONLY valid JSON, no other text.'
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3, max_tokens=300,
        )
        raw = response.choices[0].message.content
        if raw:
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.split("\n")[1]
            result = json.loads(raw)
            if isinstance(result, dict) and "acne_score" in result:
                response_cache[cache_key] = result
                return result
        return None
    except Exception as e:
        return None
