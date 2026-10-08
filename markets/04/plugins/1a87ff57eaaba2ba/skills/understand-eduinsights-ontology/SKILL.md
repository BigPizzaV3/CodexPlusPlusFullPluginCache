---
name: understand-eduinsights-ontology
description: Explain and apply the EduInsights semantic world model, including canonical entities, identifiers, relationships, native grains, applicability, coverage, source boundaries, and the most important marts. Use for questions about the EduInsights ontology, semantic layer, data model, schema, relationship map, mart meanings, or which mart fits an education, workforce, accreditation, outcome, or AI-use question.
---

# Understand the EduInsights ontology

Explain how EduInsights represents the person's question before selecting data. Preserve the question's ordinary meaning while keeping every connection at its supported level of detail.

## Follow this path

1. Identify the requested entity, measure or outcome, population, place, and period.
2. Read [world-model.md](references/world-model.md) before explaining an entity, relationship, identifier, applicability rule, or coverage state.
3. Read [important-marts.md](references/important-marts.md) before naming, comparing, or selecting a `marts.*` relation.
4. When current availability or columns matter, call `edu_describe_data` without a topic. Then inspect the selected relation with `topic: table:marts.<relation>`.
5. Use the smallest relation at the question's native level of detail. Move across entities only through an explicit identifier or relationship.
6. State the connection type and the boundary that prevents overinterpretation.

Treat live `edu_describe_data` output as the authority for deployed availability and fields. Its overview can emphasize common starting views rather than print every relation. Treat a curated mart as unavailable only when its direct table description fails. Never query `marts.semantic_catalog` directly.

## Keep the two registers separate

Use exact entity, relationship, identifier, and mart names for builders, data work, and reproducibility. For everyone else, explain the plain meaning first. Add the technical name only when it helps the person inspect or reproduce the result.

For example, say "degrees a college reported in a field and year" before `ProgramAwardCell`. Say why a value is blank instead of exposing a coverage-state code.

## Protect the meaning

- Treat reported awards as historical reporting, not proof of a current catalog program.
- Treat broader field outcomes as context for a narrower field or program.
- Treat CIP-to-SOC links as preparation relationships, not observed graduate destinations.
- Keep occupations, industries, tasks, and skills distinct.
- Treat observed AI use as behavior in the named product and population, not employment impact or universal capability.
- Preserve source release, native level of detail, applicability, coverage, and identifier uncertainty.
- Keep zero distinct from suppressed, uncollected, inapplicable, nonparticipating, stale, or unresolved data.

When the person asks for an empirical result rather than an explanation, apply these semantic rules with `$research-with-eduinsights`.

## Finish with a usable map

Complete the answer only when it identifies:

- the person's concept and the matching ontology entity or entities;
- the relationship path and whether each step is direct, inherited, structural, empirical, or contextual;
- the best current mart or focused tool and what one row represents;
- the source, period, coverage, and limitation most likely to change the interpretation.
