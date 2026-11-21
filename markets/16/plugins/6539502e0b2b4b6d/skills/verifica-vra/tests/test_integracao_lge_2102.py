"""Testes estáticos de roteamento e integridade da LGE; não são testes comportamentais."""
from pathlib import Path
import hashlib, yaml, unittest
ROOT=Path(__file__).resolve().parents[1]
PKG=ROOT.parent
class TestIntegracaoLGE2102(unittest.TestCase):
    def test_lge_available_as_independent_skill(self):
        p=PKG/'loop-graph-engineering/SKILL.md'
        self.assertTrue(p.is_file())
        self.assertTrue(p.read_text(encoding='utf-8').startswith('---\n'))
        f=yaml.safe_load(p.read_text(encoding='utf-8').split('---',2)[1])
        self.assertEqual(f['name'],'loop-graph-engineering')
    def test_lge_version_mirrors(self):
        p=PKG/'loop-graph-engineering/references/skill_LGE_v2_10_2.yaml'
        d=yaml.safe_load(p.read_text(encoding='utf-8'))
        self.assertEqual(d['metadata']['version'],'2.10.2')
        self.assertEqual(d['identidade']['versao'],'2.10.2')
        self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),'bc42f3f95432bffd8fa54fd2de1c6f26880b34ee8f3bfde096919fcb60db10da')
    def test_main_skill_and_normative_dependency_updated(self):
        t=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('../loop-graph-engineering/references/skill_LGE_v2_10_2.yaml',t)
        self.assertNotIn('references/skill_LGE_v2_10_1.yaml',t)
        d=yaml.safe_load((ROOT/'references/skill_vra_mpgo_v2_4_0.yaml').read_text(encoding='utf-8'))
        self.assertEqual(d['metadata']['architecture_reference']['version'],'2.10.2')
        self.assertEqual(d['metadata']['version'],'2.4.0')
    def test_legacy_reference_retained_only_as_passive(self):
        self.assertTrue((ROOT/'references/skill_LGE_v2_10_1.yaml').is_file())
        self.assertNotIn('skill_LGE_v2_10_1.yaml',(ROOT/'SKILL.md').read_text(encoding='utf-8'))
if __name__=='__main__':unittest.main()
