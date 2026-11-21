"""B002: exercise the advertised loop through actual host-local command entrypoints.

The fixture is deliberately small and disposable. No customer application or model is
invoked; this verifies the machinery, not installed ChatGPT behavior or Windows BAT.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

from check_package import ROOT, AUTO, SCRIPT, read_json, validate_listing_contract
from iteration.layout import INDEX, RUNNER
from iteration.release_contract import validate_receipt
from iteration.safety import read_archive, sha
from test_qualified_delivery import full_plan

REFERENCE = 'Retain this approved reference: plain integer calculator, offline, no database.\n'
CONSTRAINTS = ['Offline only; no accounts or network.', 'Preserve the integer input range and reference asset.']
ARCHITECTURE = 'One bounded integer conversion function; Python launcher; stateless CLI.'
OPTIONS = 'Optional future suggestion: labels. This is not an approved feature.'


def application(factor: int) -> str:
    return '''from Automation.RT42 import ready, case
from pathlib import Path
import os
import sys
FACTOR = FACTOR_VALUE
MAXIMUM = 1000000
marker = os.environ.get('BUILD_IMPORT_EXEC_MARKER')
if marker:
    Path(marker).write_text('Executed', encoding='utf-8')
reference = (Path(__file__).parent / 'assets' / 'reference.txt').read_text(encoding='utf-8')
assert reference.startswith('Retain this approved reference:')
def convert(text):
    if not isinstance(text, str) or not text.isascii() or not text.isdecimal() or len(text) > 7:
        raise ValueError('Enter a whole number in range')
    value = int(text)
    if not 0 <= value <= MAXIMUM:
        raise ValueError('Number out of range')
    return value * FACTOR
if '--iteration-smoke-test' in sys.argv:
    with case('open', 'startup'):
        assert convert('8') == 8 * FACTOR
        assert reference.endswith('no database.\\n')
    ready()
    print('ITERATION_SMOKE_OK')
elif '--iteration-self-test' in sys.argv:
    with case('valid', 'primary'):
        assert convert('3') == 3 * FACTOR
    with case('invalid', 'invalid-input'):
        for value in ('', '-1', '1.2', 'letters', '１２'):
            try:
                convert(value)
            except ValueError:
                pass
            else:
                raise AssertionError('Invalid input accepted')
    with case('limit', 'boundary'):
        assert convert('0') == 0
        assert convert(str(MAXIMUM)) == MAXIMUM * FACTOR
        for value in (str(MAXIMUM + 1), '9' * 5000):
            try:
                convert(value)
            except ValueError:
                pass
            else:
                raise AssertionError('Oversized input accepted')
        assert convert('1') == FACTOR
    ready()
    print('ITERATION_SELF_TEST_OK')
else:
    result = convert('8')
    ready()
    print('VALUE=' + str(result))
'''.replace('FACTOR_VALUE', str(factor))


class ListedWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='build web guide workflow ')
        self.root = Path(self.temp.name)
        self.counter = 0
        self.env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')
        # A marker only belongs to the controlled import test, never inherited executions.
        self.env.pop('BUILD_IMPORT_EXEC_MARKER', None)

    def tearDown(self):
        self.temp.cleanup()

    def command(self, state, *arguments, extra_env=None):
        proc = subprocess.run([sys.executable, '-B', str(SCRIPT/'iteration_cli.py'),
                               '--state', str(state), *map(str, arguments)],
                              capture_output=True, text=True, timeout=25,
                              env={**self.env, **(extra_env or {})})
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        return json.loads(proc.stdout)

    def action(self, state, tool_name, **arguments):
        self.counter += 1
        path = self.root / ('request_%03d.json' % self.counter)
        path.write_text(json.dumps(arguments), encoding='utf-8')
        return self.command(state, 'call', tool_name, '--arguments', path)

    def stage(self, state, project_id, factor, base='', first=False):
        current = self.action(state, 'iteration_resume', project_id=project_id)['project']
        task = self.action(state, 'iteration_begin', project_id=project_id,
                           expected_revision=current['revision'],
                           intent=f'Use factor {factor}; preserve the integer contract and reference asset.',
                           scope_paths=['PROGRAM/'] if first else ['PROGRAM/main.py'],
                           not_changed=CONSTRAINTS,
                           acceptance_criteria=[f'Normal run returns VALUE={8 * factor}.',
                                                'Invalid input never changes valid behavior.'],
                           base_build_id=base)
        files = [{'path':'PROGRAM/main.py', 'content':application(factor)}]
        if first:
            files.append({'path':'PROGRAM/assets/reference.txt', 'content':REFERENCE})
        saved = self.action(state, 'iteration_write_files', task_id=task['id'],
                            expected_task_revision=task['revision'], files=files)
        plan = full_plan()
        plan['continuation'] = not first
        plan['cases'][0]['description'] = 'Run the real integer conversion path and load the preserved reference asset.'
        self.counter += 1
        plan_path = self.root / ('plan_%03d.json' % self.counter)
        plan_path.write_text(json.dumps(plan), encoding='utf-8')
        planned = self.command(state, 'plan', '--task-id', task['id'], '--revision',
                               saved['task_revision'], '--file', plan_path)
        staged = self.action(state, 'iteration_package', task_id=task['id'],
                             expected_task_revision=planned['task_revision'],
                             summary=f'Factor changed to {factor}; original input contract retained.',
                             completed=['Requested conversion and complete source packaged.'],
                             remaining=['Native Windows not tested.'],
                             what_to_test=[f'Run the program and check VALUE={8 * factor}.'],
                             architecture=ARCHITECTURE if first else '',
                             brainstorm=OPTIONS if first else '',
                             next_prompt='Review returned logs, then agree one bounded improvement.')
        output = self.root / ('release_%s.zip' % staged['id'])
        proc = subprocess.run([sys.executable, '-B', str(SCRIPT/'deliver.py'), '--state', str(state),
                               '--build-id', staged['id'], '--output', str(output), '--allow-execute'],
                              capture_output=True, text=True, timeout=90, env=self.env)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        qualified = json.loads(proc.stdout)
        self.assertEqual(qualified['status'], 'passed')
        self.assertEqual(sha(output.read_bytes()), qualified['archive_sha256'])
        self.assertFalse(qualified['windows_bat_tested'])
        files = read_archive(output.read_bytes())
        self.assertEqual({name.split('/')[0] for name in files}, {'run.bat','PROGRAM'})
        self.assertEqual(files['PROGRAM/main.py'].decode(), application(factor))
        self.assertEqual(files['PROGRAM/assets/reference.txt'].decode(), REFERENCE)
        self.assertEqual(json.loads(files[INDEX])['constraints'], CONSTRAINTS)
        self.assertEqual(validate_receipt(files)['status'], 'payload_qualified')
        self.assertIn(ARCHITECTURE, files['PROGRAM/Automation/SX18.md'].decode())
        self.assertIn(OPTIONS, files['PROGRAM/Automation/QD47.md'].decode())
        return staged, output

    def run_report(self, state, project_id, build_id, output, factor):
        destination = self.root / ('run_%s' % build_id)
        destination.mkdir()
        with zipfile.ZipFile(output) as archive:
            archive.extractall(destination)
        proc = subprocess.run([sys.executable, '-B', str(destination/RUNNER)],
                              capture_output=True, text=True, timeout=20, env=self.env,
                              cwd=destination)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report_path = destination/'LogReport.zip'
        self.assertTrue(report_path.is_file())
        before = self.action(state, 'iteration_resume', project_id=project_id)
        ingested = self.command(state, 'log', report_path)
        after = self.action(state, 'iteration_resume', project_id=project_id)
        report = ingested['report']
        self.assertEqual(report['build_id'], build_id)
        self.assertTrue(report['manifest_matches_known_build'])
        self.assertTrue(report['application_ready_reported'])
        self.assertEqual(report['state'], 'completed')
        self.assertIn('VALUE='+str(factor*8), report['console'])
        self.assertFalse(ingested['accepted_automatically'])
        self.assertEqual(before['project'], after['project'])
        self.assertEqual(before['active_tasks'], after['active_tasks'])
        self.assertEqual(len(before['builds']), len(after['builds']))
        return report_path

    def test_full_guide_loop_three_releases_and_fresh_chat_recovery(self):
        """Real CLI + delivery + supervised logs; fresh state has only the last ZIP/report."""
        first_state = self.root/'chat-a'
        p = self.action(first_state, 'iteration_create_project', name='LifecycleFixture',
                        description='Test fixture, not a bundled customer application.', constraints=CONSTRAINTS)
        b1, zip1 = self.stage(first_state, p['id'], 2, first=True)
        self.run_report(first_state, p['id'], b1['id'], zip1, 2)
        state = self.action(first_state, 'iteration_resume', project_id=p['id'])
        self.assertIsNone(state['project']['accepted'])
        self.action(first_state, 'iteration_accept', project_id=p['id'], build_id=b1['id'],
                    expected_revision=state['project']['revision'],
                    user_confirmation='I accept this exact fixture and authorize the next factor change.',
                    windows_tested=False)
        b2, zip2 = self.stage(first_state, p['id'], 3, base=b1['id'])
        log2 = self.run_report(first_state, p['id'], b2['id'], zip2, 3)
        state = self.action(first_state, 'iteration_resume', project_id=p['id'])
        self.assertEqual(state['project']['accepted'], b1['id'])
        packet = self.action(first_state, 'iteration_continue', project_id=p['id'])
        self.assertFalse(packet['chat_created'])
        self.assertFalse(packet['reasoning_changed'])
        original_hashes = {str(path):sha(path.read_bytes()) for path in (zip1,zip2,log2)}

        # Another isolated session with no state: imports actual latest bytes, not an app name.
        fresh = self.root/'chat-b'
        self.assertEqual(self.command(fresh, 'projects')['projects'], [])
        marker = self.root/'import-must-not-run-app.txt'
        imported = self.command(fresh, 'import', zip2,
                                extra_env={'BUILD_IMPORT_EXEC_MARKER':str(marker)})
        self.assertFalse(marker.exists())
        self.assertTrue(imported['packaged'])
        ip, ib = imported['project'], imported['build']
        self.assertEqual(ip['name'], 'LifecycleFixture')
        self.assertEqual(ib['imported_archive_sha256'], sha(zip2.read_bytes()))
        recovered = self.action(fresh, 'iteration_resume', project_id=ip['id'])
        self.assertEqual(recovered['project']['constraints'], CONSTRAINTS)
        self.assertIsNone(recovered['project']['accepted'])
        self.assertEqual(recovered['active_tasks'], [])
        returned = self.command(fresh, 'log', log2)
        self.assertEqual(returned['report']['build_id'], ib['id'])
        self.assertTrue(returned['report']['applies_to_imported_original_not_regenerated_launcher'])
        self.assertEqual(returned['report']['reported_original_identity']['build_id'], b2['id'])
        self.assertFalse(returned['accepted_automatically'])
        b3, zip3 = self.stage(fresh, ip['id'], 4, base=ib['id'])
        self.run_report(fresh, ip['id'], b3['id'], zip3, 4)
        for path, digest in original_hashes.items():
            self.assertEqual(sha(Path(path).read_bytes()), digest)

    def test_requested_subtitle_is_exact_and_public_limit_is_not_hidden(self):
        result = validate_listing_contract(read_json(ROOT/'.codex-plugin/plugin.json'))
        self.assertEqual(result['subtitle_characters'], 27)
        self.assertEqual(result['zip_upload_subtitle_limit'], 240)
        self.assertEqual(result['public_directory_subtitle_limit'], 30)
        self.assertTrue(result['public_directory_subtitle_ready'])
        self.assertIn('Public-directory', result['notice'])

    def test_developer_comment_is_not_customer_description(self):
        text = read_json(ROOT/'.codex-plugin/plugin.json')['interface']['longDescription']
        for phrase in ('This is what we need', 'make sure it works that way', 'last line', 'obviously',
                       'technically Live', 'working app guaranteed', 'never crashes'):
            self.assertNotIn(phrase.casefold(), text.casefold())
        self.assertTrue(text.startswith('Describe an app'))
        self.assertIn('when you approve a proposed build'.casefold(), text.casefold())

    def test_guide_and_skill_make_review_read_only_and_recovery_explicit(self):
        contract = (AUTO/'FR72.md').read_text()
        skill = (ROOT/'skills/build/SKILL.md').read_text()
        self.assertIn('A returned LogReport.zip is feedback', skill)
        self.assertIn('import and inspect that exact archive', skill)
        self.assertIn('Never re-ask something the user already', skill)
        self.assertIn('Logs without registered source', contract)
        self.assertIn('No lengthy rebrief', contract)
        self.assertIn('not plugin automation', skill)
        self.assertIn('explicit WIP request', skill)

    def test_production_runtime_and_delivery_files_match_current_inventory(self):
        """Check tested current files; do not confuse original 0.7 hashes with later migration."""
        meta = read_json(AUTO/'AB60.json')
        current = meta['production_files_sha256']
        self.assertGreaterEqual(len(current), 14)
        for name, digest in current.items():
            with self.subTest(path=name):
                self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(), digest)
        self.assertEqual(meta['public_candidate']['version'],'0.8.6')
        self.assertEqual(meta['public_candidate']['starter_prompt'],'Press Enter to begin')

    def test_update_plan_keeps_the_installed_web_entry(self):
        meta = read_json(AUTO/'EB25.json')
        self.assertEqual(meta['current_mode'], 'update_existing_web_plugin')  # historical v0.7 private record
        self.assertTrue(meta['preserve_existing_identity'])
        self.assertFalse(meta['new_identity_allowed_with_user_authorization'])
        self.assertFalse(meta['account_operation_performed'])
        self.assertEqual(meta['apps'], [])
        self.assertEqual(meta['servers'], [])
        manifest = read_json(ROOT/'.codex-plugin/plugin.json')
        self.assertEqual(manifest['name'], 'berrer-build-mcp')
        self.assertEqual(manifest['interface']['displayName'], 'Build_')
        self.assertEqual(manifest['interface'].get('defaultPrompt'), ['Press Enter to begin'])
