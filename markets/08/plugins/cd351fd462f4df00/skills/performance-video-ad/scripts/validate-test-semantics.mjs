#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const CONTRACTS = {
  territory_baseline: {
    causalClaimScope: "baseline_only",
    layerContract: { angleFixed: true, executionFixed: true, trendWrapperFixed: true },
  },
  hook_package_discovery: {
    causalClaimScope: "package_level_only",
    layerContract: { angleFixed: false, executionFixed: false, trendWrapperFixed: false },
  },
  angle_discovery: {
    causalClaimScope: "angle_level",
    layerContract: { angleFixed: false, executionFixed: true, trendWrapperFixed: true },
  },
  hook_execution_test: {
    causalClaimScope: "execution_level",
    layerContract: { angleFixed: true, executionFixed: false, trendWrapperFixed: true },
  },
  trend_wrapper_test: {
    causalClaimScope: "wrapper_level",
    layerContract: { angleFixed: true, executionFixed: true, trendWrapperFixed: false },
  },
};

const unique = (values) => new Set(values).size;

export function validateTestSemantics(testBatch, portfolio) {
  assert.equal(testBatch.testSemanticsVersion, 1, "testSemanticsVersion=1 is required");
  const expected = CONTRACTS[testBatch.testType];
  assert.ok(expected, `unknown testType: ${testBatch.testType}`);
  assert.equal(testBatch.causalClaimScope, expected.causalClaimScope, `${testBatch.testType} must use causalClaimScope=${expected.causalClaimScope}`);
  assert.deepEqual(testBatch.layerContract, expected.layerContract, `${testBatch.testType} has an invalid layerContract`);
  assert.equal(portfolio.testSemanticsVersion, testBatch.testSemanticsVersion, "testSemanticsVersion mismatch");
  assert.equal(portfolio.testType, testBatch.testType, "testType mismatch between batch and portfolio");
  assert.equal(portfolio.causalClaimScope, testBatch.causalClaimScope, "causalClaimScope mismatch between batch and portfolio");
  assert.ok(Array.isArray(portfolio.packages) && portfolio.packages.length > 0, "Hook packages missing");

  for (const item of portfolio.packages) {
    const signatures = item.testSignatures;
    assert.ok(signatures?.angle && signatures?.execution && signatures?.trendWrapper, `Hook ${item.id}: testSignatures are required`);
    const preconditions = item.audiencePreconditions;
    assert.ok(preconditions && ["broad", "conditional"].includes(preconditions.applicability), `Hook ${item.id}: audiencePreconditions.applicability missing`);
    assert.ok(Array.isArray(preconditions.requiredDataVisibility), `Hook ${item.id}: requiredDataVisibility must be an array`);
    if (preconditions.applicability === "conditional") {
      assert.ok(preconditions.requiredDataVisibility.length > 0 && !preconditions.requiredDataVisibility.includes("none"), `Hook ${item.id}: conditional Hook requires explicit data visibility`);
      assert.ok(typeof preconditions.interpretationRisk === "string" && preconditions.interpretationRisk.trim(), `Hook ${item.id}: conditional Hook requires interpretationRisk`);
    }
  }

  const signatures = {
    angle: portfolio.packages.map((item) => item.testSignatures.angle),
    execution: portfolio.packages.map((item) => item.testSignatures.execution),
    trendWrapper: portfolio.packages.map((item) => item.testSignatures.trendWrapper),
  };
  if (expected.layerContract.angleFixed) assert.equal(unique(signatures.angle), 1, `${testBatch.testType} requires one fixed angle signature`);
  if (expected.layerContract.executionFixed) assert.equal(unique(signatures.execution), 1, `${testBatch.testType} requires one fixed execution signature`);
  if (expected.layerContract.trendWrapperFixed) assert.equal(unique(signatures.trendWrapper), 1, `${testBatch.testType} requires one fixed trend-wrapper signature`);
  const isComparative = portfolio.packages.length > 1;
  if (isComparative && !expected.layerContract.angleFixed) assert.ok(unique(signatures.angle) >= 2, `${testBatch.testType} requires at least two angle signatures`);
  if (isComparative && !expected.layerContract.executionFixed) assert.ok(unique(signatures.execution) >= 2, `${testBatch.testType} requires at least two execution signatures`);
  if (isComparative && !expected.layerContract.trendWrapperFixed && testBatch.testType === "trend_wrapper_test") assert.ok(unique(signatures.trendWrapper) >= 2, "trend_wrapper_test requires at least two wrapper signatures");

  if (testBatch.shortlistPolicy) {
    assert.equal(testBatch.shortlistPolicy.gating, false, "a pre-approval shortlist must be non-gating");
    assert.equal(testBatch.shortlistPolicy.learningUse, "EXPLORATION_ONLY", "shortlist results cannot replace the controlled batch");
    assert.ok(Number.isInteger(testBatch.shortlistPolicy.maximumPackages) && testBatch.shortlistPolicy.maximumPackages > 0, "shortlist maximumPackages missing");
  }

  return {
    testType: testBatch.testType,
    causalClaimScope: testBatch.causalClaimScope,
    angles: unique(signatures.angle),
    executions: unique(signatures.execution),
    wrappers: unique(signatures.trendWrapper),
  };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const batchFile = process.argv[2] ? path.resolve(process.argv[2]) : null;
  const portfolioFile = process.argv[3] ? path.resolve(process.argv[3]) : null;
  assert.ok(batchFile && portfolioFile, "Usage: node scripts/validate-test-semantics.mjs <test-batch.json> <hook-packages.json>");
  const [batch, portfolio] = await Promise.all([readFile(batchFile, "utf8"), readFile(portfolioFile, "utf8")]);
  const result = validateTestSemantics(JSON.parse(batch), JSON.parse(portfolio));
  console.log(`Test semantics: PASS (${result.testType} / claim=${result.causalClaimScope} / angles=${result.angles} / executions=${result.executions} / wrappers=${result.wrappers})`);
}
