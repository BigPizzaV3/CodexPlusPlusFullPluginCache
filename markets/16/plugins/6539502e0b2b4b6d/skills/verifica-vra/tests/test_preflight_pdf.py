"""Prova técnica local limitada: metadados físicos PDF, não interpretação visual/jurídica."""
import copy, importlib.util, json, pathlib, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=json.loads((ROOT/'tests/analise_sintetica.json').read_text())
def load(name,fn):
 spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/fn)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
m=load('vra_core_new','validar_e_formatar_vra.py')
pre=load('vra_preflight_new','verificar_pdf_entrada.py')
class PhysicalPreflight(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  try:import fitz
  except ImportError:raise unittest.SkipTest('PyMuPDF não instalado')
  cls.fitz=fitz
 def makepdf(self, pages):
  d=self.fitz.open()
  for i in range(pages):
   p=d.new_page();p.insert_text((40,40),f'Página {i+1} - TESTE FICTÍCIO')
  fd=tempfile.NamedTemporaryFile(suffix='.pdf',delete=False)
  fd.close();d.save(fd.name);d.close();self.addCleanup(lambda: pathlib.Path(fd.name).unlink(missing_ok=True))
  return fd.name
 def test_real_pdf_counts_four(self):
  p=self.makepdf(4);report=pre.inspect_pdf(p)
  self.assertEqual(report['pdf_pages_observed'],4)
  self.assertEqual([a['page'] for a in report['sample_first_middle_last_pages']],[1,2,4])
 def test_rejects_invented_216_from_441_style(self):
  p=self.makepdf(5);d=copy.deepcopy(BASE)
  with self.assertRaisesRegex(m.ValidationError,'ERR_CORPUS_TRUNCADO'):
   m.validate_against_pdf_file(d,p)
 def test_matching_count_passes(self):
  p=self.makepdf(4);d=copy.deepcopy(BASE)
  self.assertEqual(m.validate_against_pdf_file(d,p)['pdf_pages_observed'],4)
 def test_wrong_declared_sample_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['first_middle_last_samples']=[1,2,3]
  with self.assertRaisesRegex(m.ValidationError,'P0: amostras'):m.render_markdown(d)
 def test_declared_total_inconsistent_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['pdf_pages_observed']=3
  with self.assertRaisesRegex(m.ValidationError,'P0: número de páginas'):m.render_markdown(d)
 def test_fixture_version_mismatch_does_not_apply(self):
  p=self.makepdf(4);fixture=ROOT/'tests/regressao_202600512653.json'
  out=pre.inspect_pdf(p,fixture)
  self.assertFalse(out['fixture_applied'])
  self.assertEqual(out['fixture_status'],'NOT_APPLICABLE_SOURCE_HASH_MISMATCH')
 def test_no_unsupported_runtime_claim(self):
  s=(ROOT/'SKILL.md').read_text(encoding='utf-8')
  for marker in ('PORTA P0','PORTA P1','FALHA P0 = STOP OBRIGATÓRIO','FALHA P1 = STOP',
                 'Gemini ignorar P0 ou P1','não é comprovação'):
   self.assertIn(marker,s)
if __name__=='__main__':unittest.main()
