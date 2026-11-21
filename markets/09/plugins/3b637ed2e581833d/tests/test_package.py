import json
import re
import unittest
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_CATEGORIES = {
    "Productivity",
    "Creativity",
    "Developer Tools",
    "Business & Operations",
    "Data & Analytics",
    "Communication",
    "Education & Research",
    "Security",
    "Finance",
    "Healthcare",
    "Travel",
    "Entertainment",
    "Other",
}


def load_json(relative_path: str) -> dict:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


class PluginPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = load_json("plugin.json")
        cls.openai = cls.manifest["extensions"]["com.openai"]
        cls.interface = cls.openai["interface"]

    def test_identity_and_listing_metadata(self) -> None:
        self.assertRegex(self.manifest["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertRegex(self.manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(
            self.manifest["license"],
            "LicenseRef-YouArt-Proprietary",
        )
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("YouArt Plugin Proprietary License", license_text)
        self.assertIn("license to download the Plugin", license_text)
        self.assertLessEqual(len(self.interface["displayName"]), 30)
        self.assertLessEqual(len(self.interface["shortDescription"]), 30)
        self.assertLessEqual(len(self.interface["longDescription"]), 4_000)
        self.assertLessEqual(len(self.interface["developerName"]), 80)
        self.assertIn(self.interface["category"], ALLOWED_CATEGORIES)
        self.assertLessEqual(len(self.interface["capabilities"]), 20)

        prompts = self.interface["defaultPrompt"]
        self.assertLessEqual(len(prompts), 3)
        self.assertEqual(len(prompts), len(set(prompts)))
        for prompt in prompts:
            self.assertLessEqual(len(prompt), 128)
            self.assertNotIn("\n", prompt)
            self.assertNotIn("@", prompt)

    def test_public_urls_are_https(self) -> None:
        for field in (
            "websiteURL",
            "supportURL",
            "privacyPolicyURL",
            "termsOfServiceURL",
        ):
            parsed = urlparse(self.interface[field])
            self.assertEqual(parsed.scheme, "https", field)
            self.assertTrue(parsed.netloc, field)

        self.assertEqual(
            self.manifest["repository"],
            "https://github.com/youart-open-source/youart-plugin",
        )
        self.assertEqual(
            self.interface["supportURL"],
            "https://youart.ai/support",
        )

    def test_brand_assets_are_packaged_square_svgs(self) -> None:
        for field in ("composerIcon", "logo"):
            relative_path = self.interface[field]
            self.assertTrue(relative_path.startswith("./"))
            asset = ROOT / relative_path.removeprefix("./")
            self.assertTrue(asset.is_file(), field)
            svg = asset.read_text(encoding="utf-8")
            match = re.search(r'viewBox="0 0 ([0-9.]+) ([0-9.]+)"', svg)
            self.assertIsNotNone(match, field)
            self.assertEqual(match.group(1), match.group(2), field)
            self.assertGreaterEqual(float(match.group(1)), 48, field)

    def test_package_contains_only_the_creative_workflow_skill(self) -> None:
        skills_root = ROOT / "skills"
        skill_dirs = {
            path.name
            for path in skills_root.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        }
        self.assertEqual(skill_dirs, {"creative-workflow"})

        skill_text = (skills_root / "creative-workflow" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertTrue(skill_text.startswith("---\n"))
        frontmatter = skill_text.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name:\s*creative-workflow\s*$")
        self.assertRegex(frontmatter, r"(?m)^description:\s*\S")
        self.assertFalse(
            (skills_root / "creative-workflow" / "agents" / "openai.yaml").exists()
        )
        self.assertEqual(
            self.openai["onboardingSkill"],
            "./skills/creative-workflow/SKILL.md",
        )

    def test_mcp_connection_is_the_curated_production_endpoint(self) -> None:
        mcp = load_json("mcp.json")
        self.assertEqual(
            mcp["mcpServers"],
            {
                "youart-plugin": {
                    "type": "streamable-http",
                    "url": "https://mcp.youart.ai/plugin/mcp",
                }
            },
        )

    def test_review_materials_have_required_case_counts(self) -> None:
        review = self.openai["review"]
        cases = review["test_cases"]
        self.assertEqual(len(cases["positive"]), 5)
        self.assertEqual(len(cases["negative"]), 3)
        for case in cases["positive"]:
            self.assertTrue(case["description"])
            self.assertTrue(case["prompt"])
            self.assertTrue(case["tools_triggered"])
            self.assertTrue(case["expected_behavior"])
        for case in cases["negative"]:
            self.assertTrue(case["description"])
            self.assertTrue(case["prompt"])
            self.assertTrue(case["expected_behavior"])
        self.assertIs(review["commerce"], False)
        self.assertTrue(self.openai["publication"]["release_notes"])

    def test_marketplace_matches_plugin_identity(self) -> None:
        marketplace = load_json(".agents/plugins/marketplace.json")
        self.assertEqual(marketplace["name"], "youart")
        self.assertEqual(len(marketplace["plugins"]), 1)
        entry = marketplace["plugins"][0]
        self.assertEqual(entry["name"], self.manifest["name"])
        self.assertEqual(entry["source"], {"source": "local", "path": "./"})
        self.assertEqual(entry["category"], self.interface["category"])

    def test_public_docs_do_not_describe_a_private_or_short_film_package(self) -> None:
        public_text = "\n".join(
            (ROOT / name).read_text(encoding="utf-8")
            for name in ("README.md", "INSTALL.md", "LICENSE", "plugin.json")
        ).lower()
        self.assertNotIn("private beta", public_text)
        self.assertNotIn("private repository", public_text)
        self.assertNotIn("short-film", public_text)


if __name__ == "__main__":
    unittest.main()
