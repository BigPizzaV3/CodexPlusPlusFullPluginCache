#!/usr/bin/env node
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateVisualTreatmentContract } from "../../performance-video-ad/scripts/validate-visual-treatment-contract.mjs";
import { validateCompositingFeasibility } from "./validate-compositing-feasibility.mjs";
import { validateProductionHandoff } from "./validate-production-handoff.mjs";

const sha256 = (buffer) => createHash("sha256").update(buffer).digest("hex");

function readLockedArtifact(jobDir, reference, label) {
  assert.ok(reference && typeof reference.path === "string" && reference.path.length > 0, `${label} path is required`);
  assert.equal(path.isAbsolute(reference.path), false, `${label} path must be relative to the job directory`);
  const resolved = path.resolve(jobDir, reference.path);
  assert.ok(resolved.startsWith(`${jobDir}${path.sep}`), `${label} path escapes the job directory`);
  const buffer = readFileSync(resolved);
  assert.equal(sha256(buffer), reference.sha256, `${label} SHA-256 does not match the locked artifact`);
  return { resolved, buffer };
}

export function validateProductionEntry(jobDirectory) {
  const jobDir = path.resolve(jobDirectory);
  const handoff = JSON.parse(readFileSync(path.join(jobDir, "production-handoff.json"), "utf8"));
  validateProductionHandoff(handoff);
  assert.equal(path.basename(jobDir), handoff.jobId, "production entry: job directory basename must match jobId");
  assert.equal(handoff.lineage?.jobDirectoryId, handoff.jobId, "production entry: lineage must match jobId");

  const treatmentArtifact = readLockedArtifact(jobDir, handoff.approvedArtifacts.visualTreatment, "Visual Treatment");
  const feasibilityArtifact = readLockedArtifact(jobDir, handoff.approvedArtifacts.compositingFeasibility, "compositing feasibility");
  readLockedArtifact(jobDir, handoff.approvedArtifacts.animaticReview, "Animatic review");
  readLockedArtifact(jobDir, handoff.approvedArtifacts.timelineAudioIntent, "timeline/audio contract");

  const treatment = JSON.parse(treatmentArtifact.buffer.toString("utf8"));
  const gate = JSON.parse(feasibilityArtifact.buffer.toString("utf8"));
  validateVisualTreatmentContract(treatment, { requireSelected: true });
  validateCompositingFeasibility(treatment, gate, { requireReady: true });
  assert.equal(treatment.jobId, handoff.jobId, "production entry: Treatment jobId mismatch");
  assert.equal(gate.jobId, handoff.jobId, "production entry: feasibility jobId mismatch");
  assert.equal(gate.treatmentContract.path, handoff.approvedArtifacts.visualTreatment.path, "production entry: feasibility treatment path mismatch");
  assert.equal(gate.treatmentContract.sha256, handoff.approvedArtifacts.visualTreatment.sha256, "production entry: feasibility treatment hash mismatch");
  readLockedArtifact(jobDir, gate.proof, "composite proof");
  return { handoff, treatment, gate };
}

const isCli = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCli) {
  const jobDir = process.argv[2];
  assert.ok(jobDir, "Usage: validate-production-entry.mjs <job-dir>");
  const { handoff } = validateProductionEntry(jobDir);
  console.log(`production entry: PASS (${handoff.jobId})`);
}
