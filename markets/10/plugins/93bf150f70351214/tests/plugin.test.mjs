import test from 'node:test'
import assert from 'node:assert/strict'
import { config, calculateGST } from '../src/plugin.config.ts'
import { callTool } from '../src/core/mcp.ts'

// Source for slab list: CBIC Notification 9/2025-Integrated Tax (Rate), page 1:
// https://courier.cbic.gov.in/ECCS/advisory/2025/NOTIFICATION%20NO.%209_2025-INTEGRATED%20TAX%20(RATE)%20-1759486719.pdf
// Effective-date source: https://www.pib.gov.in/PressNoteDetails.aspx?NoteId=155252
// Independent arithmetic: tax=base*rate/100; inclusive base=total*100/(100+rate).
// 5000*18/100=900; 1180*100/118=1000; 10000*5/100=500.
test('add 18% intrastate GST to INR 5,000', () => {
  assert.deepEqual(calculateGST(5000, 18, 'add', false), {
    amount: 5000, rate: 18, mode: 'add', interstate: false, currency: 'INR',
    base: 5000, tax: 900, total: 5900, CGST: 450, SGST: 450, IGST: 0,
    componentRate: 9, rounding: 'nearest paise, half up; split remainder allocated to CGST',
  })
})
test('remove included 18% GST from INR 1,180', () => {
  const d = calculateGST(1180, 18, 'remove', false)
  assert.equal(d.base, 1000); assert.equal(d.tax, 180); assert.equal(d.total, 1180)
  assert.equal(d.CGST, 90); assert.equal(d.SGST, 90)
})
test('interstate 5% is IGST only', () => {
  const d = calculateGST(10000, 5, 'add', true)
  assert.equal(d.base, 10000); assert.equal(d.tax, 500); assert.equal(d.total, 10500)
  assert.equal(d.IGST, 500); assert.equal(d.CGST, 0); assert.equal(d.SGST, 0)
})
test('odd paise split reconciles', () => {
  const d = calculateGST(0.10, 5, 'add', false)
  assert.equal(d.tax, 0.01); assert.equal(d.CGST + d.SGST, d.tax)
})
test('zero rate and zero amount are exact', () => {
  for (const mode of ['add', 'remove']) {
    const d = calculateGST(1180, 0, mode, true)
    assert.equal(d.base, 1180); assert.equal(d.total, 1180); assert.equal(d.tax, 0)
    assert.equal(calculateGST(0, 40, mode).total, 0)
  }
})
test('special rates and inclusive half-up rounding', () => {
  assert.equal(calculateGST(10000, 0.25, 'add', true).IGST, 25)
  assert.equal(calculateGST(10000, 1.5, 'add', true).IGST, 150)
  assert.equal(calculateGST(10000, 3, 'add', true).IGST, 300)
  assert.equal(calculateGST(100, 40, 'add', true).total, 140)
  const d = calculateGST(100, 18, 'remove')
  assert.equal(d.base, 84.75); assert.equal(d.tax, 15.25)
  assert.equal(d.CGST, 7.63); assert.equal(d.SGST, 7.62)
})
test('reject invalid precision and non-finite values', () => {
  assert.throws(() => calculateGST(1.001, 18, 'add'), /decimal/)
  assert.throws(() => calculateGST(-1, 18, 'add'))
  assert.throws(() => calculateGST(Infinity, 18, 'add'))
  assert.throws(() => calculateGST(100, NaN, 'add'))
})
test('rate slabs returns dated source and card', async () => {
  const r = await callTool(config, 'rate_slabs', {})
  assert.match(r.content[0].text, /5%.*18%/s)
  assert.equal(r.structuredContent.baselineEffective, '2025-09-22')
  assert.equal(r.structuredContent.liveVerified, false)
  assert.match(r.structuredContent.source, /CBIC Notification 9\/2025/)
  assert.match(r.structuredContent.card.link.url, /utm_campaign=lauki_gst_calc/)
})
test('gst tool returns structured card and static funnel link', async () => {
  const r = await callTool(config, 'gst', { amount: 5000, rate: 18, mode: 'add' })
  assert.equal(r.structuredContent.total, 5900)
  assert.equal(r.structuredContent.CGST, 450)
  assert.match(r.structuredContent.card.link.url, /utm_content=gst--inline/)
})
