# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/` is at the ZIP root.
- [ ] `skills/web-qa-release/SKILL.md` starts with valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and references only in-package assets.
- [ ] Branding assets are square, text-free, and production-ready.
- [ ] No private test credentials, staging secrets, production logs, customer data, or internal URLs are bundled.

## Listing
- [ ] Display name is at most 30 characters.
- [ ] Subtitle is at most 30 characters.
- [ ] Long description is at most 4,000 characters.
- [ ] At most 20 capabilities, each at most 120 characters.
- [ ] At most 3 starter prompts, each at most 128 characters.
- [ ] Category is `Developer Tools`.
- [ ] Publisher identity matches the verified OpenAI Platform identity.

## Behavior
- [ ] Test full release-audit workflow.
- [ ] Test targeted regression scoping.
- [ ] Test Playwright generation/review.
- [ ] Test accessibility evidence handling.
- [ ] Test performance-regression analysis.
- [ ] Verify the skill never claims browser/device/security/deployment tests ran without evidence.
- [ ] Verify release verdicts are tied to blockers, evidence, known limitations, and rollback/monitoring.

## Review
- [ ] Review five positive and three negative test cases.
- [ ] Add/update release notes.
- [ ] Complete region availability and policy attestations.
- [ ] Wait for bundled-skill safety/security scans.

## Scope
Version 0.1.0 is skills-only. It can analyze user-provided repository/test/release evidence and create test plans or test code, but it does not automatically open a browser, execute Playwright, scan a live site, deploy, or approve a release by itself.
