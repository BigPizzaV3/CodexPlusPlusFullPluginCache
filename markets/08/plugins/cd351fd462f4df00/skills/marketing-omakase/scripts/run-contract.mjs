import assert from 'node:assert/strict';
import { canonicalJson, sha256 } from './custom-package.mjs';
export const MYMARKETER_SKILLS = ['strategy-authoring', 'mymarketer-strategy-slides', 'lp-structure', 'lp-image-builder', 'performance-video-ad', 'performance-video-production'];
export const EXPRESSION_CHOICES = ['composition', 'visual_direction', 'copy_expression', 'candidate_selection', 'pacing', 'sound_expression'];
export function chooseExecutor({ mymarketerMatches = [], hostMatches = [], customSource = null }) {
  const existing = mymarketerMatches.find(name => MYMARKETER_SKILLS.includes(name));
  if (existing) return { kind: 'mymarketer_skill', name: existing };
  if (hostMatches.length) return { kind: 'host_skill', name: hostMatches[0] };
  assert.ok(customSource?.trim(), 'custom source required when no suitable skill exists');
  return { kind: 'custom', sourceHash: sha256(customSource) };
}
export function orderSteps(steps) {
  assert.ok(Array.isArray(steps) && steps.length > 0 && steps.length <= 100);
  const map = new Map();
  for (const step of steps) {
    assert.match(step.id, /^[A-Za-z0-9][A-Za-z0-9_-]{0,79}$/);
    assert.ok(!map.has(step.id), 'duplicate step');
    assert.ok(Array.isArray(step.dependsOn)); map.set(step.id, step);
  }
  const ordered = [], done = new Set(), visiting = new Set();
  function visit(id) {
    assert.ok(map.has(id), 'missing dependency');
    if (done.has(id)) return;
    assert.ok(!visiting.has(id), 'cyclic dependencies'); visiting.add(id);
    const deps = map.get(id).dependsOn;
    assert.equal(new Set(deps).size, deps.length, 'duplicate dependency');
    for (const dep of deps) visit(dep);
    visiting.delete(id); done.add(id); ordered.push(map.get(id));
  }
  for (const id of map.keys()) visit(id);
  return ordered;
}
export function validateDelegationReceipt(receipt, { runId, scopeRevision, stepId, scopeHash, allowedChoices = [] }) {
  assert.deepEqual(Object.keys(receipt).sort(), ['kind', 'runId', 'scopeRevision', 'scopeHash', 'stepId', 'choice', 'agentId', 'reason', 'artifactHash', 'decidedAt'].sort(), 'unexpected agent receipt fields');
  assert.equal(receipt.kind, 'agent_delegation');
  for (const [key, expected] of Object.entries({ runId, scopeRevision, stepId, scopeHash })) assert.equal(receipt[key], expected, `stale delegation ${key}`);
  assert.ok(EXPRESSION_CHOICES.includes(receipt.choice) && allowedChoices.includes(receipt.choice), 'choice requires human approval');
  assert.equal(typeof receipt.agentId, 'string'); assert.ok(receipt.agentId.trim());
  assert.equal(typeof receipt.reason, 'string'); assert.ok(receipt.reason.trim());
  assert.match(receipt.artifactHash, /^[a-f0-9]{64}$/);
  assert.ok(Number.isFinite(Date.parse(receipt.decidedAt)));
  assert.ok(!('humanApproved' in receipt) && !('approvedBy' in receipt), 'agent receipt must not impersonate human');
  return receipt;
}
export function mutationContext(run, claim, operationId) {
  assert.equal(claim.scopeRevision, run.scopeRevision, 'stale scope claim');
  assert.equal(claim.runId, run.id);
  assert.ok(run.fencingToken && claim.id);
  assert.ok(typeof operationId === 'string' && operationId.length >= 8 && operationId.length <= 120 && /^[A-Za-z0-9_-]+$/.test(operationId), 'operationId must be 8–120 ASCII letters, digits, underscores or hyphens; no filename dots');
  assert.ok(typeof run.leaseToken === 'string' && /^[0-9a-f-]{36}$/i.test(run.leaseToken), 'local execution lease token required');
  return { runId: run.id, scopeRevision: run.scopeRevision, stepId: claim.id, fencingToken: run.fencingToken, leaseToken: run.leaseToken, operationId };
}
export function verifyScopeApproval(prepared, receipt) {
  assert.equal(receipt.kind, 'executor_reported_conversation');
  assert.equal(receipt.scopeRevision, prepared.scopeRevision);
  assert.equal(receipt.scopeHash, prepared.scopeHash);
  assert.ok(receipt.statement?.trim() && Number.isFinite(Date.parse(receipt.reportedAt)));
  return { kind: receipt.kind, statement: receipt.statement, reportedAt: receipt.reportedAt };
}
export const payloadHash = payload => sha256(canonicalJson(payload));

export function validateRunDelegation({ receipt, snapshot }, { area, artifactHash }) {
  const run = snapshot?.run;
  assert.ok(run && run.status === 'running', 'snapshot must record a running mandate at decision time');
  assert.ok(!('leaseToken' in run), 'secret lease token must not enter shared delegation receipts');
  assert.equal(payloadHash(run.scope), run.scopeHash, 'scope snapshot hash mismatch');
  const decidedAt = Date.parse(receipt.decidedAt);
  assert.ok(Number.isFinite(decidedAt) && decidedAt <= Date.now() + 60_000 && decidedAt <= Date.parse(run.leaseExpiresAt) && decidedAt >= Date.parse(run.approval?.reportedAt), 'decision must fall within the recorded approved lease');
  assert.equal(run.approval?.kind, 'executor_reported_conversation');
  assert.equal(run.approval.scopeRevision, run.scopeRevision);
  assert.equal(run.approval.scopeHash, run.scopeHash);
  assert.ok(run.approval.statement?.trim(), 'scoped human statement required');
  assert.ok(run.scope.delegation.includes(area), 'area not delegated');
  for (const subject of ['truth', 'material_rights']) assert.ok(run.scope.humanDecisions.some(d => d.subject === subject && d.statement?.trim()), `human ${subject} decision required`);
  assert.ok(run.scope.steps.some(s => s.id === receipt.stepId), 'step outside mandate');
  assert.equal(receipt.artifactHash, artifactHash, 'delegation output changed');
  validateDelegationReceipt(receipt, { runId: run.id, scopeRevision: run.scopeRevision, scopeHash: run.scopeHash, stepId: receipt.stepId, allowedChoices: EXPRESSION_CHOICES });
  return receipt;
}
