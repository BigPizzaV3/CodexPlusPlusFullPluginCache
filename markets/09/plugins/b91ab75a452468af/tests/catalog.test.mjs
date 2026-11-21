import test from 'node:test'
import assert from 'node:assert/strict'
import { attribution, buildCart, normalizeCatalog, trackedCheckout, trackedLink } from '../src/catalog.ts'

const live = {
  product: { currencyCode: 'INR', variants: [
    { code: 'JAWD-L1-COBALT-30', title: 'Cobalt · 30 lb', price: '499.00', available: true, stock: 292 },
    { code: 'JAWD-L2-EMBER-50', title: 'Ember · 50 lb', price: '599.00', available: true, stock: 302 },
    { code: 'JAWD-L3-ONYX-60', title: 'Onyx · 60 lb', price: '699.00', available: true, stock: 272 },
  ] },
  bundle: { sku: 'JAWD-SET-COMPLETE-3', title: 'JAWD Complete Set', price: 1599, currencyCode: 'INR', available: true, stock: 272 }
}
const response = (body, status = 200) => new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } })

test('exact attribution is used on product links', () => {
  assert.equal(trackedLink('/#levels', 'get_product'), 'https://jawd.in/?utm_source=chatgpt&utm_medium=plugin&utm_campaign=jawd_plugin&utm_content=get_product--inline#levels')
  assert.deepEqual(attribution('search_products'), { utm_source: 'chatgpt', utm_medium: 'plugin', utm_campaign: 'jawd_plugin', utm_content: 'search_products--inline' })
})
test('checkout keeps bare checkout flag and adds UTMs plus order attributes', () => {
  const out = trackedCheckout('https://wgx1s9-5g.myshopify.com/cart/123:1?checkout')
  assert.match(out, /\?checkout&/)
  for (const item of ['utm_source=chatgpt', 'utm_medium=plugin', 'utm_campaign=jawd_plugin', 'utm_content=build_cart--inline', 'attributes%5Butm_source%5D=chatgpt']) assert.match(out, new RegExp(item))
})
test('checkout rejects non-Shopify and malformed links', () => {
  assert.throws(() => trackedCheckout('https://evil.example/cart/1:1?checkout'))
  assert.throws(() => trackedCheckout('https://wgx1s9-5g.myshopify.com/cart/1:1?checkout=1'))
})
test('catalog strict validation and links', () => {
  const products = normalizeCatalog(live, 'search_products')
  assert.equal(products.length, 4)
  assert.equal(products[3].price, 1599)
  assert.match(products[0].url, /utm_content=search_products/)
  assert.throws(() => normalizeCatalog({ nope: true }, 'search_products'))
})
test('build cart calls Jawd endpoint and adds attribution', async () => {
  let request
  const result = await buildCart({ lines: [{ sku: 'JAWD-L1-COBALT-30', quantity: 1 }] }, async (url, init) => { request = { url, init }; return response({ checkoutUrl: 'https://wgx1s9-5g.myshopify.com/cart/123:1?checkout' }) })
  assert.equal(request.url, 'https://jawd.in/api/checkout')
  assert.deepEqual(JSON.parse(request.init.body), { lines: [{ sku: 'JAWD-L1-COBALT-30', quantity: 1 }] })
  assert.match(result.checkout_url, /attributes%5Butm_campaign%5D=jawd_plugin/)
})
test('build cart rejects duplicate overflow and upstream failure', async () => {
  await assert.rejects(() => buildCart({ lines: [{ sku: 'JAWD-L1-COBALT-30', quantity: 5 }, { sku: 'JAWD-L1-COBALT-30', quantity: 1 }] }, async () => response({ error: 'bad' }, 400)))
  await assert.rejects(() => buildCart({ lines: [{ sku: 'JAWD-L1-COBALT-30', quantity: 1 }] }, async () => response({}, 500)))
})
