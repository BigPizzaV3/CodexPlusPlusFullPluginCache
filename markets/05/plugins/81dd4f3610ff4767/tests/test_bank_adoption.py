import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ADOPTED = {
    "decouvrir-skills","qualifier-skill-externe","evaluer-skill","diagnostiquer-maillage","concevoir-skill","modeliser-domaine","verifier-affirmation-source","conduire-revue-systematique","revoir-exigences","extraire-actions-document","reproduire-bug","boucler-diagnostic","cartographier-code","auditer-architecture","auditer-dette-technique","choisir-strategie-tests","tester-invariants","fiabiliser-tests","mesurer-performance","tester-agent-multisurface","revoir-production","conduire-revue-adversariale","boucler-revue-correction","gerer-git","gerer-depreciation","gerer-release","gerer-mise-a-jour-dependances","proteger-donnees-sensibles","proteger-secrets","auditer-securite-agentique","qualifier-sortie-non-fiable","auditer-combinaisons-capacites","preparer-premortem","choisir-topologie-delegation","transmettre-handoff-technique","verifier-document-rendu","traiter-pdf","traiter-tableur","traiter-presentation","verifier-qualite-donnees","verifier-coherence-multiformat","comparer-documents-semantiquement","tester-webapp","concevoir-interface-non-generique",
    "verifier-contrat-public","gerer-migration-donnees","gerer-feature-flags","observer-systeme","conduire-incident","produire-retour-incident","mesurer-fiabilite-service","analyser-impact-changement","detecter-derive-documentaire","concevoir-experience","auditer-provenance-logicielle","auditer-permissions-capacites","gerer-quotas-et-pression","concevoir-sauvegarde-restauration","tracer-lignee-donnees","distiller-source-en-skill","verifier-accessibilite","auditer-fraicheur-contexte","budgeter-contexte","verifier-isolation-contextes","auditer-fraicheur-savoir","detecter-contradictions-savoir","evaluer-recherche-retrieval","verifier-liens-et-references","prioriser-travail","estimer-effort-incertitude","preparer-memo-decision","verifier-readiness","conduire-retrospective","gerer-licences","definir-metriques","gerer-environnements","detecter-derive-configuration","generer-runbook","verifier-health-readiness","tester-regression-visuelle","auditer-etats-vide-chargement-erreur","red-teamer-agent","auditer-journalisation","verifier-exemples-doc","etudier-marche","analyser-concurrence","scorer-opportunites","concevoir-offre","chiffrer-economie-unitaire","gerer-workflow-durable","gerer-annulation-et-abandon","gerer-escalade-humaine","piloter-android",
    "capitaliser","choisir-capacites","comprehension-architecturale","converger","corriger-et-reprendre","explorer-peut-etre","livrer","orchestrer-missions","passation","prelever-verbatim","produire-commandes","prouver-resultat","retrouver-savoir"
}
LOCAL_ONLY = {"piloter-boucle-magistri","tester-interface-windows","diagnostiquer-dotnet","tester-dotnet","gerer-sqlite","surveiller-cycle-processus","correler-execution-bout-en-bout","modeliser-machine-etats","verifier-interface-backend"}

class BankAdoptionTests(unittest.TestCase):
    def setUp(self):
        self.skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}

    def test_all_chatgpt_adoptions_exist(self):
        self.assertTrue(ADOPTED.issubset(self.skills), sorted(ADOPTED - self.skills))

    def test_candidate_skill_count(self):
        self.assertGreaterEqual(len(self.skills), 154)

    def test_legacy_protocol_pilot_is_absorbed_not_duplicated(self):
        self.assertNotIn("continuum-protocol", self.skills)
        for name in ("lire-protocole","evoluer-protocole","resoudre-demeures","gerer-canonicalite","proteger-concurrence","resoudre-autorite"):
            self.assertIn(name, self.skills)
        legacy=(ROOT/"skills"/"evoluer-protocole"/"SKILL.md").read_text(encoding="utf-8")
        self.assertIn("proteger-concurrence", legacy)
        self.assertIn("formulation minimale", legacy)
        self.assertIn("recomposer le delta", legacy)

    def test_local_branch_not_falsely_exposed_as_chatgpt_skill(self):
        self.assertTrue(LOCAL_ONLY.isdisjoint(self.skills), sorted(LOCAL_ONLY & self.skills))

    def test_new_skills_have_operational_contract(self):
        for name in ADOPTED:
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("## Fonction", text, name)
            self.assertIn("## Preuve", text, name)
            self.assertTrue(text.startswith(f"---\nname: {name}\n"), name)

if __name__ == "__main__":
    unittest.main()
