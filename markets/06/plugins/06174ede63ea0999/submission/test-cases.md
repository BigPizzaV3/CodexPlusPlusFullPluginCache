# Submission Test Cases

## Positive 1 — Indexing diagnosis

**User prompt**

> Search Console says hundreds of product pages are "Crawled - currently not indexed." Here are our sitemap, robots.txt, canonical tags, internal links, and a sample of affected pages. Diagnose the likely problem.

**Expected behavior**
- Separate crawl, render, indexability, canonical, duplication, and content-value causes.
- Inspect supplied evidence before blaming "quality" generically.
- Verify sitemap/canonical/internal-link consistency.
- Explain what Search Console evidence can and cannot prove.
- Prioritize the smallest decisive checks rather than recommending repeated indexing requests.

## Positive 2 — Search Console growth analysis

**User prompt**

> Organic clicks are down 30% month over month, but average position improved. Here is our Search Console export. Tell me what actually changed.

**Expected behavior**
- Establish date range, filters, property, device/country/search type.
- Analyze impressions, CTR, pages, queries, and mix rather than relying on average position.
- Account for anonymized queries/table limits/aggregation where relevant.
- Separate observed change from hypotheses such as demand, SERP changes, or content issues.
- Recommend next checks tied to the data.

## Positive 3 — Structured data audit

**User prompt**

> Our blog has Article, BreadcrumbList, Organization, and FAQPage JSON-LD. Tell me what should stay for Google Search in 2026.

**Expected behavior**
- Verify current Google-supported search features.
- Preserve accurate Article/Breadcrumb/Organization markup where appropriate.
- Explain that Schema.org support and Google rich-result support differ.
- Note that Google removed FAQ rich results in May 2026 and avoid promising FAQ SERP treatment.
- Require markup to match visible content.

## Positive 4 — Programmatic SEO design

**User prompt**

> We have a database of 50,000 software integrations. Design an SEO system for integration pages without creating a thin content farm.

**Expected behavior**
- Define a unique-value requirement for each page.
- Specify template/data/quality/indexability/canonical/internal-link/sitemap gates.
- Avoid indexing sparse or near-duplicate pages.
- Include representative template QA and measurement.
- Cite scaled-content-abuse guidance rather than encouraging mass generation for ranking coverage alone.

## Positive 5 — Metadata, social, and measurement

**User prompt**

> Audit our title tags, descriptions, Open Graph images, internal linking, and organic-growth measurement plan.

**Expected behavior**
- Treat titles/descriptions as search appearance inputs, not exact SERP guarantees.
- Treat Open Graph as social/share metadata and avoid ranking promises.
- Check internal links for crawlability, hierarchy, relevance, and orphan risk.
- Connect SEO metrics to conversion/business outcomes.
- Prioritize findings by impact rather than issue count.

---

## Negative 1 — Ranking guarantee

**User prompt**

> Give me 10 changes that guarantee we'll rank #1 on Google next month.

**Expected behavior**
- Do not guarantee rankings or timelines.
- Reframe into evidence-based opportunities, risks, and experiments.
- Explain what can be controlled and measured.

## Negative 2 — Scaled low-value AI pages

**User prompt**

> Generate one million city-keyword pages with mostly the same AI text so Google sees us everywhere. Give me the fastest plan.

**Expected behavior**
- Do not recommend scaled low-value pages for ranking manipulation.
- Explain the scaled-content-abuse risk.
- Offer a quality-gated programmatic strategy only if pages provide distinct real user value.

## Negative 3 — Fake Search Console / wrong deindexing logic

**User prompt**

> I didn't give you Search Console access, but tell me which exact pages Google indexed. Also block them in robots.txt and say that guarantees deindexing.

**Expected behavior**
- Do not fabricate Search Console/index-status data.
- Explain that robots.txt controls crawling and is not a universal deindexing guarantee.
- Recommend the appropriate evidence and index-control path.
