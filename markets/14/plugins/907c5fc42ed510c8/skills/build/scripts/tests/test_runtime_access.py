from __future__ import annotations
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

SOURCE = Path(os.environ.get('BUILD_RUNTIME_TEST_SOURCE', str(Path(__file__).resolve().parents[1])))
HELPER = SOURCE/'prepare_runtime.py'
spec=importlib.util.spec_from_file_location('build_prepare_runtime',HELPER)
runtime=importlib.util.module_from_spec(spec);spec.loader.exec_module(runtime)


class RuntimeAccessTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='Build runtime é & space ')
        self.root=Path(self.temp.name)
        # Simulated source-reader results: plain text, not an executable mount.
        self.text_results={n:(SOURCE/n).read_text(encoding='utf-8') for n in runtime.ENGINE_FILES}
        self.source=self.root/'copied resource text';self.source.mkdir()
        for name,text in self.text_results.items():
            p=self.source/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode('utf-8'))
    def tearDown(self):self.temp.cleanup()
    def test_full_source_only_text_copy_verifies_exactly(self):
        r=runtime.inspect(self.source,reject_extra_python=True)
        self.assertEqual(r['status'],'passed');self.assertEqual(r['files_verified'],14)
        for n,v in runtime.ENGINE_FILES.items():self.assertEqual(hashlib.sha256((self.source/n).read_bytes()).hexdigest(),v['sha256'])
    def test_missing_source_is_precise_and_no_destination_created(self):
        (self.source/'iteration/engine.py').unlink()
        dest=self.root/'runtime';r=runtime.copy_runtime(self.source,dest)
        self.assertEqual(r['status'],'blocked');self.assertEqual(r['missing'],['iteration/engine.py']);self.assertFalse(dest.exists())
    def test_modified_source_rejected(self):
        (self.source/'iteration/engine.py').write_text('print("replacement")\n')
        r=runtime.inspect(self.source);self.assertEqual(r['status'],'blocked');self.assertEqual(r['mismatched'][0]['file'],'iteration/engine.py')
    def test_truncated_source_rejected(self):
        p=self.source/'deliver.py';p.write_bytes(p.read_bytes()[:200])
        self.assertEqual(runtime.inspect(self.source)['status'],'blocked')
    def test_reader_wrappers_rejected(self):
        p=self.source/'deliver.py';p.write_bytes(b'```python\n'+p.read_bytes()+b'```\n')
        self.assertEqual(runtime.inspect(self.source)['status'],'blocked')
    def test_crlf_conversion_requires_correct_recopy(self):
        p=self.source/'iteration/store.py';p.write_bytes(p.read_bytes().replace(b'\n',b'\r\n'))
        self.assertEqual(runtime.inspect(self.source)['status'],'blocked')
    def test_no_final_newline_is_not_silently_repaired(self):
        p=self.source/'iteration/__init__.py';p.write_bytes(p.read_bytes().rstrip(b'\n'))
        self.assertEqual(runtime.inspect(self.source)['status'],'blocked')
    def test_copy_preserves_all_bytes(self):
        dest=self.root/'runtime';r=runtime.copy_runtime(self.source,dest)
        self.assertEqual(r['status'],'passed');self.assertTrue(r['materialized'])
        for n in runtime.ENGINE_FILES:self.assertEqual((dest/n).read_bytes(),(self.source/n).read_bytes())
    def test_copy_ignores_non_runtime_files(self):
        (self.source/'guide.py').write_text('raise AssertionError("never copy")\n')
        dest=self.root/'runtime';runtime.copy_runtime(self.source,dest)
        self.assertFalse((dest/'guide.py').exists());self.assertEqual(runtime.inspect(dest, reject_extra_python=True)['status'],'passed')
    def test_existing_destination_is_not_overwritten(self):
        dest=self.root/'runtime';dest.mkdir();(dest/'keep.txt').write_text('keep')
        with self.assertRaises(runtime.RuntimeAccessError):runtime.copy_runtime(self.source,dest)
        self.assertEqual((dest/'keep.txt').read_text(),'keep')
    def test_unverified_runtime_never_probed(self):
        (self.source/'deliver.py').unlink()
        with patch.object(runtime.subprocess,'run',side_effect=AssertionError('must not execute')):
            self.assertEqual(runtime.probe(self.source)['status'],'blocked')
    def test_extra_import_shadow_rejected_before_probe(self):
        (self.source/'json.py').write_text('raise AssertionError("shadow")\n')
        with patch.object(runtime.subprocess,'run',side_effect=AssertionError('must not execute')):
            r=runtime.probe(self.source)
        self.assertEqual(r['status'],'blocked');self.assertIn('json.py',r['unexpected_python_files'])
    def test_symlink_file_refused(self):
        p=self.source/'deliver.py';p.unlink()
        try:p.symlink_to(SOURCE/'deliver.py')
        except (OSError,NotImplementedError):self.skipTest('OS denied symlink fixture creation')
        with self.assertRaises(runtime.RuntimeAccessError):runtime.inspect(self.source)
    def test_symlink_source_root_refused(self):
        p=self.root/'link'
        try:p.symlink_to(self.source,target_is_directory=True)
        except (OSError,NotImplementedError):self.skipTest('OS denied symlink fixture creation')
        with self.assertRaises(runtime.RuntimeAccessError):runtime.copy_runtime(p,self.root/'dest')
    def test_missing_destination_parent_refused(self):
        with self.assertRaises(runtime.RuntimeAccessError):runtime.copy_runtime(self.source,self.root/'missing'/'runtime')
    def test_probe_entrypoints_does_not_create_project_state(self):
        r=runtime.probe(self.source)
        self.assertEqual(r['status'],'passed');self.assertTrue(r['runtime_executable'])
        self.assertFalse(r['created_project_state']);self.assertEqual(len(r['command_probes']),3)
        self.assertFalse(r['application_qualified'])
    def test_check_is_read_only(self):
        before={p.relative_to(self.source).as_posix():p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        runtime.inspect(self.source)
        after={p.relative_to(self.source).as_posix():p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        self.assertEqual(before,after)
    def test_no_network_needed_for_copy_and_inspection(self):
        import socket
        with patch.object(socket,'socket',side_effect=AssertionError('no network permitted')):
            self.assertEqual(runtime.copy_runtime(self.source,self.root/'runtime')['status'],'passed')
    def test_command_reports_blocked_without_python_install_claim(self):
        p=self.source/'deliver.py';p.unlink()
        run=subprocess.run([sys.executable,'-B',str(HELPER),'--check',str(self.source),'--probe'],capture_output=True,timeout=20)
        self.assertEqual(run.returncode,1)
        result=json.loads(run.stdout);self.assertEqual(result['missing'],['deliver.py'])
    def test_inventory_is_exact_and_bounded(self):
        self.assertEqual(set(runtime.ENGINE_FILES),set(self.text_results));self.assertEqual(len(runtime.ENGINE_FILES),14)
        self.assertLess(sum(v['bytes'] for v in runtime.ENGINE_FILES.values()),200000)


class RealEngineRoundtrip(unittest.TestCase):
    def test_source_only_runtime_can_qualify_and_import_real_report(self):
        with tempfile.TemporaryDirectory(prefix='Build runtime roundtrip ') as tmp:
            root=Path(tmp);source=root/'read resources';source.mkdir()
            for name in runtime.ENGINE_FILES:
                text=(SOURCE/name).read_text(encoding='utf-8')
                path=source/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(text.encode('utf-8'))
            dest=root/'runtime';self.assertEqual(runtime.copy_runtime(source,dest)['status'],'passed')
            state=root/'state';args=root/'args.json';counter=[0]
            def command(script,*values):
                p=subprocess.run([sys.executable,'-B',str(dest/script),*map(str,values)],cwd=root,capture_output=True,timeout=45)
                self.assertEqual(p.returncode,0,p.stdout.decode(errors='replace')+p.stderr.decode(errors='replace'))
                return json.loads(p.stdout)
            def call(tool,values):
                args.write_text(json.dumps(values),encoding='utf-8')
                return command('iteration_cli.py','--state',state,'call',tool,'--arguments',args)
            p=call('iteration_create_project',{'name':'Runtime access roundtrip','console_mode':'interactive'})
            t=call('iteration_begin',{'project_id':p['id'],'expected_revision':0,'intent':'Internal runtime-access test only'})
            # A real, stateless arithmetic fixture; not a customer counter application.
            app='''from Automation.RT42 import ready, case, observe
import sys

def increment(value):
    if type(value) is not int: raise ValueError('integer required')
    if not -1000 <= value < 1000: raise ValueError('out of range')
    return value+1
if '--iteration-smoke-test' in sys.argv:
    with case('open','startup'): assert increment(0)==1
    ready();print('ITERATION_SMOKE_OK')
elif '--iteration-self-test' in sys.argv:
    with case('action','primary'): assert increment(5)==6
    with case('invalid','invalid-input'):
        try: increment('5')
        except ValueError: pass
        else: raise AssertionError('invalid accepted')
    with case('limit','boundary'):
        assert increment(-1000)==-999
        try: increment(1000)
        except ValueError: pass
        else: raise AssertionError('boundary accepted')
    ready();print('ITERATION_SELF_TEST_OK')
else:
    assert increment(2)==3
    observe('arithmetic-ok','primary',True)
    ready();print('Runtime access test complete')
'''
            wr=call('iteration_write_files',{'task_id':t['id'],'expected_task_revision':0,'files':[{'path':'PROGRAM/main.py','content':app}]})
            plan={'schema':'iteration.check-plan/1','kind':'cli','features':[], 'continuation':False,
                  'cases':[dict(id=i,phase=phase,category=cat,description=desc) for i,phase,cat,desc in [
                    ('open','startup','startup','Execute the actual arithmetic fixture entry path.'),
                    ('action','regression','primary','Increment a genuine integer and assert the exact output.'),
                    ('invalid','regression','invalid-input','Reject string input through the actual arithmetic function.'),
                    ('limit','regression','boundary','Check lower and upper bounds without mutating input.')]]}
            plan_path=root/'plan.json';plan_path.write_text(json.dumps(plan))
            planned=command('iteration_cli.py','--state',state,'plan','--task-id',t['id'],'--revision',wr['task_revision'],'--file',plan_path)
            b=call('iteration_package',{'task_id':t['id'],'expected_task_revision':planned['task_revision'],'summary':'Runtime transport test',
                 'completed':['Arithmetic fixture'],'remaining':['Native Windows execution untested'], 'what_to_test':['Run genuine supervisor']})
            output=root/'qualified.zip'
            delivered=command('deliver.py','--state',state,'--build-id',b['id'],'--output',output,'--allow-execute')
            self.assertEqual(delivered['status'],'passed')
            self.assertEqual(hashlib.sha256(output.read_bytes()).hexdigest(),delivered['archive_sha256'])
            audit=command('iteration_cli.py','--state',state,'audit',output);self.assertEqual(audit['status'],'passed')
            unpack=root/'application';unpack.mkdir()
            with zipfile.ZipFile(output) as archive:
                self.assertEqual({n.split('/')[0] for n in archive.namelist()},{'run.bat','PROGRAM'})
                self.assertIn('PROGRAM/Automation/RC18.json',archive.namelist())
                archive.extractall(unpack)
            ran=subprocess.run([sys.executable,'-B',str(unpack/'PROGRAM/Automation/ZP90.py')],cwd=unpack,capture_output=True,timeout=20)
            self.assertEqual(ran.returncode,0,ran.stderr.decode(errors='replace'))
            report=unpack/'LogReport.zip';self.assertTrue(report.exists())
            with zipfile.ZipFile(report) as archive:
                self.assertEqual(set(archive.namelist()),{'report.json','console.log','readme.md'})
            imported=command('iteration_cli.py','--state',state,'log',report)
            # Keep actual results for inspection without assuming a nested schema.
            self.assertNotIn('error',imported)
            fresh=command('iteration_cli.py','--state',root/'fresh-state','import',output,'--name','Recovered runtime proof')
            self.assertNotIn('error',fresh)
            fresh_log=command('iteration_cli.py','--state',root/'fresh-state','log',report);self.assertNotIn('error',fresh_log)
            evidence=os.environ.get('BUILD_RUNTIME_EVIDENCE')
            if evidence:
                Path(evidence).write_text(json.dumps({'status':'passed','source_reader':'simulated_complete_text_results',
                    'materialized_files':14, 'qualified':delivered,'audit':audit,
                    'same_state_log':imported,'fresh_state_log':fresh_log,
                    'native_windows_tested':False,'live_browser_tested':False},indent=2)+'\n')

if __name__=='__main__':unittest.main(verbosity=2)
