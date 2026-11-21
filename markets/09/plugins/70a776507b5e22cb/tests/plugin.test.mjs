import test from 'node:test'
import assert from 'node:assert/strict'
import { config, evaluateDate, findMuhurat, planetaryCombustion } from '../src/plugin.config.ts'
import { callTool } from '../src/core/mcp.ts'

// Source: shared vedic-core reference vectors for 2026-10-01 Mumbai/Delhi and the
// classical Panchanga screening principles cited in src/plugin.config.ts.
test('check_date resolves Mumbai and returns explicit screening factors', async () => {
  const r = await callTool(config, 'check_date', { purpose: 'vehicle', date: '2026-10-05', city: 'Mumbai' })
  assert.equal(r.isError, undefined)
  assert.equal(r.structuredContent.city.includes('Mumbai'), true)
  assert.equal(typeof r.structuredContent.passed, 'boolean')
  assert.equal(r.structuredContent.guidance, 'General guidance from the classical rules; confirm the final muhurat with your family astrologer.')
  assert.match(r.structuredContent.card.link.url, /utm_campaign=naksha_muhurat/)
})

test('known date vector exposes tithi, nakshatra and weekday factors', () => {
  const r = evaluateDate('property', '2026-10-01', 'Delhi')
  assert.equal(r.place.name, 'Delhi')
  assert.equal(r.tithi.name, 'Panchami')
  assert.equal(r.tithi.paksha, 'Krishna')
  assert.equal(r.nakshatra.name, 'Rohini')
  assert.equal(r.factors.weekday.value, 'Thursday')
  assert.equal(typeof r.factors.combust.pass, 'boolean')
})

test('find_muhurat returns dates with windows for a real month', async () => {
  const result = findMuhurat('vehicle', 2, 2027, 'Pune')
  assert.equal(result.data.city.includes('Pune'), true)
  assert.ok(Array.isArray(result.data.dates))
  assert.equal(result.card.table.columns[0], 'Date')
  assert.equal(result.card.note, 'General guidance from the classical rules; confirm the final muhurat with your family astrologer.')
})

test('all tool samples render cards and static funnel links', async () => {
  for (const tool of config.tools) {
    for (const args of tool.samples) {
      const r = await callTool(config, tool.name, args)
      assert.equal(r.isError, undefined)
      assert.equal(typeof r.structuredContent.card.title, 'string')
      const url = new URL(r.structuredContent.card.link.url)
      assert.equal(url.origin, 'https://naksha.social')
      assert.equal(url.searchParams.get('utm_source'), 'chatgpt')
      assert.equal(url.searchParams.get('utm_medium'), 'plugin')
      assert.equal(url.searchParams.get('utm_campaign'), 'naksha_muhurat')
      assert.equal(url.searchParams.get('utm_content').startsWith(`${tool.name}--`), true)
    }
  }
})

test('combustion helper is deterministic for the pinned date', () => {
  const a = planetaryCombustion(new Date('2026-10-01T00:00:00Z'))
  const b = planetaryCombustion(new Date('2026-10-01T00:00:00Z'))
  assert.deepEqual(a, b)
})
