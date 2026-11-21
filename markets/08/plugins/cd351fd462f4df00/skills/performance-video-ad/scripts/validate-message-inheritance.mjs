#!/usr/bin/env node
import assert from "node:assert/strict";
import { realpathSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

export const REQUIRED_MESSAGE_CATEGORIES = [
  "pain",
  "stakes",
  "failed_approach",
  "new_belief",
  "mechanism",
  "payoff",
  "cta_deliverable",
];

function sourceIdFromRef(ref) {
  return String(ref).split("#", 1)[0];
}

export function validateMessageInheritance(contract, knownSourceIds = null) {
  assert.equal(contract.schemaVersion, 1, "message inheritance: unsupported schemaVersion");
  assert.equal(contract.sourceAssemblyVersion, 1, "message inheritance: unsupported sourceAssemblyVersion");
  assert.ok(contract.jobId && contract.offerId, "message inheritance: jobId and offerId are required");
  assert.ok(contract.categories && typeof contract.categories === "object", "message inheritance: categories are required");

  const version = contract.messageInheritanceVersion ?? 1;
  assert.ok([1, 2].includes(version), "message inheritance: unsupported messageInheritanceVersion");
  let requiredInAd = new Set(REQUIRED_MESSAGE_CATEGORIES);
  let optionalInAd = new Set();
  let intentionallyDeferred = new Set();
  if (version === 2) {
    const selection = contract.stage_selection;
    assert.ok(selection && selection.funnel_role_contract_ref, "message inheritance: v2 requires a Funnel Role Contract reference");
    requiredInAd = new Set(selection.required_in_ad_categories ?? []);
    optionalInAd = new Set(selection.optional_in_ad_categories ?? []);
    intentionallyDeferred = new Set(selection.intentionally_deferred_categories ?? []);
    assert.ok(requiredInAd.size > 0, "message inheritance: v2 requires at least one ad category");
    assert.ok(intentionallyDeferred.size > 0, "message inheritance: v2 must state what the destination will answer");
    const allSelected = [...requiredInAd, ...optionalInAd, ...intentionallyDeferred];
    assert.equal(new Set(allSelected).size, allSelected.length, "message inheritance: stage category lists overlap");
    for (const category of allSelected) assert.ok(REQUIRED_MESSAGE_CATEGORIES.includes(category), `message inheritance: unknown stage category ${category}`);
    assert.deepEqual(new Set(allSelected), new Set(REQUIRED_MESSAGE_CATEGORIES), "message inheritance: every canonical category must be assigned to ad or destination");
  }

  for (const categoryName of REQUIRED_MESSAGE_CATEGORIES) {
    const category = contract.categories[categoryName];
    assert.ok(category, `message inheritance: missing ${categoryName}`);
    assert.ok(Array.isArray(category.canonical_messages) && category.canonical_messages.length > 0, `message inheritance: ${categoryName} requires canonical messages`);
    assert.ok(Array.isArray(category.inherited_message_ids), `message inheritance: ${categoryName} inherited_message_ids must be an array`);
    if (version === 1 || requiredInAd.has(categoryName)) assert.ok(category.inherited_message_ids.length > 0, `message inheritance: ${categoryName} requires at least one inherited ad message`);
    const messages = new Map();
    for (const message of category.canonical_messages) {
      assert.ok(message.message_id && message.text, `message inheritance: ${categoryName} message requires ID and text`);
      assert.ok(!messages.has(message.message_id), `message inheritance: duplicate message ID ${message.message_id}`);
      assert.ok(Array.isArray(message.source_refs) && message.source_refs.length > 0, `message inheritance: ${message.message_id} requires source refs`);
      if (knownSourceIds) {
        for (const ref of message.source_refs) assert.ok(knownSourceIds.has(sourceIdFromRef(ref)), `message inheritance: unknown source ref ${ref}`);
      }
      messages.set(message.message_id, message);
    }
    for (const messageId of category.inherited_message_ids) {
      assert.ok(messages.has(messageId), `message inheritance: ${categoryName} inherits unknown message ${messageId}`);
    }
  }
  return { contract, version, requiredInAd: [...requiredInAd], intentionallyDeferred: [...intentionallyDeferred] };
}

async function main() {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-message-inheritance.mjs <message-inheritance-contract.json>");
  const contract = JSON.parse(await readFile(file, "utf8"));
  const result = validateMessageInheritance(contract);
  console.log(`Message inheritance: PASS (v${result.version}; ${result.requiredInAd.length} ad categories / ${result.intentionallyDeferred.length} deferred)`);
}

const isMain = (() => {
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); } catch { return false; }
})();

if (isMain) main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
