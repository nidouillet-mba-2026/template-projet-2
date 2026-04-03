"""
Moteur de recommandation immobiliere pour NidBot.
COMPLETEZ les methodes de la classe RecommandeurImmobilier.
"""

import pandas as pd
from typing import List, Dict, Optional


class RecommandeurImmobilier:
    def __init__(self, chemin_dvf: str, chemin_annonces: str):
        """Charge les donnees immobilieres."""
        self.dvf = pd.read_csv(chemin_dvf)
        self.annonces = pd.read_csv(chemin_annonces)
        self.tous_biens = pd.concat([self.dvf, self.annonces], ignore_index=True)

    def filtrer_biens(
        self,
        budget_max: int,
        surface_min: float = 0,
        nb_pieces_min: int = 1,
        type_bien: Optional[str] = None,
        quartiers: Optional[List[str]] = None,
    ) -> pd.DataFrame:
        """
        Filtre les biens selon les criteres du couple.
        Retourne un DataFrame des biens correspondants.
        """
        # VOTRE CODE ICI
        pass

    def calculer_score_bien(self, bien: pd.Series, stats_quartier: Dict) -> float:
        """
        Calcule un score sur 100 pour un bien.

        Criteres et poids :
        - Prix vs moyenne quartier (30%) : bien moins cher = meilleur score
        - Surface vs moyenne (25%) : bien plus grand = meilleur score
        - DPE (20%) : A=100, B=80, C=60, D=40, E=20, F=10, G=0
        - Extras (25%) : +10 par extra (balcon, parking, etc.)
        """
        # VOTRE CODE ICI
        pass

    def recommander(
        self,
        budget_max: int,
        surface_min: float,
        nb_pieces_min: int,
        type_bien: Optional[str] = None,
        quartiers: Optional[List[str]] = None,
        top_n: int = 5,
    ) -> List[Dict]:
        """
        Retourne les top_n meilleurs biens avec leur score.

        Format de sortie :
        [
            {
                "id": 123,
                "prix": 320000,
                "surface_m2": 75,
                "quartier": "Mourillon",
                "score": 85.5,
                "raison": "15% moins cher que la moyenne du quartier"
            },
            ...
        ]
        """
        # VOTRE CODE ICI
        pass

    def stats_quartier(self, quartier: str) -> Dict:
        """
        Retourne les statistiques d'un quartier.

        Format :
        {
            "nom": "Mourillon",
            "nb_biens": 45,
            "prix_moyen": 285000,
            "prix_m2_moyen": 3800,
            "surface_moyenne": 72,
            "pct_budget_accessible": 78.5
        }
        """
        # VOTRE CODE ICI
        pass
