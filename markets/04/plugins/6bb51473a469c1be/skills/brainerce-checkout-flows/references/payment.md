## Payment Provider Detection (DO THIS FIRST on checkout page!)

```typescript
const { hasPayments, providers, defaultProvider } = await client.getPaymentProviders();
if (!hasPayments) {
  // Show error: "Payment is not configured for this store"
  return;
}
// Primary vs additive (Shopify-parity): render wallets as express buttons ABOVE the card form.
const expressMethods = providers.filter(p => p.isAdditive);           // e.g. PayPal (WALLET)
const primary = defaultProvider && !defaultProvider.isAdditive ? defaultProvider : undefined;
```

Each provider has: `id`, `provider` (flexible string — `'stripe'`, `'grow'`, `'paypal'`, `'cardcom'`, `'morning'`, `'takbull'`, `'sandbox'`, and future providers), `name`, `publicKey`, `stripeAccountId` (Stripe only), `supportedMethods`, `testMode`, `isDefault`, plus the taxonomy fields `methodType` (`'CREDIT_CARD'` = the single primary card processor that settles the order; `'WALLET'`/other = additive), `isAdditive`, and `presentation` (`'card_form'` | `'express_button'` | …).

**Primary vs. additive:** there is one primary card processor (the `defaultProvider`, `isAdditive: false`) plus any additive methods (`isAdditive: true`, e.g. PayPal). Render additive methods as accelerated-checkout **express buttons above** the card form — they sit alongside the primary, never replace it. Create the intent with the tapped provider's `id`. (Exception: a wallet-only store has no card processor, so its wallet becomes the `defaultProvider` and stands alone.)

The payment intent returned from `createPaymentIntent()` includes a `clientSdk` object whose `renderType` tells you exactly how to render — **branch on THAT, not on the provider name**:

- `renderType: 'sdk-widget'` — load `clientSdk.scriptUrl`, mount into `<div id={clientSdk.containerId}>`. Used by Stripe, PayPal, Grow. The SDK paints its own form in your DOM.
- `renderType: 'iframe'` — render `<iframe src={clientSecret}>`. Two flavors detected by URL path:
  - Path contains `/embed/` → Brainerce-hosted embed. Render **INLINE** (no modal). Listen for `brainerce:resize` / `brainerce:redirect` postMessages. Used by Cardcom (embedded mode).
  - Any other URL → provider-hosted page. Render inside a **modal**. Used by Cardcom (hosted mode), legacy Grow iframe.
- `renderType: 'redirect'` — `window.location.href = URL`. Customer completes payment off-site and returns via SuccessRedirectUrl.
- `renderType: 'sandbox'` — show a "Complete Test Order" button; call `completeGuestCheckout(checkoutId)`. Orders are `isTestOrder: true`. Appears when `sandboxPaymentsEnabled` is true.
- `renderType: 'embedded-fields'` — reserved for future Stripe-Elements-style pattern (PCI micro-iframes for card/CVV mounted directly into the merchant form). **No provider ships this today** — handle via a "not supported yet" fallback.

Provider-specific install notes:
- **Stripe:** `npm install @stripe/stripe-js @stripe/react-stripe-js` — `loadStripe(publicKey, { stripeAccount })`
- **PayPal:** `npm install @paypal/react-paypal-js` — `PayPalScriptProvider` + `PayPalButtons`
- **Grow:** No SDK needed — JS SDK loaded via `clientSdk.scriptUrl`. Supports credit cards, Bit, Apple Pay, Google Pay.
- **Cardcom:** No SDK needed — rendering driven by `renderType: 'iframe'` + the inline/modal branch above. Supports credit cards, Bit (when terminal provisions it), installments, 3D Secure.