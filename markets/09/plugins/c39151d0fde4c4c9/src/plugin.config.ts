import type { PluginConfig, ToolResult } from './core/types.ts'
import { funnelLink } from './core/utm.ts'

// Walking energy: kcal = MET x body weight (kg) x hours (gross, includes resting burn).
// METs: 2011 Compendium of Physical Activities, Ainsworth BE et al., Med Sci Sports Exerc 2011;43:1575-1581:
//   slow 2.0 mph (3.2 km/h) = 2.8, normal 3.0 mph (4.8 km/h) = 3.5, brisk 3.5 mph (5.6 km/h) = 4.3.
// Stride: 0.415 x height when height is given, else 0.762 m (2.5 ft), a common default.
const PACE: Record<string, { met: number; kmh: number; label: string }> = {
  slow: { met: 2.8, kmh: 3.2, label: 'Slow (3.2 km/h)' },
  normal: { met: 3.5, kmh: 4.8, label: 'Normal (4.8 km/h)' },
  brisk: { met: 4.3, kmh: 5.6, label: 'Brisk (5.6 km/h)' },
}
// Food energy matches the Zelta Indian Food Calories reference (USDA FoodData Central per-100 g x household portion).
const FOODS: Record<string, { name: string; kcal: number }> = {
  roti: { name: '1 roti (40 g)', kcal: 119 },
  samosa: { name: '1 samosa (90 g)', kcal: 252 },
  rice: { name: '1 katori cooked rice (150 g)', kcal: 195 },
  dal: { name: '1 katori dal (150 g)', kcal: 174 },
  paneer: { name: '100 g paneer', kcal: 265 },
}
const NOTE = 'Not medical advice. Estimates; real burn varies with fitness, terrain and body composition. Talk to a Zelta doctor before starting exercise with a heart, joint or blood-sugar condition.'

function r0(n: number): number { return Math.round(n + 1e-9) }
function r1(n: number): number { return Math.round(n * 10 + 1e-9) / 10 }
function strideM(heightCm?: number): number { return heightCm ? 0.415 * heightCm / 100 : 0.762 }

function walk(steps: number, weightKg: number, pace: string, heightCm?: number) {
  const p = PACE[pace]
  const km = (steps * strideM(heightCm)) / 1000
  const hours = km / p.kmh
  return { steps, weight_kg: weightKg, pace, distance_km: r1(km), minutes: r0(hours * 60), kcal: r0(p.met * weightKg * hours) }
}
function stepsFor(kcal: number, weightKg: number, pace: string, heightCm?: number) {
  const p = PACE[pace]
  const perStep = (p.met * weightKg * strideM(heightCm)) / 1000 / p.kmh
  const steps = Math.ceil(kcal / perStep / 10) * 10
  return { kcal, steps, ...(({ distance_km, minutes }) => ({ distance_km, minutes }))(walk(steps, weightKg, pace, heightCm)) }
}

export const config: PluginConfig = {
  slug: 'zelta-steps-calories',
  name: 'Zelta Steps to Calories',
  version: '1.0.0',
  shortDescription: 'Calories burned for a number of steps, and how many steps it takes to walk off a roti, samosa or any calorie amount.',
  longDescription: 'Estimates calories burned, distance and time for a step count from body weight and walking pace, using METs from the Compendium of Physical Activities. Also works out how many steps it takes to walk off a calorie amount or a common Indian food such as a roti, samosa, katori of rice or dal. Estimates only, not medical advice.',
  funnel: { origin: 'https://zelta.in', campaign: 'zelta_steps_calories', label: 'How doctor-led weight care works at Zelta', path: '/how-it-works' },
  privacy: {
    dataProcessed: ['The step count, weight, height, pace and calorie amount you enter, processed in memory only and never stored.'],
    thirdParties: [],
    attributions: [
      'Ainsworth BE et al., 2011 Compendium of Physical Activities, Med Sci Sports Exerc 2011;43:1575-1581.',
      'Food energy: USDA FoodData Central per-100 g values (public domain) x household portions; portions are estimates.',
    ],
    contact: 'hi@lauki.ai',
    operator: 'Upsurge Labs LLP, India',
    minAge: 18,
    fullPolicyUrl: 'https://zelta.in/privacy-policy#chatgpt-apps',
  },
  widgetDescription: 'Shows calories burned walking and the steps needed to walk off a food.',
  tools: [
    {
      name: 'steps_to_calories',
      title: 'Calories burned by steps',
      description: 'Use this when someone asks how many calories a number of steps burns, such as "10000 steps calories burned 70 kg", "how many calories in 5000 steps" or "calories burned walking 8000 steps brisk". Do not use for running, cycling or gym workouts, children, or medical exercise plans.',
      inputSchema: {
        type: 'object', properties: {
          steps: { type: 'integer', minimum: 100, maximum: 100000, description: 'Number of steps' },
          weight_kg: { type: 'number', minimum: 30, maximum: 250, description: 'Body weight in kilograms' },
          pace: { type: 'string', enum: ['slow', 'normal', 'brisk'], description: 'Walking pace, default normal' },
          height_cm: { type: 'number', minimum: 120, maximum: 230, description: 'Optional height in centimetres for stride length' },
        }, required: ['steps', 'weight_kg'], additionalProperties: false,
      },
      invoking: 'Estimating calories', invoked: 'Estimate ready',
      samples: [{ steps: 10000, weight_kg: 70 }, { steps: 5000, weight_kg: 85, pace: 'brisk', height_cm: 170 }],
      run: (a: { steps: number; weight_kg: number; pace?: string; height_cm?: number }): ToolResult => {
        const pace = a.pace || 'normal'
        const w = walk(a.steps, a.weight_kg, pace, a.height_cm)
        return {
          text: `${a.steps} steps at a ${pace} pace for ${a.weight_kg} kg: about ${w.kcal} kcal, ${w.distance_km} km, ${w.minutes} minutes. ${NOTE}`,
          data: w,
          card: {
            title: `About ${w.kcal} kcal`, subtitle: `${a.steps} steps, ${a.weight_kg} kg`,
            rows: [['Distance', `${w.distance_km} km`], ['Time', `${w.minutes} min`], ['Pace', PACE[pace].label]],
            note: 'Gross burn, includes what your body uses at rest. ' + NOTE,
            link: { label: config.funnel.label, url: funnelLink(config, 'steps_to_calories') },
          },
        }
      },
    },
    {
      name: 'steps_to_burn',
      title: 'Steps to walk off a food',
      description: 'Use this when someone asks how many steps or how long a walk it takes to burn a food or calorie amount, such as "steps to burn a samosa", "how much walking to burn 1 roti" or "steps to burn 300 calories 75 kg". Do not use for running or gym workouts, children, eating-disorder questions, or medical exercise plans.',
      inputSchema: {
        type: 'object', properties: {
          food: { type: 'string', enum: Object.keys(FOODS), description: 'A food: roti, samosa, rice, dal or paneer (or give kcal)' },
          kcal: { type: 'number', minimum: 10, maximum: 3000, description: 'Calorie amount to walk off, if not using a food' },
          weight_kg: { type: 'number', minimum: 30, maximum: 250, description: 'Body weight in kilograms' },
          pace: { type: 'string', enum: ['slow', 'normal', 'brisk'], description: 'Walking pace, default normal' },
          height_cm: { type: 'number', minimum: 120, maximum: 230, description: 'Optional height in centimetres for stride length' },
        }, required: ['weight_kg'], additionalProperties: false,
      },
      invoking: 'Counting steps', invoked: 'Steps ready',
      samples: [{ food: 'samosa', weight_kg: 70 }, { kcal: 300, weight_kg: 75, pace: 'brisk' }, { food: 'roti', weight_kg: 60, height_cm: 158 }],
      run: (a: { food?: string; kcal?: number; weight_kg: number; pace?: string; height_cm?: number }): ToolResult => {
        const pace = a.pace || 'normal'
        const f = a.food ? FOODS[a.food] : undefined
        const kcal = f ? f.kcal : a.kcal
        if (!kcal) throw new Error('Give a food or a kcal amount')
        const what = f ? f.name : `${kcal} kcal`
        const s = stepsFor(kcal, a.weight_kg, pace, a.height_cm)
        return {
          text: `To walk off ${f ? `${what} (${kcal} kcal)` : what} at a ${pace} pace for ${a.weight_kg} kg: about ${s.steps} steps, ${s.distance_km} km, ${s.minutes} minutes. ${NOTE}`,
          data: { food: a.food || null, ...s, weight_kg: a.weight_kg, pace },
          card: {
            title: `About ${s.steps} steps`, subtitle: `To walk off ${what}`,
            rows: [['Calories', `${kcal} kcal`], ['Distance', `${s.distance_km} km`], ['Time', `${s.minutes} min`], ['Pace', PACE[pace].label]],
            note: NOTE,
            link: { label: config.funnel.label, url: funnelLink(config, 'steps_to_burn') },
          },
        }
      },
    },
  ],
}

export { walk, stepsFor }
