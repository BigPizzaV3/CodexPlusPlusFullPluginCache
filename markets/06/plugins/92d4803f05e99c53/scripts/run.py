"""Build a deterministic local trust and traceability bundle."""
import hashlib
import json
from plugin_support import main, obj, records, text, validate_json

def _refs(row, field, known):
    refs = row.get(field, [])
    if not isinstance(refs, list) or len(refs) != len(set(refs)) or any(not isinstance(x, str) or x not in known for x in refs):
        raise ValueError(f'{field} must contain unique known IDs')
    return refs

def run(data):
    obj(data); validate_json(data)
    requirements = records(data.get('requirements'), 'requirements', limit=2000)
    decisions = records(data.get('decisions'), 'decisions', limit=5000)
    evidence = records(data.get('evidence'), 'evidence', limit=5000)
    access_checks = records(data.get('access_checks'), 'access_checks', limit=5000)
    req_ids = {text(r.get('id'), 'requirements.id') for r in requirements}
    evidence_map, evidence_valid, findings = {}, {}, []
    for row in requirements: text(row.get('text'), 'requirement.text')
    for row in evidence:
        content = row.get('content')
        if not isinstance(content, str): raise ValueError('Evidence content must be supplied inline as text')
        text(row.get('origin'), 'evidence.origin')
        digest = hashlib.sha256(content.encode('utf-8')).hexdigest(); expected = row.get('expected_sha256')
        if expected is not None and (not isinstance(expected, str) or len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected)): raise ValueError('expected_sha256 must be lowercase SHA-256 hex')
        evidence_map[row['id']] = digest; evidence_valid[row['id']] = expected is None or expected == digest
        if not evidence_valid[row['id']]: findings.append({'type':'evidence_hash_mismatch','evidence_id':row['id'],'actual_sha256':digest})
        _refs(row, 'requirement_ids', req_ids)
    decision_map = {}
    for row in decisions:
        text(row.get('title'), 'decision.title'); text(row.get('rationale'), 'decision.rationale')
        decision_map[row['id']] = row
        _refs(row, 'requirement_ids', req_ids); _refs(row, 'evidence_ids', set(evidence_map))
        if row.get('status', 'active') not in ('active', 'superseded', 'proposed'): raise ValueError('decision.status must be active, superseded, or proposed')
    access_rows = []
    for row in access_checks:
        text(row.get('subject'), 'access_check.subject'); text(row.get('resource'), 'access_check.resource'); text(row.get('action'), 'access_check.action')
        expected, observed = row.get('expected'), row.get('observed', row.get('actual'))
        if expected not in ('allow','deny') or observed not in ('allow','deny'): raise ValueError('access_checks expected and observed must be allow or deny')
        refs = _refs(row, 'evidence_ids', set(evidence_map)); _refs(row, 'requirement_ids', req_ids); valid = all(evidence_valid[x] for x in refs)
        if expected != observed: findings.append({'type':'access_mismatch','access_check_id':row['id'],'expected':expected,'observed':observed})
        if not valid: findings.append({'type':'invalid_access_evidence','access_check_id':row['id']})
        access_rows.append({'id':row['id'],'subject':row['subject'],'resource':row['resource'],'action':row['action'],'expected':expected,'observed':observed,'evidence_ids':refs,'requirement_ids':row.get('requirement_ids',[]),'evidence_valid':valid,'state':'verified' if expected == observed and valid else 'needs_review'})
    coverage=[]
    for req in requirements:
        rid=req['id']; linked_decisions=[d['id'] for d in decisions if rid in d.get('requirement_ids', []) and d.get('status','active') != 'superseded']
        linked_evidence=set(e['id'] for e in evidence if rid in e.get('requirement_ids', []))
        linked_evidence.update(eid for d in decisions if rid in d.get('requirement_ids', []) for eid in d.get('evidence_ids', []))
        linked_access=[a['id'] for a in access_rows if rid in a.get('requirement_ids', [])]
        valid_evidence=sorted(x for x in linked_evidence if evidence_valid.get(x, False)); reasons=[]
        if not linked_decisions: reasons.append('no_active_decision')
        if not valid_evidence: reasons.append('no_valid_evidence')
        state='covered' if not reasons else 'needs_review'
        coverage.append({'id':rid,'text':req['text'],'state':state,'decision_ids':linked_decisions,'evidence_ids':sorted(linked_evidence),'valid_evidence_ids':valid_evidence,'access_check_ids':linked_access,'reasons':reasons})
        if reasons: findings.append({'type':'coverage_gap','requirement_id':rid,'reasons':reasons})
    access_summary={'checks':len(access_rows),'verified':sum(x['state']=='verified' for x in access_rows),'mismatches':sum(x['observed']!=x['expected'] for x in access_rows),'needs_review':sum(x['state']!='verified' for x in access_rows)}
    bundle={'requirements':len(requirements),'decisions':len(decisions),'evidence':len(evidence),'access_checks':len(access_rows),'covered_requirements':sum(x['state']=='covered' for x in coverage),'fingerprint':hashlib.sha256(json.dumps({'coverage':coverage,'access':access_rows,'evidence':evidence_map},sort_keys=True,separators=(',',':')).encode()).hexdigest()}
    return {'plugin':'aivana-trust-evidence','schema_version':1,'status':'complete' if not findings else 'needs_review','bundle':bundle,'coverage':coverage,'access_summary':access_summary,'findings':findings,'approval_required':bool(findings),'limitations':['Only supplied inline records are evaluated; no external systems, files, identities, or permissions are queried.','Evidence hashes verify content equality, not authenticity or authorship.','Access checks are declared observations and are not executed by this plugin.']}

if __name__ == '__main__': raise SystemExit(main(run))
