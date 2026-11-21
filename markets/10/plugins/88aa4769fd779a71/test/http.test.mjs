import test from 'node:test';
import assert from 'node:assert/strict';
import { once } from 'node:events';
import { connect } from 'node:net';
import { createHttpServer, closeHttpServer } from '../src/http.mjs';

const html = text => `<!doctype html><html><body>${text}</body></html>`;

async function listen(t, options) {
  const server = createHttpServer(options);
  server.listen(0, '127.0.0.1');
  await once(server, 'listening');
  t.after(() => closeHttpServer(server, { graceMs: 0 }));
  return { server, base: `http://127.0.0.1:${server.address().port}` };
}

test('missing or incomplete UI prevents startup before accepting requests', () => {
  assert.throws(() => createHttpServer({ readHtml() { throw Object.assign(new Error('missing asset'), { code: 'ENOENT' }); } }), /Run npm run build/);
  for (const incomplete of ['', '<html>', '<html>/* BUILD_SCRIPT */</html>']) {
    assert.throws(() => createHttpServer({ readHtml: () => incomplete }), /Run npm run build/);
  }
});

test('lost UI returns 503 for readiness, preview and MCP; restored builds reload without restart', async t => {
  let current = html('first build');
  const { base } = await listen(t, { readHtml: () => {
    if (current === null) throw Object.assign(new Error('internal asset path'), { code: 'ENOENT' });
    return current;
  } });
  assert.equal(await (await fetch(base)).text(), current);
  current = null;
  for (const path of ['/', '/health', '/mcp']) {
    const response = await fetch(`${base}${path}`);
    assert.equal(response.status, 503);
    assert.equal(response.headers.get('retry-after'), '5');
    assert.deepEqual(await response.json(), { status: 'unavailable' });
  }
  current = html('second build');
  assert.equal(await (await fetch(base)).text(), current);
  const response = await fetch(`${base}/health`);
  assert.equal(response.status, 200);
  assert.equal((await response.json()).status, 'ok');
});

test('slow headers and unfinished bodies receive 408 within the configured deadlines', { timeout: 19000 }, async t => {
  const { base } = await listen(t, { readHtml: () => html('ready') });
  const url = new URL(base);
  const unfinished = text => new Promise((resolve, reject) => {
    const socket = connect(Number(url.port), '127.0.0.1');
    t.after(() => socket.destroy());
    let response = '';
    socket.setTimeout(18000, () => socket.destroy(new Error('Server did not enforce its request deadline.')));
    socket.on('connect', () => socket.write(text));
    socket.on('data', chunk => { response += chunk; });
    socket.on('error', reject);
    socket.on('end', () => resolve(response));
  });
  const responses = await Promise.all([
    unfinished(`GET / HTTP/1.1\r\nHost: ${url.host}\r\n`),
    unfinished(`POST /mcp HTTP/1.1\r\nHost: ${url.host}\r\nContent-Type: application/json\r\nContent-Length: 10\r\n\r\n{`)
  ]);
  for (const response of responses) assert.match(response, /^HTTP\/1.1 408/);
  assert.equal((await fetch(`${base}/health`)).status, 200);
});

test('shutdown closes an unfinished request at the grace deadline', { timeout: 2500 }, async t => {
  const { server, base } = await listen(t, { readHtml: () => html('ready') });
  const url = new URL(base);
  const socket = connect(Number(url.port), '127.0.0.1');
  t.after(() => socket.destroy());
  socket.on('error', () => {});
  await once(socket, 'connect');
  const received = once(server, 'request');
  socket.write(`POST /mcp HTTP/1.1\r\nHost: ${url.host}\r\nContent-Type: application/json\r\nContent-Length: 10\r\n\r\n{`);
  await received;
  const closed = new Promise(resolve => socket.once('close', resolve));
  const started = performance.now();
  await closeHttpServer(server, { graceMs: 40 });
  await closed;
  const elapsed = performance.now() - started;
  assert.ok(elapsed >= 30 && elapsed < 1500, 'shutdown should allow the grace period, then close the unfinished request');
  assert.equal(server.listening, false);
});

test('public origins allow exact HTTPS origins and reject insecure or foreign origins', async t => {
  const { base } = await listen(t, { publicBaseUrls: ['https://peptara-calculator.vercel.app', 'https://calculator-deploy.vercel.app'] });
  for (const origin of ['https://peptara-calculator.vercel.app', 'https://calculator-deploy.vercel.app']) {
    const response = await fetch(`${base}/health`, { headers: { Origin: origin } });
    assert.equal(response.status, 200);
    assert.equal(response.headers.get('access-control-allow-origin'), origin);
  }
  for (const origin of ['http://peptara-calculator.vercel.app', 'https://attacker.example', 'https://peptara-calculator.vercel.app.attacker.example']) {
    assert.equal((await fetch(`${base}/health`, { headers: { Origin: origin } })).status, 403);
  }
  for (const publicBaseUrl of ['http://public.example', 'https://public.example/path', 'https://user:pass@public.example', 'https://public.example/?query=1']) {
    assert.throws(() => createHttpServer({ publicBaseUrl }), /HTTPS origins/);
  }
});

test('public information pages work and verification remains unconfigured until assigned', async t => {
  const { base } = await listen(t, {});
  for (const path of ['/privacy', '/support']) {
    const response = await fetch(`${base}${path}`);
    assert.equal(response.status, 200);
    assert.match(response.headers.get('content-type'), /text\/html/);
    assert.match(await response.text(), /Peptara Labs/);
  }
  assert.equal((await fetch(`${base}/.well-known/openai-apps-challenge`)).status, 404);
  assert.equal((await fetch(`${base}/.env`)).status, 404);
});
