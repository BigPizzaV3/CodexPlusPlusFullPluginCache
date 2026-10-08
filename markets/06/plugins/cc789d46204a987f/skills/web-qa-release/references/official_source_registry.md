# Official Source Registry

Research date: 2026-09-23

Use current primary documentation whenever QA guidance depends on browser tooling, accessibility criteria, performance metrics, security-testing methodology, or plugin packaging rules.

## OpenAI plugin packaging

- Plugins overview:
  https://developers.openai.com/plugins
- Build skills:
  https://developers.openai.com/plugins/build/skills
- Package plugins:
  https://developers.openai.com/plugins/build/plugins
- Submit plugins:
  https://developers.openai.com/plugins/deploy/submission
- Submission validation:
  https://developers.openai.com/plugins/deploy/submission-errors

Skills-only plugins can package reusable QA workflows without an MCP server.

## Playwright

Primary documentation:
- Best practices:
  https://playwright.dev/docs/best-practices
- Locators:
  https://playwright.dev/docs/locators
- Assertions:
  https://playwright.dev/docs/test-assertions
- Auto-waiting/actionability:
  https://playwright.dev/docs/actionability
- Projects / cross-browser configurations:
  https://playwright.dev/docs/test-projects
- Trace Viewer:
  https://playwright.dev/docs/trace-viewer
- Accessibility testing:
  https://playwright.dev/docs/accessibility-testing

Durable guidance:
- test user-visible behavior rather than implementation details;
- keep tests isolated;
- prefer user-facing resilient locators;
- prefer auto-retrying web assertions over arbitrary sleeps;
- use projects for required browser/device/environment matrices;
- collect traces for useful CI failure diagnosis;
- automated accessibility scans catch only part of the accessibility surface.

## WCAG

W3C WCAG 2.2:
- Understanding WCAG 2.2:
  https://www.w3.org/WAI/WCAG22/Understanding/
- What's new in WCAG 2.2:
  https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

WCAG 2.2 is organized around Perceivable, Operable, Understandable, and Robust requirements. Automated testing cannot establish complete accessibility conformance; manual testing remains necessary for many criteria and real task completion.

## Lighthouse and Core Web Vitals

- Lighthouse overview:
  https://developer.chrome.com/docs/lighthouse/overview
- Web Vitals:
  https://web.dev/articles/vitals
- Core Web Vitals threshold methodology:
  https://web.dev/articles/defining-core-web-vitals-thresholds

Current Core Web Vitals use:
- LCP <= 2.5 s for "good";
- INP <= 200 ms for "good";
- CLS <= 0.1 for "good";
evaluated at the 75th percentile for field classification.

Lighthouse is useful automated lab evidence, not proof that real-user production performance is solved. Compare lab results in equivalent environments and use field evidence such as RUM/CrUX when available.

## OWASP

- OWASP Web Security Testing Guide project:
  https://owasp.org/www-project-web-security-testing-guide/
- Stable WSTG:
  https://wstg.owasp.org/v4.2/
- Latest development guidance:
  https://wstg.owasp.org/latest/

As of late 2026, OWASP lists WSTG 4.2 as the current stable version while 5.0 is under development.

Use WSTG as a risk-based methodology and technique reference, not a mechanical checklist. Security testing should be scoped to the application's actual attack surface, threat model, data, and release risk.

## Usage rule

This file is a source registry, not frozen truth.

Verify current documentation when:
- browser/tool APIs changed;
- a WCAG criterion or conformance claim matters;
- exact Core Web Vitals thresholds matter;
- Playwright configuration/version affects code;
- security-testing guidance affects a release decision.
