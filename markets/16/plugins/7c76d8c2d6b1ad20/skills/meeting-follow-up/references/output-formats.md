# Output formats

Choose the format the user asks for. If unspecified, use a concise default recap with summary, decisions, action items, open questions, and material blockers/risks.

## Quick recap

1. Summary
2. Decisions
3. Action items
4. Open questions

## Full meeting minutes

1. Meeting information
2. Participants
3. Purpose
4. Discussion by topic
5. Decisions and status
6. Action items
7. Open questions
8. Risks and blockers
9. Next meeting (only if stated)

## Action-item table

| Task | Owner | Deadline | Priority/status | Dependency | Evidence/confidence |
|---|---|---|---|---|---|

Use `UNASSIGNED` and `NOT_SPECIFIED` where applicable. Preserve deadline phrases; put a resolved date beside the original wording.

## Decision log

| Decision | Status | Decision-maker/participants | Reason | Effective date | Evidence/confidence |
|---|---|---|---|---|---|

Do not list a proposal as a confirmed decision.

## Next-meeting agenda

- Review previous actions
- Revisit outstanding decisions
- Resolve blocked items and dependencies
- Obtain promised updates
- Add new topics only when present in the source or requested by the user

## JSON

Return valid JSON only when the user requests machine-readable output. Use a stable structure such as:

```json
{
  "meeting": {"title": "NOT_PROVIDED", "date": "NOT_PROVIDED", "type": "UNCLEAR", "participants": []},
  "summary": "",
  "topics": [],
  "decisions": [],
  "action_items": [],
  "commitments": [],
  "open_questions": [],
  "blockers": [],
  "risks": [],
  "next_meeting": "NOT_PROVIDED"
}
```

Keep only source-supported claims. Use explicit `status`, `confidence`, and evidence fields where relevant. Represent unknowns with the uncertainty codes rather than fabricated values.

## CSV

For requested CSV, provide a header row and correctly quote cells containing commas, quotation marks, or line breaks. Keep one action per row. Do not flatten multiple owners or deadlines in a way that changes meaning. State any unsupported field as blank or its agreed uncertainty code.
