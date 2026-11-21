"""Generated-program runtime regression checks, not a native host-install test."""
from __future__ import annotations
import base64, io, os, subprocess, sys, tempfile, unittest, zipfile
from pathlib import Path
from iteration.engine import Engine
from iteration.logs import parse_log_report
from iteration.runner_template import REMINDER
from fixture_support import ready_source

class NativeRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='iteration-i004-native-')
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root/'state')
    def tearDown(self):
        self.engine.close(); self.temp.cleanup()

    def build(self, source):
        project = self.engine.create_project('Native package check', constraints=['Keep Python orchestration.'])
        task = self.engine.begin(project['id'],0,'Exercise the existing local report loop.')
        self.engine.write_files(task['id'],0,[{'path':'PROGRAM/main.py','content':source}])
        build = self.engine.package(task['id'],1,'Test fixture',['Fixture source'],['Windows GUI not tested'],['Run fixture'])
        _,raw = self.engine.archive_bytes(build['id'])
        return project,build,raw

    def run_fixture(self, source):
        project, build, raw = self.build(ready_source(source))
        folder = self.root/'generated'
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            self.assertEqual({p.split('/')[0] for p in archive.namelist()},{'run.bat','PROGRAM'})
            self.assertNotIn('LogReport.zip',archive.namelist())
            archive.extractall(folder)  # trusted engine-generated test fixture only
        process = subprocess.run([sys.executable,str(folder/'PROGRAM/Automation/ZP90.py')],
            capture_output=True,text=True,timeout=25,
            env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONUTF8':'1'})
        report_bytes=(folder/'LogReport.zip').read_bytes()
        report=parse_log_report(report_bytes)
        return project,build,process,report_bytes,report

    def test_generated_successful_run_produces_local_report(self):
        p,b,process,raw,report=self.run_fixture('print("I008 runtime fixture")\n')
        self.assertEqual(process.returncode,0,process.stdout+process.stderr)
        self.assertEqual(report['state'],'completed')
        self.assertEqual(report['exit_code'],0)
        self.assertEqual(report['build_id'],b['id'])
        self.assertIn('I008 runtime fixture',report['console'])
        self.assertIsNone(report['behavior_passed'])
        self.assertIn(REMINDER,process.stdout)
        self.engine.ingest_log_report(base64.b64encode(raw).decode('ascii'))
        self.assertIsNone(self.engine.resume(p['id'])['project']['accepted'])

    def test_generated_error_report_is_not_a_pass(self):
        _,_,process,_,report=self.run_fixture('raise SystemExit(7)\n')
        self.assertEqual(process.returncode,7)
        self.assertEqual(report['state'],'runtime_failed')
        self.assertEqual(report['exit_code'],7)
        self.assertIsNone(report['behavior_passed'])

    def test_generated_report_redacts_credential_lines(self):
        _,_,_,_,report=self.run_fixture('print("password=fixture-not-a-real-password")\n')
        self.assertNotIn('fixture-not-a-real-password',report['console'])
        self.assertIn('omitted',report['console'])

    def test_next_build_keeps_accepted_baseline_and_fresh_recovery(self):
        p,b,_=self.build('print("first")\n')
        approved=self.engine.accept_from_chat(p['id'],b['id'],1,'Keep this fixture as the test baseline.')
        state=self.engine.resume(p['id'])['project']
        task=self.engine.begin(p['id'],state['revision'],'One small next change.')
        self.engine.write_files(task['id'],0,[{'path':'PROGRAM/main.py','content':'print("second")\n'}])
        b2=self.engine.package(task['id'],1,'Second fixture',['Changed print'],['User test'],['Run it'])
        self.assertEqual(self.engine.resume(p['id'])['project']['accepted'],b['id'])
        _,raw=self.engine.archive_bytes(b2['id'])
        fresh=Engine(self.root/'fresh')
        try:
            recovered=fresh.import_zip('Recovered fixture',raw)
            self.assertTrue(recovered['packaged'])
            self.assertEqual(recovered['project']['constraints'],['Keep Python orchestration.'])
            self.assertIsNone(recovered['project']['accepted'])
        finally: fresh.close()
