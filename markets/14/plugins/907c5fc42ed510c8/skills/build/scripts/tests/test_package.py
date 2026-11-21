"""Release-specific format checks; cannot prove ChatGPT import or composer behaviour."""
from __future__ import annotations
import ast
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from check_package import ROOT, AUTO, SCRIPT, payload, read_json, validate
from iteration import BUILD, __version__
from iteration.mcp import INSTRUCTIONS, TOOLS
from iteration.runner_template import REMINDER


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.m=read_json(ROOT/'.codex-plugin/plugin.json')
        self.ui=self.m['interface']
        self.skill=(ROOT/'skills/build/SKILL.md').read_text(encoding='utf-8')

    def test_documented_compatibility_format_has_one_manifest(self):
        self.assertFalse((ROOT/'plugin.json').exists())
        self.assertEqual(self.m['skills'],'./skills/')
        manifests=[rel for rel,_ in payload(ROOT) if rel.endswith('/plugin.json') or rel=='plugin.json']
        self.assertEqual(manifests,['.codex-plugin/plugin.json'])

    def test_version_and_identity(self):
        self.assertEqual((BUILD,__version__),('B005','0.5.0'))
        self.assertEqual(self.m['version'],'0.8.6')
        self.assertEqual(self.m['name'],'berrer-build-mcp')
        self.assertNotIn('id',self.m)

    def test_label_is_exactly_build_underscore(self):
        self.assertEqual(self.ui['displayName'],'Build_')
        self.assertEqual(self.ui['displayName'].count(':'),0)

    def test_documented_first_use_starter(self):
        self.assertEqual(self.ui.get('defaultPrompt'), ['Press Enter to begin'])
        self.assertNotIn('default_prompt',self.ui)
        self.assertNotIn('Build_ Build a simple counter',self.skill)

    def test_one_remote_read_only_mcp_declared(self):
        for field in ('apps','hooks'):
            self.assertNotIn(field,self.m)
        self.assertEqual(self.m['mcpServers'],'./.mcp.json')
        self.assertTrue((ROOT/'.mcp.json').exists())
        for file in ('mcp.json','.app.json'):
            self.assertFalse((ROOT/file).exists())

    def test_no_root_level_standalone_application(self):
        self.assertFalse((ROOT/'Program').exists())
        self.assertFalse((ROOT/'Run.bat').exists())
        self.assertEqual({rel.split('/')[0] for rel,_ in payload(ROOT)},
                         {'.codex-plugin','skills','assets','readme.md','.mcp.json'})

    def test_native_and_generated_zip_contracts_remain_distinct(self):
        self.assertIn('exactly run.bat and PROGRAM/',self.skill)
        self.assertIn('PROGRAM/Automation',self.skill)
        self.assertIn('LogReport.zip beside run.bat',self.skill)

    def test_maintenance_records_are_coded(self):
        for name in ('AB60.json','CP74.md','LN32.md','SX18.md','QD47.md',
                     'VT83.json','RK26.md','MJ59.jsonl','EB25.json','NT64.md','DS38.md','NK24.md'):
            self.assertTrue((AUTO/name).is_file(),name)
        for obsolete in ('HandOff','Locked In','Brainstorming'):
            self.assertFalse((ROOT/obsolete).exists())

    def test_installation_policy_never_claims_mutation(self):
        note=read_json(AUTO/'EB25.json')
        self.assertFalse(note['new_identity_allowed_with_user_authorization'])
        self.assertFalse(note['account_operation_performed'])
        self.assertFalse(note['automatic_uninstall'])
        self.assertFalse(note['publish'])
        self.assertNotIn('target_plugin_id',note)
        self.assertTrue(note['preserve_existing_identity'])
        self.assertEqual(note['current_mode'],'update_existing_web_plugin')

    def test_no_stale_account_target_in_distribution(self):
        old='Plugin_'+'01ebf4d2e5e08191a052a4a07b1ad4e3'
        for rel,path in payload(ROOT):
            if path.suffix in ('.md','.json','.jsonl'):
                self.assertNotIn(old,path.read_text(encoding='utf-8'),rel)
        note=(AUTO/'NT64.md').read_text(encoding='utf-8')
        self.assertNotIn('SAME Plugin Creator chat',note)
        self.assertNotIn('preserve that identity',note.lower())

    def test_blank_activation_is_not_build_authorization(self):
        self.assertIn('No typed prefix is required.',self.skill)
        self.assertIn('not permission to\nbuild anything',self.skill)
        self.assertIn('do not invent a project',self.skill) if 'do not invent a project' in self.skill else self.assertIn('not permission to\nbuild anything',self.skill)
        self.assertIn('For delivery, remind the', self.skill)
        self.assertIn('For brainstorming and welcome', self.skill)

    def test_asset_metadata_limits(self):
        for field,limit in [('displayName',30),('shortDescription',240),('longDescription',4000),('developerName',80)]:
            self.assertTrue(self.ui[field]); self.assertLessEqual(len(self.ui[field]),limit)
        self.assertEqual(self.ui['category'],'Developer Tools')
        self.assertLessEqual(len(self.ui['capabilities']),20)
        for field in ('composerIcon','logo'):
            self.assertTrue(self.ui[field].startswith('./assets/'))
            self.assertTrue((ROOT/self.ui[field]).is_file())

    def test_brand_colour_meets_reference_contrast(self):
        hexa=self.ui['brandColor'].lstrip('#')
        vals=[int(hexa[i:i+2],16)/255 for i in (0,2,4)]
        lum=sum(w*(v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4)
                for w,v in zip((.2126,.7152,.0722),vals))
        self.assertGreaterEqual(1.05/(lum+.05),2)

    def test_local_validator(self):
        data=validate()
        self.assertEqual(data['integrity'],'matched')
        self.assertTrue(data['starter_prompt_supplied'])
        self.assertEqual(data['account_installation'],'not_tested')

    def test_declared_unchanged_files_match_baseline(self):
        inventory=read_json(AUTO/'AB60.json')
        for rel,digest in inventory['unchanged_baseline_files_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),digest,rel)

    def test_every_python_source_supports_310_syntax(self):
        for rel,path in payload(ROOT):
            if path.suffix=='.py':
                ast.parse(path.read_text(encoding='utf-8'),filename=rel,feature_version=(3,10))

    def test_optional_bat_is_local_checker_only(self):
        bat=(SCRIPT/'Run.bat').read_bytes()
        self.assertIn(b'DisableDelayedExpansion',bat)
        self.assertIn(b'check_package.py --self-test',bat)
        self.assertIn(b'\r\n',bat)
        for forbidden in (b'curl ',b'powershell',b'pip install',b'http'):
            self.assertNotIn(forbidden,bat.lower())

    def test_cli_without_service(self):
        with tempfile.TemporaryDirectory() as temp:
            run=subprocess.run([sys.executable,str(SCRIPT/'iteration_cli.py'),'--state',temp,'status'],
                               capture_output=True,text=True,timeout=20,
                               env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
            self.assertEqual(run.returncode,0,run.stdout+run.stderr)
            s=json.loads(run.stdout)
            self.assertEqual(s['build'],'B005')
            self.assertEqual(s['version'],'0.5.0')
            self.assertFalse(s['chat_entry']['typed_prefix_required'])
            self.assertEqual(s['chat_entry']['starter_prompts'],[])
            self.assertEqual(s['reply_footer'],REMINDER)

    def test_mcp_does_not_claim_account_control(self):
        self.assertIn('alone is not permission to build',INSTRUCTIONS)
        self.assertIn(REMINDER,INSTRUCTIONS)
        self.assertFalse(any('install' in t['name'] or 'shell' in t['name'] for t in TOOLS))
