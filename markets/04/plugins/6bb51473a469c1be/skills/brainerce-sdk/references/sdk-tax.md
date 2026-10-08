## Tax Display — Where & How to Show Tax

**Tax is calculated ONLY after shipping address is entered (depends on location).**

| Location | Tax Display | Note |
|----------|-------------|------|
| Product Page | ❌ No | "Price excludes tax" (optional note) |
| Cart Page | ⚠️ "Calculated at checkout" | No address yet |
| Checkout (before address) | ⚠️ "Enter address to calculate" | Waiting for location |
| Checkout (after address) | ✅ **REQUIRED** | `checkout.taxAmount` (0 in VAT mode → `checkout.taxBreakdown.totalTax`) |
| Order Confirmation | ✅ **REQUIRED** | `order.taxAmount` (0 in VAT mode → `order.taxBreakdown.totalTax`) |

### Cart Page — Partial Display

```typescript
const totals = getCartTotals(cart);
<div className="space-y-2 text-sm">
  <div className="flex justify-between"><span>Subtotal</span><span>{formatPrice(totals.subtotal, { currency })}</span></div>
  {totals.discount > 0 && (
    <div className="flex justify-between text-green-600"><span>Discount</span><span>-{formatPrice(totals.discount, { currency })}</span></div>
  )}
  <div className="flex justify-between text-muted-foreground"><span>Shipping</span><span>Calculated at checkout</span></div>
  <div className="flex justify-between text-muted-foreground"><span>Tax</span><span>Calculated at checkout</span></div>
  <div className="flex justify-between font-bold border-t pt-2"><span>Estimated Total</span><span>{formatPrice(totals.total, { currency })}+</span></div>
</div>
```

### Checkout — After Address Entry ✅ REQUIRED

```typescript
{checkout.shippingAddress && (
  <div className="space-y-2">
    <div className="flex justify-between"><span>Subtotal</span><span>{formatPrice(checkout.subtotal, { currency })}</span></div>
    {parseFloat(checkout.discountAmount) > 0 && (
      <div className="flex justify-between text-green-600">
        <span>Discount{checkout.couponCode ? ` (${checkout.couponCode})` : ''}</span>
        <span>-{formatPrice(checkout.discountAmount, { currency })}</span>
      </div>
    )}
    <div className="flex justify-between"><span>Shipping</span><span>{formatPrice(checkout.shippingAmount, { currency })}</span></div>
    <div className="flex justify-between"><span>Tax</span><span>{formatPrice(checkout.taxAmount, { currency })}</span></div>
    {checkout.taxBreakdown?.breakdown?.length > 0 && (
      <div className="text-xs text-muted-foreground pl-4">
        {checkout.taxBreakdown.breakdown.map((tax, i) => (
          <div key={i}>{tax.name}: {formatPrice(tax.amount.toString(), { currency })} ({(tax.rate * 100).toFixed(1)}%)</div>
        ))}
      </div>
    )}
    <div className="flex justify-between text-xl font-bold border-t pt-3"><span>Total</span><span>{formatPrice(checkout.total, { currency })}</span></div>
  </div>
)}
```

### Order Confirmation — Full Display ✅ REQUIRED

```typescript
<div className="space-y-2">
  <div className="flex justify-between"><span>Subtotal</span><span>{formatPrice(order.subtotal, { currency: order.currency })}</span></div>
  {parseFloat(order.discountAmount) > 0 && (
    <div className="flex justify-between text-green-600"><span>Discount</span><span>-{formatPrice(order.discountAmount, { currency: order.currency })}</span></div>
  )}
  <div className="flex justify-between"><span>Shipping</span><span>{formatPrice(order.shippingAmount, { currency: order.currency })}</span></div>
  {/* Inclusive (VAT) stores keep taxAmount="0" — the real VAT is on taxBreakdown.totalTax. */}
  {(() => {
    const tax = parseFloat(order.taxAmount || '0') || order.taxBreakdown?.totalTax || 0;
    if (tax <= 0) return null;
    const incl = order.taxBreakdown?.pricesIncludeTax;
    return <div className="flex justify-between"><span>{incl ? 'Tax (incl.)' : 'Tax'}</span><span>{formatPrice(tax, { currency: order.currency })}</span></div>;
  })()}
  <div className="flex justify-between font-bold text-lg border-t pt-2"><span>Total Paid</span><span>{formatPrice(order.totalAmount, { currency: order.currency })}</span></div>
</div>
```