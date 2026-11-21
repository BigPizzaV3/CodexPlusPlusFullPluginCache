// Usage metric for the daily ChatGPT traffic loop (Workers Logs evt=mcp_call), same shape as chatgpt-plugin-template core 0caca1d.
// Logs ONLY plugin, method, a registered tool name (else 'unknown') and a coarse client class. Never arguments, ids or raw UA.
export const TOOLS = ['search_products', 'get_product', 'recommend_routine', 'build_cart']
export function clientClass(ua: string, qaHeader = ''): string {
  if (qaHeader === '1' || /^lauki-qa\//i.test(ua) || /python-urllib|curl\/|node-fetch|headlesschrome/i.test(ua)) return 'qa'
  return /openai|chatgpt/i.test(ua) ? 'openai' : /claude|anthropic/i.test(ua) ? 'anthropic' : /node|undici|curl|python/i.test(ua) ? 'script' : 'other'
}
export function logCalls(body: unknown, ua: string, qaHeader = '') {
  const client = clientClass(ua, qaHeader)
  for (const m of (Array.isArray(body) ? body.slice(0, 20) : [body]) as any[]) {
    const method = m && typeof m.method === 'string' ? m.method : ''
    if (method !== 'tools/call' && method !== 'initialize' && method !== 'tools/list') continue
    const n = m.params?.name
    const tool = method === 'tools/call' ? (TOOLS.includes(n) ? n : 'unknown') : undefined
    console.log(JSON.stringify({ evt: 'mcp_call', plugin: 'jawd-chatgpt-plugin', method, tool, client }))
  }
}
