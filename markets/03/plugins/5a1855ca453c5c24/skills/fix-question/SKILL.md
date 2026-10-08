---
name: fix-question
description: >
  Rewrite a loose or vague research question into a sharper, twin-friendly
  version that produces a better response from an August twin (or any
  human-like respondent). Standalone helper — invoke on its own to sharpen
  a question before sending to August, or let other skills (notably
  /feedback-loops) call it programmatically when a twin response comes back
  too vague to use. Does NOT call any August MCP tools — pure text rewrite.
  Triggers on: "rewrite this question", "make this question better",
  "sharpen my ask", "fix this research question", "this question is vague",
  "/fix-question".
---

# Fix Question

Take a user's research question (or any question destined for an August
twin) and return a sharpened version that will produce a more useful
response. This skill does not call any tools — it is a pure prompt
rewriter.

---

## When to use

- User pastes a question and asks to make it better.
- User is about to send a vague question to August and wants a rewrite first.
- Another skill (e.g. `/feedback-loops`) invokes this programmatically
  because a twin response was too thin.

## When NOT to use

- The question is already sharp — say so, don't rewrite for the sake of
  rewriting.
- User wants to actually run the question against a twin → use
  `/august-feedback` or `/august-interview`.

---

## STEP 1 — Read the question and diagnose

Identify which of these weaknesses apply. A question can have several.

1. **Abstract reference** — refers to the artifact without naming it ("this",
   "the design", "our idea"). Twins do better with concrete anchors.
2. **No decision framing** — doesn't say what the answer will inform, so
   the twin can't calibrate depth or angle.
3. **Compound** — asks two or three things in one sentence. Twins tend to
   answer only one, usually the last.
4. **Under-specified dimension** — "what do you think" style, no axis.
   Better: what specifically — clarity, appeal, credibility, price,
   emotion, next step?
5. **Leading** — presupposes an answer ("don't you think this is clearer?").
6. **Abstract detail-ask** — "what" instead of "what specifically" or
   "give me an example of".

---

## STEP 2 — Apply the rewrite rules

Apply in order:

- **(a) Name the artifact concretely.** Replace "this" / "our thing" with a
  short concrete label ("the new GNC PDP hero", "the two-line headline
  variant B").
- **(b) State the decision the answer informs.** Add a clause like "so we
  can decide whether to ship this" or "to prioritize between A and B".
- **(c) Constrain to one dimension per question.** If the ask is
  compound, split into 2–3 focused questions — return them as a numbered
  list.
- **(d) Ask for concrete detail.** Prefer "what specifically…" / "give me
  one example of…" over bare "what".
- **(e) Strip leading language.** Replace "don't you think X is better"
  with "how does X land — is it clearer, less clear, or the same?".
- **(f) Keep it under ~35 words per question.** Long prompts get skimmed.

If applying a rule would break the user's intent, don't. Preserve intent
first; sharpen second.

---

## STEP 3 — Return the rewrite

**Standalone invocation** (user is the caller):

```
*Original*
> {user's original question}

*Rewritten*
> {sharpened question — or numbered list if split}

*What changed*
{one-line explanation, e.g. "Named the artifact, split the compound ask
into two questions, added the decision context."}
```

**Programmatic invocation** (another skill is the caller — signaled by
the args being just the raw question with no framing, or by the invoking
skill setting a `terse: true` style flag):

Return **only** the rewritten question(s). No preamble, no explanation,
no bullets. If the rewrite is a single question, return one line. If it's
split, return a numbered list. This lets the caller drop the string
straight into an `ask_question` MCP call.

---

## STEP 4 — Edge cases

- **Question is already sharp.** Return the original unchanged, with a
  one-line note: "Question is already well-formed — no rewrite needed."
- **Question is unanswerable by a twin.** (e.g. "does this align with
  Josh's brief?"). Flag it: "Twins can't evaluate brief-alignment — offer
  a gut-reaction rewrite instead?" and propose one.
- **Question is too broad to sharpen without more context.** Ask the user
  what artifact / decision / audience the question is about — but only in
  standalone mode. In programmatic mode, do your best with what's given
  and note the ambiguity in a comment.

---

## Output rules

- Never invent context the user didn't provide. If they didn't say what
  the artifact is, don't make up a name — ask, or leave a placeholder like
  `{artifact name}`.
- Never over-rewrite. If two of the six rules apply, apply two — not all
  six.
- In programmatic mode, keep output copy-paste-clean: no markdown, no
  quotes around the question unless the caller expects them.
