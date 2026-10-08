import importlib.util
import json
from pathlib import Path
import shutil
import uuid
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("new_run", ROOT / "scripts/new_run.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class RunTests(unittest.TestCase):
    def setUp(self):
        # Ordinary mkdir preserves workspace ACL inheritance on Windows.
        self.base = (Path.cwd() / ("equity-run-" + uuid.uuid4().hex)).resolve()
        self.base.mkdir()
        self.addCleanup(self.cleanup_owned_directory)

    def cleanup_owned_directory(self):
        if self.base.parent != Path.cwd().resolve() or not self.base.name.startswith("equity-run-"):
            raise RuntimeError("Refusing cleanup outside the test workspace")
        shutil.rmtree(self.base)

    def test_defaults_and_unicode(self):
        dest = module.create_run(self.base / "run", "Énergie storage")
        mandate = json.loads((dest / "mandate.json").read_text(encoding="utf-8"))
        self.assertEqual(mandate["industry"], "Énergie storage")
        self.assertEqual(mandate["horizon_years"], 7)
        self.assertEqual(mandate["horizon_sensitivity_years"], [5, 10])
        self.assertIsNone(mandate["benchmark"])
        self.assertTrue((dest / "evidence.csv").exists())
        self.assertTrue((dest / "briefs").is_dir())
        self.assertFalse((dest / "scenario-input.json").exists())

    def test_refuse_overwrite(self):
        dest = self.base / "existing"
        dest.mkdir()
        marker = dest / "user.txt"
        marker.write_text("preserve", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            module.create_run(dest, "industry")
        self.assertEqual(marker.read_text(encoding="utf-8"), "preserve")

    def test_refuse_plugin_writes(self):
        with self.assertRaises(ValueError):
            module.create_run(ROOT / "runs" / "bad", "industry")

    def test_invalid_input_does_not_create_directory(self):
        dest = self.base / "invalid"
        for industry, horizon in [(" ", None), ("industry", 0), ("industry", float("nan")), ("industry", True)]:
            with self.assertRaises(ValueError):
                module.create_run(dest, industry, horizon=horizon)
            self.assertFalse(dest.exists())

    def test_overrides_are_explicit(self):
        dest = module.create_run(self.base / "override", "chips", "Global", 3)
        mandate = json.loads((dest / "mandate.json").read_text(encoding="utf-8"))
        self.assertEqual(mandate["universe"], "Global")
        self.assertEqual(mandate["horizon_years"], 3)
        self.assertEqual(mandate["horizon_sensitivity_years"], [])


if __name__ == "__main__":
    unittest.main()
