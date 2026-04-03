# NidBuyer — Votre acheteur IA à Toulon

> **Projet 2 — MBA Data & IA 2026**

## Équipe

### Pôle Produit

| Membre | Rôle |
|--------|------|
| Prénom NOM | Lead architecture |
| Prénom NOM | Backend / RAG |
| Prénom NOM | Frontend / UX |
| Prénom NOM | Données / DVF + scoring |
| Prénom NOM | Prompt engineering |

### Pôle R&D Vision

| Membre | Rôle |
|--------|------|
| Prénom NOM | Approche & dataset |
| Prénom NOM | Entraînement / évaluation |

## Demo

URL déployée : **https://TODO**

## Lancer en local

```bash
cp .env.example .env
# Remplir ANTHROPIC_API_KEY dans .env

pip install -r requirements.txt

# Backend
uvicorn backend.main:app --reload

# Frontend (autre terminal)
streamlit run frontend/app.py
```

## Architecture

```
nidbuyer/
├── backend/         # FastAPI — endpoints REST
├── frontend/        # Streamlit — interface acheteur
├── vision/          # R&D : estimation état du bien par les photos
│   ├── model.py     # Interface commune (appelée par scoring.py)
│   ├── cnn/         # Piste CNN
│   ├── llm/         # Piste LLM multimodal
│   ├── APPROACH.md  # Choix justifié + résultats mesurés
│   └── benchmark.py # Script de comparaison
├── prompts/         # System prompts + EXPERIMENTS.md
├── data/            # Annonces + DVF 2024-2026
└── tests/           # Tests scoring, RAG, vision
```

## Tâche J1 — Consolidation des données P1

Votre base RAG repose sur les annonces collectées en P1. **Avant la fin du premier jour :**

```bash
# 1. Copiez les CSV d'annonces de vos deux groupes P1 dans data/

# 2. Fusionnez et dédupliquez
python - <<'EOF'
import pandas as pd
a = pd.read_csv("data/annonces_groupe_a.csv")
b = pd.read_csv("data/annonces_groupe_b.csv")
merged = pd.concat([a, b]).drop_duplicates(subset=["url_source"])
merged.to_csv("data/annonces.csv", index=False)
print(f"{len(merged)} annonces consolidées")
EOF

# 3. Mettez à jour ce README avec le nombre réel ci-dessous
```

> Moins de 300 annonces après fusion ? Scraper de nouvelles annonces est votre priorité immédiate.

Nombre d'annonces indexées dans la base RAG : **XXX** ← *à mettre à jour J1*

## Prompt Engineering

Voir [`prompts/EXPERIMENTS.md`](prompts/EXPERIMENTS.md) — 3 versions comparées sur le même bien de référence.

## R&D Vision

Voir [`vision/APPROACH.md`](vision/APPROACH.md) — approche retenue, métriques, limites.
