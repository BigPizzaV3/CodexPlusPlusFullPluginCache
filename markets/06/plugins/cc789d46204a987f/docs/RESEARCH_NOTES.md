# Research Notes — Web App QA & Release Copilot

Research date: 2026-09-23

## Recommended name

Keep **Web App QA & Release Copilot**.

It fits OpenAI's current 30-character display-name limit and communicates both halves of the product:
- web application QA;
- release decision / launch validation.

Package: `web-app-qa-release-copilot`
Skill: `web-qa-release`

## Recommended architecture

Use a **skills-only plugin** for v0.1.

The skill is already valuable for:
- inspecting repository/PR/test evidence;
- designing user-journey coverage;
- writing/reviewing Playwright tests;
- triaging bugs;
- scoping regression;
- reviewing accessibility/performance/security evidence;
- producing a justified release verdict.

It does not require its own MCP server to do those tasks.

A later MCP/browser-backed version would make sense only if the plugin should actually:
- navigate a staging site;
- execute Playwright tests;
- collect screenshots/traces;
- run Lighthouse or accessibility scans;
- inspect CI/deployment state;
- trigger approved smoke tests.

Those live actions would require a deliberately bounded tool surface, authorization, target allowlists, and accurate destructive/open-world annotations.

## OpenAI plugin requirements checked

Current OpenAI directory rules include:
- display name <= 30 characters;
- short description <= 30 characters;
- long description <= 4,000 characters;
- <= 20 capabilities, each <= 120 characters;
- <= 3 starter prompts, each <= 128 characters;
- combined `plugin-name:skill-name` <= 64 characters;
- valid `SKILL.md` frontmatter;
- safety/security scans for bundled skills;
- verified publisher identity and policy attestations.

OpenAI's submission flow asks authors to prepare five positive and three negative test cases plus release notes.

Skills-only packages can be submitted without an MCP server.

Primary sources:
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Playwright research

Current Playwright guidance emphasizes:
- user-visible behavior over implementation details;
- isolated tests;
- user-facing locators such as roles/labels;
- auto-waiting and retrying assertions;
- browser/device/environment projects only when the product supports them;
- failure traces as useful debugging evidence.

Trace Viewer can capture actions, DOM snapshots, screenshots, network information, console information, and other context. Playwright recommends trace-on-first-retry as a practical CI pattern rather than tracing every successful run.

Accessibility scans can be integrated with Playwright/axe, but Playwright explicitly warns that automated checks catch only part of the accessibility surface and should be combined with manual assessment.

Sources:
- https://playwright.dev/docs/best-practices
- https://playwright.dev/docs/test-projects
- https://playwright.dev/docs/trace-viewer
- https://playwright.dev/docs/accessibility-testing

## Accessibility research

WCAG 2.2 remains the current W3C Recommendation and organizes accessibility under:
- Perceivable;
- Operable;
- Understandable;
- Robust.

WCAG success criteria are testable, but W3C guidance notes that some checks require manual testing and that usability/inclusive testing remain important beyond automated rules.

The skill therefore must not treat an automated accessibility score or zero axe violations as proof of conformance.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

## Performance research

Current Core Web Vitals remain:
- LCP: good <= 2.5 seconds;
- INP: good <= 200 milliseconds;
- CLS: good <= 0.1;
with the 75th percentile used for field classification.

Lighthouse provides reproducible automated lab audits for performance, accessibility, SEO, and other quality dimensions, and Lighthouse CI can help detect regressions. A Lighthouse result is lab evidence and should not be confused with real-user field performance.

Sources:
- https://developer.chrome.com/docs/lighthouse/overview
- https://web.dev/articles/vitals
- https://web.dev/articles/defining-core-web-vitals-thresholds

## Security research

OWASP describes WSTG as a comprehensive framework and technique reference for web application/security-service testing.

As of late 2026:
- WSTG 4.2 is the current stable release;
- WSTG 5.0 is under active development.

OWASP explicitly recommends tailoring and prioritizing tests to the application and business risk rather than treating the guide as a mechanical checklist.

This supports the skill's release-oriented approach: inspect auth, authorization, sessions, inputs, uploads, APIs, sensitive data, third parties, configuration, and deployment controls according to actual product risk.

Sources:
- https://owasp.org/www-project-web-security-testing-guide/
- https://wstg.owasp.org/v4.2/
- https://wstg.owasp.org/latest/

## Core product decisions

1. Evidence before verdict.
2. User journeys before implementation-detail tests.
3. Target regression to the blast radius instead of defaulting to full regression.
4. Do not claim cross-browser coverage from one browser.
5. Automated accessibility evidence does not prove accessibility.
6. Lighthouse is lab evidence, not production field truth.
7. Security scanners provide evidence, not proof of complete security.
8. Treat visual diffs according to impact and rendering variance, not raw pixel count.
9. Release decisions include deployment, rollback, and post-release monitoring.
10. Never say Ready when a material P0/P1 blocker or essential missing evidence remains.
