import type { PluginConfig, Schema, ToolResult } from './core/types.ts'
import { funnelLink } from './core/utm.ts'

// Asian-Indian adult BMI cutoffs: Misra A et al., "Consensus statement for diagnosis of obesity, abdominal obesity and the
// metabolic syndrome for Asian Indians", JAPI 2009;57:163-170 (normal 18.0-22.9, overweight 23.0-24.9, obese >=25), in line
// with WHO Expert Consultation, Lancet 2004;363:157-163 (public-health action points 23 / 27.5 for Asians).
// International cutoffs: WHO (18.5 / 25 / 30). Cutoff values are facts, no data is bundled.
const INDIAN = [
  { max: 18, label: 'Underweight' },
  { max: 23, label: 'Normal' },
  { max: 25, label: 'Overweight' },
  { max: Infinity, label: 'Obese' },
]
const WHO = [
  { max: 18.5, label: 'Underweight' },
  { max: 25, label: 'Normal' },
  { max: 30, label: 'Overweight' },
  { max: Infinity, label: 'Obese' },
]
const NOTE = 'Not medical advice. BMI is a screening number for adults 18+, not a diagnosis; it does not see muscle, age or ethnicity in full. Talk to a Zelta doctor to review it with your history.'

function r1(n: number): number { return Math.round(n * 10 + 1e-9) / 10 }
function heightCm(a: { height_cm?: number; height_ft?: number; height_in?: number }): number {
  if (a.height_cm) return a.height_cm
  if (a.height_ft) return (a.height_ft * 12 + (a.height_in || 0)) * 2.54
  throw new Error('Give height_cm, or height_ft (and optional height_in)')
}
function band(bmi: number, table: { max: number; label: string }[]): string {
  return table.find((b) => bmi < b.max)!.label
}
function bmiOf(weightKg: number, cm: number) {
  const m = cm / 100
  const bmi = r1(weightKg / (m * m))
  return {
    bmi, height_cm: r1(cm), weight_kg: r1(weightKg),
    indian_category: band(bmi, INDIAN), who_category: band(bmi, WHO),
    indian_normal_range_kg: [r1(18 * m * m), r1(22.9 * m * m)] as [number, number],
    who_normal_range_kg: [r1(18.5 * m * m), r1(24.9 * m * m)] as [number, number],
  }
}

const HEIGHT_PROPS: Record<string, Schema> = {
  height_cm: { type: 'number', minimum: 100, maximum: 250, description: 'Height in centimetres' },
  height_ft: { type: 'number', minimum: 3, maximum: 8, description: 'Height feet part, if not using centimetres' },
  height_in: { type: 'number', minimum: 0, maximum: 11.9, description: 'Height inches part, used with height_ft' },
}

export const config: PluginConfig = {
  slug: 'zelta-bmi-india',
  name: 'Zelta BMI for Indians',
  version: '1.0.0',
  shortDescription: 'Adult BMI with the Asian-Indian cutoffs (23 and 25) next to the WHO ones, plus a healthy weight range.',
  longDescription: 'Calculates adult BMI from height and weight and shows the category under the Asian-Indian consensus cutoffs, where overweight starts at 23 and obesity at 25, next to the international WHO categories. Also gives the weight range that sits in the normal band for a given height. Screening numbers only, not a diagnosis.',
  funnel: { origin: 'https://zelta.in', campaign: 'zelta_bmi_india', label: 'How doctor-led weight care works at Zelta', path: '/how-it-works' },
  privacy: {
    dataProcessed: ['The height and weight you enter, processed in memory only and never stored.'],
    thirdParties: [],
    attributions: [
      'Asian-Indian cutoffs: Misra A et al., Consensus statement for Asian Indians, JAPI 2009;57:163-170.',
      'WHO Expert Consultation, Appropriate body-mass index for Asian populations, Lancet 2004;363:157-163.',
      'International categories: WHO BMI classification.',
    ],
    contact: 'hi@lauki.ai',
    operator: 'Upsurge Labs LLP, India',
    minAge: 18,
    fullPolicyUrl: 'https://zelta.in/privacy-policy#chatgpt-apps',
  },
  widgetDescription: 'Shows adult BMI with Asian-Indian and WHO categories and a healthy weight range.',
  tools: [
    {
      name: 'bmi_check',
      title: 'BMI check (Indian cutoffs)',
      description: 'Use this when an adult asks for their BMI or whether their weight is normal, overweight or obese, such as "BMI for 72 kg 165 cm", "am I overweight at 5 ft 6 and 70 kg", or "BMI Asian cutoff". Shows the Asian-Indian category next to the WHO one. Do not use for children or teens under 18, pregnancy, diagnosis, or treatment and medication questions.',
      inputSchema: {
        type: 'object', properties: {
          weight_kg: { type: 'number', minimum: 25, maximum: 350, description: 'Body weight in kilograms' },
          ...HEIGHT_PROPS,
        }, required: ['weight_kg'], additionalProperties: false,
      },
      invoking: 'Calculating BMI', invoked: 'BMI ready',
      samples: [{ weight_kg: 72, height_cm: 165 }, { weight_kg: 70, height_ft: 5, height_in: 6 }, { weight_kg: 55, height_cm: 160 }],
      run: (a: { weight_kg: number; height_cm?: number; height_ft?: number; height_in?: number }): ToolResult => {
        const b = bmiOf(a.weight_kg, heightCm(a))
        const differs = b.indian_category !== b.who_category
        return {
          text: `BMI ${b.bmi}: ${b.indian_category} by Asian-Indian cutoffs, ${b.who_category} by WHO cutoffs. Normal-band weight at ${b.height_cm} cm: ${b.indian_normal_range_kg[0]}-${b.indian_normal_range_kg[1]} kg (Indian), ${b.who_normal_range_kg[0]}-${b.who_normal_range_kg[1]} kg (WHO). ${NOTE}`,
          data: b,
          card: {
            title: `BMI ${b.bmi}`, subtitle: `${b.weight_kg} kg at ${b.height_cm} cm`,
            highlight: { label: 'Asian-Indian category', value: b.indian_category },
            rows: [
              ['WHO category', b.who_category],
              ['Normal range, Indian cutoffs', `${b.indian_normal_range_kg[0]}-${b.indian_normal_range_kg[1]} kg`],
              ['Normal range, WHO cutoffs', `${b.who_normal_range_kg[0]}-${b.who_normal_range_kg[1]} kg`],
            ],
            chips: differs ? ['Indian and WHO categories differ at this BMI'] : undefined,
            note: NOTE,
            link: { label: config.funnel.label, url: funnelLink(config, 'bmi_check') },
          },
        }
      },
    },
    {
      name: 'healthy_weight_range',
      title: 'Healthy weight range for a height',
      description: 'Use this when an adult asks what weight is normal or ideal for a height, such as "ideal weight for 5 ft 4", "normal weight for 170 cm Indian male", or "how much should I weigh at 158 cm". Gives the BMI-based range under Asian-Indian and WHO cutoffs. Do not use for children, pregnancy, athletes judged on muscle, or diagnosis.',
      inputSchema: { type: 'object', properties: { ...HEIGHT_PROPS }, required: [], additionalProperties: false },
      invoking: 'Working out the range', invoked: 'Weight range ready',
      samples: [{ height_cm: 170 }, { height_ft: 5, height_in: 4 }],
      run: (a: { height_cm?: number; height_ft?: number; height_in?: number }): ToolResult => {
        const cm = heightCm(a)
        const b = bmiOf(60, cm)
        const m2 = (cm / 100) ** 2
        const overweightFrom = r1(23 * m2), obeseFrom = r1(25 * m2)
        return {
          text: `At ${b.height_cm} cm, the normal BMI band is ${b.indian_normal_range_kg[0]}-${b.indian_normal_range_kg[1]} kg by Asian-Indian cutoffs (overweight from ${overweightFrom} kg, obese from ${obeseFrom} kg) and ${b.who_normal_range_kg[0]}-${b.who_normal_range_kg[1]} kg by WHO cutoffs. ${NOTE}`,
          data: { height_cm: b.height_cm, indian_normal_range_kg: b.indian_normal_range_kg, who_normal_range_kg: b.who_normal_range_kg, indian_overweight_from_kg: overweightFrom, indian_obese_from_kg: obeseFrom },
          card: {
            title: `${b.indian_normal_range_kg[0]}-${b.indian_normal_range_kg[1]} kg`, subtitle: `Normal band at ${b.height_cm} cm, Asian-Indian cutoffs`,
            rows: [
              ['WHO normal band', `${b.who_normal_range_kg[0]}-${b.who_normal_range_kg[1]} kg`],
              ['Overweight from (Indian)', `${overweightFrom} kg`],
              ['Obese from (Indian)', `${obeseFrom} kg`],
            ],
            note: NOTE,
            link: { label: config.funnel.label, url: funnelLink(config, 'healthy_weight_range') },
          },
        }
      },
    },
  ],
}

export { bmiOf, heightCm }
