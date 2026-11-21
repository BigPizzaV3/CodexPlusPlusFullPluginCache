"""Validação estrutural local dos metadados de publicação da release 0.2.0.
Não verifica conteúdo remoto das páginas e não autoriza submissão pública.
"""
import json
from pathlib import Path
import unittest
from PIL import Image

ROOT = Path(__file__).resolve().parents[3]
class TestRelease013Metadata(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/'plugin.json').read_text(encoding='utf-8'))
        cls.interface=cls.manifest['extensions']['com.openai']['interface']
    def test_version_and_identity(self):
        self.assertEqual(self.manifest['version'],'0.2.0')
        self.assertEqual(self.manifest['name'],'verifica-vra')
    def test_four_listing_urls(self):
        expected = {
            'websiteURL': 'https://www.digg.ia.br',
            'supportURL': 'https://www.digg.ia.br',
            'privacyPolicyURL': 'https://digg.ia.br/privacy.html',
            'termsOfServiceURL': 'https://digg.ia.br/terms.html',
        }
        for key, value in expected.items():
            with self.subTest(key=key):
                self.assertEqual(self.interface[key],value)
    def test_interface_metadata_limits(self):
        self.assertLessEqual(len(self.interface['displayName']),30)
        self.assertLessEqual(len(self.interface['shortDescription']),30)
        self.assertLessEqual(len(self.interface['longDescription']),4000)
        self.assertIn(self.interface['category'],{'Business & Operations','Communication','Creativity','Data & Analytics','Developer Tools','Education & Research','Entertainment','Finance','Healthcare','Other','Productivity','Scientific Research','Security','Travel'})
        self.assertIsInstance(self.interface['capabilities'],list)
        self.assertTrue(1<=len(self.interface['defaultPrompt'])<=3)
        for x in self.interface['defaultPrompt']:
            self.assertTrue(x and len(x)<=128 and '\n' not in x)
    def test_icon_file(self):
        for key in ('logo','composerIcon'):
            rel=self.interface[key]
            self.assertTrue(rel.startswith('./assets/'))
            f=ROOT/rel[2:]
            self.assertTrue(f.is_file())
            with Image.open(f) as im:
                self.assertEqual(im.format,'PNG')
                self.assertEqual(im.size, (512,512))
            self.assertLessEqual(f.stat().st_size,5*1024*1024)
    def test_absence_app_binding(self):
        self.assertFalse((ROOT/'.app.json').exists())
        self.assertNotIn('apps',self.interface)
        self.assertNotIn('apps',self.manifest['extensions']['com.openai'])

if __name__ == '__main__':
    unittest.main()
