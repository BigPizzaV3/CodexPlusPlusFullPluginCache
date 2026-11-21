"""Auditoria estática da identidade da skill, sem simular execução no Gemini."""
import pathlib
import unittest
import yaml

ROOT=pathlib.Path(__file__).resolve().parents[1]

class IntegridadeSkill(unittest.TestCase):
 def test_yaml_version_and_mission(self):
  d=yaml.safe_load((ROOT/'references/skill_vra_mpgo_v2_4_0.yaml').read_text(encoding='utf-8'))
  self.assertEqual(d['metadata']['version'],'2.4.0')
  self.assertEqual(d['identidade']['versao'],'2.4.0')
  self.assertIn('JÁ PREENCHIDA',d['identidade']['responsabilidade_primaria'])
  self.assertIn('vra_item_locator',d['modelo_de_evidencia']['item_record'])
  self.assertIn('original_justification',d['modelo_de_evidencia']['item_record'])
 def test_three_roles_distinct(self):
  t=(ROOT/'SKILL.md').read_text(encoding='utf-8')
  self.assertIn('OBJETO AUDITADO',t)
  self.assertIn('fonte de prova',t)
  self.assertIn('RELATÓRIO DE AUDITORIA',t)
  self.assertIn('PROIBIDO',t)
 def test_template_has_original_values(self):
  t=(ROOT/'assets/modelo_relatorio_vra_google_docs.md').read_text(encoding='utf-8')
  for v in ('VRA ORIGINAL','Resposta ORIGINAL','Localização do item','Referências ORIGINALMENTE','ajustes propostos'):
   self.assertIn(v.lower(),t.lower())
 def test_deps_exist(self):
  for x in ('../loop-graph-engineering/references/skill_LGE_v2_10_2.yaml','references/skill_askuserquestion_v210.yaml',
            'references/skill_comunicacao_assertiva_v110.yaml','references/contrato_analise_vra.schema.json'):
   self.assertTrue((ROOT/x).is_file(),x)

if __name__=='__main__':unittest.main()
