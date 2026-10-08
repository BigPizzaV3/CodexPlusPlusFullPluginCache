# SEO & Growth Copilot Plugin

Version: 0.1.0

A skills-only technical SEO and organic-growth copilot for indexing, Search Console analysis, sitemaps, robots, canonicals, structured data, internal linking, metadata/social previews, content gaps, programmatic SEO, AI-search visibility, and measurement.

## Architecture

```text
SEO & Growth Copilot
└── seo-growth
    ├── technical SEO / indexing
    ├── Search Console analysis
    ├── metadata / social / search appearance
    ├── structured data
    ├── internal linking / content architecture
    ├── content gaps / programmatic SEO
    ├── AI-search visibility
    └── organic-growth measurement
```

No MCP server is required for v0.1.

The plugin can analyze user-provided site/code/Search Console/crawl evidence and use host-provided web/file/code capabilities, but it does not directly connect to Search Console, Analytics, CMSs, or site crawlers.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  seo-growth/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      technical_seo_indexing_framework.md
      search_console_growth_analysis.md
      metadata_social_search_appearance.md
      structured_data_schema_workflow.md
      internal_linking_content_architecture.md
      content_gap_programmatic_seo.md
      organic_growth_measurement.md
      ai_search_visibility_2026.md
      official_source_registry.md
submission/
  listing-and-prompts.md
  test-cases.md
  public-submission-checklist.md
  release-notes.md
docs/
  RESEARCH_NOTES.md
PLUGIN_CREATOR_PROMPT.md
README.md
```

## Recommended next step

Test the package with:
- one indexing failure;
- one Search Console traffic drop;
- one structured-data audit;
- one programmatic SEO project;
- one metadata/internal-linking/growth audit.

This package has **not** been created, installed, or submitted as a plugin.
