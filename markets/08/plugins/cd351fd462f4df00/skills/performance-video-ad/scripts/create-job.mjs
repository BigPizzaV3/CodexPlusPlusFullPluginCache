#!/usr/bin/env node
import assert from "node:assert/strict";
import { access, mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const skillDir = path.resolve(scriptDir, "..");
const args = process.argv.slice(2);
const jobId = args[0];
const outIndex = args.indexOf("--out");
const outRoot = outIndex >= 0 ? args[outIndex + 1] : null;
const modeIndex = args.indexOf("--mode");
const mode = modeIndex >= 0 ? args[modeIndex + 1] : "one-shot";

assert.ok(jobId && /^[a-z0-9][a-z0-9-]{2,63}$/.test(jobId), "job-id must use 3-64 lowercase letters, digits, and hyphens");
assert.ok(outRoot, "Usage: node scripts/create-job.mjs <job-id> --out <jobs-root> [--mode one-shot|controlled]");
assert.ok(["one-shot", "controlled"].includes(mode), "--mode must be one-shot or controlled");

const jobDir = path.resolve(outRoot, jobId);
try {
  await access(jobDir);
  throw new Error("Refusing to overwrite existing job: " + jobDir);
} catch (error) {
  if (error.code !== "ENOENT") throw error;
}

const commonDirectories = ["inputs", "generated", "final", "logs", "qc"];
const controlledDirectories = ["explorations", "remotion"];
const directories = mode === "controlled" ? [...commonDirectories, ...controlledDirectories] : commonDirectories;
await Promise.all(directories.map((directory) => mkdir(path.join(jobDir, directory), { recursive: true })));

const commonTemplates = [
  "offer-context.json",
  "source-manifest.json",
  "source-coverage-report.json",
  "insight-evidence-map.json",
  "sales-thesis.json",
  "concept-candidates.json",
  "destination-contract.json",
  "context-resolution.json",
  "funnel-role-contract.json",
  "cost-estimate.json",
  "approval.json"
];

const oneShotTemplates = [
  "one-shot-brief.json",
  "integrated-generation-prompt.md"
];

const controlledTemplates = [
  "creative-premise.json",
  "felt-brief.json",
  "creative-tension-map.json",
  "creative-territories.json",
  "first-frame-board.json",
  "three-second-hook-loops.json",
  "intended-reaction-map.json",
  "taste-review.json",
  "message-inheritance-contract.json",
  "copy-lineage.json",
  "strategy-snapshot.json",
  "creative-context.json",
  "expression-policy.json",
  "creative-brief.json",
  "test-batch.json",
  "incidents.json",
  "creative-hypotheses.json",
  "hook-packages.json",
  "body-contract.json",
  "body-family.json",
  "hook-portfolio-approval.json",
  "hook-handoff.json",
  "insight-render-map.json",
  "pacing-review.json",
  "ai-led-run.json",
  "first-pass-baseline.json",
  "beat-sheet.json",
  "sound-intent-map.json",
  "animatic-review.json",
  "visual-treatment-contract.json",
  "shot-dependency-graph.json",
  "shot-manifest.json",
  "route-plan.json"
];

const templates = mode === "controlled"
  ? [...commonTemplates, ...controlledTemplates]
  : [...commonTemplates, ...oneShotTemplates];

for (const template of templates) {
  const source = await readFile(path.join(skillDir, "assets/templates", template), "utf8");
  await writeFile(path.join(jobDir, template), source.replaceAll("__JOB_ID__", jobId), "utf8");
}

const productionSkillDir = path.resolve(skillDir, "../performance-video-production");
if (mode === "one-shot") {
  const reviewTemplate = await readFile(path.join(productionSkillDir, "assets/templates/one-shot-review.json"), "utf8");
  await writeFile(path.join(jobDir, "one-shot-review.json"), reviewTemplate.replaceAll("__JOB_ID__", jobId), "utf8");
} else {
  const productionTemplates = [
    ["timeline-audio-contract.json", "timeline-audio-contract.json"],
    ["compositing-feasibility-gate.json", "compositing-feasibility-gate.json"],
    ["production-handoff.json", "production-handoff.json"]
  ];
  for (const [template, output] of productionTemplates) {
    const source = await readFile(path.join(productionSkillDir, "assets/templates", template), "utf8");
    await writeFile(path.join(jobDir, output), source.replaceAll("__JOB_ID__", jobId), "utf8");
  }
}

console.log("Created performance-video-ad " + mode + " job: " + jobDir);
if (mode === "one-shot") {
  console.log("Next: resolve sources internally, lock one Sales Thesis, persist and validate concept-candidates.json, promote only the selected concept to one-shot-brief.json, and stop only for current paid approval.");
} else {
  console.log("Next: run the controlled fallback gates justified by the named exactness or continuity risk.");
}
