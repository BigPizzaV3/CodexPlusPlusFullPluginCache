"""Real child-process crash tests. Fake apps here are isolated fixtures only."""
from __future__ import annotations
import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from iteration import runner_template, lifecycle_template
from fixture_support import ready_source

HAS_DISPLAY=os.name=='nt' or bool(os.environ.get('DISPLAY'))


class FriendlyRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='iteration runtime ')
        self.root=Path(self.temp.name)/'with spaces & unicode é';self.root.mkdir()
        self.program=self.root/'PROGRAM';self.auto=self.program/'Automation';self.auto.mkdir(parents=True)
        (self.auto/'ZP90.py').write_bytes(Path(runner_template.__file__).read_bytes())
        (self.auto/'RT42.py').write_bytes(Path(lifecycle_template.__file__).read_bytes())
        (self.auto/'AB60.json').write_text(json.dumps({'project_id':'test_project','project_name':'Fixture',
            'build_id':'test_build','build_number':1,'runtime':{'console_mode':'quiet'}}))
    def tearDown(self): self.temp.cleanup()
    def launch(self,source=None):
        if source is not None:(self.program/'main.py').write_text(ready_source(source),encoding='utf-8')
        proc=subprocess.run([sys.executable,str(self.auto/'ZP90.py')],cwd=self.root,
            capture_output=True,text=True,timeout=12,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        with zipfile.ZipFile(self.root/'LogReport.zip') as z:
            meta=json.loads(z.read('report.json'));log=z.read('console.log').decode()
        return proc,meta,log
    def assert_friendly(self,proc,meta,log,exception):
        self.assertNotEqual(proc.returncode,0)
        self.assertNotEqual(meta['exit_code'],0)
        self.assertIn('Runtime error',proc.stdout)
        self.assertIn('send LogReport.zip back to Build_',proc.stdout)
        self.assertNotIn('Traceback',proc.stdout+proc.stderr)
        self.assertIn(exception,log)
    def test_index_error_is_report_only(self):
        self.assert_friendly(*self.launch("raise IndexError('No item with that key')\n"),'IndexError')
    def test_missing_import_is_report_only(self):
        self.assert_friendly(*self.launch('import deliberately_missing_fixture_module\n'),'ModuleNotFoundError')
    def test_syntax_failure_is_report_only(self):
        self.assert_friendly(*self.launch('def broken(:\n'),'SyntaxError')
    def test_missing_entry_is_reported_without_traceback(self):
        self.assert_friendly(*self.launch(),'FileNotFoundError')
    def test_explicit_nonzero_exit_is_not_success(self):
        proc,meta,log=self.launch('raise SystemExit(7)\n')
        self.assertEqual(proc.returncode,7);self.assertEqual(meta['exit_code'],7)
        self.assertIn('Runtime error',proc.stdout)
    def test_quiet_mode_keeps_stdout_in_report(self):
        proc,meta,log=self.launch('print("internal diagnostic fixture")\n')
        self.assertEqual(proc.returncode,0);self.assertEqual(meta['state'],'completed')
        self.assertIn('internal diagnostic fixture',log)
        self.assertNotIn('internal diagnostic fixture',proc.stdout)
    def test_redaction_and_no_env_dump(self):
        proc,meta,log=self.launch('print("password=private-fixture")\nraise ValueError("fixture")\n')
        self.assertNotIn('private-fixture',log);self.assertNotIn('private-fixture',proc.stdout)
        self.assertNotIn('LOCALAPPDATA',meta['environment'])
        self.assertIn('ValueError',log)
    def test_next_run_replaces_failed_report(self):
        _,meta,_=self.launch('raise RuntimeError("old failure")\n')
        proc,new,log=self.launch('print("new run")\n')
        self.assertEqual(proc.returncode,0);self.assertNotEqual(meta['report_id'],new['report_id'])
        self.assertNotIn('old failure',log)
    def test_report_write_failure_does_not_claim_saved_report(self):
        (self.program/'main.py').write_text('raise ValueError("fixture")')
        (self.root/'LogReport.zip').mkdir()
        proc=subprocess.run([sys.executable,str(self.auto/'ZP90.py')],capture_output=True,text=True,timeout=12)
        self.assertEqual(proc.returncode,74)
        self.assertIn('Do not send an older report',proc.stdout)
        self.assertNotIn('send LogReport.zip back to Build_',proc.stdout)
        self.assertNotIn('Traceback',proc.stdout+proc.stderr)
    @unittest.skipUnless(HAS_DISPLAY,'A real Tk display is required')
    def test_tk_callback_error_has_nonzero_exit(self):
        code='import tkinter as tk\nr=tk.Tk()\nr.after(20,lambda:1/0)\nr.mainloop()\n'
        self.assert_friendly(*self.launch(code),'ZeroDivisionError')
    @unittest.skipUnless(HAS_DISPLAY,'A real Tk display is required')
    def test_gui_normal_close_is_clean(self):
        code='import tkinter as tk\nr=tk.Tk()\nr.after(20,r.destroy)\nr.mainloop()\n'
        proc,meta,log=self.launch(code)
        self.assertEqual(proc.returncode,0);self.assertEqual(meta['state'],'completed')
        self.assertNotIn('invalid command name',log)
    @unittest.skipUnless(HAS_DISPLAY,'A real Tk display is required')
    def test_background_error_closes_gui_and_is_failed(self):
        code='''import tkinter as tk
import threading
r=tk.Tk()
def fail():
    raise RuntimeError('thread fixture')
t=threading.Thread(target=fail)
t.start();t.join()
r.mainloop()
'''
        self.assert_friendly(*self.launch(code),'RuntimeError')
