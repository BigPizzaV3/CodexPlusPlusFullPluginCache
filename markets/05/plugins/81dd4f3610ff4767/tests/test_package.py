import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = {"amorcer-continuum","lire-protocole","charger-contexte-continuum","executer-demande","tenir-verbatim"}
COMPATIBILITY_COORDINATORS = {"capitaliser","choisir-capacites","comprehension-architecturale","converger","corriger-et-reprendre","explorer-peut-etre","livrer","orchestrer-missions","passation","prelever-verbatim","produire-commandes","prouver-resultat","retrouver-savoir"}
REQUIRED_SPECIALISTS = {
    "appliquer-exigences-axel","appliquer-contexte-projet","maintenir-specificite-continuum","executer-powershell","traiter-retour-technique","apprendre-du-reel","choisir-livraison","questionner-totalement","construire-plan","resoudre-autorite","qualifier-preuve","appliquer-cout-zero","respecter-typographie","rechercher-trianguler","prevol-capacites","gerer-decisions","proteger-concurrence","gerer-transactions","gerer-reprise","tracer-execution","verifier-acceptation","gerer-livrables","resoudre-demeures","gerer-canonicalite","synchroniser-miroir","gerer-savoir","integrer-savoir","tenir-continuite","tenir-histoire","executer-pre-passation","executer-passation","reprendre-passation","qualifier-magister","preparer-mission-magister","clore-mission-magister","appeler-passerelle","realigner-plugin","auditer-alignement","decouvrir-skills","qualifier-skill-externe","evaluer-skill","diagnostiquer-maillage","concevoir-skill","revoir-exigences","reproduire-bug","cartographier-code","choisir-strategie-tests","revoir-production","gerer-git","auditer-securite-agentique","choisir-topologie-delegation","verifier-document-rendu","traiter-tableur","tester-webapp",
    "auditer-fraicheur-contexte","verifier-isolation-contextes","auditer-fraicheur-savoir","verifier-contrat-public","observer-systeme","gerer-quotas-et-pression","verifier-accessibilite","etudier-marche","scorer-opportunites","gerer-workflow-durable","red-teamer-agent","piloter-android","gerer-environnement-azer","qualifier-raccordabilite-noyau"
}
FORBIDDEN = [r"100\s+règles", r"14\s+Skills", r"141\s+Skills", r"6a8d227992c48191aedcde4d1001f0d9", r"Ne pas recommencer l.amorçage à chaque tour du même tchat", r"cette lecture est répétée à chaque tour", r"every Axel turn requiring a visible answer from Azer"]

class PackageContractTests(unittest.TestCase):
    def setUp(self):
        self.skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}

    def test_mesh_is_not_artificially_capped(self):
        self.assertTrue(CORE.issubset(self.skills))
        self.assertTrue(REQUIRED_SPECIALISTS.issubset(self.skills))
        self.assertTrue(COMPATIBILITY_COORDINATORS.issubset(self.skills))
        self.assertGreaterEqual(len(self.skills), 154)

    def test_skill_frontmatter_identity_matches_folder(self):
        for name in self.skills:
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith(f"---\nname: {name}\n"), name)
            self.assertRegex(text, r"(?m)^description: Use\b", name)
            self.assertRegex(text, r"(?m)^# ", name)

    def test_no_legacy_architecture(self):
        chunks = [(ROOT / "README.md").read_text(encoding="utf-8"),(ROOT / "coverage.json").read_text(encoding="utf-8"),(ROOT / "skill_graph.json").read_text(encoding="utf-8"),(ROOT / "continuum_sources.json").read_text(encoding="utf-8")]
        chunks += [p.read_text(encoding="utf-8") for p in (ROOT / "skills").glob("*/SKILL.md")]
        text = "\n".join(chunks)
        for pattern in FORBIDDEN:
            self.assertIsNone(re.search(pattern, text, re.I), pattern)

    def test_coverage_has_twelve_files_and_responsibilities(self):
        data = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
        files = data["canonical_protocol"]["files"]
        self.assertEqual([f"{i:02d}" for i in range(1,13)], [f["id"] for f in files])
        for entry in files:
            self.assertTrue(entry["responsibilities"])
            for owners in entry["responsibilities"].values():
                self.assertTrue(owners)
                self.assertTrue(set(owners).issubset(self.skills))

    def test_graph_and_source_model_reference_existing_skills(self):
        graph = json.loads((ROOT / "skill_graph.json").read_text(encoding="utf-8"))
        for edge in graph["edges"]:
            self.assertEqual(2, len(edge))
            self.assertTrue(set(edge).issubset(self.skills), edge)
        for members in graph["layers"].values():
            self.assertTrue(set(members).issubset(self.skills))
        sources = json.loads((ROOT / "continuum_sources.json").read_text(encoding="utf-8"))
        for layer in sources["layers"]:
            self.assertIn(layer["resolver"], self.skills, layer)

if __name__ == "__main__":
    unittest.main()
