import json
import runpy
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_svg_budget.py"


class CheckSvgBudgetTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.svg = self.root / "asset.svg"
        self.svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64"/>')
        self.png = self.root / "asset.png"
        Image.new("RGBA", (64, 64), (25, 80, 120, 255)).save(self.png)

    def run_check(self, width=64, height=64):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(self.svg),
                str(self.png),
                "--width",
                str(width),
                "--height",
                str(height),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotIn("Traceback", result.stderr)
        return result.returncode, json.loads(result.stdout or result.stderr)

    def test_valid_export_reports_actual_bytes(self):
        code, result = self.run_check()
        self.assertEqual(code, 0)
        self.assertTrue(result["passed"])
        self.assertEqual(result["svg_bytes"], self.svg.stat().st_size)
        self.assertEqual(result["png_bytes"], self.png.stat().st_size)

    def test_wrong_dimensions_fail(self):
        code, result = self.run_check(width=128)
        self.assertEqual(code, 1)
        self.assertFalse(result["passed"])
        self.assertFalse(result["dimensions_match"])

    def test_oversized_svg_fails(self):
        self.svg.write_text(
            '<svg xmlns="http://www.w3.org/2000/svg"><desc>' + "x" * 4096 + "</desc></svg>"
        )
        code, result = self.run_check()
        self.assertEqual(code, 1)
        self.assertFalse(result["within_budget"])

    def test_truncated_exports_are_errors(self):
        original = self.png.read_bytes()
        for removed in (1, 4, 8, 12, 20):
            with self.subTest(removed=removed):
                self.png.write_bytes(original[:-removed])
                code, result = self.run_check()
                self.assertEqual(code, 2)
                self.assertIn("error", result)

    def test_corrupt_image_data_is_an_error(self):
        data = bytearray(self.png.read_bytes())
        data[data.index(b"IDAT") + 4] ^= 1
        self.png.write_bytes(data)
        code, result = self.run_check()
        self.assertEqual(code, 2)
        self.assertIn("error", result)

    def test_malformed_svg_is_an_error(self):
        self.svg.write_text("<svg>")
        code, result = self.run_check()
        self.assertEqual(code, 2)
        self.assertIn("error", result)

    def test_svg_in_a_foreign_namespace_is_rejected(self):
        self.svg.write_text('<svg xmlns="urn:other"/>')
        code, result = self.run_check()
        self.assertEqual(code, 2)
        self.assertIn("SVG", result["error"])

    def test_disguised_tiff_never_reaches_pillow(self):
        # A real TIFF with a .png filename and a valid PNG trailer.
        iend = self.png.read_bytes()[-12:]
        Image.new("RGBA", (64, 64)).save(self.png, format="TIFF")
        with self.png.open("ab") as export:
            export.write(iend)

        for script, args in (
            (SCRIPT, [str(self.svg), str(self.png), "--width", "64", "--height", "64"]),
            (SCRIPT.with_name("review_alpha.py"), [str(self.png)]),
        ):
            with self.subTest(script=script.name):
                with (
                    patch.object(sys, "argv", [str(script), *args]),
                    patch.object(Image, "open") as image_open,
                    redirect_stderr(StringIO()),
                    self.assertRaises(SystemExit) as exit_status,
                ):
                    runpy.run_path(str(script), run_name="__main__")
                image_open.assert_not_called()
                self.assertEqual(exit_status.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
