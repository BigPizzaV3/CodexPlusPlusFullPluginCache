## Inventory, Stock Display & Reservation Countdown

### Stock Status

```typescript
// ✅ CORRECT — use SDK helper
const status = getStockStatus(product.inventory);
// Returns: "In Stock", "Out of Stock", or "Unavailable"
// With low stock: getStockStatus(product.inventory, { lowStockThreshold: 5 })
// Returns: "Low Stock" if available <= 5

const inStock = product.inventory?.inStock ?? true;
const canAddToCart = product.inventory?.canPurchase ?? false;

// Sold out is not the end of the page — offer a back-in-stock alert, but ONLY
// when nothing else can be done about it. See the `stock-alerts` topic.
const canOfferAlert =
  storeInfo.stockAlertsEnabled !== false &&
  product.inventory?.trackingMode === 'TRACKED' &&
  !canAddToCart &&
  (product.inventory?.backorderMode ?? 'NONE') === 'NONE';

// ❌ WRONG — quantity doesn't exist!
const inStock = product.inventory?.quantity > 0;
```

### StockBadge Component (include on ProductCard & ProductDetail)

```typescript
function StockBadge({ product }: { product: Product }) {
  const inv = product.inventory;
  if (!inv || !inv.inStock) return null;
  if (inv.trackingMode === 'TRACKED' && inv.available > 0 && inv.available <= 5) {
    return <span className="text-orange-600 text-sm font-medium">Only {inv.available} left!</span>;
  }
  return null;
}
```

### ReservationCountdown Component (ALWAYS include in Cart & Checkout pages)

The cart/checkout response includes a `reservation` field when reservations are active.
**Always build this component** — it only renders when `reservation.hasReservation` is true.

```typescript
import type { ReservationInfo } from 'brainerce';

function ReservationCountdown({ reservation }: { reservation?: ReservationInfo }) {
  const [remaining, setRemaining] = useState(reservation?.remainingSeconds || 0);

  useEffect(() => {
    if (!reservation?.hasReservation) return;
    setRemaining(reservation.remainingSeconds || 0);
  }, [reservation]);

  useEffect(() => {
    if (remaining <= 0) return;
    const timer = setInterval(() => setRemaining(r => Math.max(0, r - 1)), 1000);
    return () => clearInterval(timer);
  }, [remaining]);

  if (!reservation?.hasReservation || remaining <= 0) return null;

  const minutes = Math.floor(remaining / 60);
  const seconds = remaining % 60;
  const timeDisplay = `${minutes}:${seconds.toString().padStart(2, '0')}`;
  const message = reservation.countdownMessage
    ? reservation.countdownMessage.replace('{time}', timeDisplay)
    : `Items reserved for ${timeDisplay}`;

  return (
    <div className="bg-amber-50 border border-amber-200 rounded-lg p-3 text-amber-800">
      ⏱️ {message}
    </div>
  );
}

// Usage (only server Cart and Checkout have reservation — LocalCart does NOT):
// Guard: check 'id' in cart before accessing reservation
{'id' in cart && <ReservationCountdown reservation={cart.reservation} />}

// Extend reservation when customer is active
const { success, reservation } = await client.extendReservation({ cartId });

// Release reservation on abandon
await client.releaseReservation({ cartId });

// Real-time availability (considers other customers' reservations)
const availability = await client.getAvailability(['prod_123', 'prod_456']);
// item.available, item.lowStock, item.canPurchase
```