#!/usr/bin/env python3
"""Check rigorous coverage planning. A ready plan is not a passing execution."""
import argparse
import json
import re
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1]/'references/coverage-catalog.md'

def validate(campaign, catalog=CATALOG):
    expected=set(re.findall(r'^\| ([A-Z]+-\d+) \|',catalog.read_text(),re.M))
    families=campaign.get('families',{})
    if campaign.get('schemaVersion')!=1 or not campaign.get('target') or set(families)!=expected:
        raise ValueError('Campaign target, schema and exact catalog family set are required')
    cases=campaign.get('cases')
    if not isinstance(cases,list): raise ValueError('Campaign cases must be a list')
    by_id={}
    execution_keys=set()
    for case in cases:
        for field in ('id','assertionId','passId','profile','precondition','action','expected','oracle','inputMode'):
            if not isinstance(case.get(field),str) or not case[field].strip():
                raise ValueError('Every case needs a specific '+field)
        if case['id'] in by_id: raise ValueError('Duplicate campaign case ID')
        if case.get('risk') not in ('critical','high','medium','low'): raise ValueError('Case risk required')
        if case['inputMode'] not in ('browser-input','labeled-injection','observation','source-review'):
            raise ValueError('Input method must be explicitly classified')
        if not isinstance(case.get('evidence'),list) or not case['evidence'] or any(not isinstance(x,str) or not x for x in case['evidence']):
            raise ValueError('Case needs planned evidence fields')
        if not isinstance(case.get('dependsOn'),list): raise ValueError('Explicit dependency list required')
        key=(case['passId'],case['profile'],case['assertionId'])
        if key in execution_keys: raise ValueError('Duplicate execution key hides repeated cases')
        execution_keys.add(key);by_id[case['id']]=case
    visiting=set();visited=set()
    def visit(case_id):
        if case_id in visiting: raise ValueError('Cyclic case prerequisites')
        if case_id in visited:return
        if case_id not in by_id:raise ValueError('Unknown prerequisite case')
        visiting.add(case_id)
        for dep in by_id[case_id]['dependsOn']:visit(dep)
        visiting.remove(case_id);visited.add(case_id)
    for case_id in by_id:visit(case_id)
    gaps=[];counts={key:0 for key in ('applicable','excluded','blocked','unassessed')};mapped=set()
    for family,entry in families.items():
        disposition=entry.get('disposition')
        if disposition not in counts:raise ValueError('Invalid family disposition: '+family)
        counts[disposition]+=1
        reason=entry.get('reason','')
        refs=entry.get('caseIds')
        if not isinstance(refs,list) or any(ref not in by_id for ref in refs) or len(refs)!=len(set(refs)):
            raise ValueError('Invalid case mapping: '+family)
        if disposition=='unassessed':gaps.append({'family':family,'reason':'Applicability not assessed'})
        elif not isinstance(reason,str) or not reason.strip():raise ValueError('Family rationale required: '+family)
        if disposition=='applicable' and not refs:gaps.append({'family':family,'reason':'No concrete cases mapped'})
        if disposition=='blocked':gaps.append({'family':family,'reason':reason})
        if disposition in ('excluded','unassessed') and refs:raise ValueError('Unassessed/excluded family cannot claim cases')
        mapped.update(refs)
    if set(by_id)-mapped:raise ValueError('Cases are orphaned from the coverage catalog')
    if not cases:gaps.append({'reason':'No concrete cases planned'})
    return {'planningStatus':'ready' if not gaps else 'incomplete','families':counts,
            'caseCount':len(cases),'gaps':gaps,'scope':'Planning readiness only, not an execution or product verdict'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('campaign',type=Path)
    args=parser.parse_args()
    try:result=validate(json.loads(args.campaign.read_text()))
    except (ValueError,KeyError,TypeError,OSError) as error:parser.error(str(error))
    print(json.dumps(result,indent=2))
    return 0 if result['planningStatus']=='ready' else 1

if __name__=='__main__':raise SystemExit(main())
