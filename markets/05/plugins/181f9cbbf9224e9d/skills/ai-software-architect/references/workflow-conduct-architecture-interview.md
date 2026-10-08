<!--
SPDX-FileCopyrightText: 2026 Leonardo Muffato (AUTOSOFT Engineering - www.autosoft-engineering.de)
SPDX-License-Identifier: MIT
Canonical source: shared/skills/conduct-architecture-interview/SKILL.md
-->

# Conduct Architecture Interview

1. Restate the problem and scope using only supported facts.
2. Identify stakeholders, fixed constraints, assumptions, risks, and architecture-significant requirements.
3. Rank quality attributes from 1 to 5 and attach a rationale plus a measurable signal when possible.
4. Ask no more than five focused questions per round. Ask only when an answer can change a material decision; explain that impact.
5. Mark each question critical or noncritical. After at most three rounds, block on unanswered critical questions or continue with explicit assumptions.
6. Produce structured interview evidence for option evaluation; do not select a pattern during discovery.
7. Treat conflicting platform or interface statements as material when they change the option set. For example, a request for a web interface implemented with a desktop GUI toolkit requires clarification before selecting the presentation architecture.
8. Make that clarification terminal for the current turn: ask the focused question, explain its decision impact, and defer option comparison and recommendation until the user answers. Do not reinterpret one side of the contradiction as a correction.
9. Do not inspect the repository or invoke deterministic validators while asking a clarification or giving generic architecture guidance.

## Load references selectively

- Load [quality attributes](quality-attributes.md) when prioritizing runtime or development qualities and defining measurable signals.
- Load [stakeholders and constraints](stakeholder-and-constraint-discovery.md) when scope, ownership, compliance, deployment, integration, or operational boundaries are unclear.
