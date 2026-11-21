#!/usr/bin/env node
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { validateSoundIntentMap } from "../../performance-video-ad/scripts/validate-sound-intent-map.mjs";
import { validateSfxAssetRegistry } from "./select-sfx-assets.mjs";

const hashText = (text) => createHash("sha256").update(text).digest("hex");
const nonEmpty = (value, label) => assert.equal(typeof value === "string" && value.trim().length > 0, true, `${label} is required`);
const READY = new Set(["READY_FOR_MIX", "MIXED_QC_PASS"]);

export const validateAudioCueSheet = (soundIntentMap, registry, sheet, {
  requireReady = false,
  requirePass = false,
  soundIntentSha256 = null,
  registrySha256 = null,
} = {}) => {
  validateSoundIntentMap(soundIntentMap, { requireReady: true });
  validateSfxAssetRegistry(registry, { requireVerified: true, platform: soundIntentMap.platform });
  assert.equal(sheet.schemaVersion, 1, "audio cue sheet: schemaVersion must be 1");
  assert.ok(["DRAFT", "READY_FOR_MIX", "MIXED_QC_PASS", "REVISE"].includes(sheet.status), "audio cue sheet: invalid status");
  if (requireReady) assert.ok(READY.has(sheet.status), "audio cue sheet is not ready for mixing");
  if (requirePass) assert.equal(sheet.status, "MIXED_QC_PASS", "audio cue sheet is not MIXED_QC_PASS");
  assert.equal(sheet.jobId, soundIntentMap.jobId, "audio cue sheet jobId does not match sound intent map");
  assert.equal(registry.jobId, soundIntentMap.jobId, "SFX registry jobId does not match sound intent map");
  assert.equal(sheet.platform, soundIntentMap.platform, "audio cue sheet platform mismatch");
  assert.equal(sheet.fps, soundIntentMap.fps, "audio cue sheet fps mismatch");
  assert.equal(sheet.durationFrames, soundIntentMap.durationFrames, "audio cue sheet duration mismatch");
  nonEmpty(sheet.soundIntentMap?.path, "audio cue sheet soundIntentMap.path");
  nonEmpty(sheet.assetRegistry?.path, "audio cue sheet assetRegistry.path");
  assert.match(sheet.soundIntentMap?.sha256 ?? "", /^[a-f0-9]{64}$/, "audio cue sheet: invalid sound intent hash");
  assert.match(sheet.assetRegistry?.sha256 ?? "", /^[a-f0-9]{64}$/, "audio cue sheet: invalid registry hash");
  if (soundIntentSha256) assert.equal(sheet.soundIntentMap.sha256, soundIntentSha256, "audio cue sheet references a stale sound intent map");
  if (registrySha256) assert.equal(sheet.assetRegistry.sha256, registrySha256, "audio cue sheet references a stale SFX registry");

  const intents = new Map(soundIntentMap.cueIntents.map((intent) => [intent.intentId, intent]));
  const assets = new Map(registry.assets.map((asset) => [asset.assetId, asset]));
  const cueIds = new Set();
  const realizedIntentIds = new Set();
  const cues = sheet.cues ?? [];
  assert.ok(Array.isArray(cues), "audio cue sheet cues must be an array");
  for (const cue of cues) {
    nonEmpty(cue.cueId, "audio cue cueId");
    assert.equal(cueIds.has(cue.cueId), false, `audio cue sheet: duplicate cueId ${cue.cueId}`);
    cueIds.add(cue.cueId);
    const intent = intents.get(cue.intentId);
    assert.ok(intent, `${cue.cueId}: unplanned intentId ${cue.intentId}`);
    assert.equal(realizedIntentIds.has(cue.intentId), false, `${cue.cueId}: intent ${cue.intentId} is realized more than once`);
    realizedIntentIds.add(cue.intentId);
    const asset = assets.get(cue.assetId);
    assert.ok(asset, `${cue.cueId}: unknown assetId ${cue.assetId}`);
    assert.equal(asset.licenseStatus, "VERIFIED", `${cue.cueId}: asset license is not verified`);
    assert.equal(asset.commercialUseAllowed, true, `${cue.cueId}: asset is not cleared for commercial use`);
    assert.equal(asset.trademarkImitation, false, `${cue.cueId}: trademark-imitation sound is prohibited`);
    assert.ok(asset.platformScopes.includes(soundIntentMap.platform), `${cue.cueId}: asset is not cleared for ${soundIntentMap.platform}`);
    assert.ok(asset.soundFamilies.includes(intent.soundFamily), `${cue.cueId}: asset does not match planned sound family ${intent.soundFamily}`);
    assert.ok(Number.isInteger(cue.startFrame) && Number.isInteger(cue.endFrame) && cue.startFrame >= 0 && cue.endFrame > cue.startFrame && cue.endFrame <= sheet.durationFrames, `${cue.cueId}: invalid frame range`);
    assert.equal(cue.visualTriggerFrame, intent.triggerFrame, `${cue.cueId}: visual trigger drifted from sound intent`);
    assert.equal(cue.syncOffsetFrames, cue.startFrame - cue.visualTriggerFrame, `${cue.cueId}: syncOffsetFrames is inconsistent`);
    assert.ok(Math.abs(cue.syncOffsetFrames) <= intent.maxOffsetFrames, `${cue.cueId}: cue exceeds planned sync tolerance`);
    assert.equal(cue.category, intent.role, `${cue.cueId}: cue category does not match intent role`);
    assert.ok(["sfx_causal", "sfx_editorial", "sfx_brand", "ambience"].includes(cue.bus), `${cue.cueId}: invalid bus`);
    assert.ok(Number(cue.gainDb) >= -60 && Number(cue.gainDb) <= 6, `${cue.cueId}: invalid gain`);
    assert.ok(Number(cue.pitchSemitones) >= -3 && Number(cue.pitchSemitones) <= 3, `${cue.cueId}: invalid pitch`);
    nonEmpty(cue.eqProfile, `${cue.cueId}.eqProfile`);
    const overlapsNarration = (soundIntentMap.narrationWindows ?? []).some((window) => cue.startFrame < window.endFrame && cue.endFrame > window.startFrame);
    assert.equal(cue.speechOverlap, overlapsNarration, `${cue.cueId}: speechOverlap does not match narration windows`);
    if (overlapsNarration) {
      assert.equal(intent.narrationOverlap, "duck_required", `${cue.cueId}: actual narration overlap was not approved`);
      assert.ok(["planned", "applied"].includes(cue.ducking), `${cue.cueId}: narration overlap requires ducking`);
    } else {
      assert.equal(cue.ducking, "not_applicable", `${cue.cueId}: ducking should be not_applicable`);
    }
    for (const window of soundIntentMap.silenceWindows ?? []) {
      if (window.absoluteForSfx && cue.startFrame < window.endFrame && cue.endFrame > window.startFrame) {
        assert.fail(`${cue.cueId}: cue overlaps absolute SFX silence window ${window.windowId}`);
      }
    }
    assert.ok(["SELECTED", "MIXED", "QC_PASS"].includes(cue.status), `${cue.cueId}: invalid cue status`);
  }

  const omitted = new Map();
  for (const omission of sheet.omittedIntents ?? []) {
    nonEmpty(omission.intentId, "audio cue omitted intentId");
    nonEmpty(omission.reason, `${omission.intentId}.omissionReason`);
    assert.ok(intents.has(omission.intentId), `audio cue sheet: omitted unknown intent ${omission.intentId}`);
    assert.equal(omitted.has(omission.intentId), false, `audio cue sheet: duplicate omission ${omission.intentId}`);
    assert.equal(realizedIntentIds.has(omission.intentId), false, `audio cue sheet: ${omission.intentId} is both realized and omitted`);
    omitted.set(omission.intentId, omission.reason);
  }
  for (const intent of intents.values()) {
    if (intent.necessity === "required") assert.ok(realizedIntentIds.has(intent.intentId), `${intent.intentId}: required sound intent is not realized`);
    else assert.ok(realizedIntentIds.has(intent.intentId) || omitted.has(intent.intentId), `${intent.intentId}: non-required intent needs a cue or omission reason`);
  }

  const mix = sheet.mixPolicy ?? {};
  assert.equal(mix.narrationPriority, true, "audio cue sheet: narration must remain the priority bus");
  assert.equal(mix.sidechainOrAutomationRequiredForSpeechOverlap, true, "audio cue sheet: speech overlap requires sidechain or automation");
  assert.equal(mix.maximumOnsetsPerSecond, soundIntentMap.densityPolicy.maxOnsetsPerSecond, "audio cue sheet: onset cap drifted from sound intent");
  assert.equal(mix.maximumSimultaneousUnderNarration, soundIntentMap.densityPolicy.maxSimultaneousUnderNarration, "audio cue sheet: narration layer cap drifted from sound intent");
  assert.equal(mix.maximumSimultaneousWithoutNarration, soundIntentMap.densityPolicy.maxSimultaneousWithoutNarration, "audio cue sheet: layer cap drifted from sound intent");
  assert.ok(Number(mix.targetIntegratedLufs) >= -24 && Number(mix.targetIntegratedLufs) <= -10, "audio cue sheet: loudness target is outside the permitted range");
  assert.ok(Number(mix.loudnessToleranceLu) > 0 && Number(mix.loudnessToleranceLu) <= 2, "audio cue sheet: invalid loudness tolerance");
  assert.ok(Number(mix.maximumTruePeakDbtp) >= -3 && Number(mix.maximumTruePeakDbtp) <= -0.1, "audio cue sheet: invalid true-peak ceiling");
  nonEmpty(mix.loudnessTargetRationale, "audio cue sheet loudnessTargetRationale");

  const fps = sheet.fps;
  for (const cue of cues) {
    const onsetsInWindow = cues.filter((candidate) => candidate.startFrame >= cue.startFrame && candidate.startFrame < cue.startFrame + fps).length;
    assert.ok(onsetsInWindow <= mix.maximumOnsetsPerSecond, `${cue.cueId}: onset density exceeds ${mix.maximumOnsetsPerSecond} per second`);
  }
  for (const cluster of soundIntentMap.densityPolicy.highDensityClusters ?? []) {
    const clusterOnsets = cues.filter((cue) => cue.startFrame >= cluster.startFrame && cue.startFrame < cluster.endFrame).length;
    assert.ok(clusterOnsets <= cluster.maximumOnsets, `${cluster.clusterId}: onset count exceeds named cluster budget`);
  }
  for (let frame = 0; frame < sheet.durationFrames; frame += 1) {
    const active = cues.filter((cue) => cue.startFrame <= frame && cue.endFrame > frame);
    if (active.length === 0) continue;
    const narrationPresent = (soundIntentMap.narrationWindows ?? []).some((window) => frame >= window.startFrame && frame < window.endFrame);
    const cap = narrationPresent ? mix.maximumSimultaneousUnderNarration : mix.maximumSimultaneousWithoutNarration;
    assert.ok(active.length <= cap, `audio cue sheet: ${active.length} simultaneous cues at frame ${frame} exceeds cap ${cap}`);
  }

  assert.equal(sheet.distribution?.publishAllowed, false, "audio cue sheet: publication must remain blocked");
  assert.equal(sheet.distribution?.activateAdsAllowed, false, "audio cue sheet: ad activation must remain blocked");
  assert.equal(sheet.distribution?.publicSkillDistributionAllowed, false, "audio cue sheet: public Skill distribution must remain blocked");

  if (requirePass) {
    assert.ok(cues.every((cue) => cue.status === "QC_PASS"), "audio cue sheet: every cue must pass QC");
    for (const cue of cues.filter((candidate) => candidate.speechOverlap)) assert.equal(cue.ducking, "applied", `${cue.cueId}: ducking was not applied`);
    const qc = sheet.qc ?? {};
    assert.equal(qc.fullDecodePass, true, "audio cue sheet: full decode did not pass");
    assert.equal(qc.licenseCoverageStatus, "PASS", "audio cue sheet: license coverage did not pass");
    assert.equal(qc.noClipping, true, "audio cue sheet: clipping check did not pass");
    assert.equal(qc.narrationIntelligibility, "PASS", "audio cue sheet: narration intelligibility did not pass");
    assert.equal(qc.phoneSpeakerPass, true, "audio cue sheet: phone-speaker review did not pass");
    assert.equal(qc.headphonesPass, true, "audio cue sheet: headphones review did not pass");
    assert.equal(qc.targetPlayerPass, true, "audio cue sheet: target-player review did not pass");
    assert.equal(qc.highFrequencyFatiguePass, true, "audio cue sheet: high-frequency fatigue review did not pass");
    assert.equal(qc.humanTasteStatus, "PASS", "audio cue sheet: human sound Taste review did not pass");
    assert.ok(Number.isFinite(qc.observedIntegratedLufs), "audio cue sheet: observed loudness is missing");
    assert.ok(Math.abs(qc.observedIntegratedLufs - mix.targetIntegratedLufs) <= mix.loudnessToleranceLu, "audio cue sheet: loudness is outside tolerance");
    assert.ok(Number.isFinite(qc.observedTruePeakDbtp), "audio cue sheet: observed true peak is missing");
    assert.ok(qc.observedTruePeakDbtp <= mix.maximumTruePeakDbtp, "audio cue sheet: true peak exceeds ceiling");
  }
  return { jobId: sheet.jobId, status: sheet.status, cues: cues.length, omitted: omitted.size };
};

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const [soundIntentFile, registryFile, cueSheetFile] = process.argv.slice(2).filter((arg) => !arg.startsWith("--"));
  assert.ok(soundIntentFile && registryFile && cueSheetFile, "Usage: validate-audio-cue-sheet.mjs <sound-intent-map.json> <sfx-asset-registry.json> <audio-cue-sheet.json> [--require-ready|--require-pass]");
  const soundIntentText = readFileSync(soundIntentFile, "utf8");
  const registryText = readFileSync(registryFile, "utf8");
  const result = validateAudioCueSheet(JSON.parse(soundIntentText), JSON.parse(registryText), JSON.parse(readFileSync(cueSheetFile, "utf8")), {
    requireReady: process.argv.includes("--require-ready") || process.argv.includes("--require-pass"),
    requirePass: process.argv.includes("--require-pass"),
    soundIntentSha256: hashText(soundIntentText),
    registrySha256: hashText(registryText)
  });
  console.log(`audio cue sheet: PASS (${result.jobId} / ${result.cues} cues / ${result.omitted} omitted)`);
}
