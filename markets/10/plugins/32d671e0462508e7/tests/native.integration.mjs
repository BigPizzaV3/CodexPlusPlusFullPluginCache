import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import sharp from 'sharp';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import { nativeRenderer } from '../src/renderer.mjs';
import { httpServer } from '../src/server.mjs';
import { buildCarousel } from '../src/archive.mjs';
import { documentYAML } from '../src/document.mjs';
import { resourceMaps } from '../src/catalog.mjs';
import { instantiateRecipe } from '../src/recipes.mjs';

if (!process.env.CAROUSEL_RENDERER_CONFIG) throw new Error('Native integration requires CAROUSEL_RENDERER_CONFIG; this check must not silently skip rendering');
const renderer = nativeRenderer();
const output = resolve(process.env.CAROUSEL_NATIVE_TEST_OUTPUT ?? 'artifacts/native-tests');
const shape = (slide, fill, at = [.5, .5], size = [1, 1]) => ({ shape: { slide, kind: 'rectangle', at, size, fill } });

async function pixel(bytes, x, y) {
  const { data, info } = await sharp(bytes).removeAlpha().raw().toBuffer({ resolveWithObject: true });
  const start = (Math.floor(y * info.height) * info.width + Math.floor(x * info.width)) * info.channels;
  return Array.from(data.subarray(start, start + 3));
}
function near(actual, expected) { actual.forEach((channel, i) => assert.ok(Math.abs(channel - expected[i]) <= 3, `${actual} must be close to ${expected}`)); }
// ACE's ImageBlender uses Core Image's linear-light working space. The layer
// blendMode path is distinct; encoded sRGB multiplication would be a wrong oracle.
const linear = byte => { const c = byte / 255; return c <= .04045 ? c / 12.92 : ((c + .055) / 1.055) ** 2.4; };
const encoded = c => Math.round(255 * (c <= .0031308 ? c * 12.92 : 1.055 * c ** (1 / 2.4) - .055));

test('real ACE pixels and MCP image content preserve blending regions, masks, double exposure, grids and frames', { timeout: 240_000 }, async () => {
  const red = await sharp({ create: { width: 64, height: 64, channels: 3, background: '#800000' } }).png().toBuffer();
  const green = await sharp({ create: { width: 64, height: 64, channels: 3, background: '#008000' } }).png().toBuffer();
  const grid = instantiateRecipe('grids', resourceMaps.grids.get('quad'), { slide: 4, at: [.5, .27], size: [.9, .42], sources: ['red', 'green', 'green', 'red'] });
  const frame = instantiateRecipe('frames', resourceMaps.frames.get('Polaroid03'), { slide: 4, at: [.5, .76], width: .32, sources: ['red', 'green', 'red'] });
  const yaml = documentYAML({ carousel: 1, ratio: 'square-1-1', slides: 5, background: 'FFFFFF', requires: [], layers: [
    shape(1, '404040'),
    { blender: { slide: 1, at: [.25, .5], size: [.5, 1], mode: 'multiply' } },
    shape(1, '808080'),
    shape(2, '000000', [.25, .5], [.5, 1]),
    { mask: { slide: 2, at: [.5, .5], size: [1, 1], color: '000000' } },
    shape(2, '0000FF'),
    { image: { slide: 3, at: [.5, .5], size: [1, 1], source: 'red', blend: { source: 'green', mode: 'screen' } } },
    grid.layer, frame.layer,
    { sticker: { slide: 4, at: [.85, .8], size: [.2, .2], source: resourceMaps.stickers.keys().next().value } },
    shape(5, '808080'),
    { blender: { slide: 5, at: [.5, .5], size: [1, 1], mode: 'multiply' } },
    shape(5, '808080'),
    { blender: { slide: 5, at: [.5, .5], size: [1, 1], mode: 'screen' } },
    shape(5, '808080')
  ] });
  const configuration = { publicURL: 'http://127.0.0.1:0', renderer, download: async file => file.asset_name === 'red' ? red : green };
  const app = httpServer(configuration);
  await new Promise((resolve, reject) => { app.once('error', reject); app.listen(0, '127.0.0.1', resolve); });
  configuration.publicURL = `http://127.0.0.1:${app.address().port}`;
  const client = new Client({ name: 'ace-native-integration', version: '1' });
  try {
    await client.connect(new StreamableHTTPClientTransport(new URL('/mcp', configuration.publicURL)));
    const overview = await client.callTool({ name: 'get_carousel_spec', arguments: { section: 'overview' } });
    assert.equal(overview.structuredContent.capabilities.native_renderer, true);
    const result = await client.callTool({ name: 'create_carousel', arguments: { yaml, filename: 'Native compositing proof', preview_width: 360,
      asset_files: ['red', 'green'].map(name => ({ asset_name: name, file_id: name, download_url: `https://chatgpt.com/${name}.png` })) } }, undefined, { timeout: 180_000 });
    assert.notEqual(result.isError, true, JSON.stringify(result.content));
    assert.equal(result.structuredContent.preview.status, 'rendered', JSON.stringify(result.structuredContent.preview));
    assert.deepEqual(result.structuredContent.preview.warnings, []);
    assert.equal(result.structuredContent.preview.slides.length, 5);
    assert.equal(result.content.filter(item => item.type === 'image').length, 1);
    await mkdir(output, { recursive: true });
    await writeFile(resolve(output, 'compositing-preview.png'), Buffer.from(result.content.find(item => item.type === 'image').data, 'base64'));
    const rendered = [];
    for (const slide of result.structuredContent.preview.slides) {
      const response = await fetch(slide.url);
      assert.equal(response.status, 200);
      assert.equal(response.headers.get('content-type'), 'image/png');
      assert.match(response.headers.get('content-disposition'), /^inline/);
      assert.equal(response.headers.get('cache-control'), 'private, no-store');
      const bytes = Buffer.from(await response.arrayBuffer());
      rendered.push(bytes);
      await writeFile(resolve(output, `compositing-${slide.slide}.png`), bytes);
      const head = await fetch(slide.url, { method: 'HEAD' });
      assert.equal(Number(head.headers.get('content-length')), bytes.length);
      assert.equal((await head.arrayBuffer()).byteLength, 0);
    }
    const multiplied = encoded(linear(64) * linear(128));
    near(await pixel(rendered[0], .25, .5), [multiplied, multiplied, multiplied]);
    near(await pixel(rendered[0], .75, .5), [128, 128, 128]);
    near(await pixel(rendered[1], .25, .5), [0, 0, 255]);
    near(await pixel(rendered[1], .75, .5), [255, 255, 255]);
    near(await pixel(rendered[2], .5, .5), [128, 128, 0]);
    near(await pixel(rendered[3], .25, .18), [128, 0, 0]);
    near(await pixel(rendered[3], .75, .18), [0, 128, 0]);
    const chained = encoded(1 - (1 - linear(128) ** 2) * (1 - linear(128)));
    near(await pixel(rendered[4], .5, .5), [chained, chained, chained]);
    assert.equal((await fetch(result.structuredContent.download_url)).status, 200);
    await writeFile(resolve(output, 'mcp-verification.json'), JSON.stringify(result.structuredContent, null, 2));
  } finally {
    await client.close(); app.closeAllConnections(); await new Promise(resolve => app.close(resolve));
  }
});

test('every composition example renders using native fonts, frame artwork, stickers and smart grids', { timeout: 240_000 }, async () => {
  const examples = JSON.parse(await readFile(new URL('../data/examples.json', import.meta.url), 'utf8'));
  await mkdir(output, { recursive: true });
  for (const example of examples) {
    const yaml = await readFile(new URL('../' + example.file, import.meta.url), 'utf8');
    const project = await buildCarousel(yaml);
    const result = await renderer.render(project.bytes, { width: 720, slideCount: project.document.slides });
    assert.deepEqual(result.warnings, [], `${example.id} must not silently substitute fonts or resources`);
    assert.equal(result.slides.length, project.document.slides);
    await writeFile(resolve(output, `${example.id}.png`), result.sheet);
    assert.ok((await sharp(result.sheet).stats()).channels.some(channel => channel.stdev > 5), `${example.id} must not be a blank render`);
  }
});
