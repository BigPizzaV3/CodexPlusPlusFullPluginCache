"""Combine supplied signals into a reviewable outcome operations brief."""
import re
from plugin_support import main, obj, records, text, validate_json

def _refs(row, known, field):
    refs = row.get('evidence_ids', [])
    if not isinstance(refs, list) or any(not isinstance(ref, str) or ref not in known for ref in refs) or len(refs) != len(set(refs)):
        raise ValueError(f'{field} must contain unique known evidence IDs')
    return refs

def run(data):
    obj(data); validate_json(data)
    goal = text(data.get('goal'), 'goal')
    evidence = records(data.get('evidence'), 'evidence', limit=2000)
    if not evidence: raise ValueError('At least one evidence record is required')
    evidence_ids = {row['id'] for row in evidence}
    kpis = records(data.get('kpis') or [], 'kpis', limit=2000)
    revenue = records(data.get('revenue_findings') or [], 'revenue_findings', limit=2000)
    constraints = data.get('constraints', [])
    if not isinstance(constraints, list) or any(not isinstance(item, str) or not item.strip() for item in constraints):
        raise ValueError('constraints must be an array of non-empty strings')
    actions = records(data.get('actions'), 'actions', limit=200)
    steps, findings = [], []
    for row in kpis + revenue:
        _refs(row, evidence_ids, 'signal.evidence_ids')
    for index, action in enumerate(actions):
        description = action.get('description', action.get('title', action.get('action')))
        text(description, f'actions[{index}].title')
        refs = _refs(action, evidence_ids, f'actions[{index}].evidence_ids')
        reversible = action.get('reversible', True); approval = action.get('requires_approval', True)
        if type(reversible) is not bool or type(approval) is not bool: raise ValueError('Action flags must be boolean')
        steps.append({'id': action['id'], 'order': index + 1, 'action': description, 'evidence_refs': refs, 'reversible': reversible, 'approval_required': approval or not reversible})
    if not steps:
        steps = [{'id': 'assess', 'order': 1, 'action': 'Assess supplied signals against the goal', 'evidence_refs': sorted(evidence_ids), 'reversible': True, 'approval_required': True}]
    approval = any(step['approval_required'] for step in steps)
    if not kpis: findings.append({'type': 'missing_kpi_signal', 'message': 'No KPI signal was supplied'})
    if not revenue: findings.append({'type': 'missing_revenue_signal', 'message': 'No revenue finding was supplied'})
    if constraints and actions: findings.append({'type': 'constraint_review_required', 'message': 'Review proposed actions against every supplied constraint'})
    signals = {'kpis': len(kpis), 'revenue_findings': len(revenue), 'evidence': len(evidence), 'constraints': len(constraints)}
    plan = {'goal': goal, 'steps': steps, 'evidence_refs': sorted(evidence_ids), 'risks': [finding['message'] for finding in findings], 'guardrails': ['Human review before consequential action', 'No external mutation is performed', 'Preserve evidence references'], 'approval_required': approval, 'reversible_preview': {'executed': False, 'changes': [step['action'] for step in steps], 'rollback': 'Discard preview; no external state changed'}}
    return {'plugin': 'aivana-outcome-operations', 'schema_version': 1, 'status': 'needs_review' if findings else 'draft', 'summary': {**signals, 'steps': len(steps), 'approval_required': approval, 'findings': len(findings)}, 'signals': {'kpis': kpis, 'revenue_findings': revenue}, 'findings': findings, 'plan': plan, 'limitations': ['Supplied assertions are not independently verified.', 'No connector, billing, approval, or completion action is performed.']}

if __name__ == '__main__': raise SystemExit(main(run))
