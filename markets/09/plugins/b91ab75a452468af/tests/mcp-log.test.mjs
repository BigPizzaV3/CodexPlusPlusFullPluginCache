import test from 'node:test'
import assert from 'node:assert/strict'
// pure helpers live in src/usage.ts (index.ts imports Worker-only agents/mcp).
import * as mod from '../src/usage.ts'

test('clientClass marks our own traffic as qa', () => {
  assert.equal(mod.clientClass('lauki-qa/1'), 'qa')
  assert.equal(mod.clientClass('Mozilla/5.0', '1'), 'qa')
  assert.equal(mod.clientClass('curl/8.5'), 'qa')
  assert.equal(mod.clientClass('openai-mcp/1.0'), 'openai')
  assert.equal(mod.clientClass('Mozilla/5.0'), 'other')
})

test('logCalls logs only method/tool/client, unknown tools masked', () => {
  const lines = []; const orig = console.log; console.log = (s) => lines.push(JSON.parse(s))
  try {
    mod.logCalls([{ method: 'tools/call', params: { name: 'get_product', arguments: { sku: 'SECRET' } } }, { method: 'tools/call', params: { name: 'x' } }, { method: 'ping' }], 'openai-mcp/1.0')
  } finally { console.log = orig }
  assert.deepEqual(lines, [
    { evt: 'mcp_call', plugin: 'jawd-chatgpt-plugin', method: 'tools/call', tool: 'get_product', client: 'openai' },
    { evt: 'mcp_call', plugin: 'jawd-chatgpt-plugin', method: 'tools/call', tool: 'unknown', client: 'openai' },
  ])
})
