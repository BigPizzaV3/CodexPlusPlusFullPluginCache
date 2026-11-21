import type { PluginConfig, ToolResult } from './core/types.ts'
import { funnelLink } from './core/utm.ts'

// Official baseline: CBIC Notification 9/2025-Integrated Tax (Rate), 17 Sep 2025,
// corrected 18 Sep 2025, schedules I-VII, effective 22 Sep 2025.
// https://courier.cbic.gov.in/ECCS/advisory/2025/NOTIFICATION%20NO.%209_2025-INTEGRATED%20TAX%20(RATE)%20-1759486719.pdf
// Page 1 explicitly lists 5,18,40,3,0.25,1.5 and a transitional 28% schedule.
// PIB effective-date FAQ, 21 Sep 2025 (NoteId 155252):
// https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=4&NoteId=155252&lang=1&reg=20
// This is a versioned baseline, NOT an assertion that all later amendments were checked.
export const SLABS = { main: [5, 18], specialHigh: [40], nilOrExempt: [0], special: [0.25, 3], additionalSpecial: [1.5] }
const SOURCE = 'CBIC Notification 9/2025-Integrated Tax (Rate), 17 Sep 2025, corrected 18 Sep; PIB GST Simplified FAQ, 21 Sep 2025.'
const SLAB_NOTE = 'Bundled GST 2.0 baseline effective 22 September 2025, not a live rate lookup. CBIC also listed 1.5% and a transitional 28% schedule; later changes and special schemes are not fully verified here. Verify current CBIC notifications for your supply and invoice date. No HSN-level classification is provided. Nil/exempt is not the same legal treatment as zero-rated supply.'
const CALC_NOTE = 'Arithmetic estimate using your supplied rate, not a determination of the applicable tax rate or place of supply. No cess, ITC, surcharge or filing rounding included. Amounts use nearest-paise half-up rounding; any odd tax paise goes to CGST so displayed components reconcile. Intrastate CGST/SGST assumes a state transaction; UTGST is not modelled.'
const money = (n: number) => `INR ${n.toFixed(2)}`
function roundedDivide(n: bigint, d: bigint) { return (n * 2n + d) / (d * 2n) }
function units(n: number, precision: number, name: string): bigint {
  if (!Number.isFinite(n) || n < 0 || Math.abs(n - Number(n.toFixed(precision))) > 1e-9) throw new Error(`${name} must be non-negative with at most ${precision} decimal places`)
  return BigInt(n.toFixed(precision).replace('.', ''))
}
export function calculateGST(amount: number, rate: number, mode: 'add' | 'remove', interstate = false) {
  if (amount > 1e12 || rate > 100 || !['add', 'remove'].includes(mode)) throw new Error('Amount, rate or mode is out of range')
  const cents = units(amount, 2, 'amount')
  const r = units(rate, 4, 'rate')
  const scale = 1000000n // 100 percent times 10,000 rate units
  const baseCents = mode === 'add' ? cents : roundedDivide(cents * scale, scale + r)
  const taxCents = mode === 'add' ? roundedDivide(baseCents * r, scale) : cents - baseCents
  const totalCents = baseCents + taxCents
  const cgst = interstate ? 0n : (taxCents + 1n) / 2n
  const sgst = interstate ? 0n : taxCents - cgst
  const toMoney = (n: bigint) => Number(n) / 100
  return {
    amount, rate, mode, interstate, currency: 'INR',
    base: toMoney(baseCents), tax: toMoney(taxCents), total: toMoney(totalCents),
    CGST: toMoney(cgst), SGST: toMoney(sgst), IGST: interstate ? toMoney(taxCents) : 0,
    componentRate: interstate ? rate : rate / 2,
    rounding: 'nearest paise, half up; split remainder allocated to CGST',
  }
}
export const config: PluginConfig = {
  slug: 'lauki-gst-calc', name: 'Lauki GST Calculator', version: '1.0.0',
  shortDescription: 'Add or remove Indian GST and show CGST/SGST or IGST with a dated slab reference.',
  longDescription: 'Use this when you need a gst calculator, 18 gst on 5000, remove gst from 1180, cgst sgst split, or igst on interstate. Calculates using a user-supplied rate and provides a dated GST 2.0 slab reference. Do not use for HSN classification, legal tax advice, GST returns, cess, ITC eligibility or live rate verification.',
  funnel: { origin: 'https://lauki.chat', campaign: 'lauki_gst_calc', label: 'Need it done for you? Ask Lauki' },
  privacy: { dataProcessed: ['Amount, supplied percentage rate, add/remove mode and interstate flag; processed in memory.'], thirdParties: [], attributions: [SOURCE], operator: 'Upsurge Labs Pte. Ltd., Singapore', minAge: 18, fullPolicyUrl: 'https://lauki.ai/privacy/', contact: 'hi@lauki.ai' },
  widgetDescription: 'Shows base, GST, total and the CGST/SGST or IGST split, with rounding and rate-verification notes.',
  tools: [
    {
      name: 'gst', title: 'Add or remove GST',
      description: 'Use this when the user asks for a gst calculator, "18 gst on 5000", "remove gst from 1180", "cgst sgst split", or "igst on interstate". Ask for the rate if missing; never infer it from an amount or product. Add mode takes the pre-tax base; remove mode takes the GST-inclusive total. Defaults to intrastate CGST/SGST if interstate is omitted. Do not use for HSN-level rates, tax filing, place-of-supply decisions, cess, UTGST or ITC calculations.',
      inputSchema: { type: 'object', properties: {
        amount: { type: 'number', minimum: 0, maximum: 1e12, description: 'INR amount, up to two decimal places; base for add, inclusive total for remove.' },
        rate: { type: 'number', minimum: 0, maximum: 100, description: 'Total GST percentage supplied by the user, e.g. 18, not 0.18; up to four decimal places. This is not a rate-classification service.' },
        mode: { type: 'string', enum: ['add', 'remove'], description: 'add GST to base or remove included GST from total.' },
        interstate: { type: 'boolean', default: false, description: 'true = IGST; false (default) = intrastate CGST and SGST. User must confirm place-of-supply treatment.' },
      }, required: ['amount', 'rate', 'mode'], additionalProperties: false },
      invoking: 'Calculating GST', invoked: 'GST calculated',
      samples: [{ amount: 5000, rate: 18, mode: 'add' }, { amount: 1180, rate: 18, mode: 'remove' }, { amount: 10000, rate: 5, mode: 'add', interstate: true }],
      run: ({ amount, rate, mode, interstate }: { amount: number; rate: number; mode: 'add' | 'remove'; interstate: boolean }): ToolResult => {
        const d = calculateGST(amount, rate, mode, interstate)
        const split: [string, string][] = d.interstate ? [[`IGST (${rate}%)`, money(d.IGST)]] : [[`CGST (${d.componentRate}%)`, money(d.CGST)], [`SGST (${d.componentRate}%)`, money(d.SGST)]]
        return { text: `Base ${money(d.base)}; GST at ${rate}% ${money(d.tax)}; total ${money(d.total)}. ${split.map(([k, v]) => `${k}: ${v}`).join('; ')}. ${CALC_NOTE}`, data: d,
          card: { title: mode === 'add' ? 'GST added' : 'GST removed from inclusive total', subtitle: `${rate}% GST | ${d.interstate ? 'Interstate IGST' : 'Intrastate CGST + SGST (default unless specified)'}`, highlight: { label: 'Total including GST', value: money(d.total) }, rows: [['Base before GST', money(d.base)], ['Total GST', money(d.tax)], ...split], note: CALC_NOTE, link: { label: config.funnel.label, url: funnelLink(config, 'gst') } } }
      },
    },
    {
      name: 'rate_slabs', title: 'GST slab reference',
      description: 'Use this when the user asks for current GST slabs, GST 2.0 rates or the September 22 2025 GST rationalisation. Returns a dated official baseline: main 5%/18%, special 40%, nil/exempt 0%, special 3%/0.25%, and an additional 1.5% schedule, with a current-law verification warning. Do not use for HSN or product-specific rate claims, a complete list of every special scheme, or live verification of later amendments.',
      inputSchema: { type: 'object', properties: {}, additionalProperties: false },
      invoking: 'Reading bundled GST slabs', invoked: 'GST slab reference ready', samples: [{}],
      run: (): ToolResult => ({ text: `GST 2.0 baseline: main slabs 5% and 18%; special high rate 40%; nil/exempt 0%; special rates 3% and 0.25%; additional special schedule 1.5%. ${SLAB_NOTE} Source: ${SOURCE}`, data: { ...SLABS, baselineEffective: '2025-09-22', sourcesChecked: '2026-10-01', liveVerified: false, source: SOURCE, caveat: SLAB_NOTE },
        card: { title: 'GST 2.0 slab reference', subtitle: 'Dated baseline, not live-verified current law', rows: [['Main slabs', '5% / 18%'], ['Special high rate', '40%'], ['Nil / exempt', '0%'], ['Special rates', '3% / 0.25%'], ['Additional special schedule', '1.5%'], ['Baseline effective', '22 September 2025'], ['Source', SOURCE]], note: SLAB_NOTE, link: { label: config.funnel.label, url: funnelLink(config, 'rate_slabs') } } }),
    },
  ],
}
