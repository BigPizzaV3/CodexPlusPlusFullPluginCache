# Platform Engineering Copilot Plugin

Version: 0.1.0

A skills-only cloud and platform-engineering copilot for architecture, Kubernetes, IaC, CI/CD, GitOps, SRE, observability, security, and internal developer platforms.

## Architecture

```text
Platform Engineering Copilot
└── platform-engineering
    ├── platform architecture
    ├── Kubernetes operations
    ├── Terraform / IaC safety
    ├── CI/CD / GitOps
    ├── SRE / reliability / incidents
    ├── observability
    └── internal developer platforms
```

No MCP server is required for v0.1.

This plugin can review supplied configs, plans, logs, diagrams, and incident evidence, but it cannot inspect cloud accounts, run kubectl/Terraform, change IAM/networking, deploy workloads, or verify live infrastructure by itself.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  platform-engineering/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      platform_architecture_patterns.md
      kubernetes_operations_and_debugging.md
      terraform_iac_change_safety.md
      delivery_gitops_patterns.md
      sre_reliability_incident_patterns.md
      observability_telemetry_patterns.md
      internal_developer_platform_patterns.md
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

Review the package with real architecture diagrams, Kubernetes manifests/events, Terraform plans, pipelines, SLOs, and incident examples.

This package has **not** been created, installed, or submitted as a plugin.
