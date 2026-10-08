# Research & Writing Copilot Plugin

Version: 0.1.0

A skills-only research-to-publication copilot for source verification, deep technical research, technical writing, documentation, comparisons, fact-checking, Medium, LinkedIn, and publish-ready editing.

## Architecture

```text
Research & Writing Copilot
└── research-writing
    ├── research & source verification
    ├── technical articles / blogs
    ├── documentation / explainers
    ├── comparison reports
    ├── Medium / LinkedIn adapters
    └── fact-check / publish-ready editing
```

No MCP server is required for v0.1.

The plugin can use host-provided research/web/file capabilities when available, but it does not need its own publishing service or external database.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  research-writing/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      research_source_verification.md
      technical_article_blog_patterns.md
      documentation_explainer_patterns.md
      comparison_report_framework.md
      publication_adapters_medium_linkedin.md
      editing_fact_checking_publish_ready.md
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

Review the package with:
- one fresh deep-research article;
- one stale article refresh;
- one comparison report;
- one technical migration guide;
- one Medium/LinkedIn repurposing task.

This package has **not** been created, installed, or submitted as a plugin.
