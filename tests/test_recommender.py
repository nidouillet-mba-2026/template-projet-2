"""
Tests unitaires pour le moteur de recommandation.
COMPLETEZ ce fichier avec vos propres tests.

Minimum requis : 5 tests dans ce fichier.
Minimum total (tous fichiers) : 8 tests.
"""

import pytest
import pandas as pd

# Decommenter quand votre classe est implementee :
# from utils.recommender import RecommandeurImmobilier


# @pytest.fixture
# def recommandeur():
#     return RecommandeurImmobilier(
#         "data/dvf_toulon.csv",
#         "data/annonces_actuelles.csv"
#     )


# def test_filtrer_budget(recommandeur):
#     """Verifie que tous les biens filtres sont dans le budget."""
#     biens = recommandeur.filtrer_biens(budget_max=300000)
#     assert all(biens["prix"] <= 300000)


# def test_filtrer_surface(recommandeur):
#     """Verifie le filtre de surface minimum."""
#     biens = recommandeur.filtrer_biens(budget_max=450000, surface_min=60)
#     assert all(biens["surface_m2"] >= 60)


# def test_recommander_top5(recommandeur):
#     """Verifie que recommander retourne exactement 5 biens."""
#     reco = recommandeur.recommander(
#         budget_max=450000, surface_min=50, nb_pieces_min=2, top_n=5
#     )
#     assert len(reco) == 5


# def test_score_entre_0_et_100(recommandeur):
#     """Verifie que les scores sont entre 0 et 100."""
#     reco = recommandeur.recommander(
#         budget_max=450000, surface_min=50, nb_pieces_min=2
#     )
#     for bien in reco:
#         assert 0 <= bien["score"] <= 100


# def test_stats_quartier_complet(recommandeur):
#     """Verifie que stats_quartier retourne toutes les cles."""
#     stats = recommandeur.stats_quartier("Mourillon")
#     cles_requises = [
#         "nom", "nb_biens", "prix_moyen",
#         "prix_m2_moyen", "surface_moyenne", "pct_budget_accessible",
#     ]
#     for cle in cles_requises:
#         assert cle in stats
