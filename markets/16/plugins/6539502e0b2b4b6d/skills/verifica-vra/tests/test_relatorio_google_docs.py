"""Testes locais de formato e coerência; NÃO exercem Gemini, Docs ou fontes reais."""
import copy
import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('vra_formatter',ROOT/'scripts/validar_e_formatar_vra.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
BASE=json.loads((ROOT/'tests/analise_sintetica.json').read_text(encoding='utf-8'))
class LocalGoogleDocsTests(unittest.TestCase):
 def test_markdown_complete(self):
  x=m.render_markdown(copy.deepcopy(BASE))
  self.assertIn('GOIÁS',x)
  self.assertIn(m.NOTA,x)
  self.assertIn('## 9. FONTES',x)
  for it in BASE['items']:
   self.assertIn('### Item '+it['item_id'],x)
 def test_no_fake_document_link(self):
  x=m.render_markdown(copy.deepcopy(BASE))
  self.assertNotIn('docs.google.com/document/d/',x)
  self.assertNotIn('PDF GERADO',x)
 def test_full_42_items(self):
  d=copy.deepcopy(BASE)
  base=d['items'][0]
  d['items']=[]
  for n in range(42):
   item=copy.deepcopy(base);item['item_id']=f'Q-{n+1:02d}'
   d['items'].append(item)
  d['expected_items_count']=42
  # synthetic case: the original decision may be correction, so ensure one finding for every problematic item
  d['decision']='APROVACAO_DOCUMENTAL'
  d['findings']=[]
  for item in d['items']:
   item['material_status']='CONFORME';item['filling_status']='ADEQUADO'
   item.pop('evidence_gap',None)
  x=m.render_markdown(d)
  self.assertEqual(x.count('### Item Q-'),42)
  self.assertIn('Itens inventariados:** 42',x)
 def test_missing_item_blocked(self):
  d=copy.deepcopy(BASE);d['expected_items_count']+=1
  with self.assertRaises(m.ValidationError):m.render_markdown(d)
 def test_later_evidence_blocked(self):
  d=copy.deepcopy(BASE)
  self.assertTrue(d['items'][0]['evidence'])
  d['items'][0]['evidence'][0]['joined_at']='2030-01-01T10:00:00-03:00'
  with self.assertRaises(m.ValidationError):m.render_markdown(d)
 def test_approval_with_finding_blocked(self):
  d=copy.deepcopy(BASE)
  d['decision']='APROVACAO_DOCUMENTAL'
  with self.assertRaises(m.ValidationError):m.render_markdown(d)
 def test_duplicate_item_blocked(self):
  d=copy.deepcopy(BASE)
  d['items'][1]['item_id']=d['items'][0]['item_id']
  with self.assertRaises(m.ValidationError):m.render_markdown(d)
 def test_output_is_text_not_binary(self):
  x=m.render_markdown(copy.deepcopy(BASE))
  self.assertIsInstance(x,str)
  self.assertFalse(x.startswith('%PDF'))
 def test_only_one_conclusion(self):
  d=copy.deepcopy(BASE);text=m.render_markdown(d)
  self.assertEqual(text.count('**DECISÃO: '),1)
 def test_original_answer_and_vra_locator_preserved(self):
  d=copy.deepcopy(BASE)
  d['items'][1]['answer_raw']='NÃO — marcado originalmente no exemplo'
  d['items'][1]['original_justification']='Observação original: referência mov. 02'
  output=m.render_markdown(d)
  self.assertIn('NÃO — marcado originalmente no exemplo',output)
  self.assertIn('Observação original: referência mov. 02',output)
  self.assertIn('VRA original simulada, quadro I, p. 1',output)
  self.assertIn('Proposta de ajuste (não altera a VRA)',output)
 def test_missing_original_locator_blocked(self):
  d=copy.deepcopy(BASE)
  d['items'][0].pop('vra_item_locator')
  with self.assertRaises(m.ValidationError):m.render_markdown(d)
 def test_missing_original_references_blocked(self):
  d=copy.deepcopy(BASE)
  d['items'][0].pop('declared_references')
  with self.assertRaises(m.ValidationError):m.render_markdown(d)
 def test_report_not_new_vra(self):
  t=(ROOT/'SKILL.md').read_text(encoding='utf-8')
  self.assertIn('PROIBIDO',t)
  self.assertIn('não gerar uma nova VRA',t)
  output=m.render_markdown(copy.deepcopy(BASE))
  self.assertIn('RELATÓRIO DE AUDITORIA DO PREENCHIMENTO DA VRA',output)
  self.assertIn('Resposta ORIGINAL da VRA',output)
  self.assertNotIn('VRA NOVA PREENCHIDA',output)
 def test_skill_contract_and_file_refs(self):
  t=(ROOT/'SKILL.md').read_text(encoding='utf-8')
  self.assertIn('Compartilhar e exportar',t)
  self.assertIn('DOCUMENTO_CRIADO_E_VERIFICADO',t)
  self.assertIn('PRONTO_PARA_EXPORTACAO',t)
  self.assertNotIn('gerar_relatorio_vra_pdf.py',t)
  self.assertTrue((ROOT/'assets/modelo_relatorio_vra_google_docs.md').exists())
  self.assertTrue((ROOT/'references/skill_vra_mpgo_v2_4_0.yaml').exists())
  self.assertIn('MISSÃO OBRIGATÓRIA: AUDITAR, NÃO PREENCHER',t)
if __name__=='__main__':unittest.main()
