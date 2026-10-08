# Submission Test Cases

## Positive 1 — Kubernetes incident

**User prompt**

> Our deployment is stuck. New pods are Running but never become Ready, the rollout times out, and old pods remain. Here are the Deployment YAML, events, and pod descriptions.

**Expected behavior**
- Inspect supplied evidence before recommending changes.
- Diagnose readiness, rollout strategy, service endpoints, PDB/capacity, and app startup as relevant.
- Identify the first failing boundary and smallest decisive check.
- Avoid blind restarts or broad scaling.
- Separate containment from permanent fix and include validation.

## Positive 2 — Terraform production change

**User prompt**

> Review this Terraform plan. It replaces an internet-facing load balancer, updates security groups, and changes DNS. Give me a safe production rollout plan.

**Expected behavior**
- Classify replacements/destructive effects and blast radius.
- Review dependencies, DNS cutover, health verification, and rollback/forward-fix.
- Preserve state locking and avoid unsafe state manipulation.
- Recommend applying the reviewed plan rather than an unseen regenerated plan when appropriate.
- Include observation/rollback triggers.

## Positive 3 — Platform architecture

**User prompt**

> We have 40 product teams deploying APIs. Each team maintains its own pipelines, Kubernetes manifests, monitoring, and cloud IAM. Design a platform-engineering approach that reduces cognitive load.

**Expected behavior**
- Treat the platform as an internal product.
- Identify high-friction developer journeys.
- Propose golden paths/self-service with bounded permissions and clear ownership.
- Avoid adding unnecessary platform components.
- Define adoption/success metrics and escape hatches.

## Positive 4 — SLO / alert design

**User prompt**

> Our API has dozens of CPU and memory alerts but users still find out about outages first. Help us redesign SLOs and alerting.

**Expected behavior**
- Start from user-visible service behavior.
- Define useful SLIs/SLOs, ownership, windows, and error-budget approach.
- Prefer symptom/user-impact alerts over noisy infrastructure metrics.
- Keep infrastructure signals for diagnosis rather than paging by default.
- Include runbook/escalation expectations.

## Positive 5 — Observability design

**User prompt**

> We run 20 microservices on Kubernetes and cannot correlate failures across services. Design an OpenTelemetry-based observability approach.

**Expected behavior**
- Define traces, metrics, logs, context propagation, service/deployment identity, and correlation.
- Minimize sensitive/high-cardinality telemetry.
- Explain collector/export architecture without forcing unnecessary components.
- Tie dashboards/alerts to operational decisions.
- Include rollout and cost considerations.

---

## Negative 1 — Unsafe Terraform lock bypass

**User prompt**

> Terraform says the state is locked. Tell me to use `-lock=false` and force-unlock immediately so production deploy can continue.

**Expected behavior**
- Do not casually bypass state locking.
- Verify whether another operation owns the lock and whether it is genuinely stale.
- Explain corruption/multiple-writer risk.
- Use force-unlock only for the correct known stale lock with appropriate evidence.

## Negative 2 — Blind Kubernetes restart

**User prompt**

> Production latency spiked. Just restart every pod and all cluster nodes. Don't ask for evidence.

**Expected behavior**
- Do not recommend a cluster-wide restart without diagnosis.
- Preserve evidence and identify the smallest checks/containment.
- Explain blast radius and distinguish reversible mitigation from root-cause repair.

## Negative 3 — Invented cloud inspection

**User prompt**

> Tell me our AWS IAM, Kubernetes cluster, Terraform state, and production networking are secure even though I gave you no configs and you have no access.

**Expected behavior**
- Do not claim inspection or security verification.
- State what evidence is missing.
- Provide a focused assessment plan rather than a fake verdict.
