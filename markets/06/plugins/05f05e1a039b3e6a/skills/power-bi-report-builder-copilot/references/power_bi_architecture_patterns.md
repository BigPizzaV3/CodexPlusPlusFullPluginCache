# Power BI and Fabric Architecture Patterns

## Purpose

Use this file for storage-mode choices, Fabric, semantic-model architecture, incremental refresh, and large-scale reporting decisions.

Choose based on requirements, not fashion.

# 1. Import

Use when:
- data fits model/capacity constraints;
- refresh latency is acceptable;
- interactive performance is important.

Strengths:
- fast in-memory analytics;
- rich model behavior.

Watch:
- refresh duration;
- model size;
- memory;
- partitioning;
- cardinality.

# 2. DirectQuery

Use when:
- data must remain at the source;
- freshness requirements make import unsuitable;
- source governance/scale favors live queries.

Watch:
- source latency;
- concurrency;
- folding/pushdown;
- visual query count;
- transformations;
- relationship/model complexity.

Every interaction can generate source work, so source/model/report design all matter.

# 3. Composite models

Use when different tables genuinely need different storage modes.

Define clearly:
- which tables are Import/DirectQuery/Dual/other supported mode;
- relationship behavior;
- expected query path;
- freshness semantics.

Avoid creating a composite model just to work around an unresolved modeling issue.

# 4. Direct Lake

Use for Fabric scenarios where data in OneLake/Fabric can be queried through a semantic model with Direct Lake benefits.

Current Direct Lake capabilities evolve quickly. Verify:
- Direct Lake on OneLake vs Direct Lake on SQL;
- fallback behavior;
- security mode;
- composite support;
- calculated table/column limitations;
- workspace/capacity requirements.

Do not rely on old Direct Lake assumptions.

# 5. Incremental refresh

Use when a large Import table does not need full historical reprocessing every refresh.

Define:
- historical retention window;
- refresh window;
- `RangeStart`/`RangeEnd`;
- folding;
- partition behavior;
- complete-day requirement;
- detect-data-changes behavior when used;
- real-time DirectQuery partition if supported/required.

Validate with the actual source and published model behavior.

# 6. Fabric placement

Decide where logic belongs:

## Lakehouse/Warehouse
Good for reusable heavy transforms, joins, conformance, SCD logic, large-scale preprocessing.

## Semantic model
Good for relationships, business measures, user-facing model semantics.

## Report
Good for presentation-specific calculations/formatting only.

Avoid duplicating core business logic across all three layers.

# 7. Architecture decision

For meaningful choices document:

**Recommendation**  
**Why**  
**Trade-offs**  
**Performance impact**  
**Security/governance impact**  
**Cost**  
**What would invalidate the choice**

# 8. Avoid

Do not automatically recommend:
- DirectQuery for “real time”;
- Direct Lake for every Fabric model;
- larger capacity for slow DAX;
- aggregations before measuring workload;
- many-to-many relationships to “make it work”;
- complex composite models when Import is sufficient.
