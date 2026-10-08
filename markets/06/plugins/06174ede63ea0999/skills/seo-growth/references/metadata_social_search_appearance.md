# Metadata, Social, and Search Appearance

## Title elements

Good titles are:
- descriptive;
- page-specific;
- aligned with visible content;
- readable;
- not stuffed with repeated keywords.

Google may generate a different displayed title link using multiple page signals.

Do not promise exact SERP rendering.

## Meta descriptions

Use a concise page-specific summary that helps a searcher decide whether the result matches their need.

Search engines can generate snippets from page content instead of the supplied meta description.

Meta descriptions are presentation/CTR inputs, not a ranking guarantee.

## Canonical metadata

Use an absolute canonical URL where appropriate.

Keep canonical consistent with:
- redirects;
- internal links;
- sitemap;
- hreflang.

## Open Graph

Core OGP properties:
- `og:title`;
- `og:type`;
- `og:image`;
- `og:url`.

Frequently useful:
- `og:description`;
- `og:site_name`;
- image alt/type/dimensions where supported.

OGP improves social/share representation; do not describe it as a direct ranking factor.

## Search/Discover images

Google's 2026 Search documentation notes that `og:image` can be one source when choosing preferred image thumbnails in Search/Discover.

That still does not guarantee a thumbnail.

## Social-card QA

Test:
- absolute public URL;
- response status;
- content type;
- fetchability;
- redirect behavior;
- crop/safe area;
- readability at small preview sizes;
- cache refresh behavior on target networks.

Do not claim a preview is correct without testing or supplied evidence.

## Favicons

Use a stable, crawlable favicon that represents the site brand.

Current Google guidance recommends a square favicon and favors assets larger than the minimum so they render clearly.

## Site name / organization identity

When relevant align:
- visible brand;
- organization/site structured data;
- home-page title;
- favicon;
- canonical hostname.

Avoid conflicting names across metadata.

## Page-level checklist

For an important public page:
- meaningful `<title>`;
- accurate description;
- canonical;
- robots/indexability;
- OG/social metadata;
- favicon/site identity handled globally;
- structured data only if appropriate;
- visible H1/content consistent with metadata.
