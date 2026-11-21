"""End-to-end release barriers and file identity tests on disposable toy programs."""
from __future__ import annotations
import base64
import copy
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest
import zipfile
from unittest.mock import patch
from iteration.engine import Engine
from iteration.layout import INDEX, RUNNER, audit_archive
from iteration.release_contract import (PLAN, RECEIPT, LIFECYCLE, validate_plan,
                                       validate_receipt, payload_digest)
from iteration.safety import IterationError, read_archive, sha
from iteration import runner_template, lifecycle_template
from release_check import qualify
from deliver import deliver, freeze_receipt
from fixture_support import rewrite_archive


def full_plan(kind='cli', features=(), extras=()):
    cases=[('open','startup','startup','Initialize and exercise the actual fixture path.'),
           ('valid','regression','primary','Transform a valid input and verify its exact result.'),
           ('invalid','regression','invalid-input','Reject malformed input through the real parser.'),
           ('limit','regression','boundary','Reject oversized input while retaining the valid state.')]
    cases+=list(extras)
    return {'schema':'iteration.check-plan/1','kind':kind,'features':list(features),'continuation':False,
            'cases':[dict(zip(('id','phase','category','description'),c)) for c in cases]}


CLI_SOURCE = '''from Automation.RT42 import ready, case
import sys
MAX_VALUE=1000000
def number(text):
    if not isinstance(text,str) or not text.isascii() or not text.isdecimal() or len(text)>7:
        raise ValueError('Enter a whole number within the allowed range')
    value=int(text)
    if not 0 <= value <= MAX_VALUE: raise ValueError('Number too large')
    return value
if '--iteration-smoke-test' in sys.argv:
    with case('open','startup'):
        assert number('3')*2==6
    ready()
    print('ITERATION_SMOKE_OK')
elif '--iteration-self-test' in sys.argv:
    with case('valid','primary'):
        assert number('27')==27
    with case('invalid','invalid-input'):
        for value in ('', '-1', '1.2', 'abc', '１２'):
            try: number(value)
            except ValueError: pass
            else: raise AssertionError('Invalid input accepted')
    with case('limit','boundary'):
        assert number('0')==0 and number(str(MAX_VALUE))==MAX_VALUE
        for value in (str(MAX_VALUE+1), '9'*5000):
            try: number(value)
            except ValueError: pass
            else: raise AssertionError('Large input accepted')
        assert number('1')==1
    ready()
    print('ITERATION_SELF_TEST_OK')
else:
    ready()
    print(number('8'))
'''


class PlanTests(unittest.TestCase):
    def test_concrete_cli_plan_passes(self):self.assertEqual(validate_plan(full_plan())['kind'],'cli')
    def test_missing_plan_is_blocked(self):
        with self.assertRaises(IterationError):validate_plan({})
    def test_duplicate_case_rejected(self):
        p=full_plan();p['cases'][-1]['id']='valid'
        with self.assertRaises(IterationError):validate_plan(p)
    def test_unknown_feature_rejected(self):
        p=full_plan(features=['mystery'])
        with self.assertRaises(IterationError):validate_plan(p)
    def test_input_coverage_cannot_be_silently_omitted(self):
        p=full_plan();p['cases']=p['cases'][:2]
        with self.assertRaises(IterationError):validate_plan(p)
    def test_specific_inapplicability_may_be_recorded_without_inventing_features(self):
        p=full_plan();p['cases']=p['cases'][:2]
        p['not_applicable']={'invalid-input':'This fixed-output protocol fixture has no user input surface.',
                             'boundary':'A dedicated unit fixture has no numerical or file input bounds.'}
        self.assertEqual(validate_plan(p)['features'],[])
    def test_persistent_data_requires_refusal_and_restart_cases(self):
        p=full_plan(features=['persistent-data'])
        with self.assertRaises(IterationError) as c:validate_plan(p)
        self.assertEqual(c.exception.code,'missing_test_category')
    def test_backup_restore_requires_collision_recovery(self):
        with self.assertRaises(IterationError):validate_plan(full_plan(features=['backup-restore']))
    def test_file_writer_requires_file_safety(self):
        with self.assertRaises(IterationError):validate_plan(full_plan(features=['writes-files']))
    def test_network_requires_integration_case(self):
        with self.assertRaises(IterationError):validate_plan(full_plan(features=['network']))
    def test_native_requires_dependency_case(self):
        with self.assertRaises(IterationError):validate_plan(full_plan(features=['native']))
    def test_fake_prior_fixture_is_not_a_persistent_upgrade(self):
        p=full_plan(features=['persistent-data'],extras=[('persist','regression','persistence','Reload a real saved fixture in a second instance.'),
            ('refuse','regression','startup-refusal','Refuse unreadable state through application startup.'),
            ('upgrade','regression','upgrade','Load data emitted by the actual previous version.')])
        p['continuation']=True
        with self.assertRaises(IterationError) as c:validate_plan(p)
        self.assertEqual(c.exception.code,'prior_version_required')
    def test_startup_category_cannot_be_counted_in_regression(self):
        p=full_plan();p['cases'][0]['phase']='regression'
        with self.assertRaises(IterationError):validate_plan(p)


class QualifiedDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='iteration delivery ')
        self.root=Path(self.temp.name);self.engine=Engine(self.root/'state')
    def tearDown(self):self.engine.close();self.temp.cleanup()
    def build(self,source=CLI_SOURCE,plan=None,files=()):
        p=self.engine.create_project('Isolated application fixture')
        t=self.engine.begin(p['id'],0,'Validate bounded independent fixture')
        entries=[{'path':'PROGRAM/main.py','content':textwrap.dedent(source)}]+list(files)
        self.engine.write_files(t['id'],0,entries)
        self.engine.configure_checks(t['id'],1,plan or full_plan())
        b=self.engine.package(t['id'],2,'Fixture only',[],['Native Windows untested'],['Exercise fixture'])
        _,raw=self.engine.archive_bytes(b['id'])
        path=self.root/(b['id']+'.zip');path.write_bytes(raw)
        return p,b,path
    def test_engine_copies_trusted_files_verbatim(self):
        _,_,path=self.build();files=read_archive(path.read_bytes())
        self.assertEqual(files[RUNNER],Path(runner_template.__file__).read_bytes())
        self.assertEqual(files[LIFECYCLE],Path(lifecycle_template.__file__).read_bytes())
    def test_comment_only_runtime_rewrite_is_blocked(self):
        _,_,path=self.build();raw=path.read_bytes();files=read_archive(raw)
        changed=b'# removed formatting equivalence is still a mutation\n'+files[RUNNER]
        path.write_bytes(rewrite_archive(raw,{RUNNER:changed}))
        with self.assertRaises(IterationError) as c:qualify(path,allow_execute=True)
        self.assertEqual(c.exception.code,'runtime_template_mismatch')
    def test_changed_lifecycle_helper_is_blocked(self):
        _,_,path=self.build();files=read_archive(path.read_bytes())
        path.write_bytes(rewrite_archive(path.read_bytes(),{LIFECYCLE:files[LIFECYCLE]+b'\n'}))
        with self.assertRaises(IterationError) as c:qualify(path,allow_execute=True)
        self.assertEqual(c.exception.code,'lifecycle_template_mismatch')
    def test_ready_and_markers_without_declared_cases_do_not_pass(self):
        source="from Automation.RT42 import ready\nimport sys\nready()\nprint('ITERATION_SMOKE_OK' if '--iteration-smoke-test' in sys.argv else 'ITERATION_SELF_TEST_OK')\n"
        _,_,path=self.build(source)
        r=qualify(path,allow_execute=True)
        self.assertEqual(r['status'],'blocked');self.assertEqual(r['checks'][0]['missing_or_failed_cases'],['open'])
    def test_missing_boundary_case_blocks_release(self):
        source=CLI_SOURCE.replace("with case('limit','boundary'):","if True:")
        _,_,path=self.build(source);r=qualify(path,allow_execute=True)
        self.assertEqual(r['status'],'blocked');self.assertIn('limit',r['checks'][1]['missing_or_failed_cases'])
    def test_wrong_case_category_blocks_release(self):
        source=CLI_SOURCE.replace("case('limit','boundary')", "case('limit','primary')")
        _,_,path=self.build(source);r=qualify(path,allow_execute=True)
        self.assertEqual(r['status'],'blocked')
    def test_swallowed_initialization_error_never_yields_delivery(self):
        source="try:\n raise ValueError('configuration broken')\nexcept ValueError:\n pass\n"
        _,b,_=self.build(source);out=self.root/'must-not-exist.zip'
        r=deliver(self.engine,b['id'],out,allow_execute=True)
        self.assertEqual(r['status'],'blocked');self.assertFalse(out.exists())
        self.assertEqual(r['evidence']['checks'][0]['log_state'],'startup_unconfirmed')
    def test_source_rewrite_during_test_is_detected(self):
        source=CLI_SOURCE+"\nfrom pathlib import Path\nPath(__file__).write_text('changed during execution')\n"
        _,_,path=self.build(source);r=qualify(path,allow_execute=True)
        self.assertEqual(r['status'],'blocked');self.assertIn('PROGRAM/main.py',r['checks'][0]['tracked_files_changed'])
    def test_final_receipt_freeze_is_followed_by_real_reexecution(self):
        source="from pathlib import Path\nif (Path(__file__).parent/'Automation/RC18.json').exists():\n raise RuntimeError('final stage test fixture')\n"+CLI_SOURCE
        _,b,_=self.build(source);out=self.root/'no-final.zip'
        r=deliver(self.engine,b['id'],out,allow_execute=True)
        self.assertEqual(r['stage'],'final_execution');self.assertEqual(r['status'],'blocked');self.assertFalse(out.exists())
    def test_frozen_release_has_payload_receipt_and_exact_hash_evidence(self):
        p,b,path=self.build();candidate=path.read_bytes();out=self.root/'ready.zip'
        r=deliver(self.engine,b['id'],out,allow_execute=True)
        self.assertEqual(r['status'],'passed');self.assertEqual(sha(out.read_bytes()),r['evidence']['archive_sha256'])
        files=read_archive(out.read_bytes());rc=validate_receipt(files)
        self.assertEqual(rc['payload_sha256'],payload_digest(files))
        self.assertEqual(rc['preflight']['archive_sha256'],sha(candidate))
        self.assertNotEqual(sha(candidate),sha(out.read_bytes()))
        self.assertEqual((self.engine.store.exports/(b['id']+'.zip')).read_bytes(),candidate)
        snapshot=self.engine.read_file(p['id'],b['id'],RECEIPT)
        self.assertIn('payload_qualified',snapshot['content'])
        self.assertIsNone(self.engine.resume(p['id'])['project']['accepted'])
    def test_retrieved_artifact_is_qualified_not_original_candidate(self):
        p,b,_=self.build();out=self.root/'ready.zip';r=deliver(self.engine,b['id'],out,allow_execute=True)
        part=self.engine.artifact(p['id'],b['id'],0,524288)
        self.assertEqual(part['release_status'],'passed')
        self.assertEqual(base64.b64decode(part['content_base64']),out.read_bytes())
        self.assertEqual(part['sha256'],r['archive_sha256'])
    def test_acceptance_leaves_frozen_archive_unchanged(self):
        p,b,_=self.build();out=self.root/'ready.zip';deliver(self.engine,b['id'],out,allow_execute=True)
        _,before=self.engine.archive_bytes(b['id'])
        self.engine.accept_from_chat(p['id'],b['id'],1,'I accept this exact tested fixture.')
        _,after=self.engine.archive_bytes(b['id']);self.assertEqual(before,after)
    def test_repeated_retrieval_cannot_overwrite_existing_file(self):
        _,b,_=self.build();out=self.root/'ready.zip';out.write_bytes(b'KEEP')
        with self.assertRaises(IterationError) as c:deliver(self.engine,b['id'],out,allow_execute=True)
        self.assertEqual(c.exception.code,'output_exists');self.assertEqual(out.read_bytes(),b'KEEP')
    def test_receipt_cannot_be_applied_to_changed_app(self):
        _,b,_=self.build();out=self.root/'ready.zip';deliver(self.engine,b['id'],out,allow_execute=True)
        changed=rewrite_archive(out.read_bytes(),{'PROGRAM/main.py':CLI_SOURCE.encode()+b'\n# changed\n'})
        with self.assertRaises(IterationError):validate_receipt(read_archive(changed))
    def test_manifest_runtime_change_invalidates_payload_receipt(self):
        _,b,_=self.build();out=self.root/'ready.zip';deliver(self.engine,b['id'],out,allow_execute=True)
        def modify(files):
            m=json.loads(files[INDEX]);m['runtime']['console_mode']='interactive';files[INDEX]=json.dumps(m).encode()
        changed=rewrite_archive(out.read_bytes(),transform=modify)
        with self.assertRaises(IterationError):validate_receipt(read_archive(changed))
    def test_preflight_for_other_archive_cannot_freeze_receipt(self):
        _,_,path=self.build();r=qualify(path,allow_execute=True);r['archive_sha256']='0'*64
        with self.assertRaises(IterationError):freeze_receipt(path.read_bytes(),r)
    def test_returned_report_correlates_to_frozen_manifest(self):
        _,b,_=self.build();out=self.root/'ready.zip';deliver(self.engine,b['id'],out,allow_execute=True)
        work=self.root/'run';work.mkdir()
        with zipfile.ZipFile(out) as z:z.extractall(work)
        result=subprocess.run([sys.executable,str(work/RUNNER)],capture_output=True,timeout=15)
        self.assertEqual(result.returncode,0)
        report=self.engine.ingest_log_report(base64.b64encode((work/'LogReport.zip').read_bytes()).decode())
        self.assertTrue(report['report']['manifest_matches_known_build'])
        self.assertTrue(report['report']['application_ready_reported'])
        self.assertFalse(report['accepted_automatically'])
    def test_fresh_host_import_retains_release_context(self):
        _,b,_=self.build();out=self.root/'ready.zip';deliver(self.engine,b['id'],out,allow_execute=True)
        other=Engine(self.root/'fresh')
        try:
            imported=other.import_zip('Recovered fixture',out.read_bytes());self.assertTrue(imported['packaged'])
            source=other.read_file(imported['project']['id'],imported['build']['id'],'PROGRAM/main.py')
            self.assertEqual(source['content'],CLI_SOURCE)
            self.assertIsNone(other.resume(imported['project']['id'])['project']['accepted'])
        finally:other.close()

    def test_failed_internal_retry_does_not_require_invented_upgrade_data(self):
        p,b,_=self.build('pass\n')
        result=deliver(self.engine,b['id'],self.root/'blocked.zip',allow_execute=True)
        self.assertEqual(result['status'],'blocked')
        state=self.engine.resume(p['id'])
        self.assertEqual(state['builds'][0]['validation_summary']['release_gate'],'blocked')
        t=self.engine.begin(p['id'],1,'Repair the undelivered candidate',base_build_id=b['id'])
        planned=self.engine.configure_checks(t['id'],0,full_plan())
        self.assertFalse(planned['plan']['continuation'])
        self.engine.write_files(t['id'],1,[{'path':'PROGRAM/main.py','content':CLI_SOURCE}])
        b2=self.engine.package(t['id'],2,'Repaired test fixture',[],[],['Run fixture'])
        r=deliver(self.engine,b2['id'],self.root/'first-delivery.zip',allow_execute=True)
        self.assertEqual(r['status'],'passed');self.assertFalse((self.root/'blocked.zip').exists())

    def test_plan_context_cannot_reset_a_released_baseline_to_fresh(self):
        p,b,_=self.build();deliver(self.engine,b['id'],self.root/'ready.zip',allow_execute=True)
        t=self.engine.begin(p['id'],1,'Continue released fixture',base_build_id=b['id'])
        with self.assertRaises(IterationError) as c:self.engine.configure_checks(t['id'],0,full_plan())
        self.assertEqual(c.exception.code,'plan_context_mismatch')

    def test_invalid_nested_plan_types_are_controlled_errors(self):
        for change in ({'kind':[]},{'features':[{}]},{'cases':[{'id':'ok','phase':'startup','category':[]}]*2}):
            p=full_plan();p.update(change)
            with self.assertRaises(IterationError):validate_plan(p)
