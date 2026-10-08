# Plugin Creator Prompt — Web App QA & Release Copilot

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `web-app-qa-release-copilot`
- Skill: `web-qa-release`
- Display name: `Web App QA & Release Copilot`
- Version: `0.1.0`
- Category: `Developer Tools`

## Architecture

Keep v0.1 **skills-only**.

Do **not** add:
- MCP;
- browser automation;
- live staging-site access;
- CI/CD credentials;
- Lighthouse execution;
- vulnerability scanning;
- deployment actions;
- custom UI.

The skill may design Playwright tests, QA plans, release gates, and verification workflows, but it must not pretend those tests were actually executed.

## Required behavior

Preserve the existing evidence-driven QA workflow:
- inspect available repository/PR/test/screenshots/logs/release evidence first;
- classify findings as observed, automated evidence, source-supported, inferred, or needs verification;
- prioritize severity by user/business impact, likelihood, affected scope, and recoverability;
- map critical user journeys;
- scope targeted regression to the change blast radius;
- create concise reproduction reports;
- design resilient Playwright tests around user-visible behavior;
- distinguish cross-browser coverage from single-browser evidence;
- separate automated accessibility findings from manual verification;
- distinguish lab performance evidence from field evidence;
- use risk-based security/privacy release gates;
- include deployment, rollback, smoke tests, and post-release monitoring;
- use only `Ready`, `Ready with known limitations`, or `Not ready` for final release verdicts;
- never invent test execution, browser coverage, Lighthouse results, security findings, or deployment verification.

## Preserve
- `SKILL.md`
- all reference files
- `agents/openai.yaml`
- branding
- listing material
- research notes
- five positive and three negative test cases

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
10. No MCP/browser execution dependency is added.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
