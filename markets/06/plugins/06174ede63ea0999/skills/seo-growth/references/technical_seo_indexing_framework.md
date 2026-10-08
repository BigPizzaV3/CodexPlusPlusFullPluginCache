# Technical SEO and Indexing Framework

## Diagnose the first failing layer

`discover → crawl → render → index → canonicalize → rank → impression → click`

Do not skip straight to content or metadata.

## Crawlability

Check:
- HTTP status;
- robots.txt;
- internal links;
- redirect chains/loops;
- DNS/server availability;
- crawl traps;
- blocked resources when they materially affect rendering.

A URL can be known without its content being crawlable.

## Indexability

Check:
- `noindex`;
- X-Robots-Tag;
- authentication/login;
- canonical;
- duplicate/near-duplicate content;
- rendering;
- page value/quality.

## Canonicalization

Canonical signals should agree:
- redirects;
- `rel=canonical`;
- internal links;
- sitemap URLs;
- hreflang where relevant.

A declared canonical is a signal/preference, not an absolute guarantee.

Avoid:
- canonical to an unrelated page;
- self-canonical on an intentionally redirected URL;
- sitemap containing noncanonical duplicates;
- hreflang variants canonicalized to the wrong locale.

## Sitemaps

Include:
- canonical URLs;
- successful/indexable pages;
- URLs worth discovering.

Exclude:
- redirects;
- 4xx/5xx;
- `noindex`;
- duplicate parameter variants;
- private pages;
- staging/dev hosts.

`lastmod` should reflect meaningful page change if used.

Sitemap presence does not guarantee indexing.

## robots.txt

robots.txt controls crawling, not guaranteed deindexing.

Google can sometimes show a known blocked URL without a content snippet.

If deindexing requires a `noindex` directive, the crawler generally needs to fetch the page to see it.

## Status-code model

### 2xx
Page can be processed if other requirements allow.

### 3xx
Use for real URL movement/consolidation; avoid long chains.

### 4xx
Use when content is unavailable/removed as intended.

### 5xx
Signals server failure; sustained failures harm crawl/index availability.

## JavaScript

Do not use outdated absolutes such as:
- "Google cannot index JavaScript";
- "every SPA is bad for SEO";
- "SSR automatically ranks better."

Inspect:
- initial HTML;
- rendered HTML;
- hydration/client-only gaps;
- link crawlability;
- metadata rendering;
- blocked scripts/resources;
- runtime errors;
- content availability.

## Facets and parameters

For filters/faceted navigation decide which combinations:
- deserve indexable URLs;
- should remain crawlable but canonicalized;
- should be noindex;
- should be prevented from creating infinite crawl spaces.

Do not make every sort/filter combination indexable.

## Migration

For URL/domain migrations:
- map old → new one-to-one where possible;
- use permanent redirects;
- update canonicals/internal links/sitemaps;
- preserve content parity;
- verify all hostname/subdomain variants;
- monitor Search Console;
- keep redirects long enough for users/search engines to transition.

## Triage priority

Fix in this order when applicable:
1. catastrophic server/indexing blocks;
2. wrong canonical/redirect behavior;
3. crawl traps / environment leaks;
4. important orphan/unreachable pages;
5. duplicate/low-value template issues;
6. structured data/search appearance;
7. cosmetic metadata optimization.
