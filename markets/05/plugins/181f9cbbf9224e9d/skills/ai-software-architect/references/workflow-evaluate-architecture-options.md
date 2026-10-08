<!--
SPDX-FileCopyrightText: 2026 Leonardo Muffato (AUTOSOFT Engineering - www.autosoft-engineering.de)
SPDX-License-Identifier: MIT
Canonical source: shared/skills/evaluate-architecture-options/SKILL.md
-->

## Codex progressive-disclosure boundary

For a routine open comparison, this workflow plus the generated compact reference catalog are sufficient to shortlist, score, link, and recommend alternatives. Do not load every candidate or supporting reference body. Load at most one focused reference only when a specific unresolved distinction could materially change the decision. A named-pattern explanation or implementation example still requires its exact focused reference.

# Evaluate Architecture Options

## Evidence before inspection

Apply the orchestration evidence sufficiency gate before reading the active repository or calling a tool. If the user has already supplied enough constraints to judge proportionality, treat those constraints as assumptions and answer from them. Do not inspect a project merely because the task is project-bound or repository access is available.

Use repository evidence only when implementation facts could materially change the option set or the user requests review, verification, or repository-specific advice. Tool availability is not evidence of need.

Treat a request to improve or choose patterns for "this" or the current application, project, repository, or codebase as repository-specific advice. Inspect the smallest relevant source set with host-native static reads before recommending unless the user forbids inspection or has already supplied complete decision evidence. Do not claim that repository evidence was unavailable when relevant workspace files were accessible.

## Mandatory final-answer gate for an open selection

Treat questions such as "which design patterns should I use?" as an open selection, not as permission to output a prioritized stack of complementary patterns. If a missing fact can materially change the option set and no responsible default follows from current evidence, ask a focused clarification question and end the current turn without an option comparison, recommendation, or repository inspection.

Rank from observed evidence and current requirements. Before scoring, require a demonstrated current force. A named architecture or pattern may outrank `No pattern` only when simple functional or modular refactoring cannot adequately handle that force, such as active interchangeable implementations, independent deployment, a required framework boundary, or repeated change pain. Separable concerns, testability, or unverified growth alone are insufficient. Otherwise `No pattern` MUST rank highest and heavier options remain sensitivity choices. Ask one focused clarification only when no responsible current-evidence default exists; never invent likely growth.

Use the user's language and exactly one label set, in this order:

- English: `Decision scope and criteria`, `Evidence and assumptions`, `Alternatives`,
  `Recommendation`, `Supporting patterns`, `Your decision`.
- German: `Entscheidungsumfang und Kriterien`, `Evidenz und Annahmen`, `Alternativen`,
  `Empfehlung`, `Unterstützende Patterns`, `Deine Entscheidung`.
- Brazilian Portuguese: `Escopo da decisão e critérios`, `Evidências e premissas`,
  `Alternativas`, `Recomendação`, `Padrões de apoio`, `Sua decisão`.

Compare three to five credible options for the same decision when available. In the localized decision-scope section, say that Fit is an ordinal score, not a probability or measured percentage. Exact table headers: English `Option | Fit | Rationale | Main benefit | Main liability | Material assumption`; German `Option | Fit | Begründung | Hauptvorteil | Hauptnachteil | Wesentliche Annahme`; Brazilian Portuguese `Opção | Adequação | Justificativa | Principal benefício | Principal desvantagem | Premissa relevante`. Explain fewer than three credible alternatives; never pad with supporting patterns.

For a routine small-repository comparison with three alternatives, target 350 to 450 visible words for the complete six-section answer. Keep evidence bullets and table cells compact, limit supporting patterns to those that materially help the decision, and avoid repeating the same observation in the rationale and recommendation. This is a soft synthesis budget, not permission to omit required evidence, trade-offs, uncertainty, links, or decision guidance. Exceed it only when additional decision-relevant evidence is necessary.

End the localized user-decision section by asking the user to approve, revise, or request more information. Do not continue to ADR creation or implementation without that response.

A recommendation to keep the current simple structure or use no named pattern is still a proposed architecture decision. Explain the future force that would justify more structure, then visibly ask the user to approve, revise, or request more information. Do not omit the decision handoff merely because the recommendation adds nothing.

Use this compact English response template exactly for an English open selection.
For German or Brazilian Portuguese, translate the stable labels, disclosure, and
prose above; retain canonical category and pattern names for portable identities:

```markdown
## Decision scope and criteria
<one decision and its ordinal scoring criteria>

## Evidence and assumptions
<confirmed/static evidence, then explicit assumptions and unknowns>

## Alternatives
| Option | Fit | Rationale | Main benefit | Main liability | Material assumption |
| --- | ---: | --- | --- | --- | --- |
| [Category] [Linked name] | NN/100 | ... | ... | ... | ... |

## Recommendation
<the exact category and option name from one Alternatives row, uncertainty, and why the trade-off is justified>

## Supporting patterns
- [Category] [Linked name] — <its non-competing role>

## Your decision
Please approve, revise, or request more information before I continue.
```

Shape the same content as `ArchitectureOptionComparison` when a structured output is requested, including the language-neutral `offered_actions` values `approve`, `revise`, and `more-information`. Validate that complete shape in host-native structured-output mode. In Markdown, express those choices as ordinary visible guidance rather than machine-readable comments.

Before sending the answer, perform the same deterministic rendering self-check used by the Codex control plane: exactly one complete localized six-heading set appears in order, the localized decision-scope section explicitly says Fit is ordinal and not a probability or measured percentage, the matching localized six-column header is present, two to five genuine alternatives are rendered (normally three to five when that many are credible), category labels and canonical links are present, the recommendation repeats one exact table option, and the final section contains visible decision guidance. Do not emit internal control markers or HTML comments; Codex may display them to the user. When the Codex Composite routes here for a comparison, a trusted Stop hook may request one complete corrected rendering.

1. Start from recorded constraints, risks, stakeholders, and ranked quality attributes.
2. For an open-ended architecture or pattern-selection request, form three to five credible options within each material decision scope. Never pad the comparison with an option that does not address the same decision; when fewer than three credible alternatives exist, present the smaller set and explain why.
3. Load only references implicated by the current forces. Do not preload the catalog.
4. Compare benefits, liabilities, risks, assumptions, reversibility, and measurable fit. Scores support explanation; they do not replace it.
5. Include [no pattern](no-pattern.md) whenever added structure lacks a demonstrated force.
6. Recommend one option only when current evidence supports it. Keep unverified future growth conditional rather than using it to outrank the currently proportionate choice. State uncertainty and identify decisions requiring approval.
7. Keep alternative options separate from complementary supporting patterns. Do not compare an application architecture, a presentation pattern, and an object-design pattern as if they solve the same decision.
8. Do not equate similarly named patterns across process or deployment boundaries.

## User-facing comparison contract

- Present alternatives before the recommendation. For every option show a `0–100` fit score, concise rationale, main benefit, main liability, and material assumption.
- Describe the score as an ordinal fit score for this decision, not a probability or calibrated percentage. State the criteria used to score the options.
- In the localized evidence-and-assumptions section, distinguish static source observations from assumptions and unverified possibilities. Do not present a runtime claim unless runtime behavior was legitimately observed within the authorized mode.
- Prefix the first mention of every named option and supporting pattern with its category: `[GoF]`, `[Architecture]`, `[Presentation]`, `[Dependency]`, `[Data]`, `[Integration]`, `[Resilience]`, `[Modernization]`, or `[No pattern]`.
- Link the first user-facing pattern name to its canonical public reference under `https://github.com/leomuf/ai-software-architect/blob/main/shared/skills/evaluate-architecture-options/references/`, using the routed reference filename. Use plain text if the host cannot render Markdown links.
- For supporting patterns, add a one-line role explaining where each applies. Do not assign them competing fit scores unless they are genuine alternatives within the same decision.
- Apply the same category-and-link rule when mentioning a canonical pattern only to discourage or defer it. Do not end a section with a bare list such as `Avoid Repository, Unit of Work, and MVC`; either render each named pattern with its category and canonical link or describe the rejected abstraction types generically without naming catalog entries.

## Implementation example requests

- Treat loading the routed reference as a hard gate before answering a named-pattern explanation or implementation-example request. Do not answer from model memory. If the reference cannot be loaded, disclose that limitation instead of synthesizing an example.
- When the user asks for a generic Python implementation example of a GoF pattern, load only that routed `gof-*.md` reference and reuse its `Python example` verbatim. Explain briefly how the example's participants map to the pattern.
- In Codex, users invoke only `$ai-software-architect`. The Composite routes pattern explanations, implementation examples, and comparisons to this canonical module and uses its copied references without attempting sibling-skill activation.
- Reproduce the canonical example when a generic example is sufficient. For a repository-specific request, adapt the example to the user's domain and clearly identify the adaptation instead of presenting the canonical snippet as project-ready code.
- Do not load unrelated pattern files or synthesize additional variants unless the user asks for them or a materially different variant is necessary.
- Construct canonical public links from the routed filenames below. Do not browse or search the public repository merely to verify those deterministic links.
- Generic pattern explanations, implementation examples, and architecture guidance use the routed skill reference directly and need no deterministic tool call.

---

## Compact canonical reference catalog

This metadata is part of the generated open-comparison bundle. Reference bodies remain progressively disclosed.

In the Alternatives table, render a `No pattern` option as plain text after its category label and do not link it. Its focused reference remains available for explanatory detail outside that option cell.

Canonical URL base: `https://github.com/leomuf/ai-software-architect/blob/main/shared/skills/evaluate-architecture-options/references/`

Bundled path rule: `references/<File>`.

| Category | Name | File |
|---|---|---|
| Architecture | Clean Architecture | `architecture-clean.md` |
| Architecture | Event-Driven Architecture | `architecture-event-driven.md` |
| Architecture | Hexagonal Architecture | `architecture-hexagonal.md` |
| Architecture | Layered Architecture | `architecture-layered.md` |
| Architecture | Modular Monolith | `architecture-modular-monolith.md` |
| Architecture | Ports and Adapters | `architecture-ports-and-adapters.md` |
| Architecture | Service-Oriented Architecture | `architecture-service-oriented.md` |
| Architecture | Vertical Slice Architecture | `architecture-vertical-slice.md` |
| Data | Cache-Aside | `data-cache-aside.md` |
| Data | Repository | `data-repository.md` |
| Data | Unit of Work | `data-unit-of-work.md` |
| Dependency | Dependency Injection | `dependency-injection.md` |
| Dependency | Dependency Inversion | `dependency-inversion.md` |
| GoF | Abstract Factory | `gof-abstract-factory.md` |
| GoF | Adapter | `gof-adapter.md` |
| GoF | Bridge | `gof-bridge.md` |
| GoF | Builder | `gof-builder.md` |
| GoF | Chain of Responsibility | `gof-chain-of-responsibility.md` |
| GoF | Command | `gof-command.md` |
| GoF | Composite | `gof-composite.md` |
| GoF | Decorator | `gof-decorator.md` |
| GoF | Facade | `gof-facade.md` |
| GoF | Factory Method | `gof-factory-method.md` |
| GoF | Flyweight | `gof-flyweight.md` |
| GoF | Interpreter | `gof-interpreter.md` |
| GoF | Iterator | `gof-iterator.md` |
| GoF | Mediator | `gof-mediator.md` |
| GoF | Memento | `gof-memento.md` |
| GoF | Observer | `gof-observer.md` |
| GoF | Prototype | `gof-prototype.md` |
| GoF | Proxy | `gof-proxy.md` |
| GoF | Singleton | `gof-singleton.md` |
| GoF | State | `gof-state.md` |
| GoF | Strategy | `gof-strategy.md` |
| GoF | Template Method | `gof-template-method.md` |
| GoF | Visitor | `gof-visitor.md` |
| Integration | Idempotency | `integration-idempotency.md` |
| Integration | Idempotent Consumer | `integration-idempotent-consumer.md` |
| Integration | Publish/Subscribe | `integration-publish-subscribe.md` |
| Integration | Saga | `integration-saga.md` |
| Integration | Transactional Outbox | `integration-transactional-outbox.md` |
| Modernization | Anti-Corruption Layer | `modernization-anti-corruption-layer.md` |
| Presentation | Model-View-Controller | `presentation-model-view-controller.md` |
| Resilience | Circuit Breaker | `resilience-circuit-breaker.md` |
| Resilience | Retry and Backoff | `resilience-retry-and-backoff.md` |
| Resilience | Timeout and Deadline Propagation | `resilience-timeout-and-deadline.md` |
