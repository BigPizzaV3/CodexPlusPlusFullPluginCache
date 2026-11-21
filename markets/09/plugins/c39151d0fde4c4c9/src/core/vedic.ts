// vedic-core: the reviewed wave-2 math (outputs/chatgpt-plugin-wave2/vedic-core-reference.mjs), as a module.
// Every Vedic plugin MUST use these functions so no two plugins (or Naksha) disagree.
// Longitudes: astronomy-engine geocentric apparent, true ecliptic of date. Sidereal = tropical - Lahiri (linear, reference formula).
import * as A from 'astronomy-engine'
import { localToUtc } from './geo.ts'

export const TITHI = ['Pratipada', 'Dwitiya', 'Tritiya', 'Chaturthi', 'Panchami', 'Shashthi', 'Saptami', 'Ashtami', 'Navami', 'Dashami', 'Ekadashi', 'Dwadashi', 'Trayodashi', 'Chaturdashi', 'Purnima']
export const NAKSHATRA = ['Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha', 'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha', 'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati']
export const RASHI = ['Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya', 'Tula', 'Vrishchika', 'Dhanu', 'Makara', 'Kumbha', 'Meena']
export const RASHI_EN = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
export const YOGA = ['Vishkambha', 'Priti', 'Ayushman', 'Saubhagya', 'Shobhana', 'Atiganda', 'Sukarma', 'Dhriti', 'Shula', 'Ganda', 'Vriddhi', 'Dhruva', 'Vyaghata', 'Harshana', 'Vajra', 'Siddhi', 'Vyatipata', 'Variyana', 'Parigha', 'Shiva', 'Siddha', 'Sadhya', 'Shubha', 'Shukla', 'Brahma', 'Indra', 'Vaidhriti']
const KARANA_MOVING = ['Bava', 'Balava', 'Kaulava', 'Taitila', 'Gara', 'Vanija', 'Vishti']
export const VARA = ['Ravivara', 'Somavara', 'Mangalavara', 'Budhavara', 'Guruvara', 'Shukravara', 'Shanivara']
export const WEEKDAY = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
/** Amanta month named by the sidereal sign the Sun occupies at the new moon that starts it (index = sign). */
export const MONTH_BY_SUN_SIGN = ['Vaishakha', 'Jyeshtha', 'Ashadha', 'Shravana', 'Bhadrapada', 'Ashwin', 'Kartika', 'Margashirsha', 'Pausha', 'Magha', 'Phalguna', 'Chaitra']
export const MONTHS = ['Chaitra', 'Vaishakha', 'Jyeshtha', 'Ashadha', 'Shravana', 'Bhadrapada', 'Ashwin', 'Kartika', 'Margashirsha', 'Pausha', 'Magha', 'Phalguna']

const NAK_SPAN = 360 / 27
const mod360 = (x: number) => ((x % 360) + 360) % 360

export function lahiri(t: Date): number {
  const y = (t.getTime() - Date.UTC(2000, 0, 1, 12)) / (365.25 * 86400e3)
  return 23.853 + (50.2788 / 3600) * y
}
export type Planet = 'Sun' | 'Moon' | 'Mercury' | 'Venus' | 'Mars' | 'Jupiter' | 'Saturn'
export function tropicalLon(body: Planet, t: Date): number {
  return A.Ecliptic(A.GeoVector(A.Body[body], t, true)).elon
}
export const siderealLon = (body: Planet, t: Date) => mod360(tropicalLon(body, t) - lahiri(t))
/** Mean lunar node (Rahu); Ketu = +180. Meeus 47.7. */
export function rahuLon(t: Date, sidereal = true): number {
  const T = (t.getTime() - Date.UTC(2000, 0, 1, 12)) / (36525 * 86400e3)
  const om = mod360(125.04452 - 1934.136261 * T + 0.0020708 * T * T)
  return sidereal ? mod360(om - lahiri(t)) : om
}
export const elongation = (t: Date) => mod360(tropicalLon('Moon', t) - tropicalLon('Sun', t))
export const tithiIndex = (t: Date) => Math.floor(elongation(t) / 12) // 0..29
export function tithiInfo(t: Date) {
  const i = tithiIndex(t)
  const paksha = i < 15 ? 'Shukla' : 'Krishna'
  const name = i === 29 ? 'Amavasya' : TITHI[i % 15]
  return { index: i + 1, paksha, name }
}
export function nakshatraOf(siderealLongitude: number) {
  const i = Math.floor(siderealLongitude / NAK_SPAN)
  return { index: i + 1, name: NAKSHATRA[i], pada: Math.floor((siderealLongitude % NAK_SPAN) / (NAK_SPAN / 4)) + 1 }
}
export const moonNakshatra = (t: Date) => nakshatraOf(siderealLon('Moon', t))
export function rashiOf(siderealLongitude: number) {
  const i = Math.floor(siderealLongitude / 30)
  return { index: i + 1, name: RASHI[i], english: RASHI_EN[i], degree: +(siderealLongitude % 30).toFixed(2) }
}
export function yogaAt(t: Date) {
  const i = Math.floor(mod360(siderealLon('Sun', t) + siderealLon('Moon', t)) / NAK_SPAN)
  return { index: i + 1, name: YOGA[i] }
}
export function karanaAt(t: Date) {
  const k = Math.floor(elongation(t) / 6) // 0..59
  let name: string
  if (k === 0) name = 'Kimstughna'
  else if (k >= 57) name = ['Shakuni', 'Chatushpada', 'Naga'][k - 57]
  else name = KARANA_MOVING[(k - 1) % 7]
  return { index: k + 1, name }
}

/** First instant in (t0, t0+maxHours] where f(t) - target crosses zero going up (angles, wraps handled). */
export function findAngleCrossing(f: (t: Date) => number, target: number, t0: Date, maxHours = 36): Date | null {
  const diff = (t: Date) => ((f(t) - target + 540) % 360) - 180 // signed, in (-180,180]
  let a = t0.getTime(), da = diff(t0)
  const step = 30 * 60e3
  for (let b = a + step; b <= t0.getTime() + maxHours * 3600e3; b += step) {
    const db = diff(new Date(b))
    if (da < 0 && db >= 0 && db - da < 90) {
      let lo = a, hi = b
      for (let i = 0; i < 30; i++) { const mid = (lo + hi) / 2; if (diff(new Date(mid)) < 0) lo = mid; else hi = mid }
      return new Date(hi)
    }
    a = b; da = db
  }
  return null
}
export const tithiEnd = (t: Date) => findAngleCrossing(elongation, (tithiIndex(t) + 1) * 12 % 360, t, 40)
export const nakshatraEnd = (t: Date) => findAngleCrossing((x) => siderealLon('Moon', x), ((moonNakshatra(t).index) * NAK_SPAN) % 360, t, 40)

export type SunDay = { sunrise: Date; sunset: Date; nextSunrise: Date; weekday: number }
/** Sunrise/sunset for local calendar date (YYYY-MM-DD) at lat/lon in tz. Weekday is the local civil weekday. */
export function sunDay(date: string, lat: number, lon: number, tz: string): SunDay {
  const obs = new A.Observer(lat, lon, 0)
  const midnight = localToUtc(date, '00:00', tz)
  const sr = A.SearchRiseSet(A.Body.Sun, obs, +1, midnight, 1)
  const ss = A.SearchRiseSet(A.Body.Sun, obs, -1, midnight, 1)
  if (!sr || !ss) throw new Error('no sunrise (polar)')
  const nsr = A.SearchRiseSet(A.Body.Sun, obs, +1, new Date(sr.date.getTime() + 60e3), 2)!
  const [y, m, d] = date.split('-').map(Number)
  return { sunrise: sr.date, sunset: ss.date, nextSunrise: nsr.date, weekday: new Date(Date.UTC(y, m - 1, d)).getUTCDay() }
}
/** 1-based eighth-of-daylight segments, Sun..Sat. */
export const RAHU_SEG = [8, 2, 7, 5, 6, 4, 3]
export const YAMAGANDA_SEG = [5, 4, 3, 2, 1, 7, 6]
export const GULIKA_SEG = [7, 6, 5, 4, 3, 2, 1]
export function daySegment(day: SunDay, seg: number) {
  const L = (day.sunset.getTime() - day.sunrise.getTime()) / 8
  const start = new Date(day.sunrise.getTime() + (seg - 1) * L)
  return { start, end: new Date(start.getTime() + L) }
}
/** Abhijit muhurat: 8th of 15 daytime muhurtas (local noon +/- 1/30 of daylight). */
export function abhijit(day: SunDay) {
  const L = (day.sunset.getTime() - day.sunrise.getTime()) / 15
  const start = new Date(day.sunrise.getTime() + 7 * L)
  return { start, end: new Date(start.getTime() + L) }
}
/** Amanta lunar month for instant t: from the Sun's sidereal sign at the preceding new moon; adhik if next new moon has Sun in the same sign. */
export function lunarMonth(t: Date) {
  const prevNm = A.SearchMoonPhase(0, new Date(t.getTime() - 31 * 86400e3), 31)
  let nm = prevNm!.date
  // walk forward to the last new moon <= t
  for (;;) { const n = A.SearchMoonPhase(0, new Date(nm.getTime() + 86400e3), 31)!; if (n.date.getTime() > t.getTime()) break; nm = n.date }
  const nextNm = A.SearchMoonPhase(0, new Date(nm.getTime() + 86400e3), 31)!.date
  const s0 = Math.floor(siderealLon('Sun', nm) / 30), s1 = Math.floor(siderealLon('Sun', nextNm) / 30)
  const amanta = MONTH_BY_SUN_SIGN[s0]
  const adhik = s0 === s1
  const krishna = tithiIndex(t) >= 15
  const purnimanta = krishna && !adhik ? MONTHS[(MONTHS.indexOf(amanta) + 1) % 12] : amanta
  return { amanta, purnimanta, adhik, newMoon: nm, nextNewMoon: nextNm }
}
/** Vikram Samvat / Shaka for instant t (year turns at Chaitra Shukla Pratipada, amanta). */
export function samvat(t: Date) {
  const lm = lunarMonth(t)
  const y = t.getUTCFullYear()
  const mi = MONTHS.indexOf(lm.amanta)
  // Jan-Apr dates still in Pausha/Magha/Phalguna (amanta) belong to the previous samvat year.
  const newYearStarted = !(t.getUTCMonth() <= 3 && mi >= 9)
  return { vikram: (newYearStarted ? y + 57 : y + 56), shaka: (newYearStarted ? y - 78 : y - 79) }
}
export const fmtDeg = (x: number) => `${Math.floor(x)}°${String(Math.floor((x % 1) * 60)).padStart(2, '0')}'`
