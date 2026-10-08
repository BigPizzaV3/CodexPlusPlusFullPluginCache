import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class LocalNoyauBoundaryTests(unittest.TestCase):
    def test_plugin_does_not_embed_unproven_remote_mcp_or_app_manifest(self):
        self.assertFalse((ROOT/".mcp.json").exists())
        self.assertFalse((ROOT/".app.json").exists())

    def test_noyau_skill_keeps_local_execution_under_the_hood(self):
        text=(ROOT/"skills"/"agir-par-noyau"/"SKILL.md").read_text(encoding="utf-8")
        self.assertIn("MCP local",text)
        self.assertIn("API locale",text)
        self.assertIn("Noyau",text)
        self.assertIn("piloter-android",text)
        self.assertNotIn("127.0.0.1",text)
        self.assertNotIn("5086",text)

    def test_android_specialization_keeps_house_partition(self):
        text=(ROOT/"skills"/"piloter-android"/"SKILL.md").read_text(encoding="utf-8")
        self.assertIn("MCP/API de contrôle en loopback",text)
        self.assertIn("relais Android maison",text)
        self.assertIn("aucun fournisseur MCP/API externe",text)
        self.assertIn("aucun free tier",text)
        self.assertIn("aucun GitHub",text)
        self.assertNotIn("89.93.",text)
        self.assertNotIn("device.token",text)

    def test_passerelle_contract_is_separate_from_local_effect_skill(self):
        local=(ROOT/"skills"/"agir-par-noyau"/"SKILL.md").read_text(encoding="utf-8")
        signal=(ROOT/"skills"/"appeler-passerelle"/"SKILL.md").read_text(encoding="utf-8")
        self.assertIn("appeler-passerelle",local)
        for token in ("AppelPasserelle_V1","PUSH","CREATE","PULL"):
            self.assertIn(token,signal)
        self.assertNotIn("Scripts Continuum/requests",local+signal)

if __name__ == "__main__":
    unittest.main()
