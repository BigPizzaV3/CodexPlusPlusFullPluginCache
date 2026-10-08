#!/usr/bin/env python3
"""Offline checks of audit generation, versioning, and result accounting."""
import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent

def load(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

builder=load('build_payload');summary=load('summarize_runs')
campaign_validator=load('validate_campaign')

def sample_result():
    return {'schemaVersion':1,'meta':{'runId':'one','target':'test','sourceStatus':'verified',
        'sourceFingerprint':'source','suiteFingerprint':'suite','fixtureFingerprint':'fixture',
        'profile':'phone','passId':'fast'},
        'assertions':[{'id':'a','status':'passed','evidence':{'expected':1,'actual':1}}],
        'counts':dict(passed=1,failed=0,blocked=0,inconclusive=0,skipped=0,**{'not-run':0}),
        'planned':1}

class ToolTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)/'audit'
        self.create=subprocess.run([sys.executable,str(HERE/'new_audit.py'),str(self.root),'--target','Test dashboard'],capture_output=True,text=True)
        self.assertEqual(self.create.returncode,0,self.create.stderr)
    def tearDown(self): self.temp.cleanup()
    def configured(self):
        (self.root/'target.js').write_text('customElements.define("audit-example",class extends HTMLElement {});\n')
        cfg=json.loads((self.root/'audit.json').read_text())
        cfg.update(adapterConfigured=True,sourceStatus='verified',sourceEvidence='Synthetic source for offline builder validation',expectedTag='audit-example',sourcePaths=['/target.js'])
        cfg['resources'].append({'path':'/target.js','file':'target.js','contentType':'application/javascript'})
        (self.root/'audit.json').write_text(json.dumps(cfg))
        return cfg
    def test_01_existing_workspace_is_preserved(self):
        sentinel=self.root/'keep.txt';sentinel.write_text('keep')
        r=subprocess.run([sys.executable,str(HERE/'new_audit.py'),str(self.root),'--target','Again'],capture_output=True)
        self.assertNotEqual(r.returncode,0);self.assertEqual(sentinel.read_text(),'keep')
    def test_02_unconfigured_adapter_cannot_build(self):
        with self.assertRaises(ValueError): builder.build(self.root)
    def test_03_bundle_is_valid_javascript_and_expected_plan_is_written(self):
        self.configured()
        r=subprocess.run([sys.executable,str(HERE/'build_payload.py'),str(self.root)],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)
        payload=json.loads((self.root/'payload.json').read_text())
        expected=json.loads((self.root/'payload.expected.json').read_text())
        self.assertEqual(len(expected['assertionIds']),7)
        module=self.root/'function.mjs';module.write_text(payload['code'])
        node=os.environ.get('CODEX_PRIMARY_RUNTIME_NODE','node')
        checked=subprocess.run([node,'--check',str(module)],capture_output=True,text=True)
        self.assertEqual(checked.returncode,0,checked.stderr)
    def test_04_changed_source_and_suite_have_distinct_fingerprints(self):
        self.configured();first=builder.build(self.root)['context']['meta']
        with (self.root/'suite.js').open('a') as f:f.write('\n// New case revision\n')
        second=builder.build(self.root)['context']['meta']
        self.assertEqual(first['sourceFingerprint'],second['sourceFingerprint'])
        self.assertNotEqual(first['suiteFingerprint'],second['suiteFingerprint'])
        with (self.root/'target.js').open('a') as f:f.write('\n// New source\n')
        third=builder.build(self.root)['context']['meta']
        self.assertNotEqual(second['sourceFingerprint'],third['sourceFingerprint'])
    def test_05_resource_outside_workspace_rejected(self):
        cfg=self.configured();outside=self.root.parent/'outside.js';outside.write_text('private')
        cfg['resources'][0]['file']='../outside.js';(self.root/'audit.json').write_text(json.dumps(cfg))
        with self.assertRaises(ValueError):builder.build(self.root)
    def test_06_duplicate_attempts_and_mixed_sources_rejected(self):
        a=sample_result()
        with self.assertRaises(ValueError):summary.summarize([a,a])
        b=copy.deepcopy(a);b['meta']['sourceFingerprint']='changed';b['meta']['passId']='deep'
        with self.assertRaises(ValueError):summary.summarize([a,b])
    def test_07_missing_whole_pass_stays_not_run(self):
        a=sample_result();expected=[{'meta':a['meta'],'assertionIds':['a']}]
        second=copy.deepcopy(expected[0]);second['meta']['passId']='deep';second['assertionIds']=['b','c'];expected.append(second)
        result=summary.summarize([a],expected)
        self.assertEqual(result['counts']['not-run'],2);self.assertEqual(result['outcome'],'incomplete')
        self.assertEqual(result['uniqueAssertionProfileCases'],3)
    def test_08_wrong_suite_and_forged_counts_rejected(self):
        a=sample_result();expected={'meta':copy.deepcopy(a['meta']),'assertionIds':['a']}
        expected['meta']['suiteFingerprint']='new-suite'
        with self.assertRaises(ValueError):summary.summarize([a],[expected])
        a['counts']['passed']=99
        with self.assertRaises(ValueError):summary.summarize([a])
    def test_09_runner_failure_and_late_context_cleanup(self):
        self.configured();payload=builder.build(self.root)
        (self.root/'function.mjs').write_text(payload['code'])
        (self.root/'context.json').write_text(json.dumps(payload['context']))
        check=self.root/'runner-check.mjs'
        check.write_text('''
import run from './function.mjs';
import assert from 'node:assert/strict';
import fs from 'node:fs';
const context=JSON.parse(fs.readFileSync(new URL('./context.json',import.meta.url)));
const unavailable=await run({browser:{},context});
assert.equal(unavailable.data.outcome,'incomplete');
assert.equal(unavailable.data.assertions.find(x=>x.id==='gate.adapter-ready').status,'blocked');
let closes=0;
const late=await run({browser:{createBrowserContext:async()=>{
  await new Promise(r=>setTimeout(r,30));return {close:async()=>{closes++;}};
}},context:{...context,maxPassMs:5}});
assert.equal(late.data.outcome,'incomplete');
assert.equal(late.data.assertions.find(x=>x.id==='gate.cleanup').status,'blocked');
await new Promise(r=>setTimeout(r,60));
assert.equal(closes,1);
''')
        node=os.environ.get('CODEX_PRIMARY_RUNTIME_NODE','node')
        r=subprocess.run([node,str(check)],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)

    def ready_campaign(self):
        campaign=json.loads((self.root/'campaign.json').read_text())
        for entry in campaign['families'].values():
            entry.update(disposition='excluded',reason='Synthetic single-contract tool test, not a dashboard audit')
        campaign['cases']=[{'id':'toggle.phone','assertionId':'toggle','passId':'fast','profile':'phone',
            'risk':'high','precondition':'Fixture switch off and enabled',
            'action':'Tap the visible switch once','expected':'One intended service request',
            'oracle':'Compare independent intent count and exact target',
            'inputMode':'browser-input','evidence':['mock.intents','target.geometry'],'dependsOn':[]}]
        campaign['families']['HA-01'].update(disposition='applicable',reason='Fixture switch action',caseIds=['toggle.phone'])
        return campaign

    def test_10_unassessed_and_missing_case_coverage_stays_incomplete(self):
        fresh=json.loads((self.root/'campaign.json').read_text())
        self.assertEqual(campaign_validator.validate(fresh)['planningStatus'],'incomplete')
        planned=self.ready_campaign()
        self.assertEqual(campaign_validator.validate(planned)['planningStatus'],'ready')
        planned['families']['MODEL-01'].update(disposition='applicable',reason='Relevant model missing')
        self.assertEqual(campaign_validator.validate(planned)['planningStatus'],'incomplete')

    def test_11_blocked_required_family_and_invented_catalog_do_not_pass(self):
        planned=self.ready_campaign()
        planned['families']['RECOVER-01'].update(disposition='blocked',reason='Second contained page unavailable')
        self.assertEqual(campaign_validator.validate(planned)['planningStatus'],'incomplete')
        planned['families']['invented']={'disposition':'excluded'}
        with self.assertRaises(ValueError):campaign_validator.validate(planned)

    def test_12_duplicate_execution_mapping_and_cyclic_dependencies_reject(self):
        planned=self.ready_campaign()
        duplicate=copy.deepcopy(planned['cases'][0]);duplicate['id']='same-execution'
        planned['cases'].append(duplicate)
        with self.assertRaisesRegex(ValueError,'Duplicate execution'):campaign_validator.validate(planned)
        planned=self.ready_campaign();planned['cases'][0]['dependsOn']=['toggle.phone']
        with self.assertRaisesRegex(ValueError,'Cyclic'):campaign_validator.validate(planned)

    def test_13_orphaned_cases_and_evidence_free_plans_reject(self):
        planned=self.ready_campaign();planned['cases'][0]['evidence']=[]
        with self.assertRaises(ValueError):campaign_validator.validate(planned)
        planned=self.ready_campaign();planned['families']['HA-01']['caseIds']=[]
        with self.assertRaisesRegex(ValueError,'orphaned'):campaign_validator.validate(planned)

if __name__=='__main__':unittest.main(verbosity=2)
