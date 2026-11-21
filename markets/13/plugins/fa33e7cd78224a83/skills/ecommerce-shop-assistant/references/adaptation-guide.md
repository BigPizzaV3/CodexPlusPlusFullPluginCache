# Adapting This Guide to a Webshop

This guide is intentionally generic. Map the capability names below to the actual tool names the target store exposes, and adjust the notes for each tool. When integrating a concrete shop, read each real tool's parameter documentation and fill in the specifics.

## Capability → typical tool notes

### Search & discovery
- **search** (`keyword`, optional filters, sort, `page`/`pageSize`)
  - Note how each filter combines (AND vs OR). For example, an attribute filter may require ALL given ids while a goal/need filter matches ANY.
- **getBrands (`searchTerm`, `limit`)** and **getCategories** — usually return a flat list (CSV/table).
- **attribute / filter helpers** — load these before searching so you use valid filter ids rather than guessing.

### Product details
- **productDetailsByIds (list of **product** ids)** — usually has a max ids per call (e.g. 3). Returns name, description, format/size, contents, ingredients, warnings.

### Shopping cart
- **getCart** — items with line id, variant id, product id, name, size, price, totals, warnings.
- **addToCart (list of `{ variantId, quantity }`)** — usually a max items per call (e.g. 10).
- **updateCartItemQuantity (cartItemId, quantity)** — `0` typically removes the line.
- **removeCartItem (cartItemId)** or **removeCartItemByProductVariantId (variantId)**.

### Orders
- **listOrders** — optional date range, status list, `limit`.
- **getOrder (orderId)** — itemized details. Verify it is scoped to the current customer.
- **getLatestOrder (paidOnly)**.

### Checkout
- **getPaymentMethods (countryCode)** — return the available methods for the shipping country.
- **checkout (addressId, paymentMethodSystemName, phoneNumber?)**
  - Confirm the address + payment method with the customer first.
  - Some methods require a valid phone number — ask, never fake it.

### Addresses
- **listAddresses** / **getDefaultAddress** — return stored data unchanged (do not localize/translate).
- **upsertNetherlandsAddress** / **upsertBelgiumAddress**:
  - Upsert is a full replacement: `AddressId > 0` updates, `0` creates. Most fields are required.
  - NL: postcode + house number are validated; street/city filled automatically.
  - BE: street and city must be supplied explicitly.
- **deleteAddress** / **setDefaultAddressById**.

### Web pages
- **fetchStorePage (url)** — restrict to the store's own domain.

## Integration checklist

1. List the real tool names for each capability above.
2. Record constraints: max ids/items per call, required parameters, default country code, payment methods that need a phone number.
3. Record which tools are ReadOnly vs Destructive so the agent respects them.
4. Record the product-id vs variant-id convention.
5. Verify checkout guardrails (confirm address + payment method) before enabling automated ordering.