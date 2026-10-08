"""Combine sanitized incidents and explicit migration checks into a local brief."""
import re
from plugin_support import main, obj, records, text, validate_json

def _sanitize(value):
    value = re.sub(r'\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b', '[REDACTED_EMAIL]', value)
    value = re.sub(r'\b(?:token|secret|api[_-]?key)=[^&\s]+', '[REDACTED_QUERY]', value, flags=re.I)
    return re.sub(r'\b\d{2,}\b', '<id>', value)

def run(data):
    obj(data); validate_json(data)
    incidents = records(data.get('incidents'), 'incidents', limit=2000)
    if not incidents: raise ValueError('At least one incident is required')
    ids, groups, fixtures, findings = set(), {}, [], []
    for index, incident in enumerate(incidents):
        ident = incident['id']
        if ident in ids: raise ValueError('incident IDs must be unique')
        ids.add(ident); message = text(incident.get('message'), f'incidents[{index}].message'); signature = _sanitize(message)
        groups.setdefault(signature, []).append(ident)
        request = incident.get('request'); expected = incident.get('expected_response')
        if isinstance(request, dict) and isinstance(expected, dict): fixtures.append({'event_id': ident, 'request': request, 'expected_response': expected})
        else: findings.append({'type': 'not_reproducible', 'incident_id': ident, 'message': 'Request and expected_response are both required for a fixture'})
    checks = records(data.get('migration_checks') or [], 'migration_checks', limit=2000); check_rows=[]
    for index, check in enumerate(checks):
        status = check.get('status', 'needs_review')
        if status not in ('passed', 'failed', 'needs_review'): raise ValueError(f'migration_checks[{index}].status is invalid')
        refs = check.get('evidence_ids', [])
        if not isinstance(refs, list) or any(ref not in ids for ref in refs): raise ValueError('migration check evidence_ids must reference incident IDs')
        check_rows.append({'id': check['id'], 'title': text(check.get('title'), f'migration_checks[{index}].title'), 'status': status, 'evidence_refs': refs})
        if status != 'passed': findings.append({'type': 'migration_review_required', 'check_id': check['id'], 'status': status})
    approval = bool(findings)
    return {'plugin': 'aivana-incident-intelligence', 'schema_version': 1, 'status': 'needs_review' if findings else 'analyzed', 'summary': {'incidents': len(incidents), 'groups': len(groups), 'fixtures': len(fixtures), 'migration_checks': len(check_rows), 'findings': len(findings)}, 'groups': [{'signature': signature, 'incident_ids': values, 'count': len(values)} for signature, values in sorted(groups.items())], 'fixtures': fixtures, 'migration_checks': check_rows, 'findings': findings, 'approval_required': approval, 'limitations': ['Sanitization is heuristic and does not establish authenticity.', 'No traffic replay, migration, target validation, or remediation is performed.']}

if __name__ == '__main__': raise SystemExit(main(run))
