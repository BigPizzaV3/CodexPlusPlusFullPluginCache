#!/usr/bin/env node
import assert from "node:assert/strict";
import { realpathSync } from "node:fs";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const nonEmpty = (value, label) => assert.ok(typeof value === "string" && value.trim(), `sales thesis: ${label} is required`);
const sourceIdFromRef = (ref) => String(ref).split("#", 1)[0];

export function validateSalesThesis(thesis, { requireReady = false, knownSourceIds = null } = {}) {
  assert.equal(thesis.schemaVersion, 1, "sales thesis: unsupported schemaVersion");
  assert.equal(thesis.contractType, "performance_video_sales_thesis", "sales thesis: invalid contractType");
  assert.equal(thesis.salesThesisVersion, 1, "sales thesis: unsupported salesThesisVersion");
  for (const field of ["jobId", "offerId", "salesThesisId"]) nonEmpty(thesis[field], field);
  assert.ok(["DRAFT", "NEEDS_SOURCE_INPUT", "READY_FOR_PREMISE_APPROVAL"].includes(thesis.status), "sales thesis: invalid status");

  if (thesis.status === "DRAFT") {
    assert.equal(requireReady, false, "sales thesis: Creative Premise approval requires a ready Sales Thesis");
    return thesis;
  }

  if (thesis.status === "NEEDS_SOURCE_INPUT") {
    assert.equal(requireReady, false, "sales thesis: missing source understanding blocks Creative Premise approval");
    return thesis;
  }

  assert.ok(Array.isArray(thesis.raw_moments) && thesis.raw_moments.length >= 1, "sales thesis: at least one Raw Moment is required");
  const rawMomentIds = new Set();
  for (const moment of thesis.raw_moments) {
    for (const field of ["id", "situation", "source_language", "observable_behavior", "felt_stake"]) nonEmpty(moment[field], `raw moment ${moment.id ?? "<unknown>"}.${field}`);
    assert.ok(["verbatim_quote", "paraphrase", "multi_source_synthesis"].includes(moment.derivation_type), `sales thesis: raw moment ${moment.id} has invalid derivation_type`);
    assert.equal(rawMomentIds.has(moment.id), false, `sales thesis: duplicate Raw Moment ${moment.id}`);
    rawMomentIds.add(moment.id);
    validateSourceRefs(moment.source_refs, `raw moment ${moment.id}`, knownSourceIds);
  }

  const product = thesis.product_concept;
  assert.ok(product && typeof product === "object", "sales thesis: product_concept is required");
  for (const field of ["shorthand", "what_it_is", "customer_future", "reason_to_believe"]) nonEmpty(product[field], `product_concept.${field}`);
  assert.ok([...product.shorthand].length <= 80, "sales thesis: product shorthand must stay concise");
  nonEmpty(thesis.communication_concept, "communication_concept");
  nonEmpty(thesis.single_sell_reason, "single_sell_reason");
  assert.ok([...thesis.communication_concept].length <= 160, "sales thesis: communication concept must be one concise idea");
  assert.ok([...thesis.single_sell_reason].length <= 200, "sales thesis: Single Sell Reason must stay singular and concise");

  const attention = thesis.attention_hypothesis;
  nonEmpty(attention?.stop_reason, "attention_hypothesis.stop_reason");
  nonEmpty(attention?.continue_reason, "attention_hypothesis.continue_reason");
  assert.notEqual(attention.stop_reason.trim(), attention.continue_reason.trim(), "sales thesis: stop and continue reasons must be distinct");

  assert.ok(Array.isArray(thesis.sales_question_chain) && thesis.sales_question_chain.length >= 3 && thesis.sales_question_chain.length <= 6, "sales thesis: Sales Question Chain must contain three to six questions");
  const expectedOrders = thesis.sales_question_chain.map((_, index) => index + 1);
  assert.deepEqual(thesis.sales_question_chain.map((item) => item.order), expectedOrders, "sales thesis: question order must be contiguous from 1");
  for (const question of thesis.sales_question_chain) {
    nonEmpty(question.viewer_question, `question ${question.order}.viewer_question`);
    nonEmpty(question.answer_job, `question ${question.order}.answer_job`);
    validateSourceRefs(question.source_refs, `question ${question.order}`, knownSourceIds);
  }

  assert.equal(thesis.certainty, "planning_hypothesis", "sales thesis: certainty must remain planning_hypothesis");
  assert.equal(thesis.performance_claim, false, "sales thesis: a response hypothesis cannot claim performance");
  validateSourceRefs(thesis.source_refs, "source_refs", knownSourceIds);
  return thesis;
}

function validateSourceRefs(refs, label, knownSourceIds) {
  assert.ok(Array.isArray(refs) && refs.length > 0, `sales thesis: ${label} requires source refs`);
  if (!knownSourceIds) return;
  for (const ref of refs) assert.ok(knownSourceIds.has(sourceIdFromRef(ref)), `sales thesis: unknown source ref ${ref}`);
}

async function main() {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-sales-thesis.mjs <sales-thesis.json> [--require-ready]");
  const thesis = JSON.parse(await readFile(file, "utf8"));
  validateSalesThesis(thesis, { requireReady: process.argv.includes("--require-ready") });
  console.log(`Sales Thesis: PASS (${thesis.status}; ${thesis.sales_question_chain?.length ?? 0} viewer questions)`);
}

const isMain = (() => {
  try { return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url)); } catch { return false; }
})();

if (isMain) main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
