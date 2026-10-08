# Plugin Creator Prompt — SEO & Growth Copilot

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `seo-website-growth-copilot`
- Skill: `seo-growth`
- Display name: `SEO & Growth Copilot`
- Version: `0.1.0`
- Category: `Productivity`

## Product definition

This is an evidence-driven technical SEO and organic-growth copilot.

It supports:
- crawling/indexing diagnosis;
- Search Console analysis;
- sitemaps/robots/canonicals/redirects;
- metadata and search appearance;
- Open Graph/social previews;
- structured data;
- internal linking;
- content gaps;
- programmatic SEO;
- AI-search visibility;
- organic-growth measurement.

It must separate crawl, render, index, rank, click, and conversion problems rather than producing generic SEO checklists.

## Architecture

Keep v0.1 **skills-only**.

Do **not** add:
- MCP;
- Search Console authentication;
- Analytics authentication;
- CMS actions;
- crawler infrastructure;
- automatic page publishing;
- custom UI.

The skill may use host-provided web, file, code, and analysis capabilities.

## Required behavior

Preserve:
- first-failing-layer diagnosis;
- observed vs inferred evidence labels;
- robots.txt vs noindex distinction;
- canonical as signal/preference rather than guarantee;
- sitemap does not guarantee indexing;
- Search Console reporting caveats;
- title/snippet rewriting uncertainty;
- Open Graph as social/share metadata, not a ranking promise;
- Schema.org vs Google rich-result eligibility distinction;
- no fabricated schema properties;
- internal-linking relevance and crawlability;
- programmatic SEO quality/index gates;
- Google's scaled-content-abuse safeguards;
- current AI-search guidance;
- no Google SEO claim for llms.txt;
- no outdated FAQ rich-result recommendation;
- organic growth tied to downstream outcomes;
- no ranking guarantees or fake keyword/search-volume data.

## Preserve
- `SKILL.md`
- all reference files
- `agents/openai.yaml`
- branding
- listing material
- research notes
- five positive and three negative tests

## Validate
1. ZIP root and `plugin.json`.
2. `skills: "./skills/"`.
3. Skill frontmatter.
4. Combined plugin/skill identity <= 64 characters.
5. `agents/openai.yaml`.
6. Asset paths stay inside the package.
7. Public listing field limits.
8. Three starter prompts.
9. Five positive and three negative submission tests.
10. No MCP/live Search Console/Analytics dependency.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
