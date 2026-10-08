import json
import unittest
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]

class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.repo_data = json.loads((ROOT.parents[1] / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))

    def test_manifest_is_current_skills_only_bundle(self):
        self.assertEqual("continuum", self.data["name"])
        self.assertEqual("0.5.0", self.data["version"])
        self.assertEqual("./skills/", self.data["skills"])
        self.assertNotIn("mcpServers", self.data)
        self.assertNotIn("apps", self.data)

    def test_manifest_describes_mesh(self):
        text = json.dumps(self.data, ensure_ascii=False)
        self.assertIn("maillage", text.lower())
        self.assertIn("Protocole", text)
        self.assertIn("Noyau", text)
        self.assertIn("@Continuum", text)
        long_description = self.data["interface"]["longDescription"]
        self.assertIn("une fois à l’entrée du tchat", long_description)
        self.assertIn("copie de session", long_description)
        self.assertNotIn("relu intégralement à chaque tour", long_description.lower())
        self.assertEqual(long_description, self.repo_data["interface"]["longDescription"])

    def test_default_prompts_invoke_continuum(self):
        prompts = self.data["interface"]["defaultPrompt"]
        self.assertTrue(prompts and all(p.startswith("@Continuum") for p in prompts))

    def test_public_links_and_images(self):
        i = self.data["interface"]
        self.assertEqual("https://github.com/Axel-SDP/continuum-public", i["websiteURL"])
        for key in ("composerIcon", "logo"):
            path = ROOT / i[key][2:]
            self.assertTrue(path.is_file())
            raw = path.read_bytes()
            self.assertTrue(raw.startswith(b"\x89PNG\r\n\x1a\n"))
            self.assertGreaterEqual(len(raw), 24)
            width, height = struct.unpack(">II", raw[16:24])
            self.assertEqual(width, height)

if __name__ == "__main__":
    unittest.main()
