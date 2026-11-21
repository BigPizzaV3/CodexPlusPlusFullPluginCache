"""Opaque-format regression tests. Only owned fixtures are executed on the host OS."""
from __future__ import annotations
import base64
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from iteration.engine import Engine
from iteration.layout import (AUTO, LEGACY_AUTO, INDEX, RECORDS, RETAINED_PREFIX, RUNNER, audit_archive,
    identity, retain, unpack_retained)
from iteration.safety import IterationError, legacy_label, sha
from iteration.runner_template import SessionReport
from check_package import ROOT, SCRIPT


def zipped(files):
    b=io.BytesIO()
    with zipfile.ZipFile(b,'w',zipfile.ZIP_DEFLATED) as z:
        for n,d in files.items(): z.writestr(n,d)
    return b.getvalue()


def unzipped(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        return {n:z.read(n) for n in z.namelist()}


def rehash(files):
    files=dict(files)
    m=json.loads(files[INDEX]);m['file_sha256']={n:sha(d) for n,d in files.items() if n!=INDEX}
    files[INDEX]=json.dumps(m).encode()
    return files


def legacy_v1():
    files={'Run.bat':b'@echo off\r\npy -3 Program/main.py\r\n',
        'Program/main.py':b'print("stable program")\n',
        'Program/data/items.db':b'SQLite format 3\x00fixture binary\xff\x00',
        'Program/settings.json':b'{"theme":"dark"}',
        LEGACY_AUTO+'readme.md':b'Original context instructions',
        LEGACY_AUTO+'A10.md':b'Original version notes', LEGACY_AUTO+'A20.md':b'Original constraints',
        LEGACY_AUTO+'A30.md':b'Important prior architecture', LEGACY_AUTO+'A40.md':b'Future option not approved',
        LEGACY_AUTO+'A50.json':b'{"claimed_pass": true}', LEGACY_AUTO+'A60.md':b'Original session entry',
        LEGACY_AUTO+'A70.jsonl':b'{"event":"created"}\n',LEGACY_AUTO+'A81.py':b'print("old supervisor")\n'}
    m={'format':'iteration','format_version':1,'project_id':'p_oldfixture','project_name':'Legacy',
       'build_id':'b_oldfixture','constraints':['Keep the saved inventory.'],
       'locked_paths':[],'file_sha256':{n:sha(d) for n,d in files.items()}}
    files[LEGACY_AUTO+'A00.json']=json.dumps(m).encode()
    return files


class OpaqueLayoutTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.e=Engine(self.root/'state')
    def tearDown(self):
        self.e.close();self.temp.cleanup()
    def build(self):
        p=self.e.create_project('Stock fixture',constraints=['Preserve data.'])
        t=self.e.begin(p['id'],0,'Make a fixture')
        self.e.write_files(t['id'],0,[{'path':'Program/main.py','content':'print("ready")\n'}])
        b=self.e.package(t['id'],1,'Made fixture',['Source'],['Windows'],['Run it'])
        return p,b,unzipped(self.e.archive_bytes(b['id'])[1])

    def test_clean_archive_passes_final_audit(self):
        _,_,f=self.build();r=audit_archive(zipped(f))
        self.assertEqual(r['status'],'passed');self.assertEqual(r['layout_version'],3)
        self.assertEqual(r['legacy_labels'],0);self.assertEqual(r['readme_count'],1)

    def test_codes_are_stable_across_builds(self):
        _,_,f=self.build();_,_,f2=self.build()
        names=lambda v:{n for n in v if n.startswith(AUTO)}
        self.assertEqual(names(f),names(f2))
        self.assertIn(AUTO+'AB60.json',f);self.assertIn(AUTO+'LN32.md',f)
        self.assertTrue(all(re.fullmatch(r'[A-Z]{2}[0-9]{2}\.[a-z0-9]+',n[len(AUTO):]) for n in names(f)))

    def test_root_reference_is_single_and_neutral(self):
        _,_,f=self.build()
        self.assertEqual([n for n in f if n.rsplit('/',1)[-1].lower().startswith('readme.')],['PROGRAM/readme.md'])
        self.assertFalse(legacy_label(f['PROGRAM/readme.md'].decode()))
        self.assertNotIn(AUTO+'readme.md',f)
        self.assertIn(b'[LN32](Automation/LN32.md)',f['PROGRAM/readme.md'])

    def test_legacy_write_variants_are_rejected_atomically(self):
        p=self.e.create_project('Rejected');t=self.e.begin(p['id'],0,'Guard')
        for name in ('Program/HandOff/a.md','Program/hand_off/a.txt','Program/Locked In/a.md',
                     'Program/LOCKED_IN/a.md','Program/brainstormingpacket.md',
                     'Program/BRAINSTORM_PACKET.md','Program/docs/Brainstorming/b.txt',
                     'Program/docs/haND-oFF.md','Program/notes/LockedIn.md'):
            with self.subTest(path=name),self.assertRaises(IterationError):
                self.e.write_files(t['id'],0,[{'path':'Program/main.py','content':'print(1)'},{'path':name,'content':'record'}])
        self.assertEqual(self.e.list_files(p['id'],t['id'])['files'],[])

    def test_duplicate_readmes_cannot_be_written(self):
        p=self.e.create_project('Duplicate');t=self.e.begin(p['id'],0,'Guard')
        for name in ('Program/readme.md','Program/README.MD','Program/docs/readme.txt','Program/readme.me'):
            with self.subTest(path=name),self.assertRaises(IterationError):
                self.e.write_files(t['id'],0,[{'path':name,'content':'extra'}])

    def test_appended_legacy_directory_rejected_even_with_new_hashes(self):
        _,_,f=self.build();f['Program/docs/HandOff/notes.md']=b'Extra'
        with self.assertRaises(IterationError): audit_archive(zipped(rehash(f)))

    def test_empty_legacy_directory_does_not_bypass_final_audit(self):
        _,_,f=self.build();b=io.BytesIO(zipped(f))
        with zipfile.ZipFile(b,'a') as z:z.writestr('Program/Brainstorming/',b'')
        with self.assertRaises(IterationError):audit_archive(b.getvalue())

    def test_non_coded_automation_record_rejected(self):
        _,_,f=self.build();f[AUTO+'development_notes.md']=b'Extra'
        with self.assertRaises(IterationError):audit_archive(zipped(rehash(f)))

    def test_second_readme_rejected_even_when_inventory_matches(self):
        _,_,f=self.build();f[AUTO+'readme.md']=b'Extra'
        with self.assertRaises(IterationError):audit_archive(zipped(rehash(f)))

    def test_root_readme_old_label_rejected(self):
        _,_,f=self.build();f['PROGRAM/readme.md']+=b'\nSee our Brainstorming workflow.'
        with self.assertRaises(IterationError):audit_archive(zipped(rehash(f)))

    def test_broken_root_link_rejected(self):
        _,_,f=self.build();f['PROGRAM/readme.md']+=b'\n[missing](Automation/missing.md)'
        with self.assertRaises(IterationError):audit_archive(zipped(rehash(f)))

    def test_code_index_must_match_actual_files(self):
        _,_,f=self.build();m=json.loads(f[INDEX]);m['record_index']['rules']=AUTO+'WR00.md';f[INDEX]=json.dumps(m).encode()
        with self.assertRaises(IterationError):audit_archive(zipped(f))

    def test_modified_source_invalidates_final_audit(self):
        _,_,f=self.build();f['PROGRAM/main.py']=b'print("changed after export")'
        with self.assertRaises(IterationError):audit_archive(zipped(f))

    def test_prefilled_runtime_report_is_not_shipped(self):
        _,_,f=self.build();self.assertNotIn('LogReport.zip',f)
        f['LogReport.zip']=b'pretend report'
        with self.assertRaises(IterationError):audit_archive(zipped(rehash(f)))

    def test_v1_import_preserves_source_data_and_original_records(self):
        old=legacy_v1();r=self.e.import_zip('Migrated',zipped(old));self.assertTrue(r['packaged'],r)
        f=unzipped(self.e.archive_bytes(r['build']['id'])[1]);m=json.loads(f[INDEX])
        for n in ('Program/main.py','Program/data/items.db','Program/settings.json'):
            self.assertEqual(f['PROGRAM/'+n[len('Program/'):]],old[n])
        origins=m['preserved_file_origins'];preserved={x['original_path']:f[n] for n,x in origins.items()}
        for n,d in old.items():
            if n.startswith(LEGACY_AUTO) and n!=LEGACY_AUTO+'A81.py':self.assertEqual(preserved[n],d)
        self.assertIsNone(self.e.resume(r['project']['id'])['project']['accepted'])
        self.assertEqual(audit_archive(zipped(f))['status'],'passed')

    def test_unmanifested_legacy_documents_retained_without_guessing_approval(self):
        f={'Run.bat':b'@echo off','Program/main.py':b'print(1)',
           'HandOff/notes.md':b'important state','Locked In/rules.md':b'use stable API',
           'Brainstorming/brainstormingpacket.md':b'idea not authorization',
           'Program/docs/brainstorm_packet.md':b'Another option','Program/readme.md':b'previous guide',
           'Program/HandOff/image.png':b'\x89PNG\x00\xff'}
        r=self.e.import_zip('Legacy labelled',zipped(f));self.assertTrue(r['packaged'],r)
        output=unzipped(self.e.archive_bytes(r['build']['id'])[1]);m=json.loads(output[INDEX])
        retained={v['original_path']:output[n] for n,v in m['preserved_file_origins'].items()}
        for n in set(f)-{'Run.bat','Program/main.py'}:self.assertEqual(retained[n],f[n])
        self.assertEqual(m['constraints'],[])
        self.assertFalse(any(legacy_label(n) for n in output))

    def test_legacy_input_integrity_checked_before_migration(self):
        f=legacy_v1();f[AUTO+'A30.md']=b'tampered'
        with self.assertRaises(IterationError):self.e.import_zip('bad',zipped(f))
        self.assertEqual(self.e.list_projects()['projects'],[])

    def test_old_report_matches_imported_original_not_new_launcher(self):
        old=legacy_v1();folder=self.root/'old'
        for n,d in old.items():p=folder/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(d)
        report=SessionReport(folder/'Program');report.feed(b'old test\n');report.save('completed',0)
        r=self.e.import_zip('Recovered',zipped(old));self.assertTrue(r['packaged'])
        ingested=self.e.ingest_log_report(base64.b64encode((folder/'LogReport.zip').read_bytes()).decode())
        self.assertTrue(ingested['report']['applies_to_imported_original_not_regenerated_launcher'])
        self.assertFalse(ingested['accepted_automatically'])

    def test_new_supervisor_uses_new_manifest(self):
        p,b,f=self.build();folder=self.root/'program'
        for n,d in f.items():path=folder/n;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(d)
        report=SessionReport(folder/'PROGRAM');report.save('completed',0)
        self.assertEqual(report.manifest.name,'AB60.json')
        ingested=self.e.ingest_log_report(base64.b64encode((folder/'LogReport.zip').read_bytes()).decode())
        self.assertEqual(ingested['report']['build_id'],b['id'])
        self.assertTrue(ingested['report']['manifest_matches_known_build'])

    def test_recovered_records_survive_next_iteration(self):
        r=self.e.import_zip('Retained',zipped(legacy_v1()));p=r['project'];b=r['build']
        f1=unzipped(self.e.archive_bytes(b['id'])[1]);p=self.e.accept(p['id'],b['id'],1,'Keep this exact fixture')['project']
        t=self.e.begin(p['id'],p['revision'],'Small change')
        self.e.write_files(t['id'],0,[{'path':'Program/main.py','content':'print("second")\n'}])
        b2=self.e.package(t['id'],1,'small change',[],[],['Run'])
        f2=unzipped(self.e.archive_bytes(b2['id'])[1])
        self.assertEqual({n:d for n,d in f1.items() if n.startswith(RETAINED_PREFIX)},
                         {n:d for n,d in f2.items() if n.startswith(RETAINED_PREFIX)})
        self.assertEqual(f1['PROGRAM/data/items.db'],f2['PROGRAM/data/items.db'])
        self.assertEqual(self.e.resume(p['id'])['project']['accepted'],b['id'])

    def test_v2_fresh_import_keeps_retained_record_provenance(self):
        r=self.e.import_zip('First',zipped(legacy_v1()));f1=unzipped(self.e.archive_bytes(r['build']['id'])[1])
        fresh=Engine(self.root/'fresh')
        try:
            r2=fresh.import_zip('Second',zipped(f1));self.assertTrue(r2['packaged'],r2)
            f2=unzipped(fresh.archive_bytes(r2['build']['id'])[1])
            origins=json.loads(f2[INDEX])['preserved_file_origins']
            self.assertTrue(any(v['original_path']==LEGACY_AUTO+'A30.md' for v in origins.values()))
            self.assertEqual(f2['PROGRAM/data/items.db'],f1['PROGRAM/data/items.db'])
        finally:fresh.close()

    def test_retention_oversize_fails_without_silent_truncation(self):
        with self.assertRaises(IterationError):retain({'Program/HandOff/a.md':b'a'*(2*1024*1024+1)})

    def test_retained_tampering_rejected(self):
        items=retain({'HandOff/a.md':b'important'})
        first=next(iter(items.values()));first['content_base64']=base64.b64encode(b'changed').decode()
        with self.assertRaises(IterationError):unpack_retained(items)

    def test_unknown_layout_is_not_silently_guessed(self):
        with self.assertRaises(IterationError):self.e.import_zip('Unknown',zipped({'app.py':b'print(1)'}))
        self.assertEqual(self.e.list_projects()['projects'],[])

    def test_cli_audits_actual_zip_and_returns_failure_on_appended_labels(self):
        _,_,f=self.build();path=self.root/'fixture.zip';path.write_bytes(zipped(f))
        cmd=[sys.executable,str(SCRIPT/'iteration_cli.py'),'--state',str(self.root/'cli'),'audit',str(path)]
        r=subprocess.run(cmd,capture_output=True,text=True,timeout=20,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        self.assertEqual(r.returncode,0,r.stdout+r.stderr);self.assertEqual(json.loads(r.stdout)['status'],'passed')
        f['HandOff/a.md']=b'extra';path.write_bytes(zipped(f))
        r=subprocess.run(cmd,capture_output=True,text=True,timeout=20,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        self.assertEqual(r.returncode,1);self.assertEqual(json.loads(r.stdout)['error'],'layout_failed')

    def test_native_package_does_not_contain_retired_filename_labels(self):
        names=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
        self.assertFalse(any(legacy_label(n) for n in names))
        self.assertLessEqual(len([n for n in names if n.rsplit('/',1)[-1].lower().startswith('readme.')]),1)

    def test_skill_requires_final_byte_audit_and_resolves_old_preferences(self):
        skill=(ROOT/'skills/build/SKILL.md').read_text()
        self.assertIn('FINAL RELEASE GATE',skill)
        self.assertIn('Preserve the useful CONTENT',skill)
        self.assertIn('A failed audit blocks delivery',skill)
        self.assertIn('Do not append',' '.join(skill.split()))
        self.assertIn('PROGRAM/readme.md',skill)

    def test_option_and_evidence_contents_remain_present(self):
        _,_,f=self.build()
        for heading in (b'Task intent',b'Architecture goal',b'Changed systems',b'Not changed',b'Quarantined',b'Validation',b'Risks',b'Back Burner',b'Next prompt'):
            self.assertIn(heading,f[AUTO+RECORDS['options']])
        evidence=json.loads(f[AUTO+RECORDS['evidence']])
        self.assertFalse(evidence['windows_launch_tested']);self.assertFalse(evidence['project_runtime_tested'])

    def test_conflicting_identity_records_rejected(self):
        _,_,f=self.build();f[AUTO+'A00.json']=f[INDEX]
        with self.assertRaises(IterationError):identity(f)

    def test_missing_lexicon_reference_rejected(self):
        _,_,f=self.build();f['PROGRAM/readme.md']=f['PROGRAM/readme.md'].replace(b'[LN32](Automation/LN32.md)',b'LN32')
        with self.assertRaises(IterationError):audit_archive(zipped(rehash(f)))


    def test_legacy_label_on_executable_is_not_silently_moved(self):
        f={'Run.bat':b'@echo off','Program/main.py':b'import handoff_manager',
           'Program/handoff_manager.py':b'print("runtime module")'}
        with self.assertRaises(IterationError) as ctx:self.e.import_zip('Ambiguous',zipped(f))
        self.assertEqual(ctx.exception.code,'ambiguous_legacy_file')
        self.assertEqual(self.e.list_projects()['projects'],[])

    def test_saved_database_in_legacy_named_folder_is_not_silently_moved(self):
        f={'Run.bat':b'@echo off','Program/main.py':b'print("db path dependency")',
           'Program/Locked In/inventory.sqlite3':b'SQLite format 3\0'}
        with self.assertRaises(IterationError) as ctx:self.e.import_zip('Ambiguous data',zipped(f))
        self.assertEqual(ctx.exception.code,'ambiguous_legacy_file')
        self.assertEqual(self.e.list_projects()['projects'],[])

    def test_credential_filename_cannot_be_laundered_as_coded_notes(self):
        f={'Run.bat':b'@echo off','Program/main.py':b'print(1)',
           'Program/HandOff/.env':b'CUSTOM_TOKEN=private-value'}
        with self.assertRaises(IterationError) as ctx:self.e.import_zip('Secret',zipped(f))
        self.assertEqual(ctx.exception.code,'possible_secret')
        self.assertEqual(self.e.list_projects()['projects'],[])
