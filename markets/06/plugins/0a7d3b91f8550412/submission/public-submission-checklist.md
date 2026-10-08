# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/` is at the ZIP root.
- [ ] `skills/data-engineering/SKILL.md` starts with valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and references only in-package assets.
- [ ] Logo and composer icon are square supported images.
- [ ] No credentials, production data, private logs, or user-specific secrets are bundled.

## Listing
- [ ] Display name is 30 characters or fewer.
- [ ] Subtitle is 30 characters or fewer.
- [ ] Long description is 4,000 characters or fewer.
- [ ] At most 20 capabilities; each 120 characters or fewer.
- [ ] At most 3 starter prompts; each 128 characters or fewer.
- [ ] Category is `Data & Analytics`.
- [ ] Developer identity matches the verified OpenAI Platform identity.

## Review material
- [ ] Review five positive test cases.
- [ ] Review three negative test cases.
- [ ] Add/update release notes.
- [ ] Complete availability and policy attestations.
- [ ] Wait for bundled skill safety/security scans.

## Scope
Version 0.1.0 is skills-only. It does not inspect a live Spark/Databricks/Airflow environment, execute SQL/jobs, delete checkpoints, run backfills, or modify external systems unless a future tool integration is explicitly added.
