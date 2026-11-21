import type { PluginConfig, Schema, ToolResult } from './core/types.ts'
import { funnelLink } from './core/utm.ts'

// BMR: Mifflin MD, St Jeor ST et al., Am J Clin Nutr 1990;51:241-247 (men 10W + 6.25H - 5A + 5, women ... - 161).
// Activity multipliers: standard 1.2 / 1.375 / 1.55 / 1.725 / 1.9.
// 7,700 kcal per kg of body-weight change is the common rule of thumb (Wishnofsky 1958); real loss slows over time.
// Safety rails: never below 1,200 kcal (women) / 1,500 kcal (men), loss rate capped at 1% body weight and 1 kg per week.
const ACTIVITY: Record<string, number> = { sedentary: 1.2, light: 1.375, moderate: 1.55, active: 1.725, very_active: 1.9 }
const ACTIVITY_LABEL: Record<string, string> = {
  sedentary: 'Sedentary (desk job, little exercise)', light: 'Light (exercise 1-3 days a week)',
  moderate: 'Moderate (exercise 3-5 days a week)', active: 'Active (hard exercise 6-7 days)', very_active: 'Very active (physical job or twice-a-day training)',
}
const KCAL_PER_KG = 7700
const NOTE = 'Not medical advice. Estimates from a standard formula; your real needs can differ by 10% or more. Talk to a Zelta doctor before a big change, especially with diabetes, thyroid, PCOS or blood-pressure medication.'

function round(n: number): number { return Math.round(n + 1e-9) }
function r1(n: number): number { return Math.round(n * 10 + 1e-9) / 10 }
function heightCm(a: { height_cm?: number; height_ft?: number; height_in?: number }): number {
  if (a.height_cm) return a.height_cm
  if (a.height_ft) return (a.height_ft * 12 + (a.height_in || 0)) * 2.54
  throw new Error('Give height_cm, or height_ft (and optional height_in)')
}

type TargetIn = { sex: 'male' | 'female'; age: number; weight_kg: number; height_cm?: number; height_ft?: number; height_in?: number; activity: string; loss_kg_per_week?: number }
function target(a: TargetIn) {
  const h = heightCm(a)
  const bmr = 10 * a.weight_kg + 6.25 * h - 5 * a.age + (a.sex === 'male' ? 5 : -161)
  const tdee = bmr * ACTIVITY[a.activity]
  const asked = a.loss_kg_per_week ?? 0.5
  const cap = Math.min(1, 0.01 * a.weight_kg)
  const rate = Math.min(asked, cap)
  const floor = a.sex === 'male' ? 1500 : 1200
  let goal = tdee - (rate * KCAL_PER_KG) / 7
  const floored = goal < floor
  if (floored) goal = Math.min(floor, tdee)
  const actualRate = Math.round((((tdee - goal) * 7) / KCAL_PER_KG) * 100 + 1e-9) / 100
  return {
    bmr: round(bmr), maintenance_kcal: round(tdee), target_kcal: round(goal), daily_deficit_kcal: round(tdee - goal),
    loss_kg_per_week: Math.round(actualRate * 100) / 100, asked_kg_per_week: asked, rate_capped: rate < asked, floored, floor_kcal: floor,
    height_cm: r1(h),
  }
}

function timeline(current: number, goalKg: number, deficit: number) {
  if (goalKg >= current) throw new Error('target_kg must be below current_kg')
  const kg = current - goalKg
  const days = (kg * KCAL_PER_KG) / deficit
  const weeks = Math.ceil(days / 7)
  return { kg_to_lose: r1(kg), daily_deficit_kcal: deficit, weeks, months: r1(days / 30.44), kg_per_week: Math.round(((deficit * 7) / KCAL_PER_KG) * 100 + 1e-9) / 100 }
}

const HEIGHT_PROPS: Record<string, Schema> = {
  height_cm: { type: 'number', minimum: 120, maximum: 230, description: 'Height in centimetres' },
  height_ft: { type: 'number', minimum: 4, maximum: 7, description: 'Height feet part, if not using centimetres' },
  height_in: { type: 'number', minimum: 0, maximum: 11.9, description: 'Height inches part, used with height_ft' },
}

export const config: PluginConfig = {
  slug: 'zelta-calorie-target',
  name: 'Zelta Daily Calorie Target',
  version: '1.0.0',
  shortDescription: 'Maintenance calories and a safe daily calorie target for weight loss, plus how long a goal takes.',
  longDescription: 'Estimates maintenance calories with the Mifflin-St Jeor formula and an activity level, then a daily calorie target for a chosen weekly weight-loss pace with safety rails: never below 1,200 kcal for women or 1,500 kcal for men, and no faster than 1% of body weight a week. Also estimates how many weeks a weight goal takes at a daily calorie deficit. Estimates only, not medical advice.',
  funnel: { origin: 'https://zelta.in', campaign: 'zelta_calorie_target', label: 'How doctor-led weight care works at Zelta', path: '/how-it-works' },
  privacy: {
    dataProcessed: ['The sex, age, height, weight, activity level and goals you enter, processed in memory only and never stored.'],
    thirdParties: [],
    attributions: [
      'Mifflin MD, St Jeor ST et al., A new predictive equation for resting energy expenditure, Am J Clin Nutr 1990;51:241-247.',
      '7,700 kcal per kg rule of thumb (Wishnofsky 1958); real-world loss slows as weight drops.',
    ],
    contact: 'hi@lauki.ai',
    operator: 'Upsurge Labs LLP, India',
    minAge: 18,
    fullPolicyUrl: 'https://zelta.in/privacy-policy#chatgpt-apps',
  },
  widgetDescription: 'Shows maintenance calories, a daily calorie target and a weight-goal timeline.',
  tools: [
    {
      name: 'daily_calorie_target',
      title: 'Daily calorie target',
      description: 'Use this when an adult asks how many calories to eat a day to lose weight or maintain, such as "how many calories should I eat to lose weight, 30 year old woman 70 kg 160 cm", "maintenance calories", "TDEE calculator" or "calorie deficit for 0.5 kg a week". Do not use for children, pregnancy or breastfeeding, eating disorders, medical diets, or medication questions.',
      inputSchema: {
        type: 'object', properties: {
          sex: { type: 'string', enum: ['male', 'female'], description: 'Sex used by the formula' },
          age: { type: 'integer', minimum: 18, maximum: 80, description: 'Age in years' },
          weight_kg: { type: 'number', minimum: 35, maximum: 250, description: 'Current weight in kilograms' },
          ...HEIGHT_PROPS,
          activity: { type: 'string', enum: Object.keys(ACTIVITY), description: 'Activity level: sedentary, light, moderate, active or very_active' },
          loss_kg_per_week: { type: 'number', minimum: 0, maximum: 1, description: 'Weekly loss pace in kg, default 0.5; 0 = maintenance' },
        }, required: ['sex', 'age', 'weight_kg', 'activity'], additionalProperties: false,
      },
      invoking: 'Estimating calories', invoked: 'Calorie target ready',
      samples: [
        { sex: 'male', age: 30, weight_kg: 80, height_cm: 175, activity: 'moderate' },
        { sex: 'female', age: 35, weight_kg: 65, height_cm: 160, activity: 'light', loss_kg_per_week: 0.5 },
        { sex: 'female', age: 28, weight_kg: 72, height_ft: 5, height_in: 3, activity: 'sedentary' },
      ],
      run: (a: TargetIn): ToolResult => {
        const t = target(a)
        const caveats: string[] = []
        if (t.rate_capped) caveats.push(`Pace capped at ${t.loss_kg_per_week} kg a week (1% of body weight, max 1 kg)`)
        if (t.floored) caveats.push(`Held at the ${t.floor_kcal} kcal floor, so loss is slower (${t.loss_kg_per_week} kg a week)`)
        return {
          text: `Maintenance about ${t.maintenance_kcal} kcal a day (BMR ${t.bmr}). Target ${t.target_kcal} kcal a day for about ${t.loss_kg_per_week} kg a week (deficit ${t.daily_deficit_kcal} kcal).${caveats.length ? ' ' + caveats.join('. ') + '.' : ''} ${NOTE}`,
          data: t,
          card: {
            title: `${t.target_kcal} kcal a day`, subtitle: `For about ${t.loss_kg_per_week} kg a week`,
            rows: [['Maintenance', `${t.maintenance_kcal} kcal`], ['Resting (BMR)', `${t.bmr} kcal`], ['Daily deficit', `${t.daily_deficit_kcal} kcal`], ['Activity', ACTIVITY_LABEL[a.activity]]],
            chips: caveats.length ? caveats : undefined,
            note: NOTE,
            link: { label: config.funnel.label, url: funnelLink(config, 'daily_calorie_target') },
          },
        }
      },
    },
    {
      name: 'weight_loss_timeline',
      title: 'Weight goal timeline',
      description: 'Use this when someone asks how long it takes to lose a set amount of weight, such as "how long to lose 10 kg", "85 to 75 kg how many weeks" or "how fast can I lose 5 kg with a 500 calorie deficit". Do not use for medical weight-loss plans, crash diets, children, pregnancy, or medication questions.',
      inputSchema: {
        type: 'object', properties: {
          current_kg: { type: 'number', minimum: 35, maximum: 250, description: 'Current weight in kilograms' },
          target_kg: { type: 'number', minimum: 35, maximum: 250, description: 'Goal weight in kilograms, below current' },
          daily_deficit_kcal: { type: 'number', minimum: 100, maximum: 1000, description: 'Daily calorie deficit, default 500 (max 1,000)' },
        }, required: ['current_kg', 'target_kg'], additionalProperties: false,
      },
      invoking: 'Working out the timeline', invoked: 'Timeline ready',
      samples: [{ current_kg: 85, target_kg: 75 }, { current_kg: 68, target_kg: 63, daily_deficit_kcal: 400 }],
      run: (a: { current_kg: number; target_kg: number; daily_deficit_kcal?: number }): ToolResult => {
        const t = timeline(a.current_kg, a.target_kg, a.daily_deficit_kcal ?? 500)
        return {
          text: `Losing ${t.kg_to_lose} kg at a ${t.daily_deficit_kcal} kcal daily deficit takes about ${t.weeks} weeks (${t.months} months), about ${t.kg_per_week} kg a week. Real loss usually slows as weight drops, so treat this as the fastest steady case. ${NOTE}`,
          data: t,
          card: {
            title: `About ${t.weeks} weeks`, subtitle: `${a.current_kg} kg to ${a.target_kg} kg`,
            rows: [['To lose', `${t.kg_to_lose} kg`], ['Daily deficit', `${t.daily_deficit_kcal} kcal`], ['Pace', `${t.kg_per_week} kg a week`], ['In months', `${t.months}`]],
            note: 'Real loss usually slows as weight drops. ' + NOTE,
            link: { label: config.funnel.label, url: funnelLink(config, 'weight_loss_timeline') },
          },
        }
      },
    },
  ],
}

export { target, timeline }
