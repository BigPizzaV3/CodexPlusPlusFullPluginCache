// Keyless geocoding from the bundled GeoNames table (CC BY 4.0). No network calls, ever.
import data from '../data/cities.json' with { type: 'json' }
import { InputError } from './schema.ts'

type Row = [string, string, string, string, number, number, number, string]
const ROWS = (data as any).rows as Row[]
const ALIASES = (data as any).aliases as Record<string, number>

export type Place = { name: string; region: string; country: string; lat: number; lon: number; tz: string }

const norm = (s: string) => s.normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim()
const COUNTRY: Record<string, string> = { india: 'IN', bharat: 'IN', usa: 'US', 'united states': 'US', us: 'US', uk: 'GB', 'united kingdom': 'GB', england: 'GB', uae: 'AE', dubai: 'AE', canada: 'CA', australia: 'AU', singapore: 'SG', nepal: 'NP', 'sri lanka': 'LK', bangladesh: 'BD', pakistan: 'PK' }

/** Resolve free text like "Mumbai", "Pune, Maharashtra", "Bombay", "Austin, Texas, USA". Prefers India, then population. */
export function findPlace(text: string): Place {
  const parts = text.split(',').map(norm).filter(Boolean)
  if (!parts.length) throw new InputError('city is required')
  const city = parts[0]
  const qualifiers = parts.slice(1)
  const ccHint = qualifiers.map((q) => COUNTRY[q]).find(Boolean)
  let cands = ROWS.map((r, i) => ({ r, i })).filter(({ r }) => norm(r[0]) === city || norm(r[1]) === city)
  if (!cands.length && ALIASES[city] !== undefined) cands = [{ r: ROWS[ALIASES[city]], i: ALIASES[city] }]
  if (!cands.length) cands = ROWS.map((r, i) => ({ r, i })).filter(({ r }) => norm(r[1]).startsWith(city) && city.length >= 4)
  if (!cands.length) throw new InputError('city was not found; try the nearest large city, e.g. "Pune, India"')
  const score = ({ r }: { r: Row }) => {
    let s = Math.log10(r[6] + 10)
    if (r[2] === 'IN') s += 3
    if (ccHint && r[2] === ccHint) s += 20
    for (const q of qualifiers) if (norm(r[3]).includes(q) || norm(r[3]) === q) s += 10
    return s
  }
  cands.sort((a, b) => score(b) - score(a))
  const r = cands[0].r
  return { name: r[0], region: r[3], country: r[2], lat: r[4], lon: r[5], tz: r[7] }
}

/** Minutes east of UTC for an IANA zone at instant t (Intl works in Workers). */
export function tzOffsetMin(tz: string, t: Date): number {
  const f = new Intl.DateTimeFormat('en-US', { timeZone: tz, hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' })
  const p = Object.fromEntries(f.formatToParts(t).map((x) => [x.type, x.value]))
  const asUtc = Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour % 24, +p.minute, +p.second)
  return Math.round((asUtc - Math.floor(t.getTime() / 1000) * 1000) / 60000)
}

/** UTC instant of local wall-clock time (YYYY-MM-DD, HH:MM) in tz. */
export function localToUtc(date: string, time: string, tz: string): Date {
  const [y, m, d] = date.split('-').map(Number)
  const [hh, mm] = (time || '00:00').split(':').map(Number)
  const guess = new Date(Date.UTC(y, m - 1, d, hh, mm))
  const off1 = tzOffsetMin(tz, guess)
  const t1 = new Date(guess.getTime() - off1 * 60000)
  const off2 = tzOffsetMin(tz, t1)
  return off2 === off1 ? t1 : new Date(guess.getTime() - off2 * 60000)
}

/** "HH:MM" local wall time for instant t in tz. */
export function fmtTime(t: Date, tz: string): string {
  return new Intl.DateTimeFormat('en-GB', { timeZone: tz, hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).format(t)
}
/** "YYYY-MM-DD" local date for instant t in tz. */
export function fmtDate(t: Date, tz: string): string {
  const p = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit' }).formatToParts(t).map((x) => [x.type, x.value]))
  return `${p.year}-${p.month}-${p.day}`
}
/** Today's date in tz, YYYY-MM-DD. */
export const todayIn = (tz: string) => fmtDate(new Date(), tz)

export const DATE_RE = '^\\d{4}-\\d{2}-\\d{2}$'
export const TIME_RE = '^([01]?\\d|2[0-3]):[0-5]\\d$'
export function checkDate(s: string, field = 'date'): string {
  const [y, m, d] = s.split('-').map(Number)
  const dt = new Date(Date.UTC(y, m - 1, d))
  if (dt.getUTCFullYear() !== y || dt.getUTCMonth() !== m - 1 || dt.getUTCDate() !== d || y < 1900 || y > 2100) throw new InputError(`${field} must be a real date between 1900 and 2100`)
  return s
}
export const placeLabel = (p: Place) => [p.name, p.region, p.country].filter(Boolean).join(', ')
