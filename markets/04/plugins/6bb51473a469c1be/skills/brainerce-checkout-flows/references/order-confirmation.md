## Order Confirmation Page (/order-confirmation) — REQUIRED!

**MUST use `waitForOrder()` to poll for order creation!**

```typescript
function OrderConfirmation() {
  const [status, setStatus] = useState<'loading' | 'success' | 'error'>('loading');
  const [orderNumber, setOrderNumber] = useState<string | null>(null);

  useEffect(() => {
    // Break out of iframe if redirected from Grow payment page
    if (window.top !== window.self) { window.top!.location.href = window.location.href; return; }

    const checkoutId = new URLSearchParams(window.location.search).get('checkout_id');
    if (!checkoutId) { setStatus('error'); return; }

    // Step 1: Clear purchased items from cart
    client.handlePaymentSuccess(checkoutId);

    // Step 2: Poll for order creation (created automatically by webhook)
    client.waitForOrder(checkoutId, { maxWaitMs: 60000 })
      .then((result) => {
        if (result.success) setOrderNumber(result.status.orderNumber || null);
        setStatus(result.status.status === 'failed' ? 'error' : 'success');
      })
      .catch(() => setStatus('success')); // Network error — still show success
  }, []);

  if (status === 'loading') return <div>Confirming your order...</div>;
  if (status === 'error') return <div>Payment issue. Please contact support.</div>;

  return (
    <div>
      <h1>Thank you for your order!</h1>
      {orderNumber && <p>Order #{orderNumber}</p>}
      <p>You will receive a confirmation email shortly.</p>
    </div>
  );
}
```

**Common mistake:** Don't just check URL params and show success immediately!
You MUST call `waitForOrder(checkoutId)` to verify the order was created.
Also call `handlePaymentSuccess(checkoutId)` to clear purchased items from the cart.

### Optional: render full order details on the confirmation page

Want a richer thank-you page (items, shipping address, totals, the shopper's
order note)? After `waitForOrder` succeeds, fetch the full buyer-safe order —
works for guests too (possession of the checkout id is the credential):

```typescript
const order = await client.getOrderByCheckout(checkoutId);
// order.items, order.shippingAddress, order.notes, order.subtotal,
// order.shippingAmount, order.taxAmount / order.taxBreakdown, order.totalAmount
```

Render whatever subset fits your design — same field shapes as the buyer
order-history view (see "Buyer order view" section).