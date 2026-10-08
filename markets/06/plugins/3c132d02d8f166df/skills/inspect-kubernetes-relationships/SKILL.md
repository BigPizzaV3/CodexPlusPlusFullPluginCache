---
name: inspect-kubernetes-relationships
description: Review supplied local Kubernetes YAML with Nexo YAML Iron when the user needs established Service, Deployment, or Ingress relationship findings and explicit uncertainty. Use detailed inspection only when deeper evidence is needed. Do not use it as evidence of live cluster state, Helm output, policy compliance, or runtime health.
---

# Review Kubernetes Relationships

Use the bundled executable at `${PLUGIN_ROOT}/scripts/nexo-yaml-iron` as the authoritative analyzer. Codex may explain Nexo's structured result but must not compute, fill, relabel, or replace Nexo state from intuition.

## Run the review

For a supplied local manifest path, run:

```bash
"${PLUGIN_ROOT}/scripts/nexo-yaml-iron" review <path>
```

Treat this bounded Review result as the primary product-facing output. Preserve Nexo’s distinction between established findings and explicit unknowns. Do not infer a missing finding, fill an unknown, or reconstruct a different relationship state from intuition.

The current implementation supports Kubernetes Service, Deployment, and Ingress. Report other kinds as outside current coverage instead of treating their absence from the result as success.

## Use detailed inspection only when needed

When the user needs the underlying machine evidence or a deeper diagnostic view, run:

```bash
"${PLUGIN_ROOT}/scripts/nexo-yaml-iron" inspect <path> --format json
```

Use `--format ndjson` only when row-oriented output is specifically useful. Add `--snapshot`, `--partition`, or `--namespace` only when the user supplies or needs those artifact coordinates. These labels describe the report; they do not establish live cluster state.

## Present the result

For Review output:

- present Nexo's established findings as findings;
- present Nexo's unresolved evidence as explicit unknowns;
- keep canonical subjects and identifiers attached to the explanation;
- do not convert an unknown into a negative finding or downgrade an established mismatch because unrelated evidence is unknown.

If detailed `inspect` evidence is used, keep source keys, namespace context, relationship cases, and gap cases attached to the explanation. `No reported finding` is not proof that a deployment is safe, complete, policy-compliant, or healthy.

## Boundaries

- Do not connect to a cluster, read kubeconfig, call cloud APIs, render Helm, apply manifests, mutate YAML, or claim runtime observation.
- Do not present Nexo as a generic YAML linter, admission controller, security scanner, or auto-fixer.
- If the user asks for edits or deployment actions after Review or inspection, treat that as a separate task and authorization boundary.
- If the executable fails or returns an error object, report the failure and preserve the original input rather than guessing a result.
