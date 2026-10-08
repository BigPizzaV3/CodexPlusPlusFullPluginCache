# Brainerce Required Features

This is a FUNCTIONAL coverage checklist — user capabilities your build must support. It is NOT a page list or file tree. How you lay these features out (pages, modals, routes, components) is up to you and your framework.

**Build every feature marked MANDATORY, even when the underlying capability is currently disabled.** Those features auto-hide when not configured — zero visual impact — and exist so the store works the moment a store owner enables them. Features marked CONDITIONAL depend on a store setting and can be skipped when that setting is off.

## Features

### Browse, filter, and search products

Users can list products with pagination, apply category / price / attribute / custom-field filters, sort by name / price / newest, and run a search with autocomplete. Custom-field filters surface metafield definitions whose filterable=true (SELECT, MULTI_SELECT, BOOLEAN). Must handle empty states and loading states.

- SDK: client.getProducts({ page, limit, filters, sort, metafields }), client.getPublicMetafieldDefinitions(), client.getMetafieldFilters() (facet values with product counts), client.getSearchSuggestions(query)
- Status: **MANDATORY**

### View a product with variants, stock, price, and recommendations

Users can open a product, pick a variant (size/color/etc.), see the stock badge, see the price (with the regular price struck through when a sale price applies), read the description (HTML or plain text via getDescriptionContent), see metafields, and see recommended products. Image switches when the variant changes. Add-to-cart is disabled when the variant cannot be purchased.

- SDK: client.getProductBySlug(slug). Helpers: getProductPriceInfo, getVariantPrice, getStockStatus, getVariantOptions, getProductSwatches, getDescriptionContent, getProductMetafieldValue.
- Status: **MANDATORY**

### Offer a back-in-stock alert on a sold-out product

On a product (or selected variant) that is out of stock AND cannot be backordered, replace the disabled Add-to-Cart with an email capture: "Email me when it's back". Submit with the selected variantId — an alert without it waits on the product as a whole, so a shopper who wanted the medium is mailed when the small returns. Render nothing when storeInfo.stockAlertsEnabled is false (the merchant switched the feature off; submissions are then silently discarded). This is NOT a newsletter signup: no account is created and no marketing consent is granted, so never label it "Subscribe" and never gate it on consent — someone who unsubscribed from marketing can still use it. Show one message for every success ("We'll email you when it's back") — the response is uniform for a new request, a duplicate, an unknown product and an in-stock item, deliberately, so it cannot be used to read the store's stock levels. Do not promise timing: stock must hold for a few minutes and alerts go out in waves sized to the units that returned.

- SDK: client.stockAlerts.subscribe({ email, productId, variantId, locale, honeypot }). Gate on storeInfo.stockAlertsEnabled from client.getStoreInfo(), and on the item being out of stock with no backorder (getStockStatus / product.inventory).
- Status: **MANDATORY**

### Display + collect product reviews (purchaser-only) with stars, customer photos + JSON-LD

On the PDP show a Reviews section: list of customer reviews with star rating, author name (from customer profile), verified-purchase badge, body, and date — public, no login needed. Below the list, a form that adapts to the current customer: signed-in + purchased + no review yet → submit form (rating 1-5 + optional body, no name/email — those are derived from the customer profile); signed-in + purchased + already has review → edit form prefilled with rating/body plus a delete button; signed-in but did NOT purchase → "only customers who purchased this product can leave a review"; not signed in → sign-in CTA. Eligibility: physical products require an order in SHIPPED+; downloadable products additionally accept PAID/PROCESSING. On PLP cards show ★ avgRating and (reviewCount). Emit Product JSON-LD with aggregateRating ONLY when product.reviewCount > 0 — this is what unlocks the star rich snippet in Google. Reviews publish immediately; merchants moderate (hide/show) from the admin surface. Rate-limited 3 submits / 60s / IP. PHOTOS: each review can carry photos the buyer attached — render `review.images` (always an array) as a thumbnail strip on every review card, using each image's `width`/`height` so the list does not shift as they load, and link the thumbnail to the full `url`. In the form, render a file picker ONLY when `photos.enabled` from getMyProductReview() is true, cap the selection at `photos.maxPerReview`, reject files over `photos.maxBytes` before uploading, and when `photos.requiresApproval` is true say so next to the picker — a shopper who uploads, submits, and cannot find their photo will assume the site is broken.

- SDK: client.listProductReviews(productId) for the public list; client.getMyProductReview(productId) for the form-state decision; client.submitProductReview / updateMyProductReview / deleteMyProductReview for the three customer actions. All four customer methods require setCustomerToken(...) after login. Product.avgRating + Product.reviewCount are denormalized rollups returned on every product fetch. For photos: client.uploadReviewPhoto(productId, file) per file, then pass the returned `key` values as `imageKeys` on submit/update — KEYS, never urls. `imageKeys` REPLACES the photo set on update, so send the keys you are keeping; omitting the field leaves photos untouched. listProductReviews defaults to sort:'photos_first' so reviews with photos lead.
- Status: **MANDATORY**

### Render buyer-input customization fields on the product page

When a product ships with `customizationFields` (engraving text, uploaded photo, picked color, date, select / multi-select), render one control per field sorted by `position`. Enforce required + enumValues + min/max client-side. For IMAGE / GALLERY, upload via client.uploadCustomizationFile() and place the returned URL in the value. Submit all values keyed by `field.key` inside addToCart({ metadata }). Show the metadata on cart / checkout rows so the buyer can verify. Build the UI anyway — it auto-hides when a product has no customization fields. NOTE: merchants can flag a definition with `appliesToAllProducts: true`; the backend folds those into every product's `customizationFields` array automatically — the client never merges or unions anything, just reads `product.customizationFields` as-is.

- SDK: product.customizationFields, client.uploadCustomizationFile(file), client.addToCart({ productId, quantity, metadata })
- Flow: call `get-business-flows` with `'product-customization'`
- Status: **MANDATORY**

### Manage a cart with quantity, removal, and totals

Users can add items, change quantities, remove items, select which items to check out (checkbox-per-item for partial checkout), and see accurate totals (subtotal, tax, shipping, discount, total).

- SDK: client.addToCart, client.updateCartItem, client.removeCartItem, client.getCart, getCartTotals(cart)
- Flow: call `get-business-flows` with `'cart-persistence'`
- Status: **MANDATORY**

### Apply and remove coupon codes

Users can enter a coupon code, see it applied to the cart, see the discount amount, and remove it. Build the UI even if no coupons are configured today — it auto-hides.

- SDK: client.applyCoupon(cartId, code), client.removeCoupon(cartId) — on cart page. client.applyCheckoutCoupon(checkoutId, code), client.removeCheckoutCoupon(checkoutId) — on checkout page (use when checkoutId exists)
- Status: **MANDATORY**

### Display the inventory reservation countdown

Users see a live countdown showing how long their cart items are held. On expiry, users are shown an "expired" state and prompted to refresh the cart.

- SDK: Reservation timestamps come from the Cart object returned by client.getCart(). Do not implement your own timer logic.
- Flow: call `get-business-flows` with `'inventory-reservation'`
- Status: **MANDATORY**

### Complete a full checkout end-to-end

Users can enter their address, pick a shipping rate, pick a payment provider, pay, and land on a confirmation page showing the real order. Displays checkout.lineItems (not cart.items) on the summary.

- SDK: client.setShippingAddress (returns { checkout, rates }), client.selectShippingMethod, client.getPaymentProviders(), provider-specific confirm, client.handlePaymentSuccess, client.waitForOrder
- Flow: call `get-business-flows` with `'checkout'`
- Status: **MANDATORY**

### Show an order confirmation that clears the cart and waits for the real order

On landing, calls handlePaymentSuccess (mandatory) and waitForOrder (mandatory). Displays a loading state while polling. Renders the order number and line items when the order exists. Handles timeout gracefully with a link to order history.

- SDK: client.handlePaymentSuccess(checkoutId), client.waitForOrder(checkoutId)
- Flow: call `get-business-flows` with `'order-confirmation'`
- Status: **MANDATORY**

### Register a new account with email verification

Users can create an account (email, password, first + last name). Handles the requiresVerification branch by routing to an email-verification step. Verification step collects a 6-digit code and has a "resend code" action.

- SDK: client.registerCustomer({email, password, firstName, lastName}), client.verifyEmail(code), client.resendVerificationEmail()
- Flow: call `get-business-flows` with `'auth-register'`
- Status: **MANDATORY**

### Log in with email / password and handle verification branch

Users can log in. The login form handles the requiresVerification branch by routing to the verify-email step. Specific errors render (bad credentials, rate limited, disabled account).

- SDK: client.loginCustomer(email, password)
- Flow: call `get-business-flows` with `'auth-login'`
- Status: **MANDATORY**

### Sign in with OAuth providers

Users see OAuth buttons on login and register. Clicking a button redirects to the provider authorization URL. A callback handler (server-side / BFF) extracts the token from the URL, exchanges it for a session cookie, and redirects to the account area. Error params are handled.

- SDK: client.getAvailableOAuthProviders()
- Flow: call `get-business-flows` with `'oauth'`
- Status: **MANDATORY**

### Recover a forgotten password

Forgot-password UI accepts an email and calls forgotPassword. It always shows a generic success message (no account enumeration). Reset-password UI reads the token from the URL, collects a new password, calls resetPassword, and redirects to login on success. Handles expired/invalid token errors.

- SDK: client.forgotPassword(email), client.resetPassword(token, newPassword)
- Flow: call `get-business-flows` with `'password-reset'`
- Status: **MANDATORY**

### Show account profile and order history

A protected area (redirect to login when no session) that shows the customer profile (name, email, contact info) and a paginated order history with status, totals, and line items per order. Logout clears the BFF session.

- SDK: client.getMyProfile(), client.getMyOrders({page, limit}), client.clearCustomerToken()
- Status: **MANDATORY**

### Global header with cart count and search

A header visible across the experience with the store logo, navigation, a cart icon with live item count, a search input with autocomplete (debounced ~300ms, 2-char minimum), and a login / account action. Below the header, discount banners render when active.

- SDK: client.getCart() for the count, client.getSearchSuggestions(query) for autocomplete
- Status: **MANDATORY**

### Show active discount banners and badges

Active discount rules render as banners (below the header) and as badges on product cards / detail pages. Build the UI even if the store has no active discounts today — it auto-hides.

- SDK: client.getDiscountBanners(), client.getProductDiscountBadge(productId)
- Status: **MANDATORY**

### Honor store shipping zones during checkout

Checkout displays only the shipping rates valid for the customer's address. This happens automatically if you call setShippingAddress and render the returned rate list — do not filter or invent rates yourself.

- SDK: setShippingAddress returns shippingRates scoped to the zone
- Status: **MANDATORY**

### Handle downloadable products

Downloadable products show a download badge on the product card and detail page. After purchase, order confirmation and order history expose a download action. Build the UI even if no downloadables exist today — it auto-hides.

- SDK: Product type includes a downloadable flag; order includes download URLs.
- Status: **MANDATORY**

### Render store-specific custom checkout fields

Some stores configure custom checkout fields (e.g., tax ID, delivery notes, a delivery date). The checkout form must render any configured custom fields and include their values in the submission. A DATE/DATETIME field may carry a dateAvailability config, and a picker that ignores it offers days and times the API then rejects with a 400 after the shopper has committed: disable them up front instead.

- SDK: get-store-capabilities.features.hasCheckoutCustomFields; field definitions come from the checkout payload. For DATE/DATETIME, feed field.dateAvailability plus a clock ({ timezone } from getStoreInfo()) into isCalendarDateAllowed()/computeAvailableSlots()/getBusinessHoursForDate(), and isDateValueAllowed() before submit. The clock is what applies leadTimeMinutes/cutoffTime/maxDaysAhead; omit it and those are silently skipped. A weekday can carry several businessHours windows (a split day), so render every window, not just the first.
- Status: **MANDATORY**

### Serve multiple languages with a language switcher

When i18n is enabled, the experience routes by locale, sets the SDK locale (client.setLocale), includes a language switcher in the header, and renders the correct document direction by reading client.getStoreDirection(locale) — do not hardcode an RTL locale set.

- SDK: client.setLocale(locale). client.getStoreDirection(locale) for <html dir>. Read supported locales from get-store-capabilities.store.i18n.
- Status: **BUILD (enabled for this store)**

### Site header from merchant content (logo + nav + CTA)

Fetch client.content.header.get("main", locale) in the root layout. Returns null when the merchant has not seeded yet — render a hard-coded fallback so the page never crashes. Renders header.data.logo, header.data.navItems[], header.data.cta if present.

- SDK: client.content.header.get("main", locale)
- Flow: call `get-business-flows` with `'content-bootstrap'`
- Status: **MANDATORY**

### Site footer from merchant content (columns + social + copyright)

Fetch client.content.footer.get("main", locale) in the root layout. Returns null when unseeded — render a hard-coded fallback. Render footer.data.columns[].links, footer.data.social[], footer.data.copyright.

- SDK: client.content.footer.get("main", locale)
- Flow: call `get-business-flows` with `'content-bootstrap'`
- Status: **MANDATORY**

### Announcement bar at the top of every page

Fetch client.content.announcement.list(locale) in the root layout. Filter by data.startsAt / data.endsAt client-side. Render a dismissible bar when data.dismissible=true. Build the UI anyway — it auto-hides when no announcements exist.

- SDK: client.content.announcement.list(locale)
- Flow: call `get-business-flows` with `'content-bootstrap'`
- Status: **BUILD (enabled for this store)**

### FAQ page rendered from merchant content

Build /faq as an accordion fed by client.content.faq.get("main", locale). For topical FAQs, use a key parameter (shipping, returns, ...). Always sanitize answer HTML before injecting via dangerouslySetInnerHTML. Build the page anyway — it auto-hides or 404s when no FAQ rows exist.

- SDK: client.content.faq.get("main", locale), client.content.faq.list(locale)
- Flow: call `get-business-flows` with `'content-bootstrap'`
- Status: **BUILD (enabled for this store)**

### Static pages from merchant content (About, Terms, Privacy, …)

Mount a catch-all app/[slug]/page.tsx route. Inside, call client.content.page.getBySlug(params.slug, locale). On null → notFound(). On hit, sanitize page.data.html before injecting via dangerouslySetInnerHTML. Generate <Metadata> from page.data.seo. Build the route anyway — it 404s on unknown slugs.

- SDK: client.content.page.getBySlug(slug, locale), client.content.page.list(locale)
- Flow: call `get-business-flows` with `'content-bootstrap'`
- Status: **BUILD (enabled for this store)**

### Blog pages + SEO/GEO discoverability (sitemap, robots, IndexNow key, llms.txt, agents.md)

Build /blog (paginated list via client.blog.getPosts()) and /blog/[slug] (client.blog.getPost(slug); null → notFound(); sanitize post.content before dangerouslySetInnerHTML; emit Article JSON-LD via buildArticleJsonLd + jsonLdScriptProps). The store's SEO Autopilot publishes AI-written articles into this blog automatically, so posts can appear at any time — build the pages even when the blog is empty today. Discoverability requirements: (1) build sitemap.xml from the SDK helpers — products MUST use getProductSitemapEntries(client, { siteUrl }) (the listing API clamps limit to 100, so a getProducts({ limit: 1000 }) sitemap silently truncates; the helper uses a dedicated endpoint with a 5000 cap), plus getCategorySitemapEntries + getBlogSitemapEntries; (2) robots.txt must ALLOW the AI search/user crawlers by name (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Bingbot, Applebot, Amazonbot) — merchants want AI assistants to recommend their products, and these bots read raw HTML only; (3) serve the IndexNow key file at GET /indexnow-key.txt returning getStoreInfo().seo.indexNowKey as text/plain (404 while null — not a secret); (4) serve /llms.txt (store summary + categories + recent articles) AND /agents.md (agent-facing guide: machine surfaces, key URLs, how buying works) for AI answer engines; (5) when getStoreInfo().seo.googleSiteVerification is set, render <meta name="google-site-verification" content={token}> in the root layout head — it is what lets the merchant verify the domain in Search Console and claim it in Merchant Center; (6) in the not-found path of /products/[slug] and /blog/[slug], call client.resolveSlugRedirect('product'|'blog', slug) and permanentRedirect() to the returned currentSlug — the platform records every slug rename, and without this every dashboard slug edit permanently 404s the old URL. See the 'seo' topic for exact snippets.

- SDK: client.blog.getPosts({ page, limit }), client.blog.getPost(slug), getProductSitemapEntries(client, opts), getBlogSitemapEntries(client, opts), buildArticleJsonLd(post, opts), jsonLdScriptProps(data), client.resolveSlugRedirect(type, slug), getStoreInfo().seo.indexNowKey, getStoreInfo().seo.googleSiteVerification
- Status: **MANDATORY**

### Category (collection) pages — highest-leverage organic SEO

Build /category/[slug] via client.getCategoryBySlug(slug) (null → notFound()) for the landing metadata + client.getProducts({ categories: [category.id] }) for the product grid. Category pages rank for broad research-intent queries ('running shoes') that individual product pages never capture — the single highest-leverage organic surface. Render metaDescription into <meta name=description> and the sanitized description HTML BELOW the grid (so products stay above the fold); emit buildCollectionPageJsonLd + buildBreadcrumbJsonLd (NEVER buildProductJsonLd on a listing page). Append category URLs to sitemap.xml via getCategorySitemapEntries(client, { siteUrl }). The store's SEO Autopilot writes category descriptions + meta automatically, so build the page even when descriptions are sparse today. See the 'seo' topic for exact snippets.

- SDK: client.getCategoryBySlug(slug), client.getProducts({ categories }), getCategorySitemapEntries(client, opts), buildCollectionPageJsonLd(category, opts), buildBreadcrumbJsonLd(items)
- Status: **BUILD (enabled for this store)**

## Self-verification

Before you report the build complete, walk the list above and confirm each MANDATORY feature is reachable in your finished experience. Call `get-business-flows` if you need to double-check a sequence. If anything is missing, go build it.