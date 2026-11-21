#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const sha256Pattern = /^[a-f0-9]{64}$/;
const checkNames = ["treatmentLineage", "geometryOwnership", "relativeMotion", "perspective", "occlusion", "lookMatching", "readability", "fallbackReady"];
const checkStatuses = ["NOT_RUN", "PASS", "FAIL", "NOT_APPLICABLE"];
const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;

export function validateCompositingFeasibility(treatment, gate, { requireReady = false } = {}) {
  assert.equal(gate.schemaVersion, 1, "compositing feasibility: schemaVersion must be 1");
  assert.equal(gate.contractVersion, 1, "compositing feasibility: contractVersion must be 1");
  assert.equal(gate.contractType, "performance_video_compositing_feasibility", "compositing feasibility: contractType is invalid");
  assert.ok(nonEmpty(gate.jobId) && gate.jobId === treatment.jobId, "compositing feasibility: jobId must match the treatment");
  assert.ok(["DRAFT", "PROOF_READY", "PASS", "FAIL"].includes(gate.status), "compositing feasibility: status is invalid");
  assert.equal(gate.paidExecutionAllowed, false, "preproduction feasibility cannot authorize paid execution");
  assert.equal(gate.distribution?.publishAllowed, false, "compositing feasibility cannot authorize publishing");
  assert.equal(gate.distribution?.activateAdsAllowed, false, "compositing feasibility cannot authorize ad activation");

  const selectedId = treatment.approval?.selectedTreatmentId;
  const selected = treatment.treatments?.find((candidate) => candidate.treatmentId === selectedId);
  if (gate.status !== "DRAFT" || requireReady) {
    assert.equal(treatment.status, "APPROVED_FOR_FEASIBILITY", "compositing feasibility requires an approved treatment");
    assert.equal(treatment.approval?.decision, "approved", "compositing feasibility requires treatment approval");
    assert.ok(selected, "compositing feasibility: selected treatment does not exist");
    assert.equal(gate.selectedTreatmentId, selectedId, "compositing feasibility: selectedTreatmentId mismatch");
    assert.ok(nonEmpty(gate.treatmentContract?.path), "compositing feasibility: treatment path is required");
    assert.match(gate.treatmentContract?.sha256 ?? "", sha256Pattern, "compositing feasibility: treatment SHA-256 is invalid");
  }

  const proof = gate.proof;
  assert.ok(["styleframe_only", "moving_binding_proof"].includes(proof?.proofType), "compositing feasibility: proofType is invalid");
  assert.ok(Number.isInteger(proof?.frameCount) && proof.frameCount >= 1, "compositing feasibility: proof frameCount is invalid");
  assert.ok(Number(proof?.durationSeconds) >= 0, "compositing feasibility: proof durationSeconds is invalid");
  assert.ok(Array.isArray(proof?.finalFidelityElements), "compositing feasibility: finalFidelityElements must be an array");
  const movingRequired = treatment.riskProfile?.movingProofRequired === true;
  if (movingRequired && gate.status !== "DRAFT") {
    assert.equal(proof.proofType, "moving_binding_proof", "compositing feasibility: the selected risk profile requires a moving binding proof");
    assert.ok(proof.frameCount >= 12 || proof.durationSeconds >= 0.5, "compositing feasibility: moving proof must contain at least 12 frames or 0.5 seconds");
  }

  const semanticObjects = selected?.semanticCarrierObjects ?? [];
  const semanticSurfaceObjects = semanticObjects.filter((object) => object.semanticSurfaceLoad !== "none");
  const resultById = new Map();
  assert.ok(Array.isArray(gate.surfaceResults), "compositing feasibility: surfaceResults must be an array");
  for (const result of gate.surfaceResults) {
    assert.ok(nonEmpty(result.objectId), "compositing feasibility: surface result objectId is required");
    assert.equal(resultById.has(result.objectId), false, `compositing feasibility: duplicate surface result ${result.objectId}`);
    resultById.set(result.objectId, result);
    const source = semanticObjects.find((object) => object.objectId === result.objectId);
    assert.ok(source, `compositing feasibility: unknown surface object ${result.objectId}`);
    assert.equal(result.bindingMode, source.bindingMode, `compositing feasibility: bindingMode mismatch for ${result.objectId}`);
    for (const key of ["trackability", "relativeMotion", "perspective", "occlusion", "lookMatching", "readability"]) {
      assert.ok(checkStatuses.includes(result[key]), `compositing feasibility: ${result.objectId}.${key} is invalid`);
    }
    assert.ok(Array.isArray(result.evidenceRefs) && result.evidenceRefs.length > 0, `compositing feasibility: ${result.objectId} requires evidence refs`);
    if (source.worldRelation === "world_bound") {
      for (const key of ["relativeMotion", "perspective", "lookMatching", "readability"]) assert.equal(result[key], "PASS", `compositing feasibility: world-bound ${result.objectId} requires ${key} PASS`);
      if (["planar_track", "corner_pin"].includes(source.bindingMode)) assert.equal(result.trackability, "PASS", `compositing feasibility: ${result.objectId} requires trackability PASS`);
    }
    if (source.worldRelation === "screen_native") {
      assert.equal(result.relativeMotion, "NOT_APPLICABLE", `compositing feasibility: screen-native ${result.objectId} relativeMotion must be NOT_APPLICABLE`);
      assert.equal(result.perspective, "NOT_APPLICABLE", `compositing feasibility: screen-native ${result.objectId} perspective must be NOT_APPLICABLE`);
      assert.equal(result.readability, "PASS", `compositing feasibility: screen-native ${result.objectId} requires readability PASS`);
    }
  }
  if (gate.status !== "DRAFT" || requireReady) {
    for (const object of semanticSurfaceObjects) assert.ok(resultById.has(object.objectId), `compositing feasibility: missing surface result for ${object.objectId}`);
  }

  const machineStatuses = [];
  for (const name of checkNames) {
    const check = gate.machineChecks?.[name];
    assert.ok(checkStatuses.includes(check?.status), `compositing feasibility: machineChecks.${name}.status is invalid`);
    assert.ok(Array.isArray(check?.evidenceRefs), `compositing feasibility: machineChecks.${name}.evidenceRefs must be an array`);
    if (["PASS", "FAIL"].includes(check.status)) assert.ok(check.evidenceRefs.length > 0, `compositing feasibility: machineChecks.${name} requires evidence`);
    machineStatuses.push(check.status);
  }
  const derivedMachineStatus = machineStatuses.includes("FAIL") ? "FAIL" : machineStatuses.every((status) => ["PASS", "NOT_APPLICABLE"].includes(status)) ? "PASS" : "PENDING";
  assert.equal(gate.machineGate?.status, derivedMachineStatus, "compositing feasibility: machineGate status must be derived from checks");

  const humanRequired = movingRequired;
  assert.equal(gate.humanTaste?.required, humanRequired, "compositing feasibility: human Taste requirement must be risk-derived");
  assert.ok(["NOT_REQUIRED", "PENDING", "APPROVED", "REJECTED"].includes(gate.humanTaste?.status), "compositing feasibility: human Taste status is invalid");
  if (humanRequired && gate.humanTaste?.status === "APPROVED") {
    assert.ok(nonEmpty(gate.humanTaste.reviewedBy) && nonEmpty(gate.humanTaste.reviewedAt), "compositing feasibility: approved human Taste requires evidence");
  }
  if (!humanRequired) assert.equal(gate.humanTaste?.status, "NOT_REQUIRED", "compositing feasibility: low-risk treatment must mark human Taste NOT_REQUIRED");

  if (gate.status === "PASS") {
    assert.equal(gate.diagnosticOnly, false, "compositing feasibility: diagnostic-only proof cannot claim PASS");
    assert.equal(gate.machineGate.status, "PASS", "compositing feasibility: PASS status requires machine PASS");
    if (humanRequired) assert.equal(gate.humanTaste.status, "APPROVED", "compositing feasibility: PASS status requires approved human Taste");
    assert.ok(nonEmpty(proof.path), "compositing feasibility: PASS status requires a proof path");
    assert.match(proof.sha256 ?? "", sha256Pattern, "compositing feasibility: PASS status requires a valid proof SHA-256");
    assert.ok(proof.finalFidelityElements.length > 0, "compositing feasibility: PASS status requires named final-fidelity elements");
  }
  if (gate.status === "FAIL") assert.equal(gate.machineGate.status === "FAIL" || gate.humanTaste.status === "REJECTED", true, "compositing feasibility: FAIL status requires failed machine evidence or rejected human Taste");

  if (requireReady) {
    assert.equal(gate.diagnosticOnly, false, "compositing feasibility: diagnostic-only proof cannot unlock production");
    assert.equal(gate.status, "PASS", "compositing feasibility: status must be PASS");
    assert.equal(gate.machineGate.status, "PASS", "compositing feasibility: machine gate must PASS");
    if (humanRequired) assert.equal(gate.humanTaste.status, "APPROVED", "compositing feasibility: required human Taste must be approved");
    assert.ok(nonEmpty(proof.path), "compositing feasibility: proof path is required");
    assert.match(proof.sha256 ?? "", sha256Pattern, "compositing feasibility: proof SHA-256 is invalid");
    assert.ok(proof.finalFidelityElements.length > 0, "compositing feasibility: proof must name its final-fidelity elements");
  }
  return gate;
}

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const treatmentPath = process.argv[2];
  const gatePath = process.argv[3];
  assert.ok(treatmentPath && gatePath, "Usage: validate-compositing-feasibility.mjs <visual-treatment-contract.json> <compositing-feasibility-gate.json> [--require-ready]");
  const treatment = JSON.parse(readFileSync(treatmentPath, "utf8"));
  const gate = JSON.parse(readFileSync(gatePath, "utf8"));
  validateCompositingFeasibility(treatment, gate, { requireReady: process.argv.includes("--require-ready") });
  console.log(`compositing feasibility: PASS (${gate.jobId})`);
}
