import type { Schema } from './types'

export class InputError extends Error {}

/** Validate + coerce args against the schema subset. Applies defaults. Throws InputError with a user-safe message
 * (never echoes the raw value, so birth data etc. never lands in an error string). */
export function validate(schema: Schema, value: unknown, path = 'input'): any {
  if (value === undefined && schema.default !== undefined) value = structuredClone(schema.default)
  const t = schema.type
  if (t === 'object') {
    if (value === undefined || value === null) value = {}
    if (typeof value !== 'object' || Array.isArray(value)) throw new InputError(`${path} must be an object`)
    const obj = value as Record<string, unknown>
    const out: Record<string, unknown> = {}
    const props = schema.properties || {}
    for (const req of schema.required || []) if (obj[req] === undefined || obj[req] === null || obj[req] === '') throw new InputError(`${path}.${req} is required`)
    for (const [k, v] of Object.entries(obj)) {
      if (!(k in props)) {
        if (schema.additionalProperties === false) continue // drop unknown keys silently: clients add envelopes
        out[k] = v
        continue
      }
    }
    for (const [k, s] of Object.entries(props)) {
      const v = validate(s, obj[k], `${path}.${k}`)
      if (v !== undefined) out[k] = v
    }
    return out
  }
  if (value === undefined || value === null) return undefined
  if (t === 'string') {
    if (typeof value === 'number') value = String(value)
    if (typeof value !== 'string') throw new InputError(`${path} must be text`)
    const s = value.trim()
    if (/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/.test(s)) throw new InputError(`${path} contains control characters`)
    if (schema.minLength !== undefined && s.length < schema.minLength) throw new InputError(`${path} is too short`)
    if (s.length > (schema.maxLength ?? 200)) throw new InputError(`${path} is too long`)
    if (schema.pattern && !new RegExp(schema.pattern).test(s)) throw new InputError(`${path} has the wrong format`)
    if (schema.enum && !schema.enum.includes(s)) throw new InputError(`${path} must be one of: ${schema.enum.join(', ')}`)
    return s
  }
  if (t === 'number' || t === 'integer') {
    const n = typeof value === 'string' && value.trim() !== '' ? Number(value.replace(/,/g, '')) : value
    if (typeof n !== 'number' || !Number.isFinite(n)) throw new InputError(`${path} must be a number`)
    if (t === 'integer' && !Number.isInteger(n)) throw new InputError(`${path} must be a whole number`)
    if (schema.minimum !== undefined && n < schema.minimum) throw new InputError(`${path} must be at least ${schema.minimum}`)
    if (schema.maximum !== undefined && n > schema.maximum) throw new InputError(`${path} must be at most ${schema.maximum}`)
    if (schema.enum && !schema.enum.includes(n)) throw new InputError(`${path} must be one of: ${schema.enum.join(', ')}`)
    return n
  }
  if (t === 'boolean') {
    if (value === 'true') return true
    if (value === 'false') return false
    if (typeof value !== 'boolean') throw new InputError(`${path} must be true or false`)
    return value
  }
  if (t === 'array') {
    if (!Array.isArray(value)) throw new InputError(`${path} must be a list`)
    if (schema.minItems !== undefined && value.length < schema.minItems) throw new InputError(`${path} needs at least ${schema.minItems} items`)
    if (value.length > (schema.maxItems ?? 50)) throw new InputError(`${path} has too many items`)
    return value.map((v, i) => validate(schema.items || {}, v, `${path}[${i}]`))
  }
  return value
}

/** Clients sometimes wrap tool args ({arguments:{...}} or {params:{arguments:{...}}}). Unwrap once. */
export function unwrapArgs(args: unknown): Record<string, unknown> {
  let a: any = args && typeof args === 'object' ? args : {}
  for (let i = 0; i < 2; i++) {
    const keys = Object.keys(a)
    if (keys.length === 1 && (keys[0] === 'arguments' || keys[0] === 'params' || keys[0] === 'input') && a[keys[0]] && typeof a[keys[0]] === 'object') a = a[keys[0]]
  }
  return a
}
