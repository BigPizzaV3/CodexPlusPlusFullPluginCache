import test from 'node:test';
import assert from 'node:assert/strict';
import sharp from 'sharp';
import { unzipSync } from 'fflate';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { InMemoryTransport } from '@modelcontextprotocol/sdk/inMemory.js';
import { createMCPServer, ArtifactStore } from '../src/server.mjs';
import { contactSheet } from '../src/renderer.mjs';

const yaml = JSON.stringify({ carousel: 1, ratio: 'square-1-1', slides: 1, background: 'FFFFFF', requires: [], layers: [{ shape: { slide: 1, at: [.5, .5], size: [.5, .5], kind: 'rectangle', fill: 'FF0000' } }] });
async function connected(renderer, store, body) {
  const server = createMCPServer({ publicURL: 'https://preview.test', renderer, store });
  const client = new Client({ name: 'preview-tests', version: '1' });
  const [a, b] = InMemoryTransport.createLinkedPair();
  await Promise.all([server.connect(a), client.connect(b)]);
  try { await body(client); } finally { await client.close(); await server.close(); }
}

test('creation returns native image content and preserves the editable archive; explicit skip does not render', async () => {
  let calls = 0;
  const png = await sharp({ create: { width: 360, height: 360, channels: 3, background: 'red' } }).png().toBuffer();
  const renderer = { metadata: { engine: 'test-worker' }, render: async (bytes, options) => {
    calls++;
    assert.ok(unzipSync(bytes)['carousel.yaml']);
    assert.equal(options.width, 360);
    return { sheet: png, slides: [{ file: 'slide-01.png', slide: 1, width: 360, height: 360, bytes: png }], engine: { engine: 'test-worker' }, warnings: [] };
  } };
  const store = new ArtifactStore();
  await connected(renderer, store, async client => {
    const overview = await client.callTool({ name: 'get_carousel_spec', arguments: { section: 'overview' } });
    assert.equal(overview.structuredContent.capabilities.native_renderer, true);
    const result = await client.callTool({ name: 'create_carousel', arguments: { yaml, preview_width: 360 } });
    assert.equal(result.structuredContent.preview.status, 'rendered');
    assert.equal(result.structuredContent.preview.slides.length, 1);
    assert.deepEqual(Buffer.from(result.content.find(c => c.type === 'image').data, 'base64'), png);
    assert.equal(store.files.size, 3);
    assert.equal(result.structuredContent.visual_check, 'native preview rendered; visual review pending');
    const skipped = await client.callTool({ name: 'create_carousel', arguments: { yaml, preview: false } });
    assert.equal(skipped.structuredContent.preview.status, 'skipped');
    assert.equal(calls, 1);
    const rendered = await client.callTool({ name: 'render_carousel', arguments: { yaml, width: 360 } });
    assert.equal(rendered.structuredContent.preview.status, 'rendered');
    assert.equal(calls, 2);
  });
});

test('renderer failure is explicit and does not lose a successfully packaged file', async () => {
  await connected({ metadata: {}, render: async () => { throw new Error('Worker is unavailable'); } }, new ArtifactStore(), async client => {
    const result = await client.callTool({ name: 'create_carousel', arguments: { yaml } });
    assert.notEqual(result.isError, true);
    assert.ok(result.structuredContent.download_url);
    assert.equal(result.structuredContent.preview.status, 'failed');
    assert.match(result.structuredContent.preview.reason, /Worker/);
    assert.equal(result.content.some(c => c.type === 'image'), false);
    assert.equal((await client.callTool({ name: 'render_carousel', arguments: { yaml } })).isError, true);
  });
  await connected(null, new ArtifactStore(), async client => {
    assert.equal((await client.callTool({ name: 'create_carousel', arguments: { yaml } })).structuredContent.preview.status, 'unavailable');
    assert.equal((await client.callTool({ name: 'render_carousel', arguments: { yaml } })).isError, true);
  });
});

test('preview storage is atomic on capacity failure and expires PNGs with projects', () => {
  let now = 10;
  const store = new ArtifactStore({ capacity: 6, ttl: 100, now: () => now });
  store.add('work', Buffer.from('zip'));
  const png = name => ({ name, bytes: Buffer.from('png'), mimeType: 'image/png' });
  assert.throws(() => store.addMany([png('a'), png('b')]), /storage is full/);
  assert.equal(store.files.size, 1);
  const [image] = store.addMany([png('a')]);
  assert.equal(image.name, 'a.png');
  assert.equal(store.get(image.id).mimeType, 'image/png');
  now = 111;
  assert.equal(store.get(image.id), undefined);
  assert.equal(store.files.size, 0);
});

test('contact sheet includes every slide in reading order including the final partial row', async () => {
  const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#00ffff'];
  const slides = await Promise.all(colors.map(async color => ({ width: 360, height: 360, bytes: await sharp({ create: { width: 360, height: 360, channels: 3, background: color } }).png().toBuffer() })));
  const { data, info } = await sharp(await contactSheet(slides)).removeAlpha().raw().toBuffer({ resolveWithObject: true });
  for (let i = 0; i < colors.length; i++) {
    const x = 166 + (i % 4) * 316, y = 166 + Math.floor(i / 4) * 344;
    const offset = (y * info.width + x) * info.channels;
    assert.equal('#' + Buffer.from(data.subarray(offset, offset + 3)).toString('hex'), colors[i]);
  }
});
