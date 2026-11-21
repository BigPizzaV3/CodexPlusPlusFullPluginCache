#!/usr/bin/env node
import assert from "node:assert/strict";
import { realpathSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateCreativePremise } from "./validate-creative-premise-gate.mjs";
import { validateMessageInheritance } from "./validate-message-inheritance.mjs";
import { validateCopyLineage } from "./validate-copy-lineage.mjs";
import { validateSalesThesis } from "./validate-sales-thesis.mjs";

export const SOURCE_PRECEDENCE = [
  "user_designated_canonical",
  "approved_offer_decision",
  "offer_current_lp_or_spec",
  "offer_voc_research_or_interview",
  "global_project_strategy",
  "general_method_or_trend",
];

const SOURCE_FILES = [
  "offer-context.json",
  "source-manifest.json",
  "source-coverage-report.json",
  "insight-evidence-map.json",
  "creative-premise.json",
  "message-inheritance-contract.json",
  "copy-lineage.json",
];

const sorted = (items) => [...items].sort();
const sourceIdFromRef = (ref) => String(ref).split("#", 1)[0];
const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;

export function validatePrimaryOutcome(primaryOutcome, sourceById, offerId, label = "primary outcome") {
  assert.ok(primaryOutcome && typeof primaryOutcome === "object" && !Array.isArray(primaryOutcome), `${label}: primaryOutcome is required`);
  assert.equal(primaryOutcome.status, "grounded", `${label}: primaryOutcome.status must be grounded`);
  assert.ok(nonEmpty(primaryOutcome.statement), `${label}: primaryOutcome.statement is required`);
  assert.ok(Array.isArray(primaryOutcome.sourceRefs) && primaryOutcome.sourceRefs.length > 0, `${label}: primaryOutcome.sourceRefs are required`);
  assert.equal(new Set(primaryOutcome.sourceRefs).size, primaryOutcome.sourceRefs.length, `${label}: primaryOutcome.sourceRefs must be unique`);
  for (const ref of primaryOutcome.sourceRefs) {
    const sourceId = sourceIdFromRef(ref);
    assert.ok(sourceById.has(sourceId), `${label}: primaryOutcome references unknown source ${ref}`);
    const source = sourceById.get(sourceId);
    assert.equal(source.read_status, "read", `${label}: primaryOutcome source ${sourceId} was not read`);
    assert.notEqual(source.role, "background_only", `${label}: primaryOutcome source ${sourceId} is background_only`);
    assert.ok(!["global_project_strategy", "general_method_or_trend"].includes(source.canonical_level), `${label}: primaryOutcome source ${sourceId} is global/general rather than outcome authority`);
    if (source.outcome_eligibility === "request_origin") {
      assert.equal(source.canonical_level, "user_designated_canonical", `${label}: request-origin outcome source ${sourceId} must be user-designated canonical evidence`);
      assert.ok(source.offer_id === null || source.offer_id === offerId, `${label}: request-origin outcome source ${sourceId} belongs to a different offer`);
    } else if (source.outcome_eligibility === "same_offer_authoritative") {
      assert.equal(source.role, "canonical_offer", `${label}: same-offer outcome source ${sourceId} must have canonical_offer role`);
      assert.ok(["approved_offer_decision", "offer_current_lp_or_spec"].includes(source.canonical_level), `${label}: same-offer outcome source ${sourceId} has insufficient authority`);
      assert.equal(source.offer_id, offerId, `${label}: outcome source ${sourceId} belongs to a different offer`);
    } else {
      assert.fail(`${label}: primaryOutcome source ${sourceId} is not eligible outcome authority`);
    }
  }
  return primaryOutcome;
}

export function deriveCoverage(manifest) {
  const required = manifest.sources.filter((source) => source.required);
  return {
    required_sources_found: sorted(required.filter((source) => source.read_status !== "not_found").map((source) => source.source_id)),
    required_sources_read: sorted(required.filter((source) => source.read_status === "read").map((source) => source.source_id)),
    required_sources_with_evidence: sorted(required.filter((source) => source.read_status === "read" && source.evidence_count > 0).map((source) => source.source_id)),
    missing_sources: sorted(required.filter((source) => source.read_status === "not_found").map((source) => source.source_id)),
    unread_sources: sorted(required.filter((source) => source.read_status === "not_read" || source.read_status === "read_but_no_evidence_extracted").map((source) => source.source_id)),
    read_but_unused_sources: sorted(manifest.sources.filter((source) => source.read_status === "read" && source.used_in_insight_ids.length === 0).map((source) => source.source_id)),
  };
}

function validateOfferContext(context, sourceById) {
  assert.ok([1, 2].includes(context.schemaVersion), "offer context: unsupported schemaVersion");
  assert.equal(context.sourceAssemblyVersion, 1, "offer context: unsupported sourceAssemblyVersion");
  assert.equal(context.status, "OFFER_SOURCE_LOCKED", "offer context: Offer Source Lock is not complete");
  assert.deepEqual(context.sourcePrecedence, SOURCE_PRECEDENCE, "offer context: source precedence is invalid");
  assert.ok(context.offerId && context.offerName, "offer context: offer ID and name are required");
  if (context.schemaVersion === 2) validatePrimaryOutcome(context.primaryOutcome, sourceById, context.offerId, "offer context");
  assert.ok(Array.isArray(context.canonicalSourceIds) && context.canonicalSourceIds.length > 0, "offer context: canonical sources are required");
  for (const sourceId of context.canonicalSourceIds) assert.ok(sourceById.has(sourceId), `offer context: unknown canonical source ${sourceId}`);
  const global = sourceById.get(context.globalProjectStrategy?.sourceId);
  assert.ok(global, "offer context: global project strategy source is missing");
  assert.equal(context.globalProjectStrategy.role, "background_only", "offer context: global project strategy must be background_only");
  assert.equal(global.role, "background_only", "source manifest: global project strategy must be background_only");
  for (const conflict of context.conflicts) {
    for (const sourceId of [...conflict.higherPrioritySourceIds, ...conflict.lowerPrioritySourceIds]) assert.ok(sourceById.has(sourceId), `offer context: conflict references unknown source ${sourceId}`);
    assert.equal(conflict.status, "resolved_by_precedence", `offer context: unresolved source conflict ${conflict.conflictId}`);
    assert.ok(conflict.resolution, `offer context: conflict ${conflict.conflictId} needs a resolution`);
  }
}

function validateInsightMap(map, sourceById) {
  assert.equal(map.schemaVersion, 1, "insight map: unsupported schemaVersion");
  assert.equal(map.sourceAssemblyVersion, 1, "insight map: unsupported sourceAssemblyVersion");
  assert.ok(Number.isInteger(map.minimumInsightDepth) && map.minimumInsightDepth >= 1 && map.minimumInsightDepth <= 6, "insight map: invalid minimum depth");
  assert.ok(Array.isArray(map.insights) && map.insights.length > 0, "insight map: at least one insight is required");
  const insightIds = new Set();
  for (const insight of map.insights) {
    const requiredFields = ["insight_id", "raw_observation", "surface_pain", "functional_tension", "social_stake", "emotional_or_identity_stake", "existing_workaround", "why_workaround_fails", "hidden_contradiction", "desired_progress", "product_mechanism", "proof_or_limit", "confidence"];
    for (const field of requiredFields) assert.ok(typeof insight[field] === "string" && insight[field].trim(), `insight ${insight.insight_id ?? "<unknown>"}: ${field} is required`);
    assert.ok(!insightIds.has(insight.insight_id), `insight map: duplicate insight ${insight.insight_id}`);
    assert.ok(Array.isArray(insight.source_refs) && insight.source_refs.length > 0, `insight ${insight.insight_id}: source refs are required`);
    for (const ref of insight.source_refs) assert.ok(sourceById.has(sourceIdFromRef(ref)), `insight ${insight.insight_id}: unknown source ref ${ref}`);
    assert.ok(Number.isInteger(insight.insight_depth_level) && insight.insight_depth_level >= 1 && insight.insight_depth_level <= 6, `insight ${insight.insight_id}: invalid depth`);
    insightIds.add(insight.insight_id);
  }
  assert.ok(Math.max(...map.insights.map((insight) => insight.insight_depth_level)) >= map.minimumInsightDepth, `insight map: no insight reaches required Level ${map.minimumInsightDepth}`);
  return insightIds;
}

export async function validateSourceAssembly(jobDir, { requirePremiseApproval = false } = {}) {
  const documents = new Map();
  for (const file of SOURCE_FILES) documents.set(file, JSON.parse(await readFile(path.join(jobDir, file), "utf8")));
  const jobIds = new Set([...documents.values()].map((document) => document.jobId));
  const offerIds = new Set([...documents.values()].map((document) => document.offerId));
  assert.equal(jobIds.size, 1, "source assembly: jobId mismatch");
  assert.equal(offerIds.size, 1, "source assembly: offerId mismatch");

  const manifest = documents.get("source-manifest.json");
  assert.ok([1, 2].includes(manifest.schemaVersion), "source manifest: unsupported schemaVersion");
  assert.equal(manifest.sourceAssemblyVersion, 1, "source manifest: unsupported sourceAssemblyVersion");
  assert.equal(manifest.schemaVersion, documents.get("offer-context.json").schemaVersion, "source assembly: offer context/source manifest schemaVersion mismatch");
  assert.ok(Array.isArray(manifest.sources) && manifest.sources.length > 0, "source manifest: sources are required");
  const sourceById = new Map();
  for (const source of manifest.sources) {
    for (const field of ["source_id", "source_type", "role", "canonical_level", "path_or_ref", "version_or_hash", "read_status"]) assert.ok(typeof source[field] === "string" && source[field].trim(), `source manifest: ${field} missing`);
    if (manifest.schemaVersion === 2) {
      assert.ok(["request_origin", "same_offer_authoritative", "ineligible"].includes(source.outcome_eligibility), `source manifest: outcome_eligibility missing or invalid for ${source.source_id}`);
      assert.ok(source.offer_id === null || nonEmpty(source.offer_id), `source manifest: offer_id is invalid for ${source.source_id}`);
    }
    assert.ok(!sourceById.has(source.source_id), `source manifest: duplicate source ${source.source_id}`);
    assert.equal(typeof source.required, "boolean", `source ${source.source_id}: required must be boolean`);
    assert.ok(Number.isInteger(source.evidence_count) && source.evidence_count >= 0, `source ${source.source_id}: invalid evidence_count`);
    assert.ok(Array.isArray(source.used_in_insight_ids), `source ${source.source_id}: used_in_insight_ids must be an array`);
    if (source.read_status === "read") assert.ok(source.evidence_count > 0 || source.role === "background_only", `source ${source.source_id}: read source must contain extracted evidence`);
    if (source.required) {
      assert.equal(source.read_status, "read", `required source ${source.source_id} was not read with evidence`);
      assert.ok(source.evidence_count > 0, `required source ${source.source_id} has zero extracted evidence`);
      assert.ok(source.used_in_insight_ids.length > 0, `required source ${source.source_id} was read but unused`);
    }
    sourceById.set(source.source_id, source);
  }

  validateOfferContext(documents.get("offer-context.json"), sourceById);
  const insightIds = validateInsightMap(documents.get("insight-evidence-map.json"), sourceById);
  for (const source of manifest.sources) for (const insightId of source.used_in_insight_ids) assert.ok(insightIds.has(insightId), `source ${source.source_id}: unknown used insight ${insightId}`);

  const report = documents.get("source-coverage-report.json");
  const derived = deriveCoverage(manifest);
  for (const [field, value] of Object.entries(derived)) assert.deepEqual(sorted(report[field]), value, `source coverage report: ${field} does not match manifest`);
  assert.equal(report.gate_status, "PASS", "source coverage report: gate_status must be PASS");
  assert.equal(derived.missing_sources.length, 0, "source coverage: required source is missing");
  assert.equal(derived.unread_sources.length, 0, "source coverage: required source is unread or has no evidence");
  const unresolvedConflicts = report.offer_global_strategy_conflicts.filter((conflict) => conflict.status !== "resolved_by_precedence");
  assert.equal(unresolvedConflicts.length, 0, "source coverage: offer/global strategy conflict remains unresolved");

  validateMessageInheritance(documents.get("message-inheritance-contract.json"), new Set(sourceById.keys()));
  const minimumDepth = documents.get("insight-evidence-map.json").minimumInsightDepth;
  const premise = documents.get("creative-premise.json");
  let salesThesis = null;
  if (premise.schemaVersion === 2) {
    salesThesis = JSON.parse(await readFile(path.join(jobDir, "sales-thesis.json"), "utf8"));
    assert.equal(salesThesis.jobId, premise.jobId, "sales thesis: jobId mismatch");
    assert.equal(salesThesis.offerId, premise.offerId, "sales thesis: offerId mismatch");
    assert.equal(salesThesis.salesThesisId, premise.sales_thesis_id, "creative premise: Sales Thesis ID drift");
    validateSalesThesis(salesThesis, { requireReady: true, knownSourceIds: new Set(sourceById.keys()) });
  }
  validateCreativePremise(premise, { requireApproval: requirePremiseApproval, minimumDepth, knownSourceIds: new Set(sourceById.keys()) });
  const premiseSourceIds = new Set(premise.source_refs.map(sourceIdFromRef));
  for (const source of manifest.sources.filter((item) => item.required)) {
    assert.ok(premiseSourceIds.has(source.source_id), `creative premise: required source ${source.source_id} was extracted but not inherited`);
  }
  validateCopyLineage(documents.get("copy-lineage.json"), { knownSourceIds: new Set(sourceById.keys()) });

  return {
    jobId: [...jobIds][0],
    offerId: [...offerIds][0],
    primaryOutcome: documents.get("offer-context.json").schemaVersion === 2 ? documents.get("offer-context.json").primaryOutcome : null,
    outcomeGrounded: documents.get("offer-context.json").schemaVersion === 2,
    sourceCount: manifest.sources.length,
    requiredCount: manifest.sources.filter((source) => source.required).length,
    insightCount: insightIds.size,
    salesThesisId: salesThesis?.salesThesisId ?? null,
    premiseDecision: documents.get("creative-premise.json").approval.decision,
  };
}

async function main() {
  const jobDir = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(jobDir, "Usage: node scripts/validate-source-assembly.mjs <job-dir> [--require-premise-approved]");
  const result = await validateSourceAssembly(jobDir, { requirePremiseApproval: process.argv.includes("--require-premise-approved") });
  console.log(`Source assembly: PASS (${result.requiredCount} required / ${result.sourceCount} total sources, ${result.insightCount} insights)`);
  if (result.salesThesisId) console.log(`Sales Thesis: READY (${result.salesThesisId})`);
  console.log(`Creative Premise: ${result.premiseDecision}; Hook generation ${result.premiseDecision === "approved" ? "may proceed" : "remains blocked"}`);
}

const isMain = (() => {
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); } catch { return false; }
})();

if (isMain) main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
