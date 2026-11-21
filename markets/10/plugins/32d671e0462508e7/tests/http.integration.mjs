import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import { unzipSync } from 'fflate';
import { httpServer } from '../src/server.mjs';

test('ChatGPT HTTP transport can discover tools, create a project, and download its bytes', async () => {
  const configuration = { publicURL: 'http://127.0.0.1:0' };
  const app = httpServer(configuration);
  await new Promise((resolve, reject) => { app.once('error', reject); app.listen(0, '127.0.0.1', resolve); });
  configuration.publicURL = `http://127.0.0.1:${app.address().port}`;
  const client = new Client({ name: 'browser-integration-test', version: '1' });
  try {
    await client.connect(new StreamableHTTPClientTransport(new URL(`${configuration.publicURL}/mcp`)));
    assert.equal((await client.listTools()).tools.length, 5);
    const grid = await client.callTool({ name: 'get_carousel_spec', arguments: { section: 'catalogs', query: 'quad', category: 'grids' } });
    assert.equal(grid.structuredContent.catalog.entries[0].example.layers[0].grid.cells.length, 4);
    const overview = await client.callTool({ name: 'get_carousel_spec', arguments: { section: 'overview' } });
    assert.equal(overview.structuredContent.capabilities.native_renderer, false);
    const writing = await client.callTool({ name: 'get_carousel_spec', arguments: { section: 'writing' } });
    assert.equal(writing.isError, undefined);
    assert.equal(writing.structuredContent.section, 'writing');
    assert.equal(writing.content[0].text, await readFile(new URL('../skills/create-carousel/references/WRITING_GUIDE.md', import.meta.url), 'utf8'));
    const yaml = await readFile(new URL('../examples/creator-demo.yaml', import.meta.url), 'utf8');
    const result = await client.callTool({ name: 'create_carousel', arguments: { yaml, filename: 'Тест из браузера' } });
    assert.equal(result.isError, undefined);
    assert.equal(result.structuredContent.slides, 5);
    assert.ok(Array.isArray(result.structuredContent.warnings));
    assert.equal(result.structuredContent.visual_check, 'not performed');
    const response = await fetch(result.structuredContent.download_url);
    assert.equal(response.status, 200);
    assert.match(response.headers.get('content-disposition'), /attachment/);
    assert.equal(response.headers.get('cache-control'), 'private, no-store');
    const files = unzipSync(new Uint8Array(await response.arrayBuffer()));
    assert.ok(Buffer.from(files['carousel.yaml']).toString().includes('От идеи\\nк карусели'));
    assert.equal((await fetch(`${configuration.publicURL}/downloads/${'0'.repeat(48)}/other.carousel`)).status, 404);
  } finally {
    await client.close();
    app.closeAllConnections();
    await new Promise(resolve => app.close(resolve));
  }
});
