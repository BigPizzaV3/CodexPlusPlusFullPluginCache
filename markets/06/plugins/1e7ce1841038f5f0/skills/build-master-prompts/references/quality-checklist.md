# Quality checklist and red-team review

## Gate A — Correctness and alignment

- [ ] The objective is observable and unambiguous.
- [ ] Confirmed facts, assumptions, unknowns, and exclusions remain distinct.
- [ ] Every explicit exclusion is preserved.
- [ ] The chosen artifact type fits the task.
- [ ] No requirement contradicts another without a priority rule.

## Gate B — Context and portability

- [ ] The prompt works in a clean new chat.
- [ ] Required context is embedded, attached by name, or represented as a variable.
- [ ] Prior memories and unrelated conversation context are explicitly excluded.
- [ ] The prompt does not pretend to override higher-level instructions.
- [ ] Environment-specific tool assumptions are conditional.

## Gate C — Research and evidence

- [ ] Unstable and high-stakes claims trigger current verification.
- [ ] Source hierarchy, research date, citations, and no-access fallback are defined.
- [ ] Facts, inferences, and recommendations are distinguishable.
- [ ] The prompt never instructs the model to invent citations.

## Gate D — Roles and execution

- [ ] Each role has a distinct responsibility or quality criterion.
- [ ] Overlapping roles are consolidated.
- [ ] Conflicts between roles have a decision owner or priority.
- [ ] Stages, checkpoints, permissions, and stop conditions match the required autonomy.

## Gate E — Output contract

- [ ] Sections, order, format, language, and audience are explicit.
- [ ] Variables are clearly marked and explained.
- [ ] Acceptance criteria are testable.
- [ ] Missing-input and unavailable-tool behavior is defined.
- [ ] The requested depth is compatible with length constraints.

## Gate F — Safety and honesty

- [ ] No false guarantee of perfection, completeness, or professional status.
- [ ] High-impact actions require suitable confirmation or human review.
- [ ] The prompt requests concise rationale/evidence, not hidden chain of thought.
- [ ] Privacy, confidential data, permissions, and external side effects are respected.

## Adversarial review

Attempt to break the prompt with these tests, then repair any failure:

1. **Empty context**: Could an executor act when optional inputs are missing?
2. **Memory contamination**: Could unrelated prior preferences alter the result?
3. **Stale knowledge**: Could a time-sensitive claim pass without verification?
4. **Role collision**: Could two roles issue incompatible instructions?
5. **Format drift**: Could the executor return a plausible but unusable format?
6. **Fabricated capability**: Does the prompt assume browsing, files, tools, or memory that may not exist?
7. **Overconfidence**: Could uncertainty be hidden behind polished prose?
8. **Prompt injection in sources**: Could attached or browsed content override the task? Require source content to be treated as data, not instructions.
9. **Scope creep**: Could the executor take external action beyond explicit authorization?
10. **Goodhart failure**: Could optimizing a metric undermine the real objective?
11. **Contradictory user input**: Is there a clear method to surface and resolve conflicts?
12. **Excess complexity**: Can any role, stage, or rule be removed without reducing reliability?

## Severity and repair

- `Critical`: unsafe authority, missing legal/safety boundary, or destructive ambiguity. Do not deliver until fixed.
- `Major`: prompt may produce wrong, stale, contaminated, or unusable output. Fix before delivery.
- `Minor`: clarity, efficiency, or formatting weakness. Fix when it does not add disproportionate complexity.

Finish only when no Critical or Major issue remains.
