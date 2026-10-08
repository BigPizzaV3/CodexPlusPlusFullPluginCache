# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/platform-engineering/SKILL.md` has valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and uses only in-package assets.
- [ ] Branding assets are valid, square, and text-free.
- [ ] No cloud credentials, kubeconfigs, Terraform state, secrets, production URLs, or customer data are bundled.

## Listing
- [ ] Display name is at most 30 characters.
- [ ] Subtitle is at most 30 characters.
- [ ] Long description is at most 4,000 characters.
- [ ] At most 20 capabilities, each at most 120 characters.
- [ ] At most 3 starter prompts, each at most 128 characters.
- [ ] Category is `Developer Tools`.
- [ ] Publisher identity matches the verified OpenAI Platform identity.

## Behavior
- [ ] Test Kubernetes incident workflow.
- [ ] Test Terraform plan/release-safety workflow.
- [ ] Test platform-as-product architecture.
- [ ] Test SLO/error-budget/alerting design.
- [ ] Test observability architecture.
- [ ] Verify no fake cloud/cluster/IaC inspection claims.
- [ ] Verify destructive/high-blast-radius changes require scope, evidence, rollback, and validation.

## Review
- [ ] Review five positive and three negative test cases.
- [ ] Add/update release notes.
- [ ] Complete availability and policy attestations.
- [ ] Wait for bundled-skill safety/security scans.

## Scope
Version 0.1.0 is skills-only. It can design and review platform architecture, manifests, Terraform, pipelines, telemetry, and incident evidence, but it does not log into cloud accounts, execute kubectl/Terraform, modify infrastructure, or deploy workloads by itself.
