#!/usr/bin/env python3
"""Bundle a configured workspace for Browserless /function. Performs no network I/O."""
import argparse
import hashlib
import json
import re
from pathlib import Path

GATES = ['gate.adapter-ready','gate.transport-probes','gate.unexpected-traffic',
         'gate.mock-contracts','gate.runtime-errors','gate.cleanup']

def digest(value):
    return hashlib.sha256(value).hexdigest()

def within(root, value):
    path = (root/value).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError('Resource must be a file within the audit workspace: '+value)
    return path

def build(root):
    cfg = json.loads((root/'audit.json').read_text())
    if cfg.get('adapterConfigured') is not True or cfg.get('sourceStatus') != 'verified' or not cfg.get('sourceEvidence'):
        raise ValueError('Verify the source manifest and configure the target adapter before building.')
    if not cfg.get('expectedTag') or not cfg.get('sourcePaths'):
        raise ValueError('Expected mounted tag and copied target source paths are required.')
    if not isinstance(cfg.get('plan'),list) or not cfg['plan']:
        raise ValueError('A nonempty assertion plan is required.')
    ids=[p.get('id') for p in cfg['plan']]
    if not all(isinstance(i,str) and i and not i.startswith('gate.') for i in ids) or len(ids)!=len(set(ids)):
        raise ValueError('Plan IDs must be unique, nonempty, and not use the gate. prefix.')
    if not 100 <= cfg.get('stepTimeoutMs',0) < cfg.get('maxPassMs',0) <= 55000:
        raise ValueError('Choose bounded step and pass budgets; this helper caps a pass at 55 seconds.')
    for key in ('target','runId','passId','profile'):
        if not isinstance(cfg.get(key),str) or not cfg[key]:
            raise ValueError('Missing '+key)
    vp=cfg.get('viewport',{})
    if any(not isinstance(vp.get(k),int) or not 200 <= vp[k] <= 5000 for k in ('width','height')):
        raise ValueError('Viewport width/height must be integers from 200 to 5000.')
    resources=[]
    seen=set()
    for item in cfg.get('resources',[]):
        path=item['path']
        if not isinstance(path,str) or not path.startswith('/') or path.startswith('//') or any(c in path for c in ('#','\\')) or '..' in path.split('/') or path in seen:
            raise ValueError('Invalid or duplicate virtual resource path.')
        seen.add(path)
        body=within(root,item['file']).read_text(encoding='utf-8')
        resources.append({'path':path,'body':body,'contentType':item.get('contentType','text/plain')})
    if cfg.get('entry') not in seen or any(p not in seen for p in cfg['sourcePaths']):
        raise ValueError('Entry and all target sourcePaths must be supplied resources.')
    source_items=[next(r for r in resources if r['path']==p) for p in cfg['sourcePaths']]
    source_fingerprint=digest(json.dumps({'sources':source_items,'evidence':cfg['sourceEvidence']},sort_keys=True).encode())
    fingerprint=digest(json.dumps({'resources':resources,'config':cfg},sort_keys=True).encode())
    sections=[]
    for filename in ('network-policy.mjs','ledger.mjs','browser-helpers.mjs','sequence-engine.mjs','temporal-oracles.mjs'):
        code=within(root,filename).read_text()
        sections.append(re.sub(r'^export ', '', code, flags=re.M))
    suite=within(root,'suite.js').read_text()
    sections.append(suite)
    sections.append(within(root,'browserless-runner.js').read_text())
    code='\n\n'.join(sections)
    context={k:cfg[k] for k in ('entry','expectedTag','viewport','stepTimeoutMs','maxPassMs','plan')}
    context.update({'resources':resources,'meta':{
        'runId':cfg['runId'],'passId':cfg['passId'],'target':cfg['target'],
        'profile':cfg['profile'],'seed':cfg.get('seed'), 'sourceStatus':'verified',
        'sourceFingerprint':source_fingerprint,'fixtureFingerprint':fingerprint,
        'suiteFingerprint':digest(code.encode()),'sourceEvidence':cfg['sourceEvidence']
    }})
    return {'code':code,'context':context}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('workspace',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    root=args.workspace.expanduser().resolve()
    try: payload=build(root)
    except (ValueError,KeyError,OSError) as e: p.error(str(e))
    out=args.output.expanduser().resolve() if args.output else root/'payload.json'
    out.write_text(json.dumps(payload,indent=2)+'\n')
    expected=out.with_suffix('.expected.json')
    expected.write_text(json.dumps({'meta':payload['context']['meta'],
        'assertionIds':GATES+[p['id'] for p in payload['context']['plan']]},indent=2)+'\n')
    print(json.dumps({'payload':str(out),'expectedPlan':str(expected),
        'sourceFingerprint':payload['context']['meta']['sourceFingerprint'],'bytes':out.stat().st_size}))

if __name__ == '__main__':
    main()
