#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const LEGACY_KEYFRAME_ROLES = ["start_frame", "peak_action", "endpoint"];
const adaptivePolicies = ["none", "first_only", "first_last", "start_peak_end"];
const validBindings = ["screen_native", "planar_track", "corner_pin", "uv_texture_3d", "final_frame_repair", "motion_scaffold_v2v"];

export function validateKeyframeProductionPlan(plan) {
  assert.equal(plan.schemaVersion, 1, "keyframe plan: unsupported schemaVersion");
  const planVersion = plan.planVersion ?? 1;
  assert.ok([1, 2].includes(planVersion), "keyframe plan: planVersion must be 1 or 2");
  assert.ok(plan.jobId, "keyframe plan: jobId is required");
  assert.equal(plan.maximumExploratoryVideoAttemptsPerApprovedShot, 1, "keyframe plan: exploration must allow one paid attempt per approved shot");
  assert.ok(Array.isArray(plan.scenes) && plan.scenes.length > 0, "keyframe plan: scenes are required");
  if (planVersion === 1) return validateLegacyPlan(plan);

  assert.equal(plan.productionMode, "adaptive_hybrid", "keyframe plan: v2 productionMode must be adaptive_hybrid");
  const ids = plan.scenes.map((scene) => scene.sceneId);
  assert.equal(new Set(ids).size, ids.length, "keyframe plan: sceneId values must be unique");
  const aiScenes = plan.scenes.filter((scene) => ["ai_image_to_video", "ai_video"].includes(scene.generationMode));
  for (const scene of plan.scenes) {
    assert.ok(["remotion_only", "ai_image_to_video", "ai_video", "remotion_composite"].includes(scene.generationMode), `keyframe plan: ${scene.sceneId} generationMode is invalid`);
    if (!["ai_image_to_video", "ai_video"].includes(scene.generationMode)) {
      assert.equal(scene.paidVideoAllowed, false, `keyframe plan: deterministic scene ${scene.sceneId} cannot authorize paid video`);
      continue;
    }
    assert.ok(scene.coherentEvent, `keyframe plan: AI scene ${scene.sceneId} requires one coherentEvent`);
    assert.ok(scene.durationSeconds > 0, `keyframe plan: AI scene ${scene.sceneId} requires a positive duration`);
    const budget = scene.controlBudget;
    assert.ok(budget && adaptivePolicies.includes(budget.keyframePolicy), `keyframe plan: ${scene.sceneId} requires an adaptive control budget`);
    assert.ok(Array.isArray(budget.controlSources) && budget.controlSources.length > 0, `keyframe plan: ${scene.sceneId} requires controlSources`);
    if (budget.keyframePolicy !== "none" || budget.controlSources.some((source) => source !== "none")) assert.ok(budget.controlReason, `keyframe plan: ${scene.sceneId} added controls require a named reason`);
    const roles = new Set((scene.keyframes ?? []).map((frame) => frame.role));
    if (budget.keyframePolicy === "none") assert.equal(roles.size, 0, `keyframe plan: ${scene.sceneId} keyframePolicy none cannot require keyframes`);
    if (budget.keyframePolicy === "first_only") assert.equal(roles.has("start_frame"), true, `keyframe plan: ${scene.sceneId} first_only requires start_frame`);
    if (budget.keyframePolicy === "first_last") assert.equal(roles.has("start_frame") && roles.has("endpoint"), true, `keyframe plan: ${scene.sceneId} first_last requires start and endpoint`);
    if (budget.keyframePolicy === "start_peak_end") assert.equal(roles.has("start_frame") && roles.has("peak_action") && roles.has("endpoint"), true, `keyframe plan: ${scene.sceneId} start_peak_end requires three anchors`);
    if (scene.exactTextRequirement) {
      assert.equal(scene.exactContentAuthority, "deterministic", `keyframe plan: ${scene.sceneId} exact content authority must remain deterministic`);
      assert.ok(validBindings.includes(scene.bindingMode), `keyframe plan: ${scene.sceneId} exact content requires a valid binding mode`);
      assert.equal(scene.compositingFeasibilityStatus, "PASS", `keyframe plan: ${scene.sceneId} exact content requires compositing feasibility PASS`);
    }
    if (scene.paidVideoAllowed) {
      for (const frame of scene.keyframes ?? []) {
        assert.equal(frame.status, "approved", `keyframe plan: ${scene.sceneId} ${frame.role} must be approved before paid video`);
        assert.ok(frame.assetRef, `keyframe plan: ${scene.sceneId} ${frame.role} must have an asset before paid video`);
      }
    }
  }
  const anyPaidScene = aiScenes.some((scene) => scene.paidVideoAllowed);
  assert.equal(plan.paidVideoGenerationAllowed, anyPaidScene, "keyframe plan: global paid flag must match scene approvals");
  validateDistribution(plan);
  return { sceneCount: plan.scenes.length, aiSceneCount: aiScenes.length, paidVideoGenerationAllowed: plan.paidVideoGenerationAllowed };
}

function validateLegacyPlan(plan) {
  assert.equal(plan.productionMode, "keyframe_first_hybrid", "keyframe plan: legacy productionMode must be keyframe_first_hybrid");
  const ids = plan.scenes.map((scene) => scene.sceneId);
  assert.equal(new Set(ids).size, ids.length, "keyframe plan: sceneId values must be unique");
  const aiScenes = plan.scenes.filter((scene) => scene.generationMode === "ai_image_to_video");
  for (const scene of plan.scenes) {
    if (scene.exactTextRequirement) assert.notEqual(scene.generationMode, "ai_image_to_video", `keyframe plan: legacy exact text scene ${scene.sceneId} must remain deterministic`);
    if (scene.generationMode !== "ai_image_to_video") {
      assert.equal(scene.paidVideoAllowed, false, `keyframe plan: deterministic scene ${scene.sceneId} cannot authorize paid video`);
      continue;
    }
    assert.ok(scene.coherentEvent, `keyframe plan: AI scene ${scene.sceneId} requires one coherentEvent`);
    assert.ok(scene.durationSeconds > 0 && scene.durationSeconds <= 8, `keyframe plan: AI scene ${scene.sceneId} duration must be within 0-8 seconds`);
    const roles = scene.keyframes.map((frame) => frame.role);
    assert.deepEqual([...roles].sort(), [...LEGACY_KEYFRAME_ROLES].sort(), `keyframe plan: legacy AI scene ${scene.sceneId} requires exactly start, peak, and endpoint frames`);
    if (scene.paidVideoAllowed) {
      for (const frame of scene.keyframes) {
        assert.equal(frame.status, "approved", `keyframe plan: ${scene.sceneId} ${frame.role} must be approved before paid video`);
        assert.ok(frame.assetRef, `keyframe plan: ${scene.sceneId} ${frame.role} must have an asset before paid video`);
      }
      assert.equal(scene.keyframeApproval?.decision, "approved", `keyframe plan: ${scene.sceneId} keyframes are not approved`);
      assert.equal(scene.transitionPreviewApproval?.decision, "approved", `keyframe plan: ${scene.sceneId} transition preview is not approved`);
      assert.equal(scene.continuityContract?.status, "approved", `keyframe plan: ${scene.sceneId} continuity is not approved`);
    }
  }
  const anyPaidScene = aiScenes.some((scene) => scene.paidVideoAllowed);
  assert.equal(plan.paidVideoGenerationAllowed, anyPaidScene, "keyframe plan: global paid flag must match scene approvals");
  validateDistribution(plan);
  return { sceneCount: plan.scenes.length, aiSceneCount: aiScenes.length, paidVideoGenerationAllowed: plan.paidVideoGenerationAllowed };
}

function validateDistribution(plan) {
  assert.equal(plan.distribution?.publishAllowed, false, "keyframe plan: publishing must remain locked");
  assert.equal(plan.distribution?.activateAdsAllowed, false, "keyframe plan: ad activation must remain locked");
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-keyframe-production-plan.mjs <keyframe-production-plan.json>");
  const result = validateKeyframeProductionPlan(JSON.parse(await readFile(file, "utf8")));
  console.log(`Keyframe production plan: PASS (${result.sceneCount} scenes / ${result.aiSceneCount} AI motion / paid=${result.paidVideoGenerationAllowed})`);
}
