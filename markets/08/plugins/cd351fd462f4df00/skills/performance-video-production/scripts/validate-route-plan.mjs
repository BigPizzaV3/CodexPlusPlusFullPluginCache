#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const routeStatuses = ["DRAFT", "ROUTE_SELECTED", "HUMAN_TASTE_PASS", "HUMAN_TASTE_FAIL"];
const routes = ["deterministic", "generative", "hybrid"];
const motionOwners = ["deterministic", "generative"];
const previewRoles = ["timing_only", "candidate_final", "not_required"];
const overrideStatuses = ["NOT_REQUIRED", "PENDING", "APPROVED", "REJECTED"];
const pictureStrategies = ["ai_native_motion_deterministic_finish", "deterministic_first", "mixed_by_viewer_job"];
const remotionRoles = ["compositor_and_finisher", "primary_motion_engine", "adaptive_by_scene"];
const controlModes = ["directed_generation", "controlled_generation", "deterministic_composition"];
const generationUnits = ["contiguous_sequence", "bounded_shot", "not_applicable"];
const keyframePolicies = ["none", "first_only", "first_last", "start_peak_end"];
const controlSources = ["none", "first_frame", "last_frame", "identity_reference", "motion_reference", "intermediate_frame"];
const semanticSurfaceLoads = ["none", "supporting", "primary"];
const semanticCarrierTypes = ["motion", "exact_surface", "character", "environment", "editing", "mixed"];
const worldRelations = ["screen_native", "world_bound"];
const contentAuthorities = ["deterministic", "generative", "not_applicable"];
const geometryOwners = ["generated_object", "deterministic_surface", "deterministic_3d"];
const surfaceMotionOwners = ["generative", "deterministic", "tracked"];
const bindingModes = ["screen_native", "planar_track", "corner_pin", "uv_texture_3d", "final_frame_repair", "motion_scaffold_v2v", "not_applicable"];
const trackSources = ["not_required", "generated_plane_track", "post_generation_feature_track", "deterministic_camera", "uv_coordinates"];
const motionNeedKeys = [
  "spatialDepth",
  "physicalMaterialInteraction",
  "organicCameraMotion",
  "naturalSubjectMotion",
  "environmentalParallax",
];
const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;

export const validateRoutePlan = (plan) => {
  assert.equal(plan.schemaVersion, 1, "schemaVersion must be 1");
  const routePlanVersion = plan.routePlanVersion ?? 1;
  assert.ok([1, 2, 3].includes(routePlanVersion), "routePlanVersion must be 1, 2, or 3");
  assert.equal(plan.contractType, "performance_video_route_plan", "contractType is invalid");
  assert.ok(nonEmpty(plan.jobId), "jobId is required");
  assert.ok(routeStatuses.includes(plan.status), "status is invalid");
  assert.ok(Array.isArray(plan.scenes) && plan.scenes.length > 0, "at least one scene is required");
  if (routePlanVersion >= 2) {
    assert.ok(pictureStrategies.includes(plan.pictureStrategy), "pictureStrategy is invalid");
    assert.ok(remotionRoles.includes(plan.compositionPolicy?.remotionRole), "compositionPolicy.remotionRole is invalid");
  }
  if (routePlanVersion === 2) assert.equal(plan.compositionPolicy?.exactSurfacesDeterministic, true, "legacy v2 exact surfaces must remain deterministic");
  if (routePlanVersion === 3) assert.equal(plan.compositionPolicy?.exactContentAuthority, "deterministic", "exact content authority must remain deterministic");

  for (const [index, scene] of plan.scenes.entries()) {
    const prefix = `scenes[${index}]`;
    assert.ok(nonEmpty(scene.shotId), `${prefix}.shotId is required`);
    assert.ok(nonEmpty(scene.viewerJob), `${prefix}.viewerJob is required`);
    assert.equal(typeof scene.exactSurfaces?.japaneseOrUiRequired, "boolean", `${prefix}.exactSurfaces.japaneseOrUiRequired is required`);
    if (routePlanVersion <= 2) assert.equal(typeof scene.exactSurfaces?.deterministicOverlayPlanned, "boolean", `${prefix}.exactSurfaces.deterministicOverlayPlanned is required`);
    for (const key of motionNeedKeys) {
      assert.equal(typeof scene.motionQualityNeeds?.[key], "boolean", `${prefix}.motionQualityNeeds.${key} is required`);
    }
    const pressure = motionNeedKeys.filter((key) => scene.motionQualityNeeds[key]).length;
    assert.equal(scene.routePressureScore, pressure, `${prefix}.routePressureScore must equal the enabled motion needs`);
    assert.ok(routes.includes(scene.selectedRoute), `${prefix}.selectedRoute is invalid`);
    assert.ok(motionOwners.includes(scene.primaryMotionOwner), `${prefix}.primaryMotionOwner is invalid`);
    assert.ok(Array.isArray(scene.deterministicResponsibilities), `${prefix}.deterministicResponsibilities must be an array`);
    assert.ok(Array.isArray(scene.generativeResponsibilities), `${prefix}.generativeResponsibilities must be an array`);
    assert.ok(previewRoles.includes(scene.zeroCostPreview?.role), `${prefix}.zeroCostPreview.role is invalid`);
    assert.equal(typeof scene.zeroCostPreview?.candidateFinal, "boolean", `${prefix}.zeroCostPreview.candidateFinal is required`);
    assert.ok(overrideStatuses.includes(scene.humanTasteOverride?.status), `${prefix}.humanTasteOverride.status is invalid`);
    assert.ok(nonEmpty(scene.rationale), `${prefix}.rationale is required`);

    if (routePlanVersion >= 2) validateAdaptiveControl(scene, prefix);
    if (routePlanVersion === 3) validateExactSurfaceStrategy(scene, prefix);

    if (scene.selectedRoute === "deterministic") assert.equal(scene.primaryMotionOwner, "deterministic", `${prefix} deterministic route requires deterministic primary motion`);
    if (scene.selectedRoute === "generative") assert.equal(scene.primaryMotionOwner, "generative", `${prefix} generative route requires generative primary motion`);
    if (routePlanVersion <= 2 && scene.exactSurfaces.japaneseOrUiRequired && scene.primaryMotionOwner === "generative") {
      assert.equal(scene.exactSurfaces.deterministicOverlayPlanned, true, `${prefix} exact Japanese or UI requires a deterministic overlay plan`);
    }
    if (scene.zeroCostPreview.role === "timing_only") {
      assert.equal(scene.zeroCostPreview.candidateFinal, false, `${prefix} timing_only preview cannot be a final-picture candidate`);
    }
    if (scene.zeroCostPreview.role === "candidate_final") {
      assert.equal(scene.zeroCostPreview.candidateFinal, true, `${prefix} candidate_final preview must be marked as a final-picture candidate`);
    }
    if (pressure >= 2 && scene.primaryMotionOwner === "deterministic") {
      assert.equal(scene.humanTasteOverride.status, "APPROVED", `${prefix} high route pressure requires generated primary motion or a human Taste override`);
      assert.ok(nonEmpty(scene.humanTasteOverride.rationale), `${prefix} approved human Taste override requires rationale`);
    }
  }

  assert.equal(plan.distribution?.publishAllowed, false, "route plan cannot authorize publishing");
  assert.equal(plan.distribution?.activateAdsAllowed, false, "route plan cannot authorize ad activation");
  return plan;
};

function validateAdaptiveControl(scene, prefix) {
  assert.ok(controlModes.includes(scene.controlMode), `${prefix}.controlMode is invalid`);
  assert.ok(generationUnits.includes(scene.generationUnit), `${prefix}.generationUnit is invalid`);
  const budget = scene.controlBudget;
  assert.ok(budget && typeof budget === "object", `${prefix}.controlBudget is required`);
  assert.ok(keyframePolicies.includes(budget.keyframePolicy), `${prefix}.controlBudget.keyframePolicy is invalid`);
  assert.ok(Array.isArray(budget.controlSources) && budget.controlSources.length > 0, `${prefix}.controlBudget.controlSources is required`);
  for (const source of budget.controlSources) assert.ok(controlSources.includes(source), `${prefix}.controlBudget has invalid control source ${source}`);
  assert.equal(new Set(budget.controlSources).size, budget.controlSources.length, `${prefix}.controlBudget.controlSources must be unique`);
  assert.ok(Array.isArray(budget.macroLocks) && budget.macroLocks.length > 0 && budget.macroLocks.every(nonEmpty), `${prefix}.controlBudget.macroLocks is required`);
  assert.ok(Array.isArray(budget.delegatedToModel) && budget.delegatedToModel.every(nonEmpty), `${prefix}.controlBudget.delegatedToModel must be an array of non-empty strings`);

  const needsControlReason = scene.controlMode === "controlled_generation" || budget.keyframePolicy !== "none" || budget.controlSources.some((source) => source !== "none");
  if (needsControlReason) assert.ok(nonEmpty(budget.controlReason), `${prefix}.controlBudget.controlReason is required for added controls`);

  const sourceSet = new Set(budget.controlSources);
  if (budget.keyframePolicy === "none") {
    assert.equal(sourceSet.has("first_frame") || sourceSet.has("last_frame") || sourceSet.has("intermediate_frame"), false, `${prefix} keyframePolicy none cannot carry keyframe controls`);
  }
  if (budget.keyframePolicy === "first_only") assert.equal(sourceSet.has("first_frame"), true, `${prefix} first_only requires first_frame`);
  if (budget.keyframePolicy === "first_last") assert.equal(sourceSet.has("first_frame") && sourceSet.has("last_frame"), true, `${prefix} first_last requires first_frame and last_frame`);
  if (budget.keyframePolicy === "start_peak_end") assert.equal(sourceSet.has("first_frame") && sourceSet.has("intermediate_frame") && sourceSet.has("last_frame"), true, `${prefix} start_peak_end requires first, intermediate, and last frames`);

  if (scene.controlMode === "deterministic_composition") {
    assert.equal(scene.primaryMotionOwner, "deterministic", `${prefix} deterministic_composition requires deterministic primary motion`);
    assert.equal(scene.generationUnit, "not_applicable", `${prefix} deterministic_composition cannot create a generation unit`);
    assert.equal(budget.keyframePolicy, "none", `${prefix} deterministic_composition cannot require generated keyframes`);
    assert.deepEqual(budget.controlSources, ["none"], `${prefix} deterministic_composition controlSources must be [none]`);
    assert.equal(budget.delegatedToModel.length, 0, `${prefix} deterministic_composition cannot delegate primary motion`);
  }

  if (scene.controlMode === "directed_generation") {
    assert.equal(scene.primaryMotionOwner, "generative", `${prefix} directed_generation requires generative primary motion`);
    assert.ok(["generative", "hybrid"].includes(scene.selectedRoute), `${prefix} directed_generation requires a generative or hybrid route`);
    assert.ok(["contiguous_sequence", "bounded_shot"].includes(scene.generationUnit), `${prefix} directed_generation requires a generation unit`);
    assert.ok(budget.delegatedToModel.length > 0, `${prefix} directed_generation must delegate choreography to the model`);
    assert.notEqual(budget.keyframePolicy, "start_peak_end", `${prefix} directed_generation cannot default to start_peak_end overconstraint`);
  }

  if (scene.controlMode === "controlled_generation") {
    assert.equal(scene.primaryMotionOwner, "generative", `${prefix} controlled_generation requires generative primary motion`);
    assert.ok(["generative", "hybrid"].includes(scene.selectedRoute), `${prefix} controlled_generation requires a generative or hybrid route`);
    assert.ok(["contiguous_sequence", "bounded_shot"].includes(scene.generationUnit), `${prefix} controlled_generation requires a generation unit`);
    assert.ok(budget.delegatedToModel.length > 0, `${prefix} controlled_generation must still delegate non-critical motion`);
    assert.equal(sourceSet.has("none"), false, `${prefix} controlled_generation requires at least one named control source`);
  }
}

function validateExactSurfaceStrategy(scene, prefix) {
  const exact = scene.exactSurfaces;
  assert.ok(semanticSurfaceLoads.includes(exact.semanticSurfaceLoad), `${prefix}.exactSurfaces.semanticSurfaceLoad is invalid`);
  assert.ok(semanticCarrierTypes.includes(exact.semanticCarrierType), `${prefix}.exactSurfaces.semanticCarrierType is invalid`);
  assert.ok(Array.isArray(exact.surfaceObjects), `${prefix}.exactSurfaces.surfaceObjects must be an array`);
  assert.ok(nonEmpty(exact.fallbackRoute), `${prefix}.exactSurfaces.fallbackRoute is required`);
  if (exact.japaneseOrUiRequired || exact.semanticSurfaceLoad !== "none") assert.ok(exact.surfaceObjects.length > 0, `${prefix}: exact semantic surfaces require object-level ownership`);
  if (exact.semanticSurfaceLoad === "primary") assert.ok(exact.surfaceObjects.some((object) => object.readableWindows?.length > 0), `${prefix}: primary semantic surface requires a readable window`);

  const ids = new Set();
  for (const [index, object] of exact.surfaceObjects.entries()) {
    const objectPrefix = `${prefix}.exactSurfaces.surfaceObjects[${index}]`;
    assert.ok(nonEmpty(object.objectId), `${objectPrefix}.objectId is required`);
    assert.equal(ids.has(object.objectId), false, `${objectPrefix}.objectId must be unique`);
    ids.add(object.objectId);
    assert.ok(worldRelations.includes(object.worldRelation), `${objectPrefix}.worldRelation is invalid`);
    assert.ok(contentAuthorities.includes(object.contentAuthority), `${objectPrefix}.contentAuthority is invalid`);
    assert.ok(geometryOwners.includes(object.geometryOwner), `${objectPrefix}.geometryOwner is invalid`);
    assert.ok(surfaceMotionOwners.includes(object.motionOwner), `${objectPrefix}.motionOwner is invalid`);
    assert.ok(bindingModes.includes(object.bindingMode), `${objectPrefix}.bindingMode is invalid`);
    assert.ok(trackSources.includes(object.trackSource), `${objectPrefix}.trackSource is invalid`);
    for (const key of ["occlusionPlan", "lookMatchPlan", "repairPlan"]) assert.ok(nonEmpty(object[key]), `${objectPrefix}.${key} is required`);
    assert.ok(Array.isArray(object.readableWindows), `${objectPrefix}.readableWindows must be an array`);
    for (const window of object.readableWindows) {
      assert.ok(Number.isInteger(window.startFrame) && Number.isInteger(window.endFrame) && window.endFrame > window.startFrame, `${objectPrefix}: readable window is invalid`);
    }
    if (exact.japaneseOrUiRequired || exact.semanticSurfaceLoad !== "none") assert.equal(object.contentAuthority, "deterministic", `${objectPrefix}: exact content authority must be deterministic`);
    if (object.worldRelation === "screen_native") {
      assert.equal(object.bindingMode, "screen_native", `${objectPrefix}: screen-native object must use screen_native binding`);
      assert.equal(object.trackSource, "not_required", `${objectPrefix}: screen-native object must not invent a world track`);
    }
    if (object.worldRelation === "world_bound") {
      assert.notEqual(object.bindingMode, "screen_native", `${objectPrefix}: world-bound object cannot use screen-space binding`);
      if (["planar_track", "corner_pin"].includes(object.bindingMode)) assert.ok(["generated_plane_track", "post_generation_feature_track"].includes(object.trackSource), `${objectPrefix}: tracked binding requires a track source`);
      if (object.bindingMode === "uv_texture_3d") assert.ok(["deterministic_camera", "uv_coordinates"].includes(object.trackSource), `${objectPrefix}: UV/3D binding requires deterministic camera or UV coordinates`);
      if (object.bindingMode === "motion_scaffold_v2v") assert.equal(object.trackSource, "deterministic_camera", `${objectPrefix}: motion scaffold requires deterministic camera data`);
      if (object.bindingMode === "final_frame_repair") assert.ok(nonEmpty(object.repairPlan), `${objectPrefix}: final-frame repair requires a repair plan`);
    }
  }
}

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const inputPath = process.argv[2];
  assert.ok(inputPath, "Usage: validate-route-plan.mjs <route-plan.json>");
  validateRoutePlan(JSON.parse(readFileSync(inputPath, "utf8")));
  console.log("route plan: VALID");
}
