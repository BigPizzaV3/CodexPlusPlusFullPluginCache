# Research Notes — Platform Engineering Copilot

Research date: 2026-09-23

## Recommended public name

Use **Platform Engineering Copilot**.

This is cleaner than “Cloud / Platform Engineering Copilot” and keeps the product centered on the broader discipline rather than a slash-separated feature list.

Cloud architecture remains a major capability inside the plugin.

Package: `cloud-platform-engineering-copilot`
Skill: `platform-engineering`

## Recommended architecture

Use a **skills-only plugin** for v0.1.

The first release can already help with:
- architecture;
- Kubernetes manifests and incidents;
- Terraform plans;
- CI/CD and GitOps;
- IAM/security review;
- SLOs and error budgets;
- observability;
- developer-platform design;
- production change safety.

No live cloud access is required for these workflows.

A future MCP-backed release would make sense only for deliberately controlled read/action capabilities such as:
- reading Kubernetes resources/events;
- reading cloud inventory/metrics;
- reading Terraform plan/state metadata;
- querying CI/CD runs;
- reading observability signals;
- executing approved deployment or rollback operations.

Any write-capable infrastructure tool surface would require strict authorization, least privilege, accurate destructive/open-world annotations, target scoping, approval controls, and strong auditability.

## OpenAI plugin requirements

Current final-directory limits include:
- display name <= 30 characters;
- short description <= 30 characters;
- long description <= 4,000 characters;
- <= 20 capabilities, each <= 120 characters;
- <= 3 starter prompts, each <= 128 characters;
- combined `plugin-name:skill-name` <= 64 characters;
- required skill frontmatter;
- bundled skill security/safety scans;
- verified publisher identity and policy attestations.

Skills-only packages can omit remote MCP requirements.

Primary source:
https://developers.openai.com/plugins/deploy/submission-errors

## Platform engineering

Current CNCF platform-engineering guidance emphasizes:
- platform as a product;
- developers as platform customers;
- self-service;
- standardized tools/services;
- golden paths / paved roads;
- reducing cognitive load;
- collaboration across development, operations, security, and product.

Recent CNCF cloud-native platform examples combine IaC, GitOps, Kubernetes, security, and operational consistency.

Sources:
- https://www.cncf.io/blog/2025/11/19/what-is-platform-engineering/
- https://www.cncf.io/blog/2026/05/29/building-a-cloud-native-internal-developer-platform-with-kubernetes-gitops-and-supply-chain-security/

## Kubernetes

Current Kubernetes documentation clearly distinguishes:
- startup probes: has the application started?
- readiness probes: should the pod receive service traffic?
- liveness probes: should the container be restarted?

The plugin should not conflate those signals.

PodDisruptionBudgets constrain voluntary disruptions, not all availability failures.

Current Pod Security Standards define:
- Privileged;
- Baseline;
- Restricted.

Use provider/runtime/version-specific docs before hardcoding security or behavior assumptions.

Sources:
- https://kubernetes.io/docs/concepts/workloads/pods/probes/
- https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
- https://kubernetes.io/docs/concepts/security/pod-security-standards/

## Terraform

Current HashiCorp guidance emphasizes:
- `terraform fmt` and `terraform validate`;
- reviewing a plan before apply;
- protecting state because it can contain sensitive information;
- not committing state files;
- pinning versions;
- keeping state locking enabled;
- using force-unlock very carefully.

HashiCorp explicitly describes `-lock=false` as dangerous because it permits concurrent writers.

Sources:
- https://developer.hashicorp.com/terraform/language/style
- https://developer.hashicorp.com/terraform/tutorials/cli/plan
- https://developer.hashicorp.com/terraform/cli/commands/apply
- https://developer.hashicorp.com/terraform/language/state/locking

## GitOps

Current Argo CD best-practice guidance recommends separating configuration and source repositories in workflows where this improves audit history and independent configuration changes, and emphasizes immutable Git revisions.

Source:
https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/

## Observability

OpenTelemetry remains a vendor-neutral framework for traces, metrics, and logs, with broad ecosystem support.

This supports the plugin's default of designing telemetry around correlation and operational questions rather than a specific backend.

Source:
https://opentelemetry.io/docs/

## Cloud Well-Architected research

AWS current Well-Architected pillars:
- Operational Excellence;
- Security;
- Reliability;
- Performance Efficiency;
- Cost Optimization;
- Sustainability.

Azure:
- Reliability;
- Security;
- Cost Optimization;
- Operational Excellence;
- Performance Efficiency.

Google Cloud:
- Operational Excellence;
- Security/Privacy/Compliance;
- Reliability;
- Cost Optimization;
- Performance Optimization;
- Sustainability.

All three emphasize trade-offs rather than a single universally optimal architecture.

Sources:
- https://docs.aws.amazon.com/wellarchitected/latest/framework/
- https://learn.microsoft.com/en-us/azure/well-architected/
- https://docs.cloud.google.com/architecture/framework

## Core product decisions

1. Do not default to Kubernetes.
2. Do not default to multi-cloud.
3. Treat platform engineering as a product discipline, not a tooling shopping list.
4. Prefer declarative, reviewable, reversible change.
5. Keep Terraform state and locking safe.
6. Diagnose Kubernetes at the first failing boundary.
7. Use SLOs/error budgets for user-visible reliability decisions.
8. Build observability to answer operational questions.
9. Treat identity and secrets as real platform boundaries.
10. Every high-risk production change needs blast-radius, rollback, and validation thinking.
