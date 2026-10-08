# Evidence, state, and checkpoints

## Contents

- Evidence labels
- Field states
- Quality gates
- Workshop ledger
- Pause checkpoint
- Resume rules
- Final contamination scan

## Evidence labels

Apply one label to every substantive workshop item:

- **User statement:** The user asserts it but has not supplied a source.
- **Provided source:** The user supplied a document, link, transcript, dataset, or named record that supports it.
- **Customer quote:** Verbatim language with a real source supplied by the user.
- **Inference:** A synthesis derived from approved material; record which fields support it.
- **Hypothesis:** Plausible but not verified. It may guide research but is not proof.
- **Example only:** Fictional teaching content. It can never enter the user's ledger or output.

Never silently upgrade a user statement, inference, hypothesis, or example into sourced evidence.

For customer language, also record a privacy treatment: `named`, `anonymized`, or `redacted`. Ask for the source record and privacy treatment together when the quote first appears. An anonymized record label can establish provenance without exposing the customer's identity. If words are removed or replaced, show the redaction and do not present the edited text as an untouched verbatim quote.

## Field states

Track each template field as exactly one of:

- `blank`
- `draft`
- `approved`
- `hypothesis`
- `skipped`

Keep the last approved value while a revision is still in `draft`.

## Quality gates

A field is ready to draft when it is as specific as the template requires and does not depend on an unsupported claim. Check:

1. Who exactly is involved?
2. What job, situation, or problem is observable?
3. What consequence or desired outcome matters?
4. Compared with what, where required?
5. What supports the claim?
6. Does it contradict an approved field?

Ask one focused follow-up when a gate fails. After two unsuccessful follow-ups, offer `Mark as hypothesis` or `Skip`.

## Workshop ledger

Maintain this structure in conversation state:

```yaml
workshop:
  company: ""
  current_phase: 0
  current_step: 1
  fields:
    field_id:
      status: blank
      value: ""
      provenance: user statement
      source: ""
      supports: []
  omitted_optional_sections: []
  unresolved_gaps: []
```

Do not put example content in this ledger.

## Pause checkpoint

Return a copyable Markdown block using this exact structure:

```markdown
# B2B Messaging Workshop Checkpoint

**Company:** [name]
**Current phase:** [0–3]
**Completed through:** [section]
**Next step:** [exact section]

## Approved answers
- **[field]:** [value] — provenance: [label/source]

## Hypotheses
- **[field]:** [value] — needs validation: [what is missing]

## Skipped required fields
- **[field]:** [open question]

## Omitted optional sections
- [section]

## Resume instruction
Use $run-b2b-messaging-workshop to resume from this checkpoint.
```

Exclude fictional examples, internal analysis, rejected drafts, and hidden reasoning.

## Resume rules

When given a checkpoint:

1. Parse every listed field.
2. Preserve its status and provenance.
3. Confirm the company, completed-through section, and next step.
4. Flag contradictions or missing required structure instead of guessing.
5. Continue only after the user has a chance to correct the summary.

## Final contamination scan

Before finalizing, search the draft conceptually for:

- `ExampleCo` or `ExampleCo Legal`;
- the fictional Live Matter Plan;
- litigation firms, legal operations, lawyers, matters, deadlines, or legal-workflow language not supplied by the user;
- fictional prices, ranges, percentages, customer quotes, testimonials, proof, or claims;
- any clause without a ledger source.

Remove unsupported contamination or mark a user-requested borrowed idea as a hypothesis. Never leave `Example only` content in the source of truth.
