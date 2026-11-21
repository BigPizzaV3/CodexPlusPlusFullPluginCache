"""Skills-only rollback and info-page copy checks; not a native ChatGPT UI test."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from check_package import ROOT, AUTO, read_json, validate, validate_guidance_contract, validate_listing_contract
from guide import COMPOSER_LABEL, LEGACY_LABEL, guidance


class InfoPageTests(unittest.TestCase):
    def setUp(self):
        self.m = read_json(ROOT/'.codex-plugin/plugin.json')
        self.ui = self.m['interface']

    def test_selected_chip_has_new_public_name(self):
        self.assertEqual(self.ui['displayName'], 'Build_')
        self.assertEqual(COMPOSER_LABEL, 'Build_')
        self.assertNotIn('/help', self.ui['displayName'])

    def test_tagline_is_in_the_subtitle(self):
        self.assertEqual(self.ui['shortDescription'], 'Build and test Windows apps')
        self.assertEqual(len(self.ui['shortDescription']), 27)
        self.assertLessEqual(len(self.ui['shortDescription']), 30)

    def test_description_starts_with_usage_before_constraints(self):
        d = self.ui['longDescription']
        self.assertTrue(d.startswith('Describe an app and let our plugin build it for you.'))
        self.assertLess(d.index('upload LogReport.zip'), d.index('When a chat gets too long'))
        self.assertLess(d.index('run.bat'), d.index('Downloaded apps require'))

    def test_description_explains_test_return_and_fresh_chat(self):
        d = self.ui['longDescription']
        for text in ('downloadable ZIP', 'double-click run.bat', 'Logs are saved beside run.bat',
                     'review the results', 'describe changes and improvements to your app',
                     'latest build ZIP', 'new chat with Build_ enabled', 'project context'):
            self.assertIn(text, d)

    def test_requested_runtime_copy_keeps_existing_privacy_guidance(self):
        d = self.ui['longDescription']
        for text in ('Python 3.10 or newer', 'unless a runtime is included',
                     'Logs are saved beside run.bat in root.'):
            self.assertIn(text, d)
        # Public wording is supplied by the user. Existing help still explains privacy.
        help_text = (AUTO/'HP12.md').read_text(encoding='utf-8')
        self.assertIn('Nothing uploads automatically.', help_text)
        self.assertIn('Inspect reports before sharing', help_text)

    def test_public_metadata_does_not_advertise_internal_records(self):
        public = ' '.join(self.ui[k] for k in ('displayName','shortDescription','longDescription')).casefold()
        for text in ('handoff','brainstorm','locked in','ab60','ln32','automation/',
                     'onboardingskill','127.0.0.1','secure mcp','connect your server'):
            self.assertNotIn(text, public)

    def test_plain_copy_needs_no_html_or_markdown_renderer(self):
        d = self.ui['longDescription']
        self.assertNotIn('<', d)
        self.assertNotIn('**', d)
        self.assertNotIn('](', d)
        self.assertIn('Type /help for a quick guide', ' '.join(d.split()))

    def test_rejected_long_label_cannot_pass_contract(self):
        m = copy.deepcopy(self.m)
        m['interface']['displayName'] = LEGACY_LABEL
        with self.assertRaises(ValueError): validate_listing_contract(m)

    def test_intro_cannot_be_displaced_by_service_blurb(self):
        m = copy.deepcopy(self.m)
        m['interface']['longDescription'] = 'Configure a service first.\n\n'+m['interface']['longDescription']
        with self.assertRaises(ValueError): validate_listing_contract(m)

    def test_incomplete_or_oversized_usage_copy_is_rejected(self):
        for d in (None, 'Describe an app and let Build_ build it for you. Hello.', self.ui['longDescription']+'x'*4000):
            with self.subTest(description_type=type(d).__name__):
                m = copy.deepcopy(self.m); m['interface']['longDescription'] = d
                with self.assertRaises(ValueError): validate_listing_contract(m)

    def test_only_documented_starter_and_no_fake_composer_controls(self):
        self.assertEqual(self.ui['defaultPrompt'], ['Press Enter to begin'])
        for field in ('placeholder','composerPlaceholder','inputPlaceholder','onFocus','onClick'):
            with self.subTest(field=field):
                m = copy.deepcopy(self.m);m['interface'][field] = 'Type /help'
                with self.assertRaises(ValueError):validate_guidance_contract(ROOT,m)
        m=copy.deepcopy(self.m);m['interface']['defaultPrompt'] = 'Build me a counter'
        with self.assertRaises(ValueError):validate_guidance_contract(ROOT,m)

    def test_undeclared_services_are_rejected(self):
        for field in ('apps','hooks','id'):
            with self.subTest(field=field):
                m = copy.deepcopy(self.m); m[field] = './old-config.json'
                with self.assertRaises(ValueError): validate_listing_contract(m)
        from check_package import validate_web_contract
        m=copy.deepcopy(self.m);m['mcpServers']='./old-config.json'
        with self.assertRaises(ValueError): validate_web_contract(ROOT,m)

    def test_extra_discoverable_mcp_file_fails_package_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)/'copy'; shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('__pycache__','*.pyc','LogReport.zip'))
            (root/'.mcp.json').write_text('{"mcpServers":{}}',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'approved stateless read-only endpoint'): validate(root)

    def test_ui_server_pack_is_absent_not_just_disabled(self):
        for rel in ('Program', 'mcp.json', '.app.json', 'hooks',
                    'skills/build/scripts/tests/test_sidebar.py',
                    'skills/build/Automation/UI71.py',
                    'skills/build/Automation/UV31.png'):
            self.assertFalse((ROOT/rel).exists(),rel)

    def test_migration_notes_do_not_request_destructive_account_changes(self):
        d = (AUTO/'NT64.md').read_text(encoding='utf-8')
        self.assertIn('Upload new version',d)
        self.assertIn('Do not uninstall or replace the old entry',d)
        self.assertIn('requires live verification',d)
        self.assertIn('Do not alter shared connectors',d)
        self.assertFalse(read_json(AUTO/'EB25.json')['account_operation_performed'])

    def test_contract_reports_native_rendering_as_untested(self):
        d = validate_listing_contract(self.m)
        self.assertEqual(d['account_rendering'],'not_tested')
        self.assertTrue(d['server_connection_required'])
        self.assertFalse(d['native_heading_modified'])
        e = validate_guidance_contract(ROOT,self.m)['entry_hint']
        self.assertEqual(e['mechanism'],'documented_optional_starter_and_plugin_info_page')
        self.assertFalse(e['editable_prompt_text'])
        self.assertFalse(e['selection_event_handled'])

    def test_short_chip_only_is_welcome_without_build_authority(self):
        for value in ('Build_', '  Build_  ', 'BUILD_'):
            r = guidance(value)
            self.assertEqual(r['route'],'welcome')
            self.assertFalse(r['build_authorized'])
            self.assertFalse(r['state_changed'])

    def test_old_long_chip_does_not_swallow_new_task(self):
        for prefix in (COMPOSER_LABEL,LEGACY_LABEL):
            for task in ('Build a timer','Help me build a timer','Add a /help button'):
                r = guidance(prefix+' '+task)
                self.assertFalse(r['handled'])
                self.assertEqual(r['route'],'conversation')

    def test_explicit_help_still_works_after_current_chip(self):
        for prefix in ('',COMPOSER_LABEL+' '):
            r = guidance(prefix+'/help')
            self.assertEqual(r['route'],'help')
            self.assertFalse(r['state_changed'])

    def test_only_newline_separated_usage_not_an_executable_resource(self):
        d = self.ui['longDescription']
        self.assertNotIn('http://',d)
        self.assertNotIn('https://',d)
        self.assertNotIn('ui://',d)
        self.assertEqual(set(self.m['extensions']['com.openai']),{'onboardingSkill','publication','review'})

    def test_source_instructions_do_not_open_retired_guide(self):
        s = (ROOT/'skills/build/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('Do not call iteration_welcome or iteration_guide',s)
        self.assertIn('metadata is not part of the user',s)
        self.assertIn('Selection without submission is not an executable event',s)
        self.assertIn('The plugin info page uses shortDescription',s)

    def test_root_readme_links_resolve_inside_the_package(self):
        text = (ROOT/'readme.md').read_text(encoding='utf-8')
        refs = re.findall(r'\]\(([^)]+)\)',text)
        self.assertGreaterEqual(len(refs),1)
        for ref in refs:
            p = (ROOT/ref).resolve()
            p.relative_to(ROOT.resolve())
            self.assertTrue(p.is_file(),ref)
