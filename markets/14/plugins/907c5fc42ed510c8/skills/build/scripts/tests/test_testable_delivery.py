"""Complete original-engine delivery with explicit unperformed runtime checks."""
from __future__ import annotations
import base64
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

from deliver import deliver
from iteration.engine import Engine
from iteration.layout import INDEX, RUNNER, audit_archive
from iteration.records import LAUNCHER
from iteration.release_contract import LIFECYCLE, PLAN, RECEIPT, validate_receipt
from iteration.safety import IterationError, read_archive, sha
from iteration import runner_template, lifecycle_template
from fixture_support import rewrite_archive
from test_qualified_delivery import CLI_SOURCE, full_plan


GUI_SOURCE = '''import tkinter as tk
from Automation.RT42 import ready
root = tk.Tk()
root.title('Isolated display fixture')
tk.Label(root, text='Fixture').pack()
root.update_idletasks()
ready()
root.mainloop()
'''
REASON = 'GUI interaction and native Windows launch were not run in this host.'


class WindowsTestableDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='build testable delivery ')
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root/'state')

    def tearDown(self):
        self.engine.close()
        self.temp.cleanup()

    def build(self, source=GUI_SOURCE, plan=None):
        project = self.engine.create_project('Original-engine test fixture')
        task = self.engine.begin(project['id'], 0, 'Build a disposable delivery fixture')
        self.engine.write_files(task['id'], 0, [{'path': 'PROGRAM/main.py', 'content': source}])
        revision = 1
        if plan is not None:
            self.engine.configure_checks(task['id'], revision, plan)
            revision += 1
        self.engine.report(task['id'], revision, REASON, 'not_run', 'Disposable test host')
        build = self.engine.package(task['id'], revision, 'Complete fixture source',
                                    ['Source and original diagnostic runtime included'],
                                    [REASON], ['Run the principal action on Windows'])
        _, raw = self.engine.archive_bytes(build['id'])
        return project, build, raw

    def export(self, build, name='windows-testable.zip', reasons=None):
        output = self.root/name
        result = deliver(self.engine, build['id'], output, mode='windows-testable',
                         unverified_reasons=[REASON] if reasons is None else reasons)
        return result, output

    def test_no_display_or_test_plan_is_required_and_application_is_not_executed(self):
        project, build, original = self.build()
        with patch.dict(os.environ, {'DISPLAY': '', 'WAYLAND_DISPLAY': ''}), \
             patch('deliver.qualify', side_effect=AssertionError('GUI qualification must not run')):
            result, output = self.export(build)
        self.assertEqual(result['status'], 'delivered_for_windows_test')
        self.assertFalse(result['runtime_qualified'])
        self.assertFalse(result['windows_bat_tested'])
        self.assertIsNone(result['portable_receipt'])
        self.assertEqual(result['unverified_checks'], [REASON])
        self.assertEqual(output.read_bytes(), original)
        self.assertEqual(result['archive_sha256'], sha(original))
        files = read_archive(original)
        self.assertNotIn(PLAN, files)
        self.assertNotIn(RECEIPT, files)
        self.assertEqual({name.split('/')[0] for name in files}, {'run.bat', 'PROGRAM'})
        self.assertEqual(files['run.bat'], LAUNCHER.encode('utf-8'))
        self.assertEqual(files[RUNNER], Path(runner_template.__file__).read_bytes())
        self.assertEqual(files[LIFECYCLE], Path(lifecycle_template.__file__).read_bytes())
        self.assertIn(REASON, files['PROGRAM/Automation/VT83.json'].decode())
        audit_archive(output.read_bytes())
        state = self.engine.resume(project['id'])
        self.assertIsNone(state['project']['accepted'])
        self.assertEqual(state['builds'][0]['delivery']['archive_sha256'], sha(original))
        self.assertNotIn('release', state['builds'][0])
        self.assertNotIn('only its passed exact-archive output', state['continuation_prompt'])
        self.assertIn('--mode windows-testable', state['continuation_prompt'])
        artifact = self.engine.artifact(project['id'], build['id'])
        self.assertEqual(artifact['delivery_status'], 'delivered_for_windows_test')
        self.assertEqual(artifact['release_status'], 'delivered_for_windows_test')
        self.assertFalse(artifact['runtime_qualified'])

    def test_unverified_reason_is_required(self):
        _, build, _ = self.build()
        for reasons in ([], [''], ['   ']):
            with self.subTest(reasons=reasons), self.assertRaises(IterationError) as caught:
                self.export(build, reasons=reasons)
            self.assertEqual(caught.exception.code, 'unverified_reason_required')
        self.assertFalse((self.root/'windows-testable.zip').exists())

    def test_failed_source_and_actual_failed_test_are_not_packaged(self):
        for source, failed_report, code in (
            ('def broken(:\n', False, 'checks_failed'),
            (CLI_SOURCE, True, 'runtime_checks_failed'),
        ):
            with self.subTest(code=code):
                project = self.engine.create_project('Failure fixture')
                task = self.engine.begin(project['id'], 0, 'Exercise real rejection')
                self.engine.write_files(task['id'], 0, [{'path': 'PROGRAM/main.py', 'content': source}])
                if failed_report:
                    self.engine.report(task['id'], 1, 'The actual action returned the wrong result.',
                                       'failed', 'Disposable test host')
                with self.assertRaises(IterationError) as caught:
                    self.engine.package(task['id'], 1, 'Blocked fixture', [], [], ['Try fixture'])
                self.assertEqual(caught.exception.code, code)

    def test_failed_qualification_cannot_be_relabelled_as_unperformed(self):
        _, build, _ = self.build('pass\n', full_plan())
        failed = deliver(self.engine, build['id'], self.root/'failed.zip', allow_execute=True)
        self.assertEqual(failed['status'], 'blocked')
        with self.assertRaises(IterationError) as caught:
            self.export(build)
        self.assertEqual(caught.exception.code, 'qualification_failure_requires_review')
        self.assertFalse((self.root/'windows-testable.zip').exists())

    def test_changed_runtime_templates_are_rejected_even_with_rehashed_manifest(self):
        _, build, original = self.build()
        files = read_archive(original)
        for path in ('run.bat', RUNNER, LIFECYCLE):
            altered = rewrite_archive(original, {path: files[path]+b'\n'})
            with self.subTest(path=path), \
                 patch.object(self.engine, 'archive_bytes', return_value=(build, altered)), \
                 self.assertRaises(IterationError) as caught:
                self.export(build)
            self.assertEqual(caught.exception.code, 'runtime_template_mismatch')
        self.assertFalse((self.root/'windows-testable.zip').exists())

    def test_corrupted_stored_archive_is_not_exported(self):
        _, build, original = self.build()
        (self.engine.store.exports/(build['id']+'.zip')).write_bytes(original+b'corruption')
        with self.assertRaises(IterationError) as caught:
            self.export(build)
        self.assertEqual(caught.exception.code, 'artifact_corrupt')

    def test_existing_output_and_symlinks_are_not_overwritten(self):
        _, build, _ = self.build()
        existing = self.root/'existing.zip'
        existing.write_bytes(b'KEEP')
        with self.assertRaises(IterationError) as caught:
            self.export(build, 'existing.zip')
        self.assertEqual(caught.exception.code, 'output_exists')
        self.assertEqual(existing.read_bytes(), b'KEEP')
        target = self.root/'target.zip'
        link = self.root/'linked.zip'
        link.symlink_to(target)
        with self.assertRaises(IterationError) as caught:
            self.export(build, 'linked.zip')
        self.assertEqual(caught.exception.code, 'output_exists')
        self.assertFalse(target.exists())
        directory = self.root/'real-parent'
        directory.mkdir()
        parent_link = self.root/'parent-link'
        parent_link.symlink_to(directory, target_is_directory=True)
        with self.assertRaises(IterationError) as caught:
            self.export(build, 'parent-link/output.zip')
        self.assertEqual(caught.exception.code, 'unsafe_output')
        self.assertEqual(list(directory.iterdir()), [])

    def test_original_supervisor_report_matches_the_testable_archive(self):
        _, build, _ = self.build(CLI_SOURCE)
        _, output = self.export(build)
        work = self.root/'actual runtime'
        work.mkdir()
        with zipfile.ZipFile(output) as archive:
            archive.extractall(work)
        process = subprocess.run([sys.executable, str(work/RUNNER)], cwd=work,
                                 capture_output=True, timeout=15)
        self.assertEqual(process.returncode, 0, process.stderr.decode(errors='replace'))
        report = self.engine.ingest_log_report(
            base64.b64encode((work/'LogReport.zip').read_bytes()).decode())
        self.assertTrue(report['report']['manifest_matches_known_build'])
        self.assertTrue(report['report']['application_ready_reported'])
        self.assertFalse(report['accepted_automatically'])

    def test_delivered_preview_is_a_real_continuation_baseline(self):
        project, build, _ = self.build(CLI_SOURCE)
        self.export(build)
        task = self.engine.begin(project['id'], 1, 'Continue the delivered application',
                                 base_build_id=build['id'])
        with self.assertRaises(IterationError) as caught:
            self.engine.configure_checks(task['id'], 0, full_plan())
        self.assertEqual(caught.exception.code, 'plan_context_mismatch')
        plan = full_plan()
        plan['continuation'] = True
        result = self.engine.configure_checks(task['id'], 0, plan)
        self.assertTrue(result['plan']['continuation'])

    def test_fresh_import_preserves_source_and_test_limitations(self):
        _, build, _ = self.build(CLI_SOURCE)
        _, output = self.export(build)
        other = Engine(self.root/'fresh state')
        try:
            imported = other.import_zip('Recovered testable fixture', output.read_bytes())
            self.assertTrue(imported['packaged'])
            recovered = other.read_file(imported['project']['id'], imported['build']['id'], 'PROGRAM/main.py')
            self.assertEqual(recovered['content'], CLI_SOURCE)
            self.assertIsNone(other.resume(imported['project']['id'])['project']['accepted'])
            self.assertEqual(imported['build']['imported_archive_sha256'], sha(output.read_bytes()))
        finally:
            other.close()

    def test_existing_qualified_archive_keeps_its_real_receipt_on_reexport(self):
        _, build, _ = self.build(CLI_SOURCE, full_plan())
        qualified_output = self.root/'qualified.zip'
        qualified = deliver(self.engine, build['id'], qualified_output, allow_execute=True)
        self.assertEqual(qualified['status'], 'passed')
        result, output = self.export(build)
        self.assertTrue(result['runtime_qualified'])
        self.assertEqual(output.read_bytes(), qualified_output.read_bytes())
        validate_receipt(read_archive(output.read_bytes()))

    def test_later_qualification_cannot_replace_a_delivered_preview_identity(self):
        _, build, original = self.build(CLI_SOURCE, full_plan())
        _, output = self.export(build)
        with patch('deliver.qualify', side_effect=AssertionError('Do not execute before preserving delivery identity')), \
             self.assertRaises(IterationError) as caught:
            deliver(self.engine, build['id'], self.root/'replacement.zip', allow_execute=True)
        self.assertEqual(caught.exception.code, 'delivered_archive_immutable')
        self.assertEqual(output.read_bytes(), original)
        _, current = self.engine.archive_bytes(build['id'])
        self.assertEqual(current, original)
        self.assertFalse((self.root/'replacement.zip').exists())

    def test_cli_exits_successfully_without_authorizing_application_execution(self):
        _, build, _ = self.build()
        script = Path(__file__).resolve().parents[1]/'deliver.py'
        output = self.root/'cli-testable.zip'
        process = subprocess.run([sys.executable, str(script), '--state', str(self.root/'state'),
                                  '--build-id', build['id'], '--output', str(output),
                                  '--mode', 'windows-testable', '--unverified-reason', REASON],
                                 capture_output=True, timeout=15)
        self.assertEqual(process.returncode, 0, process.stdout.decode(errors='replace'))
        result = json.loads(process.stdout)
        self.assertEqual(result['status'], 'delivered_for_windows_test')
        self.assertFalse(result['runtime_qualified'])
        self.assertEqual(sha(output.read_bytes()), result['archive_sha256'])


if __name__ == '__main__':
    unittest.main()
