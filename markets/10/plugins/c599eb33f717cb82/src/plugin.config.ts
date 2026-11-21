import type { PluginConfig, Schema, ToolResult } from './core/types.ts'
import { funnelLink } from './core/utm.ts'

const round = (n: number) => Math.round((n + Number.EPSILON) * 100) / 100
const money = (n: number) => `₹${n.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`
const note = 'Illustrative fixed-rate reducing-balance calculation in INR, with monthly interest and payments at month-end. Fees, taxes, insurance, rate changes and lender-specific rounding are excluded. Not financial advice.'
export function monthlyEmi(principal: number, annualRate: number, months: number): number {
  const r = annualRate / 1200
  return r === 0 ? principal / months : principal * r / -Math.expm1(-months * Math.log1p(r))
}
type Year = { year: number; opening_balance: number; principal_paid: number; interest_paid: number; prepayment: number; closing_balance: number }
type Prepay = { amount: number; at: number; mode: 'reduce_tenure' | 'reduce_emi' }
export function amortize(principal: number, annualRate: number, months: number, prepay?: Prepay) {
  const originalEmi = monthlyEmi(principal, annualRate, months)
  let payment = originalEmi, balance = principal, interest = 0, applied = 0, elapsed = 0, lastPayment = 0
  const yearly: Year[] = []
  // at=0 is before any scheduled EMI; at=k is immediately after EMI k.
  function apply(at: number) {
    if (!prepay || prepay.at !== at) return 0
    const extra = Math.min(balance, prepay.amount)
    balance = Math.max(0, balance - extra)
    applied = extra
    if (prepay.mode === 'reduce_emi') payment = balance > 0 && months > at ? monthlyEmi(balance, annualRate, months - at) : 0
    return extra
  }
  const upfront = apply(0)
  if (upfront > 0) yearly.push({ year: 1, opening_balance: principal, principal_paid: 0, interest_paid: 0, prepayment: upfront, closing_balance: balance })
  for (let m = 1; m <= months && balance > 1e-7; m++) {
    const y = Math.floor((m - 1) / 12)
    const row = yearly[y] ?? (yearly[y] = { year: y + 1, opening_balance: balance, principal_paid: 0, interest_paid: 0, prepayment: 0, closing_balance: balance })
    const monthlyInterest = balance * annualRate / 1200
    const due = balance + monthlyInterest
    const paid = m === months ? due : Math.min(payment, due)
    const paidPrincipal = paid - monthlyInterest
    balance = Math.max(0, balance - paidPrincipal)
    if (balance < 1e-7) balance = 0
    interest += monthlyInterest
    row.principal_paid += paidPrincipal
    row.interest_paid += monthlyInterest
    row.prepayment += apply(m)
    row.closing_balance = balance
    elapsed = m
    lastPayment = paid
  }
  return { originalEmi, revisedEmi: payment, interest, applied, elapsed, lastPayment, balance, yearly }
}
function table(yearly: Year[]) {
  return { columns: ['Loan year', 'Opening balance', 'Principal in EMIs', 'Interest', 'Prepayment', 'Closing balance'], rows: yearly.map(y => [String(y.year), money(y.opening_balance), money(y.principal_paid), money(y.interest_paid), money(y.prepayment), money(y.closing_balance)]) }
}
function rowsData(yearly: Year[]) {
  return yearly.map(y => ({ year: y.year, opening_balance: round(y.opening_balance), principal_paid: round(y.principal_paid), interest_paid: round(y.interest_paid), prepayment: round(y.prepayment), closing_balance: round(y.closing_balance) }))
}
const principalSchema: Schema = { type: 'number', minimum: 1, maximum: 1e10, description: 'Loan principal in INR; 50 lakh = 5000000. Do not include fees.' }
const rateSchema: Schema = { type: 'number', minimum: 0, maximum: 60, description: 'Nominal annual interest percentage, e.g. 8.5 means 8.5% per year, not 0.085.' }
const monthsSchema: Schema = { type: 'integer', minimum: 1, maximum: 600, description: 'Original number of monthly payments; 20 years = 240 months.' }

export const config: PluginConfig = {
  slug: 'lauki-emi', name: 'Lauki EMI Calculator', version: '1.0.0',
  shortDescription: 'Calculate monthly loan EMI, total interest, yearly amortization and one-time prepayment savings.',
  longDescription: 'Use this when calculating home or car loan EMI, total interest or prepayment savings at a supplied fixed annual rate. Includes yearly amortization and tenure or EMI reduction comparisons. Do not use for lender quotes, credit eligibility, floating-rate forecasts or financial advice.',
  funnel: { origin: 'https://lauki.chat', campaign: 'lauki_emi', label: 'Need it done for you? Ask Lauki' },
  privacy: { dataProcessed: ['Loan amount, interest rate, loan duration and optional prepayment amount, timing and mode, processed in memory.'], thirdParties: [], attributions: [], operator: 'Upsurge Labs Pte. Ltd., Singapore', minAge: 18, fullPolicyUrl: 'https://lauki.ai/privacy/', contact: 'hi@lauki.ai' },
  widgetDescription: 'Shows monthly EMI, total interest, annual amortization and the effect of a single prepayment.',
  tools: [
    {
      name: 'emi', title: 'Loan EMI and interest',
      description: 'Use this when the user asks "emi for 50 lakh home loan 20 years 8.5%", "car loan emi", or "how much interest will i pay". Calculates monthly reducing-balance EMI, total interest and a yearly amortization table in INR from the supplied fixed rate. Do not use for lender offers, eligibility, floating-rate predictions or financial advice.',
      inputSchema: { type: 'object', properties: { principal: principalSchema, annual_rate: rateSchema, months: monthsSchema }, required: ['principal', 'annual_rate', 'months'], additionalProperties: false },
      samples: [{ principal: 5000000, annual_rate: 8.5, months: 240 }, { principal: 800000, annual_rate: 9, months: 60 }, { principal: 120000, annual_rate: 0, months: 12 }],
      run: ({ principal, annual_rate, months }): ToolResult => {
        const s = amortize(principal, annual_rate, months)
        return {
          text: `Monthly EMI: ${money(s.originalEmi)}. Total interest: ${money(s.interest)}. Total repayment: ${money(principal + s.interest)} over ${months} months. ${note}`,
          data: { principal, annual_rate, months, currency: 'INR', emi: round(s.originalEmi), total_interest: round(s.interest), total_repayment: round(principal + s.interest), yearly_amortization: rowsData(s.yearly) },
          card: { title: 'Loan EMI calculation', subtitle: `${months} months at ${annual_rate}% per year`, highlight: { label: 'Monthly EMI', value: money(s.originalEmi) }, rows: [['Principal', money(principal)], ['Total interest', money(s.interest)], ['Total repayment', money(principal + s.interest)]], table: table(s.yearly), note, link: { label: config.funnel.label, url: funnelLink(config, 'emi') } }
        }
      }
    },
    {
      name: 'prepayment', title: 'Prepayment savings',
      description: 'Use this when the user asks about "prepayment savings", paying off a home or car loan early, or reducing EMI after a lump-sum payment. Compare a single prepayment with the original fixed-rate loan, choosing reduce_tenure or reduce_emi. Do not use for lender-specific charges, multiple prepayments, variable interest rates or financial advice.',
      inputSchema: { type: 'object', properties: { principal: principalSchema, rate: rateSchema, months: monthsSchema, prepay_amount: { type: 'number', minimum: 0, maximum: 1e10, description: 'One-time INR prepayment. Capped at the outstanding principal; any unused amount is reported.' }, at_month: { type: 'integer', minimum: 0, maximum: 600, description: 'Apply immediately after this numbered EMI (1-based); 0 means before the first EMI. Must not exceed original months.' }, mode: { type: 'string', enum: ['reduce_tenure', 'reduce_emi'], description: 'Keep EMI and finish earlier, or keep remaining term and recalculate EMI.' } }, required: ['principal', 'rate', 'months', 'prepay_amount', 'at_month', 'mode'], additionalProperties: false },
      samples: [{ principal: 5000000, rate: 8.5, months: 240, prepay_amount: 500000, at_month: 24, mode: 'reduce_tenure' }, { principal: 5000000, rate: 8.5, months: 240, prepay_amount: 500000, at_month: 24, mode: 'reduce_emi' }, { principal: 800000, rate: 9, months: 60, prepay_amount: 100000, at_month: 12, mode: 'reduce_tenure' }],
      run: ({ principal, rate, months, prepay_amount, at_month, mode }): ToolResult => {
        if (at_month > months) throw new Error('at_month must not exceed months.')
        const base = amortize(principal, rate, months)
        const changed = amortize(principal, rate, months, { amount: prepay_amount, at: at_month, mode })
        const saving = Math.max(0, base.interest - changed.interest)
        const nextEmi = changed.applied >= (principal - 1e-7) && at_month === 0 || changed.elapsed <= at_month ? 0 : changed.revisedEmi
        const assumptions = `${note} Prepayment is applied ${at_month === 0 ? 'before the first EMI' : `after EMI ${at_month}`}. The last EMI may be smaller. Calculations retain full precision; displayed amounts are rounded to paise.`
        return {
          text: `Interest saved: ${money(saving)}. Original EMI: ${money(base.originalEmi)}; subsequent EMI: ${money(nextEmi)}. Loan finishes in ${changed.elapsed} months (${months - changed.elapsed} months saved). Prepayment applied: ${money(changed.applied)}. ${assumptions}`,
          data: { principal, rate, months, prepay_amount, at_month, mode, currency: 'INR', original_emi: round(base.originalEmi), revised_emi: round(nextEmi), original_interest: round(base.interest), new_interest: round(changed.interest), interest_saved: round(saving), prepayment_applied: round(changed.applied), unused_prepayment: round(Math.max(0, prepay_amount - changed.applied)), new_tenure_months: changed.elapsed, months_saved: months - changed.elapsed, final_payment: round(changed.lastPayment), total_repayment: round(principal + changed.interest), yearly_amortization: rowsData(changed.yearly) },
          card: { title: 'Prepayment comparison', subtitle: mode === 'reduce_tenure' ? 'Keep EMI, reduce tenure' : 'Keep term, reduce EMI', highlight: { label: 'Interest saved', value: money(saving) }, rows: [['Original EMI', money(base.originalEmi)], ['Subsequent EMI', money(nextEmi)], ['Original interest', money(base.interest)], ['New interest', money(changed.interest)], ['New tenure from loan start', `${changed.elapsed} months`], ['Months saved', String(months - changed.elapsed)], ['Prepayment applied', money(changed.applied)], ['Unused prepayment', money(Math.max(0, prepay_amount - changed.applied))], ['Total paid, including prepayment', money(principal + changed.interest)]], table: table(changed.yearly), note: assumptions, link: { label: config.funnel.label, url: funnelLink(config, 'prepayment') } }
        }
      }
    }
  ]
}
