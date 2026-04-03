#!/usr/bin/env python3
"""Generateur de rapport de notation - Projet 2 : NidBot Conseiller IA."""

import os
import xml.etree.ElementTree as ET

SCORE_MAP = {
    # k-NN from scratch (15 pts)
    "test_distance_function_exists":   (2,  "k-NN from scratch"),
    "test_distance_correct":           (4,  "k-NN from scratch"),
    "test_knn_returns_k_results":      (4,  "k-NN from scratch"),
    "test_no_sklearn_in_recommender":  (5,  "k-NN from scratch"),
    # RAG (15 pts)
    "test_rag_file_exists":                 (5,  "Pipeline RAG"),
    "test_chroma_or_faiss_in_requirements": (5,  "Pipeline RAG"),
    "test_rag_has_search_function":         (5,  "Pipeline RAG"),
    # FastAPI (10 pts)
    "test_main_py_exists":             (3,  "Backend FastAPI"),
    "test_fastapi_in_requirements":    (2,  "Backend FastAPI"),
    "test_required_endpoints_defined": (5,  "Backend FastAPI"),
    # Deploiement (10 pts)
    "test_readme_has_deployed_url":    (6,  "Deploiement"),
    "test_dockerfile_exists":          (4,  "Deploiement"),
    # Prompts (5 pts)
    "test_experiments_md_exists":      (3,  "Prompt Engineering"),
    "test_experiments_has_versions":   (2,  "Prompt Engineering"),
}

SOUTENANCE_ITEMS = [
    ("Choix d'architecture", 15),
    ("Comprehension du k-NN implemente", 10),
    ("Repartition et collaboration", 10),
    ("Demo live", 5),
]


def parse_results(xml_path):
    results = {}
    if not os.path.exists(xml_path):
        return results
    root = ET.parse(xml_path).getroot()
    for tc in root.iter("testcase"):
        name = tc.get("name", "")
        failed = tc.find("failure") is not None or tc.find("error") is not None
        skipped = tc.find("skipped") is not None
        results[name] = "skip" if skipped else ("fail" if failed else "pass")
    return results


def generate_report(results):
    lines = [
        "# Rapport d'Evaluation - Projet 2 : NidBot",
        "",
        "## Score automatique (GitHub CI)",
        "",
    ]

    categories = list(dict.fromkeys(v[1] for v in SCORE_MAP.values()))
    total_earned = total_possible = 0

    for cat in categories:
        lines += [f"### {cat}", "", "| Critere | Points | Resultat |",
                  "|---------|--------|----------|"]
        for test, (pts, c) in SCORE_MAP.items():
            if c != cat:
                continue
            status = results.get(test, "not_run")
            icon = {"pass": "PASS", "fail": "FAIL", "skip": "SKIP"}.get(status, "N/A")
            earned = pts if status == "pass" else 0
            total_earned += earned
            total_possible += pts
            display = test.replace("test_", "").replace("_", " ").title()
            lines.append(f"| {display} | {earned}/{pts} | {icon} |")
        lines.append("")

    lines += [
        "---",
        "",
        "## Soutenance (evalue par l'enseignant)",
        "",
        "| Critere | Points |",
        "|---------|--------|",
    ]
    soutenance_total = 0
    for label, pts in SOUTENANCE_ITEMS:
        lines.append(f"| {label} | ?/{pts} |")
        soutenance_total += pts

    lines += [
        "",
        "---",
        "",
        "## Resume",
        "",
        "| | Score |",
        "|--|-------|",
        f"| **CI automatique** | **{total_earned} / {total_possible}** |",
        f"| Soutenance (enseignant) | ? / {soutenance_total} |",
        f"| **Total** | **/ {total_possible + soutenance_total}** |",
        "",
    ]

    if total_earned == total_possible:
        lines.append("> Tous les tests CI passent.")
    elif total_earned >= total_possible * 0.7:
        lines.append("> Bon travail. Quelques tests en echec a corriger.")
    else:
        lines.append("> Plusieurs tests echouent. Consultez les details ci-dessus.")

    lines += ["", "---", "*Rapport genere automatiquement par le CI.*"]
    return "\n".join(lines)


def main():
    results = parse_results("eval_results.xml")
    report = generate_report(results)
    with open("evaluation_report.md", "w") as f:
        f.write(report)
    print(report)


if __name__ == "__main__":
    main()
