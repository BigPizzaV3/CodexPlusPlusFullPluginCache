import test from 'node:test';
import assert from 'node:assert/strict';
import { validateBrief, validateOutput, buildManifest, handleRpc } from './src/core.js';

test('positive: complete product brief is concept-ready', () => {
  const result = validateBrief({ brandProductName: 'Donat Genduy', productDetailsUSP: 'Topping warna-warni, empuk, jumbo, hemat', targetAudience: 'Anak-anak dan keluarga', language: 'Bahasa Indonesia, Sunda ringan' });
  assert.equal(result.validForConcept, true);
  assert.equal(result.missingRequired.length, 0);
});

test('positive: references are reported without claiming visual inspection', () => {
  const result = validateBrief({ brandProductName: 'Produk A', hasCharacterReference: true, hasProductReference: true });
  assert.equal(result.referenceStatus.character, 'provided');
  assert.equal(result.referenceStatus.product, 'provided');
});

test('positive: a correctly structured three-scene package passes', () => {
  const result = validateOutput({
    storyboards: [1,2,3].map(n => ({ scene: n, grid: '2x3', panels: [1,2,3,4,5,6] })),
    videoPrompts: ['one','two','three'], characterContinuityLock: 'Same fictional talent', productContinuityLock: 'Same supplied product reference', negativePrompt: 'No identity drift', storySummary: 'Discovery, experience, payoff', productionChecklist: ['review']
  });
  assert.equal(result.valid, true);
});

test('positive: manifest calculates total duration', () => {
  const result = buildManifest({ brandProductName: 'Produk A', storyboardCount: 3, sceneDurationSeconds: 10 });
  assert.equal(result.format.totalDurationSeconds, 30);
  assert.equal(result.deliverables.panelsPerStoryboard, 6);
});

test('positive: tools/list advertises all tools with explicit safety annotations', async () => {
  const result = await handleRpc({ jsonrpc: '2.0', id: 1, method: 'tools/list' });
  const tools = result.result.tools;
  assert.deepEqual(tools.map(t => t.name), ['validate_product_brief','validate_production_output','build_production_manifest']);
  for (const tool of tools) {
    assert.deepEqual(tool.annotations, {
      readOnlyHint: true,
      destructiveHint: false,
      openWorldHint: false
    }, `${tool.name} must publish all three explicit annotation booleans`);
  }
});

test('negative: missing product facts are not marked concept-ready', () => {
  const result = validateBrief({ brandProductName: 'Donat' });
  assert.equal(result.validForConcept, false);
  assert.ok(result.missingRequired.includes('Detail produk dan USP'));
});

test('negative: incomplete storyboard/video counts fail output validation', () => {
  const result = validateOutput({ storyboards: [{ panels: [1,2] }], videoPrompts: ['one'] });
  assert.equal(result.valid, false);
  assert.ok(result.issues.some(x => x.includes('exactly 3 storyboards')));
  assert.ok(result.issues.some(x => x.includes('exactly 3 video prompts')));
});

test('negative: unknown tool returns an MCP tool error', async () => {
  const result = await handleRpc({ jsonrpc: '2.0', id: 3, method: 'tools/call', params: { name: 'invented_tool', arguments: {} } });
  assert.equal(result.result.isError, true);
});
