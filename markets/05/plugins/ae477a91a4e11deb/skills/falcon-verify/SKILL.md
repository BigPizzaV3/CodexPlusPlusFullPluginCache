---
name: falcon-verify
description: Check whether an AI-written answer is supported by the evidence it was written from, using FALCON Verify's falcon_verify tool. Use when a user asks "is this supported", wants a summary checked against a document or data, needs every unsupported claim listed, or wants an auditable record of the check. Not for checking whether something is true in the world; FALCON verifies against the evidence supplied, nothing else.
---

# FALCON Verify

FALCON Verify answers one question: is this output supported by this evidence?
It does not know the world. A claim the evidence cannot speak to comes back
`unverifiable`, never `supported`. Every call leaves a hash-chained audit record.

## When to call

- The user has an output (a summary, an answer, a report, a chatbot reply) AND
  the material it was written from (a document, a record, a set of facts, a
  retrieved passage). Call `falcon_verify`.
- The user asks whether a run has settled, or for its journal: call
  `falcon_verify_status` or `falcon_get_journal` with the run id.
- The user asks how many verifications are left this month: call `falcon_account`.
- The user only has a statement and no evidence: do not call. Say that FALCON
  verifies against evidence the user supplies, and ask for it.

## How to call `falcon_verify`

- `output`: the prose to verify, verbatim.
- `evidence`: an object, one key per source, each value the source text or data
  VERBATIM AND IN FULL. Never summarise or paraphrase the evidence: the verdicts
  stand against exactly what is passed, and condensed evidence makes true claims
  read unsupported. A pasted document is fine as `{"document": "<text>"}`.
- `claims` (optional): when the user has already listed the claims, pass each
  as an object `{"text": "<the output's own words>", "type": "<numeric |
  comparative | temporal | categorical | causal | existential>"}`. Never pass
  bare strings. With claims supplied, no model call is needed to find them.
- `depth`: leave at the default `auto` unless the user asks for rules only
  (`extract`) or insists on a judge for every claim (`judge`, about three
  verifications' cost for one).

## Reading the result

- `status` is the epistemic status of the check, not the verdict:
  `supported` (every decided claim held), `qualified` (some did not),
  `insufficient_support` (nothing could be decided), `execution_failure`.
- `claims[]` carries one entry per claim with its `verdict` and the evidence
  fields it was bound to. Report each claim by its own words and verdict.
- `unsupported_rate` is over DECIDED claims and is `null` when none were
  decided. A null rate is not a clean result; say what could not be checked.
- `insufficiency`, when present, says what was established, what was not, why,
  and what evidence or depth would resolve each item. Relay it.
- `attribution` and `report_as` give the line to close with (FALCON Verify, the
  run id, the counts). Use it as written.
- `audit.run_id` is what the user needs to fetch the journal or status later.

## What not to do

- Do not present a FALCON verdict as a statement about the world. "Supported"
  means supported by the evidence given.
- Do not invent or complete evidence. If the user's evidence is partial, verify
  against it and say what was missing.
- Do not offer prices, plans or purchase links. If the allowance is exhausted,
  the tool says so; tell the user their Account page on falcon.1-i.ai shows
  their plan, and stop there.

## Example

User: "Verify: 'Q2 revenue was $4.2M, up 12% year over year, and gross margin
reached 31%.' Facts: 'Second-quarter revenue came in at $4.2 million, a 12%
increase over the same quarter last year. Gross margin was 30.6%.'"

Call `falcon_verify` with `output` set to the quoted sentence and `evidence`
set to `{"facts": "<the facts text verbatim>"}`. Report: revenue $4.2M
supported; up 12% supported; margin 31% unsupported (the evidence says 30.6%).
Close with the attribution line from the result.
