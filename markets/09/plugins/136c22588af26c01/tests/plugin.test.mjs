import test from 'node:test'
import assert from 'node:assert/strict'
import { config, bmiOf } from '../src/plugin.config.ts'
import { callTool } from '../src/core/mcp.ts'

// Hand-checked: 72 / 1.65^2 = 26.45; 70 kg at 5'6" (167.64 cm) = 24.91; 55 / 1.6^2 = 21.48.
test('72 kg 165 cm is obese by Indian cutoffs, overweight by WHO', async () => {
  const r = await callTool(config, 'bmi_check', { weight_kg: 72, height_cm: 165 })
  assert.equal(r.structuredContent.bmi, 26.4)
  assert.equal(r.structuredContent.indian_category, 'Obese')
  assert.equal(r.structuredContent.who_category, 'Overweight')
  assert.match(r.content[0].text, /Not medical advice/)
})

test('feet and inches convert, 24.9 is overweight for Indians but normal for WHO', async () => {
  const r = await callTool(config, 'bmi_check', { weight_kg: 70, height_ft: 5, height_in: 6 })
  assert.equal(r.structuredContent.height_cm, 167.6)
  assert.equal(r.structuredContent.bmi, 24.9)
  assert.equal(r.structuredContent.indian_category, 'Overweight')
  assert.equal(r.structuredContent.who_category, 'Normal')
})

test('boundaries: 23.0 overweight, 22.9 normal, 25.0 obese (Indian)', () => {
  assert.equal(bmiOf(23 * 4, 200).indian_category, 'Overweight')
  assert.equal(bmiOf(22.9 * 4, 200).indian_category, 'Normal')
  assert.equal(bmiOf(25 * 4, 200).indian_category, 'Obese')
  assert.equal(bmiOf(25 * 4, 200).who_category, 'Overweight')
})

test('healthy range at 170 cm', async () => {
  const r = await callTool(config, 'healthy_weight_range', { height_cm: 170 })
  assert.deepEqual(r.structuredContent.indian_normal_range_kg, [52, 66.2])
  assert.deepEqual(r.structuredContent.who_normal_range_kg, [53.5, 72])
  assert.equal(r.structuredContent.indian_overweight_from_kg, 66.5)
  assert.equal(r.structuredContent.indian_obese_from_kg, 72.3)
  assert.match(r.structuredContent.card.link.url, /utm_campaign=zelta_bmi_india/)
  assert.match(r.structuredContent.card.link.url, /^https:\/\/zelta\.in\/how-it-works\?/)
})

test('missing height fails clearly', async () => {
  const r = await callTool(config, 'healthy_weight_range', {})
  assert.equal(r.isError, true)
})
