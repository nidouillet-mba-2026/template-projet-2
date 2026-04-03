"""
Generateur de rapports PDF personnalises.
COMPLETEZ la fonction generer_rapport().
"""

from fpdf import FPDF


def generer_rapport(
    nom_couple: str,
    budget: int,
    criteres: dict,
    recommandations: list,
) -> str:
    """
    Genere un PDF personnalise pour le couple.

    Args:
        nom_couple: Nom du couple (ex: "Martin-Dupont")
        budget: Budget maximum en euros
        criteres: Dict avec surface_min, nb_pieces, quartiers, etc.
        recommandations: Liste de biens recommandes

    Returns:
        Chemin du fichier PDF genere.
    """
    pdf = FPDF()
    pdf.add_page()

    # En-tete
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Rapport Immobilier - {nom_couple}", ln=True, align="C")

    # Budget
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Budget : {budget:,} EUR", ln=True)

    # VOTRE CODE ICI : criteres, recommandations, graphiques...

    output_path = f"rapport_{nom_couple.replace(' ', '_')}.pdf"
    pdf.output(output_path)
    return output_path
