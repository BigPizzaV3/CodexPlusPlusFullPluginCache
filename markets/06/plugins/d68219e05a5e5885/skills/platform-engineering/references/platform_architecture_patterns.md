# Platform Architecture Patterns

## 1. Managed cloud workload

Use managed compute/platform services when:
- platform operations are not a differentiator;
- workload requirements fit the managed service;
- team size/skills favor lower operational burden.

Evaluate:
- availability model;
- deployment;
- scaling;
- identity;
- networking;
- observability;
- data;
- lock-in;
- cost.

Do not choose Kubernetes merely to host a few ordinary stateless services.

## 2. Kubernetes application platform

Use when Kubernetes solves concrete needs such as:
- many independently deployed workloads;
- standardized runtime/deployment model;
- workload portability requirements;
- advanced scheduling;
- shared platform capabilities;
- ecosystem/operator needs.

Define:
- cluster ownership;
- namespaces/tenancy;
- ingress/gateway;
- DNS;
- workload identity;
- secrets;
- policy/admission;
- observability;
- upgrades;
- node lifecycle;
- backup/recovery;
- capacity;
- cost allocation.

## 3. Platform-as-product / IDP

Flow:

`developer intent → approved template/golden path → platform orchestration → infrastructure/runtime → observability`

Platform product should expose:
- safe self-service;
- clear defaults;
- ownership;
- lifecycle;
- documentation;
- escape hatch;
- feedback loop.

Do not mistake a portal for a platform.

## 4. GitOps delivery

Flow:

`application/config change → review → Git desired state → reconciler → runtime`

Useful when:
- declarative reconciliation creates value;
- auditability matters;
- environment config is managed through Git.

Account for:
- secret strategy;
- drift;
- emergency changes;
- repository structure;
- promotion;
- rollback;
- controller availability/security.

## 5. Multi-region

Use only when availability/RTO/RPO justify it.

Define:
- active-active vs active-passive;
- traffic steering;
- state/data replication;
- consistency;
- failover;
- failback;
- observability;
- testing.

Untested failover is not a recovery strategy.

## 6. Multi-cloud

Reasons may include:
- regulatory constraints;
- acquisition/organizational reality;
- hard dependency requirements;
- contractual resilience requirements.

Avoid multi-cloud as a vague anti-lock-in goal when the extra operating model is not funded.

## Architecture decision format

**Recommendation**
**Requirements**
**Failure domains**
**Security boundaries**
**Operations**
**Developer experience**
**Cost**
**Trade-offs**
**What would invalidate this design**
**Validation plan**
