// Shared types for every plugin built from this template.
export type Json = null | boolean | number | string | Json[] | { [k: string]: Json }
export type JsonObject = { [k: string]: Json }

/** JSON Schema subset the runtime validates: type, enum, required, properties,
 * additionalProperties:false, minimum/maximum, minLength/maxLength, pattern, items, minItems/maxItems. */
export type Schema = {
  type?: 'object' | 'string' | 'number' | 'integer' | 'boolean' | 'array'
  description?: string
  enum?: (string | number)[]
  properties?: Record<string, Schema>
  required?: string[]
  additionalProperties?: boolean
  minimum?: number
  maximum?: number
  minLength?: number
  maxLength?: number
  pattern?: string
  format?: string
  items?: Schema
  minItems?: number
  maxItems?: number
  default?: Json
}

/** The generic card every widget renders. Tools return { card, ...data } as structuredContent. */
export type Card = {
  title: string
  subtitle?: string
  highlight?: { label: string; value: string }
  rows?: [string, string][]
  sections?: { heading: string; rows: [string, string][] }[]
  chips?: string[]
  table?: { columns: string[]; rows: string[][] }
  note?: string
  link?: { label: string; url: string }
}

export type ToolResult = { text: string; card?: Card; data?: JsonObject }

export type ToolDef = {
  name: string
  title: string
  /** Must start "Use this when..." and contain "Do not use for..." (enforced by tests). */
  description: string
  inputSchema: Schema
  /** Read-only lookups/calculators: readOnlyHint true, destructiveHint false, openWorldHint false. */
  annotations?: { readOnlyHint?: boolean; destructiveHint?: boolean; openWorldHint?: boolean; idempotentHint?: boolean }
  invoking?: string
  invoked?: string
  /** Render the shared card widget for this tool (default true). */
  widget?: boolean
  /** Sample arguments used by scripts/smoke.mjs and tests. At least one per tool. */
  samples: JsonObject[]
  /** env = the Worker bindings (KV/R2/vars from wrangler.toml); undefined in unit tests. Large datasets (IFSC, PIN) live in KV, not the bundle. */
  run: (args: any, env?: Record<string, any>) => ToolResult | Promise<ToolResult>
}

export type PluginConfig = {
  slug: string // kebab-case, also the worker name stem and repo name
  name: string // display name in the directory, no "Plugin"/"MCP" suffix
  version: string
  shortDescription: string // <= 120 chars, plugin.json extensions.com.openai.description
  longDescription: string // plugin.json description
  funnel: {
    origin: string // e.g. https://naksha.social
    campaign: string // utm_campaign, e.g. naksha_panchang
    label: string // default CTA label in the card
    path?: string // default landing path
  }
  privacy: {
    dataProcessed: string[] // what inputs are processed (in memory)
    thirdParties: string[] // outbound network calls at runtime; [] for pure compute
    attributions: string[] // data licences, e.g. GeoNames CC BY 4.0
    contact: string
    minAge?: number // default 13; brands with an 18+ service set 18
    fullPolicyUrl?: string // brand policy section that this app page belongs to
  }
  widgetDescription: string
  tools: ToolDef[]
}
