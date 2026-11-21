#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { loadExpressionProfiles, validatePortfolio } from "./validate-hook-portfolio.mjs";
import { resolveExpressionPolicy } from "./resolve-expression-policy.mjs";
import { validateExpressionIntensity } from "./validate-expression-intensity.mjs";
import { assertAnimaticApproved, validateAnimaticRecord } from "./validate-animatic-gate.mjs";
import { validateBodyContract } from "./validate-body-contract.mjs";
import { validateHookBodyFit } from "./validate-hook-body-fit.mjs";
import { validateJapaneseNaturalness } from "./validate-japanese-naturalness.mjs";
import { validateDestinationContinuity } from "./validate-destination-continuity.mjs";
import { validateTestSemantics } from "./validate-test-semantics.mjs";
import { validateSourceAssembly } from "./validate-source-assembly.mjs";
import { validateCopyLineage } from "./validate-copy-lineage.mjs";
import { validateHookHandoff } from "./validate-hook-handoff.mjs";
import { validateInsightRenderMap } from "./validate-insight-render-map.mjs";
import { validatePacingReview } from "./validate-pacing-review.mjs";
import { validateSemanticStory } from "./validate-semantic-story.mjs";
import { validateContextResolution } from "./validate-context-resolution.mjs";
import { validateFunnelRoleContract } from "./validate-funnel-role-contract.mjs";
import { validateFunnelMessageFit } from "./validate-funnel-message-fit.mjs";
import { validateFunnelContextFit } from "./validate-funnel-context-fit.mjs";
import { DISCOVERY_FILES, validateCreativeDiscovery } from "./validate-creative-discovery.mjs";
import { validateShotDependencyGraph } from "./validate-shot-dependency-graph.mjs";
import { validateSoundIntentMap } from "./validate-sound-intent-map.mjs";
import { validateVisualTreatmentContract } from "./validate-visual-treatment-contract.mjs";
import { validateCompositingFeasibility } from "../../performance-video-production/scripts/validate-compositing-feasibility.mjs";

const jobDir = process.argv[2] ? path.resolve(process.argv[2]) : null;
assert.ok(jobDir, "Usage: node scripts/validate-artifacts.mjs <job-dir>");

const requiredFiles = [
  "strategy-snapshot.json",
  "creative-context.json",
  "expression-policy.json",
  "creative-brief.json",
  "test-batch.json",
  "incidents.json",
  "creative-hypotheses.json",
  "hook-packages.json",
  "body-family.json",
  "hook-portfolio-approval.json",
  "beat-sheet.json",
  "animatic-review.json",
  "shot-manifest.json",
  "route-plan.json",
  "cost-estimate.json",
  "approval.json",
];
const sourceAssemblyFiles = [
  "offer-context.json",
  "source-manifest.json",
  "source-coverage-report.json",
  "insight-evidence-map.json",
  "creative-premise.json",
  "message-inheritance-contract.json",
  "copy-lineage.json",
];
const optionalFiles = [
  "sales-thesis.json",
  "destination-contract.json",
  "context-resolution.json",
  "funnel-role-contract.json",
  "structure-options.json",
  "structure-approval.json",
  "hook-handoff.json",
  "insight-render-map.json",
  "pacing-review.json",
  "sound-intent-map.json",
  "shot-dependency-graph.json",
  "visual-treatment-contract.json",
  "compositing-feasibility-gate.json",
  ...DISCOVERY_FILES,
  ...sourceAssemblyFiles,
];

const documents = new Map();
for (const file of requiredFiles) {
  const value = JSON.parse(await readFile(path.join(jobDir, file), "utf8"));
  documents.set(file, value);
}
for (const file of optionalFiles) {
  try {
    const value = JSON.parse(await readFile(path.join(jobDir, file), "utf8"));
    documents.set(file, value);
  } catch (error) {
    if (error.code !== "ENOENT") throw error;
  }
}
const supportedSchemaVersionsByArtifact = new Map([
  ["creative-premise.json", [1, 2]],
  ["offer-context.json", [1, 2]],
  ["source-manifest.json", [1, 2]],
]);
for (const [file, value] of documents) {
  const supportedSchemaVersions = supportedSchemaVersionsByArtifact.get(file) ?? [1];
  assert.ok(supportedSchemaVersions.includes(value.schemaVersion), `${file}: unsupported schemaVersion`);
  assert.ok(value.jobId, `${file}: jobId missing`);
}
const jobIds = new Set([...documents.values()].map((document) => document.jobId));
assert.equal(jobIds.size, 1, "jobId mismatch across artifacts");

const testBatch = documents.get("test-batch.json");
const strategySnapshot = documents.get("strategy-snapshot.json");
const destinationContract = documents.get("destination-contract.json");
const contextResolution = documents.get("context-resolution.json");
const funnelRoleContract = documents.get("funnel-role-contract.json");
const creativeContext = documents.get("creative-context.json");
const expressionPolicy = documents.get("expression-policy.json");
const funnelRoleRequired = strategySnapshot.funnelRoleVersion === 1;
if (funnelRoleRequired) {
  assert.ok(contextResolution, "funnelRoleVersion=1 requires context-resolution.json");
  assert.ok(funnelRoleContract, "funnelRoleVersion=1 requires funnel-role-contract.json");
}
if (contextResolution) validateContextResolution(contextResolution);
if (funnelRoleContract) validateFunnelRoleContract(funnelRoleContract);
assert.ok(["baseline_build", "initial_hook_test", "single_revision", "production_pick"].includes(testBatch.batchType), "test-batch.json: invalid batchType");
assert.deepEqual(testBatch.testVariables, ["hook_package"], "test-batch.json: testVariables must be [hook_package]");
for (const variable of ["audience", "offer", "body_family", "promise", "proof", "cta", "destination", "platform", "placement", "duration"]) {
  assert.ok(testBatch.fixedVariables.includes(variable), `test-batch.json: fixedVariables must include ${variable}`);
}
if (testBatch.batchType === "baseline_build") {
  assert.equal(testBatch.minimumHookPackages, 1, "test-batch.json: baseline build requires exactly one Hook Package");
  assert.equal(testBatch.targetHookPackages, 1, "test-batch.json: baseline build targets exactly one Hook Package");
} else if (testBatch.batchType === "initial_hook_test") {
  assert.ok(testBatch.minimumHookPackages >= 6, "test-batch.json: initial Hook test requires at least six Hooks");
  assert.ok(testBatch.targetHookPackages >= 8, "test-batch.json: initial Hook test must target at least eight Hooks");
}
if (testBatch.status !== "DRAFT") {
  assert.ok(testBatch.bodyFamilyId, "test-batch.json: active batch requires bodyFamilyId");
  assert.ok(testBatch.learningQuestion, "test-batch.json: active batch requires learningQuestion");
  assert.equal(creativeContext.status, "CONTEXT_CLASSIFIED", "active batch requires classified Creative Context");
  assert.equal(expressionPolicy.status, "POLICY_RESOLVED", "active batch requires resolved Expression Policy");
  assert.deepEqual(expressionPolicy, resolveExpressionPolicy(creativeContext), "expression-policy.json does not match the source-backed resolver output");
  if (testBatch.testSemanticsVersion === 1) {
    assert.ok(destinationContract, "testSemanticsVersion=1 requires destination-contract.json");
    assert.equal(destinationContract.status, "DESTINATION_REVIEWED", "active batch requires a reviewed destination contract");
    validateDestinationContinuity(destinationContract);
  }
}

// Optional direction records are internal/non-gating compatibility artifacts.
const structureOptions = documents.get("structure-options.json");
const structureApproval = documents.get("structure-approval.json");
if (structureOptions?.status === "AWAITING_STRUCTURE_CONSULTATION") {
  assert.ok(structureOptions.options.length >= 2 && structureOptions.options.length <= 3, "optional direction sprint requires two or three routes");
  const mechanisms = new Set(structureOptions.options.map((option) => option.mechanism));
  assert.equal(mechanisms.size, structureOptions.options.length, "optional direction routes must use distinct mechanisms");
  const required = ["id", "mechanism", "incident", "openingEvent0_2s", "hookCopy", "visualArc", "aiMotionValue", "deterministicFinish", "risk", "learningQuestion", "recommended"];
  for (const option of structureOptions.options) {
    for (const field of required) assert.ok(Object.hasOwn(option, field), `structure option ${option.id ?? "<unknown>"}: ${field} missing`);
  }
  assert.ok(structureOptions.options.filter((option) => option.recommended === true).length <= 1, "optional direction sprint may recommend at most one route");
}
if (structureApproval) {
  assert.equal(structureApproval.approvalScope, "BATCH_DIRECTION_ONLY", "legacy structure approval scope must remain BATCH_DIRECTION_ONLY");
  if (structureApproval.decision === "approved") {
    assert.ok(structureOptions, "approved optional direction requires structure-options.json");
    assert.ok(structureApproval.selectedOptionId, "approved optional direction requires selectedOptionId");
    assert.ok(structureOptions.options.some((option) => option.id === structureApproval.selectedOptionId), "selected optional direction does not exist");
  }
}

const portfolio = documents.get("hook-packages.json");
const hookHypotheses = documents.get("creative-hypotheses.json");
const bodyFamily = documents.get("body-family.json");
const portfolioApproval = documents.get("hook-portfolio-approval.json");
const beatSheet = documents.get("beat-sheet.json");
const animaticReview = documents.get("animatic-review.json");
const shotManifest = documents.get("shot-manifest.json");
const routePlan = documents.get("route-plan.json");
const costEstimate = documents.get("cost-estimate.json");
const paidApproval = documents.get("approval.json");
const shotDependencyGraph = documents.get("shot-dependency-graph.json");
const soundIntentMap = documents.get("sound-intent-map.json");
const visualTreatment = documents.get("visual-treatment-contract.json");
const compositingFeasibility = documents.get("compositing-feasibility-gate.json");
if (shotDependencyGraph) validateShotDependencyGraph(shotDependencyGraph);
if (soundIntentMap) validateSoundIntentMap(soundIntentMap, { requireReady: animaticReview.decision === "approved" });
const visualTreatmentRequired = strategySnapshot.visualTreatmentVersion === 1;
if (visualTreatmentRequired) {
  assert.ok(visualTreatment && compositingFeasibility, "visualTreatmentVersion=1 requires the treatment and compositing feasibility artifacts");
}
assert.equal(Boolean(visualTreatment), Boolean(compositingFeasibility), "Visual Treatment and compositing feasibility artifacts must be present together");
if (visualTreatment && compositingFeasibility) {
  validateVisualTreatmentContract(visualTreatment);
  validateCompositingFeasibility(visualTreatment, compositingFeasibility);
}
if (portfolio.packages.length > 0 || testBatch.status !== "DRAFT") {
  if (funnelRoleRequired) {
    validateFunnelContextFit(contextResolution, funnelRoleContract);
  }
}
const expressionProfiles = portfolio.expressionContractVersion === 2 ? await loadExpressionProfiles() : null;
validateAnimaticRecord(animaticReview);

const presentSourceAssemblyFiles = sourceAssemblyFiles.filter((file) => documents.has(file));
const sourceAssemblyRequired = documents.get("strategy-snapshot.json").sourceAssemblyVersion === 1;
if (sourceAssemblyRequired) assert.equal(presentSourceAssemblyFiles.length, sourceAssemblyFiles.length, "sourceAssemblyVersion=1 requires every source assembly artifact");
assert.ok(presentSourceAssemblyFiles.length === 0 || presentSourceAssemblyFiles.length === sourceAssemblyFiles.length, "source assembly artifacts must be all present or all absent");
const sourceAssemblyEnabled = presentSourceAssemblyFiles.length === sourceAssemblyFiles.length;
if (sourceAssemblyEnabled && documents.get("offer-context.json").status === "OFFER_SOURCE_LOCKED") {
  await validateSourceAssembly(jobDir, { requirePremiseApproval: portfolio.packages.length > 0 });
}
if (sourceAssemblyEnabled && portfolio.packages.length > 0) {
  assert.equal(documents.get("offer-context.json").status, "OFFER_SOURCE_LOCKED", "Hook generation is blocked until Offer Source Lock is complete");
  assert.equal(documents.get("source-coverage-report.json").gate_status, "PASS", "Hook generation is blocked until Source Coverage passes");
  assert.equal(documents.get("creative-premise.json").approval.decision, "approved", "Hook generation is blocked until Creative Premise approval");
}

const presentDiscoveryFiles = DISCOVERY_FILES.filter((file) => documents.has(file));
const discoveryRequired = strategySnapshot.creativeDiscoveryVersion === 1;
if (discoveryRequired) assert.equal(presentDiscoveryFiles.length, DISCOVERY_FILES.length, "creativeDiscoveryVersion=1 requires every creative discovery artifact");
assert.ok(presentDiscoveryFiles.length === 0 || presentDiscoveryFiles.length === DISCOVERY_FILES.length, "creative discovery artifacts must be all present or all absent");
if (presentDiscoveryFiles.length === DISCOVERY_FILES.length) {
  const knownSourceIds = sourceAssemblyEnabled && documents.get("source-manifest.json").sources.length > 0
    ? new Set(documents.get("source-manifest.json").sources.map((source) => source.source_id))
    : null;
  const discoveryResult = validateCreativeDiscovery({
    feltBrief: documents.get("felt-brief.json"),
    tensionMap: documents.get("creative-tension-map.json"),
    territories: documents.get("creative-territories.json"),
    firstFrameBoard: documents.get("first-frame-board.json"),
    hookLoops: documents.get("three-second-hook-loops.json"),
    reactionMap: documents.get("intended-reaction-map.json"),
    tasteReview: documents.get("taste-review.json"),
  }, { requireSelected: portfolio.packages.length > 0 || testBatch.status !== "DRAFT", knownSourceIds });
  if (portfolio.packages.length > 0 || testBatch.status !== "DRAFT") {
    assert.equal(testBatch.selectedTerritoryId, discoveryResult.selectedTerritoryId, "test-batch.json must inherit the human-approved Territory");
    assert.equal(portfolio.creativeTerritoryId, discoveryResult.selectedTerritoryId, "hook-packages.json must inherit the human-approved Territory");
  }
}

const bodyContracts = [];
if (portfolio.bodyContractVersion === 1) {
  assert.ok(Array.isArray(portfolio.bodyContractFiles) && portfolio.bodyContractFiles.length > 0, "Body contract files are required");
  for (const entry of portfolio.bodyContractFiles) {
    assert.ok(entry.bodyFamilyId && entry.file, "Every Body contract file entry requires bodyFamilyId and file");
    assert.equal(path.isAbsolute(entry.file), false, `Body contract path must be relative: ${entry.file}`);
    const contractPath = path.resolve(jobDir, entry.file);
    assert.ok(contractPath.startsWith(`${jobDir}${path.sep}`), `Body contract path escapes job directory: ${entry.file}`);
    const contract = JSON.parse(await readFile(contractPath, "utf8"));
    assert.equal(contract.jobId, portfolio.jobId, `${entry.file}: jobId mismatch`);
    assert.equal(contract.body_family_id, entry.bodyFamilyId, `${entry.file}: body family ID mismatch`);
    validateBodyContract(contract);
    if (funnelRoleRequired && funnelRoleContract.funnel_stage === "cold_clickthrough_ad" && funnelRoleContract.next_destination.role === "full_persuasion") {
      assert.equal(contract.funnelRoleBodyVersion, 1, `${entry.file}: cold clickthrough Body requires Funnel Role Body v1`);
      assert.equal(contract.stage_role_mode, "qualified_curiosity", `${entry.file}: cold clickthrough Body must use qualified_curiosity mode`);
    }
    validateJapaneseNaturalness(contract);
    bodyContracts.push(contract);
    documents.set(entry.file, contract);
  }
  validateHookBodyFit(portfolio, bodyContracts);
  validateJapaneseNaturalness(portfolio);
  if (portfolio.bodyFamilyMode === "consultation_cohorts") {
    assert.equal(testBatch.status, "DRAFT", "Multi-Body consultation cannot be an active controlled batch");
    assert.equal(testBatch.bodyFamilyId, null, "Multi-Body consultation cannot lock one test Body");
    assert.equal(portfolioApproval.decision, "pending", "Multi-Body consultation must split into controlled jobs before approval");
    assert.equal(bodyFamily.status, "DRAFT_NOT_LOCKED", "Legacy body-family.json must remain an unlocked placeholder during Body split consultation");
    assert.equal(bodyFamily.bodyFamilyId, null, "Legacy body-family.json cannot claim one Body during split consultation");
  }
}

const semanticBodyContracts = bodyContracts.filter((contract) => contract.semanticStrengthVersion === 1);
if (semanticBodyContracts.length > 0) {
  for (const file of ["hook-handoff.json", "insight-render-map.json", "pacing-review.json"]) {
    assert.ok(documents.has(file), `semanticStrengthVersion=1 requires ${file}`);
  }
  const hookHandoff = documents.get("hook-handoff.json");
  const insightRenderMap = documents.get("insight-render-map.json");
  const pacingReview = documents.get("pacing-review.json");
  validateHookHandoff(hookHandoff);
  validateInsightRenderMap(insightRenderMap);
  validatePacingReview(pacingReview);
  for (const contract of semanticBodyContracts) {
    validateSemanticStory({ expressionPolicy, bodyContract: contract, hookHandoff, insightRenderMap, pacingReview });
  }
}

if (sourceAssemblyEnabled && portfolio.packages.length > 0) {
  const lineage = documents.get("copy-lineage.json");
  assert.ok(["READY", "VERIFIED"].includes(lineage.status), "Hook generation requires READY or VERIFIED copy lineage");
  if (funnelRoleRequired) validateFunnelMessageFit(funnelRoleContract, lineage);
  if (bodyContracts.length === 0) validateCopyLineage(lineage, { hookPackages: portfolio, bodyContract: null });
  for (const contract of bodyContracts) validateCopyLineage(lineage, { hookPackages: portfolio, bodyContract: contract });
}

assert.equal(portfolioApproval.approvalScope, "HOOK_PORTFOLIO_AND_BODY_FAMILY", "Hook portfolio approval scope is invalid");
assert.equal(portfolio.batchType, testBatch.batchType, "batchType mismatch between test batch and Hook portfolio");
if (["baseline_build", "initial_hook_test"].includes(testBatch.batchType)) {
  assert.equal(portfolio.minimumPackages, testBatch.minimumHookPackages, "minimum Hook count mismatch between test batch and portfolio");
  assert.equal(portfolio.targetPackages, testBatch.targetHookPackages, "target Hook count mismatch between test batch and portfolio");
}
if (portfolio.packages.length > 0) {
  validatePortfolio(portfolio, expressionProfiles);
  assert.equal(expressionPolicy.status, "POLICY_RESOLVED", "Hook portfolio requires resolved Expression Policy");
  validateExpressionIntensity(portfolio, expressionPolicy);
  if (testBatch.testSemanticsVersion === 1 || portfolio.testSemanticsVersion === 1) {
    validateTestSemantics(testBatch, portfolio);
  }
  assert.equal(portfolio.bodyFamilyId, testBatch.bodyFamilyId, "bodyFamilyId mismatch between test batch and Hook portfolio");
  if (portfolio.hookModelVersion === 2) {
    assert.equal(hookHypotheses.hookModelVersion, 2, "creative-hypotheses.json requires hookModelVersion=2");
    assert.ok(Array.isArray(hookHypotheses.hypotheses) && hookHypotheses.hypotheses.length > 0, "Hook hypotheses must not be empty");
    const hypothesisById = new Map();
    for (const hypothesis of hookHypotheses.hypotheses) {
      for (const field of ["id", "family", "workIncident", "pain", "contradiction", "unresolvedQuestion", "productLinkage", "sourceEvidence"]) {
        assert.ok(Object.hasOwn(hypothesis, field), `Hook hypothesis ${hypothesis.id ?? "<unknown>"}: ${field} missing`);
      }
      assert.ok(hypothesis.sourceEvidence?.type && hypothesis.sourceEvidence?.ref, `Hook hypothesis ${hypothesis.id}: sourceEvidence requires type and ref`);
      assert.ok(!hypothesisById.has(hypothesis.id), `duplicate Hook hypothesis: ${hypothesis.id}`);
      hypothesisById.set(hypothesis.id, hypothesis);
    }
    for (const item of portfolio.packages) {
      const hypothesis = hypothesisById.get(item.hypothesisId);
      assert.ok(hypothesis, `Hook ${item.id}: unknown hypothesisId ${item.hypothesisId}`);
      assert.equal(item.hypothesisFamily, hypothesis.family, `Hook ${item.id}: hypothesisFamily mismatch`);
    }
  }
}

const beatBlocked = beatSheet.status.includes("BLOCKED_BY_HOOK_PORTFOLIO_APPROVAL");
const shotsBlockedByHook = shotManifest.status.includes("BLOCKED_BY_HOOK_PORTFOLIO_APPROVAL");
const shotsBlockedByAnimatic = shotManifest.status.includes("BLOCKED_BY_ANIMATIC_APPROVAL");
const shotsBlocked = shotsBlockedByHook || shotsBlockedByAnimatic;
const routeBlocked =
  typeof routePlan.status === "string"
    ? routePlan.status.includes("BLOCKED")
    : !Array.isArray(routePlan.routes) || routePlan.routes.length === 0;

if (portfolioApproval.decision !== "approved") {
  assert.ok(beatBlocked, "beat sheet must remain blocked before Hook portfolio approval");
  assert.ok(shotsBlockedByHook, "shot manifest must identify Hook portfolio approval as the current blocker");
  assert.ok(routeBlocked, "route plan must remain blocked before Hook portfolio approval");
  assert.notEqual(animaticReview.decision, "approved", "Animatic cannot be approved before Hook portfolio approval");
  assert.notEqual(costEstimate.status, "AWAITING_EXPLICIT_APPROVAL", "cost approval cannot be requested before Hook portfolio approval");
  assert.equal(paidApproval.paidRunAllowed, false, "paid execution cannot be enabled before Hook portfolio approval");
} else {
  validatePortfolio(portfolio, expressionProfiles);
  assert.ok(portfolioApproval.portfolioId, "approved Hook portfolio requires portfolioId");
  assert.equal(portfolioApproval.portfolioId, portfolio.portfolioId, "approved portfolioId mismatch");
  assert.ok(portfolioApproval.bodyFamilyId, "approved Hook portfolio requires bodyFamilyId");
  assert.equal(portfolioApproval.bodyFamilyId, portfolio.bodyFamilyId, "approved Body family mismatch");
  assert.equal(bodyFamily.status, "LOCKED", "approved Hook portfolio requires a locked Body family");
  assert.equal(bodyFamily.bodyFamilyId, portfolio.bodyFamilyId, "Body family artifact mismatch");
  assert.ok(portfolioApproval.approvedPackageIds.length >= testBatch.minimumHookPackages, "approved Hook count is below batch minimum");
  assert.equal(new Set(portfolioApproval.approvedPackageIds).size, portfolioApproval.approvedPackageIds.length, "approved Hook IDs must be unique");
  const packageIds = new Set(portfolio.packages.map((item) => item.id));
  for (const id of portfolioApproval.approvedPackageIds) assert.ok(packageIds.has(id), `approved Hook does not exist: ${id}`);

  if (animaticReview.decision !== "approved") {
    assert.ok(shotsBlockedByAnimatic, "shot manifest must identify Animatic approval as the current blocker");
    assert.ok(routeBlocked, "route plan must remain blocked before Animatic approval");
    assert.ok(routePlan.status.includes("ANIMATIC_APPROVAL"), "route plan must identify Animatic approval as the current blocker");
    assert.notEqual(costEstimate.status, "AWAITING_EXPLICIT_APPROVAL", "cost approval cannot be requested before Animatic approval");
    assert.equal(paidApproval.paidRunAllowed, false, "paid execution cannot be enabled before Animatic approval");
  } else {
    assertAnimaticApproved(animaticReview, portfolio, bodyFamily, jobDir);
    assert.deepEqual(new Set(animaticReview.reviewedPackageIds), new Set(portfolioApproval.approvedPackageIds), "Animatic review must cover every approved Hook");
  }
}

if (!beatBlocked) {
  assert.equal(portfolioApproval.decision, "approved", "Hook portfolio approval is required before beat compilation");
  assert.equal(beatSheet.bodyFamilyId, bodyFamily.bodyFamilyId, "beat sheet Body family mismatch");
  assert.ok(beatSheet.approvedPackageIds.length > 0, "unblocked beat sheet requires approvedPackageIds");
}
if (!shotsBlocked) {
  assert.equal(portfolioApproval.decision, "approved", "Hook portfolio approval is required before shot compilation");
  assert.equal(animaticReview.decision, "approved", "Animatic approval is required before shot compilation");
  assert.equal(shotManifest.bodyFamilyId, bodyFamily.bodyFamilyId, "shot manifest Body family mismatch");
  assert.ok(shotManifest.approvedPackageIds.length > 0, "unblocked shot manifest requires approvedPackageIds");
}
if (!routeBlocked) {
  assert.equal(shotsBlocked, false, "route plan cannot unlock before shot manifest");
  assert.equal(animaticReview.decision, "approved", "route plan cannot unlock before Animatic approval");
}
if (costEstimate.status === "AWAITING_EXPLICIT_APPROVAL") {
  assert.equal(routeBlocked, false, "cost approval cannot be requested before routing");
  assert.equal(portfolioApproval.decision, "approved", "cost approval requires Hook portfolio approval");
  assert.equal(animaticReview.decision, "approved", "cost approval requires Animatic approval");
}
if (paidApproval.decision !== "approved") assert.equal(paidApproval.paidRunAllowed, false, "pending paid approval cannot allow paid execution");
if (paidApproval.paidRunAllowed === true) {
  assert.equal(paidApproval.decision, "approved", "paidRunAllowed requires approved paid decision");
  assert.equal(portfolioApproval.decision, "approved", "paidRunAllowed requires Hook portfolio approval");
  assert.equal(animaticReview.decision, "approved", "paidRunAllowed requires Animatic approval");
  assert.equal(routeBlocked, false, "paidRunAllowed requires an unlocked route plan");
  assert.equal(costEstimate.status, "AWAITING_EXPLICIT_APPROVAL", "paidRunAllowed requires a current cost estimate");
}

const serialized = [...documents.values()].map((value) => JSON.stringify(value)).join("\n");
for (const marker of ["sk-", "FAL_KEY=", "FAL_API_KEY=", "GOOGLE_API_KEY=", "BYTEPLUS_API_KEY="]) {
  assert.equal(serialized.includes(marker), false, `possible secret leaked: ${marker}`);
}

console.log(`Artifact contract: PASS (${documents.size} files, jobId=${[...jobIds][0]})`);
const paidExecutionState = paidApproval.paidRunAllowed
  ? "approved_for_execution"
  : paidApproval.decision === "approved"
    ? `not_executable:${paidApproval.executionState ?? "approval_consumed_or_disabled"}`
    : paidApproval.decision;
console.log(`Optional direction: ${structureApproval?.decision ?? "omitted"}; Hook portfolio: ${portfolioApproval.decision}; Animatic: ${animaticReview.decision}; paid: ${paidExecutionState}`);
