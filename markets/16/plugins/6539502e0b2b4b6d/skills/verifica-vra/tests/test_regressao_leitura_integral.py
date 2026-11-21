"""Testes estruturais de regressão: dados sintéticos; não executam auditoria real nem Gemini."""
from pathlib import Path
import copy,importlib.util,json,unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('vra_formatter_regression',ROOT/'scripts/validar_e_formatar_vra.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
BASE=json.loads((ROOT/'tests/analise_sintetica.json').read_text(encoding='utf-8'))
class RegressionCoverageTests(unittest.TestCase):
 def test_full_source_index_rendered(self):
  doc=m.render_markdown(copy.deepcopy(BASE))
  self.assertIn('**Integridade do corpus:** 4 páginas; movimentos 1 a 3',doc)
  self.assertIn('Mov. 3 · páginas 3-3',doc)
 def test_movement_missing_from_inventory_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['movements'].pop(1)
  with self.assertRaisesRegex(m.ValidationError,'Inventário de movimentos incompleto'):m.render_markdown(d)
 def test_concluding_from_partial_eligible_movement_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['movements'][1]['review_status']='PARTIAL'
  with self.assertRaisesRegex(m.ValidationError,'não revisado'):m.render_markdown(d)
 def test_concluding_from_incomplete_corpus_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['corpus_incomplete']=True
  with self.assertRaisesRegex(m.ValidationError,'incompleto'):m.render_markdown(d)
 def test_wrong_temporal_inclusion_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['movements'][2]['joined_at']='2026-10-09T11:00:00-03:00'
  with self.assertRaisesRegex(m.ValidationError,'classificação temporal'):m.render_markdown(d)
 def test_document_absence_without_search_record_rejected(self):
  d=copy.deepcopy(BASE);d['findings'][0]['claim_type']='DOCUMENT_ABSENCE'
  with self.assertRaisesRegex(m.ValidationError,'sem manifesto'):m.render_markdown(d)
 def test_document_absence_keyword_without_claim_type_rejected(self):
  d=copy.deepcopy(BASE);d['findings'][0]['issue']='Certidão não consta dos autos'
  with self.assertRaisesRegex(m.ValidationError,'claim_type'):m.render_markdown(d)
 def test_document_absence_only_text_search_rejected(self):
  d=copy.deepcopy(BASE);d['findings'][0]['claim_type']='DOCUMENT_ABSENCE'
  d['absence_claims']=[{'item_id':'I(b)','document_type':'Certidão hipotética','searched_movement_ids':[1,2,3],
   'searched_page_ranges':['1-4'],'search_methods':['busca por palavras','busca por tokens'],
   'counterevidence_review':'Revisão sintética dos movimentos','conclusion':'Hipótese sintética'}]
  with self.assertRaisesRegex(m.ValidationError,'busca textual isolada'):m.render_markdown(d)
 def test_document_absence_with_positive_counterevidence_rejected(self):
  d=copy.deepcopy(BASE);d['findings'][0]['claim_type']='DOCUMENT_ABSENCE'
  d['absence_claims']=[{'item_id':'I(b)','document_type':'Certidão hipotética','searched_movement_ids':[1,2,3],
   'searched_page_ranges':['1-4'],'search_methods':['busca textual','leitura contextual'],
   'counterevidence_review':'Achada certidão positiva de presença','positive_matches':['movimento 3 p.3'], 'conclusion':'Hipótese sintética'}]
  with self.assertRaisesRegex(m.ValidationError,'contraprova'):m.render_markdown(d)
 def test_absence_claim_with_contextual_search_passes_structurally(self):
  d=copy.deepcopy(BASE);d['findings'][0]['claim_type']='DOCUMENT_ABSENCE'
  d['absence_claims']=[{'item_id':'I(b)','document_type':'Certidão hipotética','searched_movement_ids':[1,2,3],
   'searched_page_ranges':['1-4'],'search_methods':['busca textual','leitura contextual'],
   'counterevidence_review':'Sem achados afirmativos no cenário sintético','positive_matches':[],
   'conclusion':'Hipótese sintética de ausência documental'}]
  self.assertIn('Controle de alegações de ausência documental',m.render_markdown(d))
 def test_case_reference_imposes_full_corpus_and_cpen_distinction(self):
  s=(ROOT/'SKILL.md').read_text(encoding='utf-8')
  self.assertIn('Pré-varredura dos autos COMPLETOS',s)
  self.assertIn('positiva com efeitos de negativa',s)
  self.assertIn('"não consta dos autos"',s)
  reg=(ROOT/'references/NOTAS_MIGRACAO_GEMINI.md').read_text(encoding='utf-8')
  for v in ('441 páginas','movimento 4','R$ 1.710,00','10h15'):self.assertIn(v,reg)
if __name__=='__main__':unittest.main()
