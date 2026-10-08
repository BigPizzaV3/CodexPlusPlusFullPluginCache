// ---- Products ----

interface Product {
  id: string;
  name: string;
  slug?: string | null;
  description?: string | null;
  descriptionFormat?: 'text' | 'html' | 'markdown' | null;
  sku: string;
  gtin?: string | null;  // Global Trade Item Number (EAN/UPC/ISBN) — emitted in Product JSON-LD.
  mpn?: string | null;   // Manufacturer Part Number — emitted in Product JSON-LD.
  basePrice: string;   // For VARIABLE products: MIN(variants.price). For SIMPLE: the parent price. parseFloat() for math.
  salePrice?: string | null;  // For VARIABLE: MIN(variants.salePrice WHERE NOT NULL) — null iff no variant is on sale (WC is_on_sale() semantic). For SIMPLE: the parent sale price. Reliable "on sale?" check: product.salePrice !== null.
  salePriceStartsAt?: string | null;  // ISO 8601 — sale-price effective window start.
  salePriceEndsAt?: string | null;    // ISO 8601 — sale-price window end. Feeds buildProductJsonLd's priceValidUntil.
  costPrice?: string | null;
  priceMin?: string | null;  // Lowest variant price (VARIABLE products) — same as basePrice for VARIABLE, kept for back-compat and JSON-LD range display.
  priceMax?: string | null;  // Highest variant price (VARIABLE products). Use with priceMin for "₪49 – ₪199" range.
  priceVaries?: boolean;     // true when variant prices differ — show "₪49 – ₪199" range.
  // FX DISPLAY overlay (PRD §23). Set only when getProducts({ regionId }) was called AND region.currency !== store.currency. basePrice/salePrice above stay in store currency — these are additive. For presentment-enabled regions (Stripe) the displayPrice uses the same buffered rate the checkout charges (browsed == checkout); for display-only regions it is mid-market and the buyer is charged in store currency at checkout (payment provider handles customer-side FX).
  displayPrice?: string;        // basePrice × daily FX rate, in displayCurrency.
  displaySalePrice?: string;    // salePrice × rate (if salePrice present).
  displayPriceMin?: string;     // priceMin × rate (VARIABLE products).
  displayPriceMax?: string;     // priceMax × rate (VARIABLE products).
  displayCurrency?: string;     // ISO 4217 of the region — e.g. "EUR".
  status: string;
  type: 'SIMPLE' | 'VARIABLE';
  isDownloadable?: boolean;
  downloads?: DownloadFile[] | null;
  images?: ProductImage[];
  inventory?: InventoryInfo | null;
  variants?: ProductVariant[];
  categories?: Array<{ id: string; name: string; slug?: string | null }>;  // NOT string[]! Use slug to link to /category/{slug}.
  brands?: Array<{ id: string; name: string }>;
  tags?: string[];
  metafields?: ProductMetafield[];
  customizationFields?: ProductCustomizationField[];  // Buyer input fields — render on PDP, send values in cart metadata. Account-wide fields (MetafieldDefinition.appliesToAllProducts=true) are folded in here automatically; no client-side merging.
  productAttributeOptions?: Array<{
    id: string;
    attributeId: string;
    attributeOptionId: string;
    platform: string;
    attribute: { id: string; name: string; displayType?: 'DEFAULT' | 'COLOR_SWATCH' | 'IMAGE_SWATCH' | 'MIXED_SWATCH' } | null;
    attributeOption: { id: string; name: string; value?: string | null; swatchColor?: string | null; swatchColor2?: string | null; swatchImageUrl?: string | null } | null;
  }>;
  createdAt: string;
  updatedAt: string;
}

// Use getProductSwatches(product) to get grouped swatch data for storefront rendering.
// Returns Array<{ attributeName, displayType, options: Array<{ name, swatchColor?, swatchColor2?, swatchImageUrl? }> }>
// displayType rendering: COLOR_SWATCH → color circle (swatchColor/swatchColor2); IMAGE_SWATCH → image thumbnail (swatchImageUrl);
// MIXED_SWATCH → per-option: render swatchImageUrl if set, else swatchColor if set, else text only.

interface ProductImage {
  url: string;
  position?: number;
  isMain?: boolean;
  alt?: string;
}

interface ProductVariant {
  id: string;
  productId: string;
  sku?: string | null;
  name?: string | null;
  price?: string | null;
  salePrice?: string | null;
  // FX DISPLAY overlay (PRD §23) — same semantics as on the parent Product.
  displayPrice?: string;
  displaySalePrice?: string;
  displayCurrency?: string;
  attributes?: Record<string, string> | null;
  options?: Array<{ name: string; value: string }>;
  inventory?: InventoryInfo | null;
  image?: string | { url: string; thumbnailUrl?: string } | null;
  position: number;
  status?: string | null;
  createdAt: string;
  updatedAt: string;
}

interface InventoryInfo {
  total: number;
  reserved: number;
  available: number;
  trackingMode: 'TRACKED' | 'UNLIMITED' | 'DISABLED';
  inStock: boolean;       // USE THIS for stock checks
  canPurchase: boolean;   // USE THIS for add-to-cart button
  // TRACKED items only. 'NONE' = a shopper can do nothing but wait, which is
  // where a back-in-stock alert belongs. 'ALLOW'/'NOTIFY' = the storefront can
  // still sell it out of stock, so an alert there tells someone to come back and
  // do what they can already do — the API silently discards those requests.
  // Absent on older backends; treat undefined as 'NONE'.
  backorderMode?: 'NONE' | 'ALLOW' | 'NOTIFY';
}

interface ProductMetafield {
  id: string;
  definitionId: string;
  definitionKey: string;
  definitionName: string;
  type: string;
  value: string;
  variantId?: string | null;
}

// Metafield type enum — used by ProductCustomizationField.type
type MetafieldType =
  | 'TEXT' | 'TEXTAREA' | 'NUMBER' | 'BOOLEAN' | 'DATE' | 'DATETIME'
  | 'URL' | 'COLOR' | 'DIMENSION' | 'WEIGHT' | 'JSON'
  | 'IMAGE' | 'GALLERY'
  | 'SELECT' | 'MULTI_SELECT';

// Customer-facing input assigned per product. Render on the PDP in the order of `position`.
// Submit values keyed by `key` inside AddToCartDto.metadata.
// Upload files via `uploadCustomizationFile()` first, then place the returned `url` in metadata.
interface ProductCustomizationField {
  definitionId: string;
  name: string;                 // Label to show buyers
  key: string;                  // Use as metadata key in AddToCartDto.metadata
  description?: string | null;  // Help text
  type: MetafieldType;
  required: boolean;
  minLength?: number | null;    // TEXT/TEXTAREA char bounds; MULTI_SELECT array bounds
  maxLength?: number | null;
  minValue?: number | null;     // NUMBER bounds
  maxValue?: number | null;
  dateAvailability?: DateAvailabilityConstraints | null;  // DATE/DATETIME: blocked weekdays/dates, min/max date, leadTimeMinutes/cutoffTime/maxDaysAhead, (DATETIME only) business hours + slots — feed into isCalendarDateAllowed()/getBusinessHoursForDate()/computeAvailableSlots()/isDateValueAllowed(), passing { timezone } as the last argument or the relative bounds are skipped.
                                                          // Submit DATE as "YYYY-MM-DD", DATETIME as one ISO-8601 value ("2026-08-13T13:00" = store-local). A slot label glued on ("...T13:00-14:00") is a 400.
  enumValues?: CustomizationFieldOption[];  // REQUIRED for SELECT / MULTI_SELECT
  defaultValue?: string | null;
  position: number;             // Render order
}

interface DateAvailabilityConstraints {
  minDate?: string;              // "YYYY-MM-DD", inclusive
  maxDate?: string;              // "YYYY-MM-DD", inclusive
  blockedWeekdays?: number[];    // 0=Sun..6=Sat
  blockedDates?: string[];       // specific "YYYY-MM-DD" (holidays etc.)
  businessHours?: Array<{ weekday: number; open: string; close: string }>;  // "HH:mm", DATETIME only
  slotDurationMinutes?: number;  // splits businessHours into discrete slots, DATETIME only
}

interface CustomizationFieldOption {
  label: string;          // Display label (e.g., "Rose Gold")
  value: string;          // Value stored in CartItem.metadata
  swatchColor?: string | null;      // Optional hex color (e.g., "#B76E79")
  swatchImageUrl?: string | null;   // Optional swatch image URL
}

// Facet value counts — returned by getMetafieldFilters() (vibe-coded +
// storefront modes). One entry per definition the merchant marked
// filterable=true (SELECT/MULTI_SELECT/BOOLEAN). `count` = DISTINCT active
// products for that value; MULTI_SELECT stored arrays split per element;
// BOOLEAN buckets are 'true'/'false'; zero-count enumValues entries included.
// Pair `key` with getProducts({ metafields: { [key]: [value] } }).
interface MetafieldFilter {
  id: string;
  key: string;
  name: string;                 // Localized per request locale
  type: MetafieldType;
  enumValues: CustomizationFieldOption[];
  values: Array<{ value: string; count: number }>;
}
// getMetafieldFilters(params?: { locale?: string }): Promise<{ filters: MetafieldFilter[] }>

interface ProductQueryParams {
  page?: number;
  limit?: number;
  search?: string;
  status?: 'active' | 'draft';
  categories?: string | string[];
  brands?: string | string[];
  tags?: string | string[];    // Tag IDs (from getTags()) — NOT tag names
  minPrice?: number;
  maxPrice?: number;
  // Filter by custom-field (metafield) values. Keys = definition.key,
  // values = accepted values. Only definitions with filterable=true and
  // type SELECT/MULTI_SELECT/BOOLEAN are honored. AND across keys, OR within.
  metafields?: Record<string, string | string[]>;
  sortBy?: 'name' | 'price' | 'createdAt';
  sortOrder?: 'asc' | 'desc';
  // PRD §22: resolve DISPLAY prices for this region. When set + valid, each
  // product/variant gains resolvedPrice/resolvedCurrency/priceSource (additive;
  // basePrice/salePrice untouched). Absent/invalid region → nothing attached.
  // Display-only. Ignored in vibe-coded (vc_*) mode (storefront/admin paths only).
  regionId?: string;
}

interface SearchSuggestions {
  products: ProductSuggestion[];
  categories: CategorySuggestion[];
}

interface ProductSuggestion {
  id: string;
  name: string;
  slug: string | null;  // Can be null! Use id as React key
  image: string | null;
  price: string;
  basePrice: string;
  salePrice?: string | null;
  type: 'SIMPLE' | 'VARIABLE';
}

interface CategorySuggestion {
  id: string;
  name: string;
  productCount: number;
}

// getCategoryBySlug(slug) — category (collection) landing-page payload.
// Products come from getProducts({ categories: [id] }); this is metadata only.
interface CategoryDetail {
  id: string;
  name: string;
  slug: string | null;
  description: string | null;      // long-form HTML — render below the grid
  metaDescription: string | null;  // <meta name="description">
  image: string | null;
  breadcrumb: Array<{ name: string; slug: string | null }>; // root → parent
  productCount: number;
}

interface DownloadFile {
  id: string;
  name: string;
  size?: number;
  mimeType?: string;
}

// ---- Cart ----

interface Cart {
  id: string;
  sessionToken?: string | null;
  customerId?: string | null;
  status: 'ACTIVE' | 'MERGED' | 'CONVERTED' | 'ABANDONED';
  currency: string;
  notes?: string | null;
  subtotal: string;           // Use parseFloat()
  discountAmount: string;     // Use parseFloat()
  couponCode?: string | null;
  ruleDiscountAmount?: string;
  appliedDiscounts?: CartAppliedDiscount[];
  nudges?: CartNudge[];
  items: CartItem[];
  itemCount: number;
  reservation?: ReservationInfo;
  createdAt: string;
  updatedAt: string;
}

interface CartItem {
  id: string;
  productId: string;
  variantId?: string | null;
  quantity: number;
  unitPrice: string;          // Use parseFloat()
  discountAmount: string;
  product: {                  // NESTED — use item.product.name
    id: string;
    name: string;
    sku: string;
    images?: ProductImage[];
  };
  variant?: {
    id: string;
    name?: string | null;
    sku?: string | null;
    image?: ProductImage | string | null;
  } | null;
  metadata?: Record<string, unknown> | null;  // Buyer-submitted customization values, keyed by ProductCustomizationField.key
  customizations?: Record<string, { label: string; value: string | string[]; type: string }>;  // Resolved labels — use this to display "Color: Silver" without extra getProduct() call
  createdAt: string;
  updatedAt: string;
}

// Guest cart stored in localStorage
interface LocalCart {
  items: LocalCartItem[];
  couponCode?: string;
  customer?: {
    email: string;
    firstName?: string;
    lastName?: string;
    phone?: string;
  };
  shippingAddress?: {
    firstName: string;
    lastName: string;
    line1: string;
    line2?: string;
    city: string;
    region?: string;
    postalCode: string;
    country: string;
    phone?: string;
  };
}

interface LocalCartItem {
  productId: string;
  variantId?: string;
  quantity: number;
  name?: string;
  price?: string;
  image?: string;
  addedAt: string;
}

interface AddToCartDto {
  productId: string;
  variantId?: string;
  quantity: number;
  notes?: string;
  productInfo?: { name: string; price: string; image?: string; };
}

// ---- Checkout ----

type CheckoutStatus = 'PENDING' | 'SHIPPING_SET' | 'PAYMENT_PENDING' | 'PAYMENT_PROCESSING' | 'COMPLETED' | 'FAILED' | 'EXPIRED';

interface Checkout {
  id: string;
  status: CheckoutStatus;
  email?: string | null;
  customerId?: string | null;
  regionId?: string | null;  // multi-region: recorded for reporting + provider scoping. FX-at-checkout: presentment-enabled regions (Stripe) charge in the region currency — see the presentment field below; else charged in store base currency
  shippingAddress?: CheckoutAddress | null;
  billingAddress?: CheckoutAddress | null;
  shippingRateId?: string | null;
  shippingMethod?: ShippingRate | null;
  currency: string;
  subtotal: string;
  discountAmount: string;
  shippingAmount: string;
  taxAmount: string;
  taxBreakdown?: TaxBreakdown | null;
  total: string;
  surchargeAmount: string;
  appliedSurcharges?: Array<{ key: string; name: string; value: unknown; amount: string }> | null;
  customFieldValues?: Record<string, unknown> | null;
  couponCode?: string | null;
  notes?: string | null;  // Order-level shopper note — copied onto the order at completion
  lineItems: CheckoutLineItem[];  // Use THIS for order summary, NOT cart.items!
  itemCount: number;
  availableShippingRates?: ShippingRate[];
  reservation?: ReservationInfo;
  // FX-at-checkout: present ONLY when the region charges in its own currency (presentment-enabled — Stripe today). The amounts the buyer is actually CHARGED, in presentment.currency; presentment.total equals the payment intent amount. Render these (not total/currency above) when present. Absent = charged in store base currency. The fields above stay the base reference.
  presentment?: {
    currency: string;        // ISO-4217 charged currency, e.g. "EUR"
    subtotal: string;
    discountAmount: string;
    shippingAmount: string;
    taxAmount: string;
    surchargeAmount: string;
    total: string;           // equals the charged amount, to the cent
    fxChargingRate: string;  // base→presentment rate (buffer included)
    fxBufferPercent: string | null;
  };
  createdAt: string;
  updatedAt: string;
}

interface CheckoutLineItem {
  id: string;
  productId: string;
  variantId?: string | null;
  quantity: number;
  unitPrice: string;
  discountAmount: string;
  product: { id: string; name: string; sku: string; images?: ProductImage[]; };
  variant?: { id: string; name?: string | null; sku?: string | null; image?: ProductImage | string | null; } | null;
  metadata?: Record<string, unknown> | null;  // Copied from CartItem.metadata — buyer customization values
  customizations?: Record<string, { label: string; value: string | string[]; type: string }>;  // Resolved labels — same shape as OrderItem.customizations
}

interface CheckoutAddress {
  firstName: string;
  lastName: string;
  company?: string | null;
  line1: string;
  line2?: string | null;
  city: string;
  region?: string | null;
  postalCode: string;
  country: string;
  phone?: string | null;
}

interface ShippingRate {
  id: string;
  name: string;
  description?: string | null;
  price: string;
  currency: string;
  estimatedDays?: number | null;  // number, NOT string!
  source?: 'manual' | 'carrier';
  carrier?: string;   // carrier rates only, e.g. 'USPS'
  service?: string;   // carrier rates only, e.g. 'Priority'
  // Live carrier rates only. RENDER THIS AND estimatedDays, NOT name — 'name'
  // is the carrier's own service code ('USPS PriorityMailInternational') and
  // means nothing to a shopper. Manual zone rates carry no speedTier: show
  // their 'name' exactly as the merchant wrote it.
  speedTier?: 'cheapest' | 'balanced' | 'fastest';
}

interface SetShippingAddressDto {
  email: string;      // REQUIRED!
  firstName: string;
  lastName: string;
  company?: string;
  line1: string;
  line2?: string;
  city: string;
  region?: string;    // NOT "state"!
  postalCode: string;
  country: string;
  phone?: string;
  notes?: string;     // Order notes textarea — include one on checkout by default! Max 2000 chars, lands on the order
  // Pass BOTH whenever the address came from getAddressSuggestions/getAddressDetails.
  // The server re-resolves placeId to exact coordinates and matches map-drawn
  // ("polygon") delivery zones against them. Omit it and it must geocode the typed
  // text instead — a same-named street in a neighbouring city can win, quoting the
  // wrong area's rate or no delivery at all.
  placeId?: string;
  placeSessionToken?: string;  // same token used for those autocomplete calls; optional (24h server cache)
  // NOTE: there is deliberately no lat/lng field. Zone matching decides which
  // shipping rate is charged, so coordinates are never accepted from the client
  // — the server resolves them from placeId itself. The endpoint rejects ANY
  // unknown property with 400 "property lat should not exist", which blocks
  // checkout outright; the SDK (>=1.53.0) strips lat/lng/formattedAddress for
  // you, so spreading getAddressDetails().address here is safe. Over raw HTTP
  // it is not — build the body from the fields above.
}

// getAddressSuggestions(query, sessionToken, near?) result item — Places (New) predictions.
// getAddressDetails(placeId, sessionToken, options?) resolves ONE suggestion to this shape.
// sessionToken: client-generated id (crypto.randomUUID()), reused across every
// keystroke of one address-entry attempt, then passed once more to getAddressDetails —
// that pairing bills the whole attempt as ONE call, not per-keystroke.
interface AddressSuggestion {
  placeId: string;
  description: string;  // human-readable prediction text for the dropdown
}

interface AddressDetailsResult {
  address: {
    line1: string; city: string; region: string; postalCode: string;
    // country AND region can be EMPTY STRINGS. Google omits the country
    // outright for places whose sovereignty it declines to attribute — which
    // includes ordinary residential addresses (Ramat Shlomo, Giv'at Ze'ev,
    // Modi'in Ilit, Ma'ale Adumim all resolve with no country). That is a
    // normal response; the API never guesses one. Prompt the shopper to
    // confirm the country instead of submitting '' — the rest of the address
    // is valid. It also makes inZone read false against country-listed zones,
    // though a map-drawn (polygon) zone can still match — the server matches it
    // against the coordinates it resolves from placeId.
    country: string;
    // lat/lng/formattedAddress are for YOUR UI only (map pin, distance). They
    // are not part of any address payload; pass placeId instead. The SDK strips
    // them from setShippingAddress/setBillingAddress bodies, so a spread is safe.
    lat: number; lng: number; formattedAddress: string;
  };
  // false = outside the store's shipping zones — SOFT signal, show a banner,
  // never block checkout. Resolved against the same region the checkout would
  // resolve (destination country, then any regionId you pass, then the store
  // default), so it does not contradict the rates fetched afterwards.
  inZone: boolean;
}

interface CreateCheckoutDto {
  cartId: string;
  customerId?: string;
  selectedItemIds?: string[];  // Partial checkout
  regionId?: string;           // multi-region: associate the checkout with a region (must belong to the store; 400 if unknown)
}

// startGuestCheckout() return type — DISCRIMINATED UNION
type GuestCheckoutStartResponse =
  | { tracked: true; checkoutId: string; cartId: string; message: string; }
  | { tracked: false; message: string; };

interface TaxBreakdown {
  subtotal: number;
  totalTax: number;
  total: number;
  breakdown: TaxBreakdownItem[];
}

interface TaxBreakdownItem {
  name: string;
  rate: number;    // decimal: 0.17 = 17%
  amount: number;
  taxClassId?: string | null;   // rate's tax class (null = Standard)
  taxClassSlug?: string | null; // class slug for attribution (null = Standard)
}

// ---- Orders ----

type OrderStatus = 'pending' | 'processing' | 'shipped' | 'delivered' | 'cancelled' | 'refunded';

interface Order {
  id: string;
  externalId?: string;
  orderNumber?: string;
  status: OrderStatus;
  totalAmount: string;   // ALWAYS use this, not .total
  total?: string;        // optional alias
  currency?: string;
  taxAmount?: string | null;       // 0 in inclusive (VAT) mode — read taxBreakdown.totalTax
  taxBreakdown?: TaxBreakdown | null;  // carries the included VAT when prices include tax
  customer?: OrderCustomer | null;
  items: OrderItem[];
  itemCount?: number;
  shippingAddress?: OrderAddress;
  billingAddress?: OrderAddress;
  hasDownloads?: boolean;
  createdAt: string;

  // Payment + fulfillment
  paymentMethod?: string | null;
  financialStatus?: string | null;       // "pending" | "authorized" | "partially_paid" | "paid" | "partially_refunded" | "refunded" | "voided"
  fulfillmentStatus?: string | null;     // "unfulfilled" | "partial" | "fulfilled"

  // Tracking
  trackingNumber?: string | null;
  trackingUrl?: string | null;
  carrier?: string | null;
  shippedAt?: string | null;             // ISO-8601
  deliveredAt?: string | null;           // ISO-8601

  // What the shopper paid for at checkout — ADMIN reads only (getOrder /
  // getOrders); null when no live carrier rate was sold (flat-rate/zone).
  shippingSelection?: {
    carrier: string | null;              // e.g. "USPS"
    service: string | null;              // e.g. "Priority"
    methodName: string | null;           // label the shopper saw
    amount: string | null;               // in the order's currency
  } | null;

  // Timeline of status transitions, chronological
  statusHistory?: OrderStatusChange[] | null;
}

interface OrderStatusChange {
  status: OrderStatus;
  at: string;                            // ISO-8601
  note?: string | null;
}

// ⚠️ OrderItem is FLAT — unlike CartItem which is NESTED
interface OrderItem {
  productId: string;
  variantId?: string;
  sku?: string;
  name?: string;         // FLAT: item.name (NOT item.product.name!)
  quantity: number;
  price: string;         // FLAT: item.price (NOT item.unitPrice!)
  unitPrice?: string;    // alias
  totalPrice?: string;
  image?: string;        // FLAT: item.image (NOT nested)
  // Snapshot of buyer-submitted customization values captured at checkout.
  // Keyed by metafield slug. `value` is string[] for MULTI_SELECT / GALLERY, string otherwise.
  customizations?: Record<string, { label: string; value: string | string[]; type: string }>;
  taxClassSlug?: string; // frozen slug of the line's resolved tax class (omitted = Standard fallback)
}

interface OrderCustomer {
  email: string;
  name?: string;
  phone?: string;
}

interface OrderAddress {
  firstName?: string;
  lastName?: string;
  line1: string;
  line2?: string;
  city: string;
  state?: string;
  region?: string;
  postalCode: string;
  country: string;
  phone?: string;
}

interface OrderDownloadLink {
  productName: string;
  fileName: string;
  downloadUrl: string;
  downloadsUsed: number;
  downloadLimit: number | null;
  expiresAt: string | null;
}

// ---- Customers ----

interface CustomerProfile {
  id: string;
  email: string;
  firstName?: string;
  lastName?: string;
  phone?: string;
  emailVerified: boolean;
  acceptsMarketing: boolean;
  birthMonth?: number;  // 1-12. RETURNED as well as accepted, so pre-fill the profile form from it. Absent until the customer sets one.
  birthDay?: number;    // 1-31, and the day must exist in the month (Feb 29 valid, Feb 30 rejected). Returned with birthMonth or not at all, and always written as a pair.
  role?: string; // free-form merchant-set segment (e.g. "wholesale", "vip") — read-only, use to gate custom storefront features
  addresses: CustomerAddress[];
  createdAt: string;
  updatedAt: string;
}

interface CustomerAddress {
  id: string;
  label?: string;
  firstName: string;
  lastName: string;
  company?: string;
  line1: string;
  line2?: string;
  city: string;
  region?: string;     // NOT "state"!
  postalCode: string;
  country: string;
  phone?: string;
  isDefault: boolean;
  createdAt: string;
  updatedAt: string;
}

interface CustomerAuthResponse {
  customer: {
    id: string;
    email: string;
    firstName?: string;
    lastName?: string;
    phone?: string;
    emailVerified: boolean;
  };
  token: string;
  expiresAt: string;
  requiresVerification?: boolean;  // If true → redirect to /verify-email
}

interface EmailVerificationResponse {
  verified: boolean;
  message: string;
  token?: string;
  expiresAt?: string;
}

type CustomerOAuthProvider = 'GOOGLE' | 'FACEBOOK' | 'GITHUB';

interface OAuthAuthorizeResponse {
  authorizationUrl: string;
  state: string;
  provider: CustomerOAuthProvider;
}

interface OAuthProvidersResponse {
  providers: CustomerOAuthProvider[];  // returns [] when none configured
}

interface OAuthCallbackResponse {   // returned by exchangeOAuthCode(authCode)
  token: string;
  expiresAt: string;
  customer: Customer;
  isNewCustomer: boolean;
  linkedToExisting: boolean;
  provider: CustomerOAuthProvider;
  redirectUrl?: string;
}

// Values of the ?oauth_error= param on a failed social sign-in. The callback
// redirects to your redirectUrl on failure too, carrying oauth_error (this
// stable code) plus error_description (English developer detail, NOT shopper
// copy). Switch on the code to render localized copy. The list is OPEN — the
// provider's own codes pass through — so always handle the default case.
type OAuthErrorCode =
  | 'invalid_request'
  | 'invalid_state'
  | 'state_already_used'
  | 'state_expired'
  | 'provider_unsupported'
  | 'provider_error'
  | 'access_denied'                              // shopper declined consent
  | 'provider_disabled'
  | 'provider_already_linked'
  | 'oauth_account_linked_to_another_customer'
  | 'link_blocked_unverified_password_account'   // send to email verification, not a retry
  | 'store_not_found'
  | 'server_error'
  | (string & {});

interface RegisterCustomerDto {
  email: string;
  password: string;
  firstName?: string;
  lastName?: string;
  phone?: string;
  birthMonth?: number;  // 1-12, no year. Send with birthDay or not at all.
  birthDay?: number;    // 1-31. Feb 29 is accepted (celebrated Feb 28 in non-leap years).
  referralCode?: string;
}

// UpdateMyProfileDto: the same birthday pair is editable later.
//   client.updateMyProfile({ firstName, lastName, phone, acceptsMarketing, birthMonth, birthDay })
// Required at registration only when capabilities.connection.requireBirthday
// (or storeInfo.requireBirthday, where an absent field means false) is true.
// Default false. That flag is enforced on vc_* sales-channel PASSWORD
// registration only. A storeId-connected storefront has no channel to read it
// from, and OAuth sign-in and guest checkout create the customer on other
// routes that never consult it, so customers keep arriving with no birthday.
// It never applies to existing accounts.

// getCheckoutPrefillData() returns CheckoutPrefillData; its inline customer
// object carries the same birthday pair:
//   { id, email, firstName?, lastName?, phone?, emailVerified, birthMonth?, birthDay? }

// ---- Payments ----

interface PaymentProviderConfig {
  id: string;
  provider: string;           // 'stripe' | 'grow' | 'paypal'
  name: string;
  publicKey: string;
  stripeAccountId?: string;   // Stripe Connect only
  supportedMethods: string[];
  testMode: boolean;
  isDefault: boolean;         // only a primary (CREDIT_CARD) is ever the default
  methodType: 'CREDIT_CARD' | 'WALLET' | 'OFFSITE' | 'LOCAL' | 'REDEEMABLE';
  presentation: 'card_form' | 'express_button' | 'redirect' | 'local_option' | 'redeemable_field';
  isAdditive: boolean;        // wallet/alt method shown ALONGSIDE the primary (e.g. PayPal)
}
type PaymentProvider = PaymentProviderConfig;

interface PaymentProvidersConfig {
  hasPayments: boolean;
  providers: PaymentProviderConfig[];
  defaultProvider?: PaymentProviderConfig;
}

interface PaymentIntent {
  id: string;
  clientSecret: string;  // Stripe: pi_xxx_secret_xxx, Grow: payment URL, PayPal: order ID
  amount: string;
  currency: string;
  status: string;
  provider?: string;     // 'stripe' | 'grow' | 'paypal'
}

interface PaymentStatus {
  checkoutId: string;
  status: 'pending' | 'processing' | 'succeeded' | 'failed' | 'canceled';
  orderId?: string;
  orderNumber?: string;
  error?: string;
}

// ---- Saved Payment Methods (vaulted cards) ----
// Display-only summary of a customer's vaulted payment method. The
// underlying provider token is encrypted at rest in the platform DB
// and NEVER returned through the SDK.
//
// To opt into vaulting at checkout, pass saveCard: true to
// createPaymentIntent (only honored for logged-in customers).
//
// To list / remove saved methods, see:
//   client.listSavedPaymentMethods(storeId, customerId)
//   client.removeSavedPaymentMethod(storeId, customerId, methodId)

interface SavedPaymentMethodSummary {
  id: string;
  customerId: string;
  appInstallationId: string;
  paymentMethod: string;          // 'credit_card' | 'paypal' | 'bank_account'
  brand: string | null;
  last4: string | null;
  expMonth: number | null;
  expYear: number | null;
  isDefault: boolean;
  status: string;                 // 'active' | 'expired' | 'invalid'
  failureReason: string | null;
  lastUsedAt: string | null;
  expiresAt: string | null;
  createdAt: string;
  updatedAt: string;
}

interface WaitForOrderResult {
  success: boolean;
  status: PaymentStatus;   // Access: result.status.orderNumber
  attempts: number;
  waitedMs: number;
}

// ---- Helper Functions (import from 'brainerce') ----

// Price helpers
function formatPrice(priceString: string | number | undefined | null, options?: { currency?: string; locale?: string; }): string;
function getProductPrice(product: Pick<Product, 'basePrice' | 'salePrice'>): number;
function getProductPriceInfo(product: Pick<Product, 'basePrice' | 'salePrice' | 'discount' | 'priceMin' | 'priceVaries'>): {
  price: number; originalPrice: number; isOnSale: boolean; discountAmount: number; discountPercent: number;
}; // For VARIABLE products, basePrice/salePrice are pre-aggregated (MIN of variants) — the helper just reads them. Use this whenever you need an "on sale?" badge or a "X% off" label.
function getVariantPrice(variant: Pick<ProductVariant, 'price' | 'salePrice'>, productBasePrice: string): number;

// Cart helpers
function getCartTotals(cart: Pick<Cart, 'subtotal' | 'discountAmount'>, shippingPrice?: string | number): {
  subtotal: number; discount: number; shipping: number; total: number;
};
function getCartItemName(item: CartItem): string; // "Blue T-Shirt - Large" — product name plus variant name. The variant suffix is omitted when the product has no variant, or when the variant name duplicates the product name. Need the parts separately (e.g. variant on its own line)? Read item.product.name and item.variant?.name.
function getCartItemImage(item: CartItem): string | undefined;

// Product helpers
function getVariantOptions(variant: Pick<ProductVariant, 'attributes'>): Array<{ name: string; value: string }>;
function getStockStatus(inventory: InventoryInfo | null, options?: { lowStockThreshold?: number }): string;
function getDescriptionContent(product: Pick<Product, 'description' | 'descriptionFormat'>): { html: string } | { text: string } | null;
function isHtmlDescription(product: Pick<Product, 'description' | 'descriptionFormat'>): boolean;
function getProductMetafieldValue(product: Pick<Product, 'metafields'>, key: string): string | number | boolean | null;

// Common types
interface StoreInfo {
  id: string;
  name: string;
  currency: string;
  language: string;
  connectionId?: string;
  requireEmailVerification?: boolean;
  // Merchant toggle: make the birthday (birthMonth + birthDay) mandatory at
  // registration. Sales channel (vc_*) connections only, and enforced only on
  // the channel password register route, so a storeId-mode storefront never
  // receives this field and never enforces it, and OAuth sign-in and guest
  // checkout never consult it. Optional on purpose: absent means false
  // (rolling deploys serve /info without it for a while), so read it as
  // storeInfo.requireBirthday === true.
  requireBirthday?: boolean;
  // SEO surface. indexNowKey: serve verbatim at GET /indexnow-key.txt
  // (text/plain); 404 while null. Not a secret. googleSiteVerification:
  // render as <meta name="google-site-verification" content={token}> in the
  // root layout head when set (Search Console + Merchant Center claim).
  seo?: { indexNowKey: string | null; googleSiteVerification?: string | null };
  // Real merchant-configured flat-rate/free shipping zones. Feeds
  // buildProductJsonLd's shippingDetails — omitted entirely when not passed,
  // never fabricated. Weight/price-tiered rates are excluded (cost depends
  // on cart contents, no single number to declare).
  shipping?: ShippingSummaryEntry[];
  // Marketing tag ids, resolved from the marketplace apps the merchant already
  // connected — never ask the merchant for one, never read one from an env
  // var. Pass the whole object to client.initTracking(). Absent fields mean
  // that app isn't connected, which is a normal state.
  tracking?: StoreTracking;
}

interface StoreTracking {
  ga4MeasurementId?: string;  // G-XXXXXXX — auto-filled by the Google & YouTube app.
  gtmContainerId?: string;    // GTM-XXXXXX — the only tag with no discovery path; merchant-set.
  metaPixelId?: string;       // Auto-filled by the Meta Commerce app.
  tiktokPixelId?: string;     // Auto-filled by the TikTok app.
}

// One e-commerce event, fanned out to every loaded tag by
// client.trackMarketingEvent(name, payload).
type TrackingEventName =
  | 'view_item' | 'view_item_list' | 'add_to_cart' | 'remove_from_cart' | 'view_cart'
  | 'begin_checkout' | 'add_payment_info' | 'purchase' | 'search' | 'sign_up';

interface TrackingEventPayload {
  currency?: string;
  value?: number;
  transactionId?: string;  // purchase only → GA4 transaction_id / Meta eventID / TikTok event_id (de-dupes a refresh).
  shipping?: number;
  tax?: number;
  coupon?: string;
  items?: TrackingEventItem[];
}

interface TrackingEventItem {
  itemId: string;  // MUST be the SKU — the id the Google/Meta catalog feeds publish. Anything else breaks attribution silently.
  itemName?: string;
  price?: number;  // Unit price; GA4 multiplies by quantity itself.
  quantity?: number;
  itemVariant?: string;
  itemCategory?: string;
}

interface ShippingSummaryEntry {
  countries: string[];  // ISO 3166-1 alpha-2 codes this rate applies to.
  rateType: 'FLAT_RATE' | 'FREE';
  amount: number | null;  // In the store's currency. 0 for FREE, null if a FLAT_RATE has no configured amount.
  minDeliveryDays: number | null;
  maxDeliveryDays: number | null;
  handlingTime: number | null;  // Order-processing days before it ships.
}

// SEO helpers (JSON-LD builders + sitemap)
interface JsonLdOptions { siteUrl: string; path?: string; }
function buildArticleJsonLd(post: BlogPost, opts: JsonLdOptions & { organizationName?: string }): Record<string, unknown>;
// itemCondition always included (NewCondition — first-party new-goods catalog). priceValidUntil included when
// product.salePrice + product.salePriceEndsAt are both set. shippingDetails included when the shipping opt is
// passed (storeInfo.shipping) — never fabricated, omitted entirely otherwise.
function buildProductJsonLd(product: Product, opts: JsonLdOptions & { currency: string; brandName?: string; shipping?: ShippingSummaryEntry[] }): Record<string, unknown>;
function buildOrganizationJsonLd(store: StoreInfo, opts: JsonLdOptions): Record<string, unknown>;
function buildWebsiteJsonLd(store: StoreInfo, opts: JsonLdOptions & { searchUrlTemplate: string }): Record<string, unknown>;
function buildCollectionPageJsonLd(category: CategoryDetail, opts: JsonLdOptions): Record<string, unknown>;
function buildBreadcrumbJsonLd(items: Array<{ name: string; url: string }>): Record<string, unknown>;
function jsonLdScriptProps(data: Record<string, unknown>): { type: 'application/ld+json'; dangerouslySetInnerHTML: { __html: string } };

interface SitemapEntry {
  url: string;
  lastModified?: Date;
  changeFrequency?: 'always' | 'hourly' | 'daily' | 'weekly' | 'monthly' | 'yearly' | 'never';
  priority?: number;
}
function getBlogSitemapEntries(client: BrainerceClient, opts: {
  siteUrl: string; basePath?: string; locales?: string[]; defaultLocale?: string;
  pageSize?: number; maxEntries?: number;
}): Promise<SitemapEntry[]>;
// REQUIRED for the products section of sitemap.xml. The listing API clamps
// limit to 100, so getProducts({ limit: 1000 }) silently truncates a sitemap;
// this helper uses a dedicated lightweight endpoint (slug + updatedAt +
// localeSlugs, up to 5000 in one call) and falls back to pagination.
function getProductSitemapEntries(client: BrainerceClient, opts: {
  siteUrl: string; basePath?: string; locales?: string[]; defaultLocale?: string;
  pageSize?: number; maxEntries?: number;
}): Promise<SitemapEntry[]>;
function getCategorySitemapEntries(client: BrainerceClient, opts: {
  siteUrl: string; basePath?: string; locales?: string[]; defaultLocale?: string;
}): Promise<SitemapEntry[]>;
// REQUIRED in the not-found path of product/blog pages: the platform records
// every slug rename; on a hit, permanentRedirect() to currentSlug instead of
// 404ing. Returns null when no rename was recorded; never throws.
// client.resolveSlugRedirect('product' | 'blog', slug)
// → Promise<{ currentSlug: string } | null>;

interface PaginatedResponse<T> {
  data: T[];
  meta: { page: number; limit: number; total: number; totalPages: number; };
}

interface ReservationInfo {
  hasReservation: boolean;
  remainingSeconds: number;
  countdownMessage?: string;
}

// Discount types
interface DiscountBanner { /* from getDiscountBanners() */ }
interface ProductDiscountBadge {
  badgeText: string;
  originalPrice: string;
  discountedPrice: string;
}
interface CartNudge {
  text: string;
  type: string;
}
interface CartAppliedDiscount {
  ruleName: string;
  type: string;
  discountAmount: string;
  description?: string;
}

// Recommendation types
interface RecommendationVariant {
  id: string; name?: string; price?: string; salePrice?: string;
  attributes?: Record<string, string>; image?: ProductImage | string; inventory?: InventoryInfo;
}
interface ProductRecommendation {
  id: string; name: string; slug: string;
  // For a VARIABLE target, basePrice is the pinned variant's price (when
  // targetVariantId is set) or the "from {min variant}" range — never 0.
  basePrice: string; salePrice?: string;
  images: ProductImage[]; type: 'SIMPLE' | 'VARIABLE'; inventory?: InventoryInfo;
  relationType: string;
  // Variant context (VARIABLE targets):
  targetVariantId?: string | null;        // merchant-pinned variant, or null
  requiresVariantSelection?: boolean;      // true → customer must pick from variants
  pinnedVariant?: { id: string; name?: string; attributes?: Record<string, string> } | null;
  variants?: RecommendationVariant[];      // present when requiresVariantSelection
}
interface ProductRecommendationsResponse {
  crossSells: ProductRecommendation[];
  upsells: ProductRecommendation[];
  related: ProductRecommendation[];
}
interface CartRecommendationsResponse {
  recommendations: ProductRecommendation[];
}

// Cart include types (for consolidated getCart requests)
type CartIncludeOption = 'recommendations' | 'upgrades' | 'bundles';
interface CartIncludeOptions {
  include?: CartIncludeOption[];
}
interface CartWithIncludes extends Cart {
  recommendations?: { recommendations: ProductRecommendation[] };
  upgrades?: { upgrades: Record<string, CartUpgradeSuggestion> };
  bundles?: { bundles: CartBundleOffer[] };
}
interface CartUpgradeSuggestion {
  targetProduct: ProductRecommendation;
  priceDelta: string;
  deltaPercent: number;
}
interface CartBundleOfferOfferedProduct {
  id: string;
  name: string;
  slug: string | null;
  basePrice: string;
  salePrice: string | null;
  images: Array<{ url: string }>;
  type: string;
  // Variant context (VARIABLE offered products):
  variantId?: string | null;               // merchant-pinned variant for this slot
  requiresVariantSelection?: boolean;       // true → customer must pick from variants
  pinnedVariant?: { id: string; name?: string; attributes?: Record<string, string> } | null;
  variants?: RecommendationVariant[];       // present when requiresVariantSelection
  // originalPrice = pinned/cheapest variant price for VARIABLE (not a 0 parent base).
  originalPrice: string;
  discountedPrice: string;
}
interface CartBundleOffer {
  id: string;
  name: string;
  description: string | null;
  // productIds[0] = trigger product (must be in cart for the bundle to surface);
  // productIds[1..] = offered together at the bundle discount.
  triggerProductId: string;
  productIds: string[];
  // offeredProducts = productIds[1..] minus those already in cart, each with
  // its own original/discounted price applied.
  offeredProducts: CartBundleOfferOfferedProduct[];
  discountType: 'PERCENTAGE' | 'FIXED_AMOUNT';
  discountValue: string;
  totalOriginalPrice: string;
  totalDiscountedPrice: string;
}

// ---- Contact Inquiries & Forms ----

// Two shapes — legacy and flexible. The two may be mixed; `fields` wins on key collision.
interface CreateInquiryInput {
  // Legacy shape (still supported forever, backed by default "main" form)
  name?: string;                                // max 120 chars (if provided)
  email?: string;                               // must be valid email if provided
  subject?: string;                             // max 200 chars
  message?: string;                             // max 10000 chars
  phone?: string;

  // Flexible shape
  formKey?: string;                             // defaults to "main"; merchant-defined keys e.g. "newsletter"
  fields?: Record<string, unknown>;             // bag of values keyed by field key (built-in or custom)
  locale?: string;                              // e.g. "en", "he" — stored on the inquiry
  sourceMetadata?: Record<string, unknown>;     // arbitrary context (e.g. { page: '/contact', campaign: 'fall-2026' })

  // Shared
  customerId?: string;                          // link to logged-in customer
  metadata?: Record<string, unknown>;           // deprecated alias of sourceMetadata
}

interface CreateInquiryResponse {
  id: string;
  status: 'NEW';
  createdAt: string;                            // ISO datetime
}

// ---- Form schema (for dynamic rendering) ----

type ContactFormFieldType =
  | 'TEXT' | 'TEXTAREA' | 'EMAIL' | 'PHONE' | 'NUMBER'
  | 'SELECT' | 'MULTI_SELECT' | 'CHECKBOX' | 'URL' | 'DATE';

interface ContactFormFieldValidation {
  minLength?: number;
  maxLength?: number;
  min?: number;
  max?: number;
  pattern?: string;                             // regex string
  patternMessage?: string;
}

interface ContactFormPublicField {
  key: string;                                  // stable identifier, e.g. "email", "company"
  type: ContactFormFieldType;
  label: string;                                // already localized for the requested locale
  placeholder?: string;                         // already localized
  helpText?: string;                            // already localized
  isRequired: boolean;
  enumValues?: { value: string; label: string }[]; // present (non-empty) for SELECT / MULTI_SELECT
  validation?: ContactFormFieldValidation;
  defaultValue?: string;
  width?: 'FULL' | 'HALF' | 'THIRD';           // layout hint — FULL = full row, HALF = half row, THIRD = one-third row
}

interface ContactFormPublic {
  id: string;
  key: string;                                  // e.g. "main", "newsletter"
  name: string;                                 // already localized — use as form heading
  description?: string;                         // already localized — use as subtitle
  submitButton: string;                         // already localized — use as submit label
  successMessage: string;                       // already localized — render after submit succeeds
  fields: ContactFormPublicField[];             // in display order; hidden fields already filtered out
}

interface ContactFormSummary {
  key: string;
  name: string;
  isDefault: boolean;
}

// Field-type → HTML mapping for dynamic rendering
// ------------------------------------------------------------------
//   TEXT          → <input type="text" ... pattern?={validation.pattern}>
//   TEXTAREA      → <textarea rows={6} ...>
//   EMAIL         → <input type="email" autoComplete="email" ...>
//   PHONE         → <input type="tel" autoComplete="tel" ...>
//   NUMBER        → <input type="number" min={validation.min} max={validation.max}>
//   URL           → <input type="url" ...>
//   DATE          → <input type="date" ...>  (value is ISO yyyy-MM-dd)
//   SELECT        → <select>{enumValues.map(...)}</select>  — always rendered from enumValues
//   MULTI_SELECT  → multiple <input type="checkbox">, value is string[]
//   CHECKBOX      → single <input type="checkbox">, value is boolean
// ------------------------------------------------------------------
//
// Layout: render fields inside a CSS grid container.
//   width='FULL'  (default) → span entire row
//   width='HALF'            → span half the row (two HALF fields sit side-by-side)
//   width='THIRD'           → span one-third of the row (three THIRD fields sit side-by-side)
// Use a 6-column grid for clean divisibility:
//   FULL  → col-span-6 | HALF → col-span-3 | THIRD → col-span-2
// Stack to full width on small screens (< sm breakpoint).
//
// Required fields: show a red asterisk (*) next to the label, validate
// client-side before submission, and display inline error messages for
// any empty required field. Do NOT rely only on the server returning 400.
// ------------------------------------------------------------------

// SDK methods
//   await brainerce.createInquiry(input)              → POST /stores/{storeId}/inquiries
//   await brainerce.contactForms.list()               → GET  /stores/{storeId}/contact-forms
//   await brainerce.contactForms.get(key?, locale?)   → GET  /stores/{storeId}/contact-forms/{key}?locale={locale}
//
// Rules
// - Rate limit: 3 submissions / 60s per IP — handle 429 responses gracefully
// - Honeypot: always render an invisible field named `honeypot` and never send it
// - Always pass `locale` — inbox filters inquiries by language, and schema labels come back translated
// - Render `schema.name` / `description` / `submitButton` / `successMessage` directly — do NOT hardcode copy
// - Unknown field keys are stripped server-side — safe to send extras during dev
//
// A form keyed "newsletter" is STILL an inquiry: it files a message and never
// touches marketing consent, so the address can never receive a campaign. For a
// mailing list use marketing.subscribe() — see MARKETING_SIGNUP_TYPES.

// ---- Newsletter / marketing signup ----
// The email-capture popup, the footer subscribe bar, the exit-intent modal.

interface SubscribeMarketingInput {
  email: string;                                // lowercased + trimmed server-side
  firstName?: string;                           // greets them in the confirmation email
  lastName?: string;
  locale?: string;                              // language of the confirmation email, e.g. "he"
  source?: string;                              // free-form: "popup" | "footer" | "exit-intent"
  sourceMetadata?: Record<string, unknown>;     // referrer, UTM params, the page it fired on
  honeypot?: string;                            // hidden field — must be empty
}

interface SubscribeMarketingResponse {
  ok: true;                                     // identical for EVERY outcome — see below
}

// SDK method
//   await brainerce.marketing.subscribe(input)  → POST /stores/{storeId}/marketing/subscribe
//                                               → POST /vc/{connectionId}/marketing/subscribe
//
// ⛔ IT DOES NOT SUBSCRIBE ANYONE. It creates the contact and mails them a
// confirmation link; the address is unmailable, and invisible to every campaign
// audience, until the recipient clicks it. Render "Check your email to confirm"
// on success — NEVER "You're subscribed". Single opt-in is not available.
//
// ⛔ THE RESPONSE HAS NO INFORMATION IN IT. `{ ok: true }` is returned for a
// brand-new address, one that confirmed months ago, one inside its 24h resend
// cooldown, and one suppressed after a hard bounce — otherwise the form becomes
// a way to test who shops at this store. There is no branch to write.
//
// Rules
// - Rate limit: 3 requests / 60s per IP — handle 429 gracefully
// - Resend cooldown: 1 confirmation email per address per store per 24h, silent
// - Honeypot: render hidden, pass it through; non-empty rejects the request
// - Pass `locale` on a multi-language storefront or it falls back to the store
//   language. "he" and "en" are written; anything else gets English.
// - No discount code is minted. For "10% off your first order", the merchant
//   creates a coupon with the `customer_first_order` condition and you show
//   that fixed code after a successful call.
// - Lands in Dashboard → Customers with "Accepts marketing" OFF; it flips on at
//   confirmation. The contact is an ordinary guest customer row (no password).

// ---- Back-in-stock alerts ----
// The "email me when this is back" button on a sold-out product.

interface CreateStockAlertInput {
  email: string;                                // lowercased + trimmed server-side
  productId: string;
  variantId?: string;                           // REQUIRED in practice on any product with variants
  locale?: string;                              // language of the alert email, e.g. "he"
  honeypot?: string;                            // hidden field — must be empty
}

interface StockAlertResponse {
  ok: true;                                     // identical for EVERY outcome — see below
}

// SDK method
//   await brainerce.stockAlerts.subscribe(input) → POST /stores/{storeId}/stock-alerts
//                                                → POST /vc/{connectionId}/stock-alerts
//
// ⛔ IT IS NOT A SUBSCRIPTION. One email, about one item, with a link that stops
// it. No customer account, no marketing consent. Label the button "Email me when
// it's back", NEVER "Subscribe" — and never hide it from someone who unsubscribed
// from marketing, because this grants no consent to hide behind.
//
// ⛔ RENDER IT ONLY when ALL FOUR hold. "inv" is the SELECTED VARIANT's
// inventory when there is one, else the product's:
//   store.stockAlertsEnabled !== false        // merchant's switch, from getStoreInfo()
//   && inv?.trackingMode === 'TRACKED'         // UNLIMITED never runs out, DISABLED is not for sale
//   && !inv.canPurchase                        // it is actually sold out
//   && (inv.backorderMode ?? 'NONE') === 'NONE' // backorderable = already buyable
// Every other case is ignored server-side, so a button in the wrong place looks
// like it worked and does nothing. The merchant can switch the feature off at
// any time and StoreInfo.stockAlertsEnabled is the only way you learn about it.
//
// ⛔ PASS variantId on every variable product, or the alert waits on the product
// as a whole and a shopper who wanted the medium is mailed when the small returns.
//
// ⛔ THE RESPONSE HAS NO INFORMATION IN IT. `{ ok: true }` is returned for a new
// request, a duplicate, an unknown product id, an item already in stock, and a
// suppressed address — otherwise it becomes a way to read the store's stock
// levels. There is no branch to write.
//
// Rules
// - Rate limit: 5 requests / 60s per IP — handle 429 gracefully
// - At most 25 open alerts per address per store; over the cap it silently records nothing
// - A duplicate request is a no-op, not a second alert
// - An unfired alert expires after 90 days
// - Honeypot: render hidden, pass it through; non-empty rejects the request
// - Pass `locale` on a multi-language storefront or it falls back to the store
//   language. "he" and "en" are written; anything else gets English.
// - Delivery is NOT immediate and NOT to everyone at once: stock must hold for a
//   few minutes, then alerts go out in waves sized to the units that returned,
//   oldest request first. Never promise "you'll be the first to know".
// - No SMS, no price-drop alerts, no merchant-editable template.

// ---- Product Reviews ----

interface ProductReviewImage {
  id: string;
  url: string;
  thumbnailUrl: string | null;
  width: number | null;              // set these on the <img> to avoid layout shift
  height: number | null;
  position: number;
}

interface ProductReviewImageAdmin extends ProductReviewImage {
  assetKey: string;
  approvedAt: string | null;         // null = awaiting the merchant (approval stores only)
  hiddenAt: string | null;           // non-null = merchant took it down
  createdAt: string;
}

interface ProductReview {
  id: string;
  productId: string;
  authorName: string;                // max 100 chars
  rating: number;                    // integer 1-5
  body: string | null;               // plain text, max 5000 chars
  verifiedPurchase: boolean;         // derived server-side from DELIVERED orders
  hiddenAt?: string | null;          // ISO datetime; admin responses only — null = visible
  createdAt: string;                 // ISO datetime
  images: ProductReviewImage[];      // ALWAYS an array; only shopper-visible photos
}

interface ProductReviewAdmin extends Omit<ProductReview, 'images'> {
  customerId: string | null;
  authorEmail: string | null;
  orderId: string | null;
  updatedAt: string;
  images: ProductReviewImageAdmin[]; // ALL photos — pending and hidden included
}

interface WriteProductReviewInput {
  rating: number;                    // 1-5
  body?: string;                     // optional, max 5000 chars
  // Keys from uploadReviewPhoto() — NEVER urls. On update this REPLACES the photo
  // set; omitting the field leaves existing photos alone, [] removes them all.
  imageKeys?: string[];              // max 5
}

interface ReviewPhotoUpload {
  key: string;                       // this is what goes in imageKeys
  url: string;                       // local preview only — do not send it back
  width: number | null;
  height: number | null;
}

interface MyProductReview {
  eligible: boolean;
  // Machine-readable reason when not eligible. null when eligible=true.
  reason: 'no_eligible_order' | 'reviews_disabled' | 'product_not_found' | null;
  myReview: ProductReview | null;
  // The store's live photo policy. Read it instead of hard-coding limits.
  photos: {
    enabled: boolean;
    maxPerReview: number;
    maxBytes: number;
    requiresApproval: boolean;       // true = photos wait for the merchant
  };
  // The customer's OWN photos INCLUDING pending ones, so they can see their
  // upload queued rather than concluding it failed. myReview.images has only
  // the publicly visible subset.
  myImages: ProductReviewImageAdmin[];
}

// Each Product carries denormalized review stats:
//   product.avgRating: number       // 0 when reviewCount is 0
//   product.reviewCount: number     // count of visible (hiddenAt IS NULL) reviews


// ---- Modifier Groups (Restaurant / Build-Your-Own) ----
// Modifier groups are merchant-defined option blocks attached to a product
// (toppings, sauce, bread type, …). They differ from product.customizationFields:
// modifier groups are STRUCTURED priced choices validated server-side, while
// customizationFields are arbitrary buyer input (text/photo/color).
//
// Money fields are decimal STRINGS on the wire — "5.00", "-2.00" (downsell).
// Never JSON Number. Use parseFloat() only at display time. Do not compute
// the line total client-side; the server runs free-allocation and returns
// cart.items[i].unitPrice + .modifiers[] + .modifiersTotal.

export type ModifierSelectionType = 'SINGLE' | 'MULTIPLE';

export type FreeAllocationPolicy = 'EXPENSIVE_FREE' | 'CHEAPEST_FREE' | 'SELECTION_ORDER';

export interface Modifier {
  id: string;
  name: string;
  description?: string;
  /** Decimal string. Negative values = downsell modifiers ("-2.00"). */
  priceDelta: string;
  sku?: string;
  image?: { url: string; thumbnailUrl?: string; alt?: string };
  position: number;
  /** Pre-checked on first render. */
  isDefault: boolean;
  /** false = sold out — disable in UI with a "Sold out" badge. */
  available: boolean;
  /** When true, never applied as a free selection — always charges priceDelta even when freeQuantity > 0 on the group. */
  excludeFromFree?: boolean;
  /** Nested combo: opens a sub-flow; depth ≤ 3 enforced server-side. */
  referencedProductId?: string;
  translations?: Record<string, { name?: string; description?: string }>;
}

export interface ModifierGroup {
  id: string;
  /**
   * Set when fetched in a product context (the ProductModifierGroup row id).
   * Use this to update or detach the attachment without reattaching the group.
   */
  attachmentId?: string;
  /** Customer-facing canonical name. */
  name: string;
  /**
   * Admin-only disambiguator — NEVER present in storefront responses.
   * If your client code reads this, you're hitting an admin endpoint by mistake.
   */
  internalName?: string;
  description?: string;
  selectionType: ModifierSelectionType;
  /** Effective minimum after any per-attach / per-variant overrides. */
  min: number;
  /** Effective maximum; null = unlimited. **0 = group hidden for this variant** (PRD §7.2.2). */
  max?: number | null;
  freeQuantity: number;
  required: boolean;
  freeAllocationPolicy: FreeAllocationPolicy;
  modifiers: Modifier[];
  /** Effective default selections (after attachment-level overrides). */
  defaultModifierIds: string[];
  translations?: Record<string, { name?: string; description?: string }>;
}

/** Customer-side selection payload — modifierIds in click-order. */
export interface ModifierSelection {
  modifierGroupId: string;
  modifierIds: string[];
}

/** Per-line modifier breakdown surfaced on cart.items[i] / order.items[i]. */
export interface CartItemModifierLine {
  modifierId: string;
  /** Snapshot of the modifier's name at the time the line was added. */
  name: string;
  /** Decimal string snapshot of the priceDelta at the time the line was added. */
  priceDelta: string;
  /** True if this modifier consumed one of the group's free slots. */
  freeApplied: boolean;
}

/**
 * Stable error codes returned in the structured 400 envelope when a cart
 * payload fails server-side validation. The SDK exposes the envelope on
 * BrainerceError.details — switch on details.code === 'MODIFIER_VALIDATION_FAILED'
 * first, then iterate details.details.errors[]. (BrainerceError.details is the
 * whole response body; the body has its own details block — hence the two
 * hops. Over raw HTTP it is just body.details.errors[].)
 */
export type ModifierValidationCode =
  | 'REQUIRED_GROUP_MISSING'
  | 'MIN_SELECTIONS_NOT_MET'
  | 'MAX_SELECTIONS_EXCEEDED'
  | 'SINGLE_GROUP_MULTIPLE_PICKS'
  | 'UNKNOWN_MODIFIER'
  | 'UNKNOWN_GROUP'
  | 'MODIFIER_DISABLED_FOR_VARIANT'
  | 'MODIFIER_NOT_AVAILABLE'
  | 'NESTED_DEPTH_EXCEEDED'
  | 'NESTED_REQUIRES_PRODUCT_REF'
  | 'INVALID_PRICE_DELTA'
  | 'MODIFIER_PRICE_FLOOR_VIOLATED';

export interface ModifierValidationError {
  code: ModifierValidationCode;
  message: string;
  modifierGroupId?: string;
  modifierId?: string;
}

// Cart DTOs gain optional selections + nestedByModifierId — see CART_TYPES above.
// Add to cart with selections:
//
//   await client.smartAddToCart({
//     productId,
//     variantId,
//     quantity: 1,
//     selections: [
//       { modifierGroupId: 'mg_bread',    modifierIds: ['m_thick'] },
//       { modifierGroupId: 'mg_toppings', modifierIds: ['m_olive', 'm_bacon'] },
//     ],
//   });
//
// The cart line then carries:
//   cart.items[i].modifiers      — CartItemModifierLine[]
//   cart.items[i].modifiersTotal — decimal string of the paid (non-free) deltas

// ---- Content (typed merchant content store) ----
// Brainerce ships a typed content store so merchants can edit FAQ, footer,
// header, announcements, rich text, and static pages in the dashboard
// without re-prompting the AI that built the storefront. Every row has a
// 'type' + 'key' + typed 'data' payload + free-form 'customFields'.
//
// SECURITY (read carefully):
//   RICH_TEXT.html, PAGE.html, and FAQ answers are MERCHANT-AUTHORED HTML.
//   ALWAYS sanitize with isomorphic-dompurify (or equivalent) before
//   injecting via dangerouslySetInnerHTML. The server does NOT pre-sanitize
//   because some merchants embed iframes (e.g. YouTube) which strict
//   sanitizers would strip; the storefront chooses the policy.
//
// 404 contract: client.content.<type>.get(key) returns null when no
// PUBLISHED row exists. Always render a hard-coded fallback on null so
// the page never crashes when the merchant hasn't seeded yet.
//
// Default key: every type has 'main' as its universal default. Pass no
// argument to fetch the main entry; pass a custom key ('shipping',
// 'holiday-2026', 'about') for topical entries.

export type ContentType = 'FAQ' | 'FOOTER' | 'HEADER' | 'ANNOUNCEMENT' | 'RICH_TEXT' | 'PAGE';
export type ContentStatus = 'DRAFT' | 'PUBLISHED';

export interface FaqItem {
  question: string;
  /** Sanitized HTML — sanitize before rendering. */
  answer: string;
}
export interface FaqContent { items: FaqItem[] }

export interface FooterLink { label: string; url: string }
export interface FooterColumn { title: string; links: FooterLink[] }
export interface FooterSocialLink { platform: string; url: string } // 'instagram' | 'facebook' | 'x' | ...
export interface FooterContent {
  columns: FooterColumn[];
  copyright?: string;
  social?: FooterSocialLink[];
}

export interface HeaderLogo { src: string; alt: string }
export interface HeaderNavItem { label: string; url: string }
export interface HeaderCta { label: string; url: string }
export interface HeaderContent {
  logo?: HeaderLogo;
  navItems: HeaderNavItem[];
  cta?: HeaderCta;
}

export type AnnouncementSeverity = 'info' | 'warning' | 'success';
export interface AnnouncementContent {
  message: string;
  severity: AnnouncementSeverity;
  dismissible: boolean;
  /** ISO 8601 — filter client-side. */
  startsAt?: string;
  endsAt?: string;
  ctaLabel?: string;
  ctaHref?: string;
}

export interface RichTextContent {
  /** Raw HTML — sanitize before rendering. */
  html: string;
}

export interface PageSeo {
  title?: string;
  description?: string;
  ogImage?: string;
}
export interface PageContent {
  /** URL slug, lower-kebab. */
  slug: string;
  title: string;
  /** Raw HTML — sanitize before rendering. */
  html: string;
  seo?: PageSeo;
}

export interface ContentSummary {
  id: string;
  type: ContentType;
  key: string;
  name: string;
  status: ContentStatus;
  position: number;
  updatedAt: string;
}

export interface Content<T extends ContentType = ContentType> extends ContentSummary {
  type: T;
  data: T extends 'FAQ' ? FaqContent
      : T extends 'FOOTER' ? FooterContent
      : T extends 'HEADER' ? HeaderContent
      : T extends 'ANNOUNCEMENT' ? AnnouncementContent
      : T extends 'RICH_TEXT' ? RichTextContent
      : T extends 'PAGE' ? PageContent
      : never;
  /** Free-form merchant-defined extras. Read keys the merchant told you to expect. */
  customFields: Record<string, string>;
  salesChannelIds: string[];
}

// ---- SDK usage examples ----
//
// FAQ — render an accordion from the main FAQ (or a topical one):
//   const faq = await client.content.faq.get('main', locale);  // 'shipping', 'returns', ...
//   if (faq) {
//     faq.data.items.forEach(({ question, answer }) => {
//       // Render question + sanitize(answer) — never inject raw HTML.
//     });
//   }
//
// Footer — server component in root layout:
//   const footer = await client.content.footer.get('main', locale);
//   if (!footer) return <Fallback />;
//   // Render footer.data.columns, footer.data.social, footer.data.copyright
//
// Header — same pattern as footer:
//   const header = await client.content.header.get('main', locale);
//
// Announcement — multiple may be active; filter by date client-side:
//   const announcements = await client.content.announcement.list(locale);
//   const now = Date.now();
//   const active = announcements.filter((a) => {
//     const startOk = !a.data.startsAt || new Date(a.data.startsAt).getTime() <= now;
//     const endOk = !a.data.endsAt || new Date(a.data.endsAt).getTime() >= now;
//     return startOk && endOk;
//   });
//
// Rich text — inline block anywhere on a page:
//   const block = await client.content.richText.get('about-intro', locale);
//   <div dangerouslySetInnerHTML={{ __html: sanitize(block.data.html) }} />
//
// Page — catch-all route by slug (e.g. /about, /terms, /privacy):
//   // app/[slug]/page.tsx
//   const page = await client.content.page.getBySlug(params.slug, locale);
//   if (!page) notFound();
//   // page.data.title, page.data.html, page.data.seo
//   return <article dangerouslySetInnerHTML={{ __html: sanitize(page.data.html) }} />;
//
// Custom fields — every Content row carries a free-form Record<string, string>:
//   const faq = await client.content.faq.get('shipping');
//   <a href={`mailto:${faq.customFields.helpEmail}`}>Need help?</a>
//
// Cache — public reads carry Cache-Control: public, max-age=300,
// stale-while-revalidate=60. Storefront changes propagate within ~5 min
// of the merchant publishing. Do not add extra client-side caching
// beyond Next.js's default fetch cache.

// ---- Regions & Tax Classes (Admin mode, apiKey) ----
// storeId is derived from the API key — never pass it on admin calls.

// ---- Regions ---- (scopes: regions:read / regions:write)
// A region binds countries → currency + tax-display mode + payment providers.
interface Region {
  id: string;
  accountId: string;
  storeId: string;
  name: string;
  slug: string;
  currency: string;          // ISO 4217, e.g. "EUR"
  countries: string[];       // ISO 3166-1 alpha-2, e.g. ["DE","FR"]
  taxInclusive: boolean;     // show prices tax-inclusive in this region?
  automaticTaxes: boolean;
  isDefault: boolean;        // fallback when buyer's country maps to no region
  isActive: boolean;
  paymentProviders?: RegionPaymentProvider[];
  createdAt: string;
  updatedAt: string;
}

interface RegionPaymentProvider {
  id: string;
  regionId: string;
  appInstallationId: string;
  isEnabled: boolean;
  createdAt: string;
}

interface CreateRegionDto {
  name: string;
  currency: string;            // ISO 4217
  countries: string[];         // ISO 3166-1 alpha-2
  taxInclusive?: boolean;
  automaticTaxes?: boolean;
  isDefault?: boolean;
  paymentProviderIds?: string[]; // AppInstallation IDs to enable here
}
interface UpdateRegionDto extends Partial<CreateRegionDto> { isActive?: boolean }

// client.detectRegion(country, regions): Region | null  — pure, no network.
//   → region whose countries includes the code, else the default region, else null.
// Pass the resolved regionId to createCheckout to associate the checkout with a
// region (recorded for reporting + provider scoping). FX-at-checkout:
// presentment-enabled regions (Stripe) charge in the region currency and the
// response carries a presentment overlay; else charged in store base currency.
//
// Storefront (public, no apiKey — storeId mode OR vibe-coded mode, salesChannelId 'vc_*';
// the vc routes are gated on products:read, which every connection already has):
interface PublicRegion {
  id: string; name: string; slug: string; currency: string;
  countries: string[]; taxInclusive: boolean; isDefault: boolean;
}
interface PublicRegionDetail extends PublicRegion {
  paymentProviders: Array<{ id: string; appId: string; name: string | null }>;
}
// getStoreRegions(): { data: PublicRegion[] }  — active regions, default first.
// getStoreRegion(regionId): PublicRegionDetail  — one region + its providers.
interface AutoRegionResponse {
  region: PublicRegion | null;
  matched: boolean;  // true=country was in a region's list; false=fell back to default
  country: string;   // upper-cased ISO-3166-1 alpha-2; '' when caller omitted it
}
// getAutoRegion(country): AutoRegionResponse  — server-side resolution in one
//   round trip. Pair with the country your edge runtime extracts
//   (CF-IPCountry / request.geo.country / etc.) — Brainerce does NOT derive the
//   country from the request IP server-side (storefront != end-customer).

// ---- Tax Classes ---- (scopes: tax-classes:read / tax-classes:write)
// Charge differential rates by product type. A TaxRate may target a class via
// taxClassId; a rate with taxClassId=null is the Standard fallback. Per-line
// resolution: variant → product → category → store default → null.
interface TaxClass {
  id: string;
  accountId: string;
  storeId: string;
  name: string;
  slug: string;              // kebab-case, unique per store
  description?: string | null;
  isDefault: boolean;        // auto-applied to products without an explicit class
  createdAt: string;
  updatedAt: string;
}
interface CreateTaxClassDto { name: string; slug: string; description?: string; isDefault?: boolean }
type UpdateTaxClassDto = Partial<CreateTaxClassDto>;
// Bulk-assign a class to entities:
interface AssignTaxClassDto { productIds?: string[]; variantIds?: string[]; categoryIds?: string[] }

// TaxRate / CreateTaxRateDto carry an optional taxClassId (null = Standard).
// rate is a WHOLE PERCENTAGE (7.25 = 7.25%).
//
// SDK methods (admin):
//   Regions:     getRegions(), getRegion(id), createRegion(dto), updateRegion(id, dto),
//                deleteRegion(id), setDefaultRegion(id), updateRegionPaymentProviders(id, ids),
//                addRegionCountries(id, codes), removeRegionCountry(id, code),
//                getRegionCompatibleProviders(id), detectRegion(country, regions)
//   Tax classes: getTaxClasses(), getTaxClass(id), createTaxClass(dto), updateTaxClass(id, dto),
//                deleteTaxClass(id), setDefaultTaxClass(id), assignTaxClass(id, dto),
//                mergeTaxClasses(id, targetId)
//
// SDK methods (storefront, public — storeId mode OR vibe-coded mode 'vc_*', no apiKey;
// the vc routes are gated on products:read, which every connection already has):
//   getStoreRegions(), getStoreRegion(id), getAutoRegion(country)
//   getStoreTaxClasses(), estimateTax({ country?, subtotal })
//
// estimateTax returns:
interface TaxEstimateResponse {
  appliesTax: boolean;
  rate: number | null;        // percent (18 = 18%) — null when no matching rule
  rateName: string | null;
  estimatedTax: number;       // tax portion of subtotal in store currency
  pricesIncludeTax: boolean;
  currency: string;           // store currency (cart/order currency)
  note: string;               // disclaimer — preview is non-binding
}
// Non-binding by design: the authoritative tax runs at checkout against the
// full shipping address. The country comes from your edge runtime
// (CF-IPCountry / request.geo.country / etc.), NOT the request IP.

// ---- Loyalty & Rewards (storefront + vibe-coded modes) ----
interface LoyaltyTierSummary {
  id: string;
  name: string;
  level: number;              // ordering; higher = better tier
  pointsMultiplier: number;
}

interface LoyaltyNextTierSummary extends LoyaltyTierSummary {
  qualificationType: 'SPEND' | 'POINTS';
  qualificationThreshold: number;
}

interface LoyaltyStatus {
  enrolled: boolean;
  pointsBalance: number;      // redeemable points (pending earns excluded)
  lifetimeEarned: number;
  program: {
    pointsName: string;       // e.g. "points", "coins"
    currencyRatio: number;    // points needed to redeem 1 unit of store currency
    status: 'DRAFT' | 'ACTIVE' | 'PAUSED';
  } | null;                   // null when the store has no loyalty program
  tier: LoyaltyTierSummary | null;         // null if untiered / no tiers configured
  nextTier: LoyaltyNextTierSummary | null; // null if at the top tier already
  progressToNextTier: number; // 0..1
  pointsToNextTier: number | null;
  referralCode?: string | null;            // member's share code; null when referrals disabled / not enrolled
  referralWelcomeCoupon?: {                // unused welcome coupon from signing up via a referral link
    code: string;
    type: string;                          // 'PERCENTAGE' | 'FIXED_AMOUNT'
    value: number;
  } | null;
  badges?: LoyaltyBadge[];                 // earned milestone badges (newest first)
  paidMembership?: PaidMembershipInfo | null; // paid subscription; null for free members
}

// Milestone badge — display-only recognition, no discount attached
interface LoyaltyBadge {
  id: string;
  name: string;
  description: string | null;
  iconUrl: string | null;
  awardedAt: string;          // ISO timestamp
}

// Paid premium membership plan (recurring charge on a saved card)
interface LoyaltyMembershipPlan {
  id: string;
  name: string;
  perksDescription: string | null;
  priceAmount: number;        // per cycle, in store currency
  billingIntervalDays: number; // default 30
  pointsMultiplier: number;   // composes with the tier multiplier while ACTIVE
}

interface PaidMembershipInfo {
  status: 'ACTIVE' | 'PAST_DUE' | 'CANCELLED'; // PAST_DUE = last renewal failed (retried daily, perks paused)
  cancelAtPeriodEnd: boolean; // true = perks continue until nextBillingAt, then end without a charge
  nextBillingAt: string | null;
  plan: LoyaltyMembershipPlan | null;
}

// Saved payment method — display fields only, never card data
interface StorefrontSavedPaymentMethod {
  id: string;
  paymentMethod: string;      // 'credit_card' | 'paypal' | 'bank_account'
  brand: string | null;
  last4: string | null;
  expMonth: number | null;
  expYear: number | null;
  isDefault: boolean;
}

// AI recommendation — ALWAYS a reward from the store's real catalog
interface LoyaltyRewardRecommendation {
  reward: LoyaltyReward | null; // null when the catalog is empty
  reason?: string | null;       // short customer-facing copy
  source?: 'ai' | 'fallback';
}

// Public referral-link lookup — NO customerToken needed (safe pre-signup)
interface ReferralInfo {
  valid: boolean;                          // false for unknown/disabled codes
  referrerFirstName: string | null;        // for "Jane sent you a gift" copy — no other PII
  reward: {
    name: string;
    type: 'FIXED_DISCOUNT' | 'PERCENT_DISCOUNT';
    value: number;
    minOrderAmount: number | null;
  } | null;
}

interface LoyaltyReward {
  id: string;
  name: string;
  description: string | null;
  pointsCost: number;
  type: 'FIXED_DISCOUNT' | 'PERCENT_DISCOUNT';
  discountValue: number;      // currency amount (FIXED_DISCOUNT) or 0-100 percent (PERCENT_DISCOUNT)
  minOrderAmount: number | null;
  maxUsesPerUser: number;
  isActive: boolean;
  minTierLevel: number | null; // minimum tier level required, or null for no restriction
  createdAt: string;
  updatedAt: string;
}

interface RedeemRewardResult {
  couponCode: string;         // one-time coupon to apply at checkout
  discountType: 'FIXED_DISCOUNT' | 'PERCENT_DISCOUNT';
  discountValue: number;
  pointsSpent: number;
  pointsBalance: number;      // remaining balance after redemption
}

// client.getLoyaltyStatus(): Promise<LoyaltyStatus>
// client.enrollInLoyalty(): Promise<LoyaltyStatus>
// client.getAvailableRewards(): Promise<LoyaltyReward[]>
// client.getRecommendedReward(): Promise<LoyaltyRewardRecommendation>  // AI-ranked, rate-limited 5/min
// client.redeemLoyaltyReward(rewardId: string): Promise<RedeemRewardResult>
// client.reportSocialShare(platform?: string): Promise<{ awarded: boolean; points: number }>
// client.getReferralInfo(code: string): Promise<ReferralInfo>   // PUBLIC — no customerToken
// Referral signup: client.registerCustomer({ ..., referralCode })
// Birthday gift data: read it with client.getMyProfile() (profile.birthMonth / profile.birthDay,
//   absent until set, always returned as a pair) and write it with
//   client.updateMyProfile({ birthMonth, birthDay })
//   or straight at signup: client.registerCustomer({ ..., birthMonth, birthDay })
//   1-12 / 1-31, no year, both together. Feb 29 valid (celebrated Feb 28 in non-leap years).
//   Required at registration only when capabilities.connection.requireBirthday is true:
//   enforced on vc_* channel PASSWORD registration only, never on a storeId
//   storefront, never on OAuth sign-in, never on guest checkout.
//   The gift email reaches only customers with acceptsMarketing === true.
// Paid membership:
// client.getMembershipPlans(): Promise<LoyaltyMembershipPlan[]>
// client.getMySavedPaymentMethods(): Promise<StorefrontSavedPaymentMethod[]>
// client.subscribeToMembership({ planId, savedPaymentTokenId }): Promise<PaidMembershipInfo>  // charges immediately
// client.cancelMembership(): Promise<PaidMembershipInfo>  // end-of-period
