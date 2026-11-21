#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const COLD_REQUIRED_ROLES = ["pain", "tension", "surprising_reframe", "product_category", "cta"];
const COLD_DEFERRED_RESPONSIBILITIES = ["full_mechanism_explanation", "full_objection_handling", "detailed_deliverables", "pricing_explanation", "contract_persuasion"];
const COLD_PRIMARY_METRICS = ["qualified_outbound_ctr", "landing_page_view_rate"];
const COLD_GUARDRAILS = ["landing_page_engagement", "consultation_cvr", "qualified_lead_rate"];
const FORBIDDEN_COLD_CORE_ROLES = new Set(["objection", "deliverable", "pricing"]);
const nonEmpty = (value) => typeof value === "string" && value.trim().length > 0;

export function validateFunnelRoleContract(contract, { requireResolved = false } = {}) {
  assert.equal(contract.schemaVersion, 1, "funnel role: unsupported schemaVersion");
  assert.equal(contract.funnelRoleContractVersion, 1, "funnel role: unsupported funnelRoleContractVersion");
  assert.ok(contract.jobId, "funnel role: jobId missing");
  assert.ok(["DRAFT", "NEEDS_USER_INPUT", "ROLE_RESOLVED"].includes(contract.status), "funnel role: invalid status");
  if (contract.status !== "ROLE_RESOLVED" && !requireResolved) return { status: contract.status, stage: contract.funnel_stage, coreMessages: 0 };
  assert.equal(contract.status, "ROLE_RESOLVED", "funnel role: Hook work requires ROLE_RESOLVED status");

  assert.ok(Array.isArray(contract.source_refs) && contract.source_refs.length > 0, "funnel role: source refs missing");
  assert.ok(nonEmpty(contract.traffic_temperature) && nonEmpty(contract.awareness_stage) && nonEmpty(contract.funnel_stage), "funnel role: traffic, awareness, and stage are required");
  assert.ok(contract.next_destination && nonEmpty(contract.next_destination.type) && nonEmpty(contract.next_destination.ref) && nonEmpty(contract.next_destination.role), "funnel role: next destination is incomplete");
  assert.ok(contract.primary_conversion && nonEmpty(contract.primary_conversion.type) && nonEmpty(contract.primary_conversion.occurs_on), "funnel role: primary conversion is incomplete");
  assert.ok(contract.final_conversion && nonEmpty(contract.final_conversion.type) && nonEmpty(contract.final_conversion.occurs_on), "funnel role: final conversion is incomplete");
  assert.ok(Array.isArray(contract.final_conversion.occurs_after) && contract.final_conversion.occurs_after.length > 0, "funnel role: final conversion path missing");
  assert.ok(nonEmpty(contract.ad_cta_action), "funnel role: ad CTA semantic action missing");

  const role = contract.stage_role;
  assert.ok(role && Array.isArray(role.primary_jobs) && role.primary_jobs.length > 0, "funnel role: primary jobs missing");
  assert.ok(Array.isArray(role.secondary_jobs), "funnel role: secondary jobs missing");
  assert.ok(Array.isArray(role.not_responsible_for), "funnel role: deferred responsibilities missing");

  const budget = contract.message_budget;
  assert.ok(budget && Number.isInteger(budget.max_total_core_messages) && budget.max_total_core_messages > 0, "funnel role: message limit missing");
  assert.ok(Number.isInteger(budget.max_mechanism_steps) && budget.max_mechanism_steps >= 0, "funnel role: mechanism limit missing");
  assert.ok(Number.isInteger(budget.max_proof_items) && budget.max_proof_items >= 0, "funnel role: proof limit missing");
  assert.ok(Array.isArray(budget.core_messages) && budget.core_messages.length > 0, "funnel role: core message plan missing");
  assert.ok(budget.core_messages.length <= budget.max_total_core_messages, "funnel role: core messages exceed the stage budget");
  const messageIds = new Set();
  for (const message of budget.core_messages) {
    assert.ok(message.message_id && !messageIds.has(message.message_id), `funnel role: duplicate or missing message ${message.message_id ?? "<missing>"}`);
    assert.ok(nonEmpty(message.role) && nonEmpty(message.text), `funnel role: message ${message.message_id} is incomplete`);
    assert.ok(Array.isArray(message.source_refs) && message.source_refs.length > 0, `funnel role: message ${message.message_id} lacks source refs`);
    messageIds.add(message.message_id);
  }
  assert.ok(budget.core_messages.filter((message) => message.role === "mechanism").length <= budget.max_mechanism_steps, "funnel role: mechanism explanation exceeds the stage budget");
  assert.ok(budget.core_messages.filter((message) => message.role === "proof").length <= budget.max_proof_items, "funnel role: proof exceeds the stage budget");

  const handoff = contract.curiosity_handoff;
  assert.ok(handoff && nonEmpty(handoff.question_created_by_ad), "funnel role: curiosity handoff question missing");
  assert.ok(Array.isArray(handoff.answered_in_ad) && handoff.answered_in_ad.length > 0, "funnel role: answered_in_ad missing");
  assert.ok(Array.isArray(handoff.intentionally_left_for_destination) && handoff.intentionally_left_for_destination.length > 0, "funnel role: the ad must intentionally leave a destination question unresolved");
  const duplicateHandoffs = handoff.answered_in_ad.filter((item) => handoff.intentionally_left_for_destination.includes(item));
  assert.equal(duplicateHandoffs.length, 0, "funnel role: one question cannot be both answered in the ad and deferred");
  assert.equal(contract.downstream_continuity?.status, "aligned", "funnel role: ad expectation and destination answer are not aligned");
  assert.ok(nonEmpty(contract.downstream_continuity.ad_expectation) && nonEmpty(contract.downstream_continuity.destination_entry_answer), "funnel role: downstream continuity copy missing");

  const metrics = contract.stage_metrics;
  assert.ok(metrics && Array.isArray(metrics.primary) && metrics.primary.length > 0, "funnel role: primary stage metrics missing");
  assert.ok(Array.isArray(metrics.guardrails) && metrics.guardrails.length > 0, "funnel role: guardrails missing");
  assert.ok(Array.isArray(metrics.downstream), "funnel role: downstream metrics missing");
  const duration = contract.duration_strategy;
  assert.ok(duration && nonEmpty(duration.mode) && nonEmpty(duration.rationale), "funnel role: duration strategy missing");
  assert.ok(Number.isFinite(duration.target_seconds?.min) && Number.isFinite(duration.target_seconds?.max) && duration.target_seconds.min <= duration.target_seconds.max, "funnel role: duration range invalid");

  if (contract.funnel_stage === "cold_clickthrough_ad" && contract.next_destination.role === "full_persuasion") {
    for (const job of ["create_relevant_curiosity", "earn_qualified_click"]) assert.ok(role.primary_jobs.includes(job), `funnel role: cold clickthrough primary job missing ${job}`);
    for (const responsibility of COLD_DEFERRED_RESPONSIBILITIES) assert.ok(role.not_responsible_for.includes(responsibility), `funnel role: cold ad must defer ${responsibility}`);
    assert.ok(budget.max_total_core_messages <= 5, "funnel role: cold clickthrough ad cannot become a mini-LP (max five core messages)");
    assert.ok(budget.max_mechanism_steps <= 1, "funnel role: cold clickthrough ad allows at most one mechanism step");
    assert.ok(budget.max_proof_items <= 1, "funnel role: cold clickthrough ad allows at most one proof item");
    const messageRoles = budget.core_messages.map((message) => message.role);
    for (const messageRole of COLD_REQUIRED_ROLES) assert.ok(messageRoles.includes(messageRole), `funnel role: cold clickthrough message plan missing ${messageRole}`);
    assert.ok(messageRoles.every((messageRole) => !FORBIDDEN_COLD_CORE_ROLES.has(messageRole)), "funnel role: cold clickthrough core contains LP-stage explanation");
    for (const metric of COLD_PRIMARY_METRICS) assert.ok(metrics.primary.includes(metric), `funnel role: cold clickthrough primary metric missing ${metric}`);
    for (const metric of COLD_GUARDRAILS) assert.ok(metrics.guardrails.includes(metric), `funnel role: cold clickthrough guardrail missing ${metric}`);
  }

  return { status: contract.status, stage: contract.funnel_stage, coreMessages: budget.core_messages.length };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-funnel-role-contract.mjs <funnel-role-contract.json> [--require-resolved]");
  const contract = JSON.parse(await readFile(file, "utf8"));
  const result = validateFunnelRoleContract(contract, { requireResolved: process.argv.includes("--require-resolved") });
  console.log(`Funnel role: PASS (${result.status}; ${result.stage ?? "unresolved"}; ${result.coreMessages} core messages)`);
}
