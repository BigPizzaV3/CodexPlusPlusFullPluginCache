import type { PluginConfig, ToolResult } from './core/types.ts'
import { funnelLink } from './core/utm.ts'

// Protein per kg body weight per day:
//  maintain     0.83 g/kg - ICMR-NIN Nutrient Requirements for Indians 2020 (safe intake for adults).
//  weight_loss  1.2-1.6 g/kg - range used in energy-deficit studies to protect lean mass (e.g. Leidy HJ et al., Am J Clin Nutr 2015;101:1320S).
//  muscle_gain  1.6-2.2 g/kg - ISSN position stand, Jager R et al., J Int Soc Sports Nutr 2017;14:20.
// When height is given and BMI is above 25, grams are computed on the weight at BMI 25 (reference weight), a common
// practice so targets for heavier people do not overshoot.
const RANGES: Record<string, [number, number]> = { maintain: [0.83, 0.83], weight_loss: [1.2, 1.6], muscle_gain: [1.6, 2.2] }
const GOAL_LABEL: Record<string, string> = { maintain: 'Maintain', weight_loss: 'Weight loss', muscle_gain: 'Muscle gain' }

// Protein per household serving, from USDA FoodData Central per-100 g reference values (public domain) x the serving weight.
type Food = { name: string; serving: string; protein: number; diet: 'veg' | 'egg' | 'non_veg' }
const FOODS: Food[] = [
  { name: 'Dal (cooked lentils)', serving: '1 katori, 150 g', protein: 13.5, diet: 'veg' },
  { name: 'Chana / chole (cooked chickpeas)', serving: '1 katori, 150 g', protein: 13.3, diet: 'veg' },
  { name: 'Rajma (cooked kidney beans)', serving: '1 katori, 150 g', protein: 13.0, diet: 'veg' },
  { name: 'Paneer', serving: '100 g', protein: 18.3, diet: 'veg' },
  { name: 'Soya chunks (dry weight)', serving: '30 g', protein: 15.6, diet: 'veg' },
  { name: 'Curd', serving: '1 katori, 150 g', protein: 5.2, diet: 'veg' },
  { name: 'Milk', serving: '1 glass, 250 ml', protein: 8.3, diet: 'veg' },
  { name: 'Peanuts', serving: '30 g handful', protein: 7.7, diet: 'veg' },
  { name: 'Egg', serving: '1 large', protein: 6.3, diet: 'egg' },
  { name: 'Chicken breast (cooked)', serving: '100 g', protein: 31.0, diet: 'non_veg' },
  { name: 'Fish (cooked)', serving: '100 g', protein: 22.0, diet: 'non_veg' },
]
const DIETS: Record<string, string[]> = { veg: ['veg'], eggetarian: ['veg', 'egg'], non_veg: ['veg', 'egg', 'non_veg'] }
// Sample-day fill order and per-day caps (servings), so the plan stays a normal Indian day.
const PLAN_ORDER: [string, number][] = [
  ['Chicken breast (cooked)', 1], ['Fish (cooked)', 1], ['Egg', 2], ['Dal (cooked lentils)', 2], ['Paneer', 1], ['Curd', 2],
  ['Milk', 1], ['Soya chunks (dry weight)', 1], ['Chana / chole (cooked chickpeas)', 1], ['Peanuts', 1],
]
const NOTE = 'Not medical advice. People with kidney disease or on a medical diet need a doctor\'s target, not a formula. Talk to a Zelta doctor before changing your diet.'

function r0(n: number): number { return Math.round(n + 1e-9) }
function r1(n: number): number { return Math.round(n * 10 + 1e-9) / 10 }

function proteinTarget(weightKg: number, goal: string, heightCm?: number) {
  let refKg = weightKg, adjusted = false
  if (heightCm) {
    const atBmi25 = 25 * (heightCm / 100) ** 2
    if (weightKg > atBmi25) { refKg = atBmi25; adjusted = true }
  }
  const [lo, hi] = RANGES[goal]
  return { goal, weight_kg: weightKg, reference_kg: r1(refKg), adjusted, g_per_kg: [lo, hi] as [number, number], grams_low: r0(lo * refKg), grams_high: r0(hi * refKg) }
}

function foodPlan(grams: number, diet: string) {
  const allowed = new Set(DIETS[diet])
  const byName = new Map(FOODS.map((f) => [f.name, f]))
  const items: { food: string; serving: string; servings: number; protein: number }[] = []
  let total = 0
  for (const [name, cap] of PLAN_ORDER) {
    const f = byName.get(name)!
    if (!allowed.has(f.diet)) continue
    let n = 0
    while (n < cap && total < grams) { n++; total += f.protein }
    if (n) items.push({ food: f.name, serving: f.serving, servings: n, protein: r1(n * f.protein) })
    if (total >= grams) break
  }
  return { target_g: grams, diet, items, total_g: r1(total), reached: total >= grams }
}

export const config: PluginConfig = {
  slug: 'zelta-protein-target',
  name: 'Zelta Protein Per Day',
  version: '1.0.0',
  shortDescription: 'Daily protein target by body weight and goal, and a sample Indian veg, egg or non-veg day that reaches it.',
  longDescription: 'Works out a daily protein range in grams from body weight and goal (maintain, weight loss or muscle gain) using ICMR-NIN and published sports-nutrition ranges, and builds a sample day from common Indian foods such as dal, paneer, curd, soya, eggs and chicken to reach it. Estimates only, not medical advice.',
  funnel: { origin: 'https://zelta.in', campaign: 'zelta_protein_target', label: 'How doctor-led weight care works at Zelta', path: '/how-it-works' },
  privacy: {
    dataProcessed: ['The weight, height, goal and diet type you enter, processed in memory only and never stored.'],
    thirdParties: [],
    attributions: [
      'ICMR-NIN, Nutrient Requirements for Indians 2020 (adult safe protein intake 0.83 g/kg/day).',
      'Jager R et al., ISSN position stand: protein and exercise, J Int Soc Sports Nutr 2017;14:20.',
      'Leidy HJ et al., The role of protein in weight loss and maintenance, Am J Clin Nutr 2015;101:1320S-1329S.',
      'Protein per serving: USDA FoodData Central per-100 g values (public domain) x household serving weights; servings are estimates.',
    ],
    contact: 'hi@lauki.ai',
    operator: 'Upsurge Labs LLP, India',
    minAge: 18,
    fullPolicyUrl: 'https://zelta.in/privacy-policy#chatgpt-apps',
  },
  widgetDescription: 'Shows a daily protein range and a sample Indian day that reaches it.',
  tools: [
    {
      name: 'protein_per_day',
      title: 'Protein per day',
      description: 'Use this when an adult asks how much protein they need a day, such as "how much protein per day for 70 kg", "protein for weight loss 80 kg woman" or "protein intake to build muscle 65 kg". Do not use for children, pregnancy, kidney or liver disease, medical diets, or supplement and medication questions.',
      inputSchema: {
        type: 'object', properties: {
          weight_kg: { type: 'number', minimum: 30, maximum: 250, description: 'Body weight in kilograms' },
          goal: { type: 'string', enum: ['maintain', 'weight_loss', 'muscle_gain'], description: 'Goal: maintain, weight_loss or muscle_gain' },
          height_cm: { type: 'number', minimum: 120, maximum: 230, description: 'Optional height in centimetres; above BMI 25 the target uses the weight at BMI 25' },
        }, required: ['weight_kg', 'goal'], additionalProperties: false,
      },
      invoking: 'Working out protein', invoked: 'Protein target ready',
      samples: [{ weight_kg: 70, goal: 'maintain' }, { weight_kg: 85, goal: 'weight_loss', height_cm: 165 }, { weight_kg: 65, goal: 'muscle_gain' }],
      run: (a: { weight_kg: number; goal: string; height_cm?: number }): ToolResult => {
        const t = proteinTarget(a.weight_kg, a.goal, a.height_cm)
        const range = t.grams_low === t.grams_high ? `${t.grams_low} g` : `${t.grams_low}-${t.grams_high} g`
        const perKg = t.g_per_kg[0] === t.g_per_kg[1] ? `${t.g_per_kg[0]} g/kg` : `${t.g_per_kg[0]}-${t.g_per_kg[1]} g/kg`
        return {
          text: `About ${range} of protein a day ${a.goal === 'maintain' ? 'to maintain' : 'for ' + GOAL_LABEL[a.goal].toLowerCase()} (${perKg} on ${t.reference_kg} kg${t.adjusted ? ', the weight at BMI 25 for your height' : ''}). ${NOTE}`,
          data: t,
          card: {
            title: `${range} protein a day`, subtitle: `${GOAL_LABEL[a.goal]}, ${a.weight_kg} kg`,
            rows: [['Per kg', perKg], ['Calculated on', `${t.reference_kg} kg${t.adjusted ? ' (weight at BMI 25)' : ''}`]],
            note: NOTE,
            link: { label: config.funnel.label, url: funnelLink(config, 'protein_per_day') },
          },
        }
      },
    },
    {
      name: 'protein_food_plan',
      title: 'Sample Indian protein day',
      description: 'Use this when someone asks how to get a protein amount from Indian food, such as "how to get 80 g protein a day vegetarian", "high protein Indian veg foods for 100 g" or "eggetarian 90 g protein sample day". Builds a sample day from dal, paneer, curd, soya, milk, eggs, chicken and fish. Do not use for medical diets, kidney disease, allergies, or supplement questions.',
      inputSchema: {
        type: 'object', properties: {
          grams: { type: 'number', minimum: 20, maximum: 250, description: 'Daily protein target in grams' },
          diet: { type: 'string', enum: ['veg', 'eggetarian', 'non_veg'], description: 'Diet type: veg, eggetarian or non_veg' },
        }, required: ['grams', 'diet'], additionalProperties: false,
      },
      invoking: 'Building a sample day', invoked: 'Sample day ready',
      samples: [{ grams: 80, diet: 'veg' }, { grams: 100, diet: 'non_veg' }, { grams: 90, diet: 'eggetarian' }],
      run: (a: { grams: number; diet: string }): ToolResult => {
        const p = foodPlan(a.grams, a.diet)
        const lines = p.items.map((i) => `${i.servings} x ${i.food} (${i.serving}) = ${i.protein} g`)
        return {
          text: `Sample ${a.diet.replace('_', '-')} day for ${a.grams} g protein: ${lines.join('; ')}. Total about ${p.total_g} g${p.reached ? '' : ', short of the target with everyday portions; a dietitian or doctor can help close the gap'}. ${NOTE}`,
          data: p,
          card: {
            title: `${p.total_g} g protein`, subtitle: `Sample ${a.diet.replace('_', '-')} day for a ${a.grams} g target`,
            table: { columns: ['Food', 'Serving', 'Servings', 'Protein'], rows: p.items.map((i) => [i.food, i.serving, `${i.servings}`, `${i.protein} g`]) },
            note: 'Protein per serving is an estimate; brands and recipes vary. ' + NOTE,
            link: { label: config.funnel.label, url: funnelLink(config, 'protein_food_plan') },
          },
        }
      },
    },
  ],
}

export { proteinTarget, foodPlan, FOODS }
