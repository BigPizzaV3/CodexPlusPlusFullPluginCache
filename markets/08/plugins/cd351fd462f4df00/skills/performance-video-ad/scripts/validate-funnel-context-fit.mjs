#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateContextResolution } from "./validate-context-resolution.mjs";
import { validateFunnelRoleContract } from "./validate-funnel-role-contract.mjs";

const objectValue = (value, key) => value && typeof value === "object" ? value[key] : value;
const sorted = (value) => [...value].sort();

export function validateFunnelContextFit(context, contract) {
  validateContextResolution(context, { requireReady: true });
  validateFunnelRoleContract(contract, { requireResolved: true });
  assert.equal(context.jobId, contract.jobId, "funnel context fit: jobId mismatch");
  const fields = new Map(context.field_resolutions.map((field) => [field.field_id, field.value]));
  assert.equal(fields.get("traffic_temperature"), contract.traffic_temperature, "funnel context fit: traffic temperature drift");
  assert.equal(fields.get("awareness_stage"), contract.awareness_stage, "funnel context fit: awareness stage drift");
  assert.equal(fields.get("funnel_stage"), contract.funnel_stage, "funnel context fit: funnel stage drift");
  assert.equal(objectValue(fields.get("next_destination"), "ref"), contract.next_destination.ref, "funnel context fit: destination drift");
  assert.equal(objectValue(fields.get("primary_conversion"), "type"), contract.primary_conversion.type, "funnel context fit: primary conversion drift");
  assert.equal(objectValue(fields.get("final_conversion"), "type"), contract.final_conversion.type, "funnel context fit: final conversion drift");
  assert.ok(Array.isArray(fields.get("ad_primary_job")), "funnel context fit: ad_primary_job must resolve to an array");
  assert.deepEqual(sorted(fields.get("ad_primary_job")), sorted(contract.stage_role.primary_jobs), "funnel context fit: ad primary job drift");
  assert.equal(fields.get("ad_cta_action"), contract.ad_cta_action, "funnel context fit: CTA action drift");
  return { stage: contract.funnel_stage, primaryJobs: contract.stage_role.primary_jobs.length };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const [contextFile, contractFile] = process.argv.slice(2).map((file) => path.resolve(file));
  assert.ok(contextFile && contractFile, "Usage: node scripts/validate-funnel-context-fit.mjs <context-resolution.json> <funnel-role-contract.json>");
  const [context, contract] = await Promise.all([contextFile, contractFile].map((file) => readFile(file, "utf8").then(JSON.parse)));
  const result = validateFunnelContextFit(context, contract);
  console.log(`Funnel context fit: PASS (${result.stage}; ${result.primaryJobs} primary jobs)`);
}
