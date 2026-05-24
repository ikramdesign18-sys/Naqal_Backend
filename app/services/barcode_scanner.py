"""
Naqal Barcode Scanner Service
Handles barcode validation and lookup
"""

import re

class BarcodeScanner:
    """Barcode validation and processing for Pakistani products"""
    
    # Valid barcode prefixes for common Pakistani product types
    PAKISTAN_BARCODE_PREFIXES = {
        "890": "India",
        "899": "Pakistan/Indonesia", 
        "490": "Japan (P&G products)",
        "400": "Germany (Nivea, etc)",
        "360": "France (L'Oréal, Garnier)",
        "357": "USA (Johnson's, Neutrogena)",
        "869": "Turkey",
        "800": "Italy",
    }
    
    def validate_barcode(self, barcode: str) -> dict:
        """Validate and identify barcode"""
        barcode = re.sub(r'[^0-9]', '', barcode)
        
        if len(barcode) not in [8, 12, 13, 14]:
            return {
                "valid": False,
                "error": f"Invalid barcode length: {len(barcode)} digits"
            }
        
        prefix = barcode[:3]
        country = self.PAKISTAN_BARCODE_PREFIXES.get(prefix, "Unknown")
        
        return {
            "valid": True,
            "barcode": barcode,
            "prefix": prefix,
            "country": country,
            "type": "EAN-13" if len(barcode) == 13 else f"UPC/EAN-{len(barcode)}"
        }
    
    def detect_fake_barcode_issues(self, barcode: str, expected_prefixes: list) -> list:
        """Check barcode against expected prefixes for a brand"""
        issues = []
        
        barcode = re.sub(r'[^0-9]', '', barcode)
        prefix = barcode[:3]
        
        if prefix not in expected_prefixes:
            issues.append({
                "severity": "high",
                "issue": f"Barcode prefix {prefix} doesn't match brand's expected prefix {expected_prefixes}",
                "detail": "Counterfeit products often have incorrect barcode prefixes"
            })
        
        # Check for common fake barcode patterns
        if barcode.count('0') > 8:
            issues.append({
                "severity": "medium",
                "issue": "Suspicious barcode pattern (too many zeros)",
                "detail": "Counterfeits sometimes use placeholder barcodes"
            })
        
        return issues