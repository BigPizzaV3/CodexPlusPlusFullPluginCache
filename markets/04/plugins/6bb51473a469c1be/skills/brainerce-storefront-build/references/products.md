## Products & Variants

### Fetching Products

```typescript
const { data: products, meta } = await client.getProducts({ page: 1, limit: 20 });
const product = await client.getProductBySlug('product-slug'); // USE THIS for product detail pages
const product = await client.getProduct(productId);

// Search autocomplete (min 2 chars, 300ms debounce)
const suggestions = await client.getSearchSuggestions(query);
// Returns: { products: ProductSuggestion[], categories: CategorySuggestion[] }
// ⚠️ ProductSuggestion.slug can be null — use id as fallback key

// Filter products
const filtered = await client.getProducts({
  categories: ['cat_123'], minPrice: 10, maxPrice: 100,
  sortBy: 'price', sortOrder: 'asc',
});

// Filter by custom fields (metafields). Only fields the merchant marked
// `filterable: true` are honored; supported types are SELECT, MULTI_SELECT,
// BOOLEAN. AND across keys, OR within a key.
const byCustom = await client.getProducts({
  metafields: { color: ['red', 'blue'], in_stock: ['true'] },
});

// Discover which custom fields are filterable for the current store:
const { definitions } = await client.getPublicMetafieldDefinitions();
const facets = definitions.filter(d => d.filterable);
// Render a checkbox group per SELECT/MULTI_SELECT, a switch per BOOLEAN.

// Facet values WITH product counts — "Color: red (12) / blue (3)" — in one
// call instead of one getProducts round trip per value:
const { filters } = await client.getMetafieldFilters();
// filters: [{ id, key, name, type, enumValues, values: [{ value, count }] }]
// Counts are DISTINCT active products; MULTI_SELECT arrays split per element;
// BOOLEAN buckets are 'true'/'false'; zero-count enumValues are included.
// Pair each key with getProducts({ metafields: { [key]: [value] } }).
```

### i18n — translated fields come back on every request

When `storeInfo.i18n.enabled` is true, call `client.setLocale(locale)` once
— all SDK calls return translated content automatically. No per-call
`{ locale }` params needed. Translated fields include: `name`,
`description`, `slug`, `seoTitle`, `seoDescription`, plus
`categories[].name`, `brands[].name`, `tags[].name`, `variants[].name`,
`variant.attributes` keys and values (so `getVariantOptions()` returns
translated attribute/option names), `productAttributeOptions[].attribute.name`/
`attributeOption.name`, `metafields[].value`, cart item product/variant names,
and recommendation/bundle/bump product names. No client-side overlay. See the
full `i18n` section (`get-sdk-docs` topic `i18n`) for the `[locale]` route
pattern, SDK setup, and the brand/tag badge examples.

### Price Display (Use SDK Helper!)

```typescript
const { price, originalPrice, isOnSale, discountPercent } = getProductPriceInfo(product);

if (isOnSale) {
  return <><span className="text-red-600">{formatPrice(price.toString(), { currency: storeInfo.currency })}</span> <s>{formatPrice(originalPrice.toString(), { currency: storeInfo.currency })}</s> -{discountPercent}%</>;
}
return <span>{formatPrice(price.toString(), { currency: storeInfo.currency })}</span>;
```

### Variable Products — MUST switch image & price on variant change!

```typescript
import { getVariantOptions, getVariantPrice, formatPrice } from 'brainerce';
import type { Product, ProductVariant, StoreInfo } from 'brainerce';

function ProductPage({ product, storeInfo }: { product: Product; storeInfo: StoreInfo }) {
  const [selectedVariant, setSelectedVariant] = useState<ProductVariant | null>(
    product.type === 'VARIABLE' && product.variants?.length ? product.variants[0] : null
  );

  // ✅ Image MUST update when variant changes!
  const displayImage = (() => {
    if (selectedVariant?.image) {
      const img = selectedVariant.image;
      return typeof img === 'string' ? img : img.url; // variant.image can be string OR {url, thumbnailUrl?}
    }
    return product.images?.[0]?.url || '/placeholder.jpg';
  })();

  // ✅ Price MUST update when variant changes!
  const displayPrice = selectedVariant
    ? getVariantPrice(selectedVariant, product.basePrice).toString()
    : product.salePrice || product.basePrice;

  // ✅ For catalog cards: use pre-computed priceMin/priceMax instead of iterating variants
  // product.priceMin / product.priceMax are always set for VARIABLE products with explicit variant prices.
  // product.priceVaries is true when the range should be shown as "₪49 – ₪199".

  // Build attribute buttons (size, color, etc.)
  const allOptions = product.variants?.map(v => getVariantOptions(v)) || [];
  const attrNames = [...new Set(allOptions.flatMap(opts => opts.map(o => o.name)))];

  return (
    <div>
      <img src={displayImage} alt={product.name} />
      <p>{formatPrice(displayPrice, { currency: storeInfo.currency })}</p>

      {product.type === 'VARIABLE' && attrNames.map(attrName => {
        const uniqueValues = [...new Set(allOptions.flatMap(opts => opts.filter(o => o.name === attrName).map(o => o.value)))];
        const currentValue = selectedVariant ? getVariantOptions(selectedVariant).find(o => o.name === attrName)?.value : undefined;
        return (
          <div key={attrName}>
            <label>{attrName}: {currentValue}</label>
            <div className="flex gap-2">
              {uniqueValues.map(value => (
                <button key={value} onClick={() => {
                  const match = product.variants?.find(v => getVariantOptions(v).some(o => o.name === attrName && o.value === value));
                  if (match) setSelectedVariant(match);
                }} className={currentValue === value ? 'bg-black text-white' : 'border'}>
                  {value}
                </button>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}
```

### Variant Attribute Selector with Swatches (color + size **mix**)

The simple text-button picker above works, but loses the merchant-configured
**swatch metadata**. A single product often mixes one attribute that should
render as **color swatches** (e.g. `Color`) and another that should render
as **text buttons** (e.g. `Size`). The product response includes everything
you need:

- `product.productAttributeOptions[]` — the swatch definitions: `attribute.name`,
  `attribute.displayType` (the `AttributeDisplayType` enum: `DEFAULT` | `COLOR_SWATCH` | `IMAGE_SWATCH` | `MIXED_SWATCH`),
  `attributeOption.name`, `swatchColor` (hex), `swatchColor2` (hex — used for dual-color swatches
  like Black & White), `swatchImageUrl` (for fabric / pattern thumbnails).
  `MIXED_SWATCH` means each option in the group can independently pick image OR color
  (the merchant decides per option). Treat any unrecognized value as `DEFAULT`.
- `variant.attributes` — the selected value per attribute on each variant.

Use `getProductSwatches(product)` to get a render-ready, grouped structure:

```typescript
import { getProductSwatches } from 'brainerce';

const groups = getProductSwatches(product);
// [
//   { attributeName: 'color', displayType: 'COLOR_SWATCH', options: [
//     { name: 'Full Color',    swatchColor: '#1D9435', swatchColor2: null,       swatchImageUrl: null },
//     { name: 'Black & White', swatchColor: '#000000', swatchColor2: '#FFFFFF',  swatchImageUrl: null },
//   ]},
//   { attributeName: 'size', displayType: 'DEFAULT', options: [
//     { name: '16" × 20"' }, { name: '24" × 32"' }, { name: '36" × 48"' },
//   ]},
// ]
```

Render one branch per `displayType`. The same loop handles all-swatch, all-text,
and the mix case:

```typescript
function VariantPicker({
  product,
  selections,
  onSelect,
}: {
  product: Product;
  selections: Record<string, string>;          // { color: 'Full Color', size: '24" × 32"' }
  onSelect: (attrName: string, value: string) => void;
}) {
  const groups = getProductSwatches(product);
  if (groups.length === 0) return null;

  return (
    <div className="space-y-4">
      {groups.map((group) => (
        <div key={group.attributeName}>
          <label className="block mb-2 text-sm font-medium">
            {group.attributeName}: <span className="text-gray-500">{selections[group.attributeName] ?? ''}</span>
          </label>
          <div className="flex flex-wrap gap-2">
            {group.options.map((opt) => {
              const isSelected = selections[group.attributeName] === opt.name;

              // COLOR_SWATCH — round button; dual-color uses a 50/50 gradient.
              if (group.displayType === 'COLOR_SWATCH' && opt.swatchColor) {
                const bg = opt.swatchColor2
                  ? `linear-gradient(135deg, ${opt.swatchColor} 50%, ${opt.swatchColor2} 50%)`
                  : opt.swatchColor;
                return (
                  <button
                    key={opt.name}
                    type="button"
                    title={opt.name}
                    aria-pressed={isSelected}
                    onClick={() => onSelect(group.attributeName, opt.name)}
                    className={`h-9 w-9 rounded-full border-2 ${isSelected ? 'border-black ring-2 ring-black/30' : 'border-gray-300 hover:border-black'}`}
                    style={{ background: bg }}
                  />
                );
              }

              // IMAGE_SWATCH — square thumbnail (fabric/pattern preview).
              if (group.displayType === 'IMAGE_SWATCH' && opt.swatchImageUrl) {
                return (
                  <button
                    key={opt.name}
                    type="button"
                    aria-pressed={isSelected}
                    onClick={() => onSelect(group.attributeName, opt.name)}
                    className={`h-10 w-10 overflow-hidden rounded border-2 ${isSelected ? 'border-black' : 'border-gray-300'}`}
                  >
                    <img src={opt.swatchImageUrl} alt={opt.name} className="h-full w-full object-cover" />
                  </button>
                );
              }

              // MIXED_SWATCH — each option is independently image OR color (image wins if present).
              if (group.displayType === 'MIXED_SWATCH') {
                if (opt.swatchImageUrl) {
                  return (
                    <button
                      key={opt.name}
                      type="button"
                      aria-pressed={isSelected}
                      onClick={() => onSelect(group.attributeName, opt.name)}
                      className={`h-10 w-10 overflow-hidden rounded border-2 ${isSelected ? 'border-black' : 'border-gray-300'}`}
                    >
                      <img src={opt.swatchImageUrl} alt={opt.name} className="h-full w-full object-cover" />
                    </button>
                  );
                }
                if (opt.swatchColor) {
                  const bg = opt.swatchColor2
                    ? `linear-gradient(135deg, ${opt.swatchColor} 50%, ${opt.swatchColor2} 50%)`
                    : opt.swatchColor;
                  return (
                    <button
                      key={opt.name}
                      type="button"
                      title={opt.name}
                      aria-pressed={isSelected}
                      onClick={() => onSelect(group.attributeName, opt.name)}
                      className={`h-9 w-9 rounded-full border-2 ${isSelected ? 'border-black ring-2 ring-black/30' : 'border-gray-300 hover:border-black'}`}
                      style={{ background: bg }}
                    />
                  );
                }
                // option has neither image nor color → fall through to text button below.
              }

              // DEFAULT (or any swatch type missing its data) — plain text button.
              return (
                <button
                  key={opt.name}
                  type="button"
                  aria-pressed={isSelected}
                  onClick={() => onSelect(group.attributeName, opt.name)}
                  className={`rounded border px-3 py-1.5 text-sm ${isSelected ? 'bg-black text-white border-black' : 'border-gray-300 hover:border-black'}`}
                >
                  {opt.name}
                </button>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
}
```

Wire it up in the product page: keep `selections` in state, find the matching
variant after each pick, and update price / image / stock from it.

```typescript
const [selections, setSelections] = useState<Record<string, string>>({});

const matchedVariant = useMemo(() => (
  product.variants?.find((v) =>
    Object.entries(selections).every(([k, val]) => v.attributes?.[k] === val)
  ) ?? null
), [product.variants, selections]);

// Greying-out unavailable combinations: for each candidate value, run
// the same find() and check `inventory.canPurchase`. Disable the button
// if no purchasable variant exists under that selection.
```

**i18n:** `getProductSwatches` returns translated `attributeName` and
`option.name` automatically when `client.setLocale()` is active. No
client-side overlay needed. Swatch colors are language-agnostic.

### Description Rendering (handles HTML vs text)

```typescript
function ProductDescription({ product }: { product: Product }) {
  const content = getDescriptionContent(product);
  if (!content) return null;
  // Descriptions are merchant HTML and may contain <video> + host-locked
  // YouTube/Vimeo <iframe> embeds. NEVER render unsanitized — sanitize and
  // allowlist video/source + iframe (restricted to youtube/vimeo hosts).
  if ('html' in content) {
    return <div dangerouslySetInnerHTML={{ __html: sanitizeProductHtml(content.html) }} />;
  }
  return <p>{content.text}</p>;
}
```

**Sanitize descriptions.** `sanitizeProductHtml` is the host-locked sanitizer the
`create-brainerce-store` scaffold ships at `src/lib/sanitize-html.ts`. If you roll
your own, allow `video`/`source` and `iframe` **restricted** to `www.youtube.com`,
`www.youtube-nocookie.com`, `player.vimeo.com` (never arbitrary iframes), and add
those hosts to your CSP `frame-src` or embeds render blank.

### Metafields (Custom Product Fields) — display on product detail!

**IMPORTANT: Render metafield values based on `mf.type`!** Don't just display `mf.value` as text for all types.

```typescript
import { getProductMetafieldValue } from 'brainerce';
import type { ProductMetafield } from 'brainerce';

// Type-aware renderer — MUST switch on mf.type!
function MetafieldValue({ field }: { field: ProductMetafield }) {
  switch (field.type) {
    case 'IMAGE':
      return field.value ? <img src={field.value} alt={field.definitionName} className="h-16 w-16 rounded object-cover" /> : <>-</>;
    case 'GALLERY': {
      let urls: string[] = [];
      try { urls = JSON.parse(field.value); } catch { urls = field.value ? [field.value] : []; }
      return urls.length > 0 ? <div className="flex gap-2">{urls.map((url, i) => <img key={i} src={url} alt={`${field.definitionName} ${i+1}`} className="h-16 w-16 rounded object-cover" />)}</div> : <>-</>;
    }
    case 'URL':
      return field.value ? <a href={field.value} target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">{field.value}</a> : <>-</>;
    case 'COLOR':
      return field.value ? <span className="inline-flex items-center gap-2"><span className="inline-block h-4 w-4 rounded-full border" style={{ backgroundColor: field.value }} />{field.value}</span> : <>-</>;
    case 'BOOLEAN':
      return <>{field.value === 'true' ? 'Yes' : 'No'}</>;
    case 'DATE':
      return field.value ? <>{new Date(field.value).toLocaleDateString()}</> : <>-</>;
    case 'DATETIME':
      return field.value ? <>{new Date(field.value).toLocaleString()}</> : <>-</>;
    default: // TEXT, TEXTAREA, NUMBER, DIMENSION, WEIGHT, JSON
      return <>{field.value || '-'}</>;
  }
}

// Display all custom fields as a spec table
{product.metafields?.length > 0 && (
  <table>
    {product.metafields.map(mf => (
      <tr key={mf.id}>
        <td className="font-medium">{mf.definitionName}</td>
        <td><MetafieldValue field={mf} /></td>
      </tr>
    ))}
  </table>
)}

// Or get a specific field by key
const material = getProductMetafieldValue(product, 'material');
```

**Metafield fields:** `definitionName` (display label), `definitionKey` (lookup key), `value`, `type` (IMAGE, GALLERY, URL, COLOR, BOOLEAN, DATE, DATETIME, TEXT, TEXTAREA, NUMBER, DIMENSION, WEIGHT, JSON)

**Translations:** When the store has i18n enabled and `client.setLocale()` is active, both the `definitionName` (the merchant-authored label like "Warranty Info" / "מידע אחריות") **and** free-text `value` come back already translated. No per-call locale param needed.

### Product Customization Fields (Customer Input)

Some products allow customers to provide input at purchase time (e.g., text on a cake, upload a logo). Check `product.customizationFields` and render input fields accordingly.

Merchants can also flag a `MetafieldDefinition` as `appliesToAllProducts: true` — those fields are folded into every product's `customizationFields` array automatically by the backend. Client code does not need to merge or union anything: always render exactly what's in `product.customizationFields`.

```typescript
import { getProductCustomizationFields } from 'brainerce';
import type { ProductCustomizationField } from 'brainerce';

const fields = getProductCustomizationFields(product);

// Render input for each field based on field.type:
// TEXT/TEXTAREA → text input, NUMBER → number input, BOOLEAN → checkbox,
// COLOR → color picker, DATE → date picker, IMAGE → file upload, etc.
// Check field.required, field.minLength, field.maxLength, field.enumValues for validation.

// Pass customer values in metadata when adding to cart:
await client.addToCart(cartId, {
  productId: product.id,
  quantity: 1,
  metadata: { cake_text: 'Happy Birthday!' },
});

// For IMAGE fields, upload first:
const { url } = await client.uploadCustomizationFile(file);
// Then use the URL in metadata: metadata: { logo: url }
```

**Customization field properties:** `key`, `name` (display label), `type`, `required`, `minLength`, `maxLength`, `minValue`, `maxValue`, `enumValues` (array of `{label, value, swatchColor?, swatchImageUrl?}`), `defaultValue`, `position`

**SELECT / MULTI_SELECT — use `option.value` to submit, `option.label` to display:**

```typescript
for (const option of field.enumValues ?? []) {
  // option.value → what to submit in metadata
  // option.label → what to show the customer
  // option.swatchColor → optional hex color for color swatches
}
```

**Display customizations in cart / checkout — no extra API call needed:**

CartItem and CheckoutLineItem both include a `customizations` object alongside `metadata`. Use `customizations` for display — it contains resolved labels, not raw keys.

```typescript
// Works for CartItem, CheckoutLineItem, and OrderItem — same shape
const lines = Object.values(item.customizations ?? {})
  .map(c => `${c.label}: ${Array.isArray(c.value) ? c.value.join(', ') : c.value}`);
// e.g. ["Frame color: Gold", "Add-ons: Gift wrap"]
```

### Downloadable / Digital Products

Products with `isDownloadable: true` are digital products. Show a digital badge instead of stock badge, list included files, and note that download links appear after purchase.

```typescript
import type { DownloadFile } from 'brainerce';

// Check if product is digital
if (product.isDownloadable) {
  // Show "Instant Download" badge instead of StockBadge
  // List files: product.downloads?.map((file: DownloadFile) => file.name)
  // Show "Download available after purchase" note
}

// After purchase — get download links from order
const downloads = await client.getOrderDownloads(orderId);
// downloads[]: { fileName, downloadUrl, downloadsUsed, downloadLimit, expiresAt }
```

### Categories

```typescript
const { categories } = await client.getCategories();
// Product.categories is Array<{id, name, slug?}> — NOT string[]
product.categories?.map(cat => cat.name);
// Use cat.slug to link to that category's landing page: /category/{slug}
```