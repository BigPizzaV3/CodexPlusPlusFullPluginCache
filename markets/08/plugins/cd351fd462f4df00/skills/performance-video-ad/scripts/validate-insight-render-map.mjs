#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

export function validateInsightRenderMap(map) {
  assert.equal(map.schemaVersion, 1, "Insight Render Map: unsupported schemaVersion");
  assert.equal(map.renderMapVersion, 1, "Insight Render Map: unsupported version");
  assert.ok(map.jobId && map.body_family_id, "Insight Render Map: jobId and body_family_id are required");
  assert.ok(["DRAFT", "READY_FOR_HUMAN_REVIEW", "VERIFIED"].includes(map.status), "Insight Render Map: invalid status");
  assert.ok(["CONTROLLED_BATCH", "SINGLE_MASTER_EXPLORATION"].includes(map.scope), "Insight Render Map: invalid scope");
  assert.ok(Array.isArray(map.insights), "Insight Render Map: insights must be an array");
  const ids = new Set();
  for (const insight of map.insights) {
    assert.ok(insight.insight_id && !ids.has(insight.insight_id), `Insight Render Map: duplicate or missing insight_id ${insight.insight_id ?? "<missing>"}`);
    ids.add(insight.insight_id);
    assert.ok(insight.insight && ["critical", "supporting"].includes(insight.importance), `Insight Render Map ${insight.insight_id}: invalid insight`);
    assert.ok(Array.isArray(insight.source_refs) && insight.source_refs.length > 0, `Insight Render Map ${insight.insight_id}: source refs missing`);
    assert.ok(Array.isArray(insight.rendered_at), `Insight Render Map ${insight.insight_id}: rendered_at must be an array`);
    if (insight.importance === "critical" && map.status !== "DRAFT") {
      assert.ok(insight.rendered_at.length > 0, `Insight Render Map ${insight.insight_id}: critical insight is not rendered`);
      assert.ok(insight.rendered_at.some((item) => ["visual", "spoken"].includes(item.mode)), `Insight Render Map ${insight.insight_id}: critical insight needs visual or spoken evidence, not UI labels alone`);
    }
    for (const rendered of insight.rendered_at) {
      assert.ok(rendered.beat_id && rendered.evidence, `Insight Render Map ${insight.insight_id}: incomplete rendered_at entry`);
      assert.ok(["visual", "spoken", "ui", "sound"].includes(rendered.mode), `Insight Render Map ${insight.insight_id}: invalid render mode`);
    }
  }
  if (map.gate_status === "PASS") {
    assert.notEqual(map.status, "DRAFT", "Insight Render Map: DRAFT cannot declare PASS");
    assert.ok(map.insights.some((item) => item.importance === "critical"), "Insight Render Map: PASS requires critical insights");
  }
  return { insights: map.insights.length, critical: map.insights.filter((item) => item.importance === "critical").length };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-insight-render-map.mjs <insight-render-map.json>");
  const result = validateInsightRenderMap(JSON.parse(await readFile(file, "utf8")));
  console.log(`Insight Render Map: PASS (${result.insights} insights / ${result.critical} critical)`);
}
