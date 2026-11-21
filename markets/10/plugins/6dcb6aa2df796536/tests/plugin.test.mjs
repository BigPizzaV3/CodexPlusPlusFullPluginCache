import test from 'node:test'
import assert from 'node:assert/strict'
import { calculateSip, monthCount, config } from '../src/plugin.config.ts'
import { callTool } from '../src/core/mcp.ts'

// Formula reference: Groww SIP calculator, https://groww.in/calculators/sip-calculator
// It defines M = P * (((1+i)^n - 1)/i) * (1+i), with i as monthly rate.
// This plugin deliberately states its own nominal annual-rate / 12 convention.
// Groww's current page uses effective annual conversion instead; only its annuity
// identity is referenced here, not its UI result. Pins independently derived with
// Python decimal at precision 45, q=Decimal('1.01'), n=120:
// f=(q**n-1)/(q-1)*q; SIP=5000*f; goal=10000000/f; lumpsum=100000*q**n.
// Step-up pin: 5000*((q**12-1)/(q-1))*q*q**12 + 5500*((q**12-1)/(q-1))*q.
test('known SIP answer: 5000 monthly, 12% nominal, 10 years', () => {
  const r = calculateSip(5000, 12, 10)
  assert.equal(r.invested, 600000)
  assert.equal(Math.round(r.value * 100) / 100, 1161695.38)
})

test('known step-up answer: 5000, 10% annual step-up, 12% nominal, 2 years', () => {
  const r = calculateSip(5000, 12, 2, 10)
  assert.equal(Math.round(r.invested * 100) / 100, 126000)
  assert.equal(Math.round(r.value * 100) / 100, 142620.66)
})

test('goal SIP known answer: 1 crore in 10 years at 12%', () => {
  const one = calculateSip(1, 12, 10).value
  assert.equal(Math.round((10000000 / one) * 100) / 100, 43040.54)
})

test('known lumpsum answer: 100000 at 12% nominal for 10 years', async () => {
  const r = await callTool(config, 'lumpsum', { amount: 100000, rate: 12, years: 10 })
  assert.equal(r.structuredContent.value, 330038.69)
  assert.match(r.content[0].text, /not guaranteed/i)
})

test('goal tool rounds monthly amount up and returns card link', async () => {
  const r = await callTool(config, 'goal_sip', { target: 10000000, years: 10, annual_return: 12 })
  assert.equal(r.structuredContent.monthly, 43040.55)
  assert.match(r.structuredContent.card.link.url, /utm_campaign=lauki_sip/)
  assert.match(r.structuredContent.card.note, /monthly compounding/i)
})

test('zero-return exact arithmetic and step-up boundary', () => {
  assert.equal(calculateSip(5000, 0, 10).value, 600000)
  assert.equal(calculateSip(5000, 0, 2, 10).value, 126000)
  assert.equal(calculateSip(100, 0, 1, 10).invested, 1200)
  assert.equal(calculateSip(100, 0, 13 / 12, 10).invested, 1310)
})

test('first payment earns one month and negative returns produce losses', () => {
  assert.equal(calculateSip(5000, 12, 1 / 12).value, 5050)
  assert.equal(calculateSip(1000, -12, 1 / 12).value, 990)
})

test('zero target needs no contributions', async () => {
  const r = await callTool(config, 'goal_sip', { target: 0, years: 1, annual_return: 0 })
  assert.equal(r.structuredContent.monthly, 0)
  assert.equal(r.structuredContent.value, 0)
})

test('whole month validation', () => {
  assert.equal(monthCount(1.5), 18)
  assert.throws(() => monthCount(1.01), /whole number of months/)
})
