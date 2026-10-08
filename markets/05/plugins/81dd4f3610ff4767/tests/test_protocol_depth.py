import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def skill(name): return (ROOT/"skills"/name/"SKILL.md").read_text(encoding="utf-8")
def require(name,*patterns):
    text=skill(name)
    for p in patterns:
        if not re.search(p,text,re.I|re.S): raise AssertionError(f"{name}: {p}")

class ProtocolDepthTests(unittest.TestCase):
    def test_opening_and_context_are_distinct(self):
        require("lire-protocole",r"douze fichiers normatifs",r"01.*12",r"deux heures",r"Gardiennage",r"premier tour de tout nouveau tchat",r"copie de session",r"invalidée|incomplète|indisponible|douteuse",r"suspendre toute réponse de fond")
        reader=skill("lire-protocole")
        self.assertNotIn("and every Axel turn requiring a visible answer from Azer", reader)
        self.assertNotIn("- chaque nouveau message d’Axel appelant une réponse visible d’Azer.", reader)
        require("charger-contexte-continuum",r"ne limite.*Protocole|n.épuise pas tout le contexte",r"Projet",r"Savoir",r"Noyau")
        require("amorcer-continuum",r"routeur racine",r"chaque nouveau message d.Axel",r"copie de session",r"lire-protocole",r"seulement si")
        starter=skill("amorcer-continuum")
        self.assertNotIn("cette lecture est répétée à chaque tour", starter.lower())
        require("amorcer-continuum",r"## Gardiennage",r"Merci,Poursuis!##",r"aucun état résiduel")

    def test_execution_mesh(self):
        text=skill("executer-demande")
        for name in ["charger-contexte-continuum","appliquer-exigences-axel","questionner-totalement","resoudre-autorite","appliquer-cout-zero","construire-plan","qualifier-preuve","prevol-capacites","proteger-concurrence","gerer-transactions","gerer-reprise","gerer-livrables","choisir-livraison","tenir-verbatim"]:
            self.assertIn(name,text)

    def test_specificity_is_explicit(self):
        require("appliquer-exigences-axel",r"ChatGPT",r"exigence durable.*absente.*maillage|défaut de couverture")
        require("maintenir-specificite-continuum",r"ChatGPT générique",r"aucune exigence matérielle",r"responsable",r"preuve")
        require("appliquer-contexte-projet",r"Projet ne précède jamais le Protocole",r"Magister Operis")
        require("choisir-livraison",r"reconstruire",r"versions, paquets, README|identifiants, versions")

    def test_cross_cutting_rules_have_owners(self):
        require("resoudre-autorite",r"capacité technique et autorisation",r"locuteur réel",r"validation")
        require("qualifier-preuve",r"absence de preuve",r"signal",r"validation globale")
        require("appliquer-cout-zero",r"Je lève le cout 0 pour cette mission",r"capital actif",r"50 % gelés")
        require("respecter-typographie",r"français correct",r"dénominations complètes")
        require("questionner-totalement",r"recherche",r"plusieurs|angles|contradictoire")

    def test_technical_feedback_loop(self):
        require("executer-powershell",r"Windows PowerShell 5.1",r"stdout",r"stderr",r"code de sortie")
        require("traiter-retour-technique",r"étape la plus précoce",r"correction devinée")
        require("apprendre-du-reel",r"Savoir",r"bruit")

    def test_safety_is_split(self):
        require("proteger-concurrence",r"ETag",r"ne pas l.écraser")
        require("gerer-transactions",r"identité d.opération",r"rejeu")
        require("gerer-reprise",r"dernier état réellement prouvé",r"reprendre automatiquement")
        require("tracer-execution",r"raisonnement privé",r"Verbatim")
        require("prevol-capacites",r"annoncée.*découverte.*accessible.*autorisée.*opérationnelle")

    def test_library_knowledge_is_split(self):
        require("resoudre-demeures",r"Index.*unique",r"Bibliothèque GPT native",r"pas des constantes|données de routage")
        require("gerer-canonicalite",r"nature, fonction, état réel",r"source responsable")
        require("synchroniser-miroir",r"chemin.*autoritaire",r"représentation secondaire",r"second canon")
        require("gerer-savoir",r"demeure courante",r"Grande Famille")
        require("integrer-savoir",r"Magister Operis ne réalise jamais",r"demeure de transit|transit")

    def test_continuity_is_split(self):
        require("tenir-continuite",r"Qui je suis",r"Présent",r"dernier marqueur.*absorption")
        require("tenir-histoire",r"Page définitive",r"Index Histoire",r"Histoire\.md")
        require("executer-pre-passation",r"décidée uniquement par Axel",r"même tchat")
        require("executer-passation",r"nouveau tchat",r"screen",r"URL")
        require("reprendre-passation",r"Continuité Azer",r"screen",r"URL")
        require("executer-passation",r"sans accusé final",r"effective immédiatement")
        require("tenir-verbatim",r"Protocole intégral :",r"non établi")

    def test_magistri_and_local_are_split(self):
        require("qualifier-magister",r"permanent uniquement si Axel",r"Projet commun `Magistri Operis`")
        require("qualifier-magister",r"Magistri Operis conversationnels",r"logiciel, local, distant ou composite")
        require("preparer-mission-magister",r"achevable sans Passation",r"courrier",r"route")
        require("clore-mission-magister",r"disparaître",r"bruit")
        require("agir-par-noyau",r"MCP local",r"API locale",r"appeler-passerelle")
        require("appeler-passerelle",r"AppelPasserelle_V1",r"PUSH",r"CREATE",r"PULL")
        require("qualifier-raccordabilite-noyau",r"entrées, sorties",r"Passerelle",r"non construite")

    def test_azer_operational_environment_is_owned(self):
        require("gerer-environnement-azer",r"Cartographie Ordinateur Azer",r"Erreurs retenues",r"Reprise active Azer",r"checkpoint")
        require("executer-demande",r"gerer-environnement-azer")
        require("qualifier-magister",r"tchat standard `Chat`",r"moyens remplaçables")

    def test_traceability_covers_operational_mesh(self):
        import json
        data=json.loads((ROOT/"coverage.json").read_text(encoding="utf-8"))
        files=data["canonical_protocol"]["files"]
        self.assertEqual([f"{i:02}" for i in range(1,13)],[entry["id"] for entry in files])
        for entry in files:
            owners=[owner for group in entry["responsibilities"].values() for owner in group]
            self.assertGreaterEqual(len(owners),2,entry["id"])
        twelve=files[-1]["responsibilities"]["value_experiments"]
        self.assertIn("concevoir-offre",twelve)

    def test_plugin_alignment_is_provable(self):
        require("realigner-plugin",r"source, tests statiques, paquet construit, Draft publiée, version Released, installation",r"canon")
        require("auditer-alignement",r"responsabilité sans Skill",r"monolithe",r"ALIGNÉ")

if __name__ == "__main__": unittest.main()
