# Schema and form UX

## Design from the job

Before adding fields, state what the respondent must accomplish and what the
team needs to do with the response. Keep only questions that change routing,
eligibility, follow-up, or the work performed after submission.

- Use `email`, `phone`, `url`, `number`, or other typed fields when the answer
  has a real type. Do not model everything as text.
- Use single-select for one stored choice and multi-select for several. Keep
  option ids stable even when labels change.
- Use `file_upload` only when the file is necessary and supported storage can
  be connected before publish.
- Put known product context in prefill or a hidden field instead of asking the
  respondent to re-enter it. Treat URL prefill as untrusted input.
- Split long or conceptually separate flows into pages. Keep short embedded
  forms inline when a multi-page flow adds friction without clarity.

Search the closest Fillo-owned example when authoring a new use case:

```text
https://fillo.so/api/v1/agent-examples/search?q=<use-case>&detail=full
```

Add `framework=<framework>` or `capability=<capability>` when known. Adapt the
schema and interaction; do not copy another example's visual treatment into
the host app.

## Treat ids as stored data

- Give every form, page, field, choice, ranking option, and matrix row or column
  a stable semantic id.
- Never derive ids from array positions, visible copy, localization, or random
  values created during render.
- A label can change without changing stored answer meaning. Renaming a field
  or option id creates a new stored key/value and requires an intentional data
  migration or downstream update.
- Keep one schema source of truth. Do not separately maintain dashboard, CLI,
  and component schemas unless they deliberately synchronize identical data.

## Keep logic inside the schema

In JSX, use `visibleIf={when("topic").eq("sales")}`. In object schemas,
`visibleIf` is an array of conditions. Do not use conditional JSX such as
`{isSales && <Fillo.Text ... />}`; that changes the schema per visitor and can
churn synced drafts.

Use a normal submit action for multi-question forms. Set
`settings.submitMode = "auto"` only for a genuine one-tap vote, rating, CSAT,
NPS, or pulse check where selecting the answer should complete the response.

## Design every state

Verify initial, loading, required-error, invalid-format, conditional reveal,
disabled, submitting, server-error, success, and narrow-layout states. Test
keyboard order and focus placement. Do not add an extra review step unless the
content is high-risk or the user explicitly requests confirmation.
