import assert from 'node:assert/strict';
import { randomUUID } from 'node:crypto';
const PAID_TOOLS = new Set(['reserveMarketingRunSpend', 'beginMarketingRunSpend', 'reconcileMarketingRunSpend']);
// Optional explicitly configured bearer route. Host sessions can inject callQuality directly.
// Never extract a token from a browser, connector, keychain, or another session.
export function qualityClientFromEnvironment(env = process.env, fetchImpl = fetch) {
  const url = new URL(env.MARKETING_RUN_MCP_URL);
  assert.equal(url.protocol, 'https:'); assert.equal(url.pathname, '/mcp/quality');
  assert.ok(!url.username && !url.password && !url.search && !url.hash);
  assert.equal(url.origin, env.MARKETING_RUN_APPROVED_ORIGIN, 'explicit approved origin required');
  assert.ok(env.MARKETING_RUN_ACCESS_TOKEN, 'explicitly configured local MyMarketer token required');
  return async (name, args) => {
    assert.ok(PAID_TOOLS.has(name), 'tool outside paid adapter boundary');
    const response = await fetchImpl(url, { method: 'POST', redirect: 'error', signal: AbortSignal.timeout(30_000), headers: { Authorization: `Bearer ${env.MARKETING_RUN_ACCESS_TOKEN}`, 'Content-Type': 'application/json', Accept: 'application/json, text/event-stream' }, body: JSON.stringify({ jsonrpc: '2.0', id: randomUUID(), method: 'tools/call', params: { name, arguments: args } }) });
    assert.ok(response.ok, `MyMarketer HTTP ${response.status}`);
    assert.ok(response.headers.get('content-type')?.includes('application/json'), 'use host tool bridge for non-JSON MCP transport');
    const envelope = await response.json();
    assert.ok(!envelope.error && !envelope.result?.isError, 'MyMarketer rejected paid operation');
    const result = envelope.result;
    if (result.structuredContent) return result.structuredContent;
    const block = result.content?.find(item => item.type === 'text');
    assert.ok(block, 'MyMarketer returned no tool data');
    return JSON.parse(block.text);
  };
}
