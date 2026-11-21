#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const statuses = ["OBSERVED", "ROOT_CAUSE_CONFIRMED", "RECOVERED", "PROMOTED"];
const severities = ["low", "medium", "high", "critical"];
const stages = ["approved_input", "source", "raw", "fitted_asset", "composition", "stem", "final_mix", "encode", "target_player", "unknown"];
const rootCauseStatuses = ["unknown", "inferred", "confirmed"];
const rootCauseCategories = ["planning_contract", "route_selection", "provider_raw", "identity", "continuity", "ingest_decode", "timing_retime", "composition", "audio_routing", "mix", "encode", "target_player", "privacy_provenance", "readability", "unknown"];
const recoveryStatuses = ["PENDING", "RECOVERED", "BLOCKED"];
const preventionStatuses = ["CANDIDATE", "ACTIVE", "REJECTED"];
const generalizationLevels = ["job_only", "promotion_candidate", "global"];
const promotionTargets = ["none", "SKILL.md", "reference", "script"];

const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;

export const validateProductionLearning = (learning) => {
  assert.equal(learning.schemaVersion, 1, "schemaVersion must be 1");
  assert.ok(nonEmpty(learning.learningId), "learningId is required");
  assert.ok(statuses.includes(learning.status), "status is invalid");
  assert.ok(severities.includes(learning.severity), "severity is invalid");
  assert.ok(nonEmpty(learning.symptom), "symptom is required");
  assert.ok(stages.includes(learning.lastKnownGoodStage), "lastKnownGoodStage is invalid");
  assert.ok(stages.includes(learning.earliestBadStage), "earliestBadStage is invalid");
  assert.ok(Array.isArray(learning.evidence) && learning.evidence.length > 0, "at least one evidence item is required");
  for (const [index, item] of learning.evidence.entries()) {
    assert.ok(nonEmpty(item.artifact), `evidence[${index}].artifact is required`);
    assert.ok(stages.includes(item.stage), `evidence[${index}].stage is invalid`);
    assert.ok(nonEmpty(item.observation), `evidence[${index}].observation is required`);
  }

  assert.ok(rootCauseStatuses.includes(learning.rootCause?.status), "rootCause.status is invalid");
  assert.ok(rootCauseCategories.includes(learning.rootCause?.category), "rootCause.category is invalid");
  assert.ok(nonEmpty(learning.rootCause?.statement), "rootCause.statement is required");
  if (["ROOT_CAUSE_CONFIRMED", "RECOVERED", "PROMOTED"].includes(learning.status)) {
    assert.equal(learning.rootCause.status, "confirmed", `${learning.status} requires a confirmed root cause`);
    assert.notEqual(learning.earliestBadStage, "unknown", `${learning.status} requires the earliest bad stage`);
  }

  assert.ok(recoveryStatuses.includes(learning.recovery?.status), "recovery.status is invalid");
  assert.ok(Array.isArray(learning.recovery?.actions), "recovery.actions must be an array");
  assert.equal(typeof learning.recovery?.preservesApprovedCreative, "boolean", "recovery.preservesApprovedCreative is required");
  assert.equal(typeof learning.recovery?.paidRetryRequired, "boolean", "recovery.paidRetryRequired is required");
  assert.equal(learning.recovery.preservesApprovedCreative, true, "production recovery must preserve approved Creative");
  if (learning.status === "RECOVERED" || learning.status === "PROMOTED") {
    assert.equal(learning.recovery.status, "RECOVERED", `${learning.status} requires recovered status`);
    assert.ok(learning.recovery.actions.length > 0, `${learning.status} requires recovery actions`);
  }

  assert.ok(preventionStatuses.includes(learning.preventionGate?.status), "preventionGate.status is invalid");
  assert.ok(nonEmpty(learning.preventionGate?.statement), "preventionGate.statement is required");
  assert.ok(["none", "manual", "script"].includes(learning.preventionGate?.automation), "preventionGate.automation is invalid");

  const generalization = learning.generalization;
  assert.ok(generalizationLevels.includes(generalization?.level), "generalization.level is invalid");
  assert.equal(Number.isInteger(generalization?.independentJobCount) && generalization.independentJobCount >= 1, true, "independentJobCount must be a positive integer");
  assert.equal(typeof generalization?.reproducible, "boolean", "generalization.reproducible is required");
  assert.equal(typeof generalization?.singleIncidentMaterialRisk, "boolean", "generalization.singleIncidentMaterialRisk is required");
  assert.ok(promotionTargets.includes(generalization?.promotionTarget), "generalization.promotionTarget is invalid");
  assert.ok(nonEmpty(generalization?.rationale), "generalization.rationale is required");

  if (generalization.level === "job_only") {
    assert.equal(generalization.promotionTarget, "none", "job_only learning cannot have a promotion target");
  } else {
    const promotionBasis = generalization.independentJobCount >= 2 || generalization.reproducible || generalization.singleIncidentMaterialRisk;
    assert.equal(promotionBasis, true, "promotion requires recurrence, reproducibility, or material single-incident risk");
    assert.equal(learning.rootCause.status, "confirmed", "promotion requires a confirmed root cause");
    assert.notEqual(generalization.promotionTarget, "none", "promoted learning requires a promotion target");
  }
  if (learning.status === "PROMOTED") {
    assert.equal(generalization.level, "global", "PROMOTED requires global generalization");
    assert.equal(learning.preventionGate.status, "ACTIVE", "PROMOTED requires an active prevention gate");
  }

  assert.equal(learning.campaignPerformanceClaim, false, "production learning cannot claim campaign performance");
  assert.equal(learning.distribution?.publishAllowed, false, "production learning cannot authorize publishing");
  assert.equal(learning.distribution?.activateAdsAllowed, false, "production learning cannot authorize ad activation");
  return learning;
};

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const inputPath = process.argv[2];
  assert.ok(inputPath, "Usage: validate-production-learning.mjs <production-learning.json>");
  const learning = JSON.parse(readFileSync(inputPath, "utf8"));
  validateProductionLearning(learning);
  console.log(`production learning: VALID (${learning.status}, ${learning.generalization.level})`);
}
