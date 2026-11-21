from __future__ import annotations
import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from iteration.engine import Engine
from iteration.safety import IterationError
from release_check import qualify
from fixture_support import minimal_plan, traced_source


class ReleaseGateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='iteration-qualify-');self.root=Path(self.temp.name)
        self.engine=Engine(self.root/'state')
    def tearDown(self): self.engine.close();self.temp.cleanup()
    def archive(self,source):
        p=self.engine.create_project('Gate fixture');t=self.engine.begin(p['id'],0,'Run isolated fixture')
        self.engine.write_files(t['id'],0,[{'path':'PROGRAM/main.py','content':source}])
        self.engine.configure_checks(t['id'],1,minimal_plan())
        b=self.engine.package(t['id'],2,'Fixture',[],[],['Run fixture'])
        _,raw=self.engine.archive_bytes(b['id']);p=self.root/'program.zip';p.write_bytes(raw);return p
    def test_execution_needs_explicit_opt_in(self):
        p=self.archive('print("unused")')
        with self.assertRaises(IterationError) as cm:qualify(p)
        self.assertEqual(cm.exception.code,'execution_not_authorized')
    def test_two_executed_test_modes_are_required(self):
        # This tiny fixture tests the gate protocol, not a real UI's quality.
        p=self.archive(traced_source('import sys\nassert len(sys.argv)==2\nprint("ITERATION_SMOKE_OK" if sys.argv[1]=="--iteration-smoke-test" else "ITERATION_SELF_TEST_OK")\n'))
        result=qualify(p,allow_execute=True)
        self.assertEqual(result['status'],'passed');self.assertEqual(len(result['checks']),2)
        self.assertFalse(result['windows_bat_tested'])
    def test_clean_exit_without_test_marker_is_blocked(self):
        result=qualify(self.archive('print("not a test")\n'),allow_execute=True)
        self.assertEqual(result['status'],'blocked')
    def test_crash_blocks_delivery_even_if_marker_printed_first(self):
        result=qualify(self.archive('print("ITERATION_SMOKE_OK")\nraise IndexError("No item with that key")\n'),allow_execute=True)
        self.assertEqual(result['status'],'blocked')
        self.assertTrue(result['checks'][0]['diagnostic_errors'])
        self.assertFalse(result['checks'][0]['console_traceback_exposed'])
    def test_timeout_is_blocked_and_stops_child(self):
        result=qualify(self.archive('import time\ntime.sleep(60)\n'),allow_execute=True,timeout=.5)
        self.assertEqual(result['status'],'blocked');self.assertTrue(result['checks'][0]['timed_out'])
    def test_changed_source_requires_new_valid_integrity(self):
        p=self.archive('print("unused")\n')
        with zipfile.ZipFile(p) as z:files={n:z.read(n) for n in z.namelist()}
        files['PROGRAM/main.py']=b'print("tampered")\n'
        with zipfile.ZipFile(p,'w') as z:
            for name,data in files.items():z.writestr(name,data)
        with self.assertRaises(IterationError):qualify(p,allow_execute=True)
