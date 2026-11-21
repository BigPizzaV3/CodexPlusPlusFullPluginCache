#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const REQUIRED_CONTEXT_FIELDS = [
  "market_type",
  "audience_temperature",
  "awareness_stage",
  "decision_stakes",
  "trust_requirement",
  "brand_familiarity",
  "audience_sophistication",
  "evidence_maturity",
  "platform",
];

const EVIDENCE_RANK = {
  no_evidence: 0,
  mechanism_only: 1,
  qualitative_proof: 2,
  quantified_case_studies: 3,
  replicated_results: 4,
};

const confidenceFromSources = (context) => {
  const sourceCount = REQUIRED_CONTEXT_FIELDS.filter((field) => context.sources?.[field]).length;
  if (sourceCount >= 8) return "high";
  if (sourceCount >= 5) return "medium";
  return "low";
};

const confidenceForResolution = (context, resolutionRule) => {
  const sourceConfidence = confidenceFromSources(context);
  if (sourceConfidence !== "high") return sourceConfidence;
  if (["balanced_default", "strong_visual_underperformance"].includes(resolutionRule)) return "medium";
  return "high";
};

const messagePolicyFor = (resolutionRule) => {
  if (["cold_high_trust_or_stakes", "high_trust_b2c", "strong_visual_underperformance"].includes(resolutionRule)) {
    return {
      semantic_tension: "high",
      insight_strength: "high",
      surprise_required: true,
      emotional_specificity: "high",
      claim_certainty: "calibrated",
    };
  }
  if (resolutionRule === "warm_proven_familiar") {
    return {
      semantic_tension: "medium_to_high",
      insight_strength: "high",
      surprise_required: false,
      emotional_specificity: "medium_to_high",
      claim_certainty: "assertive_evidence_backed",
    };
  }
  return {
    semantic_tension: "medium_to_high",
    insight_strength: "medium_to_high",
    surprise_required: true,
    emotional_specificity: "medium_to_high",
    claim_certainty: "calibrated",
  };
};

const policyFor = (context, resolutionRule) => {
  const shared = {
    schemaVersion: 1,
    jobId: context.jobId,
    status: "POLICY_RESOLVED",
    confidence: confidenceForResolution(context, resolutionRule),
    source_fields: [...REQUIRED_CONTEXT_FIELDS],
    resolution_rule: resolutionRule,
  };

  if (["cold_high_trust_or_stakes", "high_trust_b2c", "strong_visual_underperformance"].includes(resolutionRule)) {
    return {
      ...shared,
      selected_expression_profile: "restrained_b2b_social",
      primary_attention_sources: ["workplace_contradiction", "social_tension", "semantic_tension"],
      secondary_attention_sources: ["native_format", "restrained_visual_change"],
      prohibited_primary_attention_sources: ["spectacle", "cinematic_vfx", "destruction_metaphor"],
      visual_intensity: "low_to_medium",
      motion_density: "low_to_medium",
      cognitive_load_limit: { max_simultaneous_elements: 4, max_decisions_per_scene: 1 },
      work_native_priority: "high",
      trend_wrapper_policy: "optional",
      spectacle_policy: "experimental_only",
      reasoning: [
        "Trust and decision context require attention to come from a recognizable work problem rather than spectacle.",
        "Brand, evidence, or historical context does not support using cinematic intensity as the primary attention source.",
      ],
    };
  }

  if (resolutionRule === "warm_proven_familiar") {
    return {
      ...shared,
      selected_expression_profile: "balanced_social_brand",
      primary_attention_sources: ["product_demonstration", "proof_demonstration", "semantic_tension"],
      secondary_attention_sources: ["native_format", "restrained_visual_change"],
      prohibited_primary_attention_sources: ["destruction_metaphor"],
      visual_intensity: "medium",
      motion_density: "medium",
      cognitive_load_limit: { max_simultaneous_elements: 4, max_decisions_per_scene: 1 },
      work_native_priority: "medium",
      trend_wrapper_policy: "allowed",
      spectacle_policy: "experimental_only",
      reasoning: [
        "A familiar or returning audience with proof can stop on product or evidence demonstration.",
        "Brand motion may support comprehension, but spectacle remains an isolated experiment.",
      ],
    };
  }

  if (resolutionRule === "cold_low_stakes_b2c") {
    return {
      ...shared,
      selected_expression_profile: "balanced_social_brand",
      primary_attention_sources: ["native_format", "product_demonstration", "visual_novelty"],
      secondary_attention_sources: ["restrained_visual_change", "semantic_tension"],
      prohibited_primary_attention_sources: ["destruction_metaphor"],
      visual_intensity: "medium_to_high",
      motion_density: "medium_to_high",
      cognitive_load_limit: { max_simultaneous_elements: 4, max_decisions_per_scene: 1 },
      work_native_priority: "low",
      trend_wrapper_policy: "preferred",
      spectacle_policy: "experimental_only",
      reasoning: [
        "Low-stakes consumer acquisition can test stronger native-format and visual attention.",
        "Strong visual expression is allowed as a candidate, not presumed to be a winner.",
      ],
    };
  }

  return {
    ...shared,
    selected_expression_profile: "balanced_social_brand",
    primary_attention_sources: ["semantic_tension", "product_demonstration", "native_format"],
    secondary_attention_sources: ["restrained_visual_change", "social_tension"],
    prohibited_primary_attention_sources: ["destruction_metaphor"],
    visual_intensity: "medium",
    motion_density: "medium",
    cognitive_load_limit: { max_simultaneous_elements: 4, max_decisions_per_scene: 1 },
    work_native_priority: "medium",
    trend_wrapper_policy: "optional",
    spectacle_policy: "experimental_only",
    reasoning: [
      "The context does not justify either a high-trust restraint override or a high-intensity acquisition override.",
      "Use a balanced profile and keep attention tied to meaning, product, or native format.",
    ],
  };
};

export function resolveExpressionPolicy(context) {
  assert.equal(context.schemaVersion, 1, "creative context: unsupported schemaVersion");
  assert.equal(context.status, "CONTEXT_CLASSIFIED", "creative context must be CONTEXT_CLASSIFIED");
  assert.ok(context.jobId, "creative context: jobId missing");
  for (const field of REQUIRED_CONTEXT_FIELDS) {
    assert.ok(context[field], `creative context: ${field} missing`);
    assert.ok(typeof context.sources?.[field] === "string" && context.sources[field].trim(), `creative context: source missing for ${field}`);
  }
  assert.ok(context.sources && Object.keys(context.sources).length > 0, "creative context: source references are required");
  for (const signal of context.historical_creative_signals ?? []) {
    for (const field of ["id", "signal_type", "observation", "result", "confidence", "scope", "source"]) {
      assert.ok(typeof signal[field] === "string" && signal[field].trim(), `creative context signal: ${field} missing`);
    }
  }

  const isCold = context.audience_temperature === "cold";
  const isWarm = ["warm", "retargeting", "existing_customer"].includes(context.audience_temperature);
  const proofAvailable = EVIDENCE_RANK[context.evidence_maturity] >= EVIDENCE_RANK.qualitative_proof;
  const familiar = ["partially_known", "known"].includes(context.brand_familiarity);
  const platformRoot = context.platform.toLowerCase().split(/[_-]/)[0];
  const strongVisualUnderperformed = (context.historical_creative_signals ?? []).some((signal) => {
    const scope = signal.scope.toLowerCase();
    const scopeApplies = scope.includes(platformRoot) || scope.includes(context.market_type) || scope.includes("all_market");
    return signal.signal_type === "strong_visual_expression" && signal.result === "underperformed"
      && ["medium", "high"].includes(signal.confidence) && scopeApplies;
  });

  let resolutionRule = "balanced_default";
  if (isCold && (context.trust_requirement === "high" || context.decision_stakes === "high") && context.brand_familiarity === "unknown") {
    resolutionRule = "cold_high_trust_or_stakes";
  } else if (context.market_type === "b2c" && context.trust_requirement === "high") {
    resolutionRule = "high_trust_b2c";
  } else if (strongVisualUnderperformed) {
    resolutionRule = "strong_visual_underperformance";
  } else if (isWarm && proofAvailable && familiar) {
    resolutionRule = "warm_proven_familiar";
  } else if (context.market_type === "b2c" && isCold && context.decision_stakes === "low" && context.trust_requirement === "low") {
    resolutionRule = "cold_low_stakes_b2c";
  }

  const policy = policyFor(context, resolutionRule);
  if (context.expressionPolicyVersion === 2) {
    policy.expressionPolicyVersion = 2;
    policy.message_policy = messagePolicyFor(resolutionRule);
  }
  if (strongVisualUnderperformed) policy.source_fields.push("historical_creative_signals");
  return policy;
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const args = process.argv.slice(2);
  const input = args[0] ? path.resolve(args[0]) : null;
  const outIndex = args.indexOf("--out");
  const output = outIndex >= 0 ? path.resolve(args[outIndex + 1]) : null;
  assert.ok(input, "Usage: node scripts/resolve-expression-policy.mjs <creative-context.json> [--out <expression-policy.json>]");
  const context = JSON.parse(await readFile(input, "utf8"));
  const policy = resolveExpressionPolicy(context);
  const serialized = `${JSON.stringify(policy, null, 2)}\n`;
  if (output) {
    await writeFile(output, serialized, "utf8");
    console.log(`Expression policy: ${policy.selected_expression_profile} (${policy.resolution_rule}, confidence=${policy.confidence}) -> ${output}`);
  } else {
    process.stdout.write(serialized);
  }
}
