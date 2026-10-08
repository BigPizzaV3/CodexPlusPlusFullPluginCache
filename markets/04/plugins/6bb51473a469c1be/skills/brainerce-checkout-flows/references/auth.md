## Customer Authentication

### Register

```typescript
const auth = await client.registerCustomer({ email, password, firstName, lastName });
// Password: min 8 chars, uppercase, lowercase, number, special char
// Also accepted here: phone, birthMonth, birthDay (1-12 / 1-31, no year, both together)

if (auth.requiresVerification) {
  localStorage.setItem('verificationToken', auth.token);
  localStorage.setItem('verificationEmail', email);
  window.location.href = '/verify-email';
} else {
  client.setCustomerToken(auth.token);
  localStorage.setItem('customerToken', auth.token);
  await client.syncCartOnLogin(); // REQUIRED — attaches the guest cart to the account
  window.location.href = '/account';
}
```

Make the birthday a required input on this form only when `capabilities.connection.requireBirthday` is `true` (default `false`; the same flag is on `getStoreInfo().requireBirthday`, and an absent field means `false`). It gates this password register route only: OAuth sign-in and guest checkout never consult it, so they still create customers with no birthday. That flag is enforced on `vc_*` sales-channel registration only. A storefront connected by plain `storeId` has no channel to read it from, so the API does not enforce it there, exactly like `requireEmailVerification`. It never applies to customers who already have an account.

### Login

```typescript
const auth = await client.loginCustomer({ email, password });
// Same requiresVerification check as register!
```

### Forgot Password (/forgot-password) — ALWAYS CREATE THIS PAGE

```typescript
await client.forgotPassword(email);
// Always shows success message (prevents email enumeration)
// Email with reset link sent if account exists
```

### Reset Password (/reset-password) — ALWAYS CREATE THIS PAGE

```typescript
const token = new URLSearchParams(window.location.search).get('token');
await client.resetPassword(token!, newPassword);
// On success: redirect to /login
```

### Verify Email (/verify-email) — ALWAYS CREATE THIS PAGE

Even if verification is currently disabled, the store owner can enable it at any time.

```typescript
const result = await client.verifyEmail(code, token);
if (result.verified) {
  const activeToken = result.token || token; // Use new token if returned
  client.setCustomerToken(activeToken);
  localStorage.setItem('customerToken', activeToken);
  localStorage.removeItem('verificationToken');
  await client.syncCartOnLogin(); // REQUIRED — attaches the guest cart to the account
  window.location.href = '/account';
}

// Resend code
const result = await client.resendVerificationEmail(token);
if (result.token) localStorage.setItem('verificationToken', result.token); // Update token if new one returned
```

### Social Login (OAuth)

```typescript
// Get available providers (returns [] when none configured — buttons just don't render)
const { providers } = await client.getAvailableOAuthProviders();

// Redirect to OAuth provider
const { authorizationUrl } = await client.getOAuthAuthorizeUrl('GOOGLE', {
  redirectUrl: window.location.origin + '/auth/callback', // MUST be full absolute URL
});
window.location.href = authorizationUrl;
```

### OAuth Callback Page (/auth/callback)

```typescript
const params = new URLSearchParams(window.location.search);
if (params.get('oauth_success') === 'true') {
  // Single-use auth_code is exchanged for the JWT via POST — keeps the JWT
  // out of the URL (browser history, CDN logs, Referer header).
  const code = params.get('auth_code');
  if (code) {
    const result = await client.exchangeOAuthCode(code);
    client.setCustomerToken(result.token);
    localStorage.setItem('customerToken', result.token);
    // REQUIRED — setCustomerToken only stores the JWT. Without this the guest
    // cart is never attached to the account, so "first order only" discounts
    // re-apply to returning customers, per-customer usage caps go unenforced,
    // and abandoned-cart recovery cannot identify the shopper.
    await client.syncCartOnLogin();
    // Optional: result.customer, result.isNewCustomer, result.redirectUrl
    window.location.href = result.redirectUrl || '/account';
  }
} else if (params.get('oauth_error')) {
  // Failures land on this SAME page (the redirectUrl you supplied), never on
  // the API host. `oauth_error` is a stable snake_case code — switch on it for
  // localized copy. `error_description` is English developer detail; do not
  // show it to shoppers. The list is open (provider codes pass through), so
  // always handle the default case.
  const code = params.get('oauth_error');
  if (code === 'link_blocked_unverified_password_account') {
    window.location.href = '/verify-email'; // a retry will not help
  } else if (code === 'state_expired' || code === 'state_already_used') {
    window.location.href = '/login?error=expired'; // ask them to start over
  } else {
    window.location.href = '/login?error=oauth'; // access_denied, server_error, ...
  }
}
```

> The legacy redirect format placed the JWT directly in the URL as `?token=`. That format is still emitted for backward compatibility, but it will be removed in the next major release — migrate to `auth_code` + `exchangeOAuthCode()` now.

### Account Page (/account) — uses getMyProfile() and getMyOrders()

```typescript
// ✅ CORRECT — use getMyProfile() and getMyOrders()
const profile = await client.getMyProfile(); // Returns CustomerProfile
const { data: orders } = await client.getMyOrders({ page: 1, limit: 10 }); // Returns PaginatedResponse<Order>

// ❌ WRONG — these methods don't exist!
client.getCustomerProfile();
client.getCustomerOrders();
```

The editable profile fields are `firstName`, `lastName`, `phone`, `acceptsMarketing`, `birthMonth` and `birthDay`. `getMyProfile()` returns every one of them, so seed the form state from the profile you just fetched instead of rendering empty inputs. `birthMonth`/`birthDay` (1-12 / 1-31, no year) are absent until the customer sets them, come back as a pair, and must be written as a pair. See the `loyalty` topic for the full birthday field rules.

`profile.role` is a free-form segment the merchant sets from the dashboard or admin API (e.g. `"wholesale"`, `"vip"`, `"ambassador"`) — read-only from the storefront, never sent by `updateMyProfile()`. Use it to gate custom, per-segment UI:

```typescript
if (profile.role === 'wholesale') {
  // render a wholesale price list / bulk-order UI
}
```

### Order history should show more than just totals

A useful order card includes ALL of the following when the data is present. Each section is conditional — render nothing if the field is empty.

| Section | Source field | Notes |
|---|---|---|
| Header (number, status badge, date, total) | `order.orderNumber`, `order.status`, `order.createdAt`, `order.totalAmount` | Always present. |
| Line items | `order.items[]` | Render image, name, qty, price. |
| **Per-item customizations** | `order.items[i].customizations` | Map of { label, value, type }. Render by `type` — see table below. |
| **Status timeline** | `order.statusHistory` | `OrderStatusChange[]`: `{ status, at, note? }`. Render as a vertical list. |
| **Shipping address** | `order.shippingAddress` | Standard `OrderAddress` shape. |
| **Tracking** | `order.trackingNumber`, `order.trackingUrl`, `order.carrier`, `order.shippedAt`, `order.deliveredAt` | Link out to `trackingUrl` when set. |
| **Payment** | `order.paymentMethod`, `order.financialStatus` | Badge `financialStatus` (paid / pending / refunded / partially_refunded). |
| Downloads | `order.hasDownloads` → `client.getOrderDownloads(id)` | Separate call; returns `OrderDownloadLink[]`. |
| **Order note** | `order.notes` | The shopper's own checkout note, echoed back read-only. Render when present ("Your order note"). |
| Financial summary | `order.subtotal`, `order.appliedDiscounts`, `order.couponCode` + `couponDiscount`, `order.shippingAmount`, `order.taxAmount`, `order.totalAmount` | Breakdown rows + final total. In VAT-inclusive mode `taxAmount` is 0 — read `order.taxBreakdown.totalTax` and label "Tax (incl.)". |

#### Rendering `order.items[i].customizations` by type

The map key is the metafield slug; the value is `{ label, value, type }`. Dispatch by `type`:

| Type | Value | Render |
|---|---|---|
| `TEXT`, `TEXTAREA`, `URL`, `NUMBER`, `SELECT` | string | Plain text (`URL` → anchor). |
| `BOOLEAN` | `"yes"` / `"no"` | ✓ / ✗ |
| `MULTI_SELECT` | `string[]` | Comma-separated. |
| `IMAGE` | asset URL (string) | Thumbnail linking to full-size asset. |
| `GALLERY` | `string[]` of URLs | Grid of thumbnails. |
| `COLOR` | hex string | Swatch + hex text. |
| `DATE` | ISO-8601 | `toLocaleDateString()` |
| `DATETIME` | ISO-8601 | `toLocaleString()` |
| Unknown | any | Plain text (defensive default). |

The storefront scaffolded by `create-brainerce-store` already implements this. See `src/components/account/order-history.tsx` + the sibling `order-customizations.tsx`, `order-status-timeline.tsx`, `order-shipping-block.tsx`, `order-payment-block.tsx` — mirror that structure.

### Do NOT render

These fields are NOT returned to buyers by `/customers/me/orders`. If you see them in older examples, ignore them — they are for merchant/admin views only.

- `order.accountId`, `order.storeId`, `order.customerId` (already known on the request)
- `order.customFieldValues` (order-level checkout fields — merchant concept; buyers see `items[i].customizations`)
- `order.appliedSurcharges`, `order.surchargeAmount`, `order.appliedRuleIds`, `order.downloadMeta`, `order.pickupLocationData`