import copy,importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name,filename):
 spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/filename)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
m=load('vra_core','validar_e_formatar_vra.py')
f=load('vra_formal','auditar_formato_google_docs.py')
BASE=json.loads((ROOT/'tests/analise_sintetica.json').read_text(encoding='utf-8'))
class FormatAndVisualRegression(unittest.TestCase):
 def test_formatted_report_complete(self):
  out=f.audit_format(m.render_markdown(BASE),3,BASE['decision'])
  self.assertEqual(out['format_gate'],'PASS',out)
 def test_case_gemini_output_summary_fails(self):
  text='A análise comparativa entre os autos e a VRA revela divergências.\n### Quadro I: Em conformidade.\n### Quadro II: Faltam documentos.'
  out=f.audit_format(text,42,'NECESSIDADE_DE_CORRECOES')
  self.assertEqual(out['format_gate'],'FAIL');self.assertIn('Matriz incompleta', ' '.join(out['errors']))
 def test_missing_item_fields_fails(self):
  text=m.render_markdown(BASE).replace('**Resposta ORIGINAL da VRA:**','**Resposta inventada:**',1)
  self.assertEqual(f.audit_format(text,3,BASE['decision'])['format_gate'],'FAIL')
 def test_report_without_item_fails(self):
  text=m.render_markdown(BASE).replace('### Item I(a)','### Unidade I(a)',1)
  self.assertEqual(f.audit_format(text,3,BASE['decision'])['format_gate'],'FAIL')
 def test_image_only_page_without_visual_inspection_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['image_only_pages']=[2]
  with self.assertRaisesRegex(m.ValidationError,'sem inspeção visual'):m.render_markdown(d)
 def test_image_only_page_after_visual_inspection_accepted(self):
  d=copy.deepcopy(BASE);d['source_inventory'].update({'image_only_pages':[2],'visually_inspected_pages':[2]})
  self.assertIn('RELATÓRIO DE AUDITORIA',m.render_markdown(d))
 def test_missing_range_from_review_rejected(self):
  d=copy.deepcopy(BASE);d['source_inventory']['reviewed_page_ranges']=['1-2']
  with self.assertRaisesRegex(m.ValidationError,'páginas historicamente elegíveis'):m.render_markdown(d)
 def test_original_na_markings_must_be_preserved_in_skill(self):
  s=(ROOT/'SKILL.md').read_text()
  self.assertIn('item I(k) está marcado `Não se aplica`',s)
  self.assertIn('III(f) e III(g)',s)
 def test_visual_regression_diploma_case_present_in_reference(self):
  md=(ROOT/'SKILL.md').read_text()
  for value in ('298–299','DOUTOR EM DIREITO','GATE FMT-01','ERR_RELATORIO_FORA_DO_MODELO'):self.assertIn(value,md)
if __name__=='__main__': unittest.main()
