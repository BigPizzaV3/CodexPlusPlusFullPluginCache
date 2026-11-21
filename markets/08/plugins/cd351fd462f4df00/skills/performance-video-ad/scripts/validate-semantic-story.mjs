#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { validateBodyContract } from "./validate-body-contract.mjs";
import { validateHookHandoff } from "./validate-hook-handoff.mjs";
import { validateInsightRenderMap } from "./validate-insight-render-map.mjs";
import { validatePacingReview } from "./validate-pacing-review.mjs";

const STRENGTH_RANK = { low: 0, low_to_medium: 1, medium: 2, medium_to_high: 3, high: 4 };

export function validateSemanticStory({ expressionPolicy, bodyContract, hookHandoff, insightRenderMap, pacingReview = null }) {
  assert.equal(expressionPolicy.expressionPolicyVersion, 2, "Semantic story requires Expression Policy v2");
  assert.ok(expressionPolicy.message_policy, "Semantic story requires message_policy");
  assert.ok(STRENGTH_RANK[expressionPolicy.message_policy.semantic_tension] >= STRENGTH_RANK.medium_to_high, "Semantic tension is too weak for the approved story");
  assert.ok(STRENGTH_RANK[expressionPolicy.message_policy.insight_strength] >= STRENGTH_RANK.medium_to_high, "Insight strength is too weak for the approved story");
  assert.ok(STRENGTH_RANK[expressionPolicy.message_policy.emotional_specificity] >= STRENGTH_RANK.medium_to_high, "Emotional specificity is too weak for the approved story");
  assert.ok(["calibrated", "assertive_evidence_backed"].includes(expressionPolicy.message_policy.claim_certainty), "Claim certainty must preserve expectation without unsupported guarantees");
  validateBodyContract(bodyContract);
  validateHookHandoff(hookHandoff);
  validateInsightRenderMap(insightRenderMap);
  if (pacingReview) validatePacingReview(pacingReview);
  const jobIds = new Set([expressionPolicy.jobId, bodyContract.jobId, hookHandoff.jobId, insightRenderMap.jobId, pacingReview?.jobId].filter(Boolean));
  assert.equal(jobIds.size, 1, "Semantic story artifacts have mismatched jobIds");
  assert.equal(insightRenderMap.body_family_id, bodyContract.body_family_id, "Insight Render Map Body family mismatch");
  assert.equal(insightRenderMap.gate_status, "PASS", "Critical insight render coverage must pass");
  return { bodyFamilyId: bodyContract.body_family_id, handoffs: hookHandoff.entries.length, insights: insightRenderMap.insights.length };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const files = process.argv.slice(2).map((file) => path.resolve(file));
  assert.ok(files.length >= 4 && files.length <= 5, "Usage: node scripts/validate-semantic-story.mjs <expression-policy.json> <body-contract.json> <hook-handoff.json> <insight-render-map.json> [pacing-review.json]");
  const [expressionPolicy, bodyContract, hookHandoff, insightRenderMap, pacingReview] = await Promise.all(files.map((file) => readFile(file, "utf8").then(JSON.parse)));
  const result = validateSemanticStory({ expressionPolicy, bodyContract, hookHandoff, insightRenderMap, pacingReview });
  console.log(`Semantic story: PASS (${result.bodyFamilyId} / ${result.handoffs} handoffs / ${result.insights} insights)`);
}
