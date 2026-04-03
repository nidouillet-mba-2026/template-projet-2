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

## Données P1

Ce produit est construit sur les annonces collectées collectivement lors du Projet 1.

```bash
# Récupérer les données depuis vos repos P1
git remote add p1-a <url-repo-groupe-A>
git remote add p1-b <url-repo-groupe-B>
```

Nombre d'annonces indexées dans la base RAG : **XXX**

## Prompt Engineering

Voir [`prompts/EXPERIMENTS.md`](prompts/EXPERIMENTS.md) — 3 versions comparées sur le même bien de référence.

## R&D Vision

Voir [`vision/APPROACH.md`](vision/APPROACH.md) — approche retenue, métriques, limites.
