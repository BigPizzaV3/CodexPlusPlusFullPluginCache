import type { JsonObject, PluginConfig, ToolDef } from './types'
import { InputError, unwrapArgs, validate } from './schema.ts'
import { widgetHtml } from './widget.ts'
import { privacyHtml } from './privacy.ts'

const PROTOCOLS = ['2025-11-25', '2025-06-18', '2025-03-26', '2024-11-05']
const CORS = { 'access-control-allow-origin': '*', 'access-control-allow-methods': 'GET,POST,DELETE,OPTIONS', 'access-control-allow-headers': 'content-type,authorization,mcp-session-id,mcp-protocol-version', 'access-control-max-age': '86400' }

export const widgetUri = (cfg: PluginConfig) => `ui://${cfg.slug}/card-v${cfg.version.split('.')[0]}.html`

function toolMeta(cfg: PluginConfig, t: ToolDef) {
  const meta: JsonObject = { 'openai/toolInvocation/invoking': t.invoking || 'Working...', 'openai/toolInvocation/invoked': t.invoked || 'Done' }
  if (t.widget !== false) meta['openai/outputTemplate'] = widgetUri(cfg)
  return meta
}

export function listTools(cfg: PluginConfig) {
  return cfg.tools.map((t) => ({
    name: t.name,
    title: t.title,
    description: t.description,
    inputSchema: t.inputSchema,
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true, ...(t.annotations || {}) },
    _meta: toolMeta(cfg, t),
  }))
}

export async function callTool(cfg: PluginConfig, name: string, rawArgs: unknown, env?: Record<string, any>) {
  const t = cfg.tools.find((x) => x.name === name)
  if (!t) return { content: [{ type: 'text', text: `Unknown tool ${name}` }], isError: true }
  try {
    const args = validate(t.inputSchema, unwrapArgs(rawArgs))
    const r = await t.run(args, env)
    const structuredContent: JsonObject = { ...(r.data || {}) }
    if (r.card) structuredContent.card = r.card as any
    return { content: [{ type: 'text', text: r.text }], structuredContent, _meta: toolMeta(cfg, t) }
  } catch (e) {
    // Never echo inputs. InputError messages name the field only. Plain Error messages written by the plugin
    // ("station not found in the bundled list", "use list_specs") are surfaced so ChatGPT can recover, unless they
    // contain any user-supplied string value (carpet audit Oct 1 2026: 21 plugins had useful messages swallowed).
    const msg = e instanceof InputError ? e.message : safeMessage(e, rawArgs)
    if (!(e instanceof InputError)) console.error(`tool ${name} failed: ${e instanceof Error ? e.name : 'error'}`)
    return { content: [{ type: 'text', text: msg }], isError: true }
  }
}

const GENERIC_ERROR = 'Something went wrong computing this. Please check the inputs and try again.'
function userStrings(v: unknown, out: string[] = []): string[] {
  if (typeof v === 'string') { if (v.trim().length >= 2) out.push(v.trim().toLowerCase()) }
  else if (typeof v === 'number' && String(v).length >= 3) out.push(String(v))
  else if (v && typeof v === 'object') for (const x of Object.values(v as object)) userStrings(x, out)
  return out
}
export function safeMessage(e: unknown, rawArgs: unknown): string {
  if (!(e instanceof Error) || e.name !== 'Error' || !e.message || e.message.length > 300) return GENERIC_ERROR
  const m = e.message.toLowerCase()
  if (userStrings(rawArgs).some((s) => m.includes(s))) return GENERIC_ERROR
  return e.message
}

/** Usage metric for the daily ChatGPT traffic loop (Workers Logs, evt=mcp_call). Logs ONLY plugin slug, method,
 * a REGISTERED tool name (anything else -> 'unknown') and a coarse client class. Never arguments, ids or raw UA. */
export function clientClass(ua: string, qaHeader = ''): string {
  // Our own traffic (MCP verify, curl, collector, lanes) sends X-Lauki-QA: 1 and/or a lauki-qa/ UA (carpet, Oct 2 2026).
  if (qaHeader === '1' || /^lauki-qa\//i.test(ua) || /python-urllib|curl\/|node-fetch|headlesschrome/i.test(ua)) return 'qa'
  if (/openai|chatgpt/i.test(ua)) return 'openai'
  if (/claude|anthropic/i.test(ua)) return 'anthropic'
  // Directory/registry scanners + inspectors (Oct 4 2026: listings on MCP Registry, mcp.so, Smithery brought scanner traffic).
  // Smithery = ambiguous: its listing scanner AND its gateway relaying real users share the name -> own class (carpet, Oct 4 2026).
  if (/smithery/i.test(ua)) return 'smithery'
  if (REGISTRY_RE.test(ua)) return 'registry'
  // Generic HTTP SDKs (Oct 5 2026: Go-http-client from a Hostinger audit host counted as external) -> script, never external.
  return /node|undici|curl|python|go-http-client|okhttp|axios|java\/|libwww|httpx|aiohttp/i.test(ua) ? 'script' : 'other'
}
// NOT mcp-remote: that is the stdio bridge real Claude Desktop/Cursor users run (carpet, Oct 4 2026).
const REGISTRY_RE = /glama|pulsemcp|mcp\.so|modelcontextprotocol|mcp-inspector|inspector|verifymcp|bot\b|crawler|spider|scanner|audit/i  // audit: SaSame-MCP-Audit (Hostinger AS47583) called every tool 2x on Oct 4 2026
/** Coarse class from initialize params.clientInfo.name. Never logs the raw name. */
export function clientInfoClass(name: unknown): string | undefined {
  if (typeof name !== 'string' || !name) return undefined
  if (/openai|chatgpt/i.test(name)) return 'openai'
  if (/claude|anthropic/i.test(name)) return 'anthropic'
  if (/smithery/i.test(name)) return 'smithery'
  if (REGISTRY_RE.test(name)) return 'registry'
  return undefined
}
export function logCalls(cfg: PluginConfig, body: unknown, ua: string, qaHeader = '') {
  const base = clientClass(ua, qaHeader)
  for (const m of (Array.isArray(body) ? body.slice(0, 20) : [body]) as any[]) {
    const method = m && typeof m.method === 'string' ? m.method : ''
    if (method !== 'tools/call' && method !== 'initialize' && method !== 'tools/list') continue
    const n = m.params?.name
    const tool = method === 'tools/call' ? (cfg.tools.some((t) => t.name === n) ? n : 'unknown') : undefined
    let client = base
    if (client !== 'qa') {
      // Probe tools (e.g. __verifymcp_auth_probe_*) are scanners by construction.
      if (method === 'tools/call' && typeof n === 'string' && n.startsWith('__')) client = 'registry'
      else if (method === 'initialize' && (client === 'other' || client === 'script')) client = clientInfoClass(m.params?.clientInfo?.name) || client
    }
    console.log(JSON.stringify({ evt: 'mcp_call', plugin: cfg.slug, method, tool, client }))
  }
}

async function handleRpc(cfg: PluginConfig, msg: any, env?: Record<string, any>): Promise<JsonObject | null> {
  const id = msg && (typeof msg.id === 'string' || typeof msg.id === 'number') ? msg.id : null
  const method = msg && typeof msg.method === 'string' ? msg.method : ''
  const ok = (result: unknown) => ({ jsonrpc: '2.0', id, result }) as JsonObject
  const err = (code: number, message: string) => ({ jsonrpc: '2.0', id, error: { code, message } }) as JsonObject
  if (id === null && method.startsWith('notifications/')) return null
  switch (method) {
    case 'initialize': {
      const asked = msg.params?.protocolVersion
      return ok({ protocolVersion: PROTOCOLS.includes(asked) ? asked : PROTOCOLS[1], capabilities: { tools: { listChanged: false }, resources: { listChanged: false } }, serverInfo: { name: cfg.slug, title: cfg.name, version: cfg.version } })
    }
    case 'ping': return ok({})
    case 'tools/list': return ok({ tools: listTools(cfg) })
    case 'tools/call': return ok(await callTool(cfg, msg.params?.name, msg.params?.arguments, env))
    case 'resources/list': return ok({ resources: [{ uri: widgetUri(cfg), name: `${cfg.name} card`, mimeType: 'text/html+skybridge' }] })
    case 'resources/templates/list': return ok({ resourceTemplates: [] })
    case 'resources/read': {
      if (msg.params?.uri !== widgetUri(cfg)) return err(-32602, 'Unknown resource')
      return ok({ contents: [{ uri: widgetUri(cfg), mimeType: 'text/html+skybridge', text: widgetHtml(ACCENT[cfg.funnel.origin] || '#b4532a'), _meta: { 'openai/widgetDescription': cfg.widgetDescription, 'openai/widgetPrefersBorder': true, 'openai/widgetCSP': { connect_domains: [], resource_domains: [] } } }] })
    }
    case 'prompts/list': return ok({ prompts: [] })
    default: return id === null ? null : err(-32601, 'Method not found')
  }
}

const ACCENT: Record<string, string> = { 'https://naksha.social': '#c2410c', 'https://gulab.ai': '#db2777', 'https://jawd.in': '#1d4ed8', 'https://lauki.chat': '#15803d', 'https://zelta.in': '#0f766e' }

export function makeWorker(cfg: PluginConfig) {
  return {
    async fetch(request: Request, env?: Record<string, any>): Promise<Response> {
      const url = new URL(request.url)
      if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS })
      // OpenAI plugin domain verification: token per worker via `wrangler secret put OPENAI_APPS_CHALLENGE`
      if (url.pathname === '/.well-known/openai-apps-challenge') {
        const tok = env?.OPENAI_APPS_CHALLENGE
        return tok ? new Response(String(tok).trim(), { headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store' } }) : new Response('Not found', { status: 404 })
      }
      if (url.pathname === '/privacy') return new Response(privacyHtml(cfg), { headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'public, max-age=3600' } })
      if (request.method === 'GET' && (url.pathname === '/' || url.pathname === '/health')) {
        return Response.json({ name: cfg.slug, version: cfg.version, endpoint: '/mcp', tools: cfg.tools.map((t) => t.name), privacy: `${url.origin}/privacy` }, { headers: { 'cache-control': 'no-store', ...CORS } })
      }
      if (url.pathname !== '/mcp') return new Response('Not found', { status: 404 })
      if (request.method === 'DELETE') return new Response(null, { status: 204, headers: CORS })
      if (request.method !== 'POST') return new Response('Method not allowed', { status: 405, headers: { allow: 'POST, OPTIONS', ...CORS } })
      let body: any
      try {
        const raw = await request.text()
        if (raw.length > 64_000) return Response.json({ jsonrpc: '2.0', id: null, error: { code: -32600, message: 'Request too large' } }, { status: 413, headers: CORS })
        body = JSON.parse(raw)
      } catch {
        return Response.json({ jsonrpc: '2.0', id: null, error: { code: -32700, message: 'Parse error' } }, { status: 400, headers: CORS })
      }
      const headers = { 'content-type': 'application/json', 'cache-control': 'no-store', ...CORS }
      logCalls(cfg, body, request.headers.get('user-agent') || '', request.headers.get('x-lauki-qa') || '')
      if (Array.isArray(body)) {
        const out = (await Promise.all(body.slice(0, 20).map((m) => handleRpc(cfg, m, env)))).filter(Boolean)
        return out.length ? new Response(JSON.stringify(out), { headers }) : new Response(null, { status: 202, headers: CORS })
      }
      const res = await handleRpc(cfg, body, env)
      return res ? new Response(JSON.stringify(res), { headers }) : new Response(null, { status: 202, headers: CORS })
    },
  }
}
