#!/usr/bin/env node
import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const CHECK_FIELDS = [
  "businessTensionAt0_5s",
  "whoAndSituationBy2s",
  "vfxIndependentOrExperimental",
  "promiseContinuity",
  "muteLegibility",
  "cognitiveLoadWithinPolicy",
  "ctaDestinationContinuity",
  "trustPreserved",
];

const V2_CHECK_FIELDS = ["ahaClarity", "semanticExpectationCalibrated", "insightRenderCoverage", "pacingComprehension"];

export function validateAnimaticRecord(review) {
  assert.equal(review.schemaVersion, 1, "animatic review: unsupported schemaVersion");
  assert.ok(review.jobId, "animatic review: jobId missing");
  assert.equal(review.approvalScope, "ANIMATIC_AND_PREPRODUCTION", "animatic review: invalid approvalScope");
  assert.ok(["pending", "approved", "revisions_requested", "rejected"].includes(review.decision), "animatic review: invalid decision");
  assert.ok(review.checks && typeof review.checks === "object", "animatic review: checks missing");
  const checkFields = review.reviewContractVersion === 2 ? [...CHECK_FIELDS, ...V2_CHECK_FIELDS] : CHECK_FIELDS;
  for (const field of checkFields) {
    assert.ok(["PASS", "REVISE", "REJECT", "NOT_RUN"].includes(review.checks[field]), `animatic review: invalid ${field}`);
  }
  if (review.reviewContractVersion === 2) {
    assert.ok(review.approvalGranularity, "animatic review: v2 requires approvalGranularity");
    assert.ok(Array.isArray(review.approvalGranularity.approvedElements), "animatic review: approvedElements must be an array");
    assert.ok(Array.isArray(review.approvalGranularity.pendingElements), "animatic review: pendingElements must be an array");
    assert.ok(review.approvalGranularity.revisionScope, "animatic review: revisionScope missing");
  }
  return review;
}

export function assertAnimaticApproved(review, portfolio = null, bodyFamily = null, jobDir = null) {
  validateAnimaticRecord(review);
  assert.equal(review.decision, "approved", "AI generation blocked: animatic approval is not approved");
  assert.ok(review.portfolioId, "animatic approval requires portfolioId");
  assert.ok(review.bodyFamilyId, "animatic approval requires bodyFamilyId");
  assert.ok(Array.isArray(review.reviewedPackageIds) && review.reviewedPackageIds.length > 0, "animatic approval requires reviewedPackageIds");
  assert.equal(new Set(review.reviewedPackageIds).size, review.reviewedPackageIds.length, "animatic approval reviewedPackageIds must be unique");
  assert.ok(Array.isArray(review.animaticArtifacts) && review.animaticArtifacts.length > 0, "animatic approval requires at least one low-fidelity artifact");
  assert.ok(review.animaticArtifacts.every((item) => typeof item === "string" && item.trim()), "animatic approval contains an invalid artifact reference");
  if (jobDir) {
    for (const artifact of review.animaticArtifacts) {
      assert.equal(path.isAbsolute(artifact), false, `animatic artifact must be relative to the job: ${artifact}`);
      const artifactPath = path.resolve(jobDir, artifact);
      assert.ok(artifactPath.startsWith(`${path.resolve(jobDir)}${path.sep}`), `animatic artifact escapes the job directory: ${artifact}`);
      assert.equal(existsSync(artifactPath), true, `animatic artifact does not exist: ${artifact}`);
    }
  }
  const checkFields = review.reviewContractVersion === 2 ? [...CHECK_FIELDS, ...V2_CHECK_FIELDS] : CHECK_FIELDS;
  for (const field of checkFields) assert.equal(review.checks[field], "PASS", `AI generation blocked: ${field} is not PASS`);
  if (review.reviewContractVersion === 2) assert.equal(review.approvalGranularity.pendingElements.length, 0, "AI generation blocked: Animatic approval still has pending elements");
  assert.ok(review.reviewedBy, "animatic approval requires reviewedBy");
  assert.ok(review.reviewedAt, "animatic approval requires reviewedAt");
  assert.equal(Number.isNaN(Date.parse(review.reviewedAt)), false, "animatic approval reviewedAt must be an ISO date-time");
  if (portfolio) {
    assert.equal(review.portfolioId, portfolio.portfolioId, "animatic review portfolioId mismatch");
    const packageIds = new Set(portfolio.packages.map((item) => item.id));
    for (const id of review.reviewedPackageIds) assert.ok(packageIds.has(id), `animatic review references unknown Hook: ${id}`);
  }
  if (bodyFamily) assert.equal(review.bodyFamilyId, bodyFamily.bodyFamilyId, "animatic review bodyFamilyId mismatch");
  return { reviewedHooks: review.reviewedPackageIds.length, artifacts: review.animaticArtifacts.length };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-animatic-gate.mjs <animatic-review.json>");
  const result = assertAnimaticApproved(JSON.parse(await readFile(file, "utf8")), null, null, path.dirname(file));
  console.log(`Animatic gate: PASS (${result.reviewedHooks} Hooks / ${result.artifacts} artifacts)`);
}
