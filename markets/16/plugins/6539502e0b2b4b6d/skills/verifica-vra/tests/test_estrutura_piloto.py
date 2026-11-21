"""Regressões documentais textuais com fixture de caso; não afirmam nova auditoria real."""
import json, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class Pilot(unittest.TestCase):
 def test_fixture_bound_by_hash(self):
  f=json.loads((ROOT/'tests/regressao_202600512653.json').read_text())
  self.assertEqual(len(f['pdf_sha256_exact']),64)
  self.assertEqual(f['pdf_pages'],441)
  self.assertIn(298,[a['page'] for a in f['anchors']])
  self.assertIn(383,[a['page'] for a in f['anchors']])
  self.assertEqual(f['cutoff'],'2026-09-17T10:15:00-03:00')
 def test_reference_not_hardcoded_general(self):
  t=(ROOT/'SKILL.md').read_text()
  self.assertIn('somente para a versão EXATA do PDF',t)
if __name__=='__main__':unittest.main()
