import test from 'node:test';
import assert from 'node:assert/strict';
import { once } from 'node:events';
import { request } from 'node:http';
import { connect } from 'node:net';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';
import { createHttpServer } from '../src/http.mjs';
import { RESOURCE_URI } from '../src/mcp-server.mjs';

async function http(t) {
  const server = createHttpServer();
  server.listen(0, '127.0.0.1'); await once(server, 'listening');
  const base = `http://127.0.0.1:${server.address().port}`;
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  return base;
}
async function inspectClient(client) {
  const { tools } = await client.listTools();
  assert.deepEqual(tools.map(tool => tool.name).sort(), ['calculate_concentration', 'open_concentration_calculator']);
  for (const tool of tools) {
    assert.equal(tool.annotations.readOnlyHint, true);
    assert.equal(tool.annotations.openWorldHint, false);
    assert.equal(tool._meta.ui.resourceUri, RESOURCE_URI);
    assert.equal(tool.inputSchema.additionalProperties, false);
  }
  const opened = await client.callTool({ name: 'open_concentration_calculator', arguments: {} });
  assert.equal(opened.structuredContent.mode, 'empty');
  const computed = await client.callTool({ name: 'calculate_concentration', arguments: { mass: '13.7', massUnit: 'mg', volume: '2.5', volumeUnit: 'mL' } });
  assert.equal(computed.structuredContent.result.concentration.mgPerMl, '5.48');
  const invalid = await client.callTool({ name: 'calculate_concentration', arguments: { mass: '1', massUnit: 'mg', volume: '0', volumeUnit: 'mL' } });
  assert.equal(invalid.isError, true);
  const extra = await client.callTool({ name: 'calculate_concentration', arguments: { mass: '1', massUnit: 'mg', volume: '1', volumeUnit: 'mL', dose: '2' } });
  assert.equal(extra.isError, true);
  const resource = await client.readResource({ uri: RESOURCE_URI });
  assert.equal(resource.contents[0].mimeType, 'text/html;profile=mcp-app');
  assert.match(resource.contents[0].text, /Final solution volume/);
  assert.match(resource.contents[0].text, /Calculate concentration/);
  assert.ok(!resource.contents[0].text.includes('BUILD_SCRIPT'));
}

test('real HTTP MCP client initializes, discovers, calculates, rejects invalid input and reads UI', async t => {
  const base = await http(t);
  const client = new Client({ name: 'private-test', version: '1.0.0' });
  await client.connect(new StreamableHTTPClientTransport(new URL(`${base}/mcp`)));
  try { await inspectClient(client); } finally { await client.close(); }
});
test('real stdio MCP client executes the same plugin capabilities', async () => {
  const client = new Client({ name: 'private-stdio-test', version: '1.0.0' });
  await client.connect(new StdioClientTransport({ command: process.execPath, args: [new URL('../src/stdio.mjs', import.meta.url).pathname], stderr: 'pipe' }));
  try { await inspectClient(client); } finally { await client.close(); }
});
test('preview is self-contained and does not cache input data', async t => {
  const base = await http(t); const response = await fetch(base);
  assert.equal(response.status, 200);
  assert.equal(response.headers.get('cache-control'), 'no-store');
  assert.match(response.headers.get('content-security-policy'), /connect-src 'none'/);
  const html = await response.text();
  assert.ok(!/<script[^>]+src=/.test(html));
  assert.ok(!/<link[^>]+stylesheet/.test(html));
  assert.equal((await fetch(`${base}/missing`)).status, 404);
});
test('foreign origins, DNS rebinding hosts and malformed requests are rejected', async t => {
  const base = await http(t);
  assert.equal((await fetch(base, { headers: { Origin: 'https://untrusted.example' } })).status, 403);
  const hostStatus = await new Promise((resolve, reject) => {
    const req = request(base, { headers: { Host: 'untrusted.example' } }, response => { response.resume(); resolve(response.statusCode); });
    req.on('error', reject); req.end();
  });
  assert.equal(hostStatus, 403);
  assert.equal((await fetch(`${base}/mcp`, { method: 'POST', body: '{}' })).status, 415);
  assert.equal((await fetch(`${base}/mcp`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{bad' })).status, 400);
  assert.equal((await fetch(`${base}/mcp`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: 'x'.repeat(32769) })).status, 413);
});
test('remote configuration requires HTTPS', () => {
  assert.throws(() => createHttpServer({ publicBaseUrl: 'http://external.example' }), /HTTPS/);
});
test('malformed request targets return 400 and leave the server healthy', async t => {
  const base = await http(t); const url = new URL(base);
  const response = await new Promise((resolve, reject) => {
    const socket = connect(Number(url.port), '127.0.0.1');
    let data = '';
    socket.on('connect', () => socket.write(`GET //[ HTTP/1.1\r\nHost: ${url.host}\r\nConnection: close\r\n\r\n`));
    socket.on('data', chunk => { data += chunk; });
    socket.on('end', () => resolve(data)); socket.on('error', reject);
  });
  assert.match(response, /^HTTP\/1.1 400/);
  assert.equal((await fetch(`${base}/health`)).status, 200);
});
