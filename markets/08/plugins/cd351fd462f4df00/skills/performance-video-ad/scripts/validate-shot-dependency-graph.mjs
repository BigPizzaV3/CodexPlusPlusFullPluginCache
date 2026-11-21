#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SHA256 = /^[a-f0-9]{64}$/i;
const ACTUAL_UPSTREAM_SOURCES = new Set(["actual_output_frame", "deterministic_actual_frame"]);
const APPROVED_UPSTREAM_STATUSES = new Set(["raw_approved", "deterministic_approved"]);

const assertAcyclic = (nodes, edges) => {
  const adjacency = new Map(nodes.map((node) => [node.shotId, []]));
  for (const edge of edges) adjacency.get(edge.fromShotId).push(edge.toShotId);
  const visiting = new Set();
  const visited = new Set();
  const visit = (shotId) => {
    assert.equal(visiting.has(shotId), false, `shot dependency graph: cycle detected at ${shotId}`);
    if (visited.has(shotId)) return;
    visiting.add(shotId);
    for (const next of adjacency.get(shotId)) visit(next);
    visiting.delete(shotId);
    visited.add(shotId);
  };
  for (const node of nodes) visit(node.shotId);
};

const validateContinuityEdgeForPaidTarget = (edge, upstreamNode) => {
  assert.equal(edge.continuityRequired, true, `shot dependency graph: ${edge.toShotId} must declare required continuity`);
  assert.ok(["continuous", "match_cut"].includes(edge.transitionMode), `shot dependency graph: ${edge.toShotId} continuity must use continuous or match_cut`);
  assert.ok(APPROVED_UPSTREAM_STATUSES.has(upstreamNode.executionStatus), `shot dependency graph: ${edge.toShotId} is blocked until upstream ${edge.fromShotId} has approved actual output`);
  assert.ok(ACTUAL_UPSTREAM_SOURCES.has(edge.upstreamFrame?.source), `shot dependency graph: ${edge.toShotId} cannot use a candidate still as upstream evidence`);
  assert.equal(edge.downstreamFrame?.source, "approved_input_frame", `shot dependency graph: ${edge.toShotId} requires an approved downstream start input`);
  assert.equal(edge.upstreamFrame?.status, "approved", `shot dependency graph: ${edge.fromShotId} actual frame is not approved`);
  assert.equal(edge.downstreamFrame?.status, "approved", `shot dependency graph: ${edge.toShotId} start frame is not approved`);
  assert.match(edge.upstreamFrame?.sha256 ?? "", SHA256, `shot dependency graph: ${edge.fromShotId} actual frame hash is missing`);
  assert.match(edge.downstreamFrame?.sha256 ?? "", SHA256, `shot dependency graph: ${edge.toShotId} start frame hash is missing`);
  assert.equal(edge.upstreamFrame.sha256, edge.downstreamFrame.sha256, `shot dependency graph: actual upstream last frame and downstream start frame hashes differ`);
  assert.equal(edge.actualFrameMatch, "pass", `shot dependency graph: ${edge.fromShotId} -> ${edge.toShotId} actual-frame match has not passed`);
  assert.equal(edge.transitionPreviewApproval, "approved", `shot dependency graph: ${edge.fromShotId} -> ${edge.toShotId} transition preview is not approved`);
};

export function validateShotDependencyGraph(graph, { targetShotId = null, requirePaidReady = false } = {}) {
  assert.equal(graph.schemaVersion, 1, "shot dependency graph: unsupported schemaVersion");
  assert.ok(graph.jobId, "shot dependency graph: jobId is required");
  assert.ok(Array.isArray(graph.nodes), "shot dependency graph: nodes are required");
  assert.ok(Array.isArray(graph.edges), "shot dependency graph: edges are required");
  const nodeIds = graph.nodes.map((node) => node.shotId);
  assert.equal(new Set(nodeIds).size, nodeIds.length, "shot dependency graph: shotId values must be unique");
  const nodeById = new Map(graph.nodes.map((node) => [node.shotId, node]));

  for (const node of graph.nodes) {
    assert.ok(node.shotId, "shot dependency graph: every node requires shotId");
    assert.ok(Array.isArray(node.dependsOnShotIds), `shot dependency graph: ${node.shotId} requires dependsOnShotIds`);
    assert.equal(new Set(node.dependsOnShotIds).size, node.dependsOnShotIds.length, `shot dependency graph: ${node.shotId} dependencies must be unique`);
    for (const dependencyId of node.dependsOnShotIds) assert.ok(nodeById.has(dependencyId), `shot dependency graph: ${node.shotId} depends on missing ${dependencyId}`);
    if (node.paidExecutionRequested) {
      assert.equal(node.executionMode, "paid_ai", `shot dependency graph: ${node.shotId} paid request requires paid_ai mode`);
      assert.equal(node.executionStatus, "paid_ready", `shot dependency graph: ${node.shotId} paid request is not paid_ready`);
    }
  }

  const edgeKeys = new Set();
  const incoming = new Map(graph.nodes.map((node) => [node.shotId, []]));
  for (const edge of graph.edges) {
    assert.ok(nodeById.has(edge.fromShotId), `shot dependency graph: missing upstream node ${edge.fromShotId}`);
    assert.ok(nodeById.has(edge.toShotId), `shot dependency graph: missing downstream node ${edge.toShotId}`);
    assert.notEqual(edge.fromShotId, edge.toShotId, `shot dependency graph: ${edge.toShotId} cannot depend on itself`);
    const edgeKey = `${edge.fromShotId}->${edge.toShotId}`;
    assert.equal(edgeKeys.has(edgeKey), false, `shot dependency graph: duplicate edge ${edgeKey}`);
    edgeKeys.add(edgeKey);
    incoming.get(edge.toShotId).push(edge);
  }
  assertAcyclic(graph.nodes, graph.edges);

  for (const node of graph.nodes) {
    const incomingIds = incoming.get(node.shotId).map((edge) => edge.fromShotId).sort();
    assert.deepEqual(incomingIds, [...node.dependsOnShotIds].sort(), `shot dependency graph: ${node.shotId} dependency declarations and edges differ`);
    if (!node.paidExecutionRequested) continue;
    for (const edge of incoming.get(node.shotId)) {
      const upstream = nodeById.get(edge.fromShotId);
      if (edge.continuityRequired) validateContinuityEdgeForPaidTarget(edge, upstream);
      else {
        assert.ok(["hard_cut", "independent"].includes(edge.transitionMode), `shot dependency graph: non-continuous ${edge.fromShotId} -> ${edge.toShotId} requires hard_cut or independent`);
        assert.ok(["approved", "not_applicable"].includes(edge.transitionPreviewApproval), `shot dependency graph: independent transition approval is unresolved`);
      }
    }
  }

  const requestedNodes = graph.nodes.filter((node) => node.paidExecutionRequested);
  if (graph.status === "READY_FOR_ORDERED_GENERATION") assert.ok(requestedNodes.length > 0, "shot dependency graph: READY requires at least one paid target");
  if (requirePaidReady) {
    assert.ok(targetShotId, "shot dependency graph: --target is required with --require-paid-ready");
    const target = nodeById.get(targetShotId);
    assert.ok(target, `shot dependency graph: target shot not found: ${targetShotId}`);
    assert.equal(target.paidExecutionRequested, true, `shot dependency graph: ${targetShotId} is not the approved paid target`);
    assert.ok(["READY_FOR_ORDERED_GENERATION", "GENERATION_IN_PROGRESS"].includes(graph.status), `shot dependency graph: global status does not permit paid generation`);
  }
  assert.equal(graph.distribution?.publishAllowed, false, "shot dependency graph: publishing must remain locked");
  assert.equal(graph.distribution?.activateAdsAllowed, false, "shot dependency graph: ad activation must remain locked");
  return { nodeCount: graph.nodes.length, edgeCount: graph.edges.length, requestedPaidShots: requestedNodes.map((node) => node.shotId) };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const args = process.argv.slice(2);
  const file = args[0] ? path.resolve(args[0]) : null;
  const targetIndex = args.indexOf("--target");
  const targetShotId = targetIndex >= 0 ? args[targetIndex + 1] : null;
  const requirePaidReady = args.includes("--require-paid-ready");
  assert.ok(file, "Usage: node scripts/validate-shot-dependency-graph.mjs <shot-dependency-graph.json> [--target <shot-id> --require-paid-ready]");
  const result = validateShotDependencyGraph(JSON.parse(await readFile(file, "utf8")), { targetShotId, requirePaidReady });
  console.log(`Shot dependency graph: PASS (${result.nodeCount} nodes / ${result.edgeCount} edges / paid=${result.requestedPaidShots.join(",") || "none"})`);
}
