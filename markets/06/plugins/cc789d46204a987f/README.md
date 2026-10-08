# Web App QA & Release Copilot Plugin

Version: 0.1.0

A skills-only, evidence-driven QA and release-readiness copilot for web applications.

## What it covers

- functional QA and critical user journeys;
- targeted regression planning;
- bug triage;
- Playwright test generation/review;
- browser, responsive, and visual QA;
- accessibility review;
- performance and Core Web Vitals evidence;
- security/privacy release checks;
- deployment, rollback, smoke, and monitoring readiness;
- final release verdicts.

## Architecture

```text
Web App QA & Release Copilot
└── web-qa-release
    ├── functional QA / user journeys
    ├── browser / responsive / visual testing
    ├── accessibility quality
    ├── web performance
    ├── security / privacy release checks
    └── release readiness / regression
```

No MCP server is required for v0.1.

The package can design and review tests using supplied evidence, but it does not itself open browsers, execute Playwright, run Lighthouse, scan production, deploy releases, or verify live systems.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  web-qa-release/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      functional_qa_user_journey_patterns.md
      browser_responsive_visual_testing.md
      accessibility_web_quality_checklist.md
      web_performance_testing_playbook.md
      web_security_privacy_release_checks.md
      release_readiness_regression_framework.md
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

Review the ZIP and test it with real PRs, screenshots, traces, Playwright failures, Lighthouse reports, and release candidates.

This package has **not** been created, installed, or submitted as a plugin.
