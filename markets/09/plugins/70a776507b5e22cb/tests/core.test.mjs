// Core tests - DO NOT EDIT per plugin. They pin the shared vedic-core math, geocoding and the MCP/UTM contract.
import test from 'node:test'
import assert from 'node:assert/strict'
import { config } from '../src/plugin.config.ts'
import { findPlace, fmtTime, tzOffsetMin, localToUtc } from '../src/core/geo.ts'
import { sunDay, tithiInfo, moonNakshatra, daySegment, RAHU_SEG, lunarMonth, tithiEnd } from '../src/core/vedic.ts'
import { listTools, callTool, widgetUri, logCalls, clientClass } from '../src/core/mcp.ts'
import worker from '../src/index.ts'

test('geo: aliases, India preference, tz', () => {
  assert.equal(findPlace('Bombay').name, 'Mumbai')
  assert.equal(findPlace('Bangalore').tz, 'Asia/Kolkata')
  assert.equal(findPlace('Hyderabad').country, 'IN')
  assert.equal(findPlace('Hyderabad, Pakistan').country, 'PK')
  assert.equal(findPlace('London').country, 'GB')
  assert.equal(tzOffsetMin('Asia/Kolkata', new Date()), 330)
  assert.equal(localToUtc('2026-10-01', '05:30', 'Asia/Kolkata').toISOString(), '2026-10-01T00:00:00.000Z')
})

// Reference vectors from outputs/chatgpt-plugin-wave2/vedic-core-reference.mjs (marshal 6abe179e2e5b, 4/4 known dates).
const REF = [
  [[19.076, 72.8777], '2026-10-01', '06:29', 'Krishna', 'Panchami', 'Rohini', 1, '13:57-15:27'],
  [[28.6139, 77.209], '2026-10-01', '06:13', 'Krishna', 'Panchami', 'Rohini', 1, '13:39-15:09'],
  [[28.6139, 77.209], '2025-10-21', '06:25', 'Krishna', 'Amavasya', 'Chitra', 2, '14:55-16:20'],
  [[28.6139, 77.209], '2025-07-06', '05:29', 'Shukla', 'Ekadashi', 'Vishakha', 2, '17:38-19:22'],
  [[28.6139, 77.209], '2025-11-05', '06:36', 'Shukla', 'Purnima', 'Ashwini', 4, '12:04-13:26'],
]
for (const [[lat, lon], date, sr, paksha, tithi, nak, pada, rahu] of REF) {
  test(`vedic-core reference: ${lat},${lon} ${date}`, () => {
    const p = { lat, lon, tz: 'Asia/Kolkata' }
    const d = sunDay(date, p.lat, p.lon, p.tz)
    assert.equal(fmtTime(d.sunrise, p.tz), sr)
    const ti = tithiInfo(d.sunrise)
    assert.equal(ti.paksha, paksha); assert.equal(ti.name, tithi)
    const n = moonNakshatra(d.sunrise)
    assert.equal(n.name, nak); assert.equal(n.pada, pada)
    const rk = daySegment(d, RAHU_SEG[d.weekday])
    assert.equal(`${fmtTime(rk.start, p.tz)}-${fmtTime(rk.end, p.tz)}`, rahu)
  })
}
test('vedic-core: lunar month + tithi end sanity', () => {
  const p = findPlace('Mumbai')
  const d = sunDay('2026-10-01', p.lat, p.lon, p.tz)
  const lm = lunarMonth(d.sunrise)
  assert.equal(lm.amanta, 'Bhadrapada'); assert.equal(lm.purnimanta, 'Ashwin')
  const end = tithiEnd(d.sunrise)
  assert.ok(end && end > d.sunrise && end.getTime() - d.sunrise.getTime() < 30 * 3600e3)
})

test('contract: every tool description follows "Use this when ... Do not use for"', () => {
  for (const t of listTools(config)) {
    assert.match(t.description, /^Use this when /, t.name)
    assert.match(t.description, /Do not use (for|to|when|without)/, t.name)
    assert.ok(t.description.length <= 1024, t.name)
    assert.doesNotMatch(t.description + config.shortDescription + config.longDescription, /\b(price|pricing|upgrade|subscribe|subscription|premium|discount|buy now|best|#1|plugin|mcp)\b/i, `${t.name}: no pricing/promo/superlative/plugin words`)
  }
  assert.doesNotMatch(config.name, /plugin|mcp|app$/i)
})

test('contract: every sample runs, renders a card, and every URL carries exactly the 4 static UTMs and no input value', async () => {
  for (const t of config.tools) {
    assert.ok(t.samples.length >= 1, `${t.name} needs samples`)
    for (const s of t.samples) {
      const r = await callTool(config, t.name, s)
      assert.ok(!r.isError, `${t.name} ${JSON.stringify(s)} -> ${JSON.stringify(r.content)}`)
      if (t.widget !== false) assert.ok(r.structuredContent?.card?.title, `${t.name} card`)
      const urls = JSON.stringify(r).match(/https?:\/\/[^"\s\\]+/g) || []
      for (const u of urls) {
        const url = new URL(u)
        const keys = [...url.searchParams.keys()].sort()
        assert.deepEqual(keys, ['utm_campaign', 'utm_content', 'utm_medium', 'utm_source'], `${t.name}: ${u}`)
        assert.equal(url.searchParams.get('utm_source'), 'chatgpt'); assert.equal(url.searchParams.get('utm_medium'), 'plugin')
        assert.equal(url.searchParams.get('utm_campaign'), config.funnel.campaign)
        assert.match(url.searchParams.get('utm_content'), new RegExp(`^${t.name}--(inline|panel|sidebar|fileviewer|event)$`))
        const props = t.inputSchema.properties || {}
        for (const [k, v] of Object.entries(s)) if (typeof v === 'string' && v.length > 2 && !(props[k]?.enum || []).includes(v)) assert.ok(!u.toLowerCase().includes(v.toLowerCase().replace(/ /g, '%20')) && !u.toLowerCase().includes(encodeURIComponent(v.toLowerCase())), `${t.name}: input "${v}" leaked into ${u}`)
      }
    }
  }
})

test('worker: initialize, tools/list, resources/read, notifications, privacy, GET /mcp', async () => {
  const post = (body) => worker.fetch(new Request('https://x.test/mcp', { method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream' }, body: JSON.stringify(body) }))
  const init = await (await post({ jsonrpc: '2.0', id: 1, method: 'initialize', params: { protocolVersion: '2025-06-18', capabilities: {}, clientInfo: { name: 't', version: '1' } } })).json()
  assert.equal(init.result.protocolVersion, '2025-06-18'); assert.ok(init.result.capabilities.tools)
  assert.equal((await post({ jsonrpc: '2.0', method: 'notifications/initialized' })).status, 202)
  const tl = await (await post({ jsonrpc: '2.0', id: 2, method: 'tools/list' })).json()
  assert.equal(tl.result.tools.length, config.tools.length)
  const rr = await (await post({ jsonrpc: '2.0', id: 3, method: 'resources/read', params: { uri: widgetUri(config) } })).json()
  assert.equal(rr.result.contents[0].mimeType, 'text/html+skybridge')
  assert.doesNotMatch(rr.result.contents[0].text, /<script[^>]+src=|<link[^>]+href=|fetch\(/, 'widget must be self-contained')
  const priv = await worker.fetch(new Request('https://x.test/privacy'))
  assert.match(await priv.text(), /utm_source=chatgpt/)
  assert.equal((await worker.fetch(new Request('https://x.test/mcp'))).status, 405)
})

test('mcp: plugin-authored errors surface, input echoes and internal errors stay generic; env reaches run()', async () => {
  const { safeMessage } = await import('../src/core/mcp.ts')
  assert.equal(safeMessage(new Error('station not found in the bundled list'), { code: 'KYQ' }), 'station not found in the bundled list')
  assert.match(safeMessage(new Error('No match for kyq'), { code: 'KYQ' }), /^Something went wrong/)
  assert.match(safeMessage(new TypeError('x is undefined'), {}), /^Something went wrong/)
  assert.match(safeMessage(new Error('born 1990-07-15 not valid'), { birth_date: '1990-07-15' }), /^Something went wrong/)
  const probe = { ...config, tools: [{ ...config.tools[0], run: (_a, env) => ({ text: env && env.FLAG ? 'env-ok' : 'no-env' }) }] }
  const r = await callTool(probe, probe.tools[0].name, probe.tools[0].samples[0], { FLAG: 1 })
  assert.equal(r.content[0].text, 'env-ok')
})

test('usage log: tool name + client class only, never args or unregistered names', () => {
  const lines = []
  const orig = console.log
  console.log = (s) => lines.push(s)
  try {
    const t = config.tools[0].name
    logCalls(config, [
      { jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name: t, arguments: { secret_input: 'Priya Sharma 1990-07-15' } } },
      { jsonrpc: '2.0', id: 2, method: 'tools/call', params: { name: 'Priya Sharma', arguments: {} } },
      { jsonrpc: '2.0', id: 3, method: 'ping' },
    ], 'openai-mcp/1.0 (+https://openai.com/bot)')
    assert.equal(lines.length, 2)
    const a = JSON.parse(lines[0]), b = JSON.parse(lines[1])
    assert.deepEqual(a, { evt: 'mcp_call', plugin: config.slug, method: 'tools/call', tool: t, client: 'openai' })
    assert.equal(b.tool, 'unknown')
    assert.ok(!lines.join('').includes('Priya') && !lines.join('').includes('1990'))
  } finally { console.log = orig }
  assert.equal(clientClass('Mozilla/5.0'), 'other')
  assert.equal(clientClass('node'), 'script')
  assert.equal(clientClass('openai-mcp/1.0', '1'), 'qa')
  assert.equal(clientClass('lauki-qa/verify'), 'qa')
  assert.equal(clientClass('curl/8.5.0'), 'qa')
})
