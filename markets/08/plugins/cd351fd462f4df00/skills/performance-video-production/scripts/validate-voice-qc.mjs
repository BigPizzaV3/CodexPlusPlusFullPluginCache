#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const allowedOverall = ["PENDING_HUMAN_REVIEW", "FAIL", "PASS"];
const allowedReview = ["PENDING", "FAIL", "PASS"];

export const validateVoiceQc = (report, { requirePass = false } = {}) => {
  assert.equal(report.schemaVersion, 1, "schemaVersion must be 1");
  assert.ok(allowedOverall.includes(report.status), "voice QC status is invalid");
  assert.ok(Array.isArray(report.expectedClipIds) && report.expectedClipIds.length > 0, "expectedClipIds must not be empty");
  assert.ok(Array.isArray(report.clips) && report.clips.length > 0, "voice QC clips must not be empty");

  const ids = new Set();
  for (const clip of report.clips) {
    assert.equal(typeof clip.id === "string" && clip.id.length > 0, true, "clip id is required");
    assert.equal(ids.has(clip.id), false, `duplicate voice clip: ${clip.id}`);
    ids.add(clip.id);
    assert.ok(allowedReview.includes(clip.status), `${clip.id}: clip status is invalid`);
    assert.equal(typeof clip.expectedText === "string" && clip.expectedText.length > 0, true, `${clip.id}: expectedText is required`);
    assert.ok(["human", "asr", "human_plus_asr", "pending"].includes(clip.transcriptReview?.method), `${clip.id}: transcript method is invalid`);
    for (const key of ["status", "languageMatch", "copyComplete", "foreignOrHallucinatedTail", "pronunciationStatus", "intelligibilityStatus"]) {
      assert.notEqual(clip.transcriptReview?.[key], undefined, `${clip.id}: transcriptReview.${key} is required`);
    }
    assert.ok(allowedReview.includes(clip.transcriptReview.status), `${clip.id}: transcript status is invalid`);
    assert.ok(allowedReview.includes(clip.transcriptReview.pronunciationStatus), `${clip.id}: pronunciationStatus is invalid`);
    assert.ok(allowedReview.includes(clip.transcriptReview.intelligibilityStatus), `${clip.id}: intelligibilityStatus is invalid`);
    assert.equal(typeof clip.audioQuality?.tempoRatio, "number", `${clip.id}: tempoRatio is required`);
    assert.equal(typeof clip.audioQuality?.muffled === "boolean" || (clip.status === "PENDING" && clip.audioQuality?.muffled === null), true, `${clip.id}: muffled must be boolean after review`);
    assert.equal(typeof clip.audioQuality?.clipped, "boolean", `${clip.id}: clipped is required`);
    assert.ok(allowedReview.includes(clip.audioQuality?.status), `${clip.id}: audio quality status is invalid`);
    assert.ok(allowedReview.includes(clip.syncReview?.status), `${clip.id}: sync status is invalid`);

    if (clip.status === "PASS") {
      assert.equal(clip.transcriptReview.status, "PASS", `${clip.id}: PASS requires transcript PASS`);
      assert.equal(clip.transcriptReview.languageMatch, true, `${clip.id}: PASS requires Japanese language match`);
      assert.equal(clip.transcriptReview.copyComplete, true, `${clip.id}: PASS requires complete copy`);
      assert.equal(clip.transcriptReview.foreignOrHallucinatedTail, false, `${clip.id}: hallucinated tail is forbidden`);
      assert.equal(clip.transcriptReview.pronunciationStatus, "PASS", `${clip.id}: pronunciation must PASS`);
      assert.equal(clip.transcriptReview.intelligibilityStatus, "PASS", `${clip.id}: intelligibility must PASS`);
      assert.ok(
        clip.audioQuality.tempoRatio <= 1.12 ||
          (clip.audioQuality.tempoRatio <= 1.25 && clip.audioQuality.editorialExceptionApproved === true),
        `${clip.id}: tempo ratio exceeds the approved short-form envelope`,
      );
      assert.equal(clip.audioQuality.muffled, false, `${clip.id}: muffled audio cannot PASS`);
      assert.equal(clip.audioQuality.clipped, false, `${clip.id}: clipped audio cannot PASS`);
      assert.equal(clip.audioQuality.status, "PASS", `${clip.id}: audio quality must PASS`);
      assert.equal(clip.syncReview.status, "PASS", `${clip.id}: sync must PASS`);
    }
  }

  assert.deepEqual([...ids].sort(), [...new Set(report.expectedClipIds)].sort(), "voice QC must cover every expected clip exactly once");

  assert.ok(allowedReview.includes(report.humanTasteStatus), "humanTasteStatus is invalid");
  if (report.status === "PASS") {
    assert.equal(report.humanTasteStatus, "PASS", "overall PASS requires human Taste PASS");
    assert.equal(report.clips.every((clip) => clip.status === "PASS"), true, "overall PASS requires every clip PASS");
  }
  if (report.status === "FAIL") {
    assert.equal(report.clips.some((clip) => clip.status === "FAIL"), true, "overall FAIL requires at least one failed clip");
  }
  if (requirePass) assert.equal(report.status, "PASS", "voice QC is not PASS");
  return report;
};

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const inputPath = process.argv[2];
  assert.ok(inputPath, "Usage: validate-voice-qc.mjs <voice-qc.json> [--require-pass]");
  const report = JSON.parse(readFileSync(inputPath, "utf8"));
  validateVoiceQc(report, { requirePass: process.argv.includes("--require-pass") });
  console.log(`voice QC contract: VALID (${report.status})`);
}
