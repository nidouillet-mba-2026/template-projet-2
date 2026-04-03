from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="NidBuyer API", version="0.1.0")


# --- Modèles ---

class ProfilAcheteur(BaseModel):
    intention: str          # "rp" | "rs" | "investissement" | "mixte"
    budget_max: float
    surface_min: float | None = None
    quartiers: list[str] = []
    nb_pieces_min: int | None = None
    description_libre: str = ""

class AlerteProfil(BaseModel):
    email: str
    profil: ProfilAcheteur


# --- Endpoints ---

@app.get("/biens")
def liste_biens(budget_max: float | None = None, surface_min: float | None = None, quartier: str | None = None):
    """Liste filtrée des biens disponibles."""
    # TODO : requêter la base de données / ChromaDB
    raise HTTPException(status_code=501, detail="Non implémenté")


@app.get("/biens/{bien_id}")
def detail_bien(bien_id: str):
    """Détail d'un bien + fiche décision LLM."""
    # TODO : récupérer le bien et appeler fiche_decision()
    raise HTTPException(status_code=501, detail="Non implémenté")


@app.post("/rechercher")
def rechercher(profil: ProfilAcheteur):
    """Profil acheteur → top 5 biens avec scores et fiches décision."""
    # TODO : appeler rag.search_similar() puis scoring.score_opportunite()
    raise HTTPException(status_code=501, detail="Non implémenté")


@app.post("/chat")
def chat(question: str, profil: ProfilAcheteur | None = None):
    """Question libre → réponse LLM argumentée."""
    # TODO : construire le contexte RAG + appeler l'API Anthropic
    raise HTTPException(status_code=501, detail="Non implémenté")


@app.post("/alerte")
def creer_alerte(alerte: AlerteProfil):
    """Sauvegarder un profil pour recevoir des alertes sur nouveaux biens."""
    # TODO : persister le profil (fichier JSON ou DB légère)
    raise HTTPException(status_code=501, detail="Non implémenté")


@app.get("/marche/quartiers")
def marche_quartiers():
    """Médiane DVF 2024-2026 par quartier de Toulon."""
    # TODO : lire les données DVF filtrées et agréger par quartier
    raise HTTPException(status_code=501, detail="Non implémenté")
