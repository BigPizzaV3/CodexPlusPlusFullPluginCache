#!/usr/bin/env node
import { validateRunDelegation, payloadHash } from "../../marketing-omakase/scripts/run-contract.mjs";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

export const DISCOVERY_FILES = [
  "felt-brief.json",
  "creative-tension-map.json",
  "creative-territories.json",
  "first-frame-board.json",
  "three-second-hook-loops.json",
  "intended-reaction-map.json",
  "taste-review.json",
];

const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;
const unique = (values, label) => {
  assert.equal(new Set(values).size, values.length, `creative discovery: duplicate ${label}`);
  return new Set(values);
};

function validateSourceRefs(items, knownSourceIds = null) {
  for (const item of items) {
    assert.ok(Array.isArray(item.source_refs) && item.source_refs.length > 0, `creative discovery: ${item.id ?? "artifact"} requires source refs`);
    if (knownSourceIds) {
      for (const ref of item.source_refs) {
        const sourceId = String(ref).split("#", 1)[0];
        assert.ok(knownSourceIds.has(sourceId), `creative discovery: unknown source ref ${ref}`);
      }
    }
  }
}

export function validateTasteAuthority(tasteReview) {
  if (tasteReview.agentDelegation) {
    assert.equal(tasteReview.approvedBy, null, "delegated Taste must not impersonate human approver");
    assert.equal(tasteReview.approvedAt, null, "delegated Taste uses its own timestamp");
    const { agentDelegation, ...subject } = tasteReview;
    validateRunDelegation(agentDelegation, { area: "design", artifactHash: payloadHash(subject) });
  } else {
    assert.ok(nonEmpty(tasteReview.approvedBy) && nonEmpty(tasteReview.approvedAt), "creative discovery: human Taste approval requires actor and timestamp");
  }
}

export function validateCreativeDiscovery(documents, { requireSelected = false, knownSourceIds = null } = {}) {
  const {
    feltBrief,
    tensionMap,
    territories,
    firstFrameBoard,
    hookLoops,
    reactionMap,
    tasteReview,
  } = documents;
  const all = [feltBrief, tensionMap, territories, firstFrameBoard, hookLoops, reactionMap, tasteReview];
  for (const document of all) {
    assert.equal(document?.schemaVersion, 1, "creative discovery: unsupported schemaVersion");
    assert.equal(document?.discoveryContractVersion, 1, "creative discovery: unsupported contract version");
    assert.ok(document.jobId, "creative discovery: jobId missing");
  }
  assert.equal(new Set(all.map((document) => document.jobId)).size, 1, "creative discovery: jobId mismatch");

  assert.ok(["DRAFT", "NEEDS_USER_INPUT", "READY_FOR_DISCOVERY"].includes(feltBrief.status), "creative discovery: invalid Felt Brief status");
  assert.ok(["DRAFT", "READY_FOR_TERRITORIES"].includes(tensionMap.status), "creative discovery: invalid tension status");
  assert.ok(["DRAFT", "AWAITING_TASTE_REVIEW", "SELECTED"].includes(territories.status), "creative discovery: invalid Territory status");
  assert.equal(territories.mode, "DISCOVER", "creative discovery: Territory mode must be DISCOVER");
  assert.ok(["DRAFT", "READY_FOR_TASTE_REVIEW"].includes(firstFrameBoard.status), "creative discovery: invalid First Frame status");
  assert.ok(["DRAFT", "READY_FOR_TASTE_REVIEW"].includes(hookLoops.status), "creative discovery: invalid Hook Loop status");
  assert.ok(["DRAFT", "HYPOTHESES_READY"].includes(reactionMap.status), "creative discovery: invalid reaction-map status");
  assert.ok(["AWAITING_HUMAN_REVIEW", "RECORDED"].includes(tasteReview.status), "creative discovery: invalid Taste status");

  const active = [feltBrief, tensionMap, territories, firstFrameBoard, hookLoops, reactionMap].some((document) => document.status !== "DRAFT");
  if (!active) {
    assert.equal(requireSelected, false, "creative discovery: BUILD requires an approved Creative Territory");
    return { status: "DRAFT", territories: 0, frames: 0, loops: 0, selectedTerritoryId: null };
  }

  if (feltBrief.status === "NEEDS_USER_INPUT") {
    assert.ok(Array.isArray(feltBrief.unresolved_fields) && feltBrief.unresolved_fields.length > 0, "creative discovery: unresolved Felt fields missing");
    assert.ok(Array.isArray(feltBrief.questions_to_user) && feltBrief.questions_to_user.length >= 1 && feltBrief.questions_to_user.length <= 3, "creative discovery: ask one to three bounded questions");
    for (const question of feltBrief.questions_to_user) {
      assert.ok(question.question_id && Array.isArray(question.field_ids) && question.field_ids.length > 0 && nonEmpty(question.question) && nonEmpty(question.decision_impact), "creative discovery: incomplete user question");
    }
    assert.equal(requireSelected, false, "creative discovery: unresolved Felt Brief blocks BUILD");
    return { status: "NEEDS_USER_INPUT", territories: 0, frames: 0, loops: 0, selectedTerritoryId: null };
  }

  assert.equal(feltBrief.status, "READY_FOR_DISCOVERY", "creative discovery: active discovery requires a ready Felt Brief");
  for (const field of ["private_thought", "feared_next_moment", "emotional_tension", "identity_to_preserve", "false_reflex", "surprising_possibility", "desired_relief", "desired_click_thought", "dignity_rule"]) {
    assert.ok(nonEmpty(feltBrief[field]), `creative discovery: felt-brief.${field} is required`);
  }
  assert.equal(feltBrief.unresolved_fields.length, 0, "creative discovery: ready Felt Brief cannot retain unresolved fields");
  assert.equal(feltBrief.questions_to_user.length, 0, "creative discovery: ready Felt Brief cannot retain user questions");
  validateSourceRefs([feltBrief], knownSourceIds);

  assert.equal(tensionMap.status, "READY_FOR_TERRITORIES", "creative discovery: tension map must be ready");
  assert.ok(Array.isArray(tensionMap.tensions) && tensionMap.tensions.length >= 3, "creative discovery: require at least three compressed tensions");
  const tensionIds = unique(tensionMap.tensions.map((item) => item.id), "tension ID");
  for (const tension of tensionMap.tensions) {
    for (const field of ["left_state", "right_state", "emotional_charge", "unresolved_question"]) assert.ok(nonEmpty(tension[field]), `creative discovery: tension ${tension.id} lacks ${field}`);
    assert.notEqual(tension.left_state, tension.right_state, `creative discovery: tension ${tension.id} has no contradiction`);
  }
  validateSourceRefs(tensionMap.tensions, knownSourceIds);

  assert.ok(["AWAITING_TASTE_REVIEW", "SELECTED"].includes(territories.status), "creative discovery: Territories must be reviewable");
  assert.ok(Array.isArray(territories.territories) && territories.territories.length >= 3, "creative discovery: require at least three Creative Territories");
  const territoryIds = unique(territories.territories.map((item) => item.id), "Territory ID");
  for (const territory of territories.territories) {
    for (const field of ["name", "core_tension_id", "recognition", "tension", "hope", "open_loop", "reason_to_click", "dignity_boundary", "first_frame_id", "hook_loop_id"]) assert.ok(nonEmpty(territory[field]), `creative discovery: Territory ${territory.id} lacks ${field}`);
    assert.ok(tensionIds.has(territory.core_tension_id), `creative discovery: Territory ${territory.id} cites an unknown tension`);
    for (const forbidden of ["commonBodyId", "bodyFamilyId", "fixedDurationSeconds", "finalDurationSeconds"]) assert.equal(Object.hasOwn(territory, forbidden), false, `creative discovery: Territory ${territory.id} must not lock ${forbidden}`);
  }
  validateSourceRefs(territories.territories, knownSourceIds);

  assert.equal(firstFrameBoard.status, "READY_FOR_TASTE_REVIEW", "creative discovery: First Frame Board must be ready");
  assert.equal(firstFrameBoard.displayTimeSeconds, 0.5, "creative discovery: First Frames must target 0.5 seconds");
  assert.ok(firstFrameBoard.targetFrames >= 12, "creative discovery: First Frame target must be at least twelve");
  assert.ok(Array.isArray(firstFrameBoard.frames) && firstFrameBoard.frames.length >= firstFrameBoard.targetFrames, "creative discovery: First Frame Board is undersized");
  const frameIds = unique(firstFrameBoard.frames.map((item) => item.id), "First Frame ID");
  const framesByTerritory = new Map([...territoryIds].map((id) => [id, 0]));
  for (const frame of firstFrameBoard.frames) {
    assert.ok(territoryIds.has(frame.territory_id), `creative discovery: frame ${frame.id} cites an unknown Territory`);
    for (const field of ["work_surface", "dominant_visual", "overlay_copy", "opening_event"]) assert.ok(nonEmpty(frame[field]), `creative discovery: frame ${frame.id} lacks ${field}`);
    assert.ok([...frame.overlay_copy].length <= 32, `creative discovery: frame ${frame.id} overlay is too long for a 0.5-second read`);
    framesByTerritory.set(frame.territory_id, framesByTerritory.get(frame.territory_id) + 1);
  }
  for (const [territoryId, count] of framesByTerritory) assert.ok(count >= 3, `creative discovery: Territory ${territoryId} requires at least three First Frames`);
  validateSourceRefs(firstFrameBoard.frames, knownSourceIds);

  assert.equal(hookLoops.status, "READY_FOR_TASTE_REVIEW", "creative discovery: three-second Hook Loops must be ready");
  assert.equal(hookLoops.loopDurationSeconds, 3, "creative discovery: Hook Loop duration must be three seconds");
  assert.ok(Array.isArray(hookLoops.loops) && hookLoops.loops.length >= territoryIds.size, "creative discovery: require at least one Hook Loop per Territory");
  const loopIds = unique(hookLoops.loops.map((item) => item.id), "Hook Loop ID");
  const loopsByTerritory = new Map([...territoryIds].map((id) => [id, 0]));
  for (const loop of hookLoops.loops) {
    assert.ok(territoryIds.has(loop.territory_id), `creative discovery: Hook Loop ${loop.id} cites an unknown Territory`);
    assert.ok(frameIds.has(loop.first_frame_id), `creative discovery: Hook Loop ${loop.id} cites an unknown First Frame`);
    assert.ok(nonEmpty(loop.opening_event) && nonEmpty(loop.sound) && nonEmpty(loop.loop_end_state), `creative discovery: Hook Loop ${loop.id} is incomplete`);
    assert.equal(loop.service_explanation_included, false, `creative discovery: Hook Loop ${loop.id} must not explain the service`);
    assert.equal(loop.vfx_independent, true, `creative discovery: Hook Loop ${loop.id} must work without VFX`);
    loopsByTerritory.set(loop.territory_id, loopsByTerritory.get(loop.territory_id) + 1);
  }
  for (const [territoryId, count] of loopsByTerritory) assert.ok(count >= 1, `creative discovery: Territory ${territoryId} lacks a Hook Loop`);
  for (const territory of territories.territories) {
    assert.ok(frameIds.has(territory.first_frame_id), `creative discovery: Territory ${territory.id} cites an unknown lead First Frame`);
    assert.ok(loopIds.has(territory.hook_loop_id), `creative discovery: Territory ${territory.id} cites an unknown lead Hook Loop`);
  }

  assert.equal(reactionMap.status, "HYPOTHESES_READY", "creative discovery: intended reactions must be ready");
  assert.equal(reactionMap.evidence_state, "planning_hypothesis", "creative discovery: intended reactions are hypotheses, not observations");
  assert.equal(reactionMap.performance_claim, false, "creative discovery: intended reactions cannot claim performance");
  assert.equal(reactionMap.approval_does_not_prove_performance, true, "creative discovery: Taste approval cannot prove performance");
  assert.ok(Array.isArray(reactionMap.reactions) && reactionMap.reactions.length === territoryIds.size, "creative discovery: intended reactions must cover every Territory exactly once");
  unique(reactionMap.reactions.map((item) => item.territory_id), "reaction Territory ID");
  for (const reaction of reactionMap.reactions) {
    assert.ok(territoryIds.has(reaction.territory_id), `creative discovery: reaction cites unknown Territory ${reaction.territory_id}`);
    for (const field of ["reaction_at_0_5_sec", "reaction_at_3_sec", "reaction_at_end", "reason_to_click", "intentionally_unanswered_question"]) assert.ok(nonEmpty(reaction[field]), `creative discovery: reaction ${reaction.territory_id} lacks ${field}`);
  }

  assert.equal(tasteReview.approvalScope, "CREATIVE_TERRITORY_TASTE_GATE", "creative discovery: invalid Taste approval scope");
  assert.equal(tasteReview.performanceEvidenceStatus, "not_measured", "creative discovery: Taste review is not performance evidence");
  assert.equal(tasteReview.approvalDoesNotProvePerformance, true, "creative discovery: Taste approval cannot prove performance");
  assert.ok(["pending", "approved", "revise"].includes(tasteReview.decision), "creative discovery: invalid Taste decision");

  if (tasteReview.decision === "pending") {
    assert.equal(tasteReview.status, "AWAITING_HUMAN_REVIEW", "creative discovery: pending Taste review must await a human");
    assert.equal(tasteReview.selectedTerritoryId, null, "creative discovery: pending Taste review cannot select a Territory");
    assert.equal(territories.status, "AWAITING_TASTE_REVIEW", "creative discovery: pending Taste review cannot mark Territories selected");
    assert.equal(requireSelected, false, "creative discovery: BUILD is blocked until the human Taste Gate approves one Territory");
    return { status: "AWAITING_HUMAN_REVIEW", territories: territoryIds.size, frames: frameIds.size, loops: loopIds.size, selectedTerritoryId: null };
  }

  assert.equal(tasteReview.status, "RECORDED", "creative discovery: decided Taste review must be recorded");
  const reviewedIds = unique(tasteReview.reviewedTerritoryIds, "reviewed Territory ID");
  assert.deepEqual(reviewedIds, territoryIds, "creative discovery: human Taste review must cover every Territory");
  assert.ok(Array.isArray(tasteReview.reviews) && tasteReview.reviews.length === territoryIds.size, "creative discovery: one human review is required per Territory");
  const reviewIds = unique(tasteReview.reviews.map((item) => item.territory_id), "Taste review Territory ID");
  assert.deepEqual(reviewIds, territoryIds, "creative discovery: Taste review entries must match the Territory set");

  if (tasteReview.decision === "revise") {
    assert.equal(tasteReview.selectedTerritoryId, null, "creative discovery: revise decision cannot select a Territory");
    assert.equal(requireSelected, false, "creative discovery: revise decision blocks BUILD");
    return { status: "REVISE", territories: territoryIds.size, frames: frameIds.size, loops: loopIds.size, selectedTerritoryId: null };
  }

  assert.equal(territories.status, "SELECTED", "creative discovery: approved Taste review must mark Territories selected");
  assert.ok(territoryIds.has(tasteReview.selectedTerritoryId), "creative discovery: selected Territory does not exist");
  assert.equal(territories.selectedTerritoryId, tasteReview.selectedTerritoryId, "creative discovery: selected Territory drift");
  validateTasteAuthority(tasteReview);
  const selectedReview = tasteReview.reviews.find((item) => item.territory_id === tasteReview.selectedTerritoryId);
  for (const field of ["felt_like_my_case", "emotion_moved", "wanted_to_continue", "wanted_to_click"]) assert.equal(selectedReview[field], true, `creative discovery: selected Territory failed ${field}`);
  assert.equal(selectedReview.felt_excessively_ad_like, false, "creative discovery: selected Territory feels excessively ad-like");

  return { status: "SELECTED", territories: territoryIds.size, frames: frameIds.size, loops: loopIds.size, selectedTerritoryId: tasteReview.selectedTerritoryId };
}

export async function readCreativeDiscovery(jobDir) {
  const values = await Promise.all(DISCOVERY_FILES.map((file) => readFile(path.join(jobDir, file), "utf8").then(JSON.parse)));
  const [feltBrief, tensionMap, territories, firstFrameBoard, hookLoops, reactionMap, tasteReview] = values;
  let knownSourceIds = null;
  try {
    const sourceManifest = JSON.parse(await readFile(path.join(jobDir, "source-manifest.json"), "utf8"));
    if (Array.isArray(sourceManifest.sources) && sourceManifest.sources.length > 0) knownSourceIds = new Set(sourceManifest.sources.map((source) => source.source_id));
  } catch {}
  return { documents: { feltBrief, tensionMap, territories, firstFrameBoard, hookLoops, reactionMap, tasteReview }, knownSourceIds };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const jobDir = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(jobDir, "Usage: node scripts/validate-creative-discovery.mjs <job-dir> [--require-selected]");
  const { documents, knownSourceIds } = await readCreativeDiscovery(jobDir);
  const result = validateCreativeDiscovery(documents, { requireSelected: process.argv.includes("--require-selected"), knownSourceIds });
  console.log(`Creative discovery: PASS (${result.status}; ${result.territories} Territories / ${result.frames} First Frames / ${result.loops} Hook Loops${result.selectedTerritoryId ? ` / selected=${result.selectedTerritoryId}` : ""})`);
}
