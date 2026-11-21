"""Failures must remain failures even when application exception handling returns 0."""
from __future__ import annotations
import base64
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch
from iteration import runner_template, lifecycle_template
from iteration.logs import parse_log_report
from iteration.safety import IterationError


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='iteration-lifecycle-')
        self.root=Path(self.temp.name)
        self.auto=self.root/'PROGRAM/Automation';self.auto.mkdir(parents=True)
        for name,module in [('ZP90.py',runner_template),('RT42.py',lifecycle_template)]:
            (self.auto/name).write_bytes(Path(module.__file__).read_bytes())
        (self.auto/'AB60.json').write_text(json.dumps({'format':'iteration','format_version':2,
            'project_id':'fixture_project','build_id':'fixture_build','runtime':{'console_mode':'quiet'}}))
    def tearDown(self):self.temp.cleanup()
    def launch(self,source):
        (self.root/'PROGRAM/main.py').write_text(source,encoding='utf-8')
        result=subprocess.run([sys.executable,str(self.auto/'ZP90.py')],capture_output=True,text=True,
                              timeout=15,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        raw=(self.root/'LogReport.zip').read_bytes()
        return result,parse_log_report(raw),raw
    def test_clean_exit_without_ready_is_not_completed(self):
        p,r,_=self.launch('raise SystemExit(0)\n')
        self.assertEqual(p.returncode,78);self.assertEqual(r['state'],'startup_unconfirmed')
        self.assertEqual(r['process_exit_code'],0);self.assertFalse(r['application_ready_reported'])
        self.assertIn('send LogReport.zip back',p.stdout);self.assertNotIn('Traceback',p.stdout+p.stderr)
    def test_handled_startup_refusal_is_failed_with_reason(self):
        p,r,_=self.launch("from Automation.RT42 import fail\ntry:\n raise ValueError('bad configuration')\nexcept ValueError:\n fail('config-invalid')\n")
        self.assertNotEqual(p.returncode,0);self.assertEqual(r['state'],'startup_failed')
        self.assertEqual(r['process_exit_code'],0);self.assertIn('config-invalid',r['lifecycle']['failure_codes'])
    def test_late_ready_does_not_erase_refusal(self):
        p,r,_=self.launch("from Automation.RT42 import ready,fail\nfail('cannot-open')\nready()\n")
        self.assertNotEqual(p.returncode,0);self.assertEqual(r['state'],'runtime_failed')
    def test_clean_ready_exit_records_readiness_not_quality(self):
        p,r,_=self.launch('from Automation.RT42 import ready\nready()\n')
        self.assertEqual(p.returncode,0);self.assertTrue(r['application_ready_reported'])
        self.assertIsNone(r['behavior_passed'])
    def test_unhandled_exception_before_ready_is_startup_failure(self):
        p,r,_=self.launch('raise IndexError("missing field")\n')
        self.assertEqual(r['state'],'startup_failed');self.assertIn('IndexError',r['console'])
        self.assertNotIn('Traceback',p.stdout+p.stderr)
    def test_expected_validation_error_is_not_terminal(self):
        p,r,_=self.launch("from Automation.RT42 import ready\nready()\ntry:\n int('invalid')\nexcept ValueError:\n pass\n")
        self.assertEqual(p.returncode,0);self.assertFalse(r['lifecycle']['failed'])
    def test_failed_assertion_stays_failed_when_caught(self):
        p,r,_=self.launch("from Automation.RT42 import ready,case\nready()\ntry:\n with case('limit','boundary'):\n  assert False\nexcept AssertionError:\n pass\n")
        self.assertNotEqual(p.returncode,0);self.assertFalse(r['lifecycle']['checks'][0]['passed'])
    def test_successful_case_has_stable_id_and_category(self):
        p,r,_=self.launch("from Automation.RT42 import ready,case\nready()\nwith case('math','primary'):\n assert 3*3==9\n")
        self.assertEqual(r['lifecycle']['checks'],[{'id':'math','category':'primary','passed':True}])
    def test_duplicate_case_is_rejected_even_if_caught(self):
        p,r,_=self.launch("from Automation.RT42 import ready,case\nready()\nfor i in range(2):\n try:\n  with case('same','primary'):\n   assert i>=0\n except ValueError:\n  pass\n")
        self.assertNotEqual(p.returncode,0);self.assertIn('invalid-test-record',r['lifecycle']['failure_codes'])
    def test_thread_failure_is_terminal(self):
        p,r,_=self.launch("from Automation.RT42 import ready\nimport threading\nready()\ndef broken():raise RuntimeError('thread failure')\nt=threading.Thread(target=broken);t.start();t.join()\n")
        self.assertNotEqual(p.returncode,0);self.assertIn('thread failure',r['console'])
    def test_missing_lifecycle_helper_is_not_reported_success(self):
        (self.auto/'RT42.py').unlink()
        p,r,_=self.launch('print("never start")\n')
        self.assertNotEqual(p.returncode,0);self.assertEqual(r['state'],'launcher_error')
    def test_stale_report_never_supplies_readiness_to_next_run(self):
        _,good,_=self.launch('from Automation.RT42 import ready\nready()\n')
        _,bad,_=self.launch('pass\n')
        self.assertNotEqual(good['id'],bad['id']);self.assertFalse(bad['application_ready_reported'])
    def test_raw_startup_failure_modal_can_return_zero_but_report_is_failed(self):
        if os.name!='nt' and not os.environ.get('DISPLAY'):self.skipTest('Needs a real Tk display')
        # Real window, modal wait path and deterministic dismissal; no user data.
        source="""import tkinter as tk
from Automation.RT42 import fail
r=tk.Tk();r.withdraw()
d=tk.Toplevel(r);tk.Label(d,text='Unable to initialize').pack()
d.after(60,d.destroy);r.wait_window(d)
fail('initialization-refused')
r.destroy()
"""
        p,r,_=self.launch(source)
        self.assertEqual(r['process_exit_code'],0);self.assertEqual(r['state'],'startup_failed')
    def test_old_report_without_lifecycle_stays_unknown(self):
        _,_,raw=self.launch('from Automation.RT42 import ready\nready()\n')
        with zipfile.ZipFile(io.BytesIO(raw)) as z:files={n:z.read(n) for n in z.namelist()}
        m=json.loads(files['report.json']);m.pop('lifecycle');files['report.json']=json.dumps(m).encode()
        out=io.BytesIO()
        with zipfile.ZipFile(out,'w') as z:
            for n,d in files.items():z.writestr(n,d)
        r=parse_log_report(out.getvalue());self.assertIsNone(r['application_ready_reported'])
    def test_forged_completed_with_failed_lifecycle_is_rejected(self):
        _,_,raw=self.launch("from Automation.RT42 import fail\nfail('refused')\n")
        with zipfile.ZipFile(io.BytesIO(raw)) as z:files={n:z.read(n) for n in z.namelist()}
        m=json.loads(files['report.json']);m.update(state='completed',exit_code=0);files['report.json']=json.dumps(m).encode()
        out=io.BytesIO()
        with zipfile.ZipFile(out,'w') as z:
            for n,d in files.items():z.writestr(n,d)
        with self.assertRaises(IterationError):parse_log_report(out.getvalue())
    def test_lifecycle_does_not_include_customer_values(self):
        p,r,_=self.launch("from Automation.RT42 import ready,fail\nready()\nfail('service-unavailable')\nprint('password=private-fixture-value')\n")
        self.assertNotIn('private-fixture-value',json.dumps(r));self.assertNotIn('username',json.dumps(r['lifecycle']))
    def test_wrong_nonce_is_rejected(self):
        life={'protocol':lifecycle_template.PROTOCOL,'ready':True,'failed':False,'sequence':1,'checks':[], 'failure_codes':[], 'nonce':'old'}
        with self.assertRaises(ValueError):lifecycle_template.validate(life,'new')
    def test_non_boolean_ready_is_rejected(self):
        life={'protocol':lifecycle_template.PROTOCOL,'ready':1,'failed':False,'sequence':1,'checks':[], 'failure_codes':[]}
        with self.assertRaises(ValueError):lifecycle_template.validate(life)
    def test_direct_unsupervised_api_has_no_disk_side_effect(self):
        # Import an unbound copy without disturbing a managed process.
        spec=importlib.util.spec_from_file_location('unbound_test',lifecycle_template.__file__)
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        before=set(self.root.rglob('*'));m.ready();m.fail('unbound')
        with m.case('unbound-case','primary'):assert True
        self.assertEqual(before,set(self.root.rglob('*')))
