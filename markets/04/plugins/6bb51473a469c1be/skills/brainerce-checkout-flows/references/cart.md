## Cart (Smart Methods — Guest & Logged-in)

### Smart Cart Methods (RECOMMENDED)

```typescript
const cart = await client.smartGetCart();  // Returns CartWithIncludes (extends Cart)
await client.smartAddToCart({
  productId: product.id,
  variantId: selectedVariant?.id,
  quantity: 1,
  name: product.name,                              // REQUIRED for guest display
  price: getVariantPrice(selectedVariant, product.basePrice), // REQUIRED for guest display
  image: product.images?.[0]?.url,                  // REQUIRED for guest display
});
await client.smartUpdateCartItem(productId, quantity, variantId?);
await client.smartRemoveFromCart(productId, variantId?);
```

### ⚠️ LocalCart vs Server Cart — Key Differences

- Server `Cart` has: `id`, `itemCount`, `subtotal`, `discountAmount`, `reservation`
- Guest `LocalCart` has NONE of these! Only: `items`, `couponCode`, `customer`
- To check type: `if ('id' in cart) { /* server Cart */ } else { /* LocalCart */ }`
- Item count for both: `cart.items.length`
- `getCartTotals()` only works with server `Cart`, NOT `LocalCart`
- `cart.reservation` only exists on server `Cart` and `Checkout` — NOT on `LocalCart`
- For LocalCart totals: `cart.items.reduce((sum, item) => sum + parseFloat(item.price || '0') * item.quantity, 0)`

### Partial Checkout (AliExpress Style) — REQUIRED

Cart page MUST have checkboxes to select items for checkout:

```typescript
const [selectedIndices, setSelectedIndices] = useState<number[]>(
  cart.items.map((_, i) => i) // All selected by default
);

// Checkbox for each item
<input type="checkbox" checked={selectedIndices.includes(index)} onChange={() => toggleItem(index)} />

// "Select All" checkbox
<input type="checkbox" checked={selectedIndices.length === cart.items.length} onChange={toggleAll} />

// On checkout — pass selected items
const result = await client.startGuestCheckout({ selectedIndices });
// Only selected items will be in checkout, others stay in cart!
```

### Cart Total (Use SDK Helper!)

```typescript
// ✅ CORRECT — use getCartTotals helper (server Cart only!)
const { subtotal, discount, shipping, total } = getCartTotals(cart, shippingRate?.price);

// ❌ WRONG — cart.total doesn't exist!
const total = cart.total;
```

### Coupons

**On the cart page** (before checkout is created):
```typescript
// Apply coupon — returns updated Cart with discountAmount
const updatedCart = await client.applyCoupon(cartId, 'SAVE20');
console.log(updatedCart.discountAmount); // "10.00"
console.log(updatedCart.couponCode);     // "SAVE20"

// Remove coupon
await client.removeCoupon(cartId);

// Calculate totals including discount
const totals = getCartTotals(cart); // { subtotal, discount, shipping, total }
```

> **Region-restricted coupons:** a coupon may carry `regionIds`. If the buyer's checkout region isn't in that list, `applyCoupon` / `applyCheckoutCoupon` reject the code even when everything else matches. Empty/omitted `regionIds` = valid in all regions.

**On the checkout page** (after checkout session exists — ALWAYS use this when checkoutId is available):
```typescript
// Applies to cart AND updates checkout totals in one call
const checkout = await client.applyCheckoutCoupon(checkoutId, 'SAVE20');
console.log(checkout.discountAmount); // "10.00"
console.log(checkout.total);          // correctly updated total

// Remove coupon from checkout
await client.removeCheckoutCoupon(checkoutId);
```

> ⚠️ **Critical:** if a checkout session already exists, ALWAYS use `applyCheckoutCoupon(checkoutId, code)`. Using `applyCoupon(cartId, code)` after checkout creation does NOT update the checkout total — payment will charge the original amount. Show `checkout.discountAmount` and `checkout.couponCode` in the order summary.

### ⚠️ Checkout Order Summary — Use checkout.lineItems, NOT cart.items!

```typescript
// ❌ WRONG — shows ALL cart items (not just selected ones!)
{cart.items.map(item => <div>{item.product.name}</div>)}

// ✅ CORRECT — shows only items in this checkout
{checkout.lineItems.map(item => <div>{item.product.name}</div>)}
```