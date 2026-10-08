# Search Console and Organic Growth Analysis

## Establish context first

Record:
- property;
- date range;
- comparison period;
- search type;
- country/device;
- query/page filter;
- brand/non-brand method if used;
- known releases/migrations.

## Core dimensions

Analyze:
- clicks;
- impressions;
- CTR;
- average position;
- page;
- query;
- device;
- country;
- search appearance.

Do not treat average position alone as success.

## Reporting caveats

Search Console tables may not equal chart totals because of:
- anonymized queries;
- table row limits;
- aggregation differences;
- filtering;
- data processing.

Current Google guidance notes Search Console data can lag and may differ from analytics systems because of privacy, processing, time zones, and measurement method.

## Diagnostic patterns

### Impressions down + position stable
Check:
- demand/seasonality;
- query mix;
- page eligibility;
- SERP/search-feature changes;
- filters;
- geographic/device mix.

Do not conclude "penalty" without evidence.

### Impressions stable + clicks down
Check:
- CTR;
- title/snippet;
- competing result features;
- intent mismatch;
- brand/search appearance changes.

### Page impressions move between URLs
Check:
- canonicalization;
- cannibalization;
- redirects;
- query-intent split;
- site restructuring.

### New content has zero impressions
Check:
- indexability;
- indexing status;
- internal discovery;
- sitemap;
- actual demand/intent;
- time since publishing.

## Page cohorts

Group pages by:
- template;
- topic;
- publish month;
- update month;
- product vs editorial;
- programmatic family;
- indexability status.

Cohorts are more useful than one-site aggregate when diagnosing template changes.

## Query opportunity types

- high impressions / low CTR;
- rankings with clear intent mismatch;
- queries split across competing pages;
- near-win queries with a relevant page;
- emerging queries where product/content already solves the need;
- branded queries;
- non-branded discovery.

Do not invent search volume from Search Console impressions.

## AI-generative Search reporting

As of late 2026, Google Search Console has introduced reporting for generative-AI Search visibility and controls for inclusion in AI features.

When available, separate:
- traditional Search performance;
- generative-AI impressions/pages;
- device/country;
- overall organic conversions.

Do not treat AI-feature impressions as equivalent to clicks or conversions.

## Causality

For before/after changes consider:
- seasonality;
- algorithm/search-feature changes;
- competitor changes;
- demand;
- site releases;
- migrations;
- index churn;
- measurement/filter changes.

Use "consistent with" unless a controlled test or strong evidence supports causality.
