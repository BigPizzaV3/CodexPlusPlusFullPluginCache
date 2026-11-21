#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const READY = "READY_FOR_HUMAN_LAST_MILE_REVIEW";
const REQUIRED_AI_OWNERSHIP = [
  "creative_territory_recommendation",
  "hook_body_arc",
  "proof_strategy",
  "expression_policy",
  "editorial_tempo",
  "shot_routing",
  "provider_selection",
  "deterministic_finish",
  "quality_control_and_learning",
];
const REQUIRED_DECISIONS = [
  "territory_recommendation",
  "hook_body_arc",
  "proof_strategy",
  "expression_policy",
  "editorial_tempo",
  "shot_routing",
  "provider_selection",
  "deterministic_finish",
];
const ALLOWED_HUMAN_GATES = new Set([
  "blocking_canonical_conflict",
  "creative_premise_and_taste",
  "paid_generation_cost",
  "final_last_mile_taste_review",
  "external_distribution_and_activation",
]);

export function validateAiLedRun(run, { requireReady = false } = {}) {
  assert.equal(run.schemaVersion, 1, "AI-led run: unsupported schemaVersion");
  assert.ok(run.jobId, "AI-led run: jobId missing");
  assert.ok(["DRAFT", READY, "REVISE"].includes(run.status), "AI-led run: invalid status");
  assert.equal(run.mode, "ai_led_creative_director", "AI-led run: invalid mode");
  assert.equal(run.objective, "performance_ready_short_form_ad", "AI-led run: invalid objective");
  assert.equal(run.authority?.craftMicroDirectionsRequiredFromUser, false, "AI-led run: craft micro-directions cannot be delegated to the user");
  assert.equal(run.authority?.continueAutonomouslyWhenNonBlocking, true, "AI-led run: non-blocking production decisions must continue autonomously");
  assert.ok(Number.isInteger(run.authority?.maximumQuestionsPerBlockingGate) && run.authority.maximumQuestionsPerBlockingGate <= 3, "AI-led run: blocking gate questions must be capped at three");
  assert.ok(Array.isArray(run.authority?.aiOwnedDecisions), "AI-led run: aiOwnedDecisions missing");
  assert.ok(Array.isArray(run.authority?.humanGates), "AI-led run: humanGates missing");
  for (const gate of run.authority.humanGates) assert.ok(ALLOWED_HUMAN_GATES.has(gate), `AI-led run: production craft leaked into human gate ${gate}`);
  assert.ok(Array.isArray(run.decisionLog), "AI-led run: decisionLog missing");
  assert.equal(run.internalReview?.presentOnlyAfterInternalPass, true, "AI-led run: do not present before internal review passes");
  assert.ok(Array.isArray(run.internalReview?.cycles), "AI-led run: internal review cycles missing");
  assert.equal(run.performanceContract?.campaignEvidenceStatus, "NOT_RUN", "AI-led run: pre-campaign work cannot claim campaign evidence");
  assert.equal(run.performanceContract?.guaranteeMade, false, "AI-led run: performance guarantees are prohibited");
  assert.equal(run.distribution?.paidCallsRequireApproval, true, "AI-led run: every paid call needs approval");
  assert.equal(run.distribution?.publishAllowed, false, "AI-led run: publishing must remain blocked");
  assert.equal(run.distribution?.activateAdsAllowed, false, "AI-led run: ad activation must remain blocked");
  assert.equal(run.distribution?.publicSkillDistributionAllowed, false, "AI-led run: public Skill distribution must remain blocked");

  if (requireReady || run.status === READY) {
    assert.equal(run.status, READY, "AI-led run: not ready for human last-mile review");
    for (const decision of REQUIRED_AI_OWNERSHIP) {
      assert.ok(run.authority.aiOwnedDecisions.includes(decision), `AI-led run: AI ownership missing for ${decision}`);
    }
    assert.ok(run.authority.humanGates.includes("creative_premise_and_taste"), "AI-led run: Taste gate missing");
    assert.ok(run.authority.humanGates.includes("paid_generation_cost"), "AI-led run: paid-cost gate missing");
    assert.ok(run.authority.humanGates.includes("final_last_mile_taste_review"), "AI-led run: final Taste gate missing");
    assert.ok(run.authority.humanGates.includes("external_distribution_and_activation"), "AI-led run: distribution authority gate missing");

    const decisionIds = run.decisionLog.map((decision) => decision.decisionId);
    assert.equal(new Set(decisionIds).size, decisionIds.length, "AI-led run: duplicate decision IDs");
    for (const decisionId of REQUIRED_DECISIONS) {
      const decision = run.decisionLog.find((item) => item.decisionId === decisionId);
      assert.ok(decision, `AI-led run: missing craft decision ${decisionId}`);
      assert.ok(decision.choice && decision.rationale, `AI-led run ${decisionId}: choice and rationale required`);
      assert.ok(Array.isArray(decision.sourceRefs) && decision.sourceRefs.length > 0, `AI-led run ${decisionId}: source refs required`);
      assert.equal(decision.humanDirectionRequired, false, `AI-led run ${decisionId}: craft decision cannot require user micro-direction`);
    }

    const requiredReviews = ["creative_performance_pass", "natural_speed_master_pass"];
    for (const reviewId of requiredReviews) {
      const cycle = run.internalReview.cycles.find((item) => item.reviewId === reviewId);
      assert.ok(cycle, `AI-led run: missing internal review ${reviewId}`);
      assert.equal(cycle.result, "PASS", `AI-led run: internal review ${reviewId} must pass`);
      for (const issue of cycle.issuesFound ?? []) {
        assert.ok(cycle.issuesFixedBeforePresentation?.includes(issue), `AI-led run ${reviewId}: unresolved issue was exposed to the user: ${issue}`);
      }
    }

    const performance = run.performanceContract;
    for (const field of ["hypothesisId", "responseHypothesis", "primaryMetric", "variableModule"]) {
      assert.ok(performance?.[field] && performance[field] !== "UNRESOLVED", `AI-led run: performance ${field} unresolved`);
    }
    assert.ok(Array.isArray(performance.guardrailMetrics) && performance.guardrailMetrics.length > 0 && !performance.guardrailMetrics.includes("UNRESOLVED"), "AI-led run: guardrail metrics unresolved");
    assert.ok(Array.isArray(performance.fixedModules) && performance.fixedModules.length > 0 && !performance.fixedModules.includes("UNRESOLVED"), "AI-led run: fixed modules unresolved");
    assert.equal(performance.destinationContinuity, "PASS", "AI-led run: destination continuity must pass");
    assert.equal(run.baseline?.validation, "PASS", "AI-led run: first-pass baseline validation must pass");
  }

  return { jobId: run.jobId, status: run.status, decisions: run.decisionLog.length, reviews: run.internalReview.cycles.length };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-ai-led-run.mjs <ai-led-run.json> [--require-ready]");
  const result = validateAiLedRun(JSON.parse(await readFile(file, "utf8")), { requireReady: process.argv.includes("--require-ready") });
  console.log(`AI-led creative director: PASS (${result.jobId} / ${result.decisions} decisions / ${result.reviews} internal reviews)`);
}
