#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";

const costFile = process.argv[2] ? path.resolve(process.argv[2]) : null;
const approvalFile = process.argv[3] ? path.resolve(process.argv[3]) : null;
assert.ok(costFile && approvalFile, "Usage: node scripts/approval-gate.mjs <cost-estimate.json> <approval.json>");
const cost = JSON.parse(await readFile(costFile, "utf8"));
const approval = JSON.parse(await readFile(approvalFile, "utf8"));

assert.equal(cost.jobId, approval.jobId, "jobId mismatch");
assert.equal(cost.withinBudget, true, "Paid execution blocked: estimated cost exceeds job limit");
assert.equal(approval.decision, "approved", "Paid execution blocked: approval is not approved");
assert.equal(approval.paidRunAllowed, true, "Paid execution blocked: paidRunAllowed is false");
assert.ok(cost.estimatedCostUsd <= approval.maximumApprovedCostUsd, "Paid execution blocked: approved budget exceeded");
assert.equal(approval.maximumAttempts, 1, "Exploration gate requires exactly one attempt");

console.log(`Paid execution gate: PASS (jobId=${cost.jobId}, maxAttempts=1)`);
