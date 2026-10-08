# Research Notes — SEO & Growth Copilot

Research date: 2026-09-23

## Recommended public name

Use **SEO & Growth Copilot**.

The original idea, “SEO & Website Growth Copilot,” is clear but slightly longer. “SEO & Growth Copilot” keeps the same meaning, is easier to scan in the plugin directory, and still covers the website-growth layer beyond narrow on-page SEO.

Package: `seo-website-growth-copilot`
Skill: `seo-growth`

Subtitle: **Grow organic search visibility**

## Product definition

This should be a **technical SEO + organic growth system**, not merely a metadata generator.

The workflow should diagnose:

`crawl → render → index → canonicalize → rank → impression → click → engage → convert`

That prevents common bad advice such as treating every traffic drop as a title-tag problem.

Primary use cases:
- technical SEO audit;
- Search Console analysis;
- indexing troubleshooting;
- sitemap / robots;
- canonicalization / redirects;
- structured data;
- internal linking;
- content gaps;
- metadata / OG / social previews;
- programmatic SEO;
- AI-search visibility;
- organic-growth measurement.

## Architecture

Use a **skills-only plugin** for v0.1.

The first version does not need an MCP server because much of the value is:
- interpreting site/repository evidence;
- reviewing HTML/configuration;
- analyzing exported Search Console data;
- researching current search documentation;
- designing SEO architecture;
- writing implementation guidance.

A future MCP-backed version would make sense for:
- Google Search Console Search Analytics;
- URL Inspection;
- sitemap status;
- GA4 conversion data;
- a site crawler;
- CMS content inventory;
- deployment/verification tooling.

Any integration should begin read-only. Write/publish actions should be explicit and separately permissioned.

## OpenAI plugin requirements

Current public plugin packaging supports skills-only plugins.

Current metadata limits include:
- display name <= 30 characters;
- short description <= 30 characters;
- long description <= 4,000 characters;
- <= 20 capabilities, each <= 120 characters;
- <= 3 starter prompts, each <= 128 characters;
- combined plugin/skill identity <= 64 characters.

Sources:
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Google 2026 changes that matter

Google's 2026 Search documentation contains several updates that older SEO checklists can easily miss.

### FAQ rich results

Google removed FAQ rich-result support from Search in May 2026.

Product implication:
- do not recommend `FAQPage` merely to obtain a Google FAQ SERP treatment;
- FAQ content can still serve users;
- Schema.org semantics and other consumers are separate questions.

### llms.txt

Google clarified in June 2026 that `llms.txt`:
- is not required for Google Search;
- does not positively or negatively affect Google Search visibility or rankings.

Product implication:
do not sell `llms.txt` as a Google SEO/GEO ranking tactic.

### AI Search guidance

Google added a dedicated generative-AI Search optimization guide in May 2026 and says ordinary SEO fundamentals remain relevant to AI Overviews/AI Mode because those experiences use Google's ranking/quality systems.

Product implication:
avoid unsupported “GEO hacks.” Focus on original value, crawlability, clarity, strong media, structured data, page experience, and entity/source transparency.

### Search Console AI reporting/control

By August 31, 2026, Google documented global rollout of:
- Search generative-AI inclusion controls;
- generative-AI Search performance insights.

Account/property visibility and data sufficiency can still affect what users see.

Product implication:
the plugin can analyze this data when supplied, but must verify current Search Console behavior before exact account-level instructions.

Sources:
- https://developers.google.com/search/updates
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://support.google.com/webmasters/answer/16908024
- https://support.google.com/webmasters/answer/16984139

## Crawl and indexing research

Current Google crawler guidance emphasizes:
- robots.txt controls crawling;
- a blocked URL may still be known/indexed as a URL without content/snippet;
- `noindex` is an indexing directive that generally must be crawled to be processed;
- `crawl-delay` is not supported by Google;
- sitemap declarations help discovery but do not guarantee indexation;
- canonical hints are signals, not absolute commands.

Sources:
- https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec
- https://developers.google.com/search/docs/crawling-indexing/block-indexing
- https://developers.google.com/search/docs/crawling-indexing/canonicalization
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap

## Structured data research

Google recommends:
1. use supported/accurate markup;
2. validate it;
3. deploy representative pages;
4. inspect live URLs;
5. monitor Search Console.

Schema.org vocabulary support is broader than Google's current rich-result feature support.

A valid schema does not guarantee a rich result.

Sources:
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- https://schema.org/

## Search Console interpretation

Google documents that Search Console Performance data may differ between charts/tables and from analytics because of:
- aggregation;
- table limits;
- anonymized queries;
- privacy;
- processing;
- lag;
- time zones.

Product implication:
never use a table export as though it were the complete universe of query data.

Source:
- https://support.google.com/webmasters/answer/17010575

## Open Graph / social

The Open Graph protocol defines core social metadata such as:
- `og:title`;
- `og:type`;
- `og:image`;
- `og:url`.

Google's March 2026 Search documentation update also clarified that `og:image` can be one input for preferred image selection in Search/Discover.

Product implication:
Open Graph is useful for social/share presentation and sometimes image selection signals, but should not be described as a guaranteed ranking lever.

Sources:
- https://ogp.me/
- https://developers.google.com/search/updates

## Programmatic SEO

Google's scaled-content-abuse policy targets large amounts of unoriginal low-value content generated primarily to manipulate Search, regardless of whether it is made with generative AI, scraping, or other automation.

Product implication:
programmatic SEO requires:
- distinct user intent;
- unique value/data/functionality;
- template quality gates;
- duplication controls;
- index/noindex rules;
- internal discovery;
- measurement.

Source:
- https://developers.google.com/search/docs/essentials/spam-policies

## Measurement

The plugin should measure:
- indexable inventory;
- indexed/canonicalized inventory;
- impressions;
- clicks;
- CTR;
- landing-page engagement;
- activation/conversion;
- retention/revenue when available.

Do not define success as:
- 100% sitemap indexing;
- more pages;
- more impressions alone;
- a higher average position without clicks/business impact.

## Existing strategy incorporated

The user's existing SEO strategy already contains strong guardrails around:
- not indexing every generated page;
- canonical/sitemap/robots alignment;
- programmatic SEO quality gating;
- product-led SEO;
- AI-search fundamentals;
- measuring organic acquisition through downstream activation.

This plugin generalizes those ideas into a reusable website-agnostic workflow.
