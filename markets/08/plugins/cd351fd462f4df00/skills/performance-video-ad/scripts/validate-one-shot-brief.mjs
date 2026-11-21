#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync, realpathSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const routes = ["one_shot_first", "one_shot_plus_finish", "controlled_sequence", "deterministic_demo", "blocked"];
const risks = ["low", "medium", "high"];
const statuses = ["DRAFT", "NEEDS_SOURCE_INPUT", "READY_FOR_GENERATION"];
const typographyStrategies = ["integrated_keyword_first", "exact_finish_first", "no_on_screen_text"];
const captionPolicies = ["none", "selective", "full_accessibility"];
const typographyRoles = ["hook", "reframe", "offer", "payoff"];
const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;

function validatePrimaryOutcome(primaryOutcome) {
  assert.ok(primaryOutcome && typeof primaryOutcome === "object" && !Array.isArray(primaryOutcome), "one-shot brief: primaryOutcome is required");
  assert.equal(primaryOutcome.status, "grounded", "one-shot brief: primaryOutcome.status must be grounded");
  assert.ok(nonEmpty(primaryOutcome.statement), "one-shot brief: primaryOutcome.statement is required");
  assert.ok(Array.isArray(primaryOutcome.sourceRefs) && primaryOutcome.sourceRefs.length > 0, "one-shot brief: primaryOutcome.sourceRefs are required");
  assert.equal(new Set(primaryOutcome.sourceRefs).size, primaryOutcome.sourceRefs.length, "one-shot brief: primaryOutcome.sourceRefs must be unique");
}

export function validateOneShotBrief(brief, { requireReady = false, expectedPrimaryOutcome = null, allowLegacyV1 = false } = {}) {
  assert.ok([1, 2].includes(brief.schemaVersion), "one-shot brief: unsupported schemaVersion");
  assert.equal(brief.contractType, "performance_video_one_shot_brief", "one-shot brief: invalid contractType");
  for (const field of ["jobId", "offerId", "salesThesisId", "conceptId"]) {
    assert.ok(nonEmpty(brief[field]), "one-shot brief: " + field + " is required");
  }
  if (brief.schemaVersion === 2) {
    validatePrimaryOutcome(brief.primaryOutcome);
    if (expectedPrimaryOutcome !== null) {
      assert.deepEqual(brief.primaryOutcome, expectedPrimaryOutcome, "one-shot brief: primaryOutcome lineage mismatch with offer context");
    }
  } else {
    if (requireReady) assert.equal(allowLegacyV1, true, "one-shot brief: ready schemaVersion 1 requires explicit --legacy-v1 compatibility mode");
    assert.equal(expectedPrimaryOutcome, null, "one-shot brief: legacy schemaVersion 1 cannot claim v2 primaryOutcome lineage");
  }
  assert.ok(statuses.includes(brief.status), "one-shot brief: invalid status");
  assert.ok(routes.includes(brief.routeDecision), "one-shot brief: invalid routeDecision");
  if (requireReady) assert.equal(brief.status, "READY_FOR_GENERATION", "one-shot brief: ready status is required");

  assert.ok(nonEmpty(brief.audience), "one-shot brief: audience is required");
  assert.ok(nonEmpty(brief.moment), "one-shot brief: moment is required");
  assert.ok(nonEmpty(brief.singleSellReason), "one-shot brief: singleSellReason is required");
  assert.ok(nonEmpty(brief.stopReason), "one-shot brief: stopReason is required");
  assert.ok(nonEmpty(brief.continueReason), "one-shot brief: continueReason is required");
  assert.notEqual(brief.stopReason.trim(), brief.continueReason.trim(), "one-shot brief: stopReason and continueReason must be distinct");
  assert.ok(nonEmpty(brief.falseResponse), "one-shot brief: falseResponse is required");
  assert.ok(nonEmpty(brief.surprisingReframe), "one-shot brief: surprisingReframe is required");
  assert.ok(nonEmpty(brief.offerRole), "one-shot brief: offerRole is required");
  assert.ok(nonEmpty(brief.cta), "one-shot brief: cta is required");

  assert.ok(nonEmpty(brief.visualConcept?.oneSentence), "one-shot brief: visualConcept.oneSentence is required");
  assert.ok(nonEmpty(brief.visualConcept?.requiredEndState), "one-shot brief: visualConcept.requiredEndState is required");
  assert.equal(typeof brief.visualConcept?.motionCarriesMeaning, "boolean", "one-shot brief: visualConcept.motionCarriesMeaning is required");
  assert.ok(Array.isArray(brief.semanticMotionArc) && brief.semanticMotionArc.length >= 4 && brief.semanticMotionArc.length <= 8, "one-shot brief: semanticMotionArc must contain four to eight stages");
  brief.semanticMotionArc.forEach((stage, index) => {
    assert.equal(stage.order, index + 1, "one-shot brief: semanticMotionArc order must be contiguous");
    assert.ok(nonEmpty(stage.action), "one-shot brief: semanticMotionArc action is required");
    assert.ok(nonEmpty(stage.viewerMeaning), "one-shot brief: semanticMotionArc viewerMeaning is required");
  });

  assert.ok(Array.isArray(brief.mustReadCopy) && brief.mustReadCopy.length >= 1 && brief.mustReadCopy.length <= 5, "one-shot brief: mustReadCopy must contain one to five units");
  brief.mustReadCopy.forEach((item, index) => {
    assert.equal(item.order, index + 1, "one-shot brief: mustReadCopy order must be contiguous");
    assert.ok(nonEmpty(item.text), "one-shot brief: mustReadCopy text is required");
    assert.ok([...item.text].length <= 48, "one-shot brief: must-read copy must stay short");
    assert.ok(["truth_critical", "action_critical", "comprehension_critical"].includes(item.exactness), "one-shot brief: invalid mustReadCopy exactness");
    assert.ok(Array.isArray(item.sourceRefs) && item.sourceRefs.length > 0, "one-shot brief: mustReadCopy requires sourceRefs");
  });

  const typography = brief.typographyPlan;
  assert.ok(typography && typeof typography === "object", "one-shot brief: typographyPlan is required");
  assert.ok(typographyStrategies.includes(typography.strategy), "one-shot brief: invalid typographyPlan.strategy");
  assert.ok(Array.isArray(typography.integratedKeywords) && typography.integratedKeywords.length <= 3, "one-shot brief: integratedKeywords must contain at most three units");
  typography.integratedKeywords.forEach((item, index) => {
    assert.equal(item.order, index + 1, "one-shot brief: integratedKeywords order must be contiguous");
    assert.ok(nonEmpty(item.text), "one-shot brief: integrated keyword text is required");
    assert.ok([...item.text].length <= 24, "one-shot brief: integrated keyword must stay glance-readable");
    assert.ok(typographyRoles.includes(item.role), "one-shot brief: invalid integrated keyword role");
    assert.ok(Array.isArray(item.sourceRefs) && item.sourceRefs.length > 0, "one-shot brief: integrated keyword requires sourceRefs");
  });
  assert.ok(Array.isArray(typography.exactSurfaces), "one-shot brief: exactSurfaces must be an array");
  typography.exactSurfaces.forEach((item) => {
    assert.ok(nonEmpty(item.text), "one-shot brief: exact surface text is required");
    assert.ok(["brand", "cta", "price", "quantified_claim", "legal", "proof"].includes(item.role), "one-shot brief: invalid exact surface role");
  });
  assert.ok(captionPolicies.includes(typography.captionPolicy), "one-shot brief: invalid captionPolicy");
  assert.ok(nonEmpty(typography.captionReason), "one-shot brief: captionReason is required");
  assert.ok(nonEmpty(typography.fallback), "one-shot brief: typography fallback is required");
  if (typography.strategy === "integrated_keyword_first") assert.ok(typography.integratedKeywords.length > 0, "one-shot brief: integrated_keyword_first requires at least one integrated keyword");
  if (typography.strategy === "no_on_screen_text") assert.equal(typography.integratedKeywords.length, 0, "one-shot brief: no_on_screen_text cannot declare integrated keywords");
  const actionCriticalCopy = brief.mustReadCopy.filter((item) => item.exactness === "action_critical").map((item) => item.text);
  const exactSurfaceText = new Set(typography.exactSurfaces.map((item) => item.text));
  for (const text of actionCriticalCopy) assert.ok(exactSurfaceText.has(text), "one-shot brief: action-critical copy must be owned by exactSurfaces");

  const suitability = brief.suitability;
  assert.ok(suitability && typeof suitability === "object", "one-shot brief: suitability is required");
  for (const key of ["exactSurfaceDependency", "identityRisk", "claimRisk", "privacyRisk", "continuityRisk"]) {
    assert.ok(risks.includes(suitability[key]), "one-shot brief: invalid suitability." + key);
  }
  for (const key of ["commercialStrength", "generationSolvability"]) {
    assert.ok(Number.isInteger(suitability[key]) && suitability[key] >= 1 && suitability[key] <= 5, "one-shot brief: suitability." + key + " must be 1-5");
  }

  assert.ok(Array.isArray(brief.modelFreedom?.macroLocks) && brief.modelFreedom.macroLocks.length > 0, "one-shot brief: macroLocks are required");
  assert.ok(Array.isArray(brief.modelFreedom?.delegatedToModel) && brief.modelFreedom.delegatedToModel.length > 0, "one-shot brief: delegatedToModel is required");
  assert.ok(Array.isArray(brief.noGos) && brief.noGos.length > 0, "one-shot brief: noGos are required");
  assert.ok(nonEmpty(brief.exactnessFallback?.strategy), "one-shot brief: exactness fallback strategy is required");
  assert.ok(Array.isArray(brief.sourceRefs) && brief.sourceRefs.length > 0, "one-shot brief: sourceRefs are required");

  if (["one_shot_first", "one_shot_plus_finish"].includes(brief.routeDecision)) {
    assert.equal(brief.visualConcept.motionCarriesMeaning, true, "one-shot brief: One-shot route requires motion to carry meaning");
    assert.notEqual(suitability.exactSurfaceDependency, "high", "one-shot brief: high exact-surface dependency requires a controlled route");
    assert.notEqual(suitability.privacyRisk, "high", "one-shot brief: high privacy risk blocks external One-shot generation");
    assert.ok(suitability.generationSolvability >= 3, "one-shot brief: One-shot route requires generation solvability of at least 3");
  }
  if (brief.routeDecision === "blocked") {
    assert.notEqual(brief.status, "READY_FOR_GENERATION", "one-shot brief: blocked route cannot be ready");
  }
  if (brief.routeDecision === "deterministic_demo") {
    assert.equal(brief.visualConcept.motionCarriesMeaning, false, "one-shot brief: deterministic demo should not claim model-owned semantic motion");
  }

  assert.equal(brief.distribution?.publishAllowed, false, "one-shot brief: publishing must remain blocked");
  assert.equal(brief.distribution?.activateAdsAllowed, false, "one-shot brief: ad activation must remain blocked");
  return brief;
}

function main() {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-one-shot-brief.mjs <one-shot-brief.json> [--require-ready] [--offer-context <offer-context.json>] [--legacy-v1]");
  const brief = JSON.parse(readFileSync(file, "utf8"));
  const offerContextIndex = process.argv.indexOf("--offer-context");
  const offerContextFile = offerContextIndex >= 0 ? process.argv[offerContextIndex + 1] : null;
  const requireReady = process.argv.includes("--require-ready");
  const allowLegacyV1 = process.argv.includes("--legacy-v1");
  if (requireReady && brief.schemaVersion === 2) assert.ok(offerContextFile, "one-shot brief: v2 --require-ready requires --offer-context for primaryOutcome lineage");
  const offerContext = offerContextFile ? JSON.parse(readFileSync(path.resolve(offerContextFile), "utf8")) : null;
  if (offerContext) assert.equal(offerContext.schemaVersion, 2, "one-shot brief: lineage offer context must use schemaVersion 2");
  validateOneShotBrief(brief, { requireReady, expectedPrimaryOutcome: offerContext?.primaryOutcome ?? null, allowLegacyV1 });
  const suffix = brief.schemaVersion === 1 ? "; legacy v1, no outcome-relative task evaluation" : "; grounded primaryOutcome bound";
  console.log("One-shot brief: PASS (" + brief.routeDecision + suffix + ")");
}

const isMain = (() => {
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); } catch { return false; }
})();

if (isMain) {
  try { main(); } catch (error) { console.error(error.message); process.exitCode = 1; }
}
