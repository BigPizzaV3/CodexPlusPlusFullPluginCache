---
name: council-execution-harness
description: Use when Samuel gives the Executive Council a multi-step objective spanning tools, files, apps, executors, or domains and expects the system to carry it through rather than return a to-do list.
---

# Council Execution Harness

## Goal
Turn a natural-language objective into verified execution with minimum user involvement.

## Precedence
Google Drive is the canonical Council Source of Truth.
Do not create shadow state for work already represented canonically.

## Loop
1. RECOVER
   - read `README_OPERACIONAL — Executive Council`;
   - retrieve only the domain sources needed;
   - read `06_COORDENACAO_ATIVA` when routing/handoff matters.
2. DEFINE
   - convert the request into one observable outcome;
   - identify constraints, authorization, and proving postcondition.
3. ROUTE
   - choose the competent C/domain;
   - choose the narrowest executor that can do the technical work;
   - technical home does not change under temporary assignment.
4. PLAN MINIMALLY
   - create only tasks necessary to reach the outcome;
   - order by dependency and risk;
   - do not create ceremony, documents, roles, or processes for their own sake.
5. EXECUTE
   - use available tools/apps directly;
   - delegate work that another agent/tool can safely do;
   - involve Samuel only for authentication, inaccessible information, a real subjective choice, or a material consequence not already authorized.
6. VERIFY
   - run the actual postcondition using `council-verification-gate`.
7. PERSIST
   - update canonical state only when the result changes current facts, decisions, restrictions, pending work, or integration health.
8. HANDOFF
   - if another area must act, use `06_COORDENACAO_ATIVA` with only: problem, current facts, decisions/restrictions, exact requested action.
9. CLOSE
   - remove or resolve stale pending items;
   - report result, material exception, or exact blocker.

## Concurrency
Parallelize independent reads and research.
Serialize writes that can conflict or depend on prior state.

## Escalate
Escalate only when:
- authority is unclear;
- scope/risk materially changed;
- required authorization is absent;
- repeated debugging indicates an architectural problem;
- evidence is insufficient for the consequence.

## Anti-loop
If tool calls are no longer changing evidence, state, or probability of success, stop and re-plan.
