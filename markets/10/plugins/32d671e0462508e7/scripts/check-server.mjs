import assert from 'node:assert/strict';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import { unzipSync } from 'fflate';
import { parseLayout, validateDocument } from '../src/document.mjs';

export async function checkServer({ origin, yaml, expectedPublicOrigin = origin, outputPath }) {
  const endpoint = new URL(origin);
  assert.ok(endpoint.protocol === 'https:' || (endpoint.protocol === 'http:' && ['localhost', '127.0.0.1', '[::1]'].includes(endpoint.hostname)), 'Use HTTPS, or loopback for an internal check');
  const health = await fetch(new URL('/health', endpoint), { redirect: 'error', signal: AbortSignal.timeout(10_000) });
  assert.equal(health.status, 200, 'Health endpoint must return HTTP 200');
  assert.equal((await health.json()).ok, true);

  const client = new Client({ name: 'carousel-deployment-check', version: '1' });
  try {
    await client.connect(new StreamableHTTPClientTransport(new URL('/mcp', endpoint)));
    const names = (await client.listTools()).tools.map(tool => tool.name).sort();
    for (const name of ['get_carousel_spec', 'validate_carousel', 'create_carousel']) assert.ok(names.includes(name), `Missing tool: ${name}`);
    const spec = await client.callTool({ name: 'get_carousel_spec', arguments: { section: 'rules' } });
    assert.notEqual(spec.isError, true);
    assert.ok(spec.content.some(item => item.type === 'text' && item.text.length > 100), 'Format rules must be available');
    const validation = await client.callTool({ name: 'validate_carousel', arguments: { yaml } });
    assert.notEqual(validation.isError, true, JSON.stringify(validation.content));
    assert.equal(JSON.parse(validation.content.find(item => item.type === 'text').text).valid, true);

    const result = await client.callTool({ name: 'create_carousel', arguments: { yaml, filename: 'Проверка AWS' } });
    assert.notEqual(result.isError, true, JSON.stringify(result.content));
    const project = result.structuredContent;
    assert.ok(project, 'Creation must return structured project information');
    const downloadURL = new URL(project.download_url);
    assert.equal(downloadURL.origin, new URL(expectedPublicOrigin).origin, 'Download must use the configured public HTTPS origin');
    assert.ok(downloadURL.pathname.startsWith('/downloads/'));
    const response = await fetch(new URL(downloadURL.pathname, endpoint), { redirect: 'error', signal: AbortSignal.timeout(30_000) });
    assert.equal(response.status, 200, 'Created file must be downloadable');
    assert.match(response.headers.get('content-disposition') ?? '', /attachment/);
    assert.equal(response.headers.get('cache-control'), 'private, no-store');
    const bytes = new Uint8Array(await response.arrayBuffer());
    assert.equal(bytes.byteLength, project.bytes);
    const files = unzipSync(bytes);
    assert.ok(files['carousel.yaml'], 'Native archive must contain carousel.yaml');
    const document = validateDocument(parseLayout(Buffer.from(files['carousel.yaml']).toString('utf8')));
    assert.equal(document.slides, 5);
    assert.equal(document.layers.length, 25);
    if (outputPath) {
      await mkdir(dirname(outputPath), { recursive: true });
      await writeFile(outputPath, bytes, { flag: 'wx' });
    }
    return { check: endpoint.protocol === 'https:' && endpoint.origin === downloadURL.origin ? 'public HTTPS' : 'internal HTTP', tools: names, slides: document.slides, layers: document.layers.length, bytes: bytes.byteLength, download_url: project.download_url, expires_at: project.expires_at, saved_to: outputPath ?? null, visual_check: 'not performed' };
  } finally {
    await client.close();
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const origin = process.argv[2] ?? 'https://mcp.quokka.software';
  const outputPath = process.argv[3] ?? fileURLToPath(new URL(`../artifacts/aws-check-${Date.now()}.carousel`, import.meta.url));
  const yaml = await readFile(new URL('../examples/creator-demo.yaml', import.meta.url), 'utf8');
  console.log(JSON.stringify(await checkServer({ origin, yaml, outputPath }), null, 2));
}
