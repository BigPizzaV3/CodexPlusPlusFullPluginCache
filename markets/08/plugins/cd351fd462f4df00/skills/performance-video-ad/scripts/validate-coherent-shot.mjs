#!/usr/bin/env node
import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const QC_FIELDS = ["centralCausalEvent", "impactEnergy", "identityFidelity", "naturalSpeedReadability", "adjacentSurfaceContinuity"];

export function validateCoherentShot(spec, { specPath = null, requireRawApproval = false } = {}) {
  assert.equal(spec.schemaVersion, 1, "coherent shot: unsupported schemaVersion");
  assert.equal(spec.generationUnit, "coherent_shot", "coherent shot: generationUnit must be coherent_shot");
  assert.ok(spec.jobId && spec.shotId, "coherent shot: jobId and shotId are required");
  assert.ok(spec.durationSeconds > 0 && spec.durationSeconds <= 12, "coherent shot: duration must be within 0-12 seconds");
  assert.ok(spec.oneSentenceIntent && spec.cameraSetup && spec.dominantEvent, "coherent shot: intent, cameraSetup, and dominantEvent are required");
  assert.ok(spec.expressionControl?.profile, "coherent shot: expressionControl is required");
  if (spec.expressionControl.profile === "spectacle_experiment") {
    assert.equal(spec.expressionControl.explicitUserPermission, true, "coherent shot: spectacle_experiment requires explicit user permission");
    assert.ok(spec.expressionControl.experimentPurpose, "coherent shot: spectacle_experiment requires an experiment purpose");
  }
  assert.ok(Array.isArray(spec.causalArc) && spec.causalArc.length >= 3 && spec.causalArc.length <= 5, "coherent shot: causalArc requires three to five steps");
  assert.deepEqual(spec.causalArc.map((step) => step.order), spec.causalArc.map((_, index) => index + 1), "coherent shot: causalArc orders must be contiguous");
  assert.equal(spec.controlBudget?.exactUiInAi, false, "coherent shot: exact UI must remain deterministic");
  assert.equal(spec.controlBudget?.exactTextInAi, false, "coherent shot: exact text must remain deterministic");
  assert.ok(Array.isArray(spec.referencePack) && spec.referencePack.length >= 2 && spec.referencePack.length <= 5, "coherent shot: referencePack must contain two to five items");
  const roles = spec.referencePack.map((reference) => reference.role);
  assert.equal(new Set(roles).size, roles.length, "coherent shot: reference roles must be unique");
  for (const requiredRole of ["identity_front", "identity_three_quarter"]) {
    assert.ok(roles.includes(requiredRole), `coherent shot: ${requiredRole} is required`);
  }
  const motionDriver = spec.referencePack.find((reference) => reference.role === "motion_driver");
  if (motionDriver) {
    assert.equal(motionDriver.conditioning, true, "coherent shot: motion driver must be an explicit conditioning reference");
    assert.equal(motionDriver.semantics, "motion_only", "coherent shot: motion driver semantics must be motion_only");
  }
  assert.equal(spec.humanAnimatic?.conditioning, false, "coherent shot: human Animatic must not condition generation by default");
  assert.equal(spec.humanAnimatic?.role, "human_comprehension_and_timing_only", "coherent shot: invalid human Animatic role");
  assert.ok(Array.isArray(spec.aiResponsibilities) && spec.aiResponsibilities.length > 0, "coherent shot: AI responsibilities missing");
  assert.ok(Array.isArray(spec.deterministicResponsibilities) && spec.deterministicResponsibilities.length > 0, "coherent shot: deterministic responsibilities missing");
  assert.ok(["not_used", "motion_only"].includes(spec.promptKernel?.motionReferenceRule), "coherent shot: prompt must declare motion reference use");
  assert.equal(spec.promptKernel.motionReferenceRule, motionDriver ? "motion_only" : "not_used", "coherent shot: motion reference declaration does not match the pack");
  assert.ok(Array.isArray(spec.promptKernel?.avoid) && spec.promptKernel.avoid.length > 0 && spec.promptKernel.avoid.length <= 12, "coherent shot: keep the avoid list between one and twelve items");
  assert.equal(spec.rawHeroQc?.deviationPolicy, "fail_on_intent_loss", "coherent shot: hero deviation policy must fail on intent loss");
  for (const field of QC_FIELDS) assert.ok(["NOT_RUN", "PASS", "FAIL"].includes(spec.rawHeroQc?.[field]), `coherent shot: invalid ${field}`);
  if (spec.rawHeroQc?.humanDecision === "approved" || requireRawApproval) {
    assert.equal(spec.rawHeroQc.humanDecision, "approved", "coherent shot: human raw-shot approval is required");
    for (const field of QC_FIELDS) assert.equal(spec.rawHeroQc[field], "PASS", `coherent shot: ${field} must PASS before integration`);
  }
  if (QC_FIELDS.some((field) => spec.rawHeroQc?.[field] === "FAIL")) {
    assert.notEqual(spec.rawHeroQc.humanDecision, "approved", "coherent shot: failed hero intent cannot be approved");
  }
  assert.equal(spec.paidExecution?.requiresFreshApproval, true, "coherent shot: paid execution requires fresh approval");
  assert.equal(spec.distribution?.publishAllowed, false, "coherent shot: publishing must stay locked");
  assert.equal(spec.distribution?.activateAdsAllowed, false, "coherent shot: ad activation must stay locked");

  if (specPath) {
    const baseDir = path.dirname(path.resolve(specPath));
    for (const reference of spec.referencePack) {
      assert.equal(path.isAbsolute(reference.path), false, `coherent shot: reference path must be relative: ${reference.path}`);
      const resolved = path.resolve(baseDir, reference.path);
      assert.ok(resolved.startsWith(`${baseDir}${path.sep}`), `coherent shot: reference escapes its directory: ${reference.path}`);
      assert.equal(existsSync(resolved), true, `coherent shot: reference does not exist: ${reference.path}`);
    }
    assert.equal(path.isAbsolute(spec.humanAnimatic.path), false, `coherent shot: Animatic path must be relative: ${spec.humanAnimatic.path}`);
    const explorationRoot = path.dirname(baseDir);
    const animaticPath = path.resolve(baseDir, spec.humanAnimatic.path);
    assert.ok(animaticPath.startsWith(`${explorationRoot}${path.sep}`), `coherent shot: Animatic escapes the exploration directory: ${spec.humanAnimatic.path}`);
    assert.equal(existsSync(animaticPath), true, `coherent shot: Animatic does not exist: ${spec.humanAnimatic.path}`);
  }
  return { references: roles.length, causalSteps: spec.causalArc.length, rawDecision: spec.rawHeroQc.humanDecision };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-coherent-shot.mjs <hero-shot-spec.json> [--require-raw-approved]");
  const result = validateCoherentShot(JSON.parse(await readFile(file, "utf8")), { specPath: file, requireRawApproval: process.argv.includes("--require-raw-approved") });
  console.log(`Coherent shot: PASS (${result.causalSteps} causal steps / ${result.references} references / raw=${result.rawDecision})`);
}
