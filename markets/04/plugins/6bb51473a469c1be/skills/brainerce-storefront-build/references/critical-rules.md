# Brainerce Critical Rules

Violating any of these causes production incidents. Read them before writing SDK code. These rules are framework-neutral — they apply to Next.js, Remix, Vite, Vue, Svelte, or any other client you build.

## SDK usage

- ALWAYS call the `brainerce` SDK client. Never reconstruct REST URLs or call `fetch` against the API directly.
- NEVER invent SDK method names. If a method isn't in `get-sdk-docs` or `get-type-definitions`, it doesn't exist.
- NEVER hardcode product data, category lists, or store copy that should come from the API. Brainerce is the database.
- NEVER use `submitGuestOrder()` or `createOrder()` to "skip checkout" — those bypass payment and produce unpaid orders.
- ALWAYS use the SDK helpers (`getCartTotals`, `formatPrice`, `getProductPriceInfo`, `getCartItemImage`, `getCartItemName`, `getVariantPrice`, `getStockStatus`, `getDescriptionContent`) instead of reading raw fields. The helpers are the only thing that understands the SDK's discriminated unions.

## State management

- The SDK manages cart, checkout, and session state. Do NOT duplicate it in your own store/Redux/context. Read through the SDK and call its mutation methods.
- The cart ID must be persisted between reloads so users don't lose items. Let the SDK handle this — do NOT write your own cart-to-localStorage code.
- Product lists, categories, and inventory counts are NOT client state. Fetch on demand; don't cache stale copies in localStorage or IndexedDB.
- Discount rules and coupon validity are evaluated server-side. Never re-implement them client-side.

## Authentication

- ALWAYS handle the `requiresVerification` flag in `register` and `login` responses. If true, redirect the user to an email verification step BEFORE treating them as logged in.
- ALWAYS build the verify-email, forgot-password, and reset-password flows even when the store currently has email verification disabled. They auto-hide when unused and must exist for when the store owner flips the setting.
- ALWAYS build OAuth button placeholders and a callback handler even when no OAuth provider is configured. Same reason — store owners enable providers later.
- NEVER silently swallow auth errors. Render the specific error (invalid credentials, expired token, rate limited) so the user knows what happened.

## Checkout & orders

- The checkout sequence is: `setShippingAddress` → pick a shipping rate from the returned list → `getPaymentProviders` → provider-specific confirm → `handlePaymentSuccess` → `waitForOrder`. Never skip a step, never reorder them.
- ALWAYS call `handlePaymentSuccess(checkoutId)` on the confirmation page. Without it the cart isn't cleared and the customer sees stale items on their next visit.
- ALWAYS call `waitForOrder(checkoutId)` to poll for the real order before showing an order number. The payment callback may return before the order record is written.
- NEVER treat the checkout total as the cart total — they diverge (tax, shipping, discounts). Display `checkout.lineItems` on the summary, not `cart.items`.
- The reservation timer is a hard guarantee. Display the countdown from the SDK and let the SDK handle expiry — do NOT invent your own timer.
- NEVER send a field that isn't on the DTO. Every write endpoint validates against a strict allow-list and ONE unknown property rejects the whole call with `400 "property X should not exist"` — it does not degrade, it blocks that step for every shopper. This bites on the address step: `getAddressDetails()` resolves an address carrying `lat`, `lng` and `formattedAddress`, which no address endpoint accepts, so spreading it into `setShippingAddress()` sends all three. The SDK (>=1.53.0) strips exactly those three, so the spread is safe — but do not send coordinates deliberately: zone matching decides which shipping rate is charged, so the server resolves them itself from `placeId`. `address.lat`/`lng` are for YOUR UI (map pin, distance); `placeId` is what reaches zone matching.
- ALWAYS pass `placeId` (and the same `placeSessionToken`) to `setShippingAddress` when the address came from the autocomplete, and CLEAR it as soon as the shopper edits any address field. Without it the server geocodes the typed text — materially less precise, and the failure is silent: a same-named street in a neighbouring city can win, quoting another area's rate or "we don't deliver here" for an address the store does cover.

## Auth tokens & BFF pattern

- NEVER store customer auth tokens in `localStorage` directly from client code. Use a Backend-For-Frontend proxy: the server receives the token, sets an HttpOnly cookie, and the client reads session state from an endpoint like `/api/auth/me`.
- NEVER put the admin API key (`brainerce_*`) in client code. It is a server-only secret. Client code uses `salesChannelId` (or the deprecated `connectionId` alias) or storefront endpoints.
- OAuth callbacks arrive with the token in URL params. Extract it SERVER-side and exchange it for a session cookie before redirecting to the app. Do not let the token land in browser history.
- On logout, clear the BFF session server-side. A client-only logout that forgets to tell the server leaves an active session on the server until it expires.

## Internationalization

- NEVER hardcode currency, locale, or language strings. Read them from `get-store-info` / `get-store-capabilities` and use the configured values.
- NEVER format prices with `toFixed(2)` or custom logic. Use `formatPrice()` from the SDK — it honors the store's currency and locale.
- When the store has i18n enabled (`capabilities.store.i18n.enabled === true`), you MUST call `client.setLocale(locale)` at app init and include a language switcher. All SDK reads will then return localized content automatically.
- For RTL direction, do NOT maintain a local list of RTL locales. Call `client.getStoreDirection(locale)` — it returns `'ltr' | 'rtl'` for any BCP-47 tag (covers Arabic, Hebrew, Persian, Urdu, Yiddish, and any future RTL locales the platform adds). Set `<html dir={...}>` from this value. The platform's CSS reversal handles flex layouts — do not manually swap them.

## Type safety

- NEVER use `as any` or `as unknown as`. If a type doesn't fit, either fix the usage or check the type via the SDK helpers.
- NEVER write your own copies of SDK types (Cart, Product, Order, Checkout, Address). Import them: `import type { Cart, Product } from 'brainerce'`.
- All prices are STRINGS in the SDK. `parseFloat` them before math or comparisons.
- CartItem and CheckoutLineItem are NESTED (`item.product.name`, `item.unitPrice`). OrderItem is FLAT (`item.name`, `item.price`). They are not interchangeable.
- Cart has no `.total` field — call `getCartTotals(cart)` to get `{ subtotal, tax, shipping, discount, total }`.
- `smartGetCart()` returns `CartWithIncludes` (extends `Cart`). Pass `{ include: ['recommendations', 'upgrades', 'bundles'] }` to fetch extras in one request.
- `startGuestCheckout()` is also a discriminated union. Check `result.tracked` before reading `result.checkoutId`.