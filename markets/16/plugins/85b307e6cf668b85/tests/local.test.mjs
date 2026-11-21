import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import http from 'node:http';
import { prepare, publicPath, digest } from '../scripts/pwaify.mjs';
import { createPreview } from '../scripts/preview.mjs';
import { writeQR, localURL } from '../scripts/qr.mjs';
import { options } from '../scripts/options.mjs';
import png from 'pngjs';
import jsQR from 'jsqr';

async function fixture(t) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), 'device-it-test-'));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  const dist = path.join(root, 'input');
  await fs.mkdir(dist);
  await fs.writeFile(path.join(dist, 'index.html'), '<!doctype html><html><head><title>Fixture</title></head><body><h1>Local fixture</h1><script src="app.js"></script></body></html>');
  await fs.writeFile(path.join(dist, 'app.js'), 'document.body.dataset.ready = "yes";');
  await fs.writeFile(path.join(dist, 'private.json'), '{"fixtureOnly":true}');
  const assets = path.join(root, 'assets.json');
  await fs.writeFile(assets, '["index.html","app.js"]');
  return { root, dist, assets, out: path.join(root, 'output'), name: 'Fixture' };
}

test('copies only approved static files and preserves input bytes', async t => {
  const f = await fixture(t);
  const before = await fs.readFile(path.join(f.dist, 'index.html'));
  const result = await prepare(f);
  assert.equal(result.ok, true);
  assert.deepEqual(await fs.readFile(path.join(f.dist, 'index.html')), before);
  await assert.rejects(fs.stat(path.join(f.out, 'private.json')), { code: 'ENOENT' });
  const inventory = JSON.parse(await fs.readFile(path.join(f.out, 'device-it-build.json')));
  for (const entry of inventory.precache) assert.equal(digest(await fs.readFile(path.join(f.out, entry.file))), entry.sha256);
  for (const [file, size] of [['icon-192.png', 192], ['icon-512.png', 512], ['icon-maskable-512.png', 512], ['apple-touch-icon-180.png', 180]]) {
    const icon = png.PNG.sync.read(await fs.readFile(path.join(f.out, 'device-it', file)));
    assert.equal(icon.width, size); assert.equal(icon.height, size);
  }
});

test('refuses every existing output and nested output without changes', async t => {
  const f = await fixture(t);
  await fs.mkdir(f.out);
  await fs.writeFile(path.join(f.out, 'keep.txt'), 'preserve');
  await assert.rejects(prepare(f), /already exists/);
  assert.equal(await fs.readFile(path.join(f.out, 'keep.txt'), 'utf8'), 'preserve');
  await assert.rejects(prepare({ ...f, out: path.join(f.dist, 'new') }), /non-nested/);
});

test('preserves existing manifests, service workers and registration code', async t => {
  for (const name of ['manifest.webmanifest', 'manifest.json', 'sw.js', 'service-worker.js']) {
    const f = await fixture(t);
    await fs.writeFile(path.join(f.dist, name), 'keep');
    await assert.rejects(prepare(f), /already contains PWA/);
    assert.equal(await fs.readFile(path.join(f.dist, name), 'utf8'), 'keep');
  }
  const f = await fixture(t);
  await fs.writeFile(path.join(f.dist, 'app.js'), "navigator.serviceWorker.register('/custom-worker.js');");
  await assert.rejects(prepare(f), /Existing PWA registration/);
});

test('rejects private, traversal, unsupported and duplicate paths', async t => {
  for (const file of ['../secret.js', '/app.js', 'a/../../b.js', '.env', 'private/a.js', 'api/data.js', 'secrets/key.js', 'local-state/a.js', 'node_modules/a.js', 'data.json', 'app.js.map', 'a\\b.js', 'https://remote/a.js']) assert.throws(() => publicPath(file));
  const f = await fixture(t);
  await fs.writeFile(f.assets, '["index.html","index.html"]');
  await assert.rejects(prepare(f), /Duplicate/);
});

test('rejects symlinks, malformed HTML and invalid theme before writing', async t => {
  const f = await fixture(t);
  await fs.symlink('app.js', path.join(f.dist, 'link.js'));
  await fs.writeFile(f.assets, '["index.html","link.js"]');
  await assert.rejects(prepare(f), /Symlink/);
  await fs.writeFile(f.assets, '["index.html"]');
  await assert.rejects(prepare({ ...f, theme: 'red" onclick=' }), /six-digit/);
  await fs.writeFile(path.join(f.dist, 'index.html'), '<p>Missing head and body</p>');
  await assert.rejects(prepare(f), /head\/body/);
  await assert.rejects(fs.stat(f.out), { code: 'ENOENT' });
});

test('preview serves only inventory and rejects API, query, private and POST requests', async t => {
  const f = await fixture(t); await prepare(f);
  const p = await createPreview({ dir: f.out });
  t.after(() => { p.server.closeAllConnections(); return new Promise(resolve => p.server.close(resolve)); });
  assert.equal((await fetch(p.url)).status, 200);
  for (const target of ['api/private', 'private.json', 'index.html?token=fixture', '%2e%2e/package.json']) assert.equal((await fetch(new URL(target, p.url))).status, 404);
  assert.equal((await fetch(p.url, { method: 'POST' })).status, 403);
  // Node fetch rewrites Host; use the HTTP client to exercise the actual wire header.
  const untrustedHostStatus = await new Promise((resolve, reject) => {
    http.get(p.url, { headers: { Host: 'untrusted.invalid' } }, response => {
      response.resume();
      resolve(response.statusCode);
    }).on('error', reject);
  });
  assert.equal(untrustedHostStatus, 403);
  assert.match((await fetch(p.url)).headers.get('content-security-policy'), /connect-src 'self'/);
});

test('QR round-trips local URL and refuses overwrite or remote target', async t => {
  const f = await fixture(t), file = path.join(f.root, 'qr.png');
  const url = 'http://127.0.0.1:45678/';
  await writeQR(url, file);
  const image = png.PNG.sync.read(await fs.readFile(file));
  assert.equal(jsQR(new Uint8ClampedArray(image.data), image.width, image.height).data, url);
  await assert.rejects(writeQR(url, file), { code: 'EEXIST' });
  await assert.rejects(writeQR('https://example.com/', path.join(f.root, 'no.png')), /local HTTP/);
});

test('unknown and legacy deployment arguments are rejected', () => {
  assert.throws(() => options(['--driver', 'cloudflare'], ['dist', 'out']), /Unknown/);
  assert.throws(() => options(['--dist', 'one', '--dist', 'two'], ['dist']), /duplicate/);
});

// Loopback operation must not depend on OS permission to enumerate LAN interfaces.
test('loopback QR validation works when interface enumeration is unavailable', () => {
  const original = os.networkInterfaces;
  os.networkInterfaces = () => { throw new Error('restricted host'); };
  try {
    assert.equal(localURL('http://127.0.0.1:8080/').hostname, '127.0.0.1');
    assert.equal(localURL('http://localhost:8080/').hostname, 'localhost');
    assert.throws(() => localURL('http://192.168.1.12:8080/'), /Cannot verify a LAN address/);
    assert.throws(() => localURL('https://localhost/'), /local HTTP URL/);
    assert.throws(() => localURL('http://localhost/?secret=x'), /local HTTP URL/);
  } finally { os.networkInterfaces = original; }
});
