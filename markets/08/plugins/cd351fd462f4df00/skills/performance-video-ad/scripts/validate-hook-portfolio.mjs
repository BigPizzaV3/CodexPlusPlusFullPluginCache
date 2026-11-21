#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateHookDiversity } from "./validate-hook-diversity.mjs";

const REQUIRED_FIXED_VARIABLES = [
  "audience",
  "offer",
  "body_family",
  "promise",
  "proof",
  "cta",
  "destination",
  "platform",
  "placement",
  "duration",
];

const REQUIRED_PACKAGE_FIELDS = [
  "id",
  "mechanism",
  "incidentId",
  "formatOrigin",
  "hookCopy",
  "openingComposition",
  "openingEvent",
  "firstSound",
  "firstCutSeconds",
  "sourceEvidence",
  "learningRationale",
];

const PROFILE_IDS = ["restrained_b2b_social", "balanced_social_brand", "spectacle_experiment"];
const SELECTION_CRITERIA = [
  "who_relevance",
  "problem_understanding_within_2s",
  "unresolved_question",
  "offer_connection",
  "trust",
  "compatible_body_connection",
  "production_ease",
  "visual_novelty",
];
const PRIMARY_RECOMMENDATION_REASONS = new Set(SELECTION_CRITERIA.slice(0, 6));

export async function loadExpressionProfiles() {
  const skillDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
  const profiles = new Map();
  for (const id of PROFILE_IDS) {
    const file = path.join(skillDir, "assets", "expression-profiles", `${id.replaceAll("_", "-")}.json`);
    const profile = JSON.parse(await readFile(file, "utf8"));
    assert.equal(profile.id, id, `${file}: expression profile ID mismatch`);
    assert.ok(profile.motionRules && profile.creativeChecks && profile.portfolioPolicy, `${id}: incomplete expression profile`);
    profiles.set(id, profile);
  }
  return profiles;
}

function validateExpressionControl(item, profile) {
  const control = item.expressionControl;
  assert.ok(control && typeof control === "object", `Hook ${item.id}: expressionControl missing`);
  assert.ok(typeof control.vfxIndependent === "boolean", `Hook ${item.id}: vfxIndependent must be boolean`);
  assert.ok(Number.isFinite(control.problemUnderstoodBySeconds), `Hook ${item.id}: problemUnderstoodBySeconds missing`);
  assert.ok(typeof control.painBeforeSpectacle === "boolean", `Hook ${item.id}: painBeforeSpectacle must be boolean`);
  assert.ok(typeof control.realisticWorkSurface === "boolean", `Hook ${item.id}: realisticWorkSurface must be boolean`);
  assert.ok(profile.workSurfaces.includes(control.workSurface), `Hook ${item.id}: workSurface is not allowed by ${profile.id}`);
  assert.ok(Array.isArray(control.sceneActions) && control.sceneActions.length > 0, `Hook ${item.id}: sceneActions must be a non-empty array`);
  assert.ok(control.sceneActions.length <= profile.motionRules.maxSceneActions, `Hook ${item.id}: too many actions for ${profile.id}`);
  assert.ok(profile.motionRules.allowedCameraGrammar.includes(control.cameraGrammar), `Hook ${item.id}: cameraGrammar is not allowed by ${profile.id}`);
  assert.ok(profile.motionRules.allowedSoundIntensity.includes(control.soundIntensity), `Hook ${item.id}: soundIntensity is not allowed by ${profile.id}`);
  assert.equal(control.brandTreatment, profile.motionRules.brandTreatment, `Hook ${item.id}: brandTreatment must match ${profile.id}`);
  assert.ok(control.problemUnderstoodBySeconds <= profile.creativeChecks.problemUnderstoodBySeconds, `Hook ${item.id}: work problem must be understood by ${profile.creativeChecks.problemUnderstoodBySeconds}s`);
  if (profile.creativeChecks.vfxIndependentRequired) assert.equal(control.vfxIndependent, true, `Hook ${item.id}: must survive without VFX`);
  if (profile.creativeChecks.painBeforeSpectacle) assert.equal(control.painBeforeSpectacle, true, `Hook ${item.id}: Pain must appear before visual technique`);
  if (profile.creativeChecks.realisticWorkSurfaceRequired) assert.equal(control.realisticWorkSurface, true, `Hook ${item.id}: must open on a realistic work surface`);

  const expressionText = [item.openingComposition, item.openingEvent, item.aiMotionBrief, item.firstSound].filter(Boolean).join("\n").toLowerCase();
  for (const pattern of profile.motionRules.prohibitedPatterns) {
    assert.equal(expressionText.includes(pattern.toLowerCase()), false, `Hook ${item.id}: prohibited ${profile.id} pattern found: ${pattern}`);
  }

  if (profile.portfolioPolicy.requiresPermissionOrPurpose) {
    assert.equal(item.candidateStatus, "experimental_only", `Hook ${item.id}: spectacle must remain experimental_only`);
    const hasPurpose = typeof control.experimentPurpose === "string" && control.experimentPurpose.trim().length > 0;
    assert.ok(control.explicitUserPermission === true || hasPurpose, `Hook ${item.id}: spectacle requires explicit permission or experimentPurpose`);
  }
}

export function validatePortfolio(portfolio, expressionProfiles = null) {
  assert.equal(portfolio.schemaVersion, 1, "unsupported schemaVersion");
  assert.ok(portfolio.portfolioId, "portfolioId missing");
  const isBodyConsultation = portfolio.bodyContractVersion === 1 && portfolio.bodyFamilyMode === "consultation_cohorts";
  if (isBodyConsultation) assert.equal(portfolio.bodyFamilyId, null, "Body consultation cannot claim one fixed bodyFamilyId");
  else assert.ok(portfolio.bodyFamilyId, "bodyFamilyId missing");
  assert.ok(["baseline_build", "initial_hook_test", "single_revision", "production_pick"].includes(portfolio.batchType), `Unknown batchType: ${portfolio.batchType}`);
  assert.ok(Array.isArray(portfolio.fixedVariables), "fixedVariables must be an array");
  for (const variable of REQUIRED_FIXED_VARIABLES) {
    assert.ok(portfolio.fixedVariables.includes(variable), `fixedVariables must include ${variable}`);
  }
  assert.deepEqual(portfolio.testVariables, ["hook_package"], "creative isolation requires testVariables=[hook_package]");
  assert.ok(portfolio.learningQuestion, "learningQuestion missing");
  assert.ok(Array.isArray(portfolio.packages) && portfolio.packages.length > 0, "Hook Package list must not be empty");

  if (portfolio.batchType === "baseline_build") {
    assert.equal(portfolio.minimumPackages, 1, "baseline_build requires minimumPackages=1");
    assert.equal(portfolio.targetPackages, 1, "baseline_build requires targetPackages=1");
    assert.equal(portfolio.packages.length, 1, "baseline_build builds exactly one selected-Territory ad before optimization");
    assert.equal(portfolio.sourcePortfolioId ?? null, null, "baseline_build must not cite a prior portfolio");
    assert.equal(portfolio.sourceHookPackageId ?? null, null, "baseline_build must not cite a prior Hook");
  } else if (portfolio.batchType === "initial_hook_test") {
    assert.ok(Number.isInteger(portfolio.minimumPackages) && portfolio.minimumPackages >= 6, "initial_hook_test minimumPackages must be at least 6");
    assert.ok(Number.isInteger(portfolio.targetPackages) && portfolio.targetPackages >= 8, "initial_hook_test targetPackages must be at least 8");
    assert.ok(portfolio.packages.length >= portfolio.minimumPackages, `initial_hook_test requires at least ${portfolio.minimumPackages} Hook Packages`);
    assert.equal(portfolio.sourcePortfolioId ?? null, null, "initial_hook_test must not cite a source portfolio");
    assert.equal(portfolio.sourceHookPackageId ?? null, null, "initial_hook_test must not cite a source Hook");
  } else {
    assert.ok(portfolio.sourcePortfolioId, `${portfolio.batchType} requires sourcePortfolioId`);
    assert.ok(portfolio.sourceHookPackageId, `${portfolio.batchType} requires sourceHookPackageId`);
  }

  assert.equal(new Set(portfolio.packages.map((item) => item.id)).size, portfolio.packages.length, "Hook IDs must be unique");
  for (const item of portfolio.packages) {
    for (const field of REQUIRED_PACKAGE_FIELDS) {
      assert.ok(Object.hasOwn(item, field), `Hook ${item.id ?? "<unknown>"}: ${field} missing`);
    }
    assert.ok(typeof item.hookCopy === "string" && item.hookCopy.trim(), `Hook ${item.id}: hookCopy must be non-empty`);
    assert.ok(typeof item.mechanism === "string" && item.mechanism.trim(), `Hook ${item.id}: mechanism must be non-empty`);
    assert.ok(typeof item.incidentId === "string" && item.incidentId.trim(), `Hook ${item.id}: incidentId must be non-empty`);
    assert.ok(typeof item.openingComposition === "string" && item.openingComposition.trim(), `Hook ${item.id}: openingComposition must be non-empty`);
    assert.ok(typeof item.openingEvent === "string" && item.openingEvent.trim(), `Hook ${item.id}: openingEvent must be non-empty`);
    assert.ok(typeof item.firstSound === "string" && item.firstSound.trim(), `Hook ${item.id}: firstSound must be non-empty`);
    assert.ok(Number.isFinite(item.firstCutSeconds) && item.firstCutSeconds > 0, `Hook ${item.id}: firstCutSeconds must be positive`);
    assert.ok(item.sourceEvidence && typeof item.sourceEvidence === "object", `Hook ${item.id}: sourceEvidence must be an object`);
    assert.ok(item.sourceEvidence.type && item.sourceEvidence.ref, `Hook ${item.id}: sourceEvidence requires type and ref`);
    assert.ok(typeof item.learningRationale === "string" && item.learningRationale.trim(), `Hook ${item.id}: learningRationale must be non-empty`);
  }

  let expressionProfileCounts = null;
  if (portfolio.expressionContractVersion === 2) {
    assert.ok(expressionProfiles instanceof Map, "expressionContractVersion 2 requires loaded expression profiles");
    assert.ok(expressionProfiles.has(portfolio.expression_profile), `unknown portfolio expression_profile ${portfolio.expression_profile}`);
    assert.deepEqual(portfolio.selectionCriteria, SELECTION_CRITERIA, "selectionCriteria priority order is invalid");
    expressionProfileCounts = new Map(PROFILE_IDS.map((id) => [id, 0]));
    for (const item of portfolio.packages) {
      const profile = expressionProfiles.get(item.expression_profile);
      assert.ok(profile, `Hook ${item.id}: unknown expression_profile ${item.expression_profile}`);
      assert.ok(typeof item.candidateStatus === "string" && item.candidateStatus.trim(), `Hook ${item.id}: candidateStatus missing`);
      assert.ok(PRIMARY_RECOMMENDATION_REASONS.has(item.primaryRecommendationReason), `Hook ${item.id}: primaryRecommendationReason must prioritize relevance, understanding, question, offer, trust, or Body connection`);
      validateExpressionControl(item, profile);
      expressionProfileCounts.set(profile.id, expressionProfileCounts.get(profile.id) + 1);
    }
    if (portfolio.packages.length === 8) {
      if (portfolio.expression_profile === "restrained_b2b_social") {
        assert.ok(expressionProfileCounts.get("restrained_b2b_social") >= 6, "restrained-default eight-Hook portfolio requires at least six restrained_b2b_social Hooks");
        assert.ok(expressionProfileCounts.get("balanced_social_brand") <= 1, "restrained-default eight-Hook portfolio allows at most one balanced_social_brand Hook");
      }
      assert.ok(expressionProfileCounts.get("spectacle_experiment") <= 1, "eight-Hook portfolio allows at most one spectacle_experiment Hook");
    }
  }

  const hookDiversity = portfolio.hookModelVersion === 2 ? validateHookDiversity(portfolio) : null;

  const mechanismCounts = new Map();
  for (const item of portfolio.packages) mechanismCounts.set(item.mechanism, (mechanismCounts.get(item.mechanism) ?? 0) + 1);
  if (portfolio.batchType === "initial_hook_test") {
    assert.ok(mechanismCounts.size >= 3, "initial_hook_test requires at least three distinct mechanisms");
    const largestMechanism = Math.max(...mechanismCounts.values());
    assert.ok(largestMechanism <= portfolio.packages.length / 2, "no mechanism may occupy more than half of an initial Hook portfolio");
  }

  const count = (origin) => portfolio.packages.filter((item) => item.formatOrigin === origin).length;
  const total = portfolio.packages.length;
  const grounded = count("grounded_evergreen");
  const trend = count("trend_adapted");
  const experimental = count("experimental");
  assert.equal(grounded + trend + experimental, total, "Unknown formatOrigin found");
  for (const item of portfolio.packages.filter((entry) => entry.formatOrigin === "trend_adapted")) {
    assert.ok(item.formatWrapperId, `trend-adapted Hook requires formatWrapperId: ${item.id}`);
  }

  if (portfolio.portfolioMode === "grounded_only") {
    assert.equal(grounded, total, "grounded_only requires every Hook to be grounded or evergreen");
  } else if (portfolio.portfolioMode === "balanced_default") {
    assert.ok(grounded / total >= 2 / 3, "balanced_default requires at least two-thirds grounded Hooks");
    assert.ok(trend / total <= 0.2, "balanced_default caps trend-adapted Hooks at 20%");
    assert.ok(experimental / total <= 0.2, "balanced_default caps experimental Hooks at 20%");
  } else if (portfolio.portfolioMode === "trend_exploration") {
    assert.equal(portfolio.explicitTrendRequest, true, "trend_exploration requires an explicit trend request");
    assert.ok(grounded / total >= 0.5, "trend_exploration requires at least half grounded Hooks");
    assert.ok(trend / total <= 0.34, "trend_exploration caps trend-adapted Hooks at 34%");
    assert.ok(experimental / total <= 0.17, "trend_exploration caps experimental Hooks at 17%");
  } else {
    throw new Error(`Unknown portfolioMode: ${portfolio.portfolioMode}`);
  }

  return { grounded, trend, experimental, total, mechanisms: mechanismCounts.size, expressionProfileCounts, hookDiversity };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-hook-portfolio.mjs <hook-packages.json>");
  const portfolio = JSON.parse(await readFile(file, "utf8"));
  const profiles = portfolio.expressionContractVersion === 2 ? await loadExpressionProfiles() : null;
  const result = validatePortfolio(portfolio, profiles);
  console.log(`Hook portfolio: PASS (${result.total} Hooks / ${result.mechanisms} mechanisms / ${result.grounded} grounded / ${result.trend} trend / ${result.experimental} experimental)`);
  if (result.expressionProfileCounts) {
    console.log(`Expression profiles: ${PROFILE_IDS.map((id) => `${id}=${result.expressionProfileCounts.get(id)}`).join(" / ")}`);
  }
  if (result.hookDiversity) {
    console.log(`Diversity: ${result.hookDiversity.hypothesisFamilies} hypotheses / ${result.hookDiversity.attentionMechanisms} attention mechanisms / ${result.hookDiversity.visualGrammars} visual grammars`);
  }
}
