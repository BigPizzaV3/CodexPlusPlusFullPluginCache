# Content payload shapes

Distilled from the Brainerce SDK type definitions. For a developer wiring
content into a storefront; a merchant never sees any of this.

Every entry is keyed on `(type, key)` per store and carries a `data` payload
whose shape depends on the type, plus a merchant-defined `customFields` map of
free-form string extras available on every row regardless of type.

```ts
type ContentType = 'FAQ' | 'FOOTER' | 'HEADER' | 'ANNOUNCEMENT' | 'RICH_TEXT' | 'PAGE';
type ContentStatus = 'DRAFT' | 'PUBLISHED';
```

Only `PUBLISHED` entries reach a storefront.

## ⛔ Sanitize before rendering

`RICH_TEXT.html`, `PAGE.html` and every FAQ `answer` are **merchant-authored
HTML that the server does not pre-sanitize**. That is deliberate: some merchants
embed iframes, a YouTube video for instance, which a strict sanitizer strips.
The policy is the storefront's to choose, which means the storefront has to
choose one. Use `isomorphic-dompurify` or equivalent, always, before injecting.

## The payloads

```ts
interface FaqContent {
  items: Array<{ question: string; answer: string }>; // answer is HTML
}

interface FooterContent {
  columns: Array<{ title: string; links: Array<{ label: string; url: string }> }>;
  copyright?: string;
  social?: Array<{ platform: string; url: string }>; // 'instagram' | 'facebook' | 'x' | ...
}

interface HeaderContent {
  logo?: { src: string; alt: string };
  navItems: Array<{ label: string; url: string }>;
  cta?: { label: string; url: string };
}

interface AnnouncementContent {
  message: string;
  severity: 'info' | 'warning' | 'success';
  dismissible: boolean;
  startsAt?: string; // ISO 8601
  endsAt?: string;   // ISO 8601
  ctaLabel?: string;
  ctaHref?: string;
}

interface RichTextContent {
  html: string; // raw, sanitize
}

interface PageContent {
  slug: string;  // lower-kebab
  title: string;
  html: string;  // raw, sanitize
  seo?: { title?: string; description?: string; ogImage?: string };
}
```

## Two things a storefront has to do that nothing does for it

**Filter the announcement window.** `startsAt` and `endsAt` are advisory: the
storefront filters on them client side. Ignore them and the banner runs forever,
which is how a Black Friday bar is still up in January.

**Route the pages.** A `PAGE` entry is not automatically served at its slug.
Fetch the entries, build the routes. A merchant reporting that their published
About page 404s has a routing gap, not a content problem.

## Navigation, assembled from two sources

There is no navigation entity. A menu is:

- **The category tree**, fetched as a nested structure of `{ id, name, slug,
  children[] }`. Each node links its own page at `/category/{slug}`. This is the
  browsable half.
- **`HEADER.navItems`**, a flat list of label and URL pairs. This is where links
  that are not categories go.

Render them together. Which of the two a given link belongs in is a merchant
decision, and `brainerce-store-architecture` covers how to make it.

## Category pages are the SEO surface

Worth knowing while wiring content: category landing pages rank for the broad
research queries ("running shoes") that individual product pages never capture.
`getCategoryBySlug` returns the merchant-authored landing-page description and
meta written in the dashboard SEO hub; the products come separately from
`getProducts({ categories: [id] })`. A storefront that renders a category as a
bare product grid with no copy is leaving that traffic on the table.
