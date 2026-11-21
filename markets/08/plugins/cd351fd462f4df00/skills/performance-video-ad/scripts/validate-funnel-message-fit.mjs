#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateFunnelRoleContract } from "./validate-funnel-role-contract.mjs";

export function validateFunnelMessageFit(contract, lineage, { requireAdCopy = true } = {}) {
  validateFunnelRoleContract(contract, { requireResolved: true });
  assert.ok(lineage && Array.isArray(lineage.entries), "funnel message fit: copy lineage entries missing");
  const planned = new Set(contract.message_budget.core_messages.map((message) => message.message_id));
  const rendered = new Set();
  let adEntries = 0;

  for (const entry of lineage.entries) {
    assert.ok(["planning_only", "ad", "destination"].includes(entry.delivery_scope), `funnel message fit: ${entry.copy_id ?? "<unknown>"} lacks delivery_scope`);
    if (entry.delivery_scope !== "ad") {
      assert.ok(entry.stage_message_id === null || entry.stage_message_id === undefined, `funnel message fit: non-ad copy ${entry.copy_id} must not consume an ad message slot`);
      continue;
    }
    adEntries += 1;
    assert.ok(entry.stage_message_id && planned.has(entry.stage_message_id), `funnel message fit: ad copy ${entry.copy_id} maps to an unknown core message`);
    rendered.add(entry.stage_message_id);
  }

  if (requireAdCopy) assert.ok(adEntries > 0, "funnel message fit: active ad requires ad-scoped copy lineage");
  assert.ok(rendered.size <= contract.message_budget.max_total_core_messages, "funnel message fit: rendered concepts exceed the message budget");
  if (requireAdCopy) {
    const missing = [...planned].filter((messageId) => !rendered.has(messageId));
    assert.equal(missing.length, 0, `funnel message fit: planned core messages are not rendered: ${missing.join(", ")}`);
  }
  return { adEntries, renderedMessages: rendered.size };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const [contractFile, lineageFile] = process.argv.slice(2).map((file) => path.resolve(file));
  assert.ok(contractFile && lineageFile, "Usage: node scripts/validate-funnel-message-fit.mjs <funnel-role-contract.json> <copy-lineage.json>");
  const [contract, lineage] = await Promise.all([contractFile, lineageFile].map((file) => readFile(file, "utf8").then(JSON.parse)));
  const result = validateFunnelMessageFit(contract, lineage);
  console.log(`Funnel message fit: PASS (${result.renderedMessages} core messages / ${result.adEntries} ad copy entries)`);
}
