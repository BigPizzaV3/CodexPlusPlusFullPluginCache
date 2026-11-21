#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const countsFor = (items, selector) => {
  const counts = new Map();
  for (const item of items) {
    const key = selector(item);
    counts.set(key, (counts.get(key) ?? 0) + 1);
  }
  return counts;
};

const largest = (counts) => Math.max(0, ...counts.values());

export function validateHookDiversity(portfolio) {
  assert.equal(portfolio.hookModelVersion, 2, "Hook diversity contract requires hookModelVersion=2");
  assert.ok(portfolio.diversityPolicy && typeof portfolio.diversityPolicy === "object", "diversityPolicy missing");
  const policy = portfolio.diversityPolicy;
  for (const field of ["maxSameHypothesisFamily", "maxSameVisualGrammar", "minWorkNativeHooks", "maxTrendWrappedShare", "maxSpectacleShare"]) {
    assert.ok(Number.isFinite(policy[field]), `diversityPolicy.${field} missing`);
  }
  assert.equal(policy.spectacleRequiresExplicitExperiment, true, "spectacle must require an explicit experiment");

  for (const item of portfolio.packages) {
    assert.ok(item.hypothesisId, `Hook ${item.id}: hypothesisId missing`);
    assert.ok(item.hypothesisFamily, `Hook ${item.id}: hypothesisFamily missing`);
    assert.ok(item.execution && typeof item.execution === "object", `Hook ${item.id}: execution missing`);
    assert.ok(item.execution.visualGrammar, `Hook ${item.id}: visualGrammar missing`);
    assert.ok(item.execution.primaryAttentionSource, `Hook ${item.id}: primaryAttentionSource missing`);
    assert.ok(item.execution.trendWrapper && typeof item.execution.trendWrapper.applied === "boolean", `Hook ${item.id}: trendWrapper missing`);
    if (item.formatOrigin === "trend_adapted") {
      assert.equal(item.execution.trendWrapper.applied, true, `Hook ${item.id}: trend-adapted format requires applied trendWrapper`);
      assert.equal(item.execution.trendWrapper.type, item.formatWrapperId, `Hook ${item.id}: trendWrapper.type must match formatWrapperId`);
    } else {
      assert.equal(item.execution.trendWrapper.applied, false, `Hook ${item.id}: non-trend format cannot apply a trendWrapper`);
    }
  }

  const hypothesisCounts = countsFor(portfolio.packages, (item) => item.hypothesisFamily);
  const attentionCounts = countsFor(portfolio.packages, (item) => item.execution.primaryAttentionSource);
  const grammarCounts = countsFor(portfolio.packages, (item) => item.execution.visualGrammar);
  const workNative = portfolio.packages.filter((item) => item.expressionControl?.realisticWorkSurface === true).length;
  const trendWrapped = portfolio.packages.filter((item) => item.execution.trendWrapper.applied === true).length;
  const spectacle = portfolio.packages.filter((item) => item.expression_profile === "spectacle_experiment").length;
  const total = portfolio.packages.length;
  for (const item of portfolio.packages.filter((entry) => entry.expression_profile === "spectacle_experiment")) {
    assert.equal(item.candidateStatus, "experimental_only", `Hook ${item.id}: spectacle must remain experimental_only`);
    assert.ok(item.expressionControl?.explicitUserPermission === true || item.expressionControl?.experimentPurpose, `Hook ${item.id}: spectacle requires permission or purpose`);
  }
  if (portfolio.batchType !== "initial_hook_test") {
    return { total, hypothesisFamilies: hypothesisCounts.size, attentionMechanisms: attentionCounts.size, visualGrammars: grammarCounts.size, workNative, trendWrapped, spectacle };
  }

  assert.ok(hypothesisCounts.size >= 3, "portfolio requires at least three hypothesis families");
  assert.ok(attentionCounts.size >= 3, "portfolio requires at least three attention mechanisms");
  assert.ok(largest(hypothesisCounts) <= policy.maxSameHypothesisFamily, `one hypothesis family exceeds ${policy.maxSameHypothesisFamily}`);
  assert.ok(largest(grammarCounts) <= policy.maxSameVisualGrammar, `one visual grammar exceeds ${policy.maxSameVisualGrammar}`);

  assert.ok(workNative >= policy.minWorkNativeHooks, `portfolio requires at least ${policy.minWorkNativeHooks} work-native Hooks`);
  assert.ok(trendWrapped / total <= policy.maxTrendWrappedShare, `trend-wrapped share exceeds ${policy.maxTrendWrappedShare}`);
  assert.ok(spectacle / total <= policy.maxSpectacleShare, `spectacle share exceeds ${policy.maxSpectacleShare}`);
  return {
    total,
    hypothesisFamilies: hypothesisCounts.size,
    attentionMechanisms: attentionCounts.size,
    visualGrammars: grammarCounts.size,
    workNative,
    trendWrapped,
    spectacle,
  };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-hook-diversity.mjs <hook-packages.json>");
  const result = validateHookDiversity(JSON.parse(await readFile(file, "utf8")));
  console.log(`Hook diversity: PASS (${result.hypothesisFamilies} hypotheses / ${result.attentionMechanisms} attention mechanisms / ${result.visualGrammars} visual grammars / ${result.workNative} work-native)`);
}
