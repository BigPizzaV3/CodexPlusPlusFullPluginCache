// Synthetic fixture only. Pass a new evidence directory. Every owned process closes in finally.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import http from 'node:http';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';
import png from 'pngjs';
import jsQR from 'jsqr';
import { digest } from '../scripts/pwaify.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
if (!process.argv[2]) throw new Error('Pass a new absolute fixture evidence directory');
const evidence = path.resolve(process.argv[2]);
await fs.mkdir(evidence);
const input = path.join(evidence, 'input'), output = path.join(evidence, 'prepared');
await fs.mkdir(input);
const html = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Device It fixture</title><link rel="stylesheet" href="style.css"></head><body><main><h1>Device It fixture</h1><p>Local static shell with offline interaction.</p><button id="counter">Clicks: 0</button><p id="status">Ready</p></main><script src="app.js"></script></body></html>';
await fs.writeFile(path.join(input, 'index.html'), html);
await fs.writeFile(path.join(input, 'app.js'), "let clicks=0;document.querySelector('#counter').onclick=()=>{document.querySelector('#counter').textContent='Clicks: '+(++clicks);document.querySelector('#status').textContent='Interaction verified'};");
await fs.writeFile(path.join(input, 'style.css'), 'body{font:18px system-ui;color:#14223c;background:#fff;padding:50px}main{max-width:600px;margin:auto}button{font:inherit;padding:12px 20px;background:#2155cd;color:#fff;border:0;border-radius:6px}');
await fs.writeFile(path.join(input, 'private.json'), '{"synthetic":"never copied"}');
const assets = path.join(evidence, 'public-assets.json');
await fs.writeFile(assets, '["index.html","app.js","style.css"]');
const originalHash = digest(await fs.readFile(path.join(input, 'index.html')));

function run(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [path.join(root, 'scripts/run.mjs'), ...args], { cwd: root, stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = '', stderr = '';
    child.stdout.on('data', b => stdout += b); child.stderr.on('data', b => stderr += b);
    child.on('error', reject); child.on('close', code => resolve({ code, stdout, stderr }));
  });
}
const made = await run(['prepare', '--dist', input, '--out', output, '--assets', assets, '--name', 'Device It fixture']);
assert.equal(made.code, 0, made.stderr);
await fs.writeFile(path.join(evidence, 'prepare.json'), made.stdout);
assert.equal(digest(await fs.readFile(path.join(input, 'index.html'))), originalHash);
const inventory = JSON.parse(await fs.readFile(path.join(output, 'device-it-build.json')));
let preview, previewReceipt, browser, probes, foreign;
const cleanup = {};
const result = { preparedFromPackage: root, platform: process.platform, arch: process.arch, node: process.version, assertions: [], cleanup };
const pass = name => result.assertions.push(name);
const closeServer = server => new Promise(resolve => { if (!server) return resolve(); server.closeAllConnections(); server.close(resolve); });
async function listen(server) { await new Promise(resolve => server.listen(0, '127.0.0.1', resolve)); return `http://127.0.0.1:${server.address().port}/`; }
try {
  preview = spawn(process.execPath, [path.join(root, 'scripts/run.mjs'), 'preview', '--dir', output, '--qr', path.join(evidence, 'preview-qr.png')], { cwd: root, stdio: ['ignore', 'pipe', 'pipe'] });
  previewReceipt = await new Promise((resolve, reject) => {
    let text = '', errors = '';
    const timer = setTimeout(() => reject(new Error('Preview did not start')), 10000);
    preview.stderr.on('data', b => errors += b);
    preview.stdout.on('data', b => { text += b; if (text.includes('\n')) { clearTimeout(timer); try { resolve(JSON.parse(text.split('\n')[0])); } catch (e) { reject(e); } } });
    preview.on('error', e => { clearTimeout(timer); reject(e); });
    preview.on('close', code => { if (!text) { clearTimeout(timer); reject(new Error(`Preview closed ${code}: ${errors}`)); } });
  });
  await fs.writeFile(path.join(evidence, 'preview.json'), JSON.stringify(previewReceipt, null, 2));
  const qr = png.PNG.sync.read(await fs.readFile(path.join(evidence, 'preview-qr.png')));
  assert.equal(jsQR(new Uint8ClampedArray(qr.data), qr.width, qr.height).data, previewReceipt.url);
  pass('QR PNG decodes to the running loopback preview URL');
  const checked = await run(['verify', '--url', previewReceipt.url, '--expect-text', 'Device It fixture', '--report', path.join(evidence, 'verify.json'), '--screenshot', path.join(evidence, 'offline-shell.png')]);
  assert.equal(checked.code, 0, checked.stdout + checked.stderr);
  assert.equal(JSON.parse(checked.stdout).browserClosed, true);
  pass('Packaged verifier proves manifest/icons/activation/exact bytes/offline shell and closes browser');
  const failed = await run(['verify', '--url', previewReceipt.url, '--expect-text', 'Device It fixture', '--report', path.join(evidence, 'verify-failure.json'), '--screenshot', path.join(evidence, 'does-not-exist', 'no.png')]);
  const failureReport = JSON.parse(failed.stdout);
  assert.equal(failed.code, 1); assert.equal(failureReport.ok, false); assert.equal(failureReport.browserStarted, true); assert.equal(failureReport.browserClosed, true);
  pass('Verifier closes browser and reports failure when evidence output fails after launch');
  browser = await chromium.launch({ headless: true });
  result.browserVersion = browser.version();
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(previewReceipt.url);
  await page.waitForFunction(() => navigator.serviceWorker.controller);
  await page.locator('#counter').click(); assert.equal(await page.locator('#counter').innerText(), 'Clicks: 1');
  await context.setOffline(true); await page.reload();
  await page.locator('#counter').click(); assert.equal(await page.locator('#status').innerText(), 'Interaction verified');
  await page.screenshot({ path: path.join(evidence, 'offline-interaction.png') });
  await context.close();
  pass('Fixture button works online and after offline reload');

  let foreignHits = 0;
  foreign = http.createServer((req, res) => { foreignHits++; res.writeHead(200, { 'Access-Control-Allow-Origin': '*', 'Cache-Control': 'private, no-store' }); res.end('synthetic off-origin private response'); });
  const foreignURL = await listen(foreign);
  const hits = [];
  probes = http.createServer(async (req, res) => {
    hits.push({ method: req.method, path: req.url, auth: Boolean(req.headers.authorization) });
    if (req.url === '/probe-setup') { res.writeHead(200, { 'Content-Type': 'text/html' }); res.end('<html><body>setup</body></html>'); return; }
    if (req.url.startsWith('/api/') || req.url.startsWith('/private/') || req.url.includes('?') || req.headers.authorization) { res.writeHead(200, { 'Content-Type': 'text/plain', 'Cache-Control': 'private, no-store' }); res.end('synthetic private response'); return; }
    const rel = req.url === '/' ? 'index.html' : req.url.slice(1);
    if (!inventory.publicAssets.includes(rel)) { res.writeHead(404).end(); return; }
    try {
      const type = rel.endsWith('.js') ? 'text/javascript' : rel.endsWith('.html') ? 'text/html' : rel.endsWith('.css') ? 'text/css' : rel.endsWith('.png') ? 'image/png' : 'application/json';
      res.writeHead(200, { 'Content-Type': type }); res.end(await fs.readFile(path.join(output, rel)));
    } catch { res.writeHead(500).end(); }
  });
  const probeURL = await listen(probes);
  const probeContext = await browser.newContext();
  const probePage = await probeContext.newPage();
  await probePage.goto(new URL('probe-setup', probeURL).href);
  await probePage.evaluate(async () => (await caches.open('unrelated-fixture-cache')).put('/unrelated-marker', new Response('preserve')));
  await probePage.goto(probeURL);
  await probePage.waitForFunction(() => navigator.serviceWorker.controller);
  const responses = await probePage.evaluate(async foreignURL => {
    const targets = [['/api/private', {}], ['/private/account', {}], ['/api/mutate', { method: 'POST', body: 'synthetic' }], ['/index.html?session=synthetic', {}], ['/app.js', { headers: { Authorization: 'fixture-only' } }], [foreignURL, {}]];
    const texts = [];
    for (const [url, opts] of targets) texts.push(await (await fetch(url, opts)).text());
    return texts;
  }, foreignURL);
  assert.deepEqual(responses.slice(0, 5), Array(5).fill('synthetic private response'));
  assert.equal(responses[5], 'synthetic off-origin private response');
  assert.equal(foreignHits, 1);
  const cacheState = await probePage.evaluate(async () => {
    const result = {};
    for (const name of await caches.keys()) result[name] = (await (await caches.open(name)).keys()).map(r => r.url);
    return result;
  });
  const owned = Object.entries(cacheState).filter(([name]) => name.startsWith('device-it:'));
  assert.equal(owned.length, 1);
  assert.deepEqual(owned[0][1].sort(), inventory.precache.map(x => new URL(x.file, probeURL).href).sort());
  assert.deepEqual(cacheState['unrelated-fixture-cache'], [new URL('unrelated-marker', probeURL).href]);
  await probeContext.setOffline(true);
  const denied = await probePage.evaluate(async foreignURL => {
    const urls = ['/api/private', '/private/account', '/index.html?session=synthetic', '/unknown/deep', foreignURL];
    return Promise.all(urls.map(async url => { try { await fetch(url); return false; } catch { return true; } }));
  }, foreignURL);
  assert.ok(denied.every(Boolean));
  await fs.writeFile(path.join(evidence, 'cache-boundary.json'), JSON.stringify({ responses, hits, foreignHits, cacheState, offlineUncachedRequestsRejected: denied }, null, 2));
  pass('API/private/POST/query/Authorization/off-origin requests bypass static cache; uncached offline requests fail');
  pass('Exact cache unchanged after probes; unrelated cache survives activation');
  await probeContext.close();
  // The independent fixture stays alive while the actual preview process shuts down.
  const exited = new Promise(resolve => preview.once('close', resolve));
  preview.kill('SIGTERM'); assert.equal(await exited, 0);
  await assert.rejects(fetch(previewReceipt.url));
  assert.equal(await (await fetch(foreignURL)).text(), 'synthetic off-origin private response');
  cleanup.previewStopped = true; cleanup.unrelatedServerSurvived = true;
  pass('Stopping owned preview closes its listener while unrelated fixture server survives');
  result.ok = true;
} catch (error) {
  result.ok = false; result.error = error.stack; process.exitCode = 1;
} finally {
  if (browser) { await browser.close(); cleanup.browserClosed = true; }
  if (preview && preview.exitCode === null) {
    const exited = new Promise(resolve => preview.once('close', resolve));
    preview.kill('SIGTERM'); await exited;
  }
  await closeServer(probes); await closeServer(foreign);
  cleanup.probeServerStopped = !probes?.listening; cleanup.foreignServerStopped = !foreign?.listening;
  if (previewReceipt) { try { await fetch(previewReceipt.url); cleanup.previewListenerClosed = false; } catch { cleanup.previewListenerClosed = true; } }
  await fs.writeFile(path.join(evidence, 'result.json'), JSON.stringify(result, null, 2) + '\n');
}
console.log(JSON.stringify(result, null, 2));
