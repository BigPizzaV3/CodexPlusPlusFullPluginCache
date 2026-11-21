#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const sha256Pattern = /^[a-f0-9]{64}$/;
const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;
const bindingModes = ["screen_native", "planar_track", "corner_pin", "uv_texture_3d", "final_frame_repair", "motion_scaffold_v2v", "not_applicable"];

export function validateVisualTreatmentContract(contract, { requireSelected = false } = {}) {
  assert.equal(contract.schemaVersion, 1, "visual treatment: schemaVersion must be 1");
  assert.equal(contract.contractVersion, 1, "visual treatment: contractVersion must be 1");
  assert.equal(contract.contractType, "performance_video_visual_treatment", "visual treatment: contractType is invalid");
  assert.ok(nonEmpty(contract.jobId), "visual treatment: jobId is required");
  assert.ok(["DRAFT", "AWAITING_TASTE", "APPROVED_FOR_FEASIBILITY", "REJECTED"].includes(contract.status), "visual treatment: status is invalid");
  const risk = contract.riskProfile;
  assert.ok(risk && typeof risk === "object", "visual treatment: riskProfile is required");
  assert.ok(["known", "new"].includes(risk.visualGrammarNovelty), "visual treatment: visualGrammarNovelty is invalid");
  assert.ok(["none", "supporting", "primary"].includes(risk.exactSurfaceSemanticLoad), "visual treatment: exactSurfaceSemanticLoad is invalid");
  assert.ok(["low", "medium", "high"].includes(risk.worldBindingRisk), "visual treatment: worldBindingRisk is invalid");
  assert.ok(Array.isArray(risk.reasons), "visual treatment: risk reasons must be an array");
  assert.ok(Array.isArray(contract.treatments), "visual treatment: treatments must be an array");
  if (contract.status !== "DRAFT" || requireSelected) assert.ok(contract.treatments.length >= 1 && contract.treatments.length <= 3, "visual treatment: one to three treatments are required");
  const treatmentIds = new Set();
  for (const [treatmentIndex, treatment] of contract.treatments.entries()) {
    const prefix = `visual treatment: treatments[${treatmentIndex}]`;
    assert.ok(nonEmpty(treatment.treatmentId), `${prefix}.treatmentId is required`);
    assert.equal(treatmentIds.has(treatment.treatmentId), false, `${prefix}.treatmentId must be unique`);
    treatmentIds.add(treatment.treatmentId);
    assert.ok(nonEmpty(treatment.title) && nonEmpty(treatment.lookTarget), `${prefix} requires title and lookTarget`);
    assert.ok(nonEmpty(treatment.motionGrammar?.description), `${prefix}.motionGrammar.description is required`);
    assert.ok(Array.isArray(treatment.motionGrammar?.chronologicalArc) && treatment.motionGrammar.chronologicalArc.length > 0, `${prefix}.motionGrammar.chronologicalArc is required`);
    assert.ok(Array.isArray(treatment.motionGrammar?.delegatedMotion), `${prefix}.motionGrammar.delegatedMotion must be an array`);
    assert.ok(Array.isArray(treatment.semanticCarrierObjects) && treatment.semanticCarrierObjects.length > 0, `${prefix}.semanticCarrierObjects is required`);
    const objectIds = new Set();
    for (const [objectIndex, object] of treatment.semanticCarrierObjects.entries()) {
      validateSemanticCarrierObject(object, `${prefix}.semanticCarrierObjects[${objectIndex}]`);
      assert.equal(objectIds.has(object.objectId), false, `${prefix}: duplicate objectId ${object.objectId}`);
      objectIds.add(object.objectId);
    }
    assert.ok(Array.isArray(treatment.finalLookFrames), `${prefix}.finalLookFrames must be an array`);
    for (const frame of treatment.finalLookFrames) {
      assert.ok(nonEmpty(frame.path), `${prefix}: final-look frame path is required`);
      assert.match(frame.sha256 ?? "", sha256Pattern, `${prefix}: final-look frame SHA-256 is invalid`);
    }
    assert.ok(nonEmpty(treatment.fallbackRoute?.description), `${prefix}.fallbackRoute.description is required`);
    assert.equal(treatment.fallbackRoute?.preservesViewerJob, true, `${prefix}.fallbackRoute must preserve the viewer job`);
  }

  const approval = contract.approval;
  assert.ok(["pending", "approved", "rejected"].includes(approval?.decision), "visual treatment: approval decision is invalid");
  if (approval?.decision === "approved" || requireSelected) {
    assert.equal(contract.status, "APPROVED_FOR_FEASIBILITY", "visual treatment: selected treatment requires APPROVED_FOR_FEASIBILITY status");
    assert.ok(nonEmpty(approval.selectedTreatmentId) && treatmentIds.has(approval.selectedTreatmentId), "visual treatment: approved selectedTreatmentId must exist");
    assert.ok(nonEmpty(approval.approvedBy) && nonEmpty(approval.approvedAt), "visual treatment: approval evidence is required");
    const selected = contract.treatments.find((treatment) => treatment.treatmentId === approval.selectedTreatmentId);
    assert.ok(selected.finalLookFrames.length >= 1, "visual treatment: approved treatment requires at least one final-look frame");
  }
  const selectedTreatment = nonEmpty(approval?.selectedTreatmentId)
    ? contract.treatments.find((treatment) => treatment.treatmentId === approval.selectedTreatmentId)
    : null;
  const riskRelevantTreatments = selectedTreatment ? [selectedTreatment] : contract.treatments;
  const hasPrimaryWorldBoundSurface = riskRelevantTreatments.some((treatment) =>
    treatment.semanticCarrierObjects.some((object) => object.semanticSurfaceLoad === "primary" && object.worldRelation === "world_bound"),
  );
  const movingProofExpected = risk.visualGrammarNovelty === "new" || risk.worldBindingRisk === "high" || hasPrimaryWorldBoundSurface;
  assert.equal(
    risk.movingProofRequired,
    movingProofExpected,
    "visual treatment: movingProofRequired must be derived from novelty, binding risk, and primary world-bound semantic surfaces",
  );
  assert.equal(contract.distribution?.publishAllowed, false, "visual treatment cannot authorize publishing");
  assert.equal(contract.distribution?.activateAdsAllowed, false, "visual treatment cannot authorize ad activation");
  return contract;
}

export function validateSemanticCarrierObject(object, prefix = "semantic carrier") {
  assert.ok(nonEmpty(object.objectId) && nonEmpty(object.viewerMeaning), `${prefix} requires objectId and viewerMeaning`);
  assert.ok(["motion", "exact_surface", "character", "environment", "editing", "mixed"].includes(object.semanticCarrierType), `${prefix}.semanticCarrierType is invalid`);
  assert.ok(["none", "supporting", "primary"].includes(object.semanticSurfaceLoad), `${prefix}.semanticSurfaceLoad is invalid`);
  assert.ok(["transitional", "readable_anchor", "persistent", "background"].includes(object.surfacePersistence), `${prefix}.surfacePersistence is invalid`);
  assert.ok(["screen_native", "world_bound"].includes(object.worldRelation), `${prefix}.worldRelation is invalid`);
  assert.ok(["deterministic", "generative", "not_applicable"].includes(object.contentAuthority), `${prefix}.contentAuthority is invalid`);
  assert.ok(["generated_object", "deterministic_surface", "deterministic_3d"].includes(object.geometryOwner), `${prefix}.geometryOwner is invalid`);
  assert.ok(["generative", "deterministic", "tracked"].includes(object.motionOwner), `${prefix}.motionOwner is invalid`);
  assert.ok(bindingModes.includes(object.bindingMode), `${prefix}.bindingMode is invalid`);
  assert.ok(Array.isArray(object.exactnessWindows), `${prefix}.exactnessWindows must be an array`);
  for (const window of object.exactnessWindows) {
    assert.ok(Number.isInteger(window.startFrame) && Number.isInteger(window.endFrame) && window.endFrame > window.startFrame, `${prefix}: exactness window is invalid`);
    assert.equal(typeof window.readabilityRequired, "boolean", `${prefix}: readabilityRequired is required`);
  }
  if (object.semanticSurfaceLoad !== "none") {
    assert.equal(object.contentAuthority, "deterministic", `${prefix}: exact semantic surfaces require deterministic content authority`);
    assert.ok(object.exactnessWindows.length > 0, `${prefix}: semantic surface requires an exactness window`);
  }
  if (object.worldRelation === "screen_native") assert.equal(object.bindingMode, "screen_native", `${prefix}: screen-native object must use screen_native binding`);
  if (object.worldRelation === "world_bound") assert.notEqual(object.bindingMode, "screen_native", `${prefix}: world-bound object cannot use screen-space binding`);
  if (["planar_track", "corner_pin", "uv_texture_3d", "final_frame_repair", "motion_scaffold_v2v"].includes(object.bindingMode)) {
    assert.equal(object.worldRelation, "world_bound", `${prefix}: ${object.bindingMode} requires a world-bound object`);
  }
}

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const file = process.argv[2];
  assert.ok(file, "Usage: validate-visual-treatment-contract.mjs <visual-treatment-contract.json> [--require-selected]");
  const contract = JSON.parse(readFileSync(file, "utf8"));
  validateVisualTreatmentContract(contract, { requireSelected: process.argv.includes("--require-selected") });
  console.log(`visual treatment: PASS (${contract.jobId})`);
}
