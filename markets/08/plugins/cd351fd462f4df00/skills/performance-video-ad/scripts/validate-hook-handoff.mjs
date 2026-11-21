#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

export function validateHookHandoff(contract) {
  assert.equal(contract.schemaVersion, 1, "Hook handoff: unsupported schemaVersion");
  assert.equal(contract.handoffContractVersion, 1, "Hook handoff: unsupported contract version");
  assert.ok(contract.jobId, "Hook handoff: jobId missing");
  assert.ok(["DRAFT", "READY_FOR_HUMAN_REVIEW", "LOCKED"].includes(contract.status), "Hook handoff: invalid status");
  assert.ok(["CONTROLLED_BATCH", "SINGLE_MASTER_EXPLORATION"].includes(contract.scope), "Hook handoff: invalid scope");
  assert.ok(Number.isFinite(contract.common_core_start_seconds) && contract.common_core_start_seconds > 0, "Hook handoff: common core start must be positive");
  assert.ok(Array.isArray(contract.entries), "Hook handoff: entries must be an array");
  if (contract.status !== "DRAFT") assert.ok(contract.entries.length > 0, "Hook handoff: reviewable contract requires entries");
  const ids = new Set();
  for (const entry of contract.entries) {
    assert.ok(entry.hook_id && !ids.has(entry.hook_id), `Hook handoff: duplicate or missing hook_id ${entry.hook_id ?? "<missing>"}`);
    ids.add(entry.hook_id);
    assert.ok(Number.isFinite(entry.hook_end_seconds) && Number.isFinite(entry.handoff_end_seconds), `Hook handoff ${entry.hook_id}: timing missing`);
    assert.ok(entry.handoff_end_seconds > entry.hook_end_seconds, `Hook handoff ${entry.hook_id}: handoff must follow Hook`);
    assert.equal(entry.handoff_end_seconds, contract.common_core_start_seconds, `Hook handoff ${entry.hook_id}: handoff must end at the common-core boundary`);
    for (const field of ["emotional_state", "question_to_carry", "common_core_entry_state"]) {
      assert.ok(typeof entry[field] === "string" && entry[field].trim(), `Hook handoff ${entry.hook_id}: ${field} missing`);
    }
    assert.ok(Array.isArray(entry.handoff_lines) && entry.handoff_lines.length > 0, `Hook handoff ${entry.hook_id}: handoff lines missing`);
    assert.ok(Array.isArray(entry.source_refs) && entry.source_refs.length > 0, `Hook handoff ${entry.hook_id}: source refs missing`);
  }
  return { entries: contract.entries.length, commonCoreStart: contract.common_core_start_seconds };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-hook-handoff.mjs <hook-handoff.json>");
  const result = validateHookHandoff(JSON.parse(await readFile(file, "utf8")));
  console.log(`Hook handoff: PASS (${result.entries} entries / common core ${result.commonCoreStart}s)`);
}
