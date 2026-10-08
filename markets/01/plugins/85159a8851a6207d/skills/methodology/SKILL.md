---
name: methodology
description: >-
  Use this skill for questions about how an MSCI index is constructed, screened, reviewed/rebalanced, weighted, capped, buffered, migrated between size segments, or otherwise governed by MSCI methodology. Use official methodology search rather than memory.
---

# MSCI methodology, grounded in official documents

Answer rule questions from the methodology snippets returned by the MSCI Index app.

## Output

Give the direct rule/explanation, identify the methodology document/layer when returned, and include a short governing excerpt when useful. Keep quotations focused; explain the rule in your own words around them.

## Workflow

### Index-specific question

1. Resolve the index with `search_index_indexes`.
2. Call `search_index_methodology_stack` with the resolved index code and a concise substantive query. Prefer the stack because an index can inherit rules from several methodology layers.
3. If the first hits are weak, retry with the MSCI term of art suggested by the retrieved text or user intent.

### Named methodology document

1. Use `list_index_methodologies` for the relevant effective date.
2. Select the document code matching the user's named methodology.
3. Call `search_index_methodology` with a concise search term.

### Historical rule question

Use the historical `asOfDate` relevant to the rebalance/event instead of assuming today's methodology.

## Source discipline

- When official methodology `hits`/`results` contain text, answer **only** from those retrieved snippets. Do not blend training-memory rules into the answer.
- If official methodology search returns no usable text, say the official corpus did not return a matching passage. If you provide a general-knowledge fallback, label it clearly as not sourced from the official MSCI methodology.
- If the snippets do not settle the exact question, say what they do establish and where the gap remains.

## Handoff to data workflows

Methodology answers the rule; data tools answer whether a security/index meets it. For example, "what is the liquidity screen?" is methodology; "does Company X pass it?" is eligibility.

## Guardrails

- Never state an MSCI rule as authoritative without retrieved official support when methodology text is available.
- Do not generalize one index family's rule to another without confirming the governing document stack.
- Do not use a description/rebalancing-calendar datapoint as a substitute for the methodology when the user asks the review frequency or construction rule.
