import test from 'node:test'
import assert from 'node:assert/strict'
import { config, walk, stepsFor } from '../src/plugin.config.ts'
import { callTool } from '../src/core/mcp.ts'

// 10,000 steps x 0.762 m = 7.62 km; at 4.8 km/h = 1.5875 h; 3.5 MET x 70 kg x 1.5875 h = 388.9 kcal.
test('10,000 steps at 70 kg normal pace = about 389 kcal, 7.6 km, 95 min', async () => {
  const r = await callTool(config, 'steps_to_calories', { steps: 10000, weight_kg: 70 })
  const s = r.structuredContent
  assert.equal(s.kcal, 389)
  assert.equal(s.distance_km, 7.6)
  assert.equal(s.minutes, 95)
  assert.match(r.content[0].text, /Not medical advice/)
})

test('height changes stride: 170 cm = 0.7055 m', () => {
  assert.equal(walk(10000, 70, 'normal', 170).distance_km, 7.1)
})

test('samosa (252 kcal) at 70 kg normal = 6,480 steps', async () => {
  const r = await callTool(config, 'steps_to_burn', { food: 'samosa', weight_kg: 70 })
  assert.equal(r.structuredContent.steps, 6480)
  assert.match(r.structuredContent.card.link.url, /utm_campaign=zelta_steps_calories/)
})

test('brisk walks off 300 kcal in less time than slow', () => {
  assert.ok(stepsFor(300, 75, 'brisk').minutes < stepsFor(300, 75, 'slow').minutes)
})

test('no food and no kcal fails clearly', async () => {
  const r = await callTool(config, 'steps_to_burn', { weight_kg: 70 })
  assert.equal(r.isError, true)
})
