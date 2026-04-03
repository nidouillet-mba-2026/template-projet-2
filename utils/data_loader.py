"""
Chargement et preparation des donnees.
Vous pouvez ajouter ici des fonctions utilitaires pour charger les donnees.
"""

import pandas as pd


def charger_donnees(chemin_dvf: str, chemin_annonces: str) -> pd.DataFrame:
    """Charge et concatene les donnees DVF et annonces."""
    dvf = pd.read_csv(chemin_dvf)
    annonces = pd.read_csv(chemin_annonces)
    return pd.concat([dvf, annonces], ignore_index=True)
