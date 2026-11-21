#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const READY_STATES = new Set(["READY_FOR_PRODUCTION", "PASS_LOCAL_REVIEW"]);
const SPOKEN_DELIVERIES = new Set(["spoken_and_visual", "spoken_only"]);
const MESSAGE_ROLES = new Set(["recognition", "tension", "failed_workaround", "hope", "mechanism", "proof", "payoff", "cta"]);
const SFX_MATCH = {
  impact: "impact",
  rupture: "rupture",
  passage: "whoosh",
  landing: "landing",
  transition: "transition",
  notification: "notification",
};
const RECOVERY_ORDER = [
  "trim_verified_edges",
  "fit_within_approved_tempo",
  "bounded_timeline_extension",
  "resynthesize_with_fresh_approval",
];

const nonEmpty = (value, label) => {
  assert.equal(typeof value === "string" && value.trim().length > 0, true, `${label} is required`);
};
const closeTo = (actual, expected, tolerance, label) => {
  assert.ok(Math.abs(actual - expected) <= tolerance, `${label}: expected ${expected}, received ${actual}`);
};
const normalized = (value) => value.normalize("NFKC").replace(/[\s、。！？!?,.・「」『』]/gu, "").toLowerCase();

export const validateTimelineAudioContract = (contract, { requireReady = false } = {}) => {
  assert.equal(contract.schemaVersion, 1, "timeline/audio contract: schemaVersion must be 1");
  nonEmpty(contract.jobId, "timeline/audio contract jobId");
  assert.ok(["DRAFT", "READY_FOR_PRODUCTION", "PASS_LOCAL_REVIEW", "REVISE"].includes(contract.status), "timeline/audio contract: invalid status");
  if (requireReady) assert.ok(READY_STATES.has(contract.status), "timeline/audio contract: contract is not ready");
  const ready = requireReady || READY_STATES.has(contract.status);
  assert.ok(Number(contract.fps) > 0, "timeline/audio contract: fps must be positive");
  assert.ok(Number.isInteger(contract.durationFrames) && contract.durationFrames > 0, "timeline/audio contract: durationFrames must be a positive integer");
  assert.equal(contract.slotDesign?.targetOccupancyMin, 0.88, "timeline/audio contract: provisional occupancy minimum must remain 0.88");
  assert.equal(contract.slotDesign?.targetOccupancyMax, 0.92, "timeline/audio contract: provisional occupancy maximum must remain 0.92");
  assert.equal(contract.slotDesign?.oversizedBufferProhibited, true, "timeline/audio contract: oversized buffers must remain prohibited");
  assert.equal(contract.sfxCoverageReviewed, true, "timeline/audio contract: every physical/notification event needs an SFX coverage review");
  assert.equal(contract.distribution?.publishAllowed, false, "timeline/audio contract: publishing must remain blocked");
  assert.equal(contract.distribution?.activateAdsAllowed, false, "timeline/audio contract: ad activation must remain blocked");
  assert.equal(contract.distribution?.publicSkillDistributionAllowed, false, "timeline/audio contract: public Skill distribution must remain blocked");

  const beats = contract.messageBeats ?? [];
  assert.ok(Array.isArray(beats), "timeline/audio contract: messageBeats must be an array");
  if (ready) assert.ok(beats.length > 0, "timeline/audio contract: ready messageBeats must not be empty");
  const beatById = new Map();
  const firstBeatByMessageKey = new Map();
  let previousEnd = 0;
  let previousPrimary = null;
  for (const beat of beats) {
    nonEmpty(beat.beatId, "message beatId");
    assert.equal(beatById.has(beat.beatId), false, `timeline/audio contract: duplicate beatId ${beat.beatId}`);
    assert.ok(MESSAGE_ROLES.has(beat.role), `${beat.beatId}: invalid message role`);
    assert.ok(Number.isInteger(beat.startFrame) && Number.isInteger(beat.endFrame) && beat.endFrame > beat.startFrame, `${beat.beatId}: invalid frame range`);
    assert.ok(beat.startFrame >= previousEnd, `${beat.beatId}: beats overlap or run backward`);
    assert.ok(beat.endFrame <= contract.durationFrames, `${beat.beatId}: beat exceeds timeline`);
    nonEmpty(beat.primaryMessage, `${beat.beatId}.primaryMessage`);
    nonEmpty(beat.messageKey, `${beat.beatId}.messageKey`);
    assert.ok(["major", "supporting"].includes(beat.importance), `${beat.beatId}: invalid importance`);
    assert.ok(["spoken_and_visual", "spoken_only", "visual_only"].includes(beat.delivery), `${beat.beatId}: invalid delivery`);

    if (SPOKEN_DELIVERIES.has(beat.delivery)) nonEmpty(beat.spokenText, `${beat.beatId}.spokenText`);
    if (beat.delivery === "visual_only") assert.equal(beat.spokenText, null, `${beat.beatId}: visual-only beat cannot pretend to have spoken copy`);
    if (beat.importance === "major" && ["payoff", "cta"].includes(beat.role)) {
      assert.ok(SPOKEN_DELIVERIES.has(beat.delivery), `${beat.beatId}: major ${beat.role} cannot be silent`);
    }

    if (previousPrimary !== null) {
      assert.notEqual(normalized(beat.primaryMessage), previousPrimary, `${beat.beatId}: consecutive beats repeat the same primary message`);
    }
    const repeatedBeatId = firstBeatByMessageKey.get(beat.messageKey);
    if (repeatedBeatId) {
      assert.equal(beat.progression, "intentional_recap", `${beat.beatId}: repeated messageKey requires intentional_recap`);
      assert.equal(beat.repeatsBeatId, repeatedBeatId, `${beat.beatId}: repeated messageKey must point to its original beat`);
      nonEmpty(beat.repeatRationale, `${beat.beatId}.repeatRationale`);
    } else {
      assert.equal(beat.progression, "new_information", `${beat.beatId}: a new message must advance as new_information`);
      assert.equal(beat.repeatsBeatId, null, `${beat.beatId}: new information cannot repeat another beat`);
      assert.equal(beat.repeatRationale, null, `${beat.beatId}: new information cannot carry repeat rationale`);
      firstBeatByMessageKey.set(beat.messageKey, beat.beatId);
    }

    beatById.set(beat.beatId, beat);
    previousEnd = beat.endFrame;
    previousPrimary = normalized(beat.primaryMessage);
  }

  const cues = contract.narrationCues ?? [];
  assert.ok(Array.isArray(cues), "timeline/audio contract: narrationCues must be an array");
  const cueByBeat = new Map();
  const clipIds = new Set();
  for (const cue of cues) {
    nonEmpty(cue.clipId, "narration clipId");
    assert.equal(clipIds.has(cue.clipId), false, `timeline/audio contract: duplicate clipId ${cue.clipId}`);
    clipIds.add(cue.clipId);
    const beat = beatById.get(cue.beatId);
    assert.ok(beat, `${cue.clipId}: unknown beatId ${cue.beatId}`);
    assert.equal(cueByBeat.has(cue.beatId), false, `${cue.beatId}: use one approved narration unit per message beat`);
    assert.equal(cue.exactText, beat.spokenText, `${cue.clipId}: exactText must equal the approved spokenText`);
    assert.ok(Number.isInteger(cue.startFrame) && Number.isInteger(cue.nextCueFrame) && cue.nextCueFrame > cue.startFrame, `${cue.clipId}: invalid cue frame range`);
    assert.ok(cue.startFrame >= beat.startFrame && cue.nextCueFrame <= beat.endFrame, `${cue.clipId}: narration slot must stay inside its message beat`);
    const computedSlot = (cue.nextCueFrame - cue.startFrame) / contract.fps;
    closeTo(cue.slotSeconds, computedSlot, 0.001, `${cue.clipId}.slotSeconds`);
    const computedOccupancy = cue.plannedSpeechSeconds / cue.slotSeconds;
    closeTo(cue.plannedOccupancyRatio, computedOccupancy, 0.001, `${cue.clipId}.plannedOccupancyRatio`);
    assert.ok(cue.plannedOccupancyRatio >= contract.slotDesign.targetOccupancyMin - 0.001, `${cue.clipId}: speech slot has too much buffer and will drag`);
    assert.ok(cue.plannedOccupancyRatio <= contract.slotDesign.targetOccupancyMax + 0.001, `${cue.clipId}: speech slot has insufficient provider/edit headroom`);
    assert.ok(cue.tempoRatio <= 1.25, `${cue.clipId}: tempo exceeds the approved short-form envelope`);
    if (cue.tempoRatio > 1.12) assert.equal(cue.paceApprovalStatus, "human_approved", `${cue.clipId}: tempo above 1.12x requires human pace approval`);
    else if (cue.tempoRatio > 1.05) assert.ok(["ab_review_pass", "human_approved"].includes(cue.paceApprovalStatus), `${cue.clipId}: tempo above 1.05x requires A/B review`);
    if (contract.status === "PASS_LOCAL_REVIEW") assert.equal(cue.copyVerificationStatus, "PASS", `${cue.clipId}: local-review PASS requires verified exact copy`);
    cueByBeat.set(cue.beatId, cue);
  }
  for (const beat of beats) {
    if (SPOKEN_DELIVERIES.has(beat.delivery)) assert.ok(cueByBeat.has(beat.beatId), `${beat.beatId}: spoken beat is missing narration`);
  }

  const sfxCues = contract.sfxCues ?? [];
  assert.ok(Array.isArray(sfxCues), "timeline/audio contract: sfxCues must be an array");
  const eventIds = new Set();
  for (const cue of sfxCues) {
    nonEmpty(cue.eventId, "SFX eventId");
    assert.equal(eventIds.has(cue.eventId), false, `timeline/audio contract: duplicate SFX eventId ${cue.eventId}`);
    eventIds.add(cue.eventId);
    assert.ok(beatById.has(cue.beatId), `${cue.eventId}: unknown beatId ${cue.beatId}`);
    assert.equal(cue.cueType, SFX_MATCH[cue.eventType], `${cue.eventId}: cue type does not express the visible cause`);
    assert.ok(Number.isInteger(cue.visualEventFrame) && Number.isInteger(cue.cueStartFrame), `${cue.eventId}: SFX frames must be integers`);
    assert.ok(cue.visualEventFrame >= 0 && cue.visualEventFrame < contract.durationFrames, `${cue.eventId}: visual event is outside timeline`);
    assert.ok(Math.abs(cue.cueStartFrame - cue.visualEventFrame) <= cue.maxOffsetFrames, `${cue.eventId}: SFX is not aligned to the final retimed visual event`);
  }

  const proof = contract.proofPresentation ?? {};
  assert.ok(beatById.has(proof.beatId) || proof.sourceAuditStatus === "NOT_APPLICABLE", "timeline/audio contract: proof beat is unknown");
  nonEmpty(proof.primaryHeadline, "proofPresentation.primaryHeadline");
  assert.equal(proof.administrativeCopyIsPrimary, false, "timeline/audio contract: administrative proof labels cannot become the primary ad message");
  assert.equal(proof.headlineScale, "dominant", "timeline/audio contract: the proof payoff headline must be visually dominant");
  if (proof.sourceAuditStatus === "PASS") {
    assert.equal(proof.mosaicApplied, false, "timeline/audio contract: use safe proof sources instead of obscuring them with mosaic");
    assert.ok(proof.readableAnchorCount >= 1, "timeline/audio contract: proof needs a readable anchor");
    if (proof.quantityAssetCount > 1) assert.ok(proof.readableAnchorCount >= 2, "timeline/audio contract: quantity proof needs readable anchors before and after the montage");
  }

  const recovery = contract.ttsRecoveryPolicy ?? {};
  assert.equal(recovery.slotEvaluationBasis, "maximum_available_slot", "timeline/audio contract: evaluate TTS against the maximum safe slot, not an aspirational target");
  assert.equal(recovery.preserveProviderOutputBeforePaceGate, true, "timeline/audio contract: preserve paid provider output before pace assertions");
  assert.equal(recovery.retainRequestIdBeforePaceGate, true, "timeline/audio contract: retain request ID before pace assertions");
  assert.equal(recovery.automaticRetryAllowed, false, "timeline/audio contract: paid TTS must never auto-retry");
  assert.equal(recovery.paidRetryRequiresFreshApproval, true, "timeline/audio contract: a new paid TTS call needs fresh approval");
  assert.deepEqual(recovery.recoveryOrder, RECOVERY_ORDER, "timeline/audio contract: TTS recovery order is unsafe or wasteful");

  const finalTiming = contract.finalTimingQc ?? {};
  assert.equal(finalTiming.expectedDurationSource, "video_stream", "timeline/audio contract: expected duration must be checked against the video stream");
  assert.ok(finalTiming.allowedContainerTailMilliseconds <= 100, "timeline/audio contract: container-tail allowance exceeds 100 ms");
  if (contract.status === "PASS_LOCAL_REVIEW") {
    closeTo(finalTiming.observedVideoDurationSeconds, finalTiming.expectedVideoDurationSeconds, 1 / contract.fps + 0.001, "final video-stream duration");
    const tailMs = (finalTiming.observedContainerDurationSeconds - finalTiming.observedVideoDurationSeconds) * 1000;
    assert.ok(tailMs >= -1 && tailMs <= finalTiming.allowedContainerTailMilliseconds + 0.5, `timeline/audio contract: container tail ${tailMs.toFixed(1)} ms is out of bounds`);
    assert.equal(finalTiming.fullDecodePass, true, "timeline/audio contract: full decode must pass");
    assert.equal(finalTiming.targetPlayerPass, true, "timeline/audio contract: target-player review must pass");
  }

  if (ready) {
    assert.equal(contract.slotDesign?.provisionalVoiceUsed, true, "timeline/audio contract: provisional voice must set the timeline before production");
    assert.ok(beats.some((beat) => beat.role === "recognition"), "timeline/audio contract: recognition beat missing");
    assert.ok(beats.some((beat) => beat.role === "hope"), "timeline/audio contract: hope beat missing");
    assert.ok(beats.some((beat) => beat.role === "payoff"), "timeline/audio contract: payoff beat missing");
    assert.ok(beats.some((beat) => beat.role === "cta"), "timeline/audio contract: CTA beat missing");
  }

  return { jobId: contract.jobId, status: contract.status, beats: beats.length, narrationCues: cues.length, sfxCues: sfxCues.length };
};

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const inputPath = process.argv[2];
  assert.ok(inputPath, "Usage: validate-timeline-audio-contract.mjs <timeline-audio-contract.json> [--require-ready]");
  const contract = JSON.parse(readFileSync(inputPath, "utf8"));
  const result = validateTimelineAudioContract(contract, { requireReady: process.argv.includes("--require-ready") });
  console.log(`timeline/audio contract: PASS (${result.jobId} / ${result.beats} beats / ${result.narrationCues} narration / ${result.sfxCues} SFX)`);
}
