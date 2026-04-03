# Projet 2 : NidBot - Conseiller IA Immobilier

## Objectif

Construire un assistant conversationnel deploye qui aide les couples a trouver leur bien immobilier ideal a Toulon, avec un moteur de recommandation k-NN from scratch et un pipeline RAG sur des annonces reelles.

## Evaluation automatique

A chaque `git push`, le CI evalue automatiquement votre travail.
Consultez l'onglet **Actions** > dernier workflow > **Job Summary** pour voir votre score.

**Score CI : jusqu'a 55 / 100** — les 45 points restants sont evalues en soutenance.

## Architecture

```
.
├── backend/
│   ├── main.py           <- API FastAPI (endpoints REST) - A COMPLETER
│   ├── recommender.py    <- k-NN from scratch (Grus ch.12) - A COMPLETER
│   ├── rag.py            <- Embeddings + Chroma vector store - A COMPLETER
│   └── pdf_generator.py  <- Generation rapport PDF - A COMPLETER
├── frontend/
│   └── app.py            <- Interface Streamlit ou Gradio - A COMPLETER
├── prompts/
│   ├── system.txt        <- System prompt principal - A COMPLETER
│   ├── recommandation.txt
│   └── EXPERIMENTS.md    <- Journal des 3 versions de prompts - A COMPLETER
├── data/                 <- Donnees immobilieres reelles
├── tests/
│   ├── test_recommender.py <- Vos tests unitaires (>= 3) - A COMPLETER
│   └── test_auto_eval.py   <- Tests d'evaluation (NE PAS MODIFIER)
├── Dockerfile            <- A COMPLETER pour le deploiement
├── requirements.txt      <- A COMPLETER avec vos dependances
└── README.md             <- Ce fichier
```

## Installation

```bash
git clone <votre-url>
cd <votre-repo>
pip install -r requirements.txt
```

## Lancement local

```bash
# Backend
uvicorn backend.main:app --reload

# Frontend (dans un autre terminal)
streamlit run frontend/app.py
```

## Application deployee

**URL :** <!-- REMPLACEZ PAR VOTRE URL DE DEPLOIEMENT (Railway, Render, HF Spaces...) -->

## Workflow GumLoop

<!-- Decrivez ici votre workflow GumLoop avec une capture d'ecran -->

**Cas d'usage :** [alerte nouvelles annonces / rapport hebdo / enrichissement]

## Repartition du travail

| Membre | Role | Contributions principales |
|--------|------|--------------------------|
| Prenom NOM | Backend | ... |
| Prenom NOM | RAG / Embeddings | ... |
| Prenom NOM | AI / Prompts / GumLoop | ... |
| Prenom NOM | Frontend / DevOps | ... |

## Tests

```bash
pytest tests/ -v
```

## References

- Joel Grus, *Data Science From Scratch*, ch.12 (k-NN)
