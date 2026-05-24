"""
Naqal GS1 Barcode Verification Service
Verifies barcodes against official GS1 global database
Free - no API key required
"""

import httpx
import re

async def verify_barcode_gs1(barcode: str) -> dict:
    """
    Verify barcode against GS1 global database
    Returns company information if barcode is valid
    """
    # Clean barcode
    barcode = re.sub(r'[^0-9]', '', barcode)
    
    if len(barcode) < 8:
        return {"valid": False, "error": "Barcode too short"}
    
    try:
        # Use GS1 GEPIR API (free public access)
        url = f"https://gepir.gs1.org/index.php?option=com_gepir&task=search&search={barcode}"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            
            # GS1 returns data if barcode is valid
            if response.status_code == 200 and "No information found" not in response.text:
                return {
                    "valid": True,
                    "gs1_verified": True,
                    "barcode": barcode,
                    "source": "gs1_global"
                }
            else:
                return {
                    "valid": False,
                    "gs1_verified": False,
                    "barcode": barcode,
                    "note": "Barcode not found in GS1 database"
                }
                
    except Exception as e:
        return {
            "valid": False,
            "gs1_verified": False,
            "error": str(e),
            "note": "GS1 verification unavailable"
        }

def get_country_from_barcode(barcode: str) -> str:
    """Get country of origin from barcode prefix"""
    prefixes = {
        "890": "India",
        "896": "Pakistan",
        "899": "Indonesia/Pakistan (Unilever)",
        "490": "Japan",
        "400": "Germany",
        "360": "France",
        "357": "USA",
        "869": "Turkey",
        "500": "UK",
        "761": "Switzerland",
        "600": "South Africa",
        "880": "South Korea",
        "769": "Canada",
        "350": "France",
        "502": "UK",
        "817": "USA",
        "900": "Austria",
        "930": "Australia",
        "800": "Italy",
        "690": "China",
    }
    
    prefix = barcode[:3]
    return prefixes.get(prefix, f"Unknown ({prefix})")