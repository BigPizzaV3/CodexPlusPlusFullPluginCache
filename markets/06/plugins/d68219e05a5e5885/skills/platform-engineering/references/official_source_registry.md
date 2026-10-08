# Official Source Registry

Research date: 2026-09-23

Use current primary documentation for cloud/runtime/provider-specific behavior.

## OpenAI plugin packaging

- Build skills:
  https://developers.openai.com/plugins/build/skills
- Package plugins:
  https://developers.openai.com/plugins/build/plugins
- Submission:
  https://developers.openai.com/plugins/deploy/submission
- Submission validation:
  https://developers.openai.com/plugins/deploy/submission-errors

## Kubernetes

- Probes:
  https://kubernetes.io/docs/concepts/workloads/pods/probes/
- Configure probes:
  https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
- Resource management:
  https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- Disruptions / PDB:
  https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
- Pod Security Standards:
  https://kubernetes.io/docs/concepts/security/pod-security-standards/

Key durable points:
- startup, liveness, and readiness probes have different purposes;
- PDBs apply to voluntary disruptions, not all failure modes;
- resource requests influence scheduling and capacity;
- use current security policy guidance for workload hardening.

## Terraform / HashiCorp

- Terraform style guide:
  https://developer.hashicorp.com/terraform/language/style
- Plan:
  https://developer.hashicorp.com/terraform/tutorials/cli/plan
- Apply:
  https://developer.hashicorp.com/terraform/cli/commands/apply
- State locking:
  https://developer.hashicorp.com/terraform/language/state/locking

Key durable points:
- format and validate configuration;
- review plans before apply;
- state can contain sensitive data;
- use state locking where supported;
- do not casually disable locking or force-unlock;
- pin versions and protect credentials.

## GitOps / Argo CD

- Argo CD best practices:
  https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/

Current guidance recommends clear separation of application source and configuration where it improves auditability/workflow, and emphasizes immutable Git revisions for declarative delivery.

## SRE

Google SRE:
- SRE book:
  https://sre.google/sre-book/table-of-contents/
- Workbook:
  https://sre.google/workbook/table-of-contents/

Use current SRE guidance for SLOs, error budgets, alerting, incident response, and reliability trade-offs.

## OpenTelemetry

- Documentation:
  https://opentelemetry.io/docs/

OpenTelemetry is a vendor-neutral framework for generating, collecting, and exporting traces, metrics, and logs.

## Platform engineering

CNCF:
- Platform engineering overview:
  https://www.cncf.io/blog/2025/11/19/what-is-platform-engineering/
- Cloud-native IDP / GitOps / supply-chain example:
  https://www.cncf.io/blog/2026/05/29/building-a-cloud-native-internal-developer-platform-with-kubernetes-gitops-and-supply-chain-security/

Platform engineering guidance emphasizes:
- self-service;
- platform-as-product;
- developer experience;
- golden paths/paved roads;
- reducing cognitive load.

## Provider Well-Architected frameworks

AWS:
https://docs.aws.amazon.com/wellarchitected/latest/framework/

Azure:
https://learn.microsoft.com/en-us/azure/well-architected/

Google Cloud:
https://docs.cloud.google.com/architecture/framework

Use provider-specific primary guidance for architecture recommendations.

Common cross-provider themes include:
- operational excellence;
- security;
- reliability;
- performance;
- cost.

AWS and Google Cloud also explicitly include sustainability; provider terminology and implementation details differ.

## Usage rule

Do not claim cross-cloud equivalence where provider services or semantics differ.

Verify current documentation when:
- Kubernetes version matters;
- Terraform/provider behavior matters;
- cloud service limits/features matter;
- IAM/security semantics matter;
- pricing matters;
- platform APIs changed.
