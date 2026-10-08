# Official Source Registry

Research date: 2026-09-23

Use current first-party search-engine/platform documentation for behavior that changes over time.

## OpenAI plugin packaging

- Plugins:
  https://developers.openai.com/plugins
- Build skills:
  https://developers.openai.com/plugins/build/skills
- Package plugins:
  https://developers.openai.com/plugins/build/plugins
- Submit plugins:
  https://developers.openai.com/plugins/deploy/submission
- Submission validation:
  https://developers.openai.com/plugins/deploy/submission-errors

## Google Search fundamentals

- SEO Starter Guide:
  https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Helpful, reliable, people-first content:
  https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Spam policies:
  https://developers.google.com/search/docs/essentials/spam-policies
- Generative AI / AI Search optimization guide:
  https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Search documentation updates:
  https://developers.google.com/search/updates

Important 2026 updates:
- Google removed FAQ rich results from Search in May 2026.
- Google clarified in June 2026 that `llms.txt` is not needed for Google Search and does not help or hurt Google Search visibility/rankings.
- Google added/expanded guidance for generative-AI Search features while reaffirming standard SEO fundamentals.

## Crawling, indexing, canonicals, robots

- Canonicalization:
  https://developers.google.com/search/docs/crawling-indexing/canonicalization
- Build/submit sitemap:
  https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Block indexing (`noindex`):
  https://developers.google.com/search/docs/crawling-indexing/block-indexing
- Crawlable links:
  https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- robots.txt specification:
  https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec
- Crawl budget:
  https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget
- Faceted navigation:
  https://developers.google.com/crawling/docs/faceted-navigation

Durable rules:
- robots.txt controls crawling; it is not a universal deindexing mechanism.
- A canonical declaration is a signal/preference, not a guarantee.
- Sitemaps help discovery and canonical signaling but do not guarantee indexing.
- Google does not support `crawl-delay` in robots.txt.

## Search appearance and metadata

- Search appearance:
  https://developers.google.com/search/docs/appearance
- Title links:
  https://developers.google.com/search/docs/appearance/title-link
- Snippets / meta descriptions:
  https://developers.google.com/search/docs/appearance/snippet
- Favicons:
  https://developers.google.com/search/docs/appearance/favicon-in-search
- Image SEO:
  https://developers.google.com/search/docs/appearance/google-images
- Preferred Sources:
  https://developers.google.com/search/docs/appearance/preferred-sources

Google can generate/rewrite title links and snippets rather than using supplied metadata verbatim.

Google's March 2026 documentation update clarified that both Schema.org markup and `og:image` can contribute to preferred image selection in Search/Discover.

## Structured data

- Structured data overview:
  https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Supported Search gallery:
  https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- General guidelines:
  https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Breadcrumb:
  https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- Schema.org:
  https://schema.org/

Important:
- Schema.org vocabulary support does not automatically mean Google provides a rich-result feature for the type.
- Valid structured data does not guarantee a rich result.
- Markup must match visible page content.

## Search Console

- Search Console Help:
  https://support.google.com/webmasters/
- Performance report discrepancy guidance:
  https://support.google.com/webmasters/answer/17010575
- Search generative AI control:
  https://support.google.com/webmasters/answer/16908024
- Generative-AI Search performance reporting:
  https://support.google.com/webmasters/answer/16984139

Current reporting caveats include:
- anonymized queries;
- table row limits;
- aggregation differences;
- processing lag;
- Pacific Time reporting for most date views.

As of August 31, 2026, Google documented global rollout of Search generative-AI control/reporting capabilities, though property visibility can still depend on eligibility/data.

## Open Graph / social previews

- Open Graph protocol:
  https://ogp.me/

Core OGP metadata:
- `og:title`
- `og:type`
- `og:image`
- `og:url`

Use social metadata for share-preview quality. Do not present it as a guaranteed ranking factor.

## Core Web Vitals / page experience

- Page experience:
  https://developers.google.com/search/docs/appearance/page-experience
- Web Vitals:
  https://web.dev/articles/vitals

Current Core Web Vitals "good" thresholds:
- LCP <= 2.5 s
- INP <= 200 ms
- CLS <= 0.1
typically evaluated at the 75th percentile for field data.

## Usage rule

Always re-check current docs before:
- claiming a rich-result type is supported;
- giving exact Search Console UI steps;
- stating crawler behavior for a newly introduced agent;
- giving AI-search controls/reporting guidance;
- relying on an older schema/SEO checklist.
