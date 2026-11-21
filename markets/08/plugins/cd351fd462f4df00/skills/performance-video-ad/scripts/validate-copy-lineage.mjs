#!/usr/bin/env node
import assert from "node:assert/strict";
import { realpathSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const DERIVATION_TYPES = new Set(["verbatim_quote", "paraphrase", "synthesized_copy", "creative_hypothesis"]);
const EVIDENCE_STRENGTHS = new Set(["source_direct", "multi_source_supported", "voc_supported_not_verbatim", "untested_creative_hypothesis"]);

function addStrings(target, value) {
  if (typeof value === "string" && value.trim()) target.add(value.trim());
  if (Array.isArray(value)) for (const item of value) addStrings(target, item);
}

export function collectViewerCopy(hookPackages = null, bodyContract = null) {
  const values = new Set();
  for (const item of hookPackages?.packages ?? []) {
    addStrings(values, item.hookCopy);
    addStrings(values, item.renderedCopySegments);
  }
  for (const module of bodyContract?.modules ?? []) {
    addStrings(values, module.spoken_copy);
    addStrings(values, module.screen?.ui_labels);
  }
  if (bodyContract?.cta) for (const value of Object.values(bodyContract.cta)) addStrings(values, value);
  return values;
}

export function validateCopyLineage(lineage, { knownSourceIds = null, hookPackages = null, bodyContract = null } = {}) {
  assert.equal(lineage.schemaVersion, 1, "copy lineage: unsupported schemaVersion");
  assert.equal(lineage.sourceAssemblyVersion, 1, "copy lineage: unsupported sourceAssemblyVersion");
  assert.ok(lineage.jobId && lineage.offerId, "copy lineage: jobId and offerId are required");
  assert.ok(["BLOCKED_BY_PREMISE_APPROVAL", "READY", "VERIFIED"].includes(lineage.status), "copy lineage: invalid status");
  assert.ok(Array.isArray(lineage.entries), "copy lineage: entries must be an array");
  if (lineage.status !== "BLOCKED_BY_PREMISE_APPROVAL") assert.ok(lineage.entries.length > 0, "copy lineage: READY/VERIFIED requires entries");

  const copyTexts = new Set();
  const copyIds = new Set();
  for (const entry of lineage.entries) {
    for (const field of ["copy_id", "location", "text", "derivation_type", "evidence_strength"]) assert.ok(typeof entry[field] === "string" && entry[field].trim(), `copy lineage entry: ${field} is required`);
    assert.ok(!copyIds.has(entry.copy_id), `copy lineage: duplicate copy_id ${entry.copy_id}`);
    assert.ok(DERIVATION_TYPES.has(entry.derivation_type), `copy lineage: invalid derivation_type for ${entry.copy_id}`);
    assert.ok(EVIDENCE_STRENGTHS.has(entry.evidence_strength), `copy lineage: invalid evidence_strength for ${entry.copy_id}`);
    assert.ok(Array.isArray(entry.source_refs) && entry.source_refs.length > 0, `copy lineage: ${entry.copy_id} requires source_refs`);
    if (knownSourceIds) for (const ref of entry.source_refs) assert.ok(knownSourceIds.has(String(ref).split("#", 1)[0]), `copy lineage: unknown source ref ${ref}`);
    if (entry.derivation_type === "verbatim_quote") assert.equal(entry.evidence_strength, "source_direct", `copy lineage: verbatim quote ${entry.copy_id} must be source_direct`);
    copyIds.add(entry.copy_id);
    copyTexts.add(entry.text.trim());
  }

  const viewerCopy = collectViewerCopy(hookPackages, bodyContract);
  for (const text of viewerCopy) assert.ok(copyTexts.has(text), `copy lineage: viewer-facing copy has no lineage: ${text}`);
  return lineage;
}

async function readOptional(file) {
  return file ? JSON.parse(await readFile(path.resolve(file), "utf8")) : null;
}

async function main() {
  const lineageFile = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(lineageFile, "Usage: node scripts/validate-copy-lineage.mjs <copy-lineage.json> [hook-packages.json] [body-contract.json]");
  const lineage = await readOptional(lineageFile);
  const hookPackages = await readOptional(process.argv[3]);
  const bodyContract = await readOptional(process.argv[4]);
  validateCopyLineage(lineage, { hookPackages, bodyContract });
  console.log(`Copy lineage: PASS (${lineage.entries.length} entries)`);
}

const isMain = (() => {
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); } catch { return false; }
})();

if (isMain) main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
