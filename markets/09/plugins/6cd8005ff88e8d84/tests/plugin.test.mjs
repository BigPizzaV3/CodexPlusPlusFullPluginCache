import test from 'node:test'
import assert from 'node:assert/strict'
import { config, target, timeline } from '../src/plugin.config.ts'
import { callTool } from '../src/core/mcp.ts'

// Hand-checked Mifflin-St Jeor: man 30y 175cm 80kg = 800 + 1093.75 - 150 + 5 = 1748.75; x1.55 = 2710.56.
test('man 30y 175 cm 80 kg moderate: maintenance 2711, target 2161 at 0.5 kg/week', async () => {
  const r = await callTool(config, 'daily_calorie_target', { sex: 'male', age: 30, weight_kg: 80, height_cm: 175, activity: 'moderate' })
  const s = r.structuredContent
  assert.equal(s.bmr, 1749)
  assert.equal(s.maintenance_kcal, 2711)
  assert.equal(s.target_kcal, 2161)
  assert.equal(s.daily_deficit_kcal, 550)
  assert.equal(s.loss_kg_per_week, 0.5)
  assert.match(r.content[0].text, /Not medical advice/)
})

test('woman 35y 160 cm 65 kg light: target 1257', () => {
  const t = target({ sex: 'female', age: 35, weight_kg: 65, height_cm: 160, activity: 'light' })
  assert.equal(t.bmr, 1314)
  assert.equal(t.maintenance_kcal, 1807)
  assert.equal(t.target_kcal, 1257)
})

test('never below the 1,200 kcal floor for women; pace shrinks instead', () => {
  const t = target({ sex: 'female', age: 60, weight_kg: 55, height_cm: 150, activity: 'sedentary' })
  assert.equal(t.target_kcal, 1200)
  assert.equal(t.floored, true)
  assert.ok(t.loss_kg_per_week < 0.1)
})

test('pace is capped at 1% of body weight', () => {
  const t = target({ sex: 'female', age: 25, weight_kg: 50, height_cm: 160, activity: 'active', loss_kg_per_week: 1 })
  assert.equal(t.rate_capped, true)
  assert.equal(t.loss_kg_per_week, 0.5)
})

test('85 to 75 kg at 500 kcal deficit = 22 weeks', async () => {
  const r = await callTool(config, 'weight_loss_timeline', { current_kg: 85, target_kg: 75 })
  assert.equal(r.structuredContent.weeks, 22)
  assert.equal(r.structuredContent.months, 5.1)
  assert.equal(r.structuredContent.kg_per_week, 0.45)
  assert.equal(timeline(90, 78, 600).kg_per_week, 0.55)
  assert.match(r.structuredContent.card.link.url, /utm_campaign=zelta_calorie_target/)
})

test('target above current fails clearly', () => {
  assert.throws(() => timeline(70, 75, 500), /below current/)
})
