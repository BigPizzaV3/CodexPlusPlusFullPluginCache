## Content — typed merchant content store

Brainerce ships a typed content store so merchants can edit site chrome, FAQ,
static pages, and inline rich-text blocks in the dashboard — without
re-prompting the AI that built their storefront. Every row has a `type` +
`key` + typed `data` payload + free-form `customFields`.

**Six content types.** Each one has a fixed `data` shape; the SDK's TypeScript
generics keep them in lockstep:

| Type           | Use for                                | `data` shape (abbreviated) |
| -------------- | -------------------------------------- | --------------------------- |
| `FAQ`         | Q/A accordions                         | `{ items: { question, answer }[] }` |
| `FOOTER`      | Site footer (chrome)                   | `{ columns, copyright?, social? }` |
| `HEADER`      | Top nav + logo + CTA (chrome)          | `{ logo?, navItems, cta? }` |
| `ANNOUNCEMENT`| Banners; time-bound by `startsAt/endsAt` | `{ message, severity, dismissible, ... }` |
| `RICH_TEXT`   | Free-form HTML blocks embedded inline  | `{ html }` |
| `PAGE`        | Static pages with slug + SEO           | `{ slug, title, html, seo? }` |

Run `get-type-definitions` with `domain: 'content'` for the full interfaces.

### Default key

Every type has `'main'` as its universal default key. `client.content.faq.get()`
with no arguments resolves to `key='main'`. Topical keys (`'shipping'`,
`'holiday-2026'`, `'about'`) are merchant-named.

### Reading content (any SDK mode)

Public reads work in vibe-coded mode, storefront mode, and admin mode. They
return `null` on 404 — render hard-coded fallbacks so the page never crashes
when the merchant hasn't seeded yet.

```ts
// Single entry, default key 'main', resolved to a locale
const faq = await client.content.faq.get('main', locale);
if (faq) {
  faq.data.items.forEach(({ question, answer }) => {
    // Render question + sanitize(answer)
  });
}

// All entries of a type
const allFaqs = await client.content.faq.list(locale);

// Page by URL slug — for app/[slug]/page.tsx
const page = await client.content.page.getBySlug(slug, locale);
if (!page) notFound();
```

### Security — sanitize HTML before rendering

`FAQ.items[i].answer`, `RICH_TEXT.html`, and `PAGE.html` carry
MERCHANT-AUTHORED HTML. The server does NOT pre-sanitize — some merchants
embed iframes (e.g. YouTube) which strict sanitizers would strip. ALWAYS
sanitize on the storefront before injecting:

```ts
// Recommended: isomorphic-dompurify
import DOMPurify from 'isomorphic-dompurify';
const safe = DOMPurify.sanitize(rawHtml);
<div dangerouslySetInnerHTML={{ __html: safe }} />;
```

Skipping this is XSS.

### Custom fields

Every Content row carries a free-form `customFields: Record<string, string>`.
Merchants add arbitrary key-value extras (`helpEmail`, `phoneNumber`,
`foundedYear`) that you can opt into reading:

```ts
const faq = await client.content.faq.get('shipping');
<a href={`mailto:${faq.customFields.helpEmail}`}>Need help?</a>
```

The shape is whatever the merchant entered. Read keys you expect; ignore the rest.

### Locale resolution

All public reads accept a `locale` argument. The server resolves
`translations[locale]` server-side and returns the resolved `data` payload —
the storefront does NOT need to do its own overlay. Empty / missing translations
fall through to the default-locale value.

### Cache

Public reads carry `Cache-Control: public, max-age=300, stale-while-revalidate=60`.
Merchant edits propagate within ~5 minutes. Don't layer extra client-side
caching beyond Next.js's default fetch cache.

### Admin writes (apiKey mode)

```ts
const adminClient = new BrainerceClient({ apiKey: process.env.BRAINERCE_API_KEY });

// Create — always starts in DRAFT
const faq = await adminClient.content.faq.create({
  key: 'shipping',
  name: 'Shipping FAQ',
  data: { items: [{ question: 'How long?', answer: 'Most orders ship in 2 days.' }] },
});

// Update (data replaces wholesale; last-write-wins on the data field)
await adminClient.content.update(faq.id, {
  data: { items: [{ question: 'How long?', answer: 'Updated answer.' }] },
});

// Publish / unpublish
await adminClient.content.publish(faq.id);
await adminClient.content.unpublish(faq.id);

// Hard delete
await adminClient.content.remove(faq.id);
```

Write operations throw if called from vibe-coded or storefront mode.

### Reserved key convention

`'main'` is reserved as the universal default. Don't use it for topical
entries — pick a descriptive slug (`'shipping'`, `'returns'`, `'about'`,
`'holiday-2026'`). The validation rule is `^[a-z][a-z0-9-]*$`, max 64 chars.

### See also

- `get-business-flows` with `flow: 'content-bootstrap'` for the full
  layout / FAQ / page recipe.
- `get-required-features` lists each Content surface (`site-header`,
  `site-footer`, `announcement-bar`, `faq-page`, `static-pages`).
- `get-type-definitions` with `domain: 'content'` for the TypeScript
  interfaces.