"""Public product rename is presentation-only; old Build_ text retains explicit routing."""
import json
import unittest
from check_package import ROOT
from guide import COMPOSER_LABEL, guidance

class ProductRenameTests(unittest.TestCase):
    def test_public_name_and_underlying_identity(self):
        m=json.loads((ROOT/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        self.assertEqual((m['name'],m['version']),('berrer-build-mcp','0.8.6'))
        self.assertEqual(m['interface']['displayName'],'Build_')
        self.assertEqual(COMPOSER_LABEL,'Build_')
        self.assertEqual(m['interface'].get('defaultPrompt'), ['Press Enter to begin'])
    def test_legacy_and_new_text_hints_route_to_welcome(self):
        for msg in ('Build_', '@Build_', 'Build_', 'BuildFaster'):
            with self.subTest(msg=msg):
                r=guidance(msg)
                self.assertEqual(r['route'],'welcome')
                self.assertFalse(r['build_authorized'])
    def test_new_and_legacy_help_no_side_effects(self):
        for msg in ('Build_ /help','Build_ /help','/help','How do I use BuildFaster?'):
            with self.subTest(msg=msg):
                r=guidance(msg)
                self.assertEqual(r['route'],'help')
                self.assertFalse(r['state_changed'])
    def test_app_source_is_not_routed_to_remote_gateway(self):
        m=json.loads((ROOT/'.mcp.json').read_text(encoding='utf-8'))
        self.assertEqual(m['mcpServers']['build-dependency-checker']['url'],'https://build-api.berrergate.com/mcp')
        s=(ROOT/'skills/build/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('The ONLY remote capability',s)
        self.assertIn('native mention',s)
        self.assertIn('exactly run.bat and PROGRAM/',s)
if __name__=='__main__':unittest.main()
