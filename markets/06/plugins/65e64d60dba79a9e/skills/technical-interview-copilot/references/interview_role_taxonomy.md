# Interview Role Taxonomy

## Purpose

Use this file to infer the likely interview domains from a job description, title, responsibilities, and candidate profile.

This is a routing guide, not a company-specific interview schedule. Current interview loops, assessment tools, and stage counts should be verified separately when needed.

## How to route

Identify:
1. primary role family;
2. secondary role family, if meaningful;
3. seniority;
4. strongest mandatory technologies;
5. responsibilities that imply design, operations, leadership, or domain depth.

Do not route only from the job title. Responsibilities and required outcomes matter more.

---

# 1. Backend / API Engineer

Typical emphasis:
- primary language/runtime;
- data structures and algorithms when relevant;
- API design;
- concurrency;
- databases;
- caching;
- messaging;
- testing;
- security;
- reliability;
- system design.

Senior-level follow-ups:
- failure modes;
- consistency;
- scaling;
- observability;
- migrations;
- backward compatibility;
- incident ownership.

---

# 2. Frontend Engineer

Typical emphasis:
- JavaScript/TypeScript fundamentals;
- browser/runtime behavior;
- framework knowledge;
- state management;
- component design;
- networking;
- performance;
- testing;
- accessibility;
- frontend system design.

Senior-level follow-ups:
- rendering strategy;
- caching;
- design systems;
- observability;
- bundle/runtime performance;
- cross-device behavior;
- maintainability.

---

# 3. Full-Stack Engineer

Blend backend and frontend topics.

Prioritize:
- end-to-end feature design;
- API contracts;
- state/data flow;
- persistence;
- authentication/authorization;
- testing;
- deployment;
- debugging across layers.

Avoid testing every topic equally. Follow the JD’s dominant side.

---

# 4. Data Engineer

Typical emphasis:
- SQL;
- data modeling;
- ETL/ELT;
- batch/streaming;
- Spark/distributed processing;
- orchestration;
- CDC;
- data quality;
- cloud data platforms;
- lakehouse/warehouse concepts;
- performance;
- reliability;
- backfills and replay.

Senior-level follow-ups:
- idempotency;
- late data;
- schema evolution;
- SLA/RPO/RTO;
- cost;
- observability;
- migration strategy;
- architecture trade-offs.

---

# 5. Analytics / BI Engineer

Typical emphasis:
- SQL;
- dimensional modeling;
- metric definitions;
- semantic layers;
- dashboards/reporting;
- data quality;
- stakeholder requirements;
- performance;
- visualization reasoning.

Possible tool depth:
- Power BI;
- Tableau;
- Looker;
- dbt;
- warehouse-specific SQL.

Senior-level follow-ups:
- governance;
- reusable metrics;
- model ownership;
- self-service analytics;
- semantic consistency;
- performance at scale.

---

# 6. Cloud / Platform Engineer

Typical emphasis:
- cloud primitives;
- networking;
- IAM/security;
- compute;
- storage;
- containers;
- infrastructure automation;
- deployment;
- observability;
- reliability;
- cost.

Senior-level follow-ups:
- multi-account/subscription design;
- blast radius;
- DR;
- platform abstractions;
- policy/governance;
- migration;
- capacity/cost trade-offs.

---

# 7. DevOps / SRE

Typical emphasis:
- Linux;
- networking;
- CI/CD;
- containers/orchestration;
- observability;
- incident response;
- SLI/SLO/SLA;
- automation;
- capacity;
- reliability.

Senior-level follow-ups:
- error budgets;
- toil reduction;
- rollback;
- dependency failures;
- production incidents;
- operational ownership.

---

# 8. ML Engineer

Typical emphasis:
- Python;
- ML fundamentals;
- training/inference pipelines;
- feature engineering;
- evaluation;
- deployment;
- monitoring;
- data leakage;
- model/version management;
- system design.

Senior-level follow-ups:
- online/offline consistency;
- drift;
- retraining;
- latency;
- scalability;
- experiment design;
- governance.

---

# 9. AI / GenAI Engineer

Typical emphasis:
- LLM APIs and model behavior;
- structured outputs;
- prompting as one layer, not the entire system;
- RAG;
- embeddings/retrieval;
- tools/agents;
- evaluation;
- hallucination/grounding;
- safety/security;
- latency/cost;
- production integration.

Senior-level follow-ups:
- failure analysis;
- eval design;
- prompt injection;
- tool permissions;
- observability;
- model selection;
- fallback;
- human approval;
- architecture trade-offs.

---

# 10. Data Scientist

Typical emphasis:
- statistics/probability;
- experimentation;
- data manipulation;
- SQL/Python;
- modeling;
- feature interpretation;
- evaluation;
- business reasoning;
- communicating results.

Senior-level follow-ups:
- causal assumptions;
- metric design;
- deployment/operationalization;
- stakeholder trade-offs;
- model risk.

---

# 11. Mobile Engineer

Typical emphasis:
- platform language/framework;
- lifecycle;
- navigation;
- state;
- networking;
- persistence;
- concurrency;
- testing;
- performance;
- accessibility;
- release/debugging.

Senior-level follow-ups:
- offline behavior;
- backward compatibility;
- observability;
- modularization;
- app size/performance;
- architecture.

---

# 12. QA / SDET

Typical emphasis:
- test strategy;
- automation;
- coding;
- API/UI testing;
- test data;
- CI;
- reliability;
- debugging;
- quality risk.

Senior-level follow-ups:
- coverage strategy;
- flaky tests;
- contract tests;
- performance testing;
- release gates;
- observability;
- quality ownership.

---

# 13. Security Engineer

Typical emphasis depends on specialty:
- application security;
- cloud/IAM;
- network security;
- threat modeling;
- incident response;
- secure coding;
- vulnerability analysis;
- detection/monitoring.

Do not invent exploit-heavy interview content unless the role actually calls for it.

---

# 14. Staff / Principal / Architect

This is a seniority overlay, not a separate stack.

Increase emphasis on:
- ambiguous requirements;
- architecture boundaries;
- long-term trade-offs;
- cross-team influence;
- migrations;
- risk;
- reliability;
- operational ownership;
- cost;
- security;
- technical strategy;
- mentoring/decision quality.

Reduce emphasis on trivia unless the JD explicitly requires hands-on implementation depth.

---

# Seniority scaling

## Early career
Focus on:
- fundamentals;
- implementation;
- syntax;
- debugging;
- clear reasoning;
- testing.

## Mid-level
Add:
- feature ownership;
- production debugging;
- trade-offs;
- maintainability;
- component-level design.

## Senior
Add:
- end-to-end ownership;
- architecture;
- reliability;
- security;
- performance;
- incidents;
- mentoring;
- stakeholder decisions.

## Staff / Principal
Add:
- organizational scope;
- platform/system boundaries;
- technical strategy;
- cross-team trade-offs;
- migration paths;
- operational risk;
- standards and leverage.

Do not infer people management from seniority unless supported.
