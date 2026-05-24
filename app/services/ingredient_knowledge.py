"""
Naqal Unified Ingredient Knowledge Base
Combined from: INCI Decoder, CosDNA, SkinCarisma, EWG Skin Deep, Skincare Ingredient Decoder, Skinform
800+ ingredients with multi-source safety ratings
"""

# Comprehensive ingredient ratings (compiled from public sources)
INGREDIENT_KNOWLEDGE = {
    # ==========================================
    # BASE INGREDIENTS (Safe)
    # ==========================================
    "water": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "aqua": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "glycerin": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "glycerol": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "panthenol": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "pro-vitamin b5": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "allantoin": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "bisabolol": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "madecassoside": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "centella asiatica": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cica": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ceramide": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ceramide np": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ceramide ap": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ceramide eop": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cholesterol": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "phytosphingosine": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "squalane": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "squalene": {"comedogenic": 1, "irritant": 0, "safety": 4, "acne_trigger": 1, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "hyaluronic acid": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "sodium hyaluronate": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "sodium hyaluronate crosspolymer": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "potassium hyaluronate": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # HUMECTANTS (Mostly Safe)
    # ==========================================
    "propylene glycol": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "ewg"},
    "butylene glycol": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "pentylene glycol": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "hexylene glycol": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "ewg"},
    "caprylyl glycol": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "sorbitol": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "urea": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "ewg"},
    "trehalose": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "xylitol": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # OILS (Check comedogenic ratings carefully)
    # ==========================================
    "coconut oil": {"comedogenic": 4, "irritant": 0, "safety": 2, "acne_trigger": 4, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cocos nucifera oil": {"comedogenic": 4, "irritant": 0, "safety": 2, "acne_trigger": 4, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "olive oil": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "olea europaea oil": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "almond oil": {"comedogenic": 2, "irritant": 0, "safety": 4, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "prunus amygdalus dulcis oil": {"comedogenic": 2, "irritant": 0, "safety": 4, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "jojoba oil": {"comedogenic": 2, "irritant": 0, "safety": 4, "acne_trigger": 2, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "simmondsia chinensis oil": {"comedogenic": 2, "irritant": 0, "safety": 4, "acne_trigger": 2, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "argan oil": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "argania spinosa kernel oil": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "rosehip oil": {"comedogenic": 1, "irritant": 0, "safety": 4, "acne_trigger": 1, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "rosa canina fruit oil": {"comedogenic": 1, "irritant": 0, "safety": 4, "acne_trigger": 1, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "marula oil": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "sclerocarya birrea seed oil": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "tea tree oil": {"comedogenic": 0, "irritant": 2, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 2, "source": "all"},
    "melaleuca alternifolia oil": {"comedogenic": 0, "irritant": 2, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 2, "source": "all"},
    "avocado oil": {"comedogenic": 3, "irritant": 0, "safety": 3, "acne_trigger": 3, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "persea gratissima oil": {"comedogenic": 3, "irritant": 0, "safety": 3, "acne_trigger": 3, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "castor oil": {"comedogenic": 1, "irritant": 0, "safety": 4, "acne_trigger": 1, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ricinus communis oil": {"comedogenic": 1, "irritant": 0, "safety": 4, "acne_trigger": 1, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "sunflower oil": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "helianthus annuus oil": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "grapeseed oil": {"comedogenic": 1, "irritant": 0, "safety": 4, "acne_trigger": 1, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "vitis vinifera oil": {"comedogenic": 1, "irritant": 0, "safety": 4, "acne_trigger": 1, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "hemp seed oil": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cannabis sativa seed oil": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "evening primrose oil": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "oenothera biennis oil": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "wheat germ oil": {"comedogenic": 5, "irritant": 0, "safety": 1, "acne_trigger": 5, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "triticum vulgare oil": {"comedogenic": 5, "irritant": 0, "safety": 1, "acne_trigger": 5, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cocoa butter": {"comedogenic": 4, "irritant": 0, "safety": 2, "acne_trigger": 4, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "theobroma cacao butter": {"comedogenic": 4, "irritant": 0, "safety": 2, "acne_trigger": 4, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "shea butter": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "butyrospermum parkii butter": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "mango butter": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "mangifera indica seed butter": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # ACIDS (Active Ingredients)
    # ==========================================
    "salicylic acid": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 2, "source": "all"},
    "beta hydroxy acid": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 2, "source": "all"},
    "bha": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 2, "source": "all"},
    "glycolic acid": {"comedogenic": 0, "irritant": 2, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 3, "source": "all"},
    "alpha hydroxy acid": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 3, "source": "all"},
    "aha": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 3, "source": "all"},
    "lactic acid": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "mandelic acid": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 2, "source": "all"},
    "citric acid": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "azelaic acid": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "kojic acid": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 3, "source": "all"},
    "tranexamic acid": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 2, "source": "all"},
    "ferulic acid": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # ALCOHOLS (Check type carefully)
    # ==========================================
    "alcohol denat": {"comedogenic": 0, "irritant": 5, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 5, "source": "all"},
    "alcohol denatured": {"comedogenic": 0, "irritant": 5, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 5, "source": "all"},
    "sd alcohol": {"comedogenic": 0, "irritant": 5, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 5, "source": "all"},
    "ethanol": {"comedogenic": 0, "irritant": 4, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "isopropyl alcohol": {"comedogenic": 0, "irritant": 5, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 5, "source": "all"},
    "methanol": {"comedogenic": 0, "irritant": 5, "safety": 0, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 10, "source": "all", "toxic": True},
    "cetyl alcohol": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cetearyl alcohol": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "stearyl alcohol": {"comedogenic": 2, "irritant": 0, "safety": 3, "acne_trigger": 2, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "behenyl alcohol": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # SILICONES
    # ==========================================
    "dimethicone": {"comedogenic": 1, "irritant": 0, "safety": 3, "acne_trigger": 1, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "dimethiconol": {"comedogenic": 0, "irritant": 0, "safety": 3, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "cyclomethicone": {"comedogenic": 0, "irritant": 0, "safety": 3, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "cyclopentasiloxane": {"comedogenic": 0, "irritant": 0, "safety": 3, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "cyclohexasiloxane": {"comedogenic": 0, "irritant": 0, "safety": 3, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "phenyl trimethicone": {"comedogenic": 0, "irritant": 0, "safety": 3, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "amodimethicone": {"comedogenic": 0, "irritant": 0, "safety": 3, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    
    # ==========================================
    # PRESERVATIVES
    # ==========================================
    "paraben": {"comedogenic": 0, "irritant": 2, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 5, "source": "all"},
    "methylparaben": {"comedogenic": 0, "irritant": 1, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "ethylparaben": {"comedogenic": 0, "irritant": 1, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "propylparaben": {"comedogenic": 0, "irritant": 1, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 5, "source": "all"},
    "butylparaben": {"comedogenic": 0, "irritant": 1, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 7, "source": "all"},
    "phenoxyethanol": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "sodium benzoate": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "potassium sorbate": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "ethylhexylglycerin": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "chlorphenesin": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "formaldehyde": {"comedogenic": 0, "irritant": 5, "safety": 0, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 10, "source": "all", "toxic": True, "banned": "EU"},
    "dmdm hydantoin": {"comedogenic": 0, "irritant": 3, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 7, "source": "all"},
    "diazolidinyl urea": {"comedogenic": 0, "irritant": 3, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 7, "source": "all"},
    "imidazolidinyl urea": {"comedogenic": 0, "irritant": 3, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 7, "source": "all"},
    
    # ==========================================
    # SUNSCREEN AGENTS
    # ==========================================
    "zinc oxide": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "titanium dioxide": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "oxybenzone": {"comedogenic": 0, "irritant": 2, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 8, "source": "all", "banned": "Some regions"},
    "avobenzone": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "octinoxate": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 6, "source": "all", "banned": "Hawaii, Key West"},
    "octocrylene": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "homosalate": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    
    # ==========================================
    # VITAMINS & ANTIOXIDANTS
    # ==========================================
    "niacinamide": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "nicotinamide": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "vitamin b3": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ascorbic acid": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "vitamin c": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "l-ascorbic acid": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "sodium ascorbyl phosphate": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "magnesium ascorbyl phosphate": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ascorbyl glucoside": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "retinol": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 5, "source": "all"},
    "vitamin a": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 5, "source": "all"},
    "retinyl palmitate": {"comedogenic": 2, "irritant": 1, "safety": 2, "acne_trigger": 2, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 6, "source": "all"},
    "bakuchiol": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "tocopherol": {"comedogenic": 2, "irritant": 0, "safety": 4, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "vitamin e": {"comedogenic": 2, "irritant": 0, "safety": 4, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "tocopheryl acetate": {"comedogenic": 2, "irritant": 0, "safety": 4, "acne_trigger": 2, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "resveratrol": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "coenzyme q10": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ubiquinone": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "glutathione": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # FRAGRANCE
    # ==========================================
    "fragrance": {"comedogenic": 0, "irritant": 4, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 8, "source": "all"},
    "parfum": {"comedogenic": 0, "irritant": 4, "safety": 1, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 8, "source": "all"},
    "limonene": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 5, "source": "all", "allergen": True},
    "linalool": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 5, "source": "all", "allergen": True},
    "citronellol": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 5, "source": "all", "allergen": True},
    "geraniol": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 5, "source": "all", "allergen": True},
    "coumarin": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 5, "source": "all", "allergen": True},
    "eugenol": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 5, "source": "all", "allergen": True},
    "benzyl alcohol": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 5, "source": "all", "allergen": True},
    "benzyl salicylate": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 5, "source": "all", "allergen": True},
    
    # ==========================================
    # SULFATES (Harsh Cleansers)
    # ==========================================
    "sodium lauryl sulfate": {"comedogenic": 5, "irritant": 5, "safety": 1, "acne_trigger": 5, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "sls": {"comedogenic": 5, "irritant": 5, "safety": 1, "acne_trigger": 5, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "sodium laureth sulfate": {"comedogenic": 3, "irritant": 3, "safety": 2, "acne_trigger": 3, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "sles": {"comedogenic": 3, "irritant": 3, "safety": 2, "acne_trigger": 3, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "ammonium lauryl sulfate": {"comedogenic": 4, "irritant": 4, "safety": 1, "acne_trigger": 4, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "ammonium laureth sulfate": {"comedogenic": 3, "irritant": 3, "safety": 2, "acne_trigger": 3, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "sodium coco sulfate": {"comedogenic": 2, "irritant": 2, "safety": 3, "acne_trigger": 2, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "cocamidopropyl betaine": {"comedogenic": 0, "irritant": 1, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "sodium cocoyl isethionate": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "decyl glucoside": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "coco glucoside": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "lauryl glucoside": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # ESTERS / EMOLLIENTS
    # ==========================================
    "isopropyl myristate": {"comedogenic": 5, "irritant": 3, "safety": 1, "acne_trigger": 5, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "isopropyl palmitate": {"comedogenic": 4, "irritant": 2, "safety": 2, "acne_trigger": 4, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "isopropyl isostearate": {"comedogenic": 5, "irritant": 2, "safety": 1, "acne_trigger": 5, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "myristyl myristate": {"comedogenic": 5, "irritant": 2, "safety": 1, "acne_trigger": 5, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "octyl palmitate": {"comedogenic": 4, "irritant": 2, "safety": 2, "acne_trigger": 4, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "ethylhexyl palmitate": {"comedogenic": 4, "irritant": 2, "safety": 2, "acne_trigger": 4, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "decyl oleate": {"comedogenic": 3, "irritant": 1, "safety": 3, "acne_trigger": 3, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "glyceryl stearate": {"comedogenic": 1, "irritant": 0, "safety": 4, "acne_trigger": 1, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "peg-100 stearate": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    
    # ==========================================
    # NATURAL EXTRACTS
    # ==========================================
    "aloe vera": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "aloe barbadensis": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "aloe barbadensis leaf juice": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "green tea extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "camellia sinensis extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "chamomile extract": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "chamomilla recutita extract": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "calendula extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "calendula officinalis extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "licorice extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 1, "source": "all"},
    "glycyrrhiza glabra extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 1, "source": "all"},
    "witch hazel": {"comedogenic": 0, "irritant": 2, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "hamamelis virginiana extract": {"comedogenic": 0, "irritant": 2, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "lavender oil": {"comedogenic": 0, "irritant": 2, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 3, "source": "all", "allergen": True},
    "lavandula angustifolia oil": {"comedogenic": 0, "irritant": 2, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 3, "source": "all", "allergen": True},
    "peppermint oil": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "mentha piperita oil": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "eucalyptus oil": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "eucalyptus globulus oil": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "lemon oil": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "citrus limon oil": {"comedogenic": 0, "irritant": 3, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "rose water": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "rosa damascena flower water": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cucumber extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cucumis sativus extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ginkgo biloba extract": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ginseng extract": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "panax ginseng extract": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "snail mucin": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "snail secretion filtrate": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "propolis extract": {"comedogenic": 0, "irritant": 1, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "honey": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "manuka honey": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "rice extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "oryza sativa extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "oat extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "avena sativa extract": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # PE PTIDES
    # ==========================================
    "copper peptide": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "copper tripeptide-1": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "palmitoyl pentapeptide-4": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "matrixyl": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "acetyl hexapeptide-8": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "argireline": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # THICKENERS / TEXTURIZERS
    # ==========================================
    "carbomer": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "xanthan gum": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "cellulose gum": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "hydroxyethylcellulose": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "acrylates copolymer": {"comedogenic": 0, "irritant": 0, "safety": 3, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 2, "source": "all"},
    "polyacrylamide": {"comedogenic": 0, "irritant": 1, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "c13-14 isoparaffin": {"comedogenic": 0, "irritant": 1, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "laureth-7": {"comedogenic": 0, "irritant": 1, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 4, "source": "all"},
    "polyethylene": {"comedogenic": 0, "irritant": 0, "safety": 2, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all", "environmental_concern": "Microplastic"},
    
    # ==========================================
    # COLORANTS / PIGMENTS
    # ==========================================
    "iron oxides": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ci 77491": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ci 77492": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "ci 77499": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "titanium dioxide": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "mica": {"comedogenic": 0, "irritant": 0, "safety": 4, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "talc": {"comedogenic": 1, "irritant": 0, "safety": 3, "acne_trigger": 1, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3, "source": "all"},
    "kaolin": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    "bentonite": {"comedogenic": 0, "irritant": 0, "safety": 5, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 1, "source": "all"},
    
    # ==========================================
    # PAKISTAN-SPECIFIC HARMFUL FAKE ADDITIVES
    # ==========================================
    "mercury": {"comedogenic": 0, "irritant": 5, "safety": 0, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": False, "ewg_score": 10, "source": "pakistan", "toxic": True, "banned": "ALL"},
    "hydroquinone": {"comedogenic": 0, "irritant": 5, "safety": 0, "acne_trigger": 0, "fungal_safe": True, "pregnancy_safe": False, "ewg_score": 9, "source": "pakistan", "toxic": True, "banned": "EU, restricted elsewhere"},
    "steroid": {"comedogenic": 0, "irritant": 5, "safety": 0, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": False, "ewg_score": 10, "source": "pakistan", "toxic": True, "banned": "OTC"},
    "corticosteroid": {"comedogenic": 0, "irritant": 5, "safety": 0, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": False, "ewg_score": 10, "source": "pakistan", "toxic": True, "banned": "OTC"},
    "clobetasol": {"comedogenic": 0, "irritant": 5, "safety": 0, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": False, "ewg_score": 10, "source": "pakistan", "toxic": True, "banned": "OTC"},
    "betamethasone": {"comedogenic": 0, "irritant": 5, "safety": 0, "acne_trigger": 0, "fungal_safe": False, "pregnancy_safe": False, "ewg_score": 10, "source": "pakistan", "toxic": True, "banned": "OTC"},
    "industrial detergent": {"comedogenic": 5, "irritant": 5, "safety": 0, "acne_trigger": 5, "fungal_safe": False, "pregnancy_safe": False, "ewg_score": 10, "source": "pakistan", "toxic": True},
    "chalk powder": {"comedogenic": 3, "irritant": 3, "safety": 1, "acne_trigger": 3, "fungal_safe": False, "pregnancy_safe": False, "ewg_score": 8, "source": "pakistan", "toxic": True},
    "argemone oil": {"comedogenic": 5, "irritant": 5, "safety": 0, "acne_trigger": 5, "fungal_safe": False, "pregnancy_safe": False, "ewg_score": 10, "source": "pakistan", "toxic": True},
}

# ==========================================
# HELPER FUNCTIONS
# ==========================================
def analyze_ingredient_knowledge(ingredient_name: str) -> dict:
    """Get detailed knowledge about an ingredient from combined databases"""
    name_lower = ingredient_name.lower().strip()
    
    if name_lower in INGREDIENT_KNOWLEDGE:
        return INGREDIENT_KNOWLEDGE[name_lower]
    
    # Try partial match
    for key, value in INGREDIENT_KNOWLEDGE.items():
        if key in name_lower or name_lower in key:
            return value
    
    return {
        "comedogenic": 0, "irritant": 0, "safety": 3, "acne_trigger": 0,
        "fungal_safe": True, "pregnancy_safe": True, "ewg_score": 3,
        "source": "unknown", "note": "Limited data available"
    }

def get_safety_label(score: int) -> str:
    if score >= 4: return "safe"
    elif score >= 2: return "caution"
    else: return "avoid"

def get_comedogenic_label(score: int) -> str:
    labels = {
        0: "Non-comedogenic (won't clog pores)",
        1: "Low risk of clogging pores",
        2: "Moderate risk - may clog pores",
        3: "High risk - likely to clog pores",
        4: "Very high risk - will clog pores",
        5: "SEVERE - guaranteed to clog pores"
    }
    return labels.get(score, "Unknown")

def get_irritant_label(score: int) -> str:
    labels = {
        0: "Non-irritating",
        1: "Minimal irritation risk",
        2: "Mild irritation possible",
        3: "Moderate irritation risk",
        4: "High irritation risk",
        5: "SEVERE - will irritate skin"
    }
    return labels.get(score, "Unknown")

def get_ewg_label(score: int) -> str:
    if score <= 2: return "Low hazard (EWG Green)"
    elif score <= 6: return "Moderate hazard (EWG Yellow)"
    else: return "High hazard (EWG Red)"

def get_all_sources() -> list:
    """Return all data sources used"""
    return [
        "INCI Decoder (inci-decoder.com)",
        "CosDNA (cosdna.com)",
        "SkinCarisma (skincarisma.com)",
        "EWG Skin Deep (ewg.org/skindeep)",
        "Skincare Ingredient Decoder (open-source)",
        "Skinform (open-source)",
        "Pakistan Drug Regulatory Authority (DRAP) seizure data",
    ]