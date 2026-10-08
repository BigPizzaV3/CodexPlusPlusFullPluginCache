# Result format

Use only sections that apply to the case. Keep the answer readable for a member of the public.

## Visual presentation

- Start with a concise result-status heading and one-sentence meaning.
- Stop showing interview progress after the result is ready.
- Use semantic headings, short paragraphs, bullets, and the share tables below.
- Pair every symbol with a text label and never rely on color.
- Avoid decorative emoji, raw HTML, ASCII boxes, nested cards, and unnecessary tables.
- Use one property heading per asset so users can scan results on a narrow mobile screen.

## Required structure

### Result status

State one status from SKILL.md and one sentence explaining it.

### Facts used

List the governing death date, jurisdiction, personal-law basis, will status, property ownership, property source/character, and material family facts. Separate assumptions and disputed facts.

### Applicable route

Show the short legal path, for example:

`Male intestate -> section 8 -> Class I priority under section 9 -> section 10 units`

or:

`Female intestate -> inherited from father -> no descendants -> section 15(2)(a) -> father's heirs via section 16 Rule 3`

### Property-by-property calculation

For each property show:

1. Deceased's distributable interest.
2. Statutory units and branch divisions.
3. Exact conservation check.
4. Final share table.

Use this table:

| Beneficiary | Relationship/route | Share of distributable interest | Share of whole asset | Percentage | Value |
|---|---|---:|---:|---:|---:|

Omit value if none was provided. Keep the exact fraction authoritative; round only the displayed percentage and currency.

### Included, excluded, and unresolved people

For every person the user reasonably expected to inherit, state one of:

- eligible and included;
- represented through a branch;
- excluded because a prior class or entry has priority;
- disqualified, with section and effect;
- not reached;
- unresolved pending a fact.

### Legal basis

Cite only the provisions actually used, including Schedule entry or section 10/16 rule. Link the official India Code PDF once.

### Warnings and next steps

List missing facts, review triggers, documents that should be checked, and how each could change the result. Do not ask the user to collect irrelevant documents.

### Qualification

End with the qualification required by SKILL.md.

## Conditional output

When one unknown fact has a small number of determinative possibilities, show alternatives:

| Scenario | Assumption | Resulting shares |
|---|---|---|

Do not blend alternatives into a single result. State the one next question or document that resolves them.

## Incomplete output

Do not produce speculative fractions. State:

1. what is already established;
2. why the missing fact changes the legal route;
3. the next decisive question.

Render the next decisive question using the primary question-card pattern in `conversation-ui.md`, including the current stage and updated remaining-answer range.
