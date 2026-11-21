import { McpServer } from '@modelcontextprotocol/server'
import { createMcpHandler } from 'agents/mcp/server'
import { z } from 'zod'
import { buildCart, loadProducts } from './catalog'
import { logCalls } from './usage'

type Env = { PLUGIN_VERSION?: string }
const text = (value: unknown) => ({ content: [{ type: 'text' as const, text: typeof value === 'string' ? value : JSON.stringify(value, null, 2) }] })
const error = (message: string) => ({ content: [{ type: 'text' as const, text: message }], isError: true })

function createServer(env: Env) {
  const server = new McpServer({ name: 'jawd', version: env.PLUGIN_VERSION || '0.1.0' })
  server.registerTool('search_products', { description: 'Use this when the user is shopping for a jawline exerciser, jaw trainer, chewing/face-fitness device, or wants to see JAWD products. Do not use for medical jaw pain, TMJ, orthodontic, or dental questions.', annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: true }, inputSchema: { query: z.string().optional().describe('Product name, level, or SKU') } }, async ({ query }) => {
    try { const products = await loadProducts('search_products'); const GENERIC = new Set(['jawd', 'jaw', 'jawline', 'trainer', 'trainers', 'exerciser', 'exercisers', 'product', 'products', 'all', 'the', 'a', 'show', 'me', 'face', 'fitness', 'device', 'devices', 'level', 'levels', 'lb']); const words = (query || '').toLowerCase().split(/[^a-z0-9]+/).filter((w) => w && !GENERIC.has(w)); const hits = words.length ? products.filter((p) => words.some((w) => `${p.sku} ${p.title}`.toLowerCase().includes(w))) : products; return text({ products: hits.length ? hits : products, ...(words.length && !hits.length ? { note: 'No exact match; showing the full JAWD range.' } : {}) }) } catch (e) { return error(e instanceof Error ? e.message : 'Catalog unavailable') }
  })
  server.registerTool('get_product', { description: 'Use this when the user names a JAWD product or SKU and wants current price, stock, image, or a product link. Do not use for medical jaw pain, TMJ, orthodontic, or dental questions.', annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: true }, inputSchema: { sku: z.string().describe('JAWD SKU, for example JAWD-L1-COBALT-30 or JAWD-SET-COMPLETE-3') } }, async ({ sku }) => {
    try { const products = await loadProducts('get_product'); const product = products.find((p) => p.sku.toLowerCase() === sku.trim().toLowerCase()); return product ? text(product) : error(`No JAWD product found for SKU ${sku}`) } catch (e) { return error(e instanceof Error ? e.message : 'Catalog unavailable') }
  })
  server.registerTool('recommend_routine', { description: 'Use this when the user asks how to start or structure jaw or face exercise. General fitness guidance only; no medical, cosmetic-outcome, or weight-loss claims. Do not use for medical jaw pain, TMJ, orthodontic, or dental questions.', annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false }, inputSchema: { experience: z.enum(['new', 'some-experience', 'experienced']).describe('Current experience with resistance jaw exercisers'), goal: z.enum(['start-easy', 'progressive-training', 'complete-set']).describe('Shopping goal') } }, async ({ experience, goal }) => {
    const recommendation = experience === 'new' || goal === 'start-easy' ? 'Start with Cobalt (30 lb), use short comfortable sessions, and stop if you feel pain.' : goal === 'complete-set' ? 'The Complete Set includes Cobalt, Ember, and Onyx for gradual progression. Start at the lowest comfortable level.' : 'Choose Cobalt for a conservative start, Ember only after Cobalt feels comfortable, and Onyx only for experienced users.'
    return text({ recommendation, disclaimer: 'JAWD products are fitness accessories, not medical devices. Do not use if it causes pain; consult a qualified professional for personal health advice.' })
  })
  server.registerTool('build_cart', { description: 'Use this only after the user picks a product and quantity and asks to buy. Returns an external Shopify checkout link on JAWD\'s store; nothing is charged in ChatGPT. Do not use for medical jaw pain, TMJ, orthodontic, or dental questions.', annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false }, inputSchema: { lines: z.array(z.object({ sku: z.string(), quantity: z.number().int().min(1).max(5) }).strict()).min(1).max(4).describe('SKU and quantity lines') } }, async ({ lines }) => {
    try { return text(await buildCart({ lines })) } catch (e) { return error(e instanceof Error ? e.message : 'Checkout link unavailable') }
  })
  return server
}
const handler = createMcpHandler(() => createServer({ PLUGIN_VERSION: '0.1.0' }), { route: '/mcp', corsOptions: { origin: '*', methods: 'GET,POST,DELETE,OPTIONS', headers: 'Content-Type,Authorization,Mcp-Session-Id', maxAge: 86400 } })
export default { async fetch(request: Request, env: Env, ctx: ExecutionContext) {
  const url = new URL(request.url)
  if (request.method === 'GET' && url.pathname === '/.well-known/openai-apps-challenge') return new Response('VZbJqdBJfUZk5gypAUb4Cx0UV0vSlmne0VeZey2utBw', { headers: { 'content-type': 'text/plain', 'cache-control': 'no-store' } })
  if (request.method === 'GET' && (url.pathname === '/' || url.pathname === '/health')) return new Response(JSON.stringify({ name: 'jawd-chatgpt-plugin', version: env.PLUGIN_VERSION || '0.1.0', endpoint: '/mcp', tools: ['search_products', 'get_product', 'recommend_routine', 'build_cart'], privacy: 'https://jawd.in/privacy.html' }), { headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } })
  if (request.method === 'POST' && url.pathname === '/mcp') {
    try { logCalls(await request.clone().json(), request.headers.get('user-agent') || '', request.headers.get('x-lauki-qa') || '') } catch { /* non-JSON body: handler answers it */ }
  }
  return handler(request as any, env as any, ctx as any)
} }
