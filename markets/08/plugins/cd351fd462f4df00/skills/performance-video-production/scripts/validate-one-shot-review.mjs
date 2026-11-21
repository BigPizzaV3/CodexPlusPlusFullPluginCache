#!/usr/bin/env node
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { payloadHash, validateRunDelegation } from "../../marketing-omakase/scripts/run-contract.mjs";
import { readFileSync, realpathSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const decisions = ["ACCEPT_PICTURE", "SURGICAL_FINISH", "REGENERATE_SAME_CONCEPT", "RETURN_TO_CONCEPT"];
const stages = ["none", "source", "concept", "prompt", "generation", "finish", "technical"];
const statuses = ["DRAFT", "REVIEWED"];
const checkValues = ["PASS", "REPAIRABLE", "FAIL", "NOT_APPLICABLE"];
const requiredChecks = [
  "twoSecondComprehension",
  "conceptSemantics",
  "promptConceptFit",
  "semanticMotionArc",
  "offerBinding",
  "identity",
  "criticalCopy",
  "typographyIntegration",
  "claimsAndPrivacy",
  "endingUsability",
  "technicalDecode"
];
const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;

function validateGroundedPrimaryOutcome(primaryOutcome) {
  assert.ok(primaryOutcome && typeof primaryOutcome === "object" && !Array.isArray(primaryOutcome), "one-shot review: primaryOutcome is required");
  assert.equal(primaryOutcome.status, "grounded", "one-shot review: primaryOutcome.status must be grounded when upstream is provided");
  assert.ok(nonEmpty(primaryOutcome.statement), "one-shot review: primaryOutcome.statement is required");
  assert.ok(Array.isArray(primaryOutcome.sourceRefs) && primaryOutcome.sourceRefs.length > 0, "one-shot review: primaryOutcome.sourceRefs are required");
  assert.equal(new Set(primaryOutcome.sourceRefs).size, primaryOutcome.sourceRefs.length, "one-shot review: primaryOutcome.sourceRefs must be unique");
}

function validateUnavailablePrimaryOutcome(primaryOutcome) {
  assert.ok(primaryOutcome && typeof primaryOutcome === "object" && !Array.isArray(primaryOutcome), "one-shot review: primaryOutcome is required");
  assert.deepEqual(primaryOutcome, {
    status: "unavailable",
    statement: null,
    sourceRefs: [],
    reason: "standalone_review_without_trustworthy_upstream",
  }, "one-shot review: standalone REVIEW_ONLY must explicitly mark primaryOutcome unavailable");
}

export function validateOneShotReview(review, {
  requireReviewed = false,
  expectedPrimaryOutcome = null,
  standaloneReview = false,
  allowLegacyV1 = false,
  requireFinalDelivery = false,
  finalDelivery = null,
} = {}) {
  if (requireFinalDelivery || finalDelivery) requireReviewed = true;
  assert.ok([1, 2].includes(review.schemaVersion), "one-shot review: unsupported schemaVersion");
  assert.equal(review.contractType, "performance_video_one_shot_review", "one-shot review: invalid contractType");
  for (const field of ["jobId", "conceptId", "assetRef", "assetSha256"]) {
    assert.ok(nonEmpty(review[field]), "one-shot review: " + field + " is required");
  }
  if (review.schemaVersion === 2) {
    if (expectedPrimaryOutcome !== null) {
      assert.equal(standaloneReview, false, "one-shot review: upstream brief and standalone mode are mutually exclusive");
      validateGroundedPrimaryOutcome(review.primaryOutcome);
      assert.deepEqual(review.primaryOutcome, expectedPrimaryOutcome, "one-shot review: primaryOutcome lineage mismatch with one-shot brief");
    } else {
      if (requireReviewed) assert.equal(standaloneReview, true, "one-shot review: reviewed v2 requires an upstream brief or --standalone-review");
      validateUnavailablePrimaryOutcome(review.primaryOutcome);
    }
  } else {
    if (requireReviewed) assert.equal(allowLegacyV1, true, "one-shot review: reviewed schemaVersion 1 requires explicit --legacy-v1 compatibility mode");
    assert.equal(expectedPrimaryOutcome, null, "one-shot review: legacy schemaVersion 1 cannot claim v2 primaryOutcome lineage");
    assert.equal(standaloneReview, false, "one-shot review: use --legacy-v1, not --standalone-review, for schemaVersion 1");
  }
  assert.ok(statuses.includes(review.status), "one-shot review: invalid status");
  if (requireReviewed) assert.equal(review.status, "REVIEWED", "one-shot review: REVIEWED status is required");
  assert.ok(decisions.includes(review.decision), "one-shot review: invalid decision");
  assert.ok(stages.includes(review.earliestFailureStage), "one-shot review: invalid earliestFailureStage");

  for (const key of requiredChecks) {
    assert.ok(checkValues.includes(review.checks?.[key]), "one-shot review: invalid checks." + key);
  }
  const typography = review.typographyReview;
  assert.ok(typography && typeof typography === "object", "one-shot review: typographyReview is required");
  for (const key of ["integratedKeywords", "exactSurfaces", "captionTaste"]) {
    assert.ok(checkValues.includes(typography[key]), "one-shot review: invalid typographyReview." + key);
  }
  assert.equal(typeof typography.cheapOverlayRisk, "boolean", "one-shot review: cheapOverlayRisk is required");
  assert.ok(["none", "provider_edit", "tracked_in_world", "native_end_card", "selective_caption", "regenerate"].includes(typography.selectedRepairMode), "one-shot review: invalid selectedRepairMode");
  assert.ok(nonEmpty(typography.notes), "one-shot review: typographyReview.notes is required");
  assert.ok(Array.isArray(review.issues), "one-shot review: issues must be an array");
  assert.ok(Array.isArray(review.repairScope), "one-shot review: repairScope must be an array");
  assert.equal(typeof review.sameConceptRetryAllowed, "boolean", "one-shot review: sameConceptRetryAllowed is required");
  assert.equal(review.paidRetryAuthorized, false, "one-shot review: review cannot authorize a paid retry");

  const hardSafetyPass = review.checks.claimsAndPrivacy === "PASS" && review.checks.technicalDecode === "PASS";
  if (review.decision === "ACCEPT_PICTURE") {
    assert.equal(review.earliestFailureStage, "none", "one-shot review: accepted picture cannot have a failure stage");
    for (const key of requiredChecks) assert.equal(review.checks[key], "PASS", "one-shot review: accepted picture requires all checks PASS");
    assert.equal(review.issues.length, 0, "one-shot review: accepted picture cannot keep open issues");
    assert.equal(review.repairScope.length, 0, "one-shot review: accepted picture cannot require repair");
    assert.equal(review.sameConceptRetryAllowed, false, "one-shot review: accepted picture cannot request retry");
    assert.equal(typography.cheapOverlayRisk, false, "one-shot review: accepted picture cannot keep cheap overlay risk");
    for (const key of ["integratedKeywords", "exactSurfaces", "captionTaste"]) assert.ok(["PASS", "NOT_APPLICABLE"].includes(typography[key]), "one-shot review: accepted picture requires typography PASS or NOT_APPLICABLE");
  }

  if (review.decision === "SURGICAL_FINISH") {
    assert.equal(review.checks.twoSecondComprehension, "PASS", "one-shot review: surgical finish requires opening comprehension PASS");
    assert.equal(review.checks.conceptSemantics, "PASS", "one-shot review: surgical finish requires concept semantics PASS");
    assert.equal(review.checks.promptConceptFit, "PASS", "one-shot review: surgical finish requires prompt fit PASS");
    assert.equal(review.checks.semanticMotionArc, "PASS", "one-shot review: surgical finish requires semantic motion PASS");
    assert.equal(review.checks.offerBinding, "PASS", "one-shot review: surgical finish requires offer binding PASS");
    assert.equal(hardSafetyPass, true, "one-shot review: surgical finish requires claims/privacy and decode PASS");
    assert.ok(review.repairScope.length > 0, "one-shot review: surgical finish requires a bounded repairScope");
    assert.ok(review.repairScope.length <= 5, "one-shot review: repairScope is too broad for surgical finish");
    assert.equal(review.sameConceptRetryAllowed, false, "one-shot review: surgical finish cannot also request regeneration");
    assert.notEqual(typography.selectedRepairMode, "regenerate", "one-shot review: surgical finish cannot select typography regeneration");
  }

  if (review.decision === "REGENERATE_SAME_CONCEPT") {
    assert.equal(review.checks.twoSecondComprehension, "PASS", "one-shot review: same-concept retry requires comprehension PASS");
    assert.equal(review.checks.conceptSemantics, "PASS", "one-shot review: same-concept retry requires concept semantics PASS");
    assert.equal(review.checks.promptConceptFit, "PASS", "one-shot review: same-concept retry requires prompt fit PASS");
    assert.equal(review.earliestFailureStage, "generation", "one-shot review: same-concept retry must fail first at generation");
    assert.equal(review.sameConceptRetryAllowed, true, "one-shot review: same-concept retry must be explicitly allowed");
    assert.ok(nonEmpty(review.retryHypothesis), "one-shot review: same-concept retry requires one retryHypothesis");
    assert.equal(review.repairScope.length, 0, "one-shot review: regeneration cannot carry a surgical repairScope");
  }

  if (review.decision === "RETURN_TO_CONCEPT") {
    assert.ok(["source", "concept", "prompt"].includes(review.earliestFailureStage), "one-shot review: return-to-concept must identify a source, concept, or prompt failure");
    assert.equal(review.sameConceptRetryAllowed, false, "one-shot review: return-to-concept cannot permit same-concept retry");
    assert.ok(nonEmpty(review.planningBlocker), "one-shot review: return-to-concept requires a planningBlocker");
  }

  assert.equal(review.distribution?.publishAllowed, false, "one-shot review: publishing must remain blocked");
  assert.equal(review.distribution?.activateAdsAllowed, false, "one-shot review: ad activation must remain blocked");
  if (requireFinalDelivery || finalDelivery) validateFinalDelivery(finalDelivery, review);
  return review;
}

export const finalDeliveryChecks = [
  "twoSecondComprehension", "stopAndContinueReason", "salesThesis", "semanticMotionEnding",
  "brandCtaPriceLegalClaims", "typographyAtSpeed", "privacyIdentity", "decodeDimensionsCodec",
  "timestampsCadence", "intendedAudioWindows", "providerSpeech", "voiceIsolation",
];
export function validateFinalDelivery(delivery, review) {
  assert.ok(delivery && delivery.schemaVersion === 1, "final delivery record required");
  assert.deepEqual(Object.keys(delivery).sort(), ["schemaVersion", "status", "jobId", "conceptId", "assetRef", "assetSha256", "reviewSha256", "checks", "taste", "distribution"].sort(), "unexpected final delivery fields");
  assert.match(delivery.assetSha256, /^[a-f0-9]{64}$/, "final media hash required");
  assert.match(delivery.reviewSha256, /^[a-f0-9]{64}$/, "final review hash required");
  assert.deepEqual(Object.keys(delivery.distribution ?? {}).sort(), ["activateAdsAllowed", "publishAllowed"], "unexpected final distribution permission");
  assert.equal(review.status, "REVIEWED", "final delivery requires reviewed final media");
  assert.equal(review.decision, "ACCEPT_PICTURE", "repair or retry is not final delivery");
  assert.equal(delivery.jobId, review.jobId); assert.equal(delivery.conceptId, review.conceptId);
  assert.equal(delivery.assetSha256, review.assetSha256, "final media differs from reviewed media");
  assert.equal(delivery.assetRef, review.assetRef, "final media reference drift");
  assert.equal(delivery.reviewSha256, payloadHash(review), "final media review changed");
  assert.equal(delivery.status, "DELIVERED_LOCAL_QC");
  assert.equal(delivery.distribution?.publishAllowed, false);
  assert.equal(delivery.distribution?.activateAdsAllowed, false);
  assert.deepEqual(Object.keys(delivery.checks ?? {}).sort(), [...finalDeliveryChecks].sort(), "final QC coverage incomplete");
  for (const check of finalDeliveryChecks) {
    assert.deepEqual(Object.keys(delivery.checks[check] ?? {}).sort(), ["evidence", "status"], "unexpected final QC fields");
    assert.equal(delivery.checks[check]?.status, "PASS", `final QC failed: ${check}`);
    assert.ok(nonEmpty(delivery.checks[check]?.evidence), `final QC evidence required: ${check}`);
  }
  const subject = { jobId: delivery.jobId, conceptId: delivery.conceptId, assetSha256: delivery.assetSha256, reviewSha256: delivery.reviewSha256, checks: delivery.checks };
  if (delivery.taste?.kind === "agent_delegation") {
    assert.deepEqual(Object.keys(delivery.taste).sort(), ["agentDelegation", "kind"], "AI final Taste must not impersonate a human");
    const delegation = delivery.taste.agentDelegation;
    validateRunDelegation(delegation, { area: "design", artifactHash: payloadHash(subject) });
    assert.ok(delegation.snapshot.run.scope.steps.some(step => step.id === delegation.receipt.stepId && step.skill === "performance-video-production"), "final Taste requires a production step");
  } else {
    assert.equal(delivery.taste?.kind, "human_conversation", "human or scoped AI final Taste required");
    assert.deepEqual(Object.keys(delivery.taste).sort(), ["kind", "providedBy", "recordedAt", "statement"], "human final Taste fields invalid");
    assert.ok(["user", "controller"].includes(delivery.taste.providedBy));
    assert.ok(nonEmpty(delivery.taste.statement) && Number.isFinite(Date.parse(delivery.taste.recordedAt)), "actual human final Taste evidence required");
  }
  return delivery;
}

function main() {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-one-shot-review.mjs <one-shot-review.json> [--require-reviewed] [--require-final-delivery --final-delivery <final-delivery.json>] [--one-shot-brief <one-shot-brief.json> | --standalone-review | --legacy-v1]");
  const review = JSON.parse(readFileSync(file, "utf8"));
  const briefIndex = process.argv.indexOf("--one-shot-brief");
  const briefFile = briefIndex >= 0 ? process.argv[briefIndex + 1] : null;
  const requireFinalDelivery = process.argv.includes("--require-final-delivery");
  const deliveryIndex = process.argv.indexOf("--final-delivery");
  const deliveryFile = deliveryIndex >= 0 ? process.argv[deliveryIndex + 1] : null;
  const finalDelivery = deliveryFile ? JSON.parse(readFileSync(path.resolve(deliveryFile), "utf8")) : null;
  const requireReviewed = process.argv.includes("--require-reviewed") || requireFinalDelivery;
  const standaloneReview = process.argv.includes("--standalone-review");
  const allowLegacyV1 = process.argv.includes("--legacy-v1");
  const brief = briefFile ? JSON.parse(readFileSync(path.resolve(briefFile), "utf8")) : null;
  if (brief) {
    assert.equal(brief.schemaVersion, 2, "one-shot review: upstream lineage brief must use schemaVersion 2");
    assert.equal(review.jobId, brief.jobId, "one-shot review: jobId mismatch with one-shot brief");
    assert.equal(review.conceptId, brief.conceptId, "one-shot review: conceptId mismatch with one-shot brief");
  }
  validateOneShotReview(review, {
    requireReviewed,
    expectedPrimaryOutcome: brief?.primaryOutcome ?? null,
    standaloneReview,
    allowLegacyV1, requireFinalDelivery, finalDelivery,
  });
  if (finalDelivery) {
    assert.equal(path.isAbsolute(finalDelivery.assetRef), false, "final asset must be job-relative");
    const asset = realpathSync(path.resolve(path.dirname(file), finalDelivery.assetRef));
    assert.ok(asset.startsWith(`${realpathSync(path.dirname(file))}${path.sep}`), "final asset escapes job directory");
    assert.equal(createHash("sha256").update(readFileSync(asset)).digest("hex"), finalDelivery.assetSha256, "final media bytes changed");
  }
  const outcomeMode = review.schemaVersion === 1 ? "legacy v1; no outcome-relative task evaluation" : review.primaryOutcome.status;
  console.log("One-shot review: PASS (" + review.decision + "; outcome " + outcomeMode + ")");
}

const isMain = (() => {
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); } catch { return false; }
})();

if (isMain) {
  try { main(); } catch (error) { console.error(error.message); process.exitCode = 1; }
}
