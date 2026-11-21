import { z } from 'zod'

export const SKUS = ['JAWD-L1-COBALT-30', 'JAWD-L2-EMBER-50', 'JAWD-L3-ONYX-60', 'JAWD-SET-COMPLETE-3'] as const
export const cartSchema = z.object({ lines: z.array(z.object({ sku: z.enum(SKUS), quantity: z.number().int().min(1).max(5) }).strict()).min(1).max(4) }).strict()
const price = z.union([z.string().regex(/^\d+(\.\d{1,2})?$/), z.number().finite().nonnegative()]).transform(Number)
const catalogSchema = z.object({
  product: z.object({ currencyCode: z.literal('INR'), variants: z.array(z.object({ code: z.string(), title: z.string().max(150), price, available: z.boolean(), stock: z.number().int().nonnegative().nullable() })).max(50) }),
  bundle: z.object({ sku: z.literal('JAWD-SET-COMPLETE-3'), title: z.string().max(150), price, currencyCode: z.literal('INR'), available: z.boolean(), stock: z.number().int().nonnegative().nullable() }).nullable().optional()
})
export function trackedLink(path: string, tool: string, surface = 'inline') {
  const url = new URL(path, 'https://jawd.in')
  if (url.origin !== 'https://jawd.in') throw new Error('Invalid product link')
  const params = new URLSearchParams(attribution(tool, surface))
  url.search = params.toString()
  return url.toString()
}
export function attribution(tool: string, surface = 'inline') {
  if (!/^(inline|panel|sidebar|event)$/.test(surface)) throw new Error('Invalid attribution surface')
  return { utm_source: 'chatgpt', utm_medium: 'plugin', utm_campaign: 'jawd_plugin', utm_content: `${tool}--${surface}` }
}
export function trackedCheckout(raw: string, surface = 'inline') {
  const url = new URL(raw)
  if (url.protocol !== 'https:' || url.hostname !== 'wgx1s9-5g.myshopify.com' || url.port || url.username || url.password || url.hash || !/^\/cart\/\d+:\d+(,\d+:\d+)*$/.test(url.pathname) || !/(^|&)checkout(&|$)/.test(url.search.slice(1))) throw new Error('Invalid checkout link')
  const params = attribution('build_cart', surface)
  const extra = new URLSearchParams(params)
  for (const [key, value] of Object.entries(params)) extra.set(`attributes[${key}]`, value)
  // Do NOT reserialize the original query: Shopify requires bare ?checkout.
  return raw + '&' + extra.toString()
}
export function normalizeCatalog(input: unknown, tool: string) {
  const data = catalogSchema.parse(input)
  const products = data.product.variants.filter(v => SKUS.slice(0, 3).some(s => s === v.code)).map(v => ({ sku: v.code, title: v.title, price: v.price, currency: 'INR', available: v.available && v.stock !== 0, url: trackedLink('/#levels', tool), image_url: trackedLink(`/assets/generated/jawd-exerciser-${v.code.includes('COBALT') ? 'cobalt' : v.code.includes('EMBER') ? 'ember' : 'onyx'}-alpha-v1.png`, tool) }))
  if (data.bundle) products.push({ sku: data.bundle.sku, title: data.bundle.title, price: data.bundle.price, currency: 'INR', available: data.bundle.available && data.bundle.stock !== 0, url: trackedLink('/#complete-set', tool), image_url: trackedLink('/assets/generated/jawd-complete-set-square-v2.png', tool) })
  return products
}
export type Product = ReturnType<typeof normalizeCatalog>[number]
export async function loadProducts(tool: string, fetcher: typeof fetch = fetch) {
  const response = await fetcher('https://jawd.in/api/catalog', { headers: { 'User-Agent': 'jawd-chatgpt-plugin/0.1' }, signal: AbortSignal.timeout(12000), redirect: 'manual' })
  if (response.status >= 300 && response.status < 400) throw new Error('Catalog redirect rejected. Please try again.')
  if (!response.ok) throw new Error('Catalog temporarily unavailable. Please try again.')
  return normalizeCatalog(await response.json(), tool)
}
export async function buildCart(input: unknown, fetcher: typeof fetch = fetch) {
  const parsed = cartSchema.parse(input)
  const totals = new Map<string, number>()
  for (const l of parsed.lines) totals.set(l.sku, (totals.get(l.sku) || 0) + l.quantity)
  if ([...totals.values()].some(v => v > 5)) throw new Error('Maximum five of each product.')
  const lines = [...totals].map(([sku, quantity]) => ({ sku, quantity }))
  const response = await fetcher('https://jawd.in/api/checkout', { method: 'POST', headers: { 'content-type': 'application/json', 'user-agent': 'jawd-chatgpt-plugin/0.1' }, body: JSON.stringify({ lines }), signal: AbortSignal.timeout(12000), redirect: 'manual' })
  if (response.status >= 300 && response.status < 400) throw new Error('Checkout redirect rejected. Please try again.')
  if (!response.ok) throw new Error(response.status === 409 ? 'A selected product is unavailable in that quantity.' : 'Checkout link temporarily unavailable.')
  const data = z.object({ checkoutUrl: z.string().max(4096) }).parse(await response.json())
  return { checkout_url: trackedCheckout(data.checkoutUrl), lines, message: 'Open the Shopify checkout to review final prices, shipping and payment. No order has been placed; payment details stay outside this plugin.' }
}
