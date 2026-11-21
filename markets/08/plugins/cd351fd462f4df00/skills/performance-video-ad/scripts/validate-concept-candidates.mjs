#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync, realpathSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const statuses = ["DRAFT", "AWAITING_TASTE", "SELECTED", "RETURN_TO_CONCEPT"];
const policyModes = ["comparison", "user_supplied_preference"];
const selectionModes = ["pending", "agent_selected", "human_selected", "user_supplied"];
const routes = ["one_shot_first", "one_shot_plus_finish", "controlled_sequence", "deterministic_demo", "blocked"];
const risks = ["low", "medium", "high"];
const eligibilityStates = ["eligible_for_generation", "controlled_only", "blocked"];
const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;
const score = (value, label) => assert.ok(Number.isInteger(value) && value >= 1 && value <= 5, `${label} must be 1-5`);

function validateSourceContext(sourceContext, { ready }) {
  assert.ok(sourceContext && typeof sourceContext === "object", "concept candidates: sourceContext is required");
  assert.ok(["fresh_lock", "verified_reuse"].includes(sourceContext.mode), "concept candidates: invalid sourceContext.mode");
  if (!ready) return;
  assert.ok(Array.isArray(sourceContext.canonicalSourceRefs) && sourceContext.canonicalSourceRefs.length > 0, "concept candidates: ready comparison requires canonicalSourceRefs");
  assert.ok(nonEmpty(sourceContext.checkedAt), "concept candidates: ready comparison requires sourceContext.checkedAt");
  assert.ok(["none", "resolved"].includes(sourceContext.materialChangeStatus), "concept candidates: unresolved source changes block concept comparison");
  if (sourceContext.mode === "verified_reuse") {
    assert.ok(nonEmpty(sourceContext.sourceJobRef), "concept candidates: verified reuse requires sourceJobRef");
    assert.ok(nonEmpty(sourceContext.reuseReason), "concept candidates: verified reuse requires reuseReason");
  }
}

function validateCandidate(candidate, { ready }) {
  for (const field of ["conceptId", "title", "oneSentence", "openingEvent0_2s", "painfulSituation", "falseResponse", "surprisingReframe", "offerRole", "visibleCausalEvent", "requiredEndState"]) {
    assert.ok(nonEmpty(candidate[field]), `concept candidate ${candidate.conceptId ?? "<unknown>"}: ${field} is required`);
  }
  assert.ok(/^[a-z0-9][a-z0-9-]{2,63}$/.test(candidate.conceptId), `concept candidate ${candidate.conceptId}: invalid conceptId`);
  assert.equal(typeof candidate.motionCarriesMeaning, "boolean", `concept candidate ${candidate.conceptId}: motionCarriesMeaning is required`);
  assert.ok(routes.includes(candidate.routeRecommendation), `concept candidate ${candidate.conceptId}: invalid routeRecommendation`);
  assert.ok(eligibilityStates.includes(candidate.eligibility), `concept candidate ${candidate.conceptId}: invalid eligibility`);

  const commercial = candidate.commercialStrength;
  assert.ok(commercial && typeof commercial === "object", `concept candidate ${candidate.conceptId}: commercialStrength is required`);
  for (const key of ["whoRelevance", "twoSecondComprehension", "semanticTension", "offerConnection", "trust", "clickCuriosity", "overall"]) score(commercial[key], `concept candidate ${candidate.conceptId}: commercialStrength.${key}`);
  assert.ok(nonEmpty(commercial.rationale), `concept candidate ${candidate.conceptId}: commercial rationale is required`);

  const generation = candidate.generationSolvability;
  assert.ok(generation && typeof generation === "object", `concept candidate ${candidate.conceptId}: generationSolvability is required`);
  for (const key of ["singleWorldCoherence", "lowReadingBurden", "deviationTolerance", "identityFeasibility", "endingFeasibility", "audioOptionalComprehension", "overall"]) score(generation[key], `concept candidate ${candidate.conceptId}: generationSolvability.${key}`);
  assert.ok(nonEmpty(generation.rationale), `concept candidate ${candidate.conceptId}: generation rationale is required`);

  const risk = candidate.riskProfile;
  assert.ok(risk && typeof risk === "object", `concept candidate ${candidate.conceptId}: riskProfile is required`);
  for (const key of ["exactSurfaceDependency", "identityRisk", "claimRisk", "privacyRisk", "continuityRisk"]) assert.ok(risks.includes(risk[key]), `concept candidate ${candidate.conceptId}: invalid riskProfile.${key}`);

  assert.ok(Array.isArray(candidate.mustReadCopy) && candidate.mustReadCopy.length <= 5, `concept candidate ${candidate.conceptId}: mustReadCopy must contain at most five units`);
  candidate.mustReadCopy.forEach((copy, index) => {
    assert.equal(copy.order, index + 1, `concept candidate ${candidate.conceptId}: mustReadCopy order must be contiguous`);
    assert.ok(nonEmpty(copy.text), `concept candidate ${candidate.conceptId}: copy text is required`);
    assert.ok([...copy.text].length <= 48, `concept candidate ${candidate.conceptId}: must-read copy must stay short`);
    assert.ok(["verbatim_quote", "paraphrase", "synthesized_copy", "creative_hypothesis"].includes(copy.derivationType), `concept candidate ${candidate.conceptId}: invalid derivationType`);
    assert.ok(Array.isArray(copy.sourceRefs) && copy.sourceRefs.length > 0, `concept candidate ${candidate.conceptId}: copy requires sourceRefs`);
  });
  if (ready) assert.ok(Array.isArray(candidate.sourceRefs) && candidate.sourceRefs.length > 0, `concept candidate ${candidate.conceptId}: sourceRefs are required`);

  if (["one_shot_first", "one_shot_plus_finish"].includes(candidate.routeRecommendation)) {
    assert.equal(candidate.motionCarriesMeaning, true, `concept candidate ${candidate.conceptId}: One-shot route requires semantic motion`);
    assert.notEqual(risk.exactSurfaceDependency, "high", `concept candidate ${candidate.conceptId}: high exact-surface dependency requires a controlled route`);
    assert.notEqual(risk.privacyRisk, "high", `concept candidate ${candidate.conceptId}: high privacy risk blocks external One-shot generation`);
    assert.ok(generation.overall >= 3, `concept candidate ${candidate.conceptId}: One-shot route requires generation solvability of at least 3`);
  }
  if (risk.privacyRisk === "high") assert.equal(candidate.eligibility, "blocked", `concept candidate ${candidate.conceptId}: high privacy risk must be blocked`);
  if (candidate.routeRecommendation === "blocked") assert.equal(candidate.eligibility, "blocked", `concept candidate ${candidate.conceptId}: blocked route requires blocked eligibility`);
}

export function validateConceptCandidates(document, { requireTasteReady = false, requireSelected = false, oneShotBrief = null } = {}) {
  assert.equal(document.schemaVersion, 1, "concept candidates: unsupported schemaVersion");
  assert.equal(document.contractType, "performance_video_concept_candidates", "concept candidates: invalid contractType");
  for (const field of ["jobId", "offerId", "salesThesisId"]) assert.ok(nonEmpty(document[field]), `concept candidates: ${field} is required`);
  assert.ok(statuses.includes(document.status), "concept candidates: invalid status");
  assert.equal(document.performanceClaim, false, "concept candidates: planning candidates cannot claim performance");

  const policy = document.candidatePolicy;
  assert.ok(policy && typeof policy === "object", "concept candidates: candidatePolicy is required");
  assert.ok(policyModes.includes(policy.mode), "concept candidates: invalid candidatePolicy.mode");
  assert.equal(typeof policy.userRequestedConceptComparison, "boolean", "concept candidates: userRequestedConceptComparison is required");
  const expectedMinimum = policy.mode === "comparison" ? 3 : 1;
  assert.equal(policy.minimumCandidateCount, expectedMinimum, `concept candidates: ${policy.mode} requires minimumCandidateCount ${expectedMinimum}`);

  const ready = document.status !== "DRAFT";
  validateSourceContext(document.sourceContext, { ready });
  assert.ok(Array.isArray(document.candidates), "concept candidates: candidates must be an array");
  if (ready || requireTasteReady || requireSelected) assert.ok(document.candidates.length >= expectedMinimum, `concept candidates: ${policy.mode} requires at least ${expectedMinimum} candidate(s)`);
  const conceptIds = new Set();
  for (const candidate of document.candidates) {
    validateCandidate(candidate, { ready: ready || requireTasteReady || requireSelected });
    assert.ok(!conceptIds.has(candidate.conceptId), `concept candidates: duplicate conceptId ${candidate.conceptId}`);
    conceptIds.add(candidate.conceptId);
  }

  const decision = document.decision;
  assert.ok(decision && typeof decision === "object", "concept candidates: decision is required");
  assert.ok(selectionModes.includes(decision.selectionMode), "concept candidates: invalid decision.selectionMode");
  if (decision.recommendedConceptId !== null) assert.ok(conceptIds.has(decision.recommendedConceptId), "concept candidates: recommended concept does not exist");
  if (ready || requireTasteReady || requireSelected) {
    assert.ok(nonEmpty(decision.recommendedConceptId), "concept candidates: ready comparison requires a recommendation");
    assert.ok(nonEmpty(decision.recommendationReason), "concept candidates: recommendationReason is required");
  }

  if (document.status === "AWAITING_TASTE") {
    assert.equal(policy.userRequestedConceptComparison, true, "concept candidates: AWAITING_TASTE requires explicit concept comparison");
    assert.equal(decision.selectionMode, "pending", "concept candidates: AWAITING_TASTE requires pending selection");
    assert.equal(decision.selectedConceptId, null, "concept candidates: AWAITING_TASTE cannot preselect a concept");
  }

  if (document.status === "SELECTED" || requireSelected) {
    assert.ok(nonEmpty(decision.selectedConceptId) && conceptIds.has(decision.selectedConceptId), "concept candidates: selected concept must exist");
    assert.ok(nonEmpty(decision.selectionReason), "concept candidates: selectionReason is required");
    assert.ok(nonEmpty(decision.decidedAt), "concept candidates: decidedAt is required");
    if (policy.userRequestedConceptComparison) {
      assert.equal(decision.selectionMode, "human_selected", "concept candidates: an explicit comparison requires human selection");
    } else {
      assert.ok(["agent_selected", "human_selected", "user_supplied"].includes(decision.selectionMode), "concept candidates: selected concept requires a valid selection mode");
    }
    if (["human_selected", "user_supplied"].includes(decision.selectionMode)) assert.ok(nonEmpty(decision.humanTasteEvidence), "concept candidates: human-selected concept requires Taste evidence");
  }

  if (requireTasteReady) assert.ok(["AWAITING_TASTE", "SELECTED"].includes(document.status), "concept candidates: Taste-ready status is required");
  if (oneShotBrief) {
    assert.equal(document.status, "SELECTED", "concept candidates: One-shot handoff requires SELECTED status");
    assert.equal(oneShotBrief.jobId, document.jobId, "concept candidates: One-shot brief jobId mismatch");
    assert.equal(oneShotBrief.offerId, document.offerId, "concept candidates: One-shot brief offerId mismatch");
    assert.equal(oneShotBrief.salesThesisId, document.salesThesisId, "concept candidates: One-shot brief salesThesisId mismatch");
    assert.equal(oneShotBrief.conceptId, decision.selectedConceptId, "concept candidates: One-shot brief must inherit the selected conceptId");
  }

  assert.equal(document.distribution?.publishAllowed, false, "concept candidates: publishing must remain blocked");
  assert.equal(document.distribution?.activateAdsAllowed, false, "concept candidates: ad activation must remain blocked");
  return document;
}

function main() {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-concept-candidates.mjs <concept-candidates.json> [--require-taste-ready] [--require-selected] [--one-shot-brief <file>]");
  const document = JSON.parse(readFileSync(file, "utf8"));
  const briefIndex = process.argv.indexOf("--one-shot-brief");
  const oneShotBrief = briefIndex >= 0 ? JSON.parse(readFileSync(path.resolve(process.argv[briefIndex + 1]), "utf8")) : null;
  validateConceptCandidates(document, {
    requireTasteReady: process.argv.includes("--require-taste-ready"),
    requireSelected: process.argv.includes("--require-selected"),
    oneShotBrief,
  });
  console.log(`Concept candidates: PASS (${document.status})`);
}

const isMain = (() => {
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); } catch { return false; }
})();

if (isMain) {
  try { main(); } catch (error) { console.error(error.message); process.exitCode = 1; }
}
