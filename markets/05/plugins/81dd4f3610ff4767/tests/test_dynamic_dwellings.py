import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DynamicDwellingTests(unittest.TestCase):
    def implementation_text(self):
        files = list((ROOT / "skills").glob("*/SKILL.md"))
        files += [ROOT / "coverage.json", ROOT / "continuum_sources.json", ROOT / "skill_graph.json"]
        return "\n".join(p.read_text(encoding="utf-8") for p in files)

    def test_plugin_does_not_duplicate_library_addresses(self):
        text = self.implementation_text()
        self.assertNotIn("https://chatgpt.com/library/d/", text)
        self.assertNotIn("external-gdrive:root", text)
        self.assertNotRegex(text, r"D:\\\\Source Canonique")

    def test_protocol_home_is_runtime_bound(self):
        data = json.loads((ROOT / "coverage.json").read_text(encoding="utf-8"))
        protocol = data["canonical_protocol"]
        self.assertNotIn("home", protocol)
        self.assertEqual("runtime-current-canon", protocol["home_binding"])
        self.assertEqual("lire-protocole", protocol["home_resolver"])

    def test_routing_and_mirror_are_dynamic(self):
        homes = (ROOT/"skills"/"resoudre-demeures"/"SKILL.md").read_text(encoding="utf-8")
        mirror = (ROOT/"skills"/"synchroniser-miroir"/"SKILL.md").read_text(encoding="utf-8")
        self.assertIn("pas des constantes", homes)
        self.assertIn("n’est pas une seconde écriture applicative", mirror)

if __name__ == "__main__": unittest.main()
