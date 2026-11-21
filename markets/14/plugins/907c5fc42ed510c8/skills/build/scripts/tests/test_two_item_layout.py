"""New exact customer ZIP root and coded-record/legacy-import contract."""
from __future__ import annotations
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from iteration.engine import Engine
from iteration.layout import audit_archive, INDEX, AUTO, README
from iteration.safety import IterationError, sha


def zipped(files):
    stream=io.BytesIO()
    with zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED) as z:
        for path, data in files.items(): z.writestr(path, data)
    return stream.getvalue()


class TwoItemLayoutTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.e=Engine(Path(self.tmp.name)/'state')
    def tearDown(self):
        self.e.close();self.tmp.cleanup()
    def new_zip(self):
        p=self.e.create_project('Format proof', constraints=['Keep file output offline.'])
        t=self.e.begin(p['id'],0,'Produce a complete Windows test package from a plain-language request.')
        r=self.e.write_files(t['id'],0,[{'path':'Program/main.py','content':'print("ready")\n'}])
        b=self.e.package(t['id'],r['task_revision'],'Packed a complete program',['File'],[],['Run on Windows'])
        _,raw=self.e.archive_bytes(b['id'])
        with zipfile.ZipFile(io.BytesIO(raw)) as z:files={x.filename:z.read(x) for x in z.infolist() if not x.is_dir()}
        return files,raw
    def test_exact_top_level_and_single_internal_readme(self):
        files,raw=self.new_zip()
        self.assertEqual({p.split('/')[0] for p in files},{'run.bat','PROGRAM'})
        self.assertEqual([p for p in files if p.lower().endswith('readme.md')],['PROGRAM/readme.md'])
        self.assertNotIn('LogReport.zip',files)
        self.assertEqual(audit_archive(raw)['layout_version'],3)
    def test_neutral_record_lexicon_covers_work_and_ideas(self):
        files,_=self.new_zip()
        guide=files['PROGRAM/readme.md'].decode()
        for code in ('AB60','CP74','LN32','SX18','QD47','VT83','RK26','MJ59'):
            self.assertIn('[%s](Automation/%s.'%(code,code),guide)
        self.assertIn('Design alternatives',guide)
        self.assertIn('What changed',guide)
        self.assertIn('Locked decisions',guide)
        self.assertFalse(any('/HandOff/' in p or 'Brainstorm' in p for p in files))
    def test_launcher_uses_uppercase_program_folder(self):
        files,_=self.new_zip()
        bat=files['run.bat'].decode()
        self.assertIn('PROGRAM\\Automation\\ZP90.py',bat)
        self.assertIn('PROGRAM\\runtime\\python.exe',bat)
    def test_extra_root_file_rejected_even_with_consistent_hashes(self):
        files,_=self.new_zip()
        files['readme.md']=b'Extra guide'
        man=json.loads(files[INDEX]);man['file_sha256']={k:sha(v) for k,v in files.items() if k!=INDEX};files[INDEX]=json.dumps(man).encode()
        with self.assertRaises(IterationError):audit_archive(zipped(files))
    def test_report_not_shipped_even_if_consistent(self):
        files,_=self.new_zip()
        files['LogReport.zip']=b'Faked data'
        man=json.loads(files[INDEX]);man['file_sha256']={k:sha(v) for k,v in files.items() if k!=INDEX};files[INDEX]=json.dumps(man).encode()
        with self.assertRaises(IterationError):audit_archive(zipped(files))
    def test_legacy_source_accepted_and_normalized(self):
        legacy={'Run.bat':b'@echo off\n',
                'Program/main.py':b'print("prior")\n',
                'Program/config.json':b'{"retain":true}',
                'readme.md':b'previous guide'}
        result=self.e.import_zip('Older example',zipped(legacy))
        self.assertTrue(result['packaged'])
        _,raw=self.e.archive_bytes(result['build']['id'])
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            self.assertEqual(z.read('PROGRAM/config.json'),legacy['Program/config.json'])
            self.assertEqual(z.read('PROGRAM/main.py'),legacy['Program/main.py'])
            self.assertEqual({n.split('/')[0] for n in z.namelist()},{'run.bat','PROGRAM'})
    def test_source_api_cannot_replace_generated_readme(self):
        p=self.e.create_project('Guard')
        t=self.e.begin(p['id'],0,'Safety')
        with self.assertRaises(IterationError):
            self.e.write_files(t['id'],0,[{'path':'PROGRAM/readme.md','content':'overwrite'}])
    def test_windows_case_collisions_rejected(self):
        files,_=self.new_zip();files['Program/wrong.txt']=b'wrong'
        with self.assertRaises(IterationError):audit_archive(zipped(files))

if __name__=='__main__':unittest.main()
