"""
Evaluation automatique - Projet 2 : NidBot Conseiller IA
=========================================================
Ce fichier est execute par le CI a chaque push.
NE MODIFIEZ PAS ce fichier.

Bareme automatise : 55 points / 100
Les 45 points restants sont evalues en soutenance.
"""

import os
import re
import sys

import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ===========================================================================
# K-NN FROM SCRATCH (15 pts)
# ===========================================================================
class TestKNNScratch:
    """Moteur de recommandation k-NN from scratch - Grus ch.12 (15 pts)."""

    @pytest.fixture
    def rec(self):
        sys.path.insert(0, PROJECT_ROOT)
        try:
            import backend.recommender as m
            return m
        except ImportError:
            pytest.fail(
                "backend/recommender.py introuvable ou non importable. "
                "Creez ce fichier avec distance() et knn_recommend()."
            )
        finally:
            sys.path.pop(0)

    def test_distance_function_exists(self, rec):
        """[2 pts] Fonction distance() definie dans backend/recommender.py."""
        assert hasattr(rec, "distance"), (
            "Fonction distance() introuvable dans backend/recommender.py."
        )

    def test_distance_correct(self, rec):
        """[4 pts] distance() calcule la distance euclidienne correctement."""
        # distance([0,0], [3,4]) = 5
        result = rec.distance([0.0, 0.0], [3.0, 4.0])
        assert abs(result - 5.0) < 0.01, f"Distance attendue 5.0, obtenue {result}"

    def test_knn_returns_k_results(self, rec):
        """[4 pts] knn_recommend() retourne exactement k resultats."""
        properties = [
            {"id": i, "prix": 200000 + i * 10000, "surface": 50 + i,
             "score_dpe": 0.6, "extras": 0.5, "score_quartier": 0.7}
            for i in range(10)
        ]
        profile = {"prix": 300000, "surface": 65, "score_dpe": 0.6,
                   "extras": 0.5, "score_quartier": 0.7}
        results = rec.knn_recommend(k=3, properties=properties, profile=profile,
                                    weights={"prix": 1, "surface": 1})
        assert len(results) == 3, (
            f"knn_recommend(k=3) doit retourner 3 resultats, retourne {len(results)}."
        )

    def test_no_sklearn_in_recommender(self, rec):
        """[5 pts] backend/recommender.py n'importe pas sklearn."""
        path = os.path.join(PROJECT_ROOT, "backend", "recommender.py")
        if not os.path.exists(path):
            pytest.skip("backend/recommender.py absent")
        with open(path) as f:
            source = f.read()
        assert "sklearn" not in source, (
            "backend/recommender.py importe sklearn. "
            "Implementez le k-NN from scratch (voir Grus ch.12)."
        )


# ===========================================================================
# PIPELINE RAG (15 pts)
# ===========================================================================
class TestRAG:
    """Pipeline RAG avec embeddings et vector store (15 pts)."""

    def test_rag_file_exists(self):
        """[5 pts] backend/rag.py present."""
        path = os.path.join(PROJECT_ROOT, "backend", "rag.py")
        assert os.path.exists(path), (
            "backend/rag.py introuvable. "
            "Creez ce fichier avec votre pipeline d'embeddings et Chroma."
        )

    def test_chroma_or_faiss_in_requirements(self):
        """[5 pts] requirements.txt inclut chromadb ou faiss."""
        req = os.path.join(PROJECT_ROOT, "requirements.txt")
        assert os.path.exists(req), "requirements.txt introuvable."
        with open(req) as f:
            content = f.read().lower()
        assert "chromadb" in content or "faiss" in content, (
            "requirements.txt doit inclure chromadb ou faiss-cpu "
            "pour le pipeline RAG."
        )

    def test_rag_has_search_function(self):
        """[5 pts] backend/rag.py definit une fonction de recherche semantique."""
        path = os.path.join(PROJECT_ROOT, "backend", "rag.py")
        if not os.path.exists(path):
            pytest.skip("backend/rag.py absent")
        with open(path) as f:
            source = f.read()
        has_search = (
            "def search" in source
            or "def query" in source
            or "def recherche" in source
            or ".query(" in source
        )
        assert has_search, (
            "backend/rag.py doit definir une fonction de recherche semantique "
            "(ex: search_similar(), query_properties())."
        )


# ===========================================================================
# BACKEND FASTAPI (10 pts)
# ===========================================================================
class TestAPI:
    """Backend FastAPI avec endpoints documentes (10 pts)."""

    def test_main_py_exists(self):
        """[3 pts] backend/main.py present."""
        path = os.path.join(PROJECT_ROOT, "backend", "main.py")
        assert os.path.exists(path), (
            "backend/main.py introuvable. "
            "Creez votre application FastAPI dans ce fichier."
        )

    def test_fastapi_in_requirements(self):
        """[2 pts] requirements.txt inclut fastapi."""
        req = os.path.join(PROJECT_ROOT, "requirements.txt")
        if not os.path.exists(req):
            pytest.skip("requirements.txt absent")
        with open(req) as f:
            content = f.read().lower()
        assert "fastapi" in content, (
            "requirements.txt doit inclure fastapi."
        )

    def test_required_endpoints_defined(self):
        """[5 pts] Les endpoints principaux sont definis dans backend/main.py."""
        path = os.path.join(PROJECT_ROOT, "backend", "main.py")
        if not os.path.exists(path):
            pytest.skip("backend/main.py absent")
        with open(path) as f:
            source = f.read()
        required = [
            ("/biens", "GET /biens"),
            ("/recommander", "POST /recommander"),
            ("/chat", "POST /chat ou GET /chat"),
        ]
        missing = [label for route, label in required if route not in source]
        assert not missing, (
            f"Endpoints manquants dans backend/main.py : {missing}. "
            "Consultez l'enonce pour la liste des endpoints attendus."
        )


# ===========================================================================
# DEPLOIEMENT (10 pts)
# ===========================================================================
class TestDeploiement:
    """Application deployee et accessible (10 pts)."""

    def test_readme_has_deployed_url(self):
        """[6 pts] README contient une URL de deploiement public."""
        readme = os.path.join(PROJECT_ROOT, "README.md")
        assert os.path.exists(readme), "README.md introuvable."
        with open(readme) as f:
            content = f.read()
        patterns = [
            r"https://[a-zA-Z0-9\-]+\.railway\.app",
            r"https://[a-zA-Z0-9\-]+\.onrender\.com",
            r"https://[a-zA-Z0-9\-]+\.fly\.dev",
            r"https://[a-zA-Z0-9\-]+\.streamlit\.app",
            r"https://huggingface\.co/spaces/",
        ]
        assert any(re.search(p, content) for p in patterns), (
            "README.md ne contient pas d'URL de deploiement. "
            "Deployez votre app et ajoutez le lien dans le README."
        )

    def test_dockerfile_exists(self):
        """[4 pts] Dockerfile present pour le deploiement."""
        path = os.path.join(PROJECT_ROOT, "Dockerfile")
        assert os.path.exists(path), (
            "Dockerfile introuvable. "
            "Creez un Dockerfile pour containeriser et deployer votre app."
        )


# ===========================================================================
# PROMPT ENGINEERING (5 pts)
# ===========================================================================
class TestPrompts:
    """Documentation du prompt engineering (5 pts)."""

    def test_experiments_md_exists(self):
        """[3 pts] prompts/EXPERIMENTS.md present."""
        path = os.path.join(PROJECT_ROOT, "prompts", "EXPERIMENTS.md")
        assert os.path.exists(path), (
            "prompts/EXPERIMENTS.md introuvable. "
            "Documentez vos 3 versions de prompts dans ce fichier."
        )

    def test_experiments_has_versions(self):
        """[2 pts] EXPERIMENTS.md documente au moins 3 versions de prompts."""
        path = os.path.join(PROJECT_ROOT, "prompts", "EXPERIMENTS.md")
        if not os.path.exists(path):
            pytest.skip("EXPERIMENTS.md absent")
        with open(path) as f:
            content = f.read()
        versions = re.findall(r"V[123]|version\s+[123]|##\s+[Vv]\d", content, re.IGNORECASE)
        assert len(versions) >= 3, (
            f"Seulement {len(versions)} version(s) documentee(s) dans EXPERIMENTS.md. "
            "Documentez 3 versions de votre system prompt."
        )
