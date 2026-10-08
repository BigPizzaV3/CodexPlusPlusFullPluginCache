import json,os,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class CliTests(unittest.TestCase):
    def test_example(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'result.json';r=subprocess.run([sys.executable,str(ROOT/'scripts/run.py'),'--input',str(ROOT/'examples/input.json'),'--output',str(out)],capture_output=True);self.assertEqual(r.returncode,0,r.stderr);self.assertEqual(json.loads(out.read_text())['plugin'],ROOT.name)
    def test_same_file_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'input.json';p.write_bytes((ROOT/'examples/input.json').read_bytes());r=subprocess.run([sys.executable,str(ROOT/'scripts/run.py'),'--input',str(p),'--output',str(p)],capture_output=True);self.assertEqual(r.returncode,2)
