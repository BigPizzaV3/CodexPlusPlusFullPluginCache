#!/usr/bin/env node
import assert from "node:assert/strict";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";

const args = process.argv.slice(2);
const value = (flag) => {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : null;
};
const seconds = Number(value("--seconds"));
const price = Number(value("--price-per-second"));
const attempts = Number(value("--attempts") ?? 1);
const maximum = Number(value("--max"));
const pricingAsOf = value("--as-of");
const pricingSource = value("--source");
const jobId = value("--job") ?? "unassigned-job";
const outPath = value("--out") ? path.resolve(value("--out")) : null;

assert.ok(seconds > 0, "--seconds must be positive");
assert.ok(price > 0, "--price-per-second must be positive and current");
assert.ok(Number.isInteger(attempts) && attempts > 0, "--attempts must be a positive integer");
assert.ok(maximum > 0, "--max must be positive");
assert.ok(/^\d{4}-\d{2}-\d{2}$/.test(pricingAsOf ?? ""), "--as-of must be YYYY-MM-DD");
assert.ok(/^https:\/\//.test(pricingSource ?? ""), "--source must be an official HTTPS URL");
assert.ok(outPath, "--out is required");
const ageDays = (Date.now() - new Date(`${pricingAsOf}T00:00:00Z`).getTime()) / 86_400_000;
assert.ok(ageDays >= -1 && ageDays <= 30, `pricing snapshot is stale or future-dated: ${ageDays.toFixed(1)} days`);

const estimatedCostUsd = Number((seconds * price * attempts).toFixed(4));
const report = {
  schemaVersion: 1,
  jobId,
  status: estimatedCostUsd <= maximum ? "AWAITING_EXPLICIT_APPROVAL" : "BUDGET_EXCEEDED",
  durationSeconds: seconds,
  attempts,
  usdPerSecond: price,
  estimatedCostUsd,
  maximumCostUsd: maximum,
  withinBudget: estimatedCostUsd <= maximum,
  pricingAsOf,
  pricingSource,
  requiresRecheckAtExecution: true,
};
await mkdir(path.dirname(outPath), { recursive: true });
await writeFile(outPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
console.log(`Estimated cost: $${estimatedCostUsd.toFixed(4)} / max $${maximum.toFixed(4)} (${report.status})`);
if (!report.withinBudget) process.exitCode = 2;
