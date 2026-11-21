#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const READY = new Set(["READY_FOR_PRODUCTION"]);
const ROLES = new Set(["causal", "informational", "structural", "rhythmic", "emotional", "brand", "ambience"]);
const nonEmpty = (value, label) => assert.equal(typeof value === "string" && value.trim().length > 0, true, `${label} is required`);

export const validateSoundIntentMap = (map, { requireReady = false } = {}) => {
  assert.equal(map.schemaVersion, 1, "sound intent: schemaVersion must be 1");
  nonEmpty(map.jobId, "sound intent jobId");
  nonEmpty(map.platform, "sound intent platform");
  assert.ok(["DRAFT", "READY_FOR_PRODUCTION", "REVISE"].includes(map.status), "sound intent: invalid status");
  if (requireReady) assert.ok(READY.has(map.status), "sound intent: map is not ready");
  const ready = requireReady || READY.has(map.status);
  assert.ok(Number(map.fps) > 0, "sound intent: fps must be positive");
  assert.ok(Number.isInteger(map.durationFrames) && map.durationFrames > 0, "sound intent: durationFrames must be positive");
  assert.equal(map.soundOnStrategy?.narrationPriority, true, "sound intent: narration must remain the priority bus");
  assert.equal(map.soundOnStrategy?.muteLegibilityRequired, true, "sound intent: the ad must remain understandable when muted");
  assert.ok(Number.isInteger(map.soundOnStrategy?.firstSoundByFrame) && map.soundOnStrategy.firstSoundByFrame >= 0 && map.soundOnStrategy.firstSoundByFrame < map.durationFrames, "sound intent: first sound is outside the timeline");
  nonEmpty(map.soundOnStrategy?.firstSoundJob, "sound intent firstSoundJob");

  const density = map.densityPolicy ?? {};
  assert.ok(["restrained", "balanced", "entertainment_high"].includes(density.mode), "sound intent: invalid density mode");
  nonEmpty(density.selectionReason, "sound intent density selectionReason");
  assert.ok(Number.isInteger(density.maxOnsetsPerSecond) && density.maxOnsetsPerSecond >= 1 && density.maxOnsetsPerSecond <= 6, "sound intent: maxOnsetsPerSecond must be 1-6");
  assert.ok(Number.isInteger(density.maxSimultaneousUnderNarration) && density.maxSimultaneousUnderNarration >= 1 && density.maxSimultaneousUnderNarration <= 2, "sound intent: narration overlap cap must be 1-2");
  assert.ok(Number.isInteger(density.maxSimultaneousWithoutNarration) && density.maxSimultaneousWithoutNarration >= 1 && density.maxSimultaneousWithoutNarration <= 4, "sound intent: non-narration overlap cap must be 1-4");
  assert.ok(density.maxSimultaneousUnderNarration <= density.maxSimultaneousWithoutNarration, "sound intent: narration overlap cannot exceed non-narration overlap");

  const clusters = new Map();
  for (const cluster of density.highDensityClusters ?? []) {
    nonEmpty(cluster.clusterId, "sound intent clusterId");
    assert.equal(clusters.has(cluster.clusterId), false, `sound intent: duplicate clusterId ${cluster.clusterId}`);
    assert.ok(Number.isInteger(cluster.startFrame) && Number.isInteger(cluster.endFrame) && cluster.endFrame > cluster.startFrame && cluster.endFrame <= map.durationFrames, `${cluster.clusterId}: invalid frame range`);
    nonEmpty(cluster.purpose, `${cluster.clusterId}.purpose`);
    clusters.set(cluster.clusterId, cluster);
  }
  if (density.mode === "entertainment_high") assert.ok(clusters.size > 0, "sound intent: entertainment_high requires a named high-density cluster purpose");

  const narrationWindows = map.narrationWindows ?? [];
  const narrationIds = new Set();
  for (const window of narrationWindows) {
    nonEmpty(window.windowId, "sound intent narration windowId");
    nonEmpty(window.beatId, `${window.windowId}.beatId`);
    assert.equal(narrationIds.has(window.windowId), false, `sound intent: duplicate narration window ${window.windowId}`);
    assert.ok(Number.isInteger(window.startFrame) && Number.isInteger(window.endFrame) && window.endFrame > window.startFrame && window.endFrame <= map.durationFrames, `${window.windowId}: invalid narration range`);
    narrationIds.add(window.windowId);
  }
  const sortedNarration = [...narrationWindows].sort((a, b) => a.startFrame - b.startFrame);
  for (let index = 1; index < sortedNarration.length; index += 1) {
    assert.ok(sortedNarration[index].startFrame >= sortedNarration[index - 1].endFrame, `sound intent: narration windows ${sortedNarration[index - 1].windowId} and ${sortedNarration[index].windowId} overlap`);
  }

  const silenceWindows = map.silenceWindows ?? [];
  const silenceIds = new Set();
  for (const window of silenceWindows) {
    nonEmpty(window.windowId, "sound intent silence windowId");
    assert.equal(silenceIds.has(window.windowId), false, `sound intent: duplicate silence window ${window.windowId}`);
    assert.ok(Number.isInteger(window.startFrame) && Number.isInteger(window.endFrame) && window.endFrame > window.startFrame && window.endFrame <= map.durationFrames, `${window.windowId}: invalid frame range`);
    nonEmpty(window.purpose, `${window.windowId}.purpose`);
    silenceIds.add(window.windowId);
  }

  const intents = map.cueIntents ?? [];
  assert.ok(Array.isArray(intents), "sound intent: cueIntents must be an array");
  if (ready) assert.ok(intents.length > 0, "sound intent: ready map needs at least one cue intent");
  const ids = new Set();
  const byBeatEditorial = new Map();
  const sameFrame = new Map();
  for (const intent of intents) {
    nonEmpty(intent.intentId, "sound intent intentId");
    assert.equal(ids.has(intent.intentId), false, `sound intent: duplicate intentId ${intent.intentId}`);
    ids.add(intent.intentId);
    nonEmpty(intent.beatId, `${intent.intentId}.beatId`);
    assert.ok(ROLES.has(intent.role), `${intent.intentId}: invalid role`);
    assert.ok(["required", "recommended", "optional"].includes(intent.necessity), `${intent.intentId}: invalid necessity`);
    assert.ok(Number.isInteger(intent.triggerFrame) && intent.triggerFrame >= 0 && intent.triggerFrame < map.durationFrames, `${intent.intentId}: trigger is outside timeline`);
    nonEmpty(intent.visualCause, `${intent.intentId}.visualCause`);
    nonEmpty(intent.viewerJob, `${intent.intentId}.viewerJob`);
    nonEmpty(intent.soundFamily, `${intent.intentId}.soundFamily`);
    nonEmpty(intent.desiredCharacter, `${intent.intentId}.desiredCharacter`);
    assert.ok(["none", "duck_required", "prohibited"].includes(intent.narrationOverlap), `${intent.intentId}: invalid narration overlap policy`);
    assert.ok(Number.isInteger(intent.maxOffsetFrames) && intent.maxOffsetFrames >= 0 && intent.maxOffsetFrames <= 6, `${intent.intentId}: invalid maxOffsetFrames`);
    if (["causal", "informational"].includes(intent.role)) assert.ok(intent.maxOffsetFrames <= 3, `${intent.intentId}: causal/informational cue tolerance exceeds three frames`);
    if (intent.clusterId !== null) assert.ok(clusters.has(intent.clusterId), `${intent.intentId}: unknown clusterId ${intent.clusterId}`);
    for (const window of silenceWindows) {
      if (window.absoluteForSfx && intent.triggerFrame >= window.startFrame && intent.triggerFrame < window.endFrame) {
        assert.fail(`${intent.intentId}: cue enters absolute SFX silence window ${window.windowId}`);
      }
    }
    if (["structural", "emotional"].includes(intent.role)) {
      byBeatEditorial.set(intent.beatId, (byBeatEditorial.get(intent.beatId) ?? 0) + 1);
    }
    const atFrame = sameFrame.get(intent.triggerFrame) ?? [];
    atFrame.push(intent);
    sameFrame.set(intent.triggerFrame, atFrame);
  }
  for (const [beatId, count] of byBeatEditorial) {
    assert.ok(count <= density.maxEditorialAccentsPerBeat, `${beatId}: editorial accent count ${count} exceeds profile cap`);
  }
  for (const [frame, frameIntents] of sameFrame) {
    if (frameIntents.length <= 1) continue;
    const layerId = frameIntents[0].layerGroupId;
    assert.ok(layerId && frameIntents.every((intent) => intent.layerGroupId === layerId), `sound intent: frame ${frame} has unrelated simultaneous cues`);
    assert.ok(frameIntents.length <= 3, `sound intent: layer group ${layerId} exceeds three layers`);
  }

  const motifIds = new Set();
  for (const motif of map.motifs ?? []) {
    nonEmpty(motif.motifId, "sound intent motifId");
    assert.equal(motifIds.has(motif.motifId), false, `sound intent: duplicate motifId ${motif.motifId}`);
    nonEmpty(motif.soundFamily, `${motif.motifId}.soundFamily`);
    nonEmpty(motif.reusePolicy, `${motif.motifId}.reusePolicy`);
    motifIds.add(motif.motifId);
  }

  const rights = map.rightsPolicy ?? {};
  assert.equal(rights.commercialUseRequired, true, "sound intent: commercial-use rights must be required");
  assert.equal(rights.licenseManifestRequired, true, "sound intent: license manifest must be required");
  assert.equal(rights.platformScopeVerificationRequired, true, "sound intent: platform scope must be verified");
  assert.equal(rights.trademarkNotificationImitationProhibited, true, "sound intent: trademark notification imitation must be prohibited");
  assert.equal(rights.randomWebDownloadProhibited, true, "sound intent: random web downloads must be prohibited");

  if (ready) {
    for (const [key, value] of Object.entries(map.checks ?? {})) assert.equal(value, true, `sound intent: ready check ${key} must be true`);
  }
  return { jobId: map.jobId, status: map.status, cueIntents: intents.length, silenceWindows: silenceWindows.length, narrationWindows: narrationWindows.length };
};

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const inputPath = process.argv[2];
  assert.ok(inputPath, "Usage: validate-sound-intent-map.mjs <sound-intent-map.json> [--require-ready]");
  const map = JSON.parse(readFileSync(inputPath, "utf8"));
  const result = validateSoundIntentMap(map, { requireReady: process.argv.includes("--require-ready") });
  console.log(`sound intent map: PASS (${result.jobId} / ${result.cueIntents} cues / ${result.silenceWindows} silence windows)`);
}
