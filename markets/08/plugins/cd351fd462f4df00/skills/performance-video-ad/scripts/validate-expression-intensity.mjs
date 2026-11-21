#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const INTENSITY_RANK = { low: 0, low_to_medium: 1, medium: 2, medium_to_high: 3, high: 4 };

export function validateExpressionIntensity(portfolio, policy) {
  assert.equal(policy.status, "POLICY_RESOLVED", "expression policy must be resolved");
  assert.equal(portfolio.expression_profile, policy.selected_expression_profile, "portfolio default profile must match resolved expression policy");
  assert.ok(INTENSITY_RANK[policy.visual_intensity] !== undefined, "policy visual_intensity invalid");
  assert.ok(INTENSITY_RANK[policy.motion_density] !== undefined, "policy motion_density invalid");
  if (policy.expressionPolicyVersion === 2) {
    const message = policy.message_policy;
    assert.ok(message, "Expression Policy v2 requires message_policy");
    assert.ok(INTENSITY_RANK[message.semantic_tension] !== undefined, "message semantic_tension invalid");
    assert.ok(INTENSITY_RANK[message.insight_strength] !== undefined, "message insight_strength invalid");
    assert.ok(INTENSITY_RANK[message.emotional_specificity] !== undefined, "message emotional_specificity invalid");
    assert.equal(typeof message.surprise_required, "boolean", "message surprise_required must be boolean");
    assert.ok(["conservative", "calibrated", "assertive_evidence_backed"].includes(message.claim_certainty), "message claim_certainty invalid");
    if (policy.selected_expression_profile === "restrained_b2b_social") {
      assert.ok(INTENSITY_RANK[message.semantic_tension] >= INTENSITY_RANK.medium_to_high, "restrained visuals must not force weak semantic tension");
      assert.ok(INTENSITY_RANK[message.insight_strength] >= INTENSITY_RANK.medium_to_high, "restrained visuals must not force weak insight strength");
    }
  }
  const prohibited = new Set(policy.prohibited_primary_attention_sources);

  for (const item of portfolio.packages) {
    assert.ok(item.execution, `Hook ${item.id}: execution missing`);
    const execution = item.execution;
    assert.ok(INTENSITY_RANK[execution.visualIntensity] !== undefined, `Hook ${item.id}: visualIntensity invalid`);
    assert.ok(INTENSITY_RANK[execution.motionDensity] !== undefined, `Hook ${item.id}: motionDensity invalid`);
    const experimental = item.candidateStatus === "experimental_only" && item.expression_profile === "spectacle_experiment";
    if (!experimental) {
      assert.equal(prohibited.has(execution.primaryAttentionSource), false, `Hook ${item.id}: prohibited primary attention source ${execution.primaryAttentionSource}`);
      assert.ok(INTENSITY_RANK[execution.visualIntensity] <= INTENSITY_RANK[policy.visual_intensity], `Hook ${item.id}: visual intensity exceeds policy`);
      assert.ok(INTENSITY_RANK[execution.motionDensity] <= INTENSITY_RANK[policy.motion_density], `Hook ${item.id}: motion density exceeds policy`);
      assert.ok(execution.simultaneousElements <= policy.cognitive_load_limit.max_simultaneous_elements, `Hook ${item.id}: cognitive element limit exceeded`);
      assert.ok(execution.decisionsPerScene <= policy.cognitive_load_limit.max_decisions_per_scene, `Hook ${item.id}: decisions-per-scene limit exceeded`);
      assert.equal(execution.vfxIndependent, true, `Hook ${item.id}: VFX-dependent non-experimental Hook`);
    } else {
      assert.equal(policy.spectacle_policy, "experimental_only", `Hook ${item.id}: policy does not permit spectacle experiment`);
      assert.ok(item.expressionControl?.explicitUserPermission === true || item.expressionControl?.experimentPurpose, `Hook ${item.id}: experimental expression requires permission or purpose`);
    }
  }

  return { hooks: portfolio.packages.length, profile: policy.selected_expression_profile };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const portfolioFile = process.argv[2] ? path.resolve(process.argv[2]) : null;
  const policyFile = process.argv[3] ? path.resolve(process.argv[3]) : null;
  assert.ok(portfolioFile && policyFile, "Usage: node scripts/validate-expression-intensity.mjs <hook-packages.json> <expression-policy.json>");
  const [portfolio, policy] = await Promise.all([
    readFile(portfolioFile, "utf8").then(JSON.parse),
    readFile(policyFile, "utf8").then(JSON.parse),
  ]);
  const result = validateExpressionIntensity(portfolio, policy);
  console.log(`Expression intensity: PASS (${result.hooks} Hooks / ${result.profile})`);
}
