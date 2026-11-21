import type { PluginConfig, ToolResult } from './core/types.ts'
import { funnelLink } from './core/utm.ts'
import { checkDate as validateDate, findPlace, fmtTime, placeLabel } from './core/geo.ts'
import { abhijit, lunarMonth, moonNakshatra, siderealLon, sunDay, tithiInfo, WEEKDAY } from './core/vedic.ts'

// Conservative rules synthesized from classical Panchanga election principles described at:
// https://dekhopanchang.com/en/learn/muhurta-selection and Muhurta Prakarana references.
// These are screening rules, not a replacement for a family astrologer's complete election.
const GUIDANCE = 'General guidance from the classical rules; confirm the final muhurat with your family astrologer.'
const PURPOSES: string[] = ['griha_pravesh', 'vivah', 'vehicle', 'property', 'mundan']

type Purpose = typeof PURPOSES[number]
type RuleSet = { label: string; tithis: number[]; nakshatras: string[]; weekdays: number[]; seasonalBlock: boolean }

const RULES: Record<Purpose, RuleSet> = {
  griha_pravesh: {
    label: 'Griha Pravesh',
    tithis: [2, 3, 5, 7, 10, 11, 12, 13],
    nakshatras: ['Rohini', 'Mrigashira', 'Anuradha', 'Revati', 'Uttara Phalguni', 'Uttara Ashadha', 'Uttara Bhadrapada', 'Chitra', 'Dhanishta'],
    weekdays: [1, 3, 4, 5],
    seasonalBlock: true,
  },
  vivah: {
    label: 'Vivah',
    tithis: [2, 3, 5, 7, 10, 11, 12, 13],
    nakshatras: ['Rohini', 'Mrigashira', 'Magha', 'Uttara Phalguni', 'Hasta', 'Swati', 'Anuradha', 'Mula', 'Uttara Ashadha', 'Uttara Bhadrapada', 'Revati'],
    weekdays: [1, 3, 4, 5],
    seasonalBlock: true,
  },
  vehicle: {
    label: 'Vehicle purchase',
    tithis: [2, 3, 5, 7, 10, 11, 13],
    nakshatras: ['Ashwini', 'Rohini', 'Mrigashira', 'Punarvasu', 'Pushya', 'Hasta', 'Chitra', 'Swati', 'Anuradha', 'Shravana', 'Dhanishta', 'Revati'],
    weekdays: [1, 3, 4, 5],
    seasonalBlock: false,
  },
  property: {
    label: 'Property registration',
    tithis: [2, 3, 5, 7, 10, 11, 12, 13],
    nakshatras: ['Rohini', 'Mrigashira', 'Pushya', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Anuradha', 'Shravana', 'Dhanishta', 'Revati'],
    weekdays: [1, 3, 4, 5, 6],
    seasonalBlock: false,
  },
  mundan: {
    label: 'Mundan',
    tithis: [2, 3, 5, 7, 10, 11, 13],
    nakshatras: ['Ashwini', 'Mrigashira', 'Punarvasu', 'Pushya', 'Hasta', 'Chitra', 'Swati', 'Shravana', 'Dhanishta', 'Revati'],
    weekdays: [1, 3, 4, 5],
    seasonalBlock: false,
  },
}

const DAY = 86400e3
const isoDate = (year: number, month: number, day: number) => `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`
const linkFor = (tool: string) => ({ label: config.funnel.label, url: funnelLink(config, tool) })
const within = (value: number, target: number, orb: number) => {
  const d = Math.abs(((value - target + 540) % 360) - 180)
  return d <= orb
}

function planetaryCombustion(at: Date) {
  const sun = siderealLon('Sun', at)
  const venus = siderealLon('Venus', at)
  const jupiter = siderealLon('Jupiter', at)
  return {
    venus: within(venus, sun, 10),
    jupiter: within(jupiter, sun, 11),
    any: within(venus, sun, 10) || within(jupiter, sun, 11),
  }
}

function evaluateDate(purpose: Purpose, date: string, city: string) {
  validateDate(date)
  const place = findPlace(city)
  const day = sunDay(date, place.lat, place.lon, place.tz)
  const tithi = tithiInfo(day.sunrise)
  const nakshatra = moonNakshatra(day.sunrise)
  const lunar = lunarMonth(day.sunrise)
  const weekday = day.weekday
  const rules = RULES[purpose]
  const sunSign = Math.floor(siderealLon('Sun', day.sunrise) / 30)
  const kharmas = sunSign === 8 || sunSign === 11
  // Chaturmas = Devshayani (Ashadha Shukla 11) to Devutthana (Kartika Shukla 11, released ON that day). Amanta months, tithi index 1-30.
  // Fix Oct 2 2026: was whole months Ashadha-Ashwin, which admitted Kartika Shukla 1-10 (e.g. 2026-11-11) and blocked Ashadha Shukla 1-10.
  const chaturmas = (lunar.amanta === 'Ashadha' && tithi.index >= 11) || ['Shravana', 'Bhadrapada', 'Ashwin'].includes(lunar.amanta) || (lunar.amanta === 'Kartika' && tithi.index < 11)
  // tithi.index is 1-30 (Krishna = 16-30); rules list paksha-relative tithis 1-15, Amavasya (30) never passes. Fix Oct 2 2026: Krishna tithis never matched.
  const pakshaTithi = tithi.index === 30 ? 30 : ((tithi.index - 1) % 15) + 1
  const combustion = planetaryCombustion(day.sunrise)
  const factors = {
    tithi: { value: `${tithi.paksha} ${tithi.name}`, pass: rules.tithis.includes(pakshaTithi) },
    nakshatra: { value: nakshatra.name, pass: rules.nakshatras.includes(nakshatra.name) },
    weekday: { value: WEEKDAY[weekday], pass: rules.weekdays.includes(weekday) },
    kharmas: { value: kharmas ? 'Kharmas active' : 'No Kharmas', pass: !kharmas },
    adhikMaas: { value: lunar.adhik ? 'Adhik Maas active' : 'Regular lunar month', pass: !lunar.adhik },
    chaturmas: { value: chaturmas ? 'Chaturmas active' : 'Outside Chaturmas', pass: !rules.seasonalBlock || !chaturmas },
    combust: { value: combustion.any ? `Combust: ${[combustion.venus ? 'Venus' : '', combustion.jupiter ? 'Jupiter' : ''].filter(Boolean).join(', ')}` : 'Venus and Jupiter not combust', pass: !combustion.any },
  }
  const passed = Object.values(factors).every((factor) => factor.pass)
  const window = abhijit(day)
  return { date, place, day, lunar, tithi, nakshatra, weekday, passed, factors, window, combustion, kharmas, chaturmas }
}

function factorRows(result: ReturnType<typeof evaluateDate>) {
  return Object.entries(result.factors).map(([name, factor]) => [name, `${factor.pass ? 'Pass' : 'Excluded'}: ${factor.value}`] as [string, string])
}

function resultCard(purpose: Purpose, result: ReturnType<typeof evaluateDate>, tool: string): ToolResult {
  const rule = RULES[purpose]
  const status = result.passed ? 'Passes conservative screening' : 'Does not pass conservative screening'
  const window = `${fmtTime(result.window.start, result.place.tz)}-${fmtTime(result.window.end, result.place.tz)}`
  return {
    text: `${rule.label} on ${result.date} in ${placeLabel(result.place)}: ${status}. ${GUIDANCE}`,
    data: {
      purpose,
      date: result.date,
      city: placeLabel(result.place),
      passed: result.passed,
      factors: result.factors,
      suggestedWindow: window,
      guidance: GUIDANCE,
    },
    card: {
      title: `${rule.label}: ${result.passed ? 'Screened as suitable' : 'Excluded by screening'}`,
      subtitle: `${result.date} · ${placeLabel(result.place)}`,
      highlight: { label: 'Suggested daytime window', value: window },
      rows: factorRows(result),
      note: GUIDANCE,
      link: linkFor(tool),
    },
  }
}

function monthDates(month: number, year: number) {
  const start = new Date(Date.UTC(year, month - 1, 1))
  const end = new Date(Date.UTC(year, month, 1))
  const dates: string[] = []
  for (let t = start.getTime(); t < end.getTime(); t += DAY) dates.push(new Date(t).toISOString().slice(0, 10))
  return dates
}

function findMuhurat(purpose: Purpose, month: number, year: number, city: string) {
  const results = monthDates(month, year).map((date) => evaluateDate(purpose, date, city)).filter((result) => result.passed)
  const place = findPlace(city)
  const rows = results.map((result) => [result.date, `${fmtTime(result.window.start, place.tz)}-${fmtTime(result.window.end, place.tz)}`] as [string, string])
  return {
    text: results.length ? `${RULES[purpose].label} candidates in ${year}-${String(month).padStart(2, '0')} for ${placeLabel(place)}: ${results.map((result) => result.date).join(', ')}. ${GUIDANCE}` : `No dates passed the conservative ${RULES[purpose].label} screening in ${year}-${String(month).padStart(2, '0')} for ${placeLabel(place)}. ${GUIDANCE}`,
    data: { purpose, month, year, city: placeLabel(place), dates: results.map((result) => result.date), windows: rows, guidance: GUIDANCE },
    card: { title: `${RULES[purpose].label} dates`, subtitle: `${year}-${String(month).padStart(2, '0')} · ${placeLabel(place)}`, table: { columns: ['Date', 'Suggested daytime window'], rows }, note: GUIDANCE, link: linkFor('find_muhurat') },
  }
}

export const config: PluginConfig = {
  slug: 'naksha-muhurat',
  name: 'Naksha Muhurat',
  version: '1.0.0',
  shortDescription: 'Screen traditional muhurat dates for marriage, housewarming, vehicles, property and mundan.',
  longDescription: 'Use conservative classical Panchanga rules to screen candidate dates for griha pravesh, vivah, vehicle purchase, property registration and mundan. Results show the passing factors and an indicative daytime window.',
  funnel: { origin: 'https://naksha.social', campaign: 'naksha_muhurat', label: 'Explore your chart in Naksha' },
  privacy: {
    dataProcessed: ['The purpose, month, year, date and city are processed in memory only.'],
    thirdParties: [],
    attributions: ['GeoNames city data, CC BY 4.0, bundled in the shared template.', 'Classical muhurta screening rules are cited in src/plugin.config.ts comments and are intentionally conservative.', 'Vedic calculations use the bundled reviewed vedic-core module.'],
    contact: 'support@naksha.social',
    minAge: 18,
    fullPolicyUrl: 'https://naksha.social/privacy',
  },
  widgetDescription: 'Shows conservative muhurat screening factors and an indicative daytime window.',
  tools: [
    {
      name: 'find_muhurat',
      title: 'Find muhurat dates',
      description: 'Use this when the user asks "griha pravesh muhurat october 2026", "shubh muhurat for marriage 2026", "vehicle purchase muhurat", "property registration muhurat", or wants screened dates for mundan. Do not use for guaranteed outcomes, personal horoscope matching, remedies, or replacing a family astrologer.',
      inputSchema: { type: 'object', properties: { purpose: { type: 'string', enum: PURPOSES, description: 'Purpose to screen.' }, month: { type: 'integer', minimum: 1, maximum: 12, description: 'Gregorian month, 1 to 12.' }, year: { type: 'integer', minimum: 1900, maximum: 2100, description: 'Gregorian year.' }, city: { type: 'string', minLength: 2, maxLength: 80, description: 'City such as Mumbai or Delhi.' } }, required: ['purpose', 'month', 'year', 'city'], additionalProperties: false },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true },
      invoking: 'Screening muhurat dates', invoked: 'Muhurat dates screened',
      samples: [{ purpose: 'griha_pravesh', month: 10, year: 2026, city: 'Mumbai' }, { purpose: 'vivah', month: 11, year: 2026, city: 'Delhi' }, { purpose: 'vehicle', month: 2, year: 2027, city: 'Pune' }],
      run: ({ purpose, month, year, city }: { purpose: Purpose; month: number; year: number; city: string }) => findMuhurat(purpose, month, year, city),
    },
    {
      name: 'check_date',
      title: 'Check a muhurat date',
      description: 'Use this when the user asks whether a specific date works for griha pravesh, marriage, vehicle purchase, property registration, or mundan in a city. Do not use for personal horoscope matching, guaranteed outcomes, remedies, or a final family tradition decision.',
      inputSchema: { type: 'object', properties: { purpose: { type: 'string', enum: PURPOSES, description: 'Purpose to screen.' }, date: { type: 'string', pattern: '^\\d{4}-\\d{2}-\\d{2}$', description: 'Local Gregorian date in YYYY-MM-DD.' }, city: { type: 'string', minLength: 2, maxLength: 80, description: 'City such as Mumbai or Delhi.' } }, required: ['purpose', 'date', 'city'], additionalProperties: false },
      annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true },
      invoking: 'Checking the date', invoked: 'Date checked',
      samples: [{ purpose: 'vehicle', date: '2026-10-05', city: 'Mumbai' }, { purpose: 'property', date: '2026-11-05', city: 'Delhi' }, { purpose: 'mundan', date: '2027-02-17', city: 'Pune' }],
      run: ({ purpose, date, city }: { purpose: Purpose; date: string; city: string }) => resultCard(purpose, evaluateDate(purpose, date, city), 'check_date'),
    },
  ],
}

export { evaluateDate, findMuhurat, planetaryCombustion, RULES }
