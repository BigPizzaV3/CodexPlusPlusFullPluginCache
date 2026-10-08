#!/usr/bin/env python3
"""Validate compatible pass records and count unique assertions. Never infer results."""
import argparse
import json
from pathlib import Path

STATUSES=('passed','failed','blocked','inconclusive','skipped','not-run')

def summarize(runs, expected=None):
    if not runs:
        raise ValueError('At least one result is required.')
    baseline=runs[0].get('meta',{})
    seen=set(); counts={k:0 for k in STATUSES}; required=[]
    expected_by_pass={}
    if expected is not None:
        if not expected: raise ValueError('Expected plan must not be empty')
        for item in expected:
            m=item['meta']; key=(m['passId'],m['profile'])
            if key in expected_by_pass: raise ValueError('Duplicate expected pass/profile')
            if m.get('sourceFingerprint')!=baseline.get('sourceFingerprint') or m.get('runId')!=baseline.get('runId'):
                raise ValueError('Expected plan source/run does not match')
            ids=item.get('assertionIds',[])
            if not ids or len(ids)!=len(set(ids)): raise ValueError('Invalid expected assertion IDs')
            expected_by_pass[key]=item
    for run in runs:
        meta=run.get('meta',{})
        for k in ('runId','target','sourceFingerprint'):
            if not meta.get(k) or meta[k]!=baseline.get(k):
                raise ValueError('Incompatible or missing '+k)
        for k in ('suiteFingerprint','fixtureFingerprint','profile','passId'):
            if not meta.get(k): raise ValueError('Missing '+k)
        if meta.get('sourceStatus')!='verified': raise ValueError('Unverified source parity')
        if expected is not None:
            planned=expected_by_pass.get((meta['passId'],meta['profile']))
            if not planned: raise ValueError('Unexpected pass/profile result')
            for k in ('suiteFingerprint','fixtureFingerprint'):
                if meta[k]!=planned['meta'].get(k): raise ValueError('Result does not match expected '+k)
        rows=run.get('assertions')
        if not isinstance(rows,list) or not rows: raise ValueError('Missing assertion records')
        local={k:0 for k in STATUSES}
        for row in rows:
            key=(meta['passId'],meta['profile'],row.get('id'))
            if not row.get('id') or key in seen: raise ValueError('Duplicate or missing assertion key')
            if expected is not None and row['id'] not in planned['assertionIds']:
                raise ValueError('Unplanned assertion ID')
            seen.add(key)
            status=row.get('status')
            if status not in STATUSES: raise ValueError('Invalid status')
            if status!='not-run' and not row.get('evidence'): raise ValueError('Executed status lacks evidence/reason')
            local[status]+=1; counts[status]+=1
            if row.get('required',True): required.append(status)
        if run.get('planned')!=len(rows) or run.get('counts')!=local:
            raise ValueError('Declared counts do not match assertion records')
    if expected is not None:
        for (pass_id,profile),item in expected_by_pass.items():
            for assertion_id in item['assertionIds']:
                key=(pass_id,profile,assertion_id)
                if key not in seen:
                    seen.add(key);counts['not-run']+=1;required.append('not-run')
    outcome='failed' if 'failed' in required else 'passed' if required and all(x=='passed' for x in required) else 'incomplete'
    return {'runId':baseline['runId'],'target':baseline['target'],'sourceFingerprint':baseline['sourceFingerprint'],
        'passFiles':len(runs),'uniqueAssertionProfileCases':len(seen),'counts':counts,'outcome':outcome,
        'scope':'expected campaign' if expected is not None else 'supplied pass files only',
        'note':'Cases include profile/pass dimensions. Repeat attempts must be reviewed separately. Without expected plans, missing whole passes cannot be detected.'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('results',nargs='+',type=Path)
    p.add_argument('--output',type=Path)
    p.add_argument('--expected',nargs='+',type=Path,help='Expected-plan files produced before running each pass')
    args=p.parse_args()
    try:
        runs=[]
        for path in args.results:
            raw=json.loads(path.read_text());runs.append(raw.get('data',raw))
        expected=[json.loads(path.read_text()) for path in args.expected] if args.expected else None
        summary=summarize(runs,expected)
    except (ValueError,KeyError,OSError) as e: p.error(str(e))
    text=json.dumps(summary,indent=2)+'\n'
    if args.output: args.output.write_text(text)
    print(text,end='')

if __name__=='__main__': main()
