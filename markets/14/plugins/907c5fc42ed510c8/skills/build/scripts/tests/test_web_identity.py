"""New browser-only package safeguards; not a test of OpenAI's importer."""
import ast
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from check_package import ROOT, AUTO, SCRIPT, payload, read_json, validate_web_contract, validate_guidance_contract
from guide import guidance
from iteration.engine import Engine
from iteration.records import LAUNCHER
from iteration import BUILD, __version__

class WebIdentityTests(unittest.TestCase):
    def setUp(self):
        self.m = read_json(ROOT/'.codex-plugin/plugin.json')

    def test_new_package_is_not_the_retired_namespace(self):
        self.assertEqual(self.m['name'],'berrer-build-mcp')
        self.assertNotEqual(self.m['name'],'iteration')
        self.assertEqual((BUILD,__version__),('B005','0.5.0'))
        self.assertEqual(self.m['interface']['displayName'],'Build_')

    def test_account_identity_is_not_embedded(self):
        n = read_json(AUTO/'EB25.json')
        self.assertEqual(n['initial_mode'],'new_private_upload')
        self.assertFalse(n['account_operation_performed'])
        self.assertFalse(n['old_entry_mutated'])
        for name in ('id','target_plugin_id'):
            self.assertNotIn(name,n)
            self.assertNotIn(name,self.m)

    def test_no_connection_or_platform_flag_is_allowed(self):
        for field in ('mcpServers','apps','hooks','platform','platforms','desktopOnly','localMarketplace'):
            with self.subTest(field=field):
                m=copy.deepcopy(self.m);m[field]={}
                with self.assertRaises(ValueError):validate_web_contract(ROOT,m)

    def test_nested_connection_config_is_rejected(self):
        for name in ('mcp.json','.app.json','marketplace.json','hooks.json'):
            with self.subTest(name=name):
                original=list(payload(ROOT))
                with patch('check_package.payload',return_value=iter(original+[(f'skills/build/Automation/{name}',Path(name))])):
                    with self.assertRaises(ValueError):validate_web_contract(ROOT,self.m)

    def test_extensions_only_allow_text_onboarding(self):
        for field in ('mcpServers','apps','hooks','onSelect','sidebar','placeholder'):
            with self.subTest(field=field):
                m=copy.deepcopy(self.m);m['extensions']['com.openai'][field]={}
                with self.assertRaises(ValueError):validate_guidance_contract(ROOT,m)

    def test_web_contract_does_not_claim_account_or_exclusivity(self):
        r=validate_web_contract(ROOT,self.m)
        self.assertEqual(r['target'],'ChatGPT web')
        self.assertFalse(r['desktop_required'])
        self.assertTrue(r['server_required'])
        self.assertFalse(r['platform_exclusion_claimed'])
        self.assertEqual(r['host_installation'],'not_tested')
        self.assertEqual(r['host_update_control'],'not_tested')

    def test_web_requirement_appears_in_main_skill_before_work(self):
        t=(ROOT/'skills/build/SKILL.md').read_text()
        self.assertLess(t.index('## Target: ChatGPT web'),t.index('## Recover before changing'))
        self.assertIn('Do not redirect programming, testing or ZIP production to that MCP gateway.',t)
        self.assertIn('not plugin installation',t)
        self.assertIn('No substantive request means no build.',t)
        self.assertNotIn('MCP: encode',t)
        self.assertIn('CLI log command accepts the file directly',t)

    def test_public_help_and_welcome_are_rebranded(self):
        for msg in ('/help',''):
            r=guidance(msg)
            self.assertIn('Build_',r['text'])
            self.assertNotIn('Iterate',r['text'])
            self.assertNotIn('Iteration',r['text'])
            self.assertFalse(r['state_changed'])
            self.assertFalse(r['build_authorized'])

    def test_old_plugin_label_is_not_a_new_help_command(self):
        for msg in ('Iterate: /help','Iterate:', 'How do I use Iterate?', 'Iterate: /help to get started'):
            self.assertFalse(guidance(msg)['handled'])

    def test_build_word_is_not_confused_with_selection(self):
        for msg in ('Build a timer','Build_help','Build__ /help','Build_: /help','Build_ do not run tests'):
            self.assertFalse(guidance(msg)['handled'])

    def test_new_chip_routes_help_without_extra_colon(self):
        for msg in ('Build_ /help','build_ HELP','Build_ How do I use Build_?'):
            self.assertEqual(guidance(msg)['route'],'help')

    def test_current_status_identifies_new_label_without_protocol_change(self):
        with tempfile.TemporaryDirectory() as td:
            e=Engine(Path(td))
            try:
                s=e.status()
                self.assertEqual(s['name'],'Build_')
                self.assertEqual(s['chat_entry']['display_name'],'Build_')
                self.assertEqual(s['chat_entry']['starter_prompts'],[])
                self.assertFalse(s['capabilities']['model_inference'])
                self.assertTrue(s['capabilities']['hash_bound_delivery_v1'])
            finally:e.close()

    def test_report_schema_stays_compatible_and_errors_point_to_build(self):
        source=(SCRIPT/'iteration/runner_template.py').read_text()
        self.assertIn("SCHEMA = 'iteration.logreport/1'",source)
        self.assertIn('send LogReport.zip back to Build_ for a fix',source)
        self.assertIn('send LogReport.zip back to Build_ for a fix',LAUNCHER)
        self.assertNotIn('back to Iterate',source+LAUNCHER)

    def test_provenance_is_honest_about_baseline_and_brand_changes(self):
        p=read_json(AUTO/'AB60.json')
        self.assertTrue(p['baseline'].startswith('Build_ B'))
        self.assertEqual(p['target_surface'],'ChatGPT web')
        unchanged=p['unchanged_baseline_files_sha256'];brand=p['branding_only_files_sha256']
        self.assertTrue(brand)
        self.assertTrue(p['production_files_sha256'])
        self.assertFalse(set(unchanged)&set(brand))
        for rel,h in unchanged.items():
            self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),h)
        source=read_json(AUTO/'AB60.json')['public_submission']['immutable_user_export_files_sha256']
        for rel in brand:
            # B004 branding is archived as provenance, but v0.7.1 installs newer art.
            self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),source[rel])

    def test_new_installation_has_no_uninstall_or_legacy_update_requirement(self):
        t=(AUTO/'NT64.md').read_text()
        self.assertIn('UPDATE EXISTING WEB PLUGIN',t)
        self.assertIn('Do not use the old Iterate',t)
        self.assertIn('Do not install via Codex or a desktop-local source',t)
        self.assertIn('Upload new version',t)
        self.assertIn('requires live verification',t)

    def test_help_remains_readable_without_execution_or_server(self):
        m=self.m
        self.assertEqual(m['interface']['shortDescription'],'Build and test Windows apps')
        self.assertTrue(m['interface']['longDescription'].startswith('Describe an app and let our plugin'))
        self.assertIn('new chat with Build_ enabled',m['interface']['longDescription'])
        self.assertNotIn('/help',m['interface']['displayName'])
        self.assertEqual(m['interface'].get('defaultPrompt'), ['Press Enter to begin'])
        self.assertTrue((AUTO/'HP12.md').is_file())
