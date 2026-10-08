# Expert role registry

Select only roles that materially change the work. Extend the registry only for a reusable capability class, not for one project or technology label.

## Product and strategy

- `EXECUTIVE_PRODUCT_DIRECTOR` — product outcomes, product coherence, scope and value framing.
- `PRINCIPAL_PRODUCT_STRATEGIST` — market, user, positioning, and product trade-offs.
- `PRODUCT_SYSTEMS_ARCHITECT` — product model, capability relationships, and system behavior.
- `DOMAIN_STRATEGY_SPECIALIST` — domain-specific constraints and evidence.

## Software architecture

- `PRINCIPAL_SOFTWARE_ARCHITECT` — system boundaries, architecture contracts, and major trade-offs.
- `DISTRIBUTED_SYSTEMS_ARCHITECT` — distribution, consistency, resilience, and scale.
- `CLOUD_ARCHITECT` — cloud topology, deployment, and managed-service boundaries.
- `INTEGRATION_ARCHITECT` — interfaces, external systems, events, and compatibility.
- `DATA_ARCHITECT` — data ownership, lifecycle, lineage, and schemas.

## Engineering

- `PRINCIPAL_FRONTEND_ENGINEER`, `PRINCIPAL_BACKEND_ENGINEER`, `PRINCIPAL_FULL_STACK_ENGINEER`.
- `API_ARCHITECT`, `DATABASE_ENGINEER`, `MOBILE_ENGINEER`, `INFRASTRUCTURE_ENGINEER`.
- `DEVOPS_SRE`, `RELIABILITY_ENGINEER`.
- `SECURITY_ENGINEER` — implements approved security controls; cannot independently accept its own critical security decisions.

## AI

- `AI_SYSTEMS_ARCHITECT`, `AGENT_SYSTEMS_ARCHITECT`, `ML_ENGINEER`.
- `AI_EVALUATION_ENGINEER`, `SEARCH_RAG_ENGINEER`, `AI_GUARDRAILS_ENGINEER`.

## Design

- `EXECUTIVE_CREATIVE_DIRECTOR`, `DIGITAL_ART_DIRECTOR`, `UX_DIRECTOR`.
- `DESIGN_SYSTEMS_LEAD`, `TYPOGRAPHY_SPECIALIST`, `INTERACTION_DESIGNER`, `MOTION_DIRECTOR`.

## Realtime graphics and 3D

- `TECHNICAL_ART_DIRECTOR`, `REALTIME_3D_WEB_ENGINEER`, `SHADER_ENGINEER`.
- `ASSET_ARTIST`, `LOOKDEV_DIRECTOR`, `MATERIAL_ARTIST`, `LIGHTING_DIRECTOR`.
- `CAMERA_COMPOSITION_DIRECTOR`, `GPU_PERFORMANCE_ENGINEER`.

## QA and assurance

- `PRINCIPAL_QA_ARCHITECT`, `TEST_ARCHITECT`, `VISUAL_QUALITY_DIRECTOR`.
- `ACCESSIBILITY_SPECIALIST`, `PERFORMANCE_REVIEWER`, `SECURITY_REVIEWER`, `REGRESSION_ENGINEER`.
- `TECHNICAL_REVIEWER` — independently checks cross-component contracts, technical evidence and trade-offs.
- `IMPLEMENTATION_REVIEWER` — independently checks actual changes against permitted scope, task contract and evidence.

## Operations

- `RELEASE_ENGINEER`, `OBSERVABILITY_SRE_SPECIALIST`, `MIGRATION_ARCHITECT`, `INCIDENT_RECOVERY_SPECIALIST`.

## Required role contract

For every activated role record: `ROLE_ID`, title, domain, mission, expert standard, core expertise, responsibilities, activation and non-activation conditions, `MAY_DECIDE`, `MUST_NOT_DECIDE`, allowed decision classes, required inputs and outputs, review obligations, stop conditions, evidence requirements, common failure modes, and handoff rules.

Instantiate the contract with these explicit fields (not a mandatory roster):

```text
ROLE_ID
TITLE
DOMAIN
MISSION
EXPERT_STANDARD
OWNS
DOES_NOT_OWN
CORE_CAPABILITIES
ACTIVATE_WHEN
DO_NOT_ACTIVATE_WHEN
CLASS_1_BOUNDARIES
CLASS_2_AUTHORITY
CLASS_3_INTERACTION
INPUTS
OUTPUTS
EVIDENCE
REVIEW_OBLIGATIONS
STOP_CONDITIONS
COMMON_FAILURE_MODES
HANDOFF
```

OWNS/DOES_NOT_OWN express responsibilities; CORE_CAPABILITIES expresses core expertise. MAY_DECIDE/MUST_NOT_DECIDE must agree with the explicit authority fields. Existing stable IDs cover equivalent titles (for example TYPOGRAPHY_SPECIALIST, REALTIME_3D_WEB_ENGINEER and CAMERA_COMPOSITION_DIRECTOR); do not create duplicate role skills. Independence requires non-involvement in the implementation and critical decisions, not merely another role label.
