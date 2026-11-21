"""Plugin-neutral fixtures only: no customer application is shipped by these tests."""
from __future__ import annotations
import os
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch
from check_package import ROOT, payload
from iteration.engine import Engine
from release_check import _isolated_environment, qualify
from fixture_support import minimal_plan, traced_source


class GenericEnvironmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='iteration generic environment ')
        self.root = Path(self.temp.name)
    def tearDown(self):
        self.temp.cleanup()

    def test_custom_app_settings_and_credentials_are_not_inherited(self):
        inherited = {'PATH': '/fixture/bin', 'WIDGET_DATA_DIR': '/live/data',
                     'SOMETHING_DATABASE_URL': 'private-connection',
                     'SERVICE_API_KEY': 'private-key', 'PYTHONPATH': '/live/code',
                     'APP_CONFIG': '/live/config', 'PYTHONHOME': '/live/python'}
        with patch.dict(os.environ, inherited, clear=True):
            env = _isolated_environment(self.root)
            self.assertEqual(env['PATH'], '/fixture/bin')
            for key in inherited:
                if key != 'PATH':
                    self.assertNotIn(key, env)
            self.assertEqual(dict(os.environ), inherited)

    def test_os_display_and_library_support_remains_available(self):
        supplied = {'Path': 'C:\\runtime', 'SystemRoot': 'C:\\Windows',
                    'DISPLAY': ':99', 'XAUTHORITY': '/display/auth',
                    'TCL_LIBRARY': '/runtime/tcl', 'LC_ALL': 'C.UTF-8'}
        with patch.dict(os.environ, supplied, clear=True):
            env = _isolated_environment(self.root)
        for key, value in supplied.items():
            self.assertEqual(env[key], value)

    def test_all_data_and_temp_directories_are_disposable_and_exist(self):
        env = _isolated_environment(self.root)
        keys = ('HOME', 'USERPROFILE', 'LOCALAPPDATA', 'APPDATA',
                'XDG_DATA_HOME', 'XDG_CONFIG_HOME', 'XDG_CACHE_HOME',
                'XDG_STATE_HOME', 'TEMP', 'TMP', 'TMPDIR', 'ITERATION_TEST_DATA_DIR')
        for key in keys:
            target = Path(env[key])
            self.assertTrue(target.is_dir(), key)
            target.resolve().relative_to(self.root.resolve())
        self.assertEqual(env['PYTHONUTF8'], '1')
        self.assertEqual(env['PYTHONDONTWRITEBYTECODE'], '1')

    def test_independent_runs_have_different_test_state(self):
        a = _isolated_environment(self.root/'a')
        b = _isolated_environment(self.root/'b')
        self.assertNotEqual(a['ITERATION_TEST_DATA_DIR'], b['ITERATION_TEST_DATA_DIR'])
        (Path(a['ITERATION_TEST_DATA_DIR'])/'sentinel').write_text('old')
        self.assertFalse((Path(b['ITERATION_TEST_DATA_DIR'])/'sentinel').exists())


class GenericWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='iteration independent cases ')
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root/'state')
    def tearDown(self):
        self.engine.close()
        self.temp.cleanup()

    def run_fixture(self, source: str, console_mode: str = 'quiet') -> dict:
        project = self.engine.create_project('Independent fixture', console_mode=console_mode)
        task = self.engine.begin(project['id'], 0, 'Exercise an independent isolated test fixture')
        self.engine.write_files(task['id'], 0, [{'path':'PROGRAM/main.py', 'content':traced_source(source)}])
        self.engine.configure_checks(task['id'], 1, minimal_plan())
        build = self.engine.package(task['id'], 2, 'Temporary fixture', [], [], ['Fixture assertions'])
        _, raw = self.engine.archive_bytes(build['id'])
        archive = self.root/'fixture.zip'
        archive.write_bytes(raw)
        return qualify(archive, allow_execute=True)

    def test_stateless_cli_checks_do_not_require_gui_or_database(self):
        result = self.run_fixture('''
            import argparse
            import sys
            def parse(tokens):
                p = argparse.ArgumentParser()
                p.add_argument('number', type=int)
                p.add_argument('--factor', type=int, default=2)
                value = p.parse_args(tokens)
                return value.number * value.factor
            assert parse(['7']) == 14
            assert parse(['-3', '--factor', '4']) == -12
            assert parse(['0']) == 0
            flags = {'--iteration-smoke-test':'ITERATION_SMOKE_OK',
                     '--iteration-self-test':'ITERATION_SELF_TEST_OK'}
            assert len(sys.argv) == 2 and sys.argv[1] in flags
            print(flags[sys.argv[1]])
        ''', console_mode='interactive')
        self.assertEqual(result['status'], 'passed')
        self.assertEqual(len(result['checks']), 2)

    def test_json_persistence_uses_disposable_data_not_inherited_app_path(self):
        source = '''
            import json, os, subprocess, sys
            from pathlib import Path
            assert 'WIDGET_DATA_DIR' not in os.environ
            assert 'SERVICE_API_KEY' not in os.environ
            root = Path(os.environ['ITERATION_TEST_DATA_DIR'])
            path = root/'settings.json'
            value = {'theme':'compact', 'count':7, 'version':1}
            staged = root/'staged.json'
            staged.write_text(json.dumps(value), encoding='utf-8')
            staged.replace(path)
            assert json.loads(path.read_text(encoding='utf-8')) == value
            code = "import json,sys; assert json.load(open(sys.argv[1],encoding='utf-8'))['count']==7"
            subprocess.run([sys.executable, '-c', code, str(path)], check=True)
            snapshot = path.read_bytes()
            try:
                json.loads('{malformed')
                raise AssertionError('Malformed data accepted')
            except json.JSONDecodeError:
                assert path.read_bytes() == snapshot
            flags = {'--iteration-smoke-test':'ITERATION_SMOKE_OK',
                     '--iteration-self-test':'ITERATION_SELF_TEST_OK'}
            assert len(sys.argv) == 2 and sys.argv[1] in flags
            print(flags[sys.argv[1]])
        '''
        with patch.dict(os.environ, {'WIDGET_DATA_DIR':'/real/user/data', 'SERVICE_API_KEY':'private'}):
            result = self.run_fixture(source)
        self.assertEqual(result['status'], 'passed')

    def test_csv_file_transform_checks_output_and_invalid_input(self):
        result = self.run_fixture('''
            import csv, io, os, sys
            from pathlib import Path
            def convert(text):
                rows = list(csv.DictReader(io.StringIO(text)))
                return [(row['name'].strip(), int(row['amount'])) for row in rows]
            rows = convert('name,amount\\nalpha,2\\nbeta,3\\n')
            assert rows == [('alpha',2), ('beta',3)]
            root = Path(os.environ['ITERATION_TEST_DATA_DIR'])
            output = root/'totals.csv'
            with output.open('w',newline='',encoding='utf-8') as handle:
                writer = csv.writer(handle)
                writer.writerow(['name','amount'])
                writer.writerows(rows)
            assert convert(output.read_text(encoding='utf-8')) == rows
            before = output.read_bytes()
            try:
                convert('name,amount\\nalpha,invalid\\n')
                raise AssertionError('Invalid number accepted')
            except ValueError:
                assert output.read_bytes() == before
            flags = {'--iteration-smoke-test':'ITERATION_SMOKE_OK',
                     '--iteration-self-test':'ITERATION_SELF_TEST_OK'}
            assert len(sys.argv) == 2 and sys.argv[1] in flags
            print(flags[sys.argv[1]])
        ''')
        self.assertEqual(result['status'], 'passed')

    def test_new_project_does_not_inherit_previous_source_or_constraints(self):
        p1 = self.engine.create_project('First domain', constraints=['Keep its specialist behaviour'])
        t = self.engine.begin(p1['id'], 0, 'Original task')
        self.engine.write_files(t['id'], 0, [{'path':'PROGRAM/main.py','content':'print("old-domain-only")\n'}])
        self.engine.package(t['id'],1,'Original',[],[],['Original'])
        p2 = self.engine.create_project('New independent domain')
        self.assertNotEqual(p1['id'],p2['id'])
        self.assertEqual(p2['constraints'], [])
        self.assertIsNone(p2.get('accepted_build_id'))

    def test_distribution_contains_no_customer_app_or_nested_build_archive(self):
        for rel, _ in payload(ROOT):
            self.assertFalse(rel.startswith('PROGRAM/'), rel)
            self.assertFalse(rel.lower().endswith(('.zip','.sqlite','.db','.exe')), rel)
        skill = (ROOT/'skills/build/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('For persistent data ONLY:', skill)
        self.assertIn('For stateless apps, do not invent a database', skill)
        self.assertIn('ITERATION_TEST_DATA_DIR for ALL test state', skill)
