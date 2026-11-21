"""Functional evidence feedback tests: legacy compatibility and qualified generated report."""
from __future__ import annotations
import base64, io, json, os, sys, tempfile, subprocess, unittest, zipfile
from pathlib import Path
from iteration.engine import Engine
from iteration.lifecycle_template import validate, observe, ready, _start
from iteration.logs import parse_log_report

class FunctionalFeedbackTests(unittest.TestCase):
    def test_legacy_lifecycle_without_observations_remains_valid_and_unproven(self):
        import hashlib
        legacy_lifecycle={'protocol':'iteration.lifecycle/1','ready':True,'failed':False,
            'sequence':1,'failure_codes':[],'checks':[]}
        meta={'schema':'iteration.logreport/1','report_id':'r_'+'a'*32,
            'identity':{'project_id':'p_example123','build_id':'b_example123'},
            'manifest_sha256':'b'*64,'state':'completed','exit_code':0,
            'lifecycle':legacy_lifecycle}
        out=io.BytesIO()
        with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
            z.writestr('report.json',json.dumps(meta));z.writestr('console.log','');z.writestr('readme.md','legacy')
        report=parse_log_report(out.getvalue())
        self.assertEqual(report['functional_observations'],[])
        self.assertEqual(report['feedback_hint'],'no_functional_evidence_in_report')
        self.assertIsNone(report['behavior_passed'])

    def test_bounded_counts_and_no_values(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'events.json'
            _start(path,'nonce-test')
            ready()
            observe('state-restored','persistence',True)
            observe('state-restored','persistence',True)
            observe('save-readback','persistence',False)
            observe('save-readback','persistence',True)
            record=json.loads(path.read_text())
            checked=validate(record,'nonce-test')
            self.assertEqual(checked['observations'],[{'id':'state-restored','category':'persistence','ok':2,'failed':0},
                {'id':'save-readback','category':'persistence','ok':1,'failed':1}])
            self.assertNotIn('actual-count-value',json.dumps(record))

    def test_no_raw_values_or_oversized_or_malformed_observations(self):
        base={'protocol':'iteration.lifecycle/1','ready':True,'failed':False,'sequence':1,'failure_codes':[],
            'checks':[],'observations':[{'id':'state-restored','category':'persistence','ok':1,'failed':0}]}
        with self.assertRaises(ValueError):validate({**base,'observations':[{'id':'restored-23','category':'persistence','ok':1,'failed':0,'count_value':23}]})
        with self.assertRaises(ValueError):validate({**base,'observations':[{'id':'user/home/me','category':'persistence','ok':1,'failed':0}]})
        with self.assertRaises(ValueError):validate({**base,'observations':[{'id':'state-restored','category':'persistence','ok':True,'failed':0}]})
        with self.assertRaises(ValueError):validate({**base,'observations':base['observations']*2})
        with self.assertRaises(ValueError):validate({**base,'observations':base['observations']*33})
        with self.assertRaises(ValueError):observe('bad value','ui',True)
        with self.assertRaises(TypeError):observe('fine','ui',1)

    def test_generated_program_logs_observations_and_injects_no_customer_values(self):
        source='''import json,os,sys\nfrom pathlib import Path\nfrom Automation.RT42 import ready, observe, case\np=Path(os.environ.get("ITERATION_TEST_DATA_DIR") or os.environ.get("ITERATION_FIXTURE_DIR") or ".")/"state.json"\nif "--iteration-smoke-test" in sys.argv:\n    with case("open","startup"):\n        assert 1+1==2\n    ready();print("ITERATION_SMOKE_OK")\nelif "--iteration-self-test" in sys.argv:\n    with case("valid","primary"):\n        p.write_text(json.dumps({"version":1,"count":54}))\n        assert json.loads(p.read_text())["count"]==54\n    ready();print("ITERATION_SELF_TEST_OK")\nelse:\n    existed=p.exists()\n    if existed:\n        value=json.loads(p.read_text())["count"]\n        observe("state-restored","persistence",value==54)\n    else:\n        p.write_text(json.dumps({"version":1,"count":54}))\n    ready()\n'''
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            engine=Engine(root/'state')
            try:
                pr=engine.create_project('Feedback fixture',constraints=['No raw user data in reports'])
                task=engine.begin(pr['id'],0,'Test functional observations')
                engine.write_files(task['id'],0,[{'path':'PROGRAM/main.py','content':source}])
                b=engine.package(task['id'],1,'Fixture',[],[],['Run with an existing saved file'])
                _,raw=engine.archive_bytes(b['id'])
                work=root/'output'
                with zipfile.ZipFile(io.BytesIO(raw)) as z:z.extractall(work)
                data=root/'data';data.mkdir()
                state=data/'state.json';state.write_text(json.dumps({'version':1,'count':54}))
                sub=subprocess.run([sys.executable,str(work/'PROGRAM/Automation/ZP90.py')],cwd=work,
                    env={**os.environ,'ITERATION_FIXTURE_DIR':str(data)},timeout=15,capture_output=True,text=True)
                self.assertEqual(sub.returncode,0,sub.stdout+sub.stderr)
                report=parse_log_report((work/'LogReport.zip').read_bytes())
                self.assertEqual(report['state'],'completed')
                self.assertEqual(report['functional_observations'],[{'id':'state-restored','category':'persistence','ok':1,'failed':0}])
                self.assertIsNone(report['behavior_passed'])
                self.assertEqual(report['feedback_hint'],'use_approved_pending_work_or_finish')
                ing=engine.ingest_log_report(base64.b64encode((work/'LogReport.zip').read_bytes()).decode())
                self.assertIn('already-approved',ing['review_direction'])
                self.assertFalse(ing['accepted_automatically'])
            finally:
                engine.close()

if __name__=='__main__': unittest.main()
