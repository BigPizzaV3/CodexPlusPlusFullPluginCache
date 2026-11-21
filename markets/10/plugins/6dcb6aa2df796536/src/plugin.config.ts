import type { PluginConfig, ToolResult, Schema } from './core/types.ts'
import { funnelLink } from './core/utm.ts'

const DISCLAIMER = 'Illustrative only. Returns are not guaranteed. Not investment advice. Taxes, fees and inflation are excluded.'
const COMPOUNDING = 'Monthly compounding: the entered annual rate is nominal, divided by 12 (12% means 1% monthly, about 12.68% effective annually). It is not an effective annual CAGR.'
const TIMING = 'SIP payments are made at the beginning of each month; valuation is at the end of the final month. Annual step-up starts with payment 13, then 25, and so on.'
const money = (n: number) => '₹' + n.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
const round = (n: number) => Math.round(n * 100) / 100
const amountSchema: Schema = { type: 'number', minimum: 0, maximum: 1e10, description: 'Amount in INR, entered as a number; 1 crore = 10000000.' }
const rateSchema: Schema = { type: 'number', minimum: -99, maximum: 100, description: 'Assumed nominal annual return percentage, e.g. 12 means 12% per year, compounded at 1% monthly. Not effective annual CAGR; not a guaranteed return.' }
const yearsSchema: Schema = { type: 'number', minimum: 1 / 12, maximum: 50, description: 'Duration in years, between one month and 50 years. Must correspond to a whole number of months, e.g. 1.5 = 18 months.' }

export function monthCount(years: number): number {
  const months = Math.round(years * 12)
  if (!Number.isFinite(years) || months < 1 || months > 600 || Math.abs(years * 12 - months) > 1e-8) throw new Error('years must represent a whole number of months between 1 and 600')
  return months
}
export function calculateSip(monthly: number, annualReturn: number, years: number, stepUpPct = 0) {
  const months = monthCount(years), growth = 1 + annualReturn / 1200
  let invested = 0, value = 0
  for (let m = 0; m < months; m++) {
    const contribution = monthly * Math.pow(1 + stepUpPct / 100, Math.floor(m / 12))
    invested += contribution
    value = (value + contribution) * growth
  }
  return { invested, value, months }
}
function result(tool: string, title: string, data: Record<string, number | string>, rows: [string, string][], timing = ''): ToolResult {
  const note = [COMPOUNDING, timing, DISCLAIMER].filter(Boolean).join(' ')
  return {
    text: `${title}. ${rows.map(([label, value]) => `${label}: ${value}`).join('; ')}. ${note}`,
    data: { ...data, currency: 'INR', compounding: COMPOUNDING, timing, disclaimer: DISCLAIMER },
    card: { title, rows, note, link: { label: config.funnel.label, url: funnelLink(config, tool) } },
  }
}

export const config: PluginConfig = {
  slug: 'lauki-sip',
  name: 'Lauki SIP Calculator',
  version: '1.0.0',
  shortDescription: 'Calculate SIP, annual step-up SIP, lumpsum growth and monthly savings for a target.',
  longDescription: 'Use this when calculating "sip calculator 5000 per month 10 years 12%", "step up sip", "lumpsum return calculator", or "how much to invest monthly for 1 crore". Uses a stated nominal annual rate with monthly compounding. Do not use for fund recommendations, guaranteed returns, tax calculations or investment advice.',
  funnel: { origin: 'https://lauki.chat', campaign: 'lauki_sip', label: 'Need it done for you? Ask Lauki' },
  privacy: {
    dataProcessed: ['Investment amounts, assumed annual return, duration, target and optional annual contribution step-up, processed in memory.'],
    thirdParties: [],
    attributions: [],
    operator: 'Upsurge Labs Pte. Ltd., Singapore', minAge: 18, fullPolicyUrl: 'https://lauki.ai/privacy/', contact: 'hi@lauki.ai',
  },
  widgetDescription: 'Shows illustrative invested capital, projected value or monthly contribution required, with the compounding convention and disclaimer.',
  tools: [
    {
      name: 'sip', title: 'SIP and step-up SIP calculator',
      description: 'Use this when the user asks "sip calculator 5000 per month 10 years 12%" or "step up sip" to estimate monthly investment growth with an optional annual percentage increase. Assumes beginning-of-month payments and nominal annual return divided by 12. Do not use for fund selection, guaranteed returns, tax calculations or investment advice.',
      inputSchema: { type: 'object', properties: { monthly: amountSchema, annual_return: rateSchema, years: yearsSchema, step_up_pct: { type: 'number', minimum: 0, maximum: 100, default: 0, description: 'Annual contribution increase in percent; 10 increases the monthly amount by 10% starting in month 13, and again every 12 months.' } }, required: ['monthly', 'annual_return', 'years'], additionalProperties: false },
      samples: [{ monthly: 5000, annual_return: 12, years: 10 }, { monthly: 5000, annual_return: 12, years: 10, step_up_pct: 10 }, { monthly: 10000, annual_return: 0, years: 5 }],
      run: ({ monthly, annual_return, years, step_up_pct = 0 }) => {
        const { invested, value, months } = calculateSip(monthly, annual_return, years, step_up_pct)
        return result('sip', 'Illustrative SIP projection', { invested: round(invested), value: round(value), gain: round(value - invested), months, monthly, annual_return, step_up_pct }, [['Initial monthly contribution', money(monthly)], ['Invested', money(invested)], ['Projected value', money(value)], ['Projected gain / loss', money(value - invested)], ['Duration', `${months} months`], ['Nominal annual return', `${annual_return}%`], ['Annual contribution step-up', `${step_up_pct}%`]], TIMING)
      },
    },
    {
      name: 'goal_sip', title: 'Monthly SIP for a goal',
      description: 'Use this when the user asks "how much to invest monthly for 1 crore" or needs a constant monthly SIP for a target amount, duration and assumed nominal annual return. Do not use for personalized investment advice, fund recommendations, guaranteed outcomes or inflation-adjusted goals.',
      inputSchema: { type: 'object', properties: { target: amountSchema, years: yearsSchema, annual_return: rateSchema }, required: ['target', 'years', 'annual_return'], additionalProperties: false },
      samples: [{ target: 10000000, years: 10, annual_return: 12 }, { target: 120000, years: 1, annual_return: 0 }],
      run: ({ target, years, annual_return }) => {
        const factor = calculateSip(1, annual_return, years)
        const exact = target / factor.value
        const monthly = Math.ceil(exact * 100) / 100
        const projected = calculateSip(monthly, annual_return, years)
        return result('goal_sip', 'Illustrative monthly SIP for your goal', { monthly, monthly_exact: exact, target, months: factor.months, annual_return, invested: round(projected.invested), value: round(projected.value) }, [['Target (future nominal rupees)', money(target)], ['Monthly contribution needed', money(monthly)], ['Total contributions', money(projected.invested)], ['Projected value', money(projected.value)], ['Duration', `${factor.months} months`], ['Nominal annual return', `${annual_return}%`]], 'Constant beginning-of-month contributions; no annual step-up. Monthly contribution is rounded up to the next paise. The target is not adjusted for inflation.')
      },
    },
    {
      name: 'lumpsum', title: 'Lumpsum return calculator',
      description: 'Use this when the user asks "lumpsum return calculator" to estimate future value of a single investment using monthly compounding of a nominal annual rate. Do not use for guaranteed returns, tax calculations, effective annual CAGR inputs or fund recommendations.',
      inputSchema: { type: 'object', properties: { amount: amountSchema, rate: rateSchema, years: yearsSchema }, required: ['amount', 'rate', 'years'], additionalProperties: false },
      samples: [{ amount: 100000, rate: 12, years: 10 }, { amount: 250000, rate: 8, years: 5 }],
      run: ({ amount, rate, years }) => {
        const months = monthCount(years)
        const value = amount * Math.pow(1 + rate / 1200, months)
        return result('lumpsum', 'Illustrative lumpsum projection', { invested: amount, value: round(value), gain: round(value - amount), months, rate }, [['Invested', money(amount)], ['Projected value', money(value)], ['Projected gain / loss', money(value - amount)], ['Duration', `${months} months`], ['Nominal annual return', `${rate}%`]], 'One investment at the start; no additional contributions.')
      },
    },
  ],
}
