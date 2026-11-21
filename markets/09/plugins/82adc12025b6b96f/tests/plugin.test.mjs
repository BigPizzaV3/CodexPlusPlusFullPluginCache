import test from 'node:test'
import assert from 'node:assert/strict'
import { config, proteinTarget, foodPlan } from '../src/plugin.config.ts'
import { callTool } from '../src/core/mcp.ts'

// ICMR-NIN 0.83 g/kg x 70 = 58.1; weight at BMI 25 for 165 cm = 68.06 kg -> 1.2-1.6 g/kg = 82-109 g.
test('70 kg maintain = 58 g (ICMR-NIN 0.83 g/kg)', async () => {
  const r = await callTool(config, 'protein_per_day', { weight_kg: 70, goal: 'maintain' })
  assert.equal(r.structuredContent.grams_low, 58)
  assert.equal(r.structuredContent.grams_high, 58)
  assert.match(r.content[0].text, /Not medical advice/)
})

test('85 kg at 165 cm, weight loss: computed on the BMI-25 weight', () => {
  const t = proteinTarget(85, 'weight_loss', 165)
  assert.equal(t.adjusted, true)
  assert.equal(t.reference_kg, 68.1)
  assert.equal(t.grams_low, 82)
  assert.equal(t.grams_high, 109)
})

test('65 kg muscle gain = 104-143 g', () => {
  const t = proteinTarget(65, 'muscle_gain')
  assert.equal(t.grams_low, 104)
  assert.equal(t.grams_high, 143)
})

test('veg 80 g sample day has no egg or meat and reaches the target', async () => {
  const r = await callTool(config, 'protein_food_plan', { grams: 80, diet: 'veg' })
  const p = r.structuredContent
  assert.equal(p.reached, true)
  assert.equal(p.total_g, 92.9)
  assert.ok(!p.items.some((i) => /Egg|Chicken|Fish/.test(i.food)))
  assert.match(p.card.link.url, /utm_campaign=zelta_protein_target/)
})

test('non-veg 100 g day uses chicken and fish first', () => {
  const p = foodPlan(100, 'non_veg')
  assert.equal(p.items[0].food, 'Chicken breast (cooked)')
  assert.equal(p.total_g, 110.9)
})
