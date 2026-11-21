"""Actual old-source fixture production and gate association, with no customer data."""
from __future__ import annotations
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from iteration.engine import Engine
from iteration.safety import IterationError,sha
from release_check import qualify
from deliver import deliver
from test_application_cases import JSON_SOURCE
from test_qualified_delivery import full_plan


class PriorVersionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='iteration-prior-')
        self.root=Path(self.temp.name);self.engine=Engine(self.root/'state')
        p=self.engine.create_project('Prior source fixture');t=self.engine.begin(p['id'],0,'Create an old saved-state emitter fixture')
        source="from pathlib import Path\nimport os,json\np=Path(os.environ['ITERATION_TEST_DATA_DIR']);p.mkdir(parents=True,exist_ok=True)\n(p/'settings.json').write_text(json.dumps({'version':1,'count':17}),encoding='utf-8')\n"
        self.engine.write_files(t['id'],0,[{'path':'Program/main.py','content':source}])
        old=self.engine.package(t['id'],1,'Old emitter fixture',[],[],['Use disposable fixture state'])
        _,raw=self.engine.archive_bytes(old['id'])
        self.previous=self.root/'previous.zip';self.previous.write_bytes(raw)
        # Execute the actual old source to produce the fixture, not a guessed schema.
        emitter=self.root/'emitter.py';emitter.write_text(source)
        data=self.root/'old-state'
        subprocess.run([sys.executable,str(emitter)],env={**os.environ,'ITERATION_TEST_DATA_DIR':str(data)},check=True,timeout=10)
        self.fixture=(data/'settings.json').read_bytes()
        self.engine.accept_from_chat(p['id'],old['id'],1,'Accept the synthetic emitter solely as an integration-test baseline.')
        self.task=self.engine.begin(p['id'],2,'Continue actual old source with verified fixture')
        self.extras=[('persist','regression','persistence','Reopen a saved file in an independent process.'),
                ('refuse','regression','startup-refusal','Run actual malformed-state startup and verify its refusal.'),
                ('snapshots','regression','collision-recovery','Create two snapshots without replacing the earlier one.'),
                ('safe','regression','file-safety','Preserve valid state on a rejected import.'),
                ('prior','regression','upgrade','Reproduce fixture using actual old source and load it correctly.')]
        self.plan=full_plan('cli',['persistent-data','backup-restore','writes-files'],self.extras)
        self.plan.update(continuation=True,previous_archive_sha256=sha(raw),
            prior_fixtures=[{'path':'Program/tests/old-state.json','sha256':sha(self.fixture)}])
        extra=r'''
if '--iteration-self-test' in sys.argv:
    with case('prior','upgrade'):
        previous=Path(os.environ['ITERATION_PREVIOUS_BUILD_DIR'])
        destination=root/'reproduced-old-state'
        subprocess.run([sys.executable,str((previous/'PROGRAM/main.py' if (previous/'PROGRAM/main.py').exists() else previous/'Program/main.py'))],
            env={**os.environ,'ITERATION_TEST_DATA_DIR':str(destination)},check=True,timeout=8)
        expected=Path(__file__).parent/'tests/old-state.json'
        actual=destination/'settings.json'
        assert actual.read_bytes()==expected.read_bytes()
        assert read(actual)=={'version':1,'count':17}
'''
        self.source=JSON_SOURCE+extra
    def tearDown(self):self.engine.close();self.temp.cleanup()
    def make(self):
        self.engine.configure_checks(self.task['id'],0,self.plan)
        self.engine.write_files(self.task['id'],1,[{'path':'Program/main.py','content':self.source},
            {'path':'Program/tests/old-state.json','content':self.fixture.decode()}])
        b=self.engine.package(self.task['id'],2,'Continuation fixture',[],[],['Run tests'])
        _,raw=self.engine.archive_bytes(b['id']);path=self.root/'new.zip';path.write_bytes(raw)
        return b,path
    def test_wrong_prior_archive_claim_is_rejected_before_packaging(self):
        self.plan['previous_archive_sha256']='0'*64
        with self.assertRaises(IterationError) as c:self.engine.configure_checks(self.task['id'],0,self.plan)
        self.assertEqual(c.exception.code,'prior_version_mismatch')
    def test_prior_fixture_must_match_its_declared_bytes(self):
        self.plan['prior_fixtures'][0]['sha256']='0'*64
        with self.assertRaises(IterationError) as c:self.make()
        self.assertEqual(c.exception.code,'prior_fixture_mismatch')
    def test_missing_actual_prior_archive_blocks_execution(self):
        _,path=self.make()
        with self.assertRaises(IterationError) as c:qualify(path,allow_execute=True)
        self.assertEqual(c.exception.code,'prior_version_required')
    def test_wrong_supplied_previous_file_is_not_accepted(self):
        _,path=self.make();wrong=self.root/'wrong.zip';wrong.write_bytes(b'wrong bytes')
        with self.assertRaises(IterationError) as c:qualify(path,allow_execute=True,previous_archive=wrong)
        self.assertEqual(c.exception.code,'prior_version_mismatch')
    def test_actual_prior_source_is_exercised_in_exact_final_release_check(self):
        b,_=self.make();out=self.root/'delivered.zip'
        r=deliver(self.engine,b['id'],out,allow_execute=True,previous_archive=self.previous)
        self.assertEqual(r['status'],'passed',json.dumps(r,indent=2))
        self.assertEqual(r['evidence']['prior_archive_sha256'],sha(self.previous.read_bytes()))
        cases=r['evidence']['checks'][1]['observed_cases']
        self.assertIn({'id':'prior','category':'upgrade','passed':True},cases)
