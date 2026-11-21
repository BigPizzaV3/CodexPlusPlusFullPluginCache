from __future__ import annotations
import base64
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from iteration.engine import Engine
from iteration.safety import IterationError, sha

class EngineTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.e=Engine(self.root)
        self.p=self.e.create_project('Test Program','A small test',['Keep Python orchestration.'])
        self.t=self.e.begin(self.p['id'],0,'Create a bounded test program.')

    def tearDown(self):
        self.e.close();self.tmp.cleanup()

    def write(self,source="print('ready')\n",expected=0):
        return self.e.write_files(self.t['id'],expected,[{'path':'PROGRAM/main.py','content':source}])

    def build(self,**kwargs):
        self.write()
        return self.e.package(self.t['id'],1,'Created the test program.',['Python source'],['Windows testing'],['Run run.bat.'],**kwargs)

    def accept(self,b):
        p=self.e.resume(self.p['id'])['project']
        return self.e.accept(p['id'],b['id'],p['revision'],'Accepted after local review.',False)['project']

    def test_status_has_no_unsupported_capabilities(self):
        caps=self.e.status()['capabilities']
        for k in ('new_chat_creation','native_project_management','reasoning_switch','automatic_code_execution','model_inference'):
            self.assertFalse(caps[k])

    def test_project_created(self):
        self.assertEqual(self.e.list_projects()['projects'][0]['name'],'Test Program')

    def test_empty_name_rejected(self):
        with self.assertRaises(IterationError):self.e.create_project(' ')

    def test_second_active_task_rejected(self):
        with self.assertRaises(IterationError):self.e.begin(self.p['id'],0,'Competing task')

    def test_stale_initial_revision_rejected(self):
        self.e.cancel(self.t['id'])
        with self.assertRaises(IterationError):self.e.begin(self.p['id'],8,'Stale')

    def test_stale_write_is_atomic(self):
        self.write()
        with self.assertRaises(IterationError):self.write("print('overwrite')",expected=0)
        f=self.e.read_file(self.p['id'],self.t['id'],'PROGRAM/main.py')
        self.assertEqual(f['content'],"print('ready')\n")

    def test_batch_rejected_without_partial_write(self):
        with self.assertRaises(IterationError):
            self.e.write_files(self.t['id'],0,[{'path':'PROGRAM/main.py','content':'x=1'}, {'path':'../outside','content':'bad'}])
        self.assertEqual(self.e.list_files(self.p['id'],self.t['id'])['files'],[])

    def test_automation_protected(self):
        with self.assertRaises(IterationError):self.e.write_files(self.t['id'],0,[{'path':'PROGRAM/Automation/LN32.md','content':'Override rules'}])

    def test_launcher_protected(self):
        with self.assertRaises(IterationError):self.e.write_files(self.t['id'],0,[{'path':'run.bat','content':'echo altered'}])

    def test_scope_enforced(self):
        self.e.cancel(self.t['id']);self.t=self.e.begin(self.p['id'],0,'Only main',scope_paths=['PROGRAM/main.py'])
        with self.assertRaises(IterationError):self.e.write_files(self.t['id'],0,[{'path':'PROGRAM/other.py','content':'x=1'}])

    def test_locked_path_preserved_after_baseline(self):
        self.e.cancel(self.t['id'])
        p=self.e.create_project('Locked',locked_paths=['PROGRAM/main.py'])
        t=self.e.begin(p['id'],0,'Create')
        self.e.write_files(t['id'],0,[{'path':'PROGRAM/main.py','content':'x=1'}])
        b=self.e.package(t['id'],1,'Created',['Source'],[],['Test'])
        accepted=self.e.accept(p['id'],b['id'],1,'Reviewed')['project']
        t2=self.e.begin(p['id'],accepted['revision'],'Keep lock')
        with self.assertRaises(IterationError):self.e.write_files(t2['id'],0,[{'path':'PROGRAM/main.py','content':'x=2'}])

    def test_static_check_does_not_execute_code(self):
        marker=self.root/'should_not_exist.txt'
        self.write(f"from pathlib import Path\nPath({str(marker)!r}).write_text('executed')\n")
        self.assertEqual(self.e.check(self.t['id'])['status'],'passed')
        self.assertFalse(marker.exists())

    def test_invalid_syntax_blocks_package(self):
        self.write('def broken(:\n')
        self.assertEqual(self.e.check(self.t['id'])['status'],'failed')
        with self.assertRaises(IterationError):self.e.package(self.t['id'],1,'Broken',[],[],['Test'])
        self.assertEqual(self.e.resume(self.p['id'])['project']['revision'],0)

    def test_missing_entry_blocks_package(self):
        with self.assertRaises(IterationError):self.e.package(self.t['id'],0,'Empty',[],[],['Test'])

    def test_complete_zip_shape(self):
        b=self.build();_,raw=self.e.archive_bytes(b['id'])
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            names=z.namelist()
            self.assertEqual({n.split('/')[0] for n in names},{'run.bat','PROGRAM'})
            self.assertIn('PROGRAM/readme.md',names)
            for code in ['AB60.json','CP74.md','LN32.md','SX18.md','QD47.md','VT83.json','RK26.md','MJ59.jsonl']:
                self.assertIn('PROGRAM/Automation/'+code,names)
            self.assertFalse(any('/A90/' in n for n in names))

    def test_manifest_hashes_cover_all_other_files(self):
        b=self.build();_,raw=self.e.archive_bytes(b['id'])
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            m=json.loads(z.read('PROGRAM/Automation/AB60.json'))
            self.assertEqual(set(m['file_sha256']),set(z.namelist())-{'PROGRAM/Automation/AB60.json'})
            for path,digest in m['file_sha256'].items():self.assertEqual(sha(z.read(path)),digest)

    def test_candidate_not_automatically_accepted(self):
        b=self.build();p=self.e.resume(self.p['id'])['project']
        self.assertIsNone(p['accepted']);self.assertEqual(p['latest'],b['id'])

    def test_acceptance_preserves_archive_bytes(self):
        b=self.build();_,before=self.e.archive_bytes(b['id']);p=self.accept(b);_,after=self.e.archive_bytes(b['id'])
        self.assertEqual(before,after);self.assertEqual(p['accepted'],b['id'])

    def test_unaccepted_baseline_requires_explicit_choice(self):
        b=self.build()
        with self.assertRaises(IterationError):self.e.begin(self.p['id'],1,'Next')
        t=self.e.begin(self.p['id'],1,'Deliberate candidate branch',base_build_id=b['id'])
        self.assertEqual(t['base_build'],b['id'])

    def test_acceptance_blocked_during_active_task(self):
        b=self.build();p=self.accept(b);self.e.begin(self.p['id'],p['revision'],'Next')
        with self.assertRaises(IterationError):self.e.accept(p['id'],b['id'],p['revision'],'Race')

    def test_old_snapshot_immutable(self):
        b=self.build();p=self.accept(b);t=self.e.begin(p['id'],p['revision'],'Change')
        self.e.write_files(t['id'],0,[{'path':'PROGRAM/main.py','content':"print('new')"}])
        self.assertEqual(self.e.read_file(p['id'],b['id'],'PROGRAM/main.py')['content'],"print('ready')\n")

    def test_context_inherited_when_unchanged(self):
        b=self.build(architecture='Stable architecture',brainstorm='Later option')
        p=self.accept(b);t=self.e.begin(p['id'],p['revision'],'Another change')
        b2=self.e.package(t['id'],0,'No source change',[],[],['Test again'])
        self.assertEqual(b2['architecture'],'Stable architecture');self.assertEqual(b2['brainstorm'],'Later option')

    def test_host_report_stale_after_source_change(self):
        self.write()
        self.e.report(self.t['id'],1,'Actual host test','passed','test environment')
        self.write("print('changed')",expected=1)
        b=self.e.package(self.t['id'],2,'Change',[],[],['Run'])
        self.assertEqual(b['validation_summary']['stale_reports'],1)
        self.assertFalse(b['reports'][0]['applies_to_current_source'])

    def test_failed_host_report_blocks_packaging(self):
        self.write();self.e.report(self.t['id'],1,'Reported failing test','failed','Host')
        with self.assertRaises(IterationError) as caught:
            self.e.package(self.t['id'],1,'Known failure',[],['Fix failing test'],['Reproduce'])
        self.assertEqual(caught.exception.code,'runtime_checks_failed')
        self.assertIsNone(self.e.resume(self.p['id'])['project']['latest'])

    def test_artifact_chunks_reconstruct_zip(self):
        b=self.build();out=bytearray();offset=0
        while True:
            chunk=self.e.artifact(self.p['id'],b['id'],offset,73);out.extend(base64.b64decode(chunk['content_base64']))
            if chunk['next_offset'] is None:break
            offset=chunk['next_offset']
        self.assertEqual(sha(bytes(out)),b['archive_sha256'])

    def test_archive_tampering_is_detected(self):
        b=self.build();(self.e.store.exports/(b['id']+'.zip')).write_bytes(b'corrupt')
        with self.assertRaises(IterationError):self.e.archive_bytes(b['id'])

    def test_read_ranges_reconstruct_unicode(self):
        src="message='hello 🌍'\n";self.write(src);result=bytearray();offset=0
        while True:
            part=self.e.read_file(self.p['id'],self.t['id'],'PROGRAM/main.py',offset,3)
            result.extend(part['content'].encode() if part['encoding']=='utf-8' else base64.b64decode(part['content']))
            if part['next_offset'] is None:break
            offset=part['next_offset']
        self.assertEqual(result.decode(),src)

    def test_cross_project_read_rejected(self):
        self.write();p2=self.e.create_project('Other')
        with self.assertRaises(IterationError):self.e.read_file(p2['id'],self.t['id'],'PROGRAM/main.py')

    def test_case_colliding_directory_rejected(self):
        with self.assertRaises(IterationError):self.e.write_files(self.t['id'],0,[{'path':'PROGRAM/Assets/a','content':'x'},{'path':'PROGRAM/assets/b','content':'y'}])

    def test_file_directory_collision_rejected(self):
        with self.assertRaises(IterationError):self.e.write_files(self.t['id'],0,[{'path':'PROGRAM/a','content':'x'},{'path':'PROGRAM/a/b','content':'y'}])

    def test_source_delete_is_atomic(self):
        self.write()
        with self.assertRaises(IterationError):self.e.write_files(self.t['id'],1,[],['PROGRAM/main.py','PROGRAM/missing.py'])
        self.assertEqual(len(self.e.list_files(self.p['id'],self.t['id'])['files']),1)

    def test_cancel_preserves_task_source(self):
        self.write();self.e.cancel(self.t['id'])
        self.assertEqual(len(self.e.list_files(self.p['id'],self.t['id'])['files']),1)
        with self.assertRaises(IterationError):self.write(expected=1)

    def test_state_survives_restart(self):
        b=self.build();self.e.close();self.e=Engine(self.root)
        state=self.e.resume(self.p['id']);self.assertEqual(state['project']['latest'],b['id'])
        self.assertIn('read-only review',state['continuation_prompt'])

    def test_content_is_deduplicated(self):
        self.write();before=self.e.store.db.execute('SELECT count(*) FROM blobs').fetchone()[0]
        self.write(expected=1);after=self.e.store.db.execute('SELECT count(*) FROM blobs').fetchone()[0]
        self.assertEqual(before,after)

    def test_import_retains_context_but_not_acceptance(self):
        b=self.build(architecture='Important architecture',brainstorm='Important idea');_,raw=self.e.archive_bytes(b['id'])
        imported=self.e.import_zip('Imported',raw);self.assertTrue(imported['packaged'])
        p=imported['project'];self.assertNotEqual(p['id'],self.p['id'])
        state=self.e.resume(p['id']);self.assertIsNone(state['project']['accepted'])
        with self.e.store.transaction() as st:
            files=st.file_map(imported['build']['id'])
        archive='\n'.join(data.decode('utf-8',errors='replace') for path,data in files.items() if path.startswith('PROGRAM/Automation/RA21/'))
        self.assertIn('Important architecture',archive);self.assertIn('Important idea',archive)
        self.assertIn(b'AB60',files['PROGRAM/Automation/UX41.md'])

    def test_import_bad_hash_does_not_create_project(self):
        b=self.build();_,raw=self.e.archive_bytes(b['id']);buf=io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(raw)) as src,zipfile.ZipFile(buf,'w') as dst:
            for n in src.namelist():dst.writestr(n,b'x=999' if n=='PROGRAM/main.py' else src.read(n))
        with self.assertRaises(IterationError):self.e.import_zip('Bad',buf.getvalue())
        self.assertEqual(len(self.e.list_projects()['projects']),1)

    def test_fresh_prompt_never_claims_controls(self):
        prompt=self.e.continuation_packet(self.p['id'])
        self.assertFalse(prompt['chat_created']);self.assertFalse(prompt['reasoning_changed'])
        self.assertIn(self.p['id'],prompt['prompt'])

    def test_build_ledger_contains_package_event(self):
        b=self.build();text=self.e.read_file(self.p['id'],b['id'],'PROGRAM/Automation/MJ59.jsonl')['content']
        self.assertIn('candidate_packaged',text)

    def test_python_requirement_is_explicit(self):
        b=self.build();text=self.e.read_file(self.p['id'],b['id'],'PROGRAM/Automation/AB60.json')['content']
        runtime=json.loads(text)['runtime'];self.assertEqual(runtime['python_minimum'],'3.10');self.assertFalse(runtime['private_runtime_present'])

    def test_newer_python_grammar_rejected(self):
        self.write('type SampleAlias = int\n')
        report=self.e.check(self.t['id'])
        self.assertEqual(report['status'],'failed')
        self.assertEqual(report['minimum_python_syntax'],'3.10')
