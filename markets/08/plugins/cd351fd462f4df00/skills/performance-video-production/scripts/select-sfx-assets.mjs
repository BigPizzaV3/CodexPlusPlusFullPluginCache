#!/usr/bin/env node
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateSoundIntentMap } from "../../performance-video-ad/scripts/validate-sound-intent-map.mjs";

const hashText = (text) => createHash("sha256").update(text).digest("hex");
const nonEmpty = (value, label) => assert.equal(typeof value === "string" && value.trim().length > 0, true, `${label} is required`);

export const validateSfxAssetRegistry = (registry, { requireVerified = false, platform = null } = {}) => {
  assert.equal(registry.schemaVersion, 1, "SFX registry: schemaVersion must be 1");
  nonEmpty(registry.jobId, "SFX registry jobId");
  nonEmpty(registry.platform, "SFX registry platform");
  assert.ok(["DRAFT", "VERIFIED"].includes(registry.status), "SFX registry: invalid status");
  if (requireVerified) assert.equal(registry.status, "VERIFIED", "SFX registry is not VERIFIED");
  if (platform) assert.equal(registry.platform, platform, "SFX registry platform does not match sound intent map");
  assert.ok(Array.isArray(registry.assets), "SFX registry assets must be an array");
  const ids = new Set();
  for (const asset of registry.assets) {
    nonEmpty(asset.assetId, "SFX registry assetId");
    assert.equal(ids.has(asset.assetId), false, `SFX registry: duplicate assetId ${asset.assetId}`);
    ids.add(asset.assetId);
    nonEmpty(asset.path, `${asset.assetId}.path`);
    assert.match(asset.sha256 ?? "", /^[a-f0-9]{64}$/, `${asset.assetId}: invalid sha256`);
    assert.ok(["owned", "original_recording", "procedural", "licensed_library", "platform_library"].includes(asset.sourceKind), `${asset.assetId}: invalid sourceKind`);
    assert.ok(["VERIFIED", "PENDING", "REJECTED"].includes(asset.licenseStatus), `${asset.assetId}: invalid licenseStatus`);
    nonEmpty(asset.licenseRef, `${asset.assetId}.licenseRef`);
    assert.ok(Number(asset.durationSeconds) > 0, `${asset.assetId}: durationSeconds must be positive`);
    assert.ok(Array.isArray(asset.soundFamilies) && asset.soundFamilies.length > 0, `${asset.assetId}: soundFamilies are required`);
    assert.ok(Array.isArray(asset.platformScopes) && asset.platformScopes.length > 0, `${asset.assetId}: platformScopes are required`);
    if (asset.licenseStatus === "VERIFIED") {
      assert.equal(asset.commercialUseAllowed, true, `${asset.assetId}: commercial use is not allowed`);
      assert.equal(asset.trademarkImitation, false, `${asset.assetId}: trademark imitation is prohibited`);
    }
  }
  return { jobId: registry.jobId, status: registry.status, assets: registry.assets.length };
};

const gainForRole = {
  causal: -6,
  informational: -12,
  structural: -10,
  rhythmic: -12,
  emotional: -10,
  brand: -10,
  ambience: -18,
};
const busForRole = {
  causal: "sfx_causal",
  informational: "sfx_editorial",
  structural: "sfx_editorial",
  rhythmic: "sfx_editorial",
  emotional: "sfx_editorial",
  brand: "sfx_brand",
  ambience: "ambience",
};
const pitchForIntent = (intent) => {
  if (intent.tags?.includes("variant-b")) return -0.5;
  if (intent.tags?.includes("variant-c")) return -1;
  return 0;
};

const scoreAsset = (asset, intent) => {
  let score = 0;
  if (asset.soundFamilies.includes(intent.soundFamily)) score += 100;
  const tags = new Set(asset.tags ?? []);
  for (const tag of intent.tags ?? []) if (tags.has(tag)) score += 5;
  if (asset.sourceKind === "owned" || asset.sourceKind === "original_recording" || asset.sourceKind === "procedural") score += 2;
  return score;
};

export const selectSfxAssets = (soundIntentMap, registry, {
  soundIntentPath = "sound-intent-map.json",
  soundIntentSha256 = "0".repeat(64),
  registryPath = "sfx-asset-registry.json",
  registrySha256 = "0".repeat(64),
} = {}) => {
  validateSoundIntentMap(soundIntentMap, { requireReady: true });
  validateSfxAssetRegistry(registry, { requireVerified: true, platform: soundIntentMap.platform });
  assert.equal(registry.jobId, soundIntentMap.jobId, "SFX registry jobId does not match sound intent map");

  const eligible = registry.assets.filter((asset) => (
    asset.licenseStatus === "VERIFIED"
    && asset.commercialUseAllowed === true
    && asset.trademarkImitation === false
    && asset.platformScopes.includes(soundIntentMap.platform)
  ));
  const cues = [];
  const omittedIntents = [];
  for (const intent of soundIntentMap.cueIntents) {
    const candidates = eligible
      .filter((asset) => asset.soundFamilies.includes(intent.soundFamily))
      .map((asset) => ({ asset, score: scoreAsset(asset, intent) }))
      .sort((a, b) => b.score - a.score || a.asset.assetId.localeCompare(b.asset.assetId));
    if (candidates.length === 0) {
      if (intent.necessity === "required") throw new Error(`${intent.intentId}: no licensed asset matches required sound family ${intent.soundFamily}`);
      omittedIntents.push({ intentId: intent.intentId, reason: `No rights-verified ${intent.soundFamily} asset for ${soundIntentMap.platform}` });
      continue;
    }
    const asset = candidates[0].asset;
    const durationFrames = Math.max(1, Math.ceil(asset.durationSeconds * soundIntentMap.fps));
    const startFrame = intent.triggerFrame;
    const endFrame = Math.min(soundIntentMap.durationFrames, startFrame + durationFrames);
    const overlapsNarration = (soundIntentMap.narrationWindows ?? []).some((window) => startFrame < window.endFrame && endFrame > window.startFrame);
    if (overlapsNarration && intent.narrationOverlap !== "duck_required") {
      throw new Error(`${intent.intentId}: selected asset overlaps narration but the approved intent does not allow ducked overlap`);
    }
    cues.push({
      cueId: `cue-${intent.intentId}`,
      intentId: intent.intentId,
      assetId: asset.assetId,
      startFrame,
      endFrame,
      visualTriggerFrame: intent.triggerFrame,
      syncOffsetFrames: 0,
      category: intent.role,
      bus: busForRole[intent.role],
      gainDb: gainForRole[intent.role],
      pitchSemitones: pitchForIntent(intent),
      eqProfile: overlapsNarration ? "narration-safe" : "neutral",
      speechOverlap: overlapsNarration,
      ducking: overlapsNarration ? "planned" : "not_applicable",
      fadeInMs: intent.role === "ambience" ? 80 : 0,
      fadeOutMs: intent.role === "ambience" ? 160 : 40,
      status: "SELECTED"
    });
  }

  return {
    schemaVersion: 1,
    jobId: soundIntentMap.jobId,
    status: "READY_FOR_MIX",
    platform: soundIntentMap.platform,
    fps: soundIntentMap.fps,
    durationFrames: soundIntentMap.durationFrames,
    soundIntentMap: { path: soundIntentPath, sha256: soundIntentSha256 },
    assetRegistry: { path: registryPath, sha256: registrySha256 },
    cues,
    omittedIntents,
    mixPolicy: {
      narrationPriority: true,
      sidechainOrAutomationRequiredForSpeechOverlap: true,
      targetIntegratedLufs: -16,
      loudnessToleranceLu: 1,
      maximumTruePeakDbtp: -1,
      loudnessTargetRationale: "Configurable short-form review target; narration intelligibility and target-player review remain authoritative.",
      maximumOnsetsPerSecond: soundIntentMap.densityPolicy.maxOnsetsPerSecond,
      maximumSimultaneousUnderNarration: soundIntentMap.densityPolicy.maxSimultaneousUnderNarration,
      maximumSimultaneousWithoutNarration: soundIntentMap.densityPolicy.maxSimultaneousWithoutNarration
    },
    qc: {
      fullDecodePass: false,
      licenseCoverageStatus: "PASS",
      observedIntegratedLufs: null,
      observedTruePeakDbtp: null,
      noClipping: false,
      narrationIntelligibility: "PENDING",
      phoneSpeakerPass: false,
      headphonesPass: false,
      targetPlayerPass: false,
      highFrequencyFatiguePass: false,
      humanTasteStatus: "PENDING"
    },
    distribution: {
      publishAllowed: false,
      activateAdsAllowed: false,
      publicSkillDistributionAllowed: false
    }
  };
};

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const [soundIntentFile, registryFile, outputFile] = process.argv.slice(2);
  assert.ok(soundIntentFile && registryFile && outputFile, "Usage: select-sfx-assets.mjs <sound-intent-map.json> <sfx-asset-registry.json> <audio-cue-sheet.json>");
  const soundIntentText = readFileSync(soundIntentFile, "utf8");
  const registryText = readFileSync(registryFile, "utf8");
  const result = selectSfxAssets(JSON.parse(soundIntentText), JSON.parse(registryText), {
    soundIntentPath: path.basename(soundIntentFile),
    soundIntentSha256: hashText(soundIntentText),
    registryPath: path.basename(registryFile),
    registrySha256: hashText(registryText)
  });
  writeFileSync(outputFile, `${JSON.stringify(result, null, 2)}\n`, "utf8");
  console.log(`SFX asset selection: READY_FOR_MIX (${result.cues.length} cues, ${result.omittedIntents.length} omitted)`);
}
