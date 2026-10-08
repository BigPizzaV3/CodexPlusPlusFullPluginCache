## ⚠️ CHECKOUT FLOW (CRITICAL — READ CAREFULLY!)

### Guest vs Logged-In — THE #1 cause of "Cart not found" errors!

| User Type | Cart Location | Checkout Method | Get Checkout ID |
|-----------|---------------|-----------------|-----------------|
| **Guest** | localStorage | `startGuestCheckout()` | `result.checkoutId` (check `result.tracked` first!) |
| **Logged-in** | Server | `createCheckout({ cartId })` | `checkout.id` |

```typescript
// ❌ THIS WILL FAIL for guest users — "Cart not found" error!
const cart = await client.smartGetCart();
await client.createCheckout({ cartId: cart.id }); // 💥 "__local__" doesn't exist on server!

// ✅ CORRECT — check user type first!
async function startCheckout() {
  const cart = await client.smartGetCart();

  if (client.isCustomerLoggedIn()) {
    const checkout = await client.createCheckout({ cartId: cart.id });
    return checkout.id;
  } else {
    const result = await client.startGuestCheckout();
    if (!result.tracked) throw new Error('Checkout tracking not enabled');
    return result.checkoutId;
  }
}
```

### Full Checkout Flow (Multi-Provider)

1. Customer fills cart
2. Customer optionally applies coupon on cart page → `applyCoupon(cartId, code)`
3. Detect payment providers → `getPaymentProviders()`
4. Start checkout session (`startGuestCheckout()` or `createCheckout()`)
5. Set shipping address (includes required email) → `setShippingAddress()` — also pass `notes` from the **"Order notes" textarea that every checkout page should include by default** (optional field, max 2000 chars; lands on the order for the merchant)
5b. (Optional) Turn the address `line1` field into a typeahead instead of free text → `getAddressSuggestions(query, sessionToken)` returns predictions as the customer types (debounce ~300ms); `getAddressDetails(placeId, sessionToken)` resolves the picked suggestion to a full address + `inZone` flag. Generate `sessionToken` once per address-entry attempt (e.g. `crypto.randomUUID()`) and reuse it across both calls — this is what keeps the calls cheap even if the customer types a lot. `inZone: false` is a soft signal (show a non-blocking "outside our regular delivery zones — we'll confirm by phone" banner), never a reason to block checkout. Suggestions cover deliverable addresses only — street addresses, routes, buildings, sub-premises — so businesses, stations and other establishments never appear, and a shopper who types only a landmark name gets an empty list. **If you use this, pass the picked `placeId` (and the same `sessionToken`) on to `setShippingAddress()` in step 5** — that is what lets the server match map-drawn ("polygon") delivery zones against exact coordinates rather than re-geocoding the typed address, which can otherwise resolve to a same-named street in another city and quote the wrong zone's rate or none at all.
6. Select shipping method → `selectShippingMethod()`
6b. (Optional) Set checkout custom fields → `setCheckoutCustomFields()` — surcharges auto-calculated
7. Create payment intent → `createPaymentIntent()` → returns `{ clientSecret, provider }`
8. Branch on the **`clientSdk.renderType`** returned by `createPaymentIntent()` — NEVER hard-code by provider name. Values: `'sdk-widget'` (Stripe, PayPal, Grow), `'iframe'` (Cardcom hosted or Brainerce-hosted embed — detect via URL path), `'redirect'`, `'sandbox'`, `'embedded-fields'` (reserved).
9. **Order is created AUTOMATICALLY after payment succeeds (via webhook) — for ALL providers!**

### Checkout Page Component

```typescript
import { loadStripe } from '@stripe/stripe-js';
import { Elements, PaymentElement, useStripe, useElements } from '@stripe/react-stripe-js';

function CheckoutPage() {
  const [paymentData, setPaymentData] = useState<{
    clientSecret: string; provider: string; checkoutId: string; clientSdk?: { renderType: string };
  } | null>(null);
  const [stripePromise, setStripePromise] = useState<ReturnType<typeof loadStripe> | null>(null);
  const [paypalClientId, setPaypalClientId] = useState<string | null>(null);
  const [checkout, setCheckout] = useState<Checkout | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  // Optional "Order notes" textarea — render it on the checkout page by default
  const [orderNotes, setOrderNotes] = useState('');

  useEffect(() => { startCheckout(); }, []);

  async function startCheckout() {
    try {
      const cart = client.getLocalCart();
      if (!cart.customer?.email) { window.location.href = '/cart?error=email_required'; return; }
      if (!cart.shippingAddress) { window.location.href = '/cart?error=address_required'; return; }
      if (cart.items.length === 0) { window.location.href = '/cart?error=cart_empty'; return; }

      // Step 1: Detect available payment providers
      const { hasPayments, providers } = await client.getPaymentProviders();
      if (!hasPayments) { setError('Payment not configured. Contact the store owner.'); return; }
      const stripeProvider = providers.find(p => p.provider === 'stripe');
      const growProvider = providers.find(p => p.provider === 'grow');
      const paypalProvider = providers.find(p => p.provider === 'paypal');

      // Step 2: Start tracked checkout
      const checkoutResult = await client.startGuestCheckout();
      if (!checkoutResult.tracked) { setError('Checkout tracking not enabled'); return; }
      const checkoutId = checkoutResult.checkoutId;

      // Step 3: Set shipping address (email is REQUIRED) — returns available shipping rates!
      const { checkout: checkoutData, rates } = await client.setShippingAddress(checkoutId, {
        email: cart.customer.email,
        firstName: cart.shippingAddress.firstName,
        lastName: cart.shippingAddress.lastName,
        line1: cart.shippingAddress.line1,
        line2: cart.shippingAddress.line2,
        city: cart.shippingAddress.city,
        region: cart.shippingAddress.region,  // NOT "state"!
        postalCode: cart.shippingAddress.postalCode,
        country: cart.shippingAddress.country,
        phone: cart.shippingAddress.phone,
        notes: orderNotes || undefined,  // from the "Order notes" textarea — include one by default
        // Set when the shopper picked an autocomplete suggestion. Lets the server match
        // map-drawn ("polygon") delivery zones against exact coordinates instead of
        // re-geocoding the typed text. Never send lat/lng — no such field exists.
        placeId: pickedPlaceId || undefined,
        placeSessionToken: addressSessionToken || undefined,
      });
      setCheckout(checkoutData);

      // Step 3b: Let customer pick a shipping method from the returned rates
      if (rates && rates.length > 0) {
        // Each rate has: id, price, estimatedDays, and EITHER speedTier (live
        // carrier rate) OR a merchant-written name (manual zone rate).
        // Label carrier rates yourself — never render their `name`, which is the
        // carrier's own service code ('USPS PriorityMailInternational'):
        //   const TIERS = { cheapest: 'Standard delivery', balanced: 'Express delivery', fastest: 'Priority delivery' };
        //   const label = rate.speedTier ? TIERS[rate.speedTier] : rate.name;
        // Carrier rates arrive already narrowed to at most three, cheapest first.
        // For simplicity, auto-select first — in your UI, show a radio/select list
        await client.selectShippingMethod(checkoutId, rates[0].id);
      }

      // Step 4: Create payment intent — returns provider type!
      // Pass saveCard: true when the customer ticked "save my card for next time" —
      // only honored for logged-in customers (not guests). The vaulted card then
      // appears in client.listSavedPaymentMethods(storeId, customerId) and can be
      // charged off-session via subscription / one-click checkout flows.
      const paymentIntent = await client.createPaymentIntent(checkoutId, {
        successUrl: `${window.location.origin}/order-confirmation?checkout_id=${checkoutId}`,
        cancelUrl: `${window.location.origin}/checkout?error=payment_cancelled`,
        // saveCard: customerOptedIn,  // optional opt-in
      });

      setPaymentData({ clientSecret: paymentIntent.clientSecret, provider: paymentIntent.provider, checkoutId, clientSdk: paymentIntent.clientSdk });

      // Step 5: Initialize the correct payment provider
      if (paymentIntent.provider === 'stripe' && stripeProvider) {
        setStripePromise(loadStripe(stripeProvider.publicKey, { stripeAccount: stripeProvider.stripeAccountId }));
      } else if (paymentIntent.provider === 'paypal' && paypalProvider) {
        setPaypalClientId(paypalProvider.publicKey);
      }
      // Grow needs no client-side initialization — uses iframe
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to start checkout');
    } finally {
      setLoading(false);
    }
  }

  if (loading) return <div>Loading checkout...</div>;
  if (error) return <div className="text-red-600">{error}</div>;
  if (!paymentData) return <div>Unable to initialize payment</div>;

  // Render payment UI based on provider
  if (paymentData.provider === 'sandbox') {
    return (
      <div className="text-center p-6 bg-amber-50 border border-amber-200 rounded-lg">
        <h3 className="font-semibold mb-2">Test Mode</h3>
        <p className="text-sm text-gray-600 mb-4">No real payment will be charged.</p>
        <button onClick={async () => {
          await client.completeGuestCheckout(checkoutId);
          window.location.href = \`/order-confirmation?checkout_id=\${checkoutId}\`;
        }} className="bg-amber-500 text-white px-6 py-2 rounded">
          Complete Test Order
        </button>
      </div>
    );
  }
  if (paymentData.clientSdk?.renderType === 'iframe') {
    return <PaymentIframe clientSecret={paymentData.clientSecret} checkoutId={paymentData.checkoutId} />;
  }
  if (paymentData.provider === 'paypal' && paypalClientId) {
    return <PayPalPaymentForm clientId={paypalClientId} orderId={paymentData.clientSecret} checkoutId={paymentData.checkoutId} />;
  }
  if (paymentData.provider === 'stripe' && stripePromise) {
    return (
      <Elements stripe={stripePromise} options={{ clientSecret: paymentData.clientSecret }}>
        <StripePaymentForm checkoutId={paymentData.checkoutId} />
      </Elements>
    );
  }
  return <div>Unable to initialize payment provider</div>;
}
```

### Stripe Payment Form

```typescript
// npm install @stripe/stripe-js @stripe/react-stripe-js
function StripePaymentForm({ checkoutId }: { checkoutId: string }) {
  const stripe = useStripe();
  const elements = useElements();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!stripe || !elements) return;
    setLoading(true);
    setError(null);

    const { error: stripeError } = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: `${window.location.origin}/order-confirmation?checkout_id=${checkoutId}`,
      },
      redirect: 'if_required',
    });

    if (stripeError) { setError(stripeError.message || 'Payment failed'); setLoading(false); return; }
    window.location.href = `/order-confirmation?checkout_id=${checkoutId}`;
  }

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      {error && <div className="text-red-600 mt-4 p-3 bg-red-50 rounded">{error}</div>}
      <button type="submit" disabled={!stripe || loading} className="w-full mt-4 bg-blue-600 text-white py-3 rounded disabled:opacity-50">
        {loading ? 'Processing...' : 'Pay Now'}
      </button>
    </form>
  );
}
```

### Iframe-Based Providers (Cardcom, Sola, legacy Grow, etc.)

When `clientSdk.renderType === 'iframe'`, the payment intent returns a `clientSecret` which is a URL to load in an iframe. There are TWO flavors of iframe rendering you must handle:

**Flavor A — Brainerce-hosted embed (URL path contains `/embed/`):** The iframe loads a Brainerce-branded compact form (e.g. Cardcom OpenFields, Sola iFields). Render it **INLINE** inside your checkout flow (next to the order summary) — NO modal, NO dark overlay. The embed page posts messages to resize itself and to request top-level navigation (e.g. for Bit express-pay buttons).

⚠️ **You MUST call `confirmSdkPayment(checkoutId, data)` on `brainerce:payment-complete` — do NOT just navigate to the confirmation page.** For some providers (e.g. Sola) the card was only *tokenized* inside the iframe; the real charge runs server-side, at confirm time, using the token payload carried in `data`. Skipping this call means the charge never happens and the checkout is stuck in `PAYMENT_PENDING` forever — polling `payment-status` alone cannot recover it for these providers.

**Flavor B — Provider-hosted page (any other URL):** The iframe loads a full provider-branded page with its own header/chrome. Render inside a **modal overlay** so it doesn't fight your checkout layout.

Detect flavor by URL path — works across localhost/staging/prod without a domain list:

```typescript
function PaymentIframe({ clientSecret, checkoutId }: { clientSecret: string; checkoutId: string }) {
  const [height, setHeight] = useState(540); // default before resize message arrives
  const isBrainerceEmbed = (() => {
    try { return new URL(clientSecret).pathname.includes('/embed/'); }
    catch { return false; }
  })();

  useEffect(() => {
    function handleMessage(e: MessageEvent) {
      const data = e.data as { type?: string; height?: number; url?: string };
      if (data?.type === 'brainerce:resize' && typeof data.height === 'number') {
        setHeight(data.height);
      }
      if (data?.type === 'brainerce:redirect' && typeof data.url === 'string') {
        // Top-level navigation (e.g. Bit). ALWAYS validate against an allowlist
        // before navigating — never trust the URL blindly. The SDK ships with
        // a maintained list of payment-provider hosts; prefer it over a local
        // copy so 'npm update brainerce' picks up new providers automatically.
        if (isAllowedPaymentUrl(data.url)) { window.top!.location.href = data.url; }
      }
      if (data?.type === 'brainerce:payment-complete') {
        // REQUIRED: forward the full payload — for confirm-time-charge
        // providers (Sola) this carries the card tokens the server needs to
        // actually run the charge. Do not skip this and just navigate.
        const client = getClient();
        client.confirmSdkPayment(checkoutId, (e.data as { data?: Record<string, unknown> }).data)
          .catch((err) => console.warn('confirmSdkPayment failed:', err))
          .finally(() => { window.location.href = `/order-confirmation?checkout_id=${checkoutId}`; });
      }
    }
    window.addEventListener('message', handleMessage);
    return () => window.removeEventListener('message', handleMessage);
  }, [checkoutId]);

  if (isBrainerceEmbed) {
    // Inline: part of the checkout flow, no overlay
    return (
      <div className="w-full">
        <iframe
          src={clientSecret}
          style={{ width: '100%', height, border: 0, transition: 'height 0.2s ease-out' }}
          title="Payment"
          allow="payment"
        />
      </div>
    );
  }

  // Provider-hosted page: modal overlay
  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center bg-black/50 py-6 overflow-y-auto">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-4xl mx-4">
        <iframe
          src={clientSecret}
          style={{ width: '100%', height: '90vh', minHeight: 700, border: 0 }}
          title="Payment"
          allow="payment"
        />
      </div>
    </div>
  );
}

// Allowlist check is provided by the SDK — covers Stripe, PayPal, Cardcom,
// Meshulam, Grow, CreditGuard, plus Brainerce-hosted embed shells. To extend
// for a self-hosted PSP, pass { extraHosts: ['my-psp.example.com'] }.
import { isAllowedPaymentUrl } from 'brainerce';
```

### PayPal Payment Form

```typescript
// npm install @paypal/react-paypal-js
import { PayPalScriptProvider, PayPalButtons } from '@paypal/react-paypal-js';

function PayPalPaymentForm({ clientId, orderId, checkoutId }: { clientId: string; orderId: string; checkoutId: string }) {
  const [error, setError] = useState<string | null>(null);
  return (
    <div>
      {error && <div className="text-red-600 mb-4">{error}</div>}
      <PayPalScriptProvider options={{ clientId, intent: 'capture' }}>
        <PayPalButtons
          style={{ layout: 'vertical', label: 'pay' }}
          createOrder={() => orderId}
          onApprove={async () => { window.location.href = `/order-confirmation?checkout_id=${checkoutId}`; }}
          onError={(err) => { console.error('PayPal error:', err); setError('Payment failed.'); }}
          onCancel={() => setError('Payment was cancelled.')}
        />
      </PayPalScriptProvider>
    </div>
  );
}
```