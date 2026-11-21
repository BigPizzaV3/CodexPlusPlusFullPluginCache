#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

export function validatePacingReview(review) {
  assert.equal(review.schemaVersion, 1, "Pacing review: unsupported schemaVersion");
  const pacingContractVersion = review.pacingContractVersion ?? 1;
  assert.ok([1, 2].includes(pacingContractVersion), "Pacing review: unsupported pacingContractVersion");
  assert.ok(review.jobId, "Pacing review: jobId missing");
  assert.ok(["DRAFT", "READY_FOR_HUMAN_REVIEW", "APPROVED", "REVISE"].includes(review.status), "Pacing review: invalid status");
  assert.ok(["FINAL_LENGTH", "COMPREHENSION_FIRST_MASTER"].includes(review.mode), "Pacing review: invalid mode");
  assert.equal(review.human_review_required, true, "Pacing review: human review must remain required");
  assert.ok(Number.isFinite(review.duration_seconds) && review.duration_seconds > 0, "Pacing review: invalid duration");
  assert.ok(Number.isInteger(review.limits?.max_new_concepts_per_beat) && review.limits.max_new_concepts_per_beat >= 1, "Pacing review: invalid concept limit");
  assert.ok(Number.isInteger(review.limits?.max_simultaneous_reading_layers) && review.limits.max_simultaneous_reading_layers >= 1, "Pacing review: invalid reading-layer limit");
  if (pacingContractVersion === 2) {
    assert.ok(Number.isFinite(review.limits?.minimum_single_layer_read_seconds) && review.limits.minimum_single_layer_read_seconds >= 1, "Pacing review v2: invalid single-layer reading floor");
    assert.ok(Number.isFinite(review.limits?.minimum_two_layer_read_seconds) && review.limits.minimum_two_layer_read_seconds >= review.limits.minimum_single_layer_read_seconds, "Pacing review v2: invalid two-layer reading floor");
    assert.ok(Number.isFinite(review.limits?.minimum_post_read_hold_seconds) && review.limits.minimum_post_read_hold_seconds >= 0.5, "Pacing review v2: post-read hold must be at least 0.5 seconds");
  }
  assert.ok(Array.isArray(review.beats), "Pacing review: beats must be an array");
  if (review.mode === "COMPREHENSION_FIRST_MASTER" && review.status !== "APPROVED") {
    assert.equal(review.compression_allowed, false, "Pacing review: compression must remain blocked before Master approval");
    assert.ok(review.end_card_seconds >= 3.5, "Pacing review: comprehension Master End Card must hold for at least 3.5 seconds");
  }
  let previousEnd = null;
  for (const beat of review.beats) {
    const beatDuration = beat.end_seconds - beat.start_seconds;
    assert.ok(beatDuration > 0, `Pacing review ${beat.beat_id}: invalid timing`);
    if (previousEnd !== null) assert.ok(beat.start_seconds >= previousEnd, `Pacing review ${beat.beat_id}: beats overlap or run backward`);
    previousEnd = beat.end_seconds;
    assert.ok(beat.new_concepts <= review.limits.max_new_concepts_per_beat, `Pacing review ${beat.beat_id}: concept limit exceeded`);
    assert.ok(beat.simultaneous_reading_layers <= review.limits.max_simultaneous_reading_layers, `Pacing review ${beat.beat_id}: reading-layer limit exceeded`);
    if (pacingContractVersion === 2) {
      assert.ok(Number.isFinite(beat.minimum_read_seconds) && beat.minimum_read_seconds >= 0, `Pacing review v2 ${beat.beat_id}: minimum_read_seconds missing`);
      assert.ok(Number.isFinite(beat.post_read_hold_seconds) && beat.post_read_hold_seconds >= review.limits.minimum_post_read_hold_seconds, `Pacing review v2 ${beat.beat_id}: post-read hold is too short`);
      const readingFloor = beat.simultaneous_reading_layers >= 2
        ? review.limits.minimum_two_layer_read_seconds
        : beat.simultaneous_reading_layers === 1
          ? review.limits.minimum_single_layer_read_seconds
          : 0;
      assert.ok(beat.minimum_read_seconds >= readingFloor, `Pacing review v2 ${beat.beat_id}: declared reading time is below the layer floor`);
      assert.ok(beatDuration + 0.001 >= beat.minimum_read_seconds + beat.post_read_hold_seconds, `Pacing review v2 ${beat.beat_id}: beat ends before reading and comprehension hold complete`);
    }
    assert.ok(["PASS", "REVISE", "NOT_RUN"].includes(beat.status), `Pacing review ${beat.beat_id}: invalid status`);
  }
  if (review.status === "READY_FOR_HUMAN_REVIEW") {
    assert.ok(review.beats.length > 0, "Pacing review: reviewable Master requires beats");
    assert.ok(review.beats.every((beat) => beat.status === "PASS"), "Pacing review: prehuman beat checks must pass before human review");
  }
  return { beats: review.beats.length, duration: review.duration_seconds, pacingContractVersion };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-pacing-review.mjs <pacing-review.json>");
  const result = validatePacingReview(JSON.parse(await readFile(file, "utf8")));
  console.log(`Pacing review: PASS (${result.beats} beats / ${result.duration}s)`);
}
