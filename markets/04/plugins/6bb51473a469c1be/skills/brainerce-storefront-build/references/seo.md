## SEO & Discoverability

Brainerce's **SEO Autopilot** writes and publishes blog posts automatically
(keyword planning → AI article → publish → IndexNow ping). Your storefront
must make that content discoverable: category pages (the highest-leverage
organic surface), product + category + blog entries in the sitemap, an
AI-crawler-friendly robots.txt, the IndexNow key file, the site-verification
meta tag, and the AI-discovery files (/llms.txt + /agents.md) — plus JSON-LD
builders you should use on every page type.

### 1. JSON-LD builders (use these, never hand-rolled objects)

```tsx
import {
  buildProductJsonLd,       // PDPs ONLY — never listing pages
  buildArticleJsonLd,       // blog post pages
  buildCollectionPageJsonLd, // category / collection pages
  buildOrganizationJsonLd,  // homepage — brand entity (Knowledge Panel + AI)
  buildWebsiteJsonLd,       // homepage — sitelinks search box (Authority signal)
  buildBreadcrumbJsonLd,
  jsonLdScriptProps,        // XSS-safe <script> props (escapes '<')
} from 'brainerce';

// `siteUrl` must be the storefront's PUBLIC origin. Do NOT read it from an env
// var with a hardcoded default — the value is often unknown until runtime (an
// AI builder deploys to a domain it owns; a container host learns its hostname
// only from the request), and a wrong absolute URL is indistinguishable from a
// correct one to a crawler. Resolve it: explicit env (SITE_URL) first, then
// hosting-platform vars (VERCEL_PROJECT_PRODUCTION_URL, CF_PAGES_URL, ...),
// then the request's x-forwarded-host. Never fall back to a literal address.
const siteUrl = await getCanonicalSiteUrl();

// Homepage — brand/Authority signals (Organization feeds the Knowledge Panel +
// AI answers via sameAs social profiles; WebSite enables the sitelinks search
// box). searchUrlTemplate must point at the store's real search route.
<script {...jsonLdScriptProps(buildOrganizationJsonLd(storeInfo, {
  siteUrl,
}))} />
<script {...jsonLdScriptProps(buildWebsiteJsonLd(storeInfo, {
  siteUrl,
  searchUrlTemplate: '/products?search={search_term_string}',
}))} />

// Blog article page
<script {...jsonLdScriptProps(buildArticleJsonLd(post, {
  siteUrl,
  path: `/blog/${post.slug}`,
  organizationName: storeInfo.name,
}))} />

// Product page (single-product pages only)
<script {...jsonLdScriptProps(buildProductJsonLd(product, {
  siteUrl,
  path: `/products/${product.slug}`,
  currency: storeInfo.currency,
  shipping: storeInfo.shipping, // optional — real flat-rate/free zones, adds shippingDetails when present
}))} />

// Category page (CollectionPage — NEVER Product markup on a listing)
<script {...jsonLdScriptProps(buildCollectionPageJsonLd(category, {
  siteUrl,
  path: `/category/${category.slug}`,
}))} />
```

The builders encode Google's rules: `aggregateRating` only when
`reviewCount > 0` (with explicit `bestRating`/`worstRating`), AggregateOffer
(with `offerCount`) for VARIABLE products, ISO-4217 currency, and the full
availability mapping — `InStock` from the backend's pre-computed
`inventory.inStock`, `BackOrder` for purchasable-while-out-of-stock products,
`OutOfStock` otherwise. Do NOT re-derive availability yourself.
`buildProductJsonLd`'s Offer also always includes `itemCondition` (hardcoded
`NewCondition` — first-party new-goods catalog), `priceValidUntil` when the
product has an active sale-price window (`salePriceEndsAt`), and
`shippingDetails` when you pass `shipping` from `storeInfo.shipping` — never
fabricated, omitted entirely when you don't pass it.

### 2. Category page — the highest-leverage organic surface (BUILD IT)

Category (collection) pages rank for broad research-intent queries individual
products never capture. `/category/[slug]` via `client.getCategoryBySlug(slug)`
(`null` → 404) for the metadata + `getProducts({ categories: [id] })` for the
grid. The SEO Autopilot writes the description + meta in the dashboard; the
storefront renders `metaDescription` into the meta tag and the sanitized
`description` HTML **below** the grid, plus CollectionPage + Breadcrumb JSON-LD.

### 3. Product + category + blog entries in sitemap.xml (REQUIRED)

⚠️ **Products MUST use `getProductSitemapEntries`.** The public listing API
clamps `limit` to 100, so a naive `getProducts({ limit: 1000 })` sitemap
**silently truncates at 100 products**. The helper uses a dedicated
lightweight endpoint (slug + updatedAt only, up to 5000 in one call) and
falls back to pagination on older backends.

```ts
// app/sitemap.ts
import {
  getProductSitemapEntries,
  getBlogSitemapEntries,
  getCategorySitemapEntries,
} from 'brainerce';

const productPages = await getProductSitemapEntries(client, {
  siteUrl: baseUrl, locales: supportedLocales, defaultLocale,
}).catch(() => []);
const categoryPages = await getCategorySitemapEntries(client, {
  siteUrl: baseUrl, locales: supportedLocales, defaultLocale,
}).catch(() => []);
const blogPages = await getBlogSitemapEntries(client, {
  siteUrl: baseUrl,
  locales: supportedLocales,   // optional, multi-locale stores
  defaultLocale,
}).catch(() => []);
return [...staticPages, ...productPages, ...categoryPages, ...blogPages];
```

Autopilot articles and category pages missing from the sitemap never get
crawled. Also include indexable static routes (/, /products, /faq, /contact)
and merchant content pages (`client.content.page.list()` → `/pages/{slug}`).

### 3b. robots.txt — allow the AI crawlers (REQUIRED)

Merchants want ChatGPT / Perplexity / Claude / Copilot to recommend their
products. Those engines' crawlers read raw HTML and respect robots.txt — a
default-deny (or an aggressive bot blocker) makes the store invisible to
them. Allow the AI search/user agents by name, keep checkout/account/api
disallowed:

```ts
// app/robots.ts
const DISALLOW = ['/api/', '/auth/', '/checkout/', '/account/'];
export default function robots() {
  return {
    rules: [
      { userAgent: '*', allow: '/', disallow: DISALLOW },
      // AI search + user-request agents — REQUIRED for AI-assistant visibility
      { userAgent: ['OAI-SearchBot', 'ChatGPT-User', 'Claude-SearchBot',
                    'Claude-User', 'PerplexityBot', 'Perplexity-User',
                    'Bingbot', 'Applebot', 'Amazonbot'],
        allow: '/', disallow: DISALLOW },
      // Training crawlers — allowed by default (model familiarity feeds
      // zero-shot recommendations); flip to disallow only if the merchant
      // explicitly objects to AI training. Blocking these does NOT affect
      // search visibility.
      { userAgent: ['GPTBot', 'ClaudeBot', 'CCBot', 'Google-Extended',
                    'Meta-ExternalAgent', 'Applebot-Extended'],
        allow: '/', disallow: DISALLOW },
    ],
    sitemap: `${baseUrl}/sitemap.xml`,
  };
}
```

### 4. IndexNow key file (REQUIRED)

The platform pings IndexNow (instant indexing on Bing/Yandex/etc.) whenever a
blog post publishes. Search engines verify ownership by fetching
`/indexnow-key.txt`. Serve it exactly like this:

```ts
// app/indexnow-key.txt/route.ts
import { getServerClient } from '@/core/lib/brainerce';

export const revalidate = 3600;

export async function GET() {
  const info = await getServerClient().getStoreInfo().catch(() => null);
  const key = info?.seo?.indexNowKey;
  if (!key) return new Response(null, { status: 404 });
  return new Response(key, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
}
```

The key comes from `getStoreInfo().seo.indexNowKey` — NOT a secret (the file
is public by protocol design). 404 while `null` is correct; the platform
skips pings until the file verifies.

### 5. llms.txt + agents.md (REQUIRED)

Two AI-discovery files, same data, two conventions. `/llms.txt` is the
site summary AI answer engines read; `/agents.md` is the agent-facing guide
(what the site sells, where the machine surfaces live, how buying works) —
the convention shopping agents standardized on in 2026. Serve both and keep
them consistent:

```ts
// app/llms.txt/route.ts
export const revalidate = 3600;
export async function GET() {
  const client = getServerClient();
  const [info, posts, cats] = await Promise.all([
    client.getStoreInfo().catch(() => null),
    client.blog.getPosts({ limit: 20 }).catch(() => null),
    client.getCategories().catch(() => null),
  ]);
  const lines = [
    `# ${info?.name}`,
    info?.metaDescription ? `> ${info.metaDescription}` : '',
    '## Key pages',
    `- [Products](${baseUrl}/products)`,
    ...(cats?.categories ?? []).filter((c) => c.slug)
      .map((c) => `- [${c.name}](${baseUrl}/category/${c.slug})`),
    `- [Blog](${baseUrl}/blog)`,
    '## Machine-readable surfaces',
    `- [Agent guide](${baseUrl}/agents.md)`,
    `- [Sitemap](${baseUrl}/sitemap.xml)`,
    '## Recent articles',
    ...(posts?.data ?? []).map((p) => `- [${p.title}](${baseUrl}/blog/${p.slug})`),
  ];
  return new Response(lines.filter(Boolean).join('\n'), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
}

// app/agents.md/route.ts — same shape, markdown content type. State: what the
// store is (name + metaDescription), that product data is server-rendered
// with schema.org JSON-LD, the machine surfaces (sitemap.xml, llms.txt,
// indexnow-key.txt), key URLs (catalog, top categories, blog, FAQ, contact),
// the currency, and that checkout happens on-site.
```

**Recommended companion:** a blog RSS feed at `/blog/rss.xml`
(`application/rss+xml`, latest ~50 posts from `client.blog.getPosts()`,
XML-escape every field) plus
`<link rel="alternate" type="application/rss+xml" href="/blog/rss.xml" />`
in the root layout head — the SEO Autopilot auto-publishes articles, and RSS
lets readers/aggregators follow them.

**Multi-locale gotcha:** the locale middleware's matcher usually excludes
dotted paths (`(?!.*\..*)`). Keep `llms.txt/`, `indexnow-key.txt/`, and
`agents.md/` route directories at the app ROOT — never inside `[locale]/`,
where the un-rewritten request would resolve as the homepage with
`locale="llms.txt"` and serve HTML instead of the file. `/blog/rss.xml` is
dotted AND nested — it must ALSO sit at the app root (`app/blog/rss.xml/`);
the literal `blog` segment wins over `[locale]` so locale pages keep working.

### 6. Google site-verification meta tag (REQUIRED when set)

The merchant pastes their Search Console verification token in the dashboard
(channel settings). Render it in the root layout `<head>` — it is what lets
them verify the domain in Search Console and claim the website in Merchant
Center:

```tsx
{storeInfo?.seo?.googleSiteVerification ? (
  <meta name="google-site-verification" content={storeInfo.seo.googleSiteVerification} />
) : null}
```

### 7. Renamed slugs must 301, not 404 (REQUIRED)

The platform records every product/blog slug rename. In the not-found path of
`/products/[slug]` and `/blog/[slug]`, resolve before giving up — otherwise
every slug edit in the dashboard permanently 404s the old URL and its ranking:

```tsx
import { notFound, permanentRedirect } from 'next/navigation';

let product;
try {
  product = await client.getProductBySlug(slug);
} catch {
  const redirect = await client.resolveSlugRedirect('product', slug); // 'blog' for posts
  if (redirect) permanentRedirect(`/products/${redirect.currentSlug}`);
  notFound();
}
```

`resolveSlugRedirect` returns `null` when no rename was recorded (genuine
404) and never throws. Rename chains (a→b→c) collapse to one hop. Default
locale stays unprefixed in the redirect target.

### Staying fresh

Subscribe to the `blog.post.published` / `blog.post.updated` outbound
webhook events (merchant dashboard → Webhooks) to revalidate your `/blog`
ISR caches the moment the autopilot publishes. Without a webhook, standard
ISR revalidation windows apply.

Blog rendering itself (`/blog` + `/blog/[slug]`) is covered in the "blog"
topic — those pages are required for any store with published posts.
