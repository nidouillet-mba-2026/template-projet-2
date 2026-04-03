# Conformite RGPD - NidBot

## 1. Donnees Collectees

| Donnee | Obligatoire | Finalite | Duree conservation |
|--------|-------------|----------|-------------------|
| Ages du couple | Oui | Personnaliser les recommandations | Session uniquement |
| Situation pro | Oui | Evaluer capacite d'emprunt | Session uniquement |
| Budget | Oui | Filtrer les biens | Session uniquement |
| Nom du couple | Non | Personnaliser le rapport PDF | Supprime apres telechargement |
| <!-- AJOUTEZ LES AUTRES DONNEES --> | | | |

## 2. Base Legale

**Base legale choisie :** <!-- Consentement / Interet legitime / Execution contrat -->

**Justification :**
<!-- VOTRE JUSTIFICATION - 3-5 lignes -->

## 3. Droits des Utilisateurs

### Droit d'acces
**Comment l'utilisateur accede a ses donnees ?**
<!-- VOTRE REPONSE -->

### Droit de rectification
**Comment l'utilisateur modifie ses donnees ?**
<!-- VOTRE REPONSE -->

### Droit a l'effacement
**Comment l'utilisateur supprime ses donnees ?**
<!-- VOTRE REPONSE -->

**Implementation technique :**
```python
def supprimer_donnees_utilisateur(session_id):
    # VOTRE CODE
    pass
```

## 4. Securite des Donnees

| Mesure | Implementation |
|--------|---------------|
| Chiffrement | <!-- Oui/Non - Details --> |
| Anonymisation | <!-- Oui/Non - Details --> |
| Acces restreint | <!-- Oui/Non - Details --> |
| Logs d'acces | <!-- Oui/Non - Details --> |

## 5. Bandeau de Consentement

**Texte du bandeau :**
```
<!-- REDIGEZ LE TEXTE DU BANDEAU DE CONSENTEMENT - max 3 lignes -->
```

**Code Streamlit :**
```python
if "consent" not in st.session_state:
    st.warning("<!-- VOTRE TEXTE DE CONSENTEMENT -->")
    col1, col2 = st.columns(2)
    if col1.button("J'accepte"):
        st.session_state.consent = True
        st.rerun()
    if col2.button("Je refuse"):
        st.stop()
```

## 6. Registre des Traitements (simplifie)

| Traitement | Responsable | Destinataires | Transfert hors UE |
|------------|-------------|---------------|-------------------|
| Recommandation de biens | NidDouillet | Utilisateur uniquement | Non |
| Generation rapport | NidDouillet | Utilisateur uniquement | Non |
| <!-- AUTRES --> | | | |
