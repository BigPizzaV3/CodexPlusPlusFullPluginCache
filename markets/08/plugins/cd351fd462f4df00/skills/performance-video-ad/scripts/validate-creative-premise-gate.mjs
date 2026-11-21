#!/usr/bin/env node
import assert from "node:assert/strict";
import { realpathSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

export function validateCreativePremise(premise, { requireApproval = false, minimumDepth = 1, knownSourceIds = null } = {}) {
  assert.ok([1, 2].includes(premise.schemaVersion), "creative premise: unsupported schemaVersion");
  assert.equal(premise.sourceAssemblyVersion, 1, "creative premise: unsupported sourceAssemblyVersion");
  for (const field of ["jobId", "offerId", "audience", "moment", "felt_problem", "feared_consequence", "false_solution", "surprising_truth", "product_revelation", "single_message"]) {
    assert.ok(typeof premise[field] === "string" && premise[field].trim(), `creative premise: ${field} is required`);
  }
  assert.ok(Array.isArray(premise.source_refs) && premise.source_refs.length > 0, "creative premise: source_refs are required");
  if (premise.schemaVersion === 2) {
    assert.ok(typeof premise.sales_thesis_id === "string" && premise.sales_thesis_id.trim(), "creative premise: v2 requires sales_thesis_id");
  }
  if (knownSourceIds) {
    for (const ref of premise.source_refs) assert.ok(knownSourceIds.has(String(ref).split("#", 1)[0]), `creative premise: unknown source ref ${ref}`);
  }
  assert.ok(Number.isInteger(premise.insight_depth_level) && premise.insight_depth_level >= minimumDepth, `creative premise: insight depth must be at least Level ${minimumDepth}`);
  assert.equal(premise.approval?.scope, "CREATIVE_PREMISE", "creative premise: invalid approval scope");
  assert.ok(["pending", "approved", "rejected"].includes(premise.approval?.decision), "creative premise: invalid approval decision");
  if (premise.approval.decision === "approved") {
    assert.equal(premise.status, "APPROVED", "creative premise: approved decision requires APPROVED status");
    assert.ok(premise.approval.approvedBy && premise.approval.approvedAt, "creative premise: approved decision requires approver and timestamp");
  }
  if (requireApproval) {
    assert.equal(premise.approval.decision, "approved", "Creative Premise must be human-approved before Hook generation");
    assert.equal(premise.status, "APPROVED", "Creative Premise must be APPROVED before Hook generation");
  }
  return premise;
}

async function main() {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  const requireApproval = process.argv.includes("--require-approved");
  const depthIndex = process.argv.indexOf("--minimum-depth");
  const minimumDepth = depthIndex >= 0 ? Number(process.argv[depthIndex + 1]) : 1;
  assert.ok(file, "Usage: node scripts/validate-creative-premise-gate.mjs <creative-premise.json> [--require-approved] [--minimum-depth 4]");
  const premise = JSON.parse(await readFile(file, "utf8"));
  validateCreativePremise(premise, { requireApproval, minimumDepth });
  console.log(`Creative Premise: PASS (depth=${premise.insight_depth_level}, approval=${premise.approval.decision})`);
}

const isMain = (() => {
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); } catch { return false; }
})();

if (isMain) main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
