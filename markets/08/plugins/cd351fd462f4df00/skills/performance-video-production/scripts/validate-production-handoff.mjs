#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const sha256Pattern = /^[a-f0-9]{64}$/;
const nonEmpty = (value, label) => assert.equal(typeof value === "string" && value.trim().length > 0, true, `${label} is required`);

export const validateProductionHandoff = (handoff) => {
  assert.equal(handoff.schemaVersion, 1, "schemaVersion must be 1");
  const contractVersion = handoff.contractVersion ?? 1;
  assert.ok([1, 2, 3, 4].includes(contractVersion), "contractVersion must be 1, 2, 3, or 4");
  assert.equal(handoff.contractType, "performance_video_production_handoff", "contractType is invalid");
  assert.equal(handoff.handoffStatus, "APPROVED_FOR_PRODUCTION", "handoffStatus must be APPROVED_FOR_PRODUCTION");
  for (const key of ["jobId", "offerId", "strategySnapshotId", "selectedTerritoryId", "hookPackageId", "bodyFamilyId"]) {
    nonEmpty(handoff[key], key);
  }

  assert.equal(handoff.approvedArtifacts?.animaticReview?.status, "APPROVED", "approved Animatic review is required");
  nonEmpty(handoff.approvedArtifacts?.animaticReview?.path, "approvedArtifacts.animaticReview.path");
  assert.match(handoff.approvedArtifacts?.animaticReview?.sha256 ?? "", sha256Pattern, "approved Animatic SHA-256 is invalid");
  assert.ok(["READY_FOR_PRODUCTION", "PASS_LOCAL_REVIEW"].includes(handoff.approvedArtifacts?.timelineAudioIntent?.status), "approved timeline/audio intent is required");
  nonEmpty(handoff.approvedArtifacts?.timelineAudioIntent?.path, "approvedArtifacts.timelineAudioIntent.path");
  assert.match(handoff.approvedArtifacts?.timelineAudioIntent?.sha256 ?? "", sha256Pattern, "timeline/audio contract SHA-256 is invalid");
  if (contractVersion >= 4) {
    assert.equal(handoff.approvedArtifacts?.visualTreatment?.status, "APPROVED", "approved Visual Treatment is required");
    nonEmpty(handoff.approvedArtifacts?.visualTreatment?.path, "approvedArtifacts.visualTreatment.path");
    assert.match(handoff.approvedArtifacts?.visualTreatment?.sha256 ?? "", sha256Pattern, "Visual Treatment SHA-256 is invalid");
    assert.equal(handoff.approvedArtifacts?.compositingFeasibility?.status, "PASS", "compositing feasibility PASS is required");
    nonEmpty(handoff.approvedArtifacts?.compositingFeasibility?.path, "approvedArtifacts.compositingFeasibility.path");
    assert.match(handoff.approvedArtifacts?.compositingFeasibility?.sha256 ?? "", sha256Pattern, "compositing feasibility SHA-256 is invalid");
    validateLineage(handoff.lineage, handoff.jobId);
  }

  const creative = handoff.immutableCreative;
  assert.ok(creative && typeof creative === "object", "immutableCreative is required");
  for (const key of ["audience", "moment", "promise", "hook", "cta", "destination"]) nonEmpty(creative[key], `immutableCreative.${key}`);
  assert.ok(Array.isArray(creative.bodyBeats) && creative.bodyBeats.length > 0, "immutableCreative.bodyBeats must not be empty");
  assert.ok(Array.isArray(creative.exactCopy) && creative.exactCopy.length > 0, "immutableCreative.exactCopy must not be empty");
  if (contractVersion >= 2) {
    for (const key of ["salesThesisId", "singleSellReason", "stopReason", "continueReason"]) nonEmpty(creative[key], `immutableCreative.${key}`);
    assert.notEqual(creative.stopReason.trim(), creative.continueReason.trim(), "immutableCreative stopReason and continueReason must be distinct");
    assert.ok(Array.isArray(creative.salesQuestionChain) && creative.salesQuestionChain.length >= 3 && creative.salesQuestionChain.length <= 6, "immutableCreative.salesQuestionChain must contain three to six questions");
    assert.deepEqual(creative.salesQuestionChain.map((item) => item.order), creative.salesQuestionChain.map((_, index) => index + 1), "immutableCreative.salesQuestionChain order must be contiguous from 1");
    for (const [index, item] of creative.salesQuestionChain.entries()) {
      nonEmpty(item.viewerQuestion, `immutableCreative.salesQuestionChain[${index}].viewerQuestion`);
      nonEmpty(item.answerJob, `immutableCreative.salesQuestionChain[${index}].answerJob`);
    }
  }
  if (contractVersion >= 3) validateProductionIntent(handoff.productionIntent);

  const delivery = handoff.finalDelivery;
  assert.ok(delivery && typeof delivery === "object", "finalDelivery is required");
  assert.ok(Number(delivery.width) > 0 && Number(delivery.height) > 0 && Number(delivery.fps) > 0, "final delivery dimensions and fps are required");
  assert.ok(Number(delivery.durationSeconds) > 0, "finalDelivery.durationSeconds must be positive");
  assert.equal(delivery.distribution?.publishAllowed, false, "publishAllowed must remain false at production handoff");
  assert.equal(delivery.distribution?.activateAdsAllowed, false, "activateAdsAllowed must remain false at production handoff");

  assert.ok(Array.isArray(handoff.scenes) && handoff.scenes.length > 0, "scenes must not be empty");
  const ids = new Set();
  let previousEnd = 0;
  for (const [index, scene] of handoff.scenes.entries()) {
    nonEmpty(scene.shotId, `scenes[${index}].shotId`);
    assert.equal(ids.has(scene.shotId), false, `duplicate shotId: ${scene.shotId}`);
    ids.add(scene.shotId);
    nonEmpty(scene.viewerJob, `scenes[${index}].viewerJob`);
    nonEmpty(scene.visualIntent, `scenes[${index}].visualIntent`);
    assert.ok(["deterministic", "generative", "hybrid"].includes(scene.executionClass), `${scene.shotId}: executionClass is invalid`);
    assert.ok(["hard_cut", "continuous", "match_cut", "overlay"].includes(scene.continuityType), `${scene.shotId}: continuityType is invalid`);
    assert.ok(Number(scene.timeRange?.startSeconds) >= previousEnd - 0.001, `${scene.shotId}: scenes overlap or are out of order`);
    assert.ok(Number(scene.timeRange?.endSeconds) > Number(scene.timeRange?.startSeconds), `${scene.shotId}: invalid timeRange`);
    previousEnd = Number(scene.timeRange.endSeconds);
    assert.ok(Array.isArray(scene.deterministicResponsibilities), `${scene.shotId}: deterministicResponsibilities is required`);
    assert.ok(Array.isArray(scene.generativeResponsibilities), `${scene.shotId}: generativeResponsibilities is required`);
    assert.ok(Array.isArray(scene.lockedFields) && scene.lockedFields.length > 0, `${scene.shotId}: lockedFields must not be empty`);
    assert.ok(Array.isArray(scene.rejectionCriteria) && scene.rejectionCriteria.length > 0, `${scene.shotId}: rejectionCriteria must not be empty`);
    if (scene.exactTextRequired) {
      assert.ok(scene.deterministicResponsibilities.some((item) => /text|copy|Japanese|UI/i.test(item)), `${scene.shotId}: exact text must be deterministic`);
    }
    if (contractVersion >= 4) validateSurfaceOwnership(scene, index);
  }

  assert.equal(handoff.approvals?.animaticApproved, true, "animaticApproved must be true");
  assert.equal(handoff.approvals?.handoffApproved, true, "handoffApproved must be true");
  assert.ok(["PENDING", "APPROVED", "NOT_REQUIRED"].includes(handoff.approvals?.paidGenerationStatus), "paidGenerationStatus is invalid");
  return handoff;
};

function validateProductionIntent(intent) {
  assert.ok(intent && typeof intent === "object", "productionIntent is required for contractVersion 3");
  assert.ok(["ai_native_motion_deterministic_finish", "deterministic_first", "mixed_by_viewer_job"].includes(intent.pictureStrategy), "productionIntent.pictureStrategy is invalid");
  nonEmpty(intent.heroVisualConcept, "productionIntent.heroVisualConcept");
  for (const field of ["mustFeel", "mustSee", "macroLocks", "delegatedMotion", "exactSurfaceResponsibilities", "allowedUnitBoundaryReasons"]) {
    assert.ok(Array.isArray(intent[field]) && intent[field].length > 0, `productionIntent.${field} must not be empty`);
    if (field !== "allowedUnitBoundaryReasons") assert.ok(intent[field].every((value) => typeof value === "string" && value.trim()), `productionIntent.${field} must contain non-empty strings`);
  }
  const boundaryReasons = ["semantic_change", "camera_reset", "identity_risk", "exact_surface_boundary", "privacy_boundary", "verified_model_limit", "accepted_hard_cut"];
  for (const reason of intent.allowedUnitBoundaryReasons) assert.ok(boundaryReasons.includes(reason), `productionIntent has invalid unit boundary reason ${reason}`);
  assert.equal(new Set(intent.allowedUnitBoundaryReasons).size, intent.allowedUnitBoundaryReasons.length, "productionIntent.allowedUnitBoundaryReasons must be unique");
  assert.ok(["compositor_and_finisher", "primary_motion_engine", "adaptive_by_scene"].includes(intent.remotionRole), "productionIntent.remotionRole is invalid");
  const overlap = intent.macroLocks.filter((lock) => intent.delegatedMotion.includes(lock));
  assert.equal(overlap.length, 0, "productionIntent cannot both lock and delegate the same motion decision");
  if (intent.pictureStrategy === "ai_native_motion_deterministic_finish") {
    assert.equal(intent.remotionRole, "compositor_and_finisher", "AI-native picture strategy requires Remotion to remain compositor and finisher");
    assert.ok(intent.delegatedMotion.length > 0, "AI-native picture strategy must delegate motion choreography");
  }
}

function validateLineage(lineage, jobId) {
  assert.ok(lineage && typeof lineage === "object", "lineage is required for contractVersion 4");
  nonEmpty(lineage.jobDirectoryId, "lineage.jobDirectoryId");
  assert.equal(lineage.jobDirectoryId, jobId, "lineage.jobDirectoryId must match jobId");
  for (const key of ["parentJobId", "derivedFromJobId"]) {
    assert.equal(lineage[key] === null || typeof lineage[key] === "string", true, `lineage.${key} must be null or a string`);
    if (lineage[key] !== null) nonEmpty(lineage[key], `lineage.${key}`);
  }
  if (lineage.parentJobId && lineage.derivedFromJobId) assert.notEqual(lineage.parentJobId, lineage.derivedFromJobId, "lineage parent and derived source must be distinct");
}

function validateSurfaceOwnership(scene, index) {
  const prefix = `scenes[${index}].surfaceOwnership`;
  assert.ok(Array.isArray(scene.surfaceOwnership), `${prefix} is required for contractVersion 4`);
  if (scene.exactTextRequired) assert.ok(scene.surfaceOwnership.length > 0, `${prefix} must name the exact surface owner`);
  const ids = new Set();
  for (const surface of scene.surfaceOwnership) {
    nonEmpty(surface.objectId, `${prefix}.objectId`);
    assert.equal(ids.has(surface.objectId), false, `${prefix} contains duplicate objectId ${surface.objectId}`);
    ids.add(surface.objectId);
    assert.ok(["deterministic", "generative", "not_applicable"].includes(surface.contentAuthority), `${prefix} contentAuthority is invalid`);
    assert.ok(["generated_object", "deterministic_surface", "deterministic_3d"].includes(surface.geometryOwner), `${prefix} geometryOwner is invalid`);
    assert.ok(["generative", "deterministic", "tracked"].includes(surface.motionOwner), `${prefix} motionOwner is invalid`);
    assert.ok(["screen_native", "planar_track", "corner_pin", "uv_texture_3d", "final_frame_repair", "motion_scaffold_v2v", "not_applicable"].includes(surface.bindingMode), `${prefix} bindingMode is invalid`);
    assert.ok(Array.isArray(surface.exactnessWindows), `${prefix} exactnessWindows must be an array`);
    for (const window of surface.exactnessWindows) assert.ok(Number.isInteger(window.startFrame) && Number.isInteger(window.endFrame) && window.endFrame > window.startFrame, `${prefix} exactness window is invalid`);
    if (scene.exactTextRequired) {
      assert.equal(surface.contentAuthority, "deterministic", `${prefix}: exact text authority must be deterministic`);
      assert.ok(surface.exactnessWindows.length > 0, `${prefix}: exact text requires a readable window`);
    }
  }
}

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const inputPath = process.argv[2];
  assert.ok(inputPath, "Usage: validate-production-handoff.mjs <production-handoff.json>");
  const handoff = JSON.parse(readFileSync(inputPath, "utf8"));
  validateProductionHandoff(handoff);
  console.log(`production handoff: PASS (${handoff.jobId})`);
}
