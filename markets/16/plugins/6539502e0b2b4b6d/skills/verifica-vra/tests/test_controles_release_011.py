"""Regressões da release 0.1.1. Não comprovam leitura material dos autos ou Docs."""
import copy, hashlib, importlib.util, json, pathlib, tempfile, unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('vra_release_011',ROOT/'scripts/validar_e_formatar_vra.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
BASE=json.loads((ROOT/'tests/analise_sintetica.json').read_text(encoding='utf-8'))
try: import fitz
except ImportError:fitz=None

class TestControlesRelease011(unittest.TestCase):
 def test_gapped_page_inventory_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory'].pop('unassigned_page_ranges')
  with self.assertRaisesRegex(v.ValidationError,'páginas físicas sem vínculo'):v.validate(d)
 def test_unassigned_page_without_note_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory'].pop('unassigned_pages_note')
  with self.assertRaisesRegex(v.ValidationError,'unassigned_pages_note'):v.validate(d)
 def test_unassigned_page_unreviewed_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['reviewed_page_ranges']=['1-3']
  with self.assertRaisesRegex(v.ValidationError,'páginas não vinculadas'):v.validate(d)
 def test_unassigned_overlap_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['unassigned_page_ranges']=['3-4']
  with self.assertRaisesRegex(v.ValidationError,'duplicadas'):v.validate(d)
 def test_movement_page_mismatch_rejected(self):
  d=copy.deepcopy(BASE);d['items'][0]['evidence'][0]['page']='2'
  with self.assertRaisesRegex(v.ValidationError,'fora do movimento'):v.validate(d)
 def test_sources_page_mismatch_rejected(self):
  d=copy.deepcopy(BASE);d['sources'][0]['page']='3'
  with self.assertRaisesRegex(v.ValidationError,'fora do movimento'):v.validate(d)
 def test_unresolved_movement_in_substantive_conclusion_rejected(self):
  d=copy.deepcopy(BASE);d['cutoff_at']='2026-10-05';d['cutoff_precision']='DATE_ONLY';d['date_only_resolution']='Ordem não comprovada'
  d['source_inventory']['movements'][0]['temporal_status']='UNRESOLVED'
  with self.assertRaisesRegex(v.ValidationError,'não resolvida'):v.validate(d)
 def test_local_render_passes_both_gates(self):
  d=copy.deepcopy(BASE);out=v.render_markdown(d)
  self.assertEqual(v.validate_formatted_report(out,len(d['items']),d['decision'])['format_gate'],'PASS')
 def test_fake_hash_rejected_when_original_available(self):
  if fitz is None:self.skipTest('PyMuPDF indisponível')
  with tempfile.TemporaryDirectory() as tmp:
   p=pathlib.Path(tmp)/'fake.pdf'
   with fitz.open() as pdf:
    pdf.new_page();pdf.save(p)
   d=copy.deepcopy(BASE);d['vra_pdf_sha256']='0'*64
   with self.assertRaisesRegex(v.ValidationError,'ERR_VRA_ORIGINAL_DIFERENTE'):v.validate_original_vra_file(d,p)
 def test_mismatched_autos_sha_rejected(self):
  if fitz is None:self.skipTest('PyMuPDF indisponível')
  with tempfile.TemporaryDirectory() as tmp:
   p=pathlib.Path(tmp)/'autos.pdf'
   with fitz.open() as pdf:
    for _ in range(4):pdf.new_page()
    pdf.save(p)
   d=copy.deepcopy(BASE);d['source_inventory']['source_pdf_sha256']='0'*64
   with self.assertRaisesRegex(v.ValidationError,'ERR_CORPUS_DIFERENTE'):v.validate_against_pdf_file(d,p)
 def test_valid_matching_shas(self):
  if fitz is None:self.skipTest('PyMuPDF indisponível')
  with tempfile.TemporaryDirectory() as tmp:
   p=pathlib.Path(tmp)/'source.pdf'
   with fitz.open() as pdf:
    for _ in range(4):pdf.new_page()
    pdf.save(p)
   digest=hashlib.sha256(p.read_bytes()).hexdigest()
   d=copy.deepcopy(BASE);d['source_inventory']['source_pdf_sha256']=digest;d['vra_pdf_sha256']=digest
   self.assertEqual(v.validate_against_pdf_file(d,p)['pdf_pages_observed'],4)
   self.assertEqual(v.validate_original_vra_file(d,p)['source_sha256'],digest)

if __name__=='__main__':unittest.main()
