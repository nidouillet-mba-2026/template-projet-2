"""
Configuration du projet NidBot.
Modifiez les valeurs selon vos besoins.
"""

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ---------------------------------------------------------------------------
# Parametres metier
# ---------------------------------------------------------------------------
BUDGET_MAX_DEFAULT = 450000
ZONE_CODES_POSTAUX = ["83000", "83100", "83200"]
QUARTIERS_TOULON = [
    "Mourillon", "Centre-ville", "Pont-du-Las", "La Rode",
    "Saint-Jean-du-Var", "Le Lavandou", "Cap Brun", "Aguillon",
]

# ---------------------------------------------------------------------------
# API (optionnel - peut utiliser un mock si pas de cle)
# ---------------------------------------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "mock")
USE_MOCK_LLM = OPENAI_API_KEY == "mock"
