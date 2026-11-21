// Usage: npm run smoke -- https://<slug>-stag.upsurge.workers.dev/mcp
// Live JSON-RPC smoke: initialize, tools/list, resources/read, then EVERY sample of EVERY tool via tools/call.
// Exit 0 only if all pass. Prints one JSON summary line (paste it into the wave2 tracking table).
import { config } from '../src/plugin.config.ts'

const url = process.argv[2]
if (!url) { console.error('usage: npm run smoke -- <mcp url>'); process.exit(2) }
let id = 0
async function rpc(method, params) {
  const r = await fetch(url, { method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream', 'x-lauki-qa': '1', 'user-agent': 'lauki-qa/smoke' }, body: JSON.stringify({ jsonrpc: '2.0', id: ++id, method, params }) })
  if (r.status !== 200) throw new Error(`${method} HTTP ${r.status}`)
  const j = await r.json()
  if (j.error) throw new Error(`${method} ${j.error.message}`)
  return j.result
}
const fails = []
let calls = 0
try {
  const init = await rpc('initialize', { protocolVersion: '2025-06-18', capabilities: {}, clientInfo: { name: 'smoke', version: '1' } })
  if (init.serverInfo.name !== config.slug) fails.push(`serverInfo ${init.serverInfo.name}`)
  const { tools } = await rpc('tools/list', {})
  const names = tools.map((t) => t.name).sort().join(',')
  if (names !== config.tools.map((t) => t.name).sort().join(',')) fails.push(`tools/list mismatch: ${names}`)
  const { resources } = await rpc('resources/list', {})
  for (const res of resources) { const rr = await rpc('resources/read', { uri: res.uri }); if (rr.contents[0].mimeType !== 'text/html+skybridge') fails.push('widget mime') }
  for (const t of config.tools) for (const s of t.samples) {
    calls++
    try {
      const r = await rpc('tools/call', { name: t.name, arguments: s })
      if (r.isError) fails.push(`${t.name} ${JSON.stringify(s)}: ${r.content?.[0]?.text}`)
      else if (t.widget !== false && !r.structuredContent?.card) fails.push(`${t.name}: no card`)
    } catch (e) { fails.push(`${t.name}: ${e.message}`) }
  }
} catch (e) { fails.push(String(e.message || e)) }
const health = await fetch(new URL('/privacy', url)).then((r) => r.status).catch(() => 0)
if (health !== 200) fails.push(`privacy ${health}`)
console.log(JSON.stringify({ slug: config.slug, url, tools: config.tools.length, calls, pass: calls - fails.length, fails }))
process.exit(fails.length ? 1 : 0)
