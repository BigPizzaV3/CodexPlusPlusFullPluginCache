## SDK Setup

```bash
npm install brainerce
```

```typescript
// lib/brainerce.ts — create this file FIRST
import { BrainerceClient } from 'brainerce';

export const client = new BrainerceClient({
  salesChannelId: 'vc_YOUR_CONNECTION_ID',
});

// Cart helpers — save cart ID to localStorage
export function getCartId(): string | null {
  if (typeof window === 'undefined') return null;
  return localStorage.getItem('cartId');
}
export function setCartId(id: string): void { localStorage.setItem('cartId', id); }
export function clearCartId(): void { localStorage.removeItem('cartId'); }

// Customer token helpers — persist auth across page loads
export function setCustomerToken(token: string | null): void {
  if (token) {
    localStorage.setItem('customerToken', token);
    client.setCustomerToken(token);
  } else {
    localStorage.removeItem('customerToken');
    client.clearCustomerToken();
  }
}
export function restoreCustomerToken(): string | null {
  const token = localStorage.getItem('customerToken');
  if (token) client.setCustomerToken(token);
  return token;
}
export function isLoggedIn(): boolean {
  return !!localStorage.getItem('customerToken');
}
```

### Get Store Info (ALWAYS call on app initialization)

```typescript
import type { StoreInfo } from 'brainerce';

const [storeInfo, setStoreInfo] = useState<StoreInfo | null>(null);

useEffect(() => {
  client.getStoreInfo().then(setStoreInfo).catch(console.error);
}, []);
// storeInfo.currency → use for all formatPrice() calls
// storeInfo.name, storeInfo.language, storeInfo.requireEmailVerification
// storeInfo.requireBirthday === true → require birthMonth + birthDay at registration
//   (channel connections only; the field is absent on older backends, and absent means false)
```

### Imports — Types & Helpers

```typescript
import {
  BrainerceClient,
  // Types
  type Product, type ProductVariant, type Cart, type CartItem,
  type Checkout, type CheckoutLineItem, type Order, type OrderItem,
  type CustomerProfile, type CustomerAddress, type ShippingRate,
  type PaymentProvider, type PaymentIntent, type PaymentStatus,
  type SearchSuggestions, type ProductSuggestion, type CategorySuggestion,
  type OAuthAuthorizeResponse, type CustomerOAuthProvider,
  type ReservationInfo, type StoreInfo,
  type DiscountBanner, type ProductDiscountBadge, type CartNudge,
  type ProductRecommendation, type ProductRecommendationsResponse, type CartRecommendationsResponse,
  // Helpers (USE THESE!)
  formatPrice, getCartTotals, getProductPrice, getProductPriceInfo,
  getVariantPrice, getVariantOptions, getStockStatus,
  getCartItemName, getCartItemImage,
  getDescriptionContent, isHtmlDescription,
  getProductMetafieldValue, getProductCustomizationFields,
} from 'brainerce';
```

### Available features — request each topic for full docs

| Topic | What it covers |
|-------|----------------|
| `products` | Catalog listing, search, PDP, variants, swatches, stock, attributes |
| `cart` | Guest + logged-in cart, add/remove/update, reservations |
| `checkout` | Guest + customer checkout, shipping, address |
| `payment` | Payment providers, intents, status polling, confirmation |
| `auth` | Customer sign-up, login, OAuth, email verification |
| `discounts` | Coupons, banners, nudges |
| `recommendations` | Cross-sell / upsell grids |
| `reviews` | Product reviews, ratings & customer photos |
| `inventory` | Stock badges, reservation countdown |
| `inquiries` | Contact / custom forms |
| `i18n` | Multi-language, RTL |
| `admin` | Server-to-server admin API (products, orders, customers) |
| `storefront-bot` | **AI chat widget** — add Brainerce's AI shopping assistant to any page with one script tag or `BrainerceBot.mount()`. Answers product questions, shows recommendation cards, handles cart adds, opens escalation form. |
| `content` | Blog, articles, static pages |