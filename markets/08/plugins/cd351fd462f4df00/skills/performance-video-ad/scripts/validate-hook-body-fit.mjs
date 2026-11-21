#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateBodyContract } from "./validate-body-contract.mjs";

const sorted = (values) => [...values].sort();

export function validateHookBodyFit(portfolio, contracts) {
  assert.equal(portfolio.bodyContractVersion, 1, "Hook/Body fit requires bodyContractVersion=1");
  const hookBodyReuseVersion = portfolio.hookBodyReuseVersion ?? 0;
  assert.ok([0, 1].includes(hookBodyReuseVersion), "unsupported hookBodyReuseVersion");
  assert.ok(Array.isArray(contracts) && contracts.length > 0, "At least one Body contract is required");
  const byId = new Map();
  for (const contract of contracts) {
    validateBodyContract(contract);
    if (hookBodyReuseVersion === 1) assert.equal(contract.hookBodyReuseVersion, 1, `Body ${contract.body_family_id}: hookBodyReuseVersion=1 is required`);
    assert.ok(!byId.has(contract.body_family_id), `Duplicate Body family: ${contract.body_family_id}`);
    byId.set(contract.body_family_id, contract);
  }

  const contractIds = sorted(byId.keys());
  assert.deepEqual(sorted(portfolio.bodyFamilyIds ?? []), contractIds, "Portfolio bodyFamilyIds must match supplied Body contracts");
  assert.equal(portfolio.comparisonPolicy, "WITHIN_BODY_FAMILY_ONLY", "Cross-Body performance comparison is prohibited");
  if (contracts.length === 1) {
    assert.equal(portfolio.bodyFamilyMode, "single_fixed", "One Body contract requires single_fixed mode");
    assert.equal(portfolio.bodyFamilyId, contracts[0].body_family_id, "Fixed Body family mismatch");
  } else {
    assert.equal(portfolio.bodyFamilyMode, "consultation_cohorts", "Multiple Body contracts are consultation cohorts, not one controlled test");
    assert.equal(portfolio.bodyFamilyId, null, "Consultation cohorts cannot claim one fixed bodyFamilyId");
  }

  const hookById = new Map(portfolio.packages.map((hook) => [hook.id, hook]));
  assert.equal(hookById.size, portfolio.packages.length, "Hook IDs must be unique");
  const assigned = new Map();
  for (const hook of portfolio.packages) {
    assert.ok(hook.promiseFamily, `Hook ${hook.id}: promiseFamily missing`);
    assert.ok(hook.matchedBodyFamilyId, `Hook ${hook.id}: matchedBodyFamilyId missing`);
    const contract = byId.get(hook.matchedBodyFamilyId);
    assert.ok(contract, `Hook ${hook.id}: unknown Body family ${hook.matchedBodyFamilyId}`);
    assert.equal(hook.promiseFamily, contract.promise_family, `Hook ${hook.id}: promise family does not match Body ${contract.body_family_id}`);
    assert.ok(contract.matched_hook_ids.includes(hook.id), `Hook ${hook.id}: Body contract does not include the Hook`);
    if (hookBodyReuseVersion === 1) {
      const entry = hook.bodyEntryCompatibility;
      const locked = contract.hook_entry_contract;
      assert.ok(entry, `Hook ${hook.id}: bodyEntryCompatibility missing`);
      assert.equal(entry.decision, "PASS", `Hook ${hook.id}: ${entry.decision ?? "missing decision"}; remove it from this fixed-Body job`);
      assert.equal(entry.signature, locked.signature, `Hook ${hook.id}: Body entry signature changed; a new Body is required`);
      assert.equal(entry.viewerState, locked.required_viewer_state, `Hook ${hook.id}: viewer state does not reach the locked Body entry`);
      assert.equal(entry.openQuestion, locked.required_open_question, `Hook ${hook.id}: open question changed; a new Body is required`);
      assert.equal(entry.expectedBodyAnswer, locked.expected_body_answer, `Hook ${hook.id}: expected Body answer changed; a new Body is required`);
      assert.ok(typeof entry.reason === "string" && entry.reason.trim(), `Hook ${hook.id}: compatibility reason missing`);
    }
    assigned.set(hook.id, (assigned.get(hook.id) ?? 0) + 1);
  }
  for (const contract of contracts) {
    const contractFamilies = new Set();
    for (const hookId of contract.matched_hook_ids) {
      const hook = hookById.get(hookId);
      assert.ok(hook, `Body ${contract.body_family_id}: unknown matched Hook ${hookId}`);
      assert.equal(hook.matchedBodyFamilyId, contract.body_family_id, `Hook ${hookId}: Body mapping is inconsistent`);
      contractFamilies.add(hook.promiseFamily);
    }
    assert.equal(contractFamilies.size, 1, `Body ${contract.body_family_id}: mixed Promise families are prohibited`);
    assert.equal([...contractFamilies][0], contract.promise_family, `Body ${contract.body_family_id}: promise family mismatch`);
  }
  for (const hook of portfolio.packages) assert.equal(assigned.get(hook.id), 1, `Hook ${hook.id}: must map to exactly one Body family`);
  if (contracts.length === 1) assert.equal(new Set(portfolio.packages.map((hook) => hook.promiseFamily)).size, 1, "One Body cannot absorb multiple Promise families");
  return { hooks: portfolio.packages.length, bodyFamilies: contracts.length };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const portfolioFile = process.argv[2] ? path.resolve(process.argv[2]) : null;
  const contractFiles = process.argv.slice(3).map((file) => path.resolve(file));
  assert.ok(portfolioFile && contractFiles.length > 0, "Usage: node scripts/validate-hook-body-fit.mjs <hook-packages.json> <body-contract.json> [more...]");
  const portfolio = JSON.parse(await readFile(portfolioFile, "utf8"));
  const contracts = await Promise.all(contractFiles.map((file) => readFile(file, "utf8").then(JSON.parse)));
  const result = validateHookBodyFit(portfolio, contracts);
  console.log(`Hook/Body fit: PASS (${result.hooks} Hooks / ${result.bodyFamilies} Body families / within-family comparison only)`);
}
