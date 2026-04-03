"""
Tests supplementaires pour l'application.
COMPLETEZ ce fichier avec vos propres tests.

Ajoutez au moins 3 tests ici pour atteindre le minimum de 8 tests au total.
"""

import pytest

# Exemples de tests a implementer :

# def test_filtrage_budget_450k():
#     """Cas reel : couple avec budget 450k trouve des biens."""
#     from utils.recommender import RecommandeurImmobilier
#     recommandeur = RecommandeurImmobilier(
#         "data/dvf_toulon.csv", "data/annonces_actuelles.csv"
#     )
#     biens = recommandeur.filtrer_biens(
#         budget_max=450000, surface_min=60, nb_pieces_min=3
#     )
#     assert len(biens) > 0, "Aucun bien trouve pour un couple avec 450k"


# def test_cas_limite_budget_faible():
#     """Cas limite : budget tres faible."""
#     from utils.recommender import RecommandeurImmobilier
#     recommandeur = RecommandeurImmobilier(
#         "data/dvf_toulon.csv", "data/annonces_actuelles.csv"
#     )
#     biens = recommandeur.filtrer_biens(budget_max=50000)
#     assert isinstance(biens, pd.DataFrame)


# def test_quartier_inexistant():
#     """Cas erreur : quartier qui n'existe pas."""
#     from utils.recommender import RecommandeurImmobilier
#     recommandeur = RecommandeurImmobilier(
#         "data/dvf_toulon.csv", "data/annonces_actuelles.csv"
#     )
#     stats = recommandeur.stats_quartier("QuartierInexistant")
#     assert stats is None or stats.get("nb_biens", 0) == 0
