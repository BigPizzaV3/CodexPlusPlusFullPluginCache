---
name: diagram-generator
description: Create accurate, readable diagrams for software systems, data models, workflows, APIs, and user journeys.
---

# Diagram Generator

Use this skill when the user asks to visualize architecture, processes, dependencies, data, interactions, timelines, or journeys.

## Diagram selection

Choose the smallest diagram that answers the question:

- **Flowchart:** decisions, business processes, or operational workflows.
- **Sequence diagram:** interactions between users, services, APIs, queues, or databases over time.
- **Architecture diagram:** systems, boundaries, services, storage, and external providers.
- **Entity-relationship diagram:** entities, fields, keys, and relationships.
- **State diagram:** lifecycle states and transitions.
- **Timeline:** chronological events or delivery phases.
- **Mind map:** concepts and their relationships.
- **User journey:** steps, touchpoints, pain points, and outcomes.
- **Deployment diagram:** environments, infrastructure, regions, and runtime boundaries.

Use Mermaid by default unless the user requests another language such as PlantUML, Graphviz, or D2.

## Workflow

1. Restate the diagram's purpose in one short sentence.
2. Identify actors, components, boundaries, inputs, outputs, decisions, and dependencies from the supplied context.
3. Select the diagram type and state it briefly.
4. Produce a complete renderable diagram, not pseudocode or a partial fragment.
5. Add only the minimum legend or assumptions needed to interpret it.
6. If the diagram describes an existing codebase, cite inspected files and label inferred relationships.

## Accuracy rules

- Do not invent services, tables, endpoints, events, or relationships that are not supplied or observed.
- Label assumptions clearly and ask for clarification when a missing relationship changes the diagram materially.
- Preserve direction, sequence, cardinality, and ownership.
- For ERDs, show primary keys, foreign keys, and cardinality when known.
- For sequences, preserve request/response order, retries, async boundaries, and failure paths.
- For architectures, distinguish internal components from third-party systems and trust boundaries.
- For workflows, include validation, error, retry, and completion states when relevant.

## Output rules

When the user asks to see a diagram, prioritize the rendered visual. Show source code only when requested or when rendering is unavailable. If rendering is unavailable, provide the complete source in a fenced code block and say which renderer can display it.

For complex diagrams, offer focused views such as “high-level architecture” and “request detail” instead of producing one unreadable mega-diagram.

## Review mode

When reviewing an existing diagram, check for missing actors, ambiguous arrows, overloaded nodes, inconsistent names, missing failure paths, incorrect cardinality, and boundaries that hide important security or ownership assumptions.
