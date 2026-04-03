"""
Moteur de recommandation k-NN from scratch.
Reference : Joel Grus, "Data Science From Scratch", chapitre 12.

IMPORTANT : N'importez pas sklearn. Implementez les fonctions vous-memes.
"""

import math


def normalize(xs: list[float]) -> list[float]:
    """
    Normalise une liste de valeurs entre 0 et 1.
    Retourne la liste inchangee si min == max.
    """
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez normalize()")


def distance(v1: list[float], v2: list[float]) -> float:
    """
    Distance euclidienne entre deux vecteurs de meme longueur.
    Exemple : distance([0, 0], [3, 4]) == 5.0
    """
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez distance() - voir Grus ch.12")


def property_to_vector(prop: dict, weights: dict) -> list[float]:
    """
    Convertit un bien en vecteur de features normalise.
    weights : poids de chaque dimension (ex: {"prix": 1.0, "surface": 0.8})
    """
    # VOTRE CODE ICI
    # Dimensions suggerees : prix, surface, score_dpe, extras, score_quartier
    raise NotImplementedError("Implementez property_to_vector()")


def knn_recommend(
    k: int,
    properties: list[dict],
    profile: dict,
    weights: dict,
) -> list[dict]:
    """
    Retourne les k biens les plus proches du profil du couple.

    Etapes :
    1. Convertir chaque bien et le profil en vecteur
    2. Calculer la distance entre le profil et chaque bien
    3. Trier par distance croissante
    4. Retourner les k premiers

    Parametre properties : liste de dicts avec au moins les cles
        {id, prix, surface, score_dpe, extras, score_quartier}
    Parametre profile : meme structure que les biens
    """
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez knn_recommend() - voir Grus ch.12")
