# Brainerce Business Flows

These sequences are framework-neutral and non-negotiable. Your framework and file layout are your choice — the order of SDK calls and the error handling is not.

## Checkout

The checkout sequence is strict. Skipping or reordering any step produces broken orders.

1. **Collect address + email.** Build a form that captures customer email, billing address, shipping address (with `line1`, `line2`, `city`, `region`, `postalCode`, `country`). `email` is REQUIRED on `SetShippingAddressDto`. Optionally turn `line1` into an autocomplete typeahead instead of plain text — see `get_code_example('checkout-address-autocomplete')`. Keep city/region/postalCode/country visible and editable even after autocomplete fills them (never hide them — the lookup is never 100% accurate). Auto-fill line1/city/postalCode/country directly from the resolved address. For `region`: it's Google's own administrative-area code, usually (not guaranteed) the same ISO 3166-2 subdivision code this store's region list uses — validate it against `getShippingDestinations().regions[country]` (match by `code`) before assigning it; if it's not a recognized code, leave the dropdown for manual selection instead of assigning an unrecognized value.
2. **Submit the address to get shipping rates.**
   ```ts
   const { checkout, rates } = await client.setShippingAddress(checkoutId, {
     email,
     firstName,
     lastName,
     line1, line2, city, region, postalCode, country,
     placeId,           // REQUIRED whenever the address came from the autocomplete
     placeSessionToken, // the same token used for those autocomplete calls
   });
   ```
   `rates` = available shipping rates for that address + the store's zones. `checkout` = updated checkout object.

   **If you used the autocomplete, you MUST pass `placeId` through here.** The server re-resolves it to the address's exact coordinates and matches map-drawn ("polygon") delivery zones against those. Drop it and the server has to geocode the typed address text instead, which is materially less precise — a same-named street in a neighbouring city can outrank the right one, so the shopper is quoted another area's rate or told there is no delivery at all. Clear `placeId` if the shopper edits any address field after picking a suggestion — the coordinates belong to the suggestion, not to the edited text, and dropping it correctly falls back to geocoding what they actually typed. Never send `lat`/`lng`: no such field exists, because zone matching decides which rate is charged and coordinates are therefore never accepted from the client.
3. **Let the customer pick a rate**, then persist the selection:
   ```ts
   await client.selectShippingMethod(checkoutId, rateId);
   ```
   Label each row with `rate.speedTier` (`'cheapest' | 'balanced' | 'fastest'`) and `rate.estimatedDays` — NOT `rate.name`, which on a live carrier rate is the carrier's own service code (`USPS PriorityMailInternational`) and means nothing to a shopper. Write the tier labels in the store's language (`{ cheapest: 'Standard delivery', balanced: 'Express delivery', fastest: 'Priority delivery' }`). Manual zone rates carry no `speedTier` — show their `name` exactly as the merchant wrote it. Carrier rates arrive already narrowed to at most three, cheapest first; do not filter them further.
4. **Fetch payment providers:**
   ```ts
   const providers = await client.getPaymentProviders();
   ```
   The response tells you which providers are configured (Stripe, Grow, PayPal, Sandbox) and how to render each. Each provider has a `renderType` telling you whether to show a Stripe Elements form, a redirect button, a PayPal button, or a sandbox "complete test order" button.
5. **Confirm payment using the provider's recommended flow.** For Stripe: Stripe Elements → `stripe.confirmCardPayment` using the clientSecret returned by the SDK. For sandbox payments: call `completeGuestCheckout(checkoutId)` directly. For PayPal/Grow: follow the redirect and handle the return on your confirmation page.
6. **On the confirmation page, ALWAYS call both:**
   ```ts
   await client.handlePaymentSuccess(checkoutId);  // clears the cart
   const order = await client.waitForOrder(checkoutId);  // polls until the order exists
   ```
7. **Display `checkout.lineItems`, not `cart.items`, on the summary.** Cart totals and checkout totals diverge (tax, shipping, discounts). Use `checkout.lineItems`, `checkout.shippingAmount`, `checkout.taxAmount`, `checkout.totalAmount`.

Never bypass these steps. Never call `submitGuestOrder` / `createOrder` — those produce unpaid orders.

## Registration

1. **Collect** email, password, first name, last name. Enforce strong passwords client-side: 8+ chars, upper, lower, number, special.
2. **Call registerCustomer:**
   ```ts
   const result = await client.registerCustomer({ email, password, firstName, lastName });
   ```
3. **Branch on `result.requiresVerification`:**
   - If `true`: store the token temporarily (e.g. sessionStorage), route the user to your verify-email UI. Do NOT treat them as logged in yet.
   - If `false`: call `client.setCustomerToken(result.token)`, then `await client.syncCartOnLogin()`, and route to the account area.
4. **On the verify-email step:** collect a 6-digit code and call `client.verifyEmail(code)`. Offer a "resend code" button wired to `client.resendVerificationEmail()`.
5. **After verifyEmail resolves:** call `client.setCustomerToken(result.token)` — the user is now logged in — then `await client.syncCartOnLogin()` to attach the guest cart, and route to the account area.

Build the verify-email step EVEN IF the store currently has verification disabled. It auto-hides; store owners enable it later.

## Login

1. **Collect** email + password.
2. **Call loginCustomer:**
   ```ts
   const result = await client.loginCustomer(email, password);
   ```
3. **Branch on `result.requiresVerification`:**
   - If `true`: route to verify-email. The user must complete verification before accessing account features.
   - If `false`: call `client.setCustomerToken(result.token)`, then `await client.syncCartOnLogin()` to attach the guest cart to the account, and route to the previous page (or account area). Skipping the sync leaves the cart anonymous — first-order discounts and per-customer caps then misbehave for this shopper.
4. **Offer OAuth buttons** from `client.getAvailableOAuthProviders()`. Render a placeholder region even when no providers are returned — the region auto-hides today and shows buttons the moment a provider is enabled in the dashboard.
5. **On error**, render the specific message (invalid credentials, rate limited, account disabled) — never swallow.

## Password reset

Two separate steps — the user navigates out via email between them.

**Forgot password step:**
1. Collect the user's email.
2. `await client.forgotPassword(email)`.
3. ALWAYS show a generic success message ("If that email exists, you'll receive a reset link"), regardless of whether the account exists. Leaking existence is an account enumeration vulnerability.

**Reset password step (user arrives here from the email link):**
1. Read the `token` query parameter from the URL.
2. If the token is missing, show an error and a link back to forgot-password.
3. Collect a new password + confirmation. Enforce the same strength rules as registration.
4. `await client.resetPassword(token, newPassword)`.
5. On success: route to login with a "password updated" message.
6. On expired/invalid token: show the specific error and a link back to forgot-password.

Build both steps EVEN IF the store has no email provider configured today — they auto-hide and must exist.

## OAuth sign-in

1. **Get available provider names:**
   ```ts
   const { providers } = await client.getAvailableOAuthProviders();
   // providers = ['GOOGLE', 'FACEBOOK', 'GITHUB'] (strings, not objects with authorizationUrl)
   ```
2. **For each provider, fetch the authorization URL:**
   ```ts
   const { authorizationUrl } = await client.getOAuthAuthorizeUrl(provider, {
     redirectUrl: `${window.location.origin}/auth/callback`,
   });
   window.location.href = authorizationUrl; // full-page redirect, NOT a popup
   ```
3. **On the callback page** the URL contains `auth_code` + `oauth_success` (or `oauth_error`) query params. Exchange the single-use code for the JWT — never read the token from the URL:
   ```ts
   const params = new URLSearchParams(location.search);
   const code = params.get('auth_code');
   if (code) {
     const result = await client.exchangeOAuthCode(code);
     client.setCustomerToken(result.token);
     await client.syncCartOnLogin(); // REQUIRED — see step 5
     // then redirect to account
   }
   ```
   The legacy `?token=` URL param is still emitted for backward compatibility but will be removed in the next major release — migrate to `auth_code` now.
4. **On failure** the browser lands on the SAME `redirectUrl` (never on the API host), carrying `oauth_error` + `error_description`. `oauth_error` is a stable snake_case code — switch on it for localized copy; `error_description` is English developer detail, not shopper copy:
   ```ts
   const code = params.get('oauth_error');
   if (code === 'link_blocked_unverified_password_account') {
     router.push('/verify-email'); // the address needs verifying — a retry will not help
   } else if (code) {
     router.push(`/login?error=${code}`); // access_denied, state_expired, server_error, ...
   }
   ```
   The code list is open — the provider's own codes pass through, so always handle the default case.
5. **Claim the guest cart:** `await client.syncCartOnLogin()` after `setCustomerToken`. `setCustomerToken` only stores the JWT — it does NOT attach the cart the shopper filled before signing in. Skip this and the cart stays anonymous forever, which silently breaks every feature keyed on buyer identity: "first order only" discounts re-apply to returning customers, per-customer usage caps go unenforced, and abandoned-cart recovery cannot identify the shopper. This is the single most-missed step in the OAuth flow.

Build the OAuth button region AND the callback handler even when no providers are configured. They auto-hide.

## Order confirmation

The confirmation flow must run EVERY time a customer lands on your order confirmation surface, whether they were redirected from Stripe, PayPal, Grow, or a sandbox test button.

1. **Read `checkoutId` from the URL or the session.**
2. **Clear the cart:** `await client.handlePaymentSuccess(checkoutId)`. This is mandatory — without it the cart still contains the purchased items on the next visit.
3. **Wait for the order to exist:** `const order = await client.waitForOrder(checkoutId)`. The payment webhook may return before the order record is written; this helper polls until it appears (or times out).
4. **Render a loading state during step 3.** Users see a "confirming order" spinner, not a "not found" error.
5. **On success:** render the order number and line items from the returned `order` object.
6. **If you were redirected from Grow inside an iframe:** break out of the iframe before rendering so the user sees a full-page confirmation.
7. **On timeout:** show a "we're still processing, you'll receive an email" message with a link to the account order history — the order WILL show up there.

## Cart persistence

The SDK manages the cart's lifecycle. Do NOT reinvent it.

- **Cart ID persistence:** the SDK stores the cart ID across reloads. You do not need to write cart-to-localStorage code yourself.
- **Reads:** `client.getCart()` returns the current cart. Call it on mount in your cart UI and on any page that shows a cart count (header).
- **Writes:** use `client.addToCart`, `client.updateCartItem`, `client.removeCartItem`, `client.applyCoupon`, `client.removeCoupon`. After each mutation the SDK returns the updated cart. On the **checkout page** use `client.applyCheckoutCoupon(checkoutId, code)` / `client.removeCheckoutCoupon(checkoutId)` — these update checkout totals atomically. Never use `applyCoupon` after a checkout session exists.
- **Totals:** call `getCartTotals(cart)` — do NOT read `cart.total`. The helper understands taxes, shipping, and discounts.
- **`smartGetCart()`** returns `CartWithIncludes` (extends `Cart`). All carts are server-side. Pass `{ include: ['recommendations', 'upgrades', 'bundles'] }` to fetch extras in one request.
- **Claim the cart on EVERY sign-in:** `await client.syncCartOnLogin()` immediately after `client.setCustomerToken(...)` — password login, email verification, and OAuth alike. `setCustomerToken` only stores the JWT; it does NOT attach the cart the shopper already filled. An unclaimed cart has no buyer identity, and the failures are silent rather than loud: `customer_first_order` discounts keep applying to returning customers, per-customer usage caps go unenforced at cart time, and abandoned-cart recovery cannot tell who to email. This is the single most-missed call in the auth flow.
- **NEVER mutate cart state outside SDK helpers.** Any hand-rolled cart update risks desync with the reservation timer and the checkout flow.

## Inventory reservation

When inventory reservation is configured on the store, adding an item to the cart reserves stock for a fixed window (the `reservationTimeout` from `get-store-capabilities`). If the window expires before checkout, the reservation is released and the item may become unavailable.

- **Display the countdown** from the cart's reservation field. The SDK returns an expiry timestamp — render the remaining seconds and refresh once per second.
- **On expiry:** call `client.getCart()` to refresh. Items whose reservations expired are flagged by the server.
- **Do NOT implement your own timer logic.** The SDK is the source of truth for reservation state. Client timers drift and mislead users.
- **On the checkout page:** if reservations have expired, block payment and show a "your cart has expired, please review it" message with a link back to the cart page.
- **On the cart page:** show per-item availability — items that can no longer be purchased (because their reservation expired or the stock dropped) should display an "out of stock" badge and the "proceed to checkout" action should be disabled until they are removed.

The reservation strategy (`HARD` vs `SOFT`) is exposed via `get-store-capabilities`. A HARD reservation means the stock is physically held; a SOFT reservation just tracks intent. Your UI behaves identically either way — the SDK hides the difference.

## Product customization (buyer input)

Products can ship with `customizationFields: ProductCustomizationField[]` — buyer-filled inputs (engraving text, uploaded photo, pick-a-color, etc.). If you ignore them, merchants lose the data they need to fulfill the order.

1. **Read the fields** from the product payload. Sort by `position`. If the array is empty, nothing to render.
2. **Render one control per field** based on `type`:
   - `TEXT` / `URL` / `COLOR` / `DIMENSION` / `WEIGHT` → `<input type="text">` (honour `minLength`/`maxLength`)
   - `TEXTAREA` → `<textarea>`
   - `NUMBER` → `<input type="number">` (honour `minValue`/`maxValue`)
   - `BOOLEAN` → checkbox (value `true`/`false`)
   - `DATE` → `<input type="date">` (ISO `YYYY-MM-DD`)
   - `DATETIME` → `<input type="datetime-local">` (ISO timestamp)
   - `SELECT` → `<select>` populated from `enumValues` (value = one string)
   - `MULTI_SELECT` → checkbox group from `enumValues` (value = `string[]`)
   - `IMAGE` → file input + preview (value = one URL string)
   - `GALLERY` → multi-file input (value = `string[]` of URLs)
   - `JSON` → advanced; render an admin-style editor or skip unless you control the data
3. **For IMAGE / GALLERY types: upload FIRST, then attach the URL.** Call `client.uploadCustomizationFile(file)` — it returns `{ url }`. Put that `url` string into the field value. NEVER put a `File` object in cart metadata.
4. **Enforce `required: true` client-side** before add-to-cart — show a red hint, block submit. The server re-validates; you want the user to fix it before the request fails.
5. **Add to cart with metadata keyed by `field.key`:**
   ```ts
   await client.addToCart({
     productId,
     quantity: 1,
     metadata: {
       engraving_text: 'For Mom',
       frame_color: 'Gold',
       upload_photo: photoUrl,      // from uploadCustomizationFile()
       addons: ['Gift wrap'],       // MULTI_SELECT
     },
   });
   ```
6. **On cart / checkout UIs, surface the metadata.** `CartItem.metadata` and `CheckoutLineItem.metadata` carry the values the buyer submitted. Show them in the line-item row so the buyer can verify before paying (especially uploaded image thumbnails).
7. **After the order is placed, values live on `OrderItem.customizations`** — a `Record<string, { label, value, type }>` keyed by field key. Definitions may be renamed/deleted after the order; the snapshot preserves what the buyer saw at purchase time.

**Apply-to-all fields.** A merchant can flag a `MetafieldDefinition` with `appliesToAllProducts: true` — the backend then includes it in every product's `customizationFields` array automatically, including products created after the flag was set. Your client code reads `product.customizationFields` as-is and never merges or unions anything — just render what's there.

Server-side guardrails that WILL reject bad requests (so validate client-side to avoid round-trips):
- Unknown keys → rejected. Only use keys that appear in `product.customizationFields`.
- Missing `required` fields → rejected.
- `SELECT` value not in `enumValues` → rejected.
- `MULTI_SELECT` value not `string[]` OR containing values outside `enumValues` → rejected.
- `IMAGE` / `GALLERY` values must be URLs returned from `/customization-upload` on this store — pasting an external URL is rejected.
- Upload > 5MB or non-image MIME → rejected by upload endpoint.
- More than 10 uploads per IP per minute → 429.

Never render customization fields without also wiring the upload + metadata flow — a form that submits nothing is worse than no form at all.

## Content Bootstrap — site chrome & static content

Every Brainerce storefront should render merchant-defined site chrome (header, footer, announcements, FAQ, static pages) from the Content API. The merchant edits these in the Brainerce dashboard; storefronts pick up changes within ~5 minutes (public reads carry `Cache-Control: public, max-age=300, stale-while-revalidate=60`).

1. **Fetch chrome at the root layout** (server component if Next.js). All three return `null` on 404 — render hard-coded fallbacks so the page never crashes when the merchant hasn't seeded yet.
   ```ts
   const [header, footer, announcements] = await Promise.all([
     client.content.header.get('main', locale),
     client.content.footer.get('main', locale),
     client.content.announcement.list(locale),
   ]);
   ```

2. **FAQ — fetch lazily on the FAQ page.** Default key is `'main'`; pass a topical key (`'shipping'`, `'returns'`) for sub-FAQs.
   ```ts
   const faq = await client.content.faq.get('main', locale);
   if (faq) {
     faq.data.items.forEach(({ question, answer }) => {
       // sanitize(answer) — see step 4
     });
   }
   ```

3. **Static pages — catch-all route by slug:**
   ```tsx
   // app/[slug]/page.tsx
   export default async function Page({ params }) {
     const page = await client.content.page.getBySlug(params.slug, locale);
     if (!page) notFound();
     return (
       <article dangerouslySetInnerHTML={{ __html: sanitize(page.data.html) }} />
     );
   }
   ```

4. **SECURITY — sanitize HTML before rendering.** `FAQ.items[i].answer`, `PAGE.html`, and `RICH_TEXT.html` are merchant-authored HTML. The server does NOT pre-sanitize because some merchants embed iframes (e.g. YouTube). Always sanitize at the edge of your render:
   ```ts
   import DOMPurify from 'isomorphic-dompurify';
   const safe = DOMPurify.sanitize(rawHtml);
   <div dangerouslySetInnerHTML={{ __html: safe }} />;
   ```
   Skipping this is XSS.

5. **Announcements — multiple may be active; filter by date client-side:**
   ```ts
   const now = Date.now();
   const visible = announcements.filter((a) => {
     const startOk = !a.data.startsAt || new Date(a.data.startsAt).getTime() <= now;
     const endOk = !a.data.endsAt || new Date(a.data.endsAt).getTime() >= now;
     return startOk && endOk;
   });
   ```

6. **RTL direction — call `client.getStoreDirection(locale)`:**
   ```tsx
   const dir = client.getStoreDirection(locale);
   <html lang={locale} dir={dir}>...</html>
   ```
   Do NOT maintain a local RTL locale set — the SDK helper covers Arabic / Hebrew / Persian / Urdu / Yiddish today and picks up any future RTL locale automatically.

7. **Custom fields — every Content row has free-form `customFields: Record<string, string>`.** Read keys the merchant told you to expect:
   ```ts
   const faq = await client.content.faq.get('shipping');
   <a href={`mailto:${faq.customFields.helpEmail}`}>Need help?</a>
   ```

8. **Cache:** public reads carry `Cache-Control: public, max-age=300, stale-while-revalidate=60`. Don't add extra client-side caching beyond Next.js's default fetch cache — merchants expect their edits to appear within ~5 minutes.

**Translations.** All public reads accept a `locale` argument; the server resolves `translations[locale]` server-side. Empty / missing overlays fall through to the default-locale value. The storefront does NOT need to do its own per-field overlay — call with the active locale and render what comes back.