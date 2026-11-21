#!/usr/bin/env node
import assert from "node:assert/strict";
import { File } from "node:buffer";
import { createHash } from "node:crypto";
import { lstat, mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { resolveFalCredential } from "./fal-credential-resolver.mjs";
import { assertAnimaticApproved } from "./validate-animatic-gate.mjs";
import { validateShotDependencyGraph } from "./validate-shot-dependency-graph.mjs";

const args = process.argv.slice(2);
const valueFor = (flag) => {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : null;
};
const jobDir = valueFor("--job-dir") ? path.resolve(valueFor("--job-dir")) : null;
const shotId = valueFor("--shot");
const execute = args.includes("--execute");
const runContextPath = valueFor("--run-context");
assert.ok(jobDir && shotId, "Usage: node scripts/fal-generation-adapter.mjs --job-dir <path> --shot <shot-id> [--execute]");

const readJson = async (name) => JSON.parse(await readFile(path.join(jobDir, name), "utf8"));
const [approval, cost, shotManifest, routePlan, animaticReview, portfolio, bodyFamily] = await Promise.all([
  readJson("approval.json"),
  readJson("cost-estimate.json"),
  readJson("shot-manifest.json"),
  readJson("route-plan.json"),
  readJson("animatic-review.json"),
  readJson("hook-packages.json"),
  readJson("body-family.json"),
]);
const shot = shotManifest.shots.find((item) => item.id === shotId);
const shotRoute = routePlan.routes.find((item) => item.shotId === shotId);
const candidate = shotRoute?.candidates?.find((item) => item.provider === "fal" && item.selected === true)
  ?? shotRoute?.candidates?.find((item) => item.provider === "fal");
assert.ok(shot, `Shot not found: ${shotId}`);
assert.ok(candidate, `fal route not found: ${shotId}`);
assert.match(candidate.endpoint ?? "", /^fal-ai\/[a-zA-Z0-9._\/-]+$/, "fal endpoint must start with fal-ai/");
assert.ok(candidate.providerInput && typeof candidate.providerInput === "object", "route candidate.providerInput is required");
assert.ok(candidate.outputUrlPath, "route candidate.outputUrlPath is required (example: video.url)");
const prompt = shot.prompt ?? shot.creativePrompt;
assert.ok(prompt, `Shot ${shotId} requires prompt or creativePrompt`);

const tokenValues = {
  "{{prompt}}": prompt,
  "{{durationSeconds}}": shot.durationSeconds ?? shot.duration,
  "{{uploadedInputUrl}}": "<uploaded-after-approval>",
};
const replaceTokens = (value, replacements) => {
  if (Array.isArray(value)) return value.map((item) => replaceTokens(item, replacements));
  if (value && typeof value === "object") {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, replaceTokens(item, replacements)]));
  }
  if (typeof value === "string" && Object.hasOwn(replacements, value)) return replacements[value];
  return value;
};
const sanitizedInput = replaceTokens(candidate.providerInput, tokenValues);
const localOutputName = shot.outputName ?? `${shot.id}.mp4`;
assert.equal(path.basename(localOutputName), localOutputName, "shot.outputName must be a filename, not a path");

const dryRun = {
  mode: execute ? "EXECUTE_REQUESTED" : "DRY_RUN",
  jobId: approval.jobId,
  shotId,
  endpoint: candidate.endpoint,
  modelProfileId: candidate.modelProfileId ?? null,
  providerInput: sanitizedInput,
  estimatedCostUsd: cost.estimatedCostUsd,
  approvedMaximumUsd: approval.maximumApprovedCostUsd,
  maximumAttempts: shot.maximumAttempts,
  localOutputPath: `generated/${localOutputName}`,
};
if (!execute) {
  console.log(JSON.stringify(dryRun, null, 2));
  console.log("No upload or provider request was submitted.");
  process.exit(0);
}

assertAnimaticApproved(animaticReview, portfolio, bodyFamily, jobDir);
const dependencyGraph = await readJson("shot-dependency-graph.json");
validateShotDependencyGraph(dependencyGraph, { targetShotId: shot.id, requirePaidReady: true });
assert.equal(cost.jobId, approval.jobId, "cost/approval jobId mismatch");
assert.equal(cost.withinBudget, true, "Paid execution blocked: estimate exceeds job limit");
assert.equal(cost.requiresRecheckAtExecution, false, "Paid execution blocked: pricing must be rechecked");
assert.equal(approval.decision, "approved", "Paid execution blocked: approval is not approved");
assert.equal(approval.paidRunAllowed, true, "Paid execution blocked: paidRunAllowed is false");
assert.ok(cost.estimatedCostUsd <= approval.maximumApprovedCostUsd, "Paid execution blocked: approved budget exceeded");
assert.equal(approval.maximumAttempts, 1, "Exploration gate requires exactly one approved attempt");
assert.equal(shot.maximumAttempts, 1, "Exploration gate requires exactly one shot attempt");
const credential = resolveFalCredential();
assert.ok(credential, "Paid execution blocked: fal credential is missing from the environment and macOS Keychain");

// Run execution is additionally fenced by the approved scope and budget ledger.
// All original animatic, dependency, human cost and attempt gates above still apply.
if (runContextPath) {
  assert.match(shotId, /^[A-Za-z0-9][A-Za-z0-9_-]{0,79}$/, "run shot ID must be a safe journal key");
  const { runFal, falTransport } = await import("../../marketing-omakase/scripts/fal-run-adapter.mjs");
  const { payloadHash } = await import("../../marketing-omakase/scripts/run-contract.mjs");
  const { qualityClientFromEnvironment } = await import("../../marketing-omakase/scripts/quality-client.mjs");
  const contextFile = path.resolve(runContextPath);
  const contextStat = await lstat(contextFile);
  assert.ok(contextStat.isFile() && !contextStat.isSymbolicLink() && (contextStat.mode & 0o077) === 0, "run context must be a private regular file (0600)");
  const run = JSON.parse(await readFile(contextFile, "utf8"));
  assert.ok(!JSON.stringify(sanitizedInput).includes("<uploaded-after-approval>"), "Run path requires an already approved provider input URL; upload is a separate scoped operation");
  assert.equal(run.request.model, candidate.endpoint, "run model differs from selected route");
  assert.equal(run.request.payloadHash, payloadHash(sanitizedInput), "run payload differs from approved provider input");
  const outcome = await runFal({
    journalPath: path.join(jobDir, `marketing-run.${shotId}.json`),
    projectId: run.projectId, context: run.context,
    request: { ...run.request, payload: sanitizedInput },
    callQuality: qualityClientFromEnvironment(), transport: falTransport({ credential: credential.value }), dryRun: false,
  });
  // A single invocation does one status check. Resume the same command / request ID.
  console.log(JSON.stringify({ status: outcome.status, requestId: outcome.requestId, spendId: outcome.spendId }));
  if (outcome.status !== "completed") process.exit(0);
  const outputUrl = candidate.outputUrlPath.split(".").reduce((value, key) => value?.[key], outcome.result);
  assert.ok(outputUrl, `fal result missing ${candidate.outputUrlPath}`);
  const parsed = new URL(outputUrl);
  assert.equal(parsed.protocol, "https:", "provider result must use HTTPS");
  const response = await fetch(outputUrl, { redirect: "error", signal: AbortSignal.timeout(60_000) });
  assert.ok(response.ok, `fal result download failed: HTTP ${response.status}`);
  const outputBytes = Buffer.from(await response.arrayBuffer());
  await mkdir(path.join(jobDir, "generated"), { recursive: true });
  await writeFile(path.join(jobDir, "generated", localOutputName), outputBytes);
  await writeFile(path.join(jobDir, `job-manifest.${shotId}.json`), JSON.stringify({
    schemaVersion: 1, jobId: approval.jobId, shotId, status: "GENERATED_PENDING_QC",
    distributionStatus: "LOCAL_QC_ONLY", publishAllowed: false, provider: "fal", endpoint: candidate.endpoint,
    modelProfileId: candidate.modelProfileId ?? null, requestId: outcome.requestId,
    spendId: outcome.spendId, runId: run.context.runId, scopeRevision: run.context.scopeRevision,
    localOutputPath: `generated/${localOutputName}`, outputSha256: createHash("sha256").update(outputBytes).digest("hex"),
    actualCostUsd: null, retryCount: 0, technicalQc: "PENDING", creativeQc: "PENDING",
  }, null, 2));
  process.exit(0);
}

let uploadedInputUrl = null;
let inputHash = null;
let clientPackage;
try {
  clientPackage = await import("@fal-ai/client");
} catch {
  throw new Error("@fal-ai/client is not available in this project. Install it only in the approved execution environment.");
}
const { fal } = clientPackage;
fal.config({ credentials: credential.value });
if (JSON.stringify(candidate.providerInput).includes("{{uploadedInputUrl}}")) {
  assert.ok(shot.inputPath, "shot.inputPath is required by providerInput");
  assert.equal(path.isAbsolute(shot.inputPath), false, "shot.inputPath must be relative to the job directory");
  const inputPath = path.resolve(jobDir, shot.inputPath);
  assert.ok(inputPath.startsWith(`${jobDir}${path.sep}`), "shot.inputPath escapes the job directory");
  const inputBytes = await readFile(inputPath);
  inputHash = createHash("sha256").update(inputBytes).digest("hex");
  uploadedInputUrl = await fal.storage.upload(new File([inputBytes], path.basename(inputPath), {
    type: shot.inputMimeType ?? "application/octet-stream",
  }));
}
const providerInput = replaceTokens(candidate.providerInput, {
  "{{prompt}}": prompt,
  "{{durationSeconds}}": shot.durationSeconds ?? shot.duration,
  "{{uploadedInputUrl}}": uploadedInputUrl,
});
const submittedAt = new Date().toISOString();
const submission = await fal.queue.submit(candidate.endpoint, { input: providerInput });
const requestId = submission.request_id;
assert.ok(requestId, "fal submission returned no request ID");

const pollIntervalMs = Math.max(1000, candidate.pollIntervalMs ?? 3000);
const timeoutMs = Math.min(30 * 60_000, Math.max(30_000, candidate.timeoutMs ?? 15 * 60_000));
const deadline = Date.now() + timeoutMs;
let providerStatus = await fal.queue.status(candidate.endpoint, { requestId, logs: false });
while (["IN_QUEUE", "IN_PROGRESS"].includes(providerStatus.status)) {
  assert.ok(Date.now() < deadline, `fal request timed out after ${timeoutMs}ms`);
  await new Promise((resolve) => setTimeout(resolve, pollIntervalMs));
  providerStatus = await fal.queue.status(candidate.endpoint, { requestId, logs: false });
}
assert.equal(providerStatus.status, "COMPLETED", `fal request failed: ${providerStatus.status}`);
const result = await fal.queue.result(candidate.endpoint, { requestId });
const outputUrl = candidate.outputUrlPath.split(".").reduce((value, key) => value?.[key], result.data);
assert.ok(outputUrl, `fal result missing ${candidate.outputUrlPath}`);
const response = await fetch(outputUrl);
assert.ok(response.ok, `fal result download failed: HTTP ${response.status}`);
const outputBytes = Buffer.from(await response.arrayBuffer());
const generatedDir = path.join(jobDir, "generated");
await mkdir(generatedDir, { recursive: true });
const localOutputPath = path.join(generatedDir, localOutputName);
await writeFile(localOutputPath, outputBytes);

let redactedOutputUrl = null;
try {
  const parsed = new URL(outputUrl);
  redactedOutputUrl = `${parsed.origin}${parsed.pathname}`;
} catch {
  redactedOutputUrl = "<provider-output-url-redacted>";
}
const manifest = {
  schemaVersion: 1,
  jobId: approval.jobId,
  status: "GENERATED_PENDING_QC",
  distributionStatus: "LOCAL_QC_ONLY",
  publishAllowed: false,
  shotId,
  provider: "fal",
  endpoint: candidate.endpoint,
  modelProfileId: candidate.modelProfileId ?? null,
  adapterVersion: "performance-video-ad-v1",
  promptHash: createHash("sha256").update(prompt).digest("hex"),
  inputFileHash: inputHash,
  requestId,
  submittedAt,
  completedAt: new Date().toISOString(),
  estimatedCostUsd: cost.estimatedCostUsd,
  actualCostUsd: null,
  retryCount: 0,
  providerOutputUrlWithoutQuery: redactedOutputUrl,
  localOutputPath: path.relative(jobDir, localOutputPath),
  outputSha256: createHash("sha256").update(outputBytes).digest("hex"),
  technicalQc: "PENDING",
  creativeQc: "PENDING",
};
await writeFile(path.join(jobDir, `job-manifest.${shotId}.json`), `${JSON.stringify(manifest, null, 2)}\n`, "utf8");
console.log(`Downloaded generated asset: ${path.relative(jobDir, localOutputPath)}`);
console.log("State: GENERATED_PENDING_QC / LOCAL_QC_ONLY. No publishing action was performed.");
