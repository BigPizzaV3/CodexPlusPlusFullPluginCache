import test from 'node:test';
import assert from 'node:assert/strict';
import sharp from 'sharp';
import { unzipSync } from 'fflate';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import { documentYAML, parseLayout, validateDocument } from '../src/document.mjs';
import { ArtifactStore, UploadStore, httpServer } from '../src/server.mjs';

const layout = (...sources) => documentYAML({ carousel: 1, ratio: 'portrait-4-5', slides: 1, background: 'F4F0E8', requires: [],
  layers: sources.map((source, index) => ({ image: { slide: 1, at: [0.5, 0.3 + index * 0.4], size: [0.5, 0.3], source } })) });
const text = result => result.content.map(part => part.text ?? '').join('\n');
const put = (url, body) => fetch(url, { method: 'PUT', body });

test('photographs from the user’s computer reach a project through one-time upload links', async () => {
  const store = new ArtifactStore(), uploads = new UploadStore({ limit: 64 * 1024 });
  const configuration = { publicURL: 'http://127.0.0.1:0', store, uploads, download: async () => { throw new Error('nothing is downloaded for uploads'); } };
  const app = httpServer(configuration);
  await new Promise((resolve, reject) => { app.once('error', reject); app.listen(0, '127.0.0.1', resolve); });
  configuration.publicURL = `http://127.0.0.1:${app.address().port}`;
  const client = new Client({ name: 'upload-test', version: '1' });
  try {
    await client.connect(new StreamableHTTPClientTransport(new URL(`${configuration.publicURL}/mcp`)));
    const tool = (await client.listTools()).tools.find(entry => entry.name === 'prepare_photo_upload');
    assert.equal(tool.annotations.readOnlyHint, false);
    assert.equal(tool.annotations.destructiveHint, false);
    assert.ok(tool.title);
    const prepared = await client.callTool({ name: 'prepare_photo_upload', arguments: { asset_names: ['run', 'spare', 'big'] } });
    assert.equal(prepared.isError, undefined);
    const slots = Object.fromEntries(prepared.structuredContent.uploads.map(slot => [slot.asset_name, slot]));
    for (const slot of Object.values(slots)) {
      assert.equal(new URL(slot.upload_url).origin, configuration.publicURL);
      assert.equal(new URL(slot.upload_url).pathname, `/uploads/${slot.upload_id}`);
    }
    assert.equal(prepared.structuredContent.max_bytes, 64 * 1024);
    assert.ok(Date.parse(prepared.structuredContent.expires_at) > Date.now());
    assert.ok((await client.callTool({ name: 'prepare_photo_upload', arguments: { asset_names: ['twin', 'twin'] } })).isError);

    const photograph = await sharp({ create: { width: 2, height: 3, channels: 3, background: '#ff0000' } }).withMetadata({ orientation: 6 }).jpeg().toBuffer();
    const accepted = await put(slots.run.upload_url, photograph);
    assert.equal(accepted.status, 200);
    assert.deepEqual(await accepted.json(), { upload_id: slots.run.upload_id, asset_name: 'run', format: 'jpeg', bytes: photograph.byteLength });
    assert.equal((await put(slots.run.upload_url, photograph)).status, 409);
    // A rejected file leaves the link open, so the caller can send the right one.
    assert.equal((await put(slots.spare.upload_url, Buffer.from('not a photograph'))).status, 415);
    assert.equal((await put(slots.spare.upload_url, photograph)).status, 200);
    assert.equal((await put(slots.big.upload_url, Buffer.alloc(64 * 1024 + 1))).status, 413);
    assert.equal((await put(`${configuration.publicURL}/uploads/${'0'.repeat(48)}`, photograph)).status, 404);
    assert.equal((await fetch(slots.spare.upload_url)).status, 405);

    const created = await client.callTool({ name: 'create_carousel', arguments: { yaml: layout('run'), photo_uploads: [slots.run.upload_id, slots.spare.upload_id] } });
    assert.equal(created.isError, undefined, text(created));
    const files = unzipSync(new Uint8Array(await (await fetch(created.structuredContent.download_url)).arrayBuffer()));
    const document = validateDocument(parseLayout(Buffer.from(files['carousel.yaml']).toString('utf8')));
    assert.deepEqual(Object.keys(document.assets), ['run']);
    assert.deepEqual(document.assets.run.pixels, [3, 2]);
    assert.match(document.assets.run.file, /^assets\/[a-f0-9]{64}\.jpg$/);
    const meta = await sharp(files[document.assets.run.file]).metadata();
    assert.equal(meta.orientation, undefined);
    assert.equal(meta.exif, undefined);
    assert.deepEqual(Object.keys(files).sort(), [document.assets.run.file, 'carousel.yaml']);

    const empty = await client.callTool({ name: 'create_carousel', arguments: { yaml: layout('big'), photo_uploads: [slots.big.upload_id] } });
    assert.ok(empty.isError);
    assert.match(text(empty), /upload_url/);
    const unknown = await client.callTool({ name: 'create_carousel', arguments: { yaml: layout('run'), photo_uploads: ['0'.repeat(48)] } });
    assert.ok(unknown.isError);
    assert.match(text(unknown), /prepare_photo_upload/);
    const twice = await client.callTool({ name: 'create_carousel', arguments: { yaml: layout('run'), photo_uploads: [slots.run.upload_id], asset_files: [{ download_url: 'https://files.oaiusercontent.com/run', file_id: 'file-1', asset_name: 'run' }] } });
    assert.ok(twice.isError);
    assert.match(text(twice), /duplicate asset_name run/);
  } finally {
    await client.close();
    app.closeAllConnections();
    await new Promise(resolve => app.close(resolve));
  }
});

test('upload slots expire, refuse a full store, and only take distinct names', async () => {
  let now = 0;
  const uploads = new UploadStore({ ttl: 10, capacity: 1024, now: () => now });
  const photograph = await sharp({ create: { width: 4, height: 4, channels: 3, background: '#00ff00' } }).png().toBuffer();
  assert.throws(() => uploads.reserve(['a', 'a']), /duplicate/);
  const [first, second] = uploads.reserve(['a', 'b']);
  await uploads.receive(first.id, photograph);
  assert.equal(uploads.get(first.id).bytes.byteLength, photograph.byteLength);
  await assert.rejects(uploads.receive(second.id, Buffer.concat([photograph, Buffer.alloc(1024)])), error => error.status === 507);
  now = 10;
  assert.equal(uploads.get(first.id), undefined);
  await assert.rejects(uploads.receive(second.id, photograph), error => error.status === 404);
});
