import test from 'node:test'
import assert from 'node:assert/strict'
import { amortize, monthlyEmi, config } from '../src/plugin.config.ts'
import { callTool } from '../src/core/mcp.ts'

// Source: https://quickcalci.com/emi-calculator documents P*r*(1+r)^n/((1+r)^n-1).
// Independent Python Decimal (40 digits), P=5000000,r=Decimal('8.5')/1200,n=240:
// EMI=43391.16166827669272522408792538623814668; n*EMI-P=5413878.800386406254.
// Requested spec pin: nearest rupee EMI is 43,391.
const near = (actual, expected, tolerance = 1e-6) => assert.ok(Math.abs(actual - expected) < tolerance, `${actual} != ${expected}`)
test('pinned 50 lakh home loan EMI and interest', () => {
  assert.equal(Math.round(monthlyEmi(5000000, 8.5, 240)), 43391)
  near(monthlyEmi(5000000, 8.5, 240), 43391.16166827669)
  const result = amortize(5000000, 8.5, 240)
  near(result.interest, 5413878.800386406)
  assert.equal(result.yearly.length, 20)
  assert.equal(result.balance, 0)
  near(result.yearly.reduce((s,y) => s + y.principal_paid, 0), 5000000)
})

test('zero-rate loan is principal divided by months', () => {
  const result = amortize(120000, 0, 12)
  assert.equal(result.originalEmi, 10000)
  assert.equal(result.interest, 0)
  assert.equal(result.yearly[0].closing_balance, 0)
})

// Hand-derived small positive-rate vector: P=210, r=10% monthly, n=2.
// EMI=121. Month 1 interest=21, principal=100, balance=110.
// Prepay 55 => balance 55; month 2 interest=5.5, final payment=60.5; savings=5.5.
for (const mode of ['reduce_emi', 'reduce_tenure']) {
  test(`hand-derived positive-interest prepayment: ${mode}`, () => {
    const result = amortize(210, 120, 2, { amount: 55, at: 1, mode })
    near(result.originalEmi, 121)
    near(result.interest, 26.5)
    near(result.lastPayment, 60.5)
    near(amortize(210, 120, 2).interest - result.interest, 5.5)
    near(result.revisedEmi, mode === 'reduce_emi' ? 60.5 : 121)
  })
}

test('prepayment reduces interest and tenure when reducing tenure', () => {
  const base = amortize(5000000, 8.5, 240)
  const changed = amortize(5000000, 8.5, 240, { amount: 500000, at: 24, mode: 'reduce_tenure' })
  assert.equal(changed.applied, 500000)
  assert.ok(changed.interest < base.interest)
  assert.ok(changed.elapsed < 240)
  assert.equal(changed.revisedEmi, base.originalEmi)
  near(changed.yearly.reduce((sum,y) => sum + y.principal_paid + y.prepayment, 0), 5000000)
})

test('prepayment recalculates EMI in reduce_emi mode', () => {
  const changed = amortize(5000000, 8.5, 240, { amount: 500000, at: 24, mode: 'reduce_emi' })
  assert.equal(changed.applied, 500000)
  assert.ok(changed.revisedEmi < changed.originalEmi)
  assert.equal(changed.elapsed, 240)
})

test('zero-rate hand-calculated prepayment effects', () => {
  const shorter = amortize(120000, 0, 12, { amount: 30000, at: 3, mode: 'reduce_tenure' })
  assert.equal(shorter.elapsed, 9)
  assert.equal(shorter.interest, 0)
  const lower = amortize(120000, 0, 12, { amount: 45000, at: 3, mode: 'reduce_emi' })
  assert.equal(lower.revisedEmi, 5000)
  assert.equal(lower.elapsed, 12)
})

test('full upfront repayment has no EMI, interest or elapsed months', async () => {
  const r = await callTool(config, 'prepayment', { principal: 120000, rate: 8, months: 12, prepay_amount: 150000, at_month: 0, mode: 'reduce_tenure' })
  assert.equal(r.structuredContent.revised_emi, 0)
  assert.equal(r.structuredContent.new_interest, 0)
  assert.equal(r.structuredContent.new_tenure_months, 0)
  assert.equal(r.structuredContent.unused_prepayment, 30000)
})

test('final-month prepayment has no effect and reports unused amount', async () => {
  const r = await callTool(config, 'prepayment', { principal: 120000, rate: 0, months: 12, prepay_amount: 30000, at_month: 12, mode: 'reduce_emi' })
  assert.equal(r.structuredContent.prepayment_applied, 0)
  assert.equal(r.structuredContent.unused_prepayment, 30000)
  assert.equal(r.structuredContent.months_saved, 0)
})

test('zero prepayment preserves original loan', () => {
  const a = amortize(5000000, 8.5, 240)
  const b = amortize(5000000, 8.5, 240, { amount: 0, at: 24, mode: 'reduce_emi' })
  near(a.interest, b.interest)
  near(a.originalEmi, b.revisedEmi)
  assert.equal(b.elapsed, 240)
})

test('tool cards include static funnel links and yearly data', async () => {
  const r = await callTool(config, 'emi', { principal: 5000000, annual_rate: 8.5, months: 240 })
  assert.match(r.content[0].text, /Monthly EMI/)
  assert.equal(r.structuredContent.emi, 43391.16)
  assert.equal(r.structuredContent.card.link.url, 'https://lauki.chat/?utm_source=chatgpt&utm_medium=plugin&utm_campaign=lauki_emi&utm_content=emi--inline')
  assert.equal(r.structuredContent.yearly_amortization.length, 20)
})

test('prepayment tool returns savings card', async () => {
  const r = await callTool(config, 'prepayment', { principal: 5000000, rate: 8.5, months: 240, prepay_amount: 500000, at_month: 24, mode: 'reduce_tenure' })
  assert.ok(r.structuredContent.interest_saved > 0)
  assert.equal(r.structuredContent.card.link.url, 'https://lauki.chat/?utm_source=chatgpt&utm_medium=plugin&utm_campaign=lauki_emi&utm_content=prepayment--inline')
})

test('invalid loan values and timing return MCP errors', async () => {
  for (const args of [{ principal: -1, annual_rate: 8, months: 12 }, { principal: 100, annual_rate: -1, months: 12 }, { principal: 100, annual_rate: 8, months: 0 }, { principal: 100, annual_rate: 8, months: 2.5 }]) {
    assert.equal((await callTool(config, 'emi', args)).isError, true)
  }
  assert.equal((await callTool(config, 'prepayment', { principal: 100, rate: 8, months: 12, prepay_amount: 50, at_month: 13, mode: 'reduce_emi' })).isError, true)
})
