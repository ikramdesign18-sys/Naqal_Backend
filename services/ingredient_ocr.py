"""
Naqal Ingredient OCR Service
Extracts ingredients from product label photos
"""

import re

class IngredientOCR:
    """Process and analyze ingredient text from labels"""
    
    # Common ingredient list patterns
    INGREDIENTS_HEADERS = [
        "ingredients", "ingredients:", "inci", "inci:",
        "composition", "contains", "ingrédients",
        "اجزاء", "ingredientes"
    ]
    
    def parse_ingredients_text(self, raw_text: str) -> dict:
        """Parse raw OCR text to extract structured ingredient list"""
        
        if not raw_text:
            return {"error": "No text extracted", "ingredients": [], "full_text": ""}
        
        # Clean text
        text = raw_text.lower().strip()
        
        # Find ingredients section
        ingredients_start = -1
        for header in self.INGREDIENTS_HEADERS:
            idx = text.find(header)
            if idx != -1:
                ingredients_start = idx + len(header)
                break
        
        if ingredients_start == -1:
            # Try to use all text as ingredients
            ingredients_text = text
        else:
            ingredients_text = text[ingredients_start:]
        
        # Clean up
        ingredients_text = ingredients_text.strip().rstrip('.').rstrip(',')
        
        # Split into individual ingredients
        ingredients = self._split_ingredients(ingredients_text)
        
        # Analyze ingredient list quality
        quality_check = self._check_quality(ingredients, raw_text)
        
        return {
            "full_text": raw_text,
            "ingredients_text": ingredients_text,
            "ingredients": ingredients,
            "count": len(ingredients),
            "quality": quality_check
        }
    
    def _split_ingredients(self, text: str) -> list:
        """Split ingredient text into individual ingredients"""
        # Clean common separators
        text = re.sub(r'\s+', ' ', text)
        
        # Split by commas, but not within parentheses
        ingredients = []
        current = ""
        paren_count = 0
        
        for char in text:
            if char == '(':
                paren_count += 1
                current += char
            elif char == ')':
                paren_count -= 1
                current += char
            elif char == ',' and paren_count == 0:
                if current.strip():
                    ingredients.append(current.strip())
                current = ""
            else:
                current += char
        
        if current.strip():
            ingredients.append(current.strip())
        
        # Clean each ingredient
        cleaned = []
        for ing in ingredients:
            ing = ing.strip().strip('*').strip('-').strip()
            if len(ing) > 2:  # Skip single characters
                cleaned.append(ing)
        
        return cleaned
    
    def _check_quality(self, ingredients: list, raw_text: str) -> dict:
        """Check quality of extracted ingredients"""
        quality_score = 0
        issues = []
        
        if len(ingredients) == 0:
            issues.append("No ingredients found")
        elif len(ingredients) < 3:
            issues.append("Very few ingredients found - possibly incomplete")
            quality_score = 30
        elif len(ingredients) < 10:
            quality_score = 70
            issues.append("Limited ingredient list")
        else:
            quality_score = 100
        
        # Check for garbage text
        garbage_ratio = sum(1 for i in ingredients if len(i) < 2 or i.isdigit()) / max(len(ingredients), 1)
        if garbage_ratio > 0.3:
            issues.append("High amount of unrecognized text - try better lighting")
            quality_score = max(0, quality_score - 40)
        
        return {
            "score": quality_score,
            "reliable": quality_score >= 60,
            "issues": issues
        }