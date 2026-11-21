import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import sharp from 'sharp';
import { unzipSync } from 'fflate';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { InMemoryTransport } from '@modelcontextprotocol/sdk/inMemory.js';
import { buildCarousel } from '../src/archive.mjs';
import { documentYAML, getSpec, parseLayout, validateDocument } from '../src/document.mjs';
import { getSpecResponse } from '../src/spec.mjs';
import { ArtifactStore, createMCPServer, downloadImage } from '../src/server.mjs';

const base = () => ({ carousel: 1, ratio: 'portrait-4-5', slides: 2, background: 'F4F0E8', requires: [], layers: [{ text: { slide: 1, at: [0.5, 0.35], string: 'Идея\nстановится каруселью', font: { design: 'system', size: 0.07, weight: 'bold' }, color: '101828' } }] });
const layout = document => documentYAML(document);

test('a project is a real archive containing editable Unicode text and inferred capabilities', async () => {
  const input = base();
  input.layers.push({ shape: { slide: 2, at: [0.5, 0.5], size: [1, 1], kind: 'rectangle', fill: 'C7FF6B' } });
  const result = await buildCarousel(layout(input));
  const entries = unzipSync(result.bytes);
  assert.deepEqual(Object.keys(entries), ['carousel.yaml']);
  const decoded = validateDocument(parseLayout(Buffer.from(entries['carousel.yaml']).toString()));
  assert.equal(decoded.layers[0].text.string, input.layers[0].text.string);
  assert.equal(decoded.layers[1].shape.kind, 'rectangle');
  assert.deepEqual(decoded.requires, ['layer.shape']);
});

test('image bytes are oriented, stripped, hashed and embedded once; unused images are excluded', async () => {
  const input = base();
  const photograph = await sharp({ create: { width: 2, height: 3, channels: 3, background: '#ff0000' } }).withMetadata({ orientation: 6 }).png().toBuffer();
  input.layers.push({ image: { slide: 1, at: [0.5, 0.7], size: [0.5, 0.3], source: 'photo_1' } });
  input.layers.push({ image: { slide: 2, at: [0.5, 0.7], size: [0.5, 0.3], source: 'photo_1' } });
  const result = await buildCarousel(layout(input), new Map([['photo_1', photograph], ['unused', photograph]]));
  const entries = unzipSync(result.bytes);
  assert.equal(Object.keys(entries).length, 2);
  assert.deepEqual(Object.keys(result.document.assets), ['photo_1']);
  const asset = result.document.assets.photo_1;
  assert.equal(asset.file, `assets/${createHash('sha256').update(entries[asset.file]).digest('hex')}.png`);
  const meta = await sharp(entries[asset.file]).metadata();
  assert.equal(meta.orientation, undefined);
  assert.equal(meta.exif, undefined);
  assert.deepEqual(asset.pixels, [3, 2]);
});

test('empty photo slots need no media and remain editable', async () => {
  const input = base();
  input.layers.push({ frame: { slide: 2, at: [0.5, 0.6], width: 0.8, preset: 'Polaroid03', photos: [{ source: null }, { source: null }, { source: null }] } });
  const result = await buildCarousel(layout(input));
  assert.equal(result.document.layers[1].frame.photos.length, 3);
  assert.equal(Object.keys(unzipSync(result.bytes)).length, 1);
});

test('invalid and silently ignored layout fields are rejected', () => {
  for (const modify of [
    d => { d.slides = 21; },
    d => { d.layers[0].text.size = [1, 1]; },
    d => { d.layers[0].text.slide = 3; },
    d => { d.layers[0].text.font.family = 'Invented@1'; },
    d => { d.layers.push({ sticker: { slide: 1, at: [0.5, 0.5], size: [0.2, 0.2], source: 'catalog:Fake/art' } }); },
    d => { d.layers.push({ image: { slide: 1, at: [0.5, 0.5], size: [0.2, 0.2], source: 'missing' } }); },
    d => { d.layers.push({ image: { slide: 1, at: [0.5, 0.5], size: [0.2, 0.2], source: 'constructor' } }); },
    d => { d.layers.push({ frame: { slide: 1, at: [0.5, 0.5], width: 0.8, preset: 'Polaroid03', photos: [{ source: null }] } }); },
    d => { d.layers.push({ image: { slide: 1, at: [0.5, 0.5], size: [0.2, 0.2], source: null, crop: [0, 0, 1, 1] } }); },
    d => { d.requires = ['unsupported.extension']; },
    d => { d.layers[0].text.font.size = Infinity; }
  ]) {
    const input = base(); modify(input);
    assert.throws(() => validateDocument(input));
  }
});

test('duplicate keys, aliases, explicit tags, block strings and multiple documents are rejected', () => {
  for (const yaml of ['slides: 1\nslides: 2', 'a: &a [1, 2]\nb: *a', 'a: !!str 12', 'text: |\n  line\n', 'a: 1\n---\na: 2']) assert.throws(() => parseLayout(yaml));
});

test('gradient requirements and stop ordering are enforced', () => {
  const input = base();
  const shape = { slide: 2, at: [0.5, 0.5], size: [1, 1], kind: 'rectangle', fill: '111111', gradient: { style: 'linear', stops: [{ at: 0, color: '111111' }, { at: 1, color: 'FFFFFF' }] } };
  input.layers.push({ shape });
  assert.deepEqual(validateDocument(input).requires, ['layer.shape', 'layer.shape.gradient']);
  shape.gradient.stops.reverse();
  assert.throws(() => validateDocument(input));
});

test('catalog search returns exact native identifiers', () => {
  const found = getSpecResponse('catalogs', 'Polaroid03').catalog;
  assert.equal(found.entries[0].id, 'Polaroid03');
  assert.equal(found.entries[0].example.layers[0].frame.photos.length, 3);
  assert.match(getSpec('catalogs', 'Caveat'), /Caveat@1/);
  assert.match(getSpec('catalogs', 'DOES_NOT_EXIST'), /No matching/);
});

test('download links expire and unrelated requests cannot retrieve stored projects', () => {
  let now = 0;
  const store = new ArtifactStore({ ttl: 10, now: () => now, capacity: 3 });
  const entry = store.add('../Тест.carousel', Uint8Array.of(1, 2, 3));
  assert.equal(entry.name, '..-Тест.carousel');
  assert.equal(store.get('unknown'), undefined);
  assert.throws(() => store.add('another', Uint8Array.of(1)));
  now = 10;
  assert.equal(store.get(entry.id), undefined);
});

test('image downloading rejects arbitrary hosts and redirects and enforces size limits', async () => {
  for (const url of ['http://files.oaiusercontent.com/image', 'https://127.0.0.1/image', 'https://files.oaiusercontent.com.evil.example/image', 'https://files.oaiusercontent.com:8443/image']) await assert.rejects(() => downloadImage({ download_url: url }));
  let options;
  const bytes = await downloadImage({ download_url: 'https://files.oaiusercontent.com/image' }, async (_url, opts) => { options = opts; return new Response(Uint8Array.of(1, 2, 3)); });
  assert.deepEqual([...bytes], [1, 2, 3]);
  assert.equal(options.redirect, 'error');
  await assert.rejects(() => downloadImage({ download_url: 'https://files.oaiusercontent.com/image' }, async () => new Response('too large', { headers: { 'content-length': String(21 * 1024 * 1024) } })));
});

test('an MCP client discovers the tools and receives a usable downloadable project', async () => {
  const store = new ArtifactStore();
  const server = createMCPServer({ publicURL: 'https://carousels.example', store });
  const client = new Client({ name: 'test', version: '1' });
  const [clientTransport, serverTransport] = InMemoryTransport.createLinkedPair();
  await Promise.all([server.connect(serverTransport), client.connect(clientTransport)]);
  try {
    const { tools } = await client.listTools();
    assert.deepEqual(tools.map(t => t.name), ['get_carousel_spec', 'validate_carousel', 'create_carousel', 'render_carousel', 'prepare_photo_upload']);
    const files = tools[2].inputSchema.properties.asset_files.items;
    assert.deepEqual(files.required, ['download_url', 'file_id']);
    for (const key of ['file_name', 'mime_type']) assert.ok(files.properties[key]);
    const result = await client.callTool({ name: 'create_carousel', arguments: { yaml: layout(base()), filename: 'Моя карусель' } });
    assert.equal(result.isError, undefined);
    assert.equal(result.structuredContent.filename, 'Моя карусель.carousel');
    const url = new URL(result.structuredContent.download_url);
    assert.equal(url.origin, 'https://carousels.example');
    assert.ok(unzipSync(store.get(url.pathname.split('/')[2]).bytes)['carousel.yaml']);
    const invalid = await client.callTool({ name: 'create_carousel', arguments: { yaml: 'slides: 0' } });
    assert.equal(invalid.isError, true);
  } finally { await client.close(); await server.close(); }
});
