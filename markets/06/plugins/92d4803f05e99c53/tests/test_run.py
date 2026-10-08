import copy, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from run import run

class TrustEvidenceTests(unittest.TestCase):
    def setUp(self): self.data = json.loads((ROOT/'examples/input.json').read_text(encoding='utf-8'))
    def test_example_is_complete_and_pure(self):
        original=copy.deepcopy(self.data); result=run(self.data)
        self.assertEqual(result['plugin'], 'aivana-trust-evidence'); self.assertEqual(result['status'], 'complete'); self.assertFalse(result['approval_required']); self.assertEqual(self.data, original)
    def test_gap_and_access_mismatch_require_approval(self):
        self.data['access_checks'][0]['observed']='deny'; self.data['decisions']=[]
        result=run(self.data)
        self.assertEqual(result['status'], 'needs_review'); self.assertTrue(result['approval_required'])
        self.assertIn('access_mismatch', {x['type'] for x in result['findings']})
    def test_bad_hash_and_unknown_reference(self):
        self.data['evidence'][0]['expected_sha256']='0'*64
        self.assertIn('evidence_hash_mismatch', {x['type'] for x in run(self.data)['findings']})
        self.data['decisions'][0]['evidence_ids']=['missing']
        with self.assertRaises(ValueError): run(self.data)
    def test_required_fields_and_cli(self):
        for field in ('requirements','decisions','evidence','access_checks'):
            bad=copy.deepcopy(self.data); del bad[field]
            with self.assertRaises(ValueError): run(bad)
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp)/'nested/result.json'; p=subprocess.run([sys.executable,str(ROOT/'scripts/run.py'),'--input',str(ROOT/'examples/input.json'),'--output',str(output)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr); self.assertEqual(json.loads(output.read_text())['status'],'complete')

if __name__ == '__main__': unittest.main()
