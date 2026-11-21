"""Read-only guidance, manifest wiring, and the optional first-use starter contract.

Local tests exercise the helper and packaged instructions, NOT live LLM routing or
ChatGPT's account-side onboarding. Those need an installed conversation test.
"""
from __future__ import annotations
import ast
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import guide
from check_package import ROOT, AUTO, SCRIPT, read_json, validate_guidance_contract
from iteration.runner_template import REMINDER


class GuidanceTests(unittest.TestCase):
    def test_slash_help_returns_bundled_copy(self):
        r = guide.guidance('/help')
        self.assertEqual(r['route'], 'help')
        self.assertEqual(r['text'], (AUTO/'HP12.md').read_text(encoding='utf-8').strip())
        self.assertFalse(r['build_authorized'])
        self.assertFalse(r['state_changed'])

    def test_help_aliases_are_full_message_and_case_insensitive(self):
        for message in ('help', 'HELP', ' /help ', 'help please', 'show help',
                        'How do I use Build_?', 'How do I get started?',
                        'What can you do?', 'Build_ /help'):
            with self.subTest(message=message):
                self.assertEqual(guide.guidance(message)['route'], 'help')

    def test_blank_chip_and_greeting_use_short_welcome(self):
        for message in ('', '  ', 'Build_', 'Hi', 'hello!', 'get started', 'Press Enter to begin'):
            with self.subTest(message=message):
                self.assertEqual(guide.guidance(message)['route'], 'welcome')

    def test_repeated_blank_does_not_repeat_welcome(self):
        r = guide.guidance('', already_welcomed=True)
        self.assertEqual(r['route'], 'ask')
        self.assertNotIn('Welcome to Build_', r['text'])
        self.assertEqual(r['text'], 'What would you like to build or change?')

    def test_explicit_help_can_be_repeated(self):
        self.assertEqual(guide.guidance('/help', already_welcomed=True)['route'], 'help')

    def test_unselected_plugin_does_not_handle_greetings_or_help(self):
        for msg in ('', 'hi', '/help', 'what can you do'):
            self.assertFalse(guide.guidance(msg, selected=False)['handled'])

    def test_real_requests_are_not_swallowed_by_help_keyword(self):
        for msg in ('Help me build a timer', 'Add a /help button', 'Fix the help window', 'Press Enter to begin building a timer',
                    'Build a helpdesk app', 'Hello, make a CSV cleaner',
                    'Build_ build a counter', '/help then build a timer',
                    'Please help me fix the attached report',
                    'Can you help me understand this failure?'):
            with self.subTest(message=msg):
                r = guide.guidance(msg)
                self.assertFalse(r['handled'])
                self.assertFalse(r['build_authorized'])
                self.assertIsNone(r['text'])

    def test_quoted_code_urls_and_file_paths_are_not_commands(self):
        for msg in ('"/help"', '`/help`', 'print("/help")', 'https://example.test/help',
                    '/help/file.txt', '../HP12.md', 'C:\\help', 'Log says: /help'):
            self.assertFalse(guide.guidance(msg)['handled'])

    def test_unknown_command_does_not_execute_or_echo_content(self):
        r = guide.guidance('/delete everything; password=private')
        self.assertFalse(r['handled'])
        self.assertNotIn('password', json.dumps(r))
        self.assertFalse(r['build_authorized'])

    def test_help_reads_only_the_fixed_help_resource(self):
        with patch.object(Path, 'read_text', return_value='Guidance\n\n'+REMINDER) as read:
            self.assertEqual(guide.guidance('/help')['route'], 'help')
            read.assert_called_once_with(encoding='utf-8')

    def test_invalid_message_type_size_or_flags_refused(self):
        for msg in (None, 7, [], 'a'*16001):
            with self.assertRaises(ValueError): guide.guidance(msg)
        with self.assertRaises(ValueError): guide.guidance('help', already_welcomed='yes')
        with self.assertRaises(ValueError): guide.guidance('help', selected=1)

    def test_missing_guidance_is_error_not_fabricated_setup_success(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(guide, 'AUTO', Path(tmp)):
            with self.assertRaises(OSError): guide.guidance('/help')

    def test_incomplete_guidance_is_rejected(self):
        with patch.object(Path, 'read_text', return_value='Missing guidance'):
            with self.assertRaises(ValueError): guide.guidance('help')
            with self.assertRaises(ValueError): guide.guidance('Press Enter to begin')

    def test_short_user_copy_hides_internal_methodology(self):
        for name, limit in (('WC23.md',100), ('HP12.md',240)):
            text=(AUTO/name).read_text(encoding='utf-8')
            self.assertLessEqual(len(text.split()),limit)
            for label in ('Automation/', 'brainstorm', 'handoff', 'locked in', 'AB60'):
                self.assertNotIn(label,text.lower() if label.islower() else text)
            self.assertIn('LogReport.zip',text)
            if name=='WC23.md':self.assertTrue(text.rstrip().rstrip('*').endswith('What would you like to make?'))

    def test_privacy_source_recovery_and_no_commands_requirement_are_clear(self):
        help_text=guide.guidance('help')['text']
        self.assertIn('Nothing uploads automatically',help_text)
        self.assertIn('not a replacement for the program ZIP',help_text)
        self.assertIn('without changing your program',help_text)
        self.assertIn('What would you like to make?',guide.guidance('')['text'])

    def test_guide_has_no_build_engine_network_or_subprocess_import(self):
        tree=ast.parse((SCRIPT/'guide.py').read_text(encoding='utf-8'))
        imports=[]
        for n in ast.walk(tree):
            if isinstance(n,ast.Import): imports.extend(a.name for a in n.names)
            elif isinstance(n,ast.ImportFrom): imports.append(n.module)
        self.assertTrue(set(imports)<= {'__future__','argparse','json','re','sys','pathlib'})

    def run_local_preview(self, arguments, state_exists):
        with tempfile.TemporaryDirectory(prefix='iterate guidance with spaces ') as tmp:
            work=Path(tmp);state=work/'protected state';outputs=work/'outputs';outputs.mkdir()
            if state_exists:
                state.mkdir();(state/'records.json').write_bytes(b'{"unchanged":true}')
            (outputs/'customer.zip').write_bytes(b'not to be read or changed')
            (outputs/'LogReport.zip').write_bytes(b'private report sentinel')
            def snapshot():
                return {p.relative_to(work).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in work.rglob('*') if p.is_file()}
            before=snapshot(); dirs_before={p.relative_to(work) for p in work.rglob('*') if p.is_dir()}
            env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','ITERATION_STATE_DIR':str(state),
                 'ITERATION_TEST_DATA_DIR':str(outputs),'API_KEY':'private-test-sentinel'}
            p=subprocess.run([sys.executable,'-B',str(SCRIPT/'guide.py'),*arguments],
                             cwd=work,env=env,capture_output=True,text=True,timeout=10)
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            self.assertEqual(before,snapshot())
            self.assertEqual(dirs_before,{p.relative_to(work) for p in work.rglob('*') if p.is_dir()})
            self.assertNotIn('private-test-sentinel',p.stdout+p.stderr)
            self.assertFalse((work/'LogReport.zip').exists())
            return p.stdout

    def test_help_with_existing_project_and_reports_has_no_disk_side_effect(self):
        r=json.loads(self.run_local_preview(['--message','/help','--json'],True))
        self.assertEqual(r['route'],'help')

    def test_welcome_does_not_create_state(self):
        text=self.run_local_preview(['--welcome'],False)
        self.assertIn('Welcome to Build_',text)

    def test_normal_request_does_not_auto_create_project_in_preview(self):
        r=json.loads(self.run_local_preview(['--message','Help me build a counter','--json'],False))
        self.assertFalse(r['handled'])


class OnboardingPackageTests(unittest.TestCase):
    def setUp(self):
        self.m=read_json(ROOT/'.codex-plugin/plugin.json')
        self.skill=(ROOT/'skills/build/SKILL.md').read_text(encoding='utf-8')
        self.setup=(ROOT/'skills/build-start/SKILL.md').read_text(encoding='utf-8')

    def test_manifest_uses_documented_root_extension(self):
        info=validate_guidance_contract(ROOT,self.m)
        self.assertEqual(info['onboarding_skill'],'./skills/build-start/SKILL.md')
        self.assertNotIn('onboardingSkill',self.m['interface'])
        self.assertEqual(info['host_setup_invocation'],'not_tested')

    def test_exact_documented_starter_and_no_fake_composer_controls(self):
        self.assertEqual(self.m['interface']['defaultPrompt'], ['Press Enter to begin'])
        for field in ('default_prompt','placeholder','composerPlaceholder','onFocus','onClick'):
            self.assertNotIn(field,self.m)
            self.assertNotIn(field,self.m['interface'])
        self.assertEqual(self.m['interface']['displayName'],'Build_')

    def test_bad_or_external_onboarding_references_are_rejected(self):
        for ref in ('../outside/SKILL.md','/absolute/SKILL.md','https://example.test/SKILL.md',
                    './skills/../outside/SKILL.md','./skills/missing/SKILL.md',None,{}):
            m=copy.deepcopy(self.m);m['extensions']['com.openai']['onboardingSkill']=ref
            with self.assertRaises(ValueError):validate_guidance_contract(ROOT,m)

    def test_fake_placeholder_field_is_rejected(self):
        m=copy.deepcopy(self.m);m['interface']['placeholder']='Type /help'
        with self.assertRaises(ValueError):validate_guidance_contract(ROOT,m)

    def test_misnested_onboarding_and_unapproved_extensions_are_rejected(self):
        m=copy.deepcopy(self.m);m['interface']['onboardingSkill']=m.pop('extensions')
        with self.assertRaises(ValueError):validate_guidance_contract(ROOT,m)
        m=copy.deepcopy(self.m);m['extensions']['com.openai']['onFocus']='welcome'
        with self.assertRaises(ValueError):validate_guidance_contract(ROOT,m)

    def test_onboarding_skill_is_included_under_skills_root(self):
        paths=sorted(p.relative_to(ROOT).as_posix() for p in (ROOT/'skills').rglob('SKILL.md'))
        self.assertEqual(paths,['skills/build-start/SKILL.md','skills/build/SKILL.md'])
        front=self.setup.split('---',2)
        self.assertIn('name: build-start',front[1])
        self.assertLessEqual(len(front[1]),1024)

    def test_setup_preserves_typed_requests_and_never_claims_installation(self):
        for clause in ('Preserve any existing typed request', 'Do not infer successful installation',
                       'do not swallow it', 'Do not generate a demo or archive',
                       'do not repeat it', 'never insert, clear, focus'):
            self.assertIn(clause,self.setup)
        self.assertIn('LogReport.zip',self.setup)

    def test_help_routing_precedes_production_tools(self):
        self.assertLess(self.skill.index('## Entry routing'),self.skill.index('use the installed host-local engine'))
        self.assertIn('Do not call status/projects/resume',self.skill)
        self.assertIn('do not require\nPython execution for help',self.skill)
        self.assertIn('not a registered native ChatGPT slash command',self.skill)
        self.assertIn('Add a /help button',self.skill)

    def test_only_optional_remote_read_only_mcp_with_no_account_binding(self):
        for field in ('apps','hooks','id'):
            self.assertNotIn(field,self.m)
        self.assertEqual(self.m['mcpServers'],'./.mcp.json')
        self.assertTrue((ROOT/'.mcp.json').exists())

    def test_core_release_files_match_preserved_or_brand_only_provenance(self):
        provenance=read_json(AUTO/'AB60.json')
        index={**provenance['production_files_sha256'], **provenance['branding_only_files_sha256']}
        names=['deliver.py','release_check.py','iteration_cli.py','Run.bat',
               'iteration/engine.py','iteration/runner_template.py','iteration/lifecycle_template.py',
               'iteration/records.py','iteration/release_contract.py','iteration/layout.py',
               'iteration/safety.py','iteration/store.py','iteration/logs.py']
        for name in names:
            rel='skills/build/scripts/'+name
            self.assertIn(rel,index)
            self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),index[rel])
