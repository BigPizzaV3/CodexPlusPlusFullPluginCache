#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const READY = "READY_FOR_HUMAN_LAST_MILE_REVIEW";
const PROOF_SEQUENCE = [
  "large_readable_proof",
  "rapid_quantity_cascade",
  "quantity_wall",
  "large_payoff_proof",
];

export function validateFirstPassBaseline(baseline, { requireReady = false } = {}) {
  assert.equal(baseline.schemaVersion, 1, "First-pass baseline: unsupported schemaVersion");
  assert.ok(baseline.jobId, "First-pass baseline: jobId missing");
  assert.ok(["DRAFT", READY, "REVISE"].includes(baseline.status), "First-pass baseline: invalid status");
  assert.equal(baseline.productionMode, "first_pass_85_baseline", "First-pass baseline: invalid productionMode");
  assert.equal(baseline.targetCompletionPercent, 85, "First-pass baseline: target must remain 85 percent");
  assert.ok(baseline.selectedTerritoryId, "First-pass baseline: selectedTerritoryId missing");
  assert.equal(baseline.review?.lastMileHumanReviewRequired, true, "First-pass baseline: last-mile human review must remain required");
  assert.equal(baseline.learningBoundary?.completionPercentIsPerformanceEvidence, false, "First-pass baseline: completion estimate cannot be performance evidence");
  assert.equal(baseline.learningBoundary?.campaignPerformanceObserved, false, "First-pass baseline: campaign performance must remain unobserved");
  assert.equal(baseline.distribution?.publishAllowed, false, "First-pass baseline: publishing must remain blocked");
  assert.equal(baseline.distribution?.activateAdsAllowed, false, "First-pass baseline: ad activation must remain blocked");
  assert.equal(baseline.distribution?.publicSkillDistributionAllowed, false, "First-pass baseline: public Skill distribution must remain blocked");

  const timeline = baseline.timeline ?? {};
  assert.ok(Number.isFinite(timeline.durationSeconds) && timeline.durationSeconds > 0, "First-pass baseline: invalid duration");
  assert.ok(Number.isFinite(timeline.incidentBySeconds) && timeline.incidentBySeconds <= 0.5, "First-pass baseline: incident must appear by 0.5 seconds");
  assert.ok(Number.isFinite(timeline.whoAndProblemBySeconds) && timeline.whoAndProblemBySeconds <= 2, "First-pass baseline: WHO and problem must appear by two seconds");
  assert.ok(Number.isFinite(timeline.endCardSeconds) && timeline.endCardSeconds >= 3.5, "First-pass baseline: End Card must hold for at least 3.5 seconds");
  assert.ok(Array.isArray(timeline.beats), "First-pass baseline: beats must be an array");

  let previousEnd = 0;
  for (const beat of timeline.beats) {
    assert.ok(beat.beatId && beat.semanticJob, "First-pass baseline: every beat needs an ID and semantic job");
    assert.ok(["comprehension_anchor", "action_compression", "quantity_montage", "payoff_anchor", "end_card"].includes(beat.role), `First-pass baseline ${beat.beatId}: invalid role`);
    assert.ok(Number.isFinite(beat.startSeconds) && Number.isFinite(beat.endSeconds) && beat.endSeconds > beat.startSeconds, `First-pass baseline ${beat.beatId}: invalid timing`);
    assert.ok(beat.startSeconds + 0.001 >= previousEnd, `First-pass baseline ${beat.beatId}: beats overlap or run backward`);
    assert.ok(beat.endSeconds <= timeline.durationSeconds + 0.001, `First-pass baseline ${beat.beatId}: beat exceeds duration`);
    if (beat.role === "quantity_montage") {
      assert.notEqual(beat.introducesNewClaim, true, `First-pass baseline ${beat.beatId}: quantity montage cannot introduce a new claim`);
    }
    previousEnd = beat.endSeconds;
  }

  const hero = baseline.generatedHero ?? {};
  assert.equal(hero.motionInterpolationApplied, false, "First-pass baseline: motion interpolation cannot be the default integration path");
  assert.ok(Array.isArray(hero.speedSegments), "First-pass baseline: speedSegments must be an array");
  if (hero.used) {
    assert.ok(hero.rawAssetRef, "First-pass baseline: generated hero needs a Raw asset reference");
    assert.match(hero.rawSha256 ?? "", /^[a-f0-9]{64}$/, "First-pass baseline: generated hero needs a Raw SHA-256");
    assert.equal(hero.rawReviewedAtNaturalSpeed, true, "First-pass baseline: generated Raw must be reviewed at natural speed");
    assert.equal(hero.humanRawApproval, "approved", "First-pass baseline: generated Raw needs human approval");
    assert.ok(["trimmed", "none_detected"].includes(hero.deadAirDecision), "First-pass baseline: generated Raw needs a dead-air decision");
    assert.ok(Number.isFinite(hero.sourceFrameRate) && hero.sourceFrameRate > 0, "First-pass baseline: source frame rate missing");
    assert.ok(Number.isFinite(hero.deliveryFrameRate) && hero.deliveryFrameRate > 0, "First-pass baseline: delivery frame rate missing");
    for (const segment of hero.speedSegments) {
      assert.ok(segment.sourceEndSeconds > segment.sourceStartSeconds, "First-pass baseline: invalid speed-segment boundary");
      assert.ok(Number.isFinite(segment.rate) && segment.rate > 0, "First-pass baseline: invalid speed rate");
    }
    if (hero.speedSegments.some((segment) => segment.rate !== 1)) {
      assert.ok(hero.speedSegments.some((segment) => segment.purpose === "preserve_readable_endpoint" && segment.rate === 1), "First-pass baseline: a retimed hero must preserve a native-speed readable endpoint");
    }
  } else {
    assert.equal(hero.humanRawApproval, "not_applicable", "First-pass baseline: unused generated hero must be not_applicable");
    assert.equal(hero.deadAirDecision, "not_applicable", "First-pass baseline: unused generated hero must have no dead-air decision");
  }

  const proof = baseline.proof ?? {};
  assert.ok(["none", "offer_artifact"].includes(proof.mode), "First-pass baseline: invalid proof mode");
  assert.ok(Array.isArray(proof.sourceRefs) && Array.isArray(proof.sequence), "First-pass baseline: proof arrays missing");
  assert.equal(proof.resultsClaimUsed, false, "First-pass baseline: unverified results claims are prohibited");
  if (proof.mode === "offer_artifact") {
    assert.equal(proof.sourceAuditStatus, "pass", "First-pass baseline: artifact proof needs a passing source audit");
    assert.ok(proof.sourceRefs.length > 0, "First-pass baseline: artifact proof needs source refs");
    assert.ok(proof.sourceClassification, "First-pass baseline: artifact proof needs source classification");
    assert.equal(proof.mosaicApplied, false, "First-pass baseline: artifact proof must remain readable; use safe source material instead of mosaic");
    assert.ok(["readable_anchor_then_quantity", "single_artifact_demo"].includes(proof.presentationStrategy), "First-pass baseline: artifact proof needs an adaptive presentation strategy");
    assert.ok(proof.readableAnchorCount >= 1, "First-pass baseline: artifact proof needs at least one readable anchor");
    if (proof.presentationStrategy === "readable_anchor_then_quantity") {
      assert.ok(proof.readableAnchorCount >= 2, "First-pass baseline: quantity proof needs readable anchors before and after the montage");
      assert.ok(proof.quantityAssetCount >= 6, "First-pass baseline: a quantity claim needs at least six source-audited assets");
      assert.deepEqual(proof.sequence, PROOF_SEQUENCE, "First-pass baseline: quantity proof must use anchor -> cascade -> wall -> payoff");
    } else {
      assert.ok(proof.quantityAssetCount >= 1, "First-pass baseline: single-artifact proof needs one source-audited asset");
      assert.deepEqual(proof.sequence, ["large_readable_proof", "large_payoff_proof"], "First-pass baseline: single-artifact proof must stay readable");
    }
    for (const source of proof.sourceRefs) {
      assert.ok(source.assetRef, "First-pass baseline: proof source assetRef missing");
      assert.match(source.sha256 ?? "", /^[a-f0-9]{64}$/, "First-pass baseline: proof source SHA-256 missing");
    }
  } else {
    assert.equal(proof.presentationStrategy, "none", "First-pass baseline: no-proof mode must use no presentation strategy");
    assert.equal(proof.sourceAuditStatus, "not_applicable", "First-pass baseline: no-proof mode must use not_applicable source audit");
    assert.equal(proof.sourceRefs.length, 0, "First-pass baseline: no-proof mode cannot retain source refs");
    assert.equal(proof.readableAnchorCount, 0, "First-pass baseline: no-proof mode cannot claim readable proof anchors");
    assert.equal(proof.quantityAssetCount, 0, "First-pass baseline: no-proof mode cannot claim quantity assets");
    assert.equal(proof.sequence.length, 0, "First-pass baseline: no-proof mode cannot claim a proof sequence");
  }

  if (requireReady || baseline.status === READY) {
    assert.equal(baseline.status, READY, "First-pass baseline: not ready for human last-mile review");
    for (const [name, passed] of Object.entries(baseline.prerequisites ?? {})) {
      assert.equal(passed, true, `First-pass baseline: prerequisite ${name} must pass`);
    }
    for (const name of ["offer", "audience", "funnelRole", "hookBodyArc", "destinationCta"]) {
      assert.equal(baseline.locks?.[name], true, `First-pass baseline: lock ${name} must be true`);
    }
    assert.ok(baseline.locks?.tempoProfile && baseline.locks.tempoProfile !== "unresolved", "First-pass baseline: tempo profile is unresolved");
    assert.equal(timeline.oneSemanticActionPerCut, true, "First-pass baseline: every cut needs one semantic action");
    assert.ok(timeline.beats.some((beat) => beat.role === "comprehension_anchor"), "First-pass baseline: comprehension anchor missing");
    assert.ok(timeline.beats.some((beat) => beat.role === "payoff_anchor"), "First-pass baseline: payoff anchor missing");
    const endCard = timeline.beats.find((beat) => beat.role === "end_card");
    assert.ok(endCard, "First-pass baseline: End Card beat missing");
    assert.ok(endCard.endSeconds - endCard.startSeconds + 0.001 >= timeline.endCardSeconds, "First-pass baseline: End Card beat is shorter than declared hold");
    for (const name of ["exactJapanese", "brand", "offerTerms", "cta", "constantFrameRate", "startAtZero", "fullDecodePass", "targetPlayerBoundaryPass"]) {
      assert.equal(baseline.deterministicFinish?.[name], true, `First-pass baseline: deterministic finish ${name} must pass`);
    }
    assert.equal(baseline.deterministicFinish?.width, 1080, "First-pass baseline: width must be 1080");
    assert.equal(baseline.deterministicFinish?.height, 1920, "First-pass baseline: height must be 1920");
    assert.equal(baseline.deterministicFinish?.pixelFormat, "yuv420p", "First-pass baseline: pixel format must be yuv420p");
    assert.equal(baseline.review?.machineCreativeGate, "PASS", "First-pass baseline: machine Creative gate must pass");
    assert.equal(baseline.review?.technicalGate, "PASS", "First-pass baseline: technical gate must pass");
    assert.ok(["pending", "approximately_85_percent"].includes(baseline.review?.humanAssessment), "First-pass baseline: invalid human last-mile state");
  }

  return {
    jobId: baseline.jobId,
    status: baseline.status,
    beats: timeline.beats.length,
    proofMode: proof.mode,
  };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-first-pass-baseline.mjs <first-pass-baseline.json> [--require-ready]");
  const baseline = JSON.parse(await readFile(file, "utf8"));
  const result = validateFirstPassBaseline(baseline, { requireReady: process.argv.includes("--require-ready") });
  console.log(`First-pass 85 baseline: PASS (${result.jobId} / ${result.beats} beats / ${result.proofMode})`);
}
