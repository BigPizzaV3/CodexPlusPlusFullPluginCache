"""Submission v0.8.2: executable package invariants, not portal approval."""
import json
import unittest
from check_package import ROOT, AUTO

class Public083Tests(unittest.TestCase):
    def test_review_and_identity(self):
        m=json.loads((ROOT/'.codex-plugin/plugin.json').read_text())
        self.assertEqual((m['name'],m['version']),('berrer-build-mcp','0.8.6'))
        self.assertEqual(m['interface']['category'],'Developer Tools')
        self.assertEqual(m['interface']['displayName'],'Build_')
        self.assertEqual(m['interface'].get('defaultPrompt'), ['Press Enter to begin'])
        self.assertEqual(len(m['extensions']['com.openai']['review']['test_cases']['positive']),5)
        self.assertEqual(len(m['extensions']['com.openai']['review']['test_cases']['negative']),3)
        self.assertEqual(len(m['extensions']['com.openai']['review']['prompts']),4)
        self.assertNotIn('demo_recording_url',m['extensions']['com.openai']['review'])
    def test_server_and_data_boundaries(self):
        m=json.loads((ROOT/'.mcp.json').read_text())
        self.assertEqual(m['mcpServers']['build-dependency-checker']['url'],'https://build-api.berrergate.com/mcp')
        self.assertFalse((ROOT/'.app.json').exists())
        s=(ROOT/'skills/build/SKILL.md').read_text()
        self.assertIn('exactly run.bat and PROGRAM/',s)
        self.assertIn('PROGRAM/readme.md',s)
        self.assertIn('The ONLY remote capability',s)

if __name__ == '__main__':unittest.main()
