"""Static/on-host-preview B084 onboarding gates; no claim about native ChatGPT UI rendering."""
import json
import unittest
from check_package import ROOT
from guide import guidance

class Onboarding084Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        cls.skill=(ROOT/'skills/build/SKILL.md').read_text(encoding='utf-8')
        cls.welcome=(ROOT/'skills/build/Automation/WC23.md').read_text(encoding='utf-8')

    def test_public_name_and_single_explicit_starter(self):
        ui=self.manifest['interface']
        self.assertEqual(ui['displayName'],'Build_')
        self.assertEqual(ui['defaultPrompt'],['Press Enter to begin'])
        self.assertEqual(self.manifest['name'],'berrer-build-mcp')

    def test_starter_only_issues_welcome_no_build(self):
        for message in ('Press Enter to begin',' press enter to BEGIN ', 'Build_ Press Enter to begin', 'Press Enter to start'):
            with self.subTest(message=message):
                r=guidance(message)
                self.assertEqual(r['route'],'welcome')
                self.assertFalse(r['build_authorized'])
                self.assertFalse(r['state_changed'])

    def test_starter_is_not_repeated_in_same_conversation(self):
        r=guidance('Press Enter to begin',already_welcomed=True)
        self.assertEqual(r['route'],'ask')
        self.assertNotIn('Welcome to Build_',r['text'])

    def test_unselected_does_not_invoke_starter(self):
        self.assertFalse(guidance('Press Enter to begin',selected=False)['handled'])

    def test_direct_build_message_is_never_intercepted(self):
        for message in ('Build me a calculator', 'Make me a Windows stockroom app',
                        'Build_ build me a counter','Press Enter to begin making a puzzle app'):
            with self.subTest(message=message):
                r=guidance(message)
                self.assertEqual(r['route'],'conversation')
                self.assertFalse(r['handled'])

    def test_rough_concept_stays_conversational(self):
        for message in ('I have a rough game idea', 'Could we discuss a stockroom app?'):
            r=guidance(message)
            self.assertEqual(r['route'],'conversation')
        for expected in ('**EXPLORE:**','**DIRECT BUILD:**','Shall I build this first prototype for you to test?'):
            self.assertIn(expected,self.skill)

    def test_welcome_explains_customer_process(self):
        for expected in ('Describe your app idea','discuss','first prototype','LogReport.zip',
                         'What would you like to make?'):
            self.assertIn(expected,self.welcome)
        self.assertNotIn('your report confirms',self.welcome.casefold())

    def test_release_keeps_existing_gateway_and_zip_layout(self):
        self.assertIn('exactly `run.bat` and `PROGRAM/`',self.skill)
        mcp=json.loads((ROOT/'.mcp.json').read_text())
        self.assertEqual(mcp['mcpServers']['build-dependency-checker']['url'],
                         'https://build-api.berrergate.com/mcp')
        self.assertIn('**RETURN:**',self.skill)

    def test_review_cases_unchanged(self):
        cases=self.manifest['extensions']['com.openai']['review']['test_cases']
        self.assertEqual(len(cases['positive']),5)
        self.assertEqual(len(cases['negative']),3)

    def test_no_claim_of_automatic_native_composer_injection(self):
        self.assertIn('host-controlled',self.skill)
        self.assertIn('Starter UI presentation/prefilling is not guaranteed',self.skill)
        self.assertIn('do not claim native composer control',self.skill)

if __name__=='__main__':unittest.main()
