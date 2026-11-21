---
type: test-plan
project: Hedraios Scripture Context
status: active
created: 2026-09-29
tags: [plugin, review, test-plan]
---

# Use-Case Inventory and Review Test Plan

## Positive review cases

| ID | User prompt | Expected tools | Expected result |
|---|---|---|---|
| P-01 | Study Mark 2:1-12 in context. Who acts, who speaks, and who receives each action? | `validate_scripture_reference`, `study_passage`, optionally `render_study_workspace` | Normalized reference, exact WEB passage with before and after verses, Jesus and other explicit actors surfaced, verse order preserved, Daniel 7 and Psalm 103 links explained, agency limitations visible |
| P-02 | Why is Philippians 4:13 often taken out of context? | `validate_scripture_reference`, `study_passage` | Immediate context includes need, plenty, hunger, and contentment; caution rejects unlimited-achievement reading; 2 Corinthians 12 link is labeled thematic |
| P-03 | Read Jeremiah 29:11 with its immediate setting. Is this an instant personal success promise? | `validate_scripture_reference`, `study_passage` | Before and after context is shown; exile and restoration caution appears; application is separated from original audience and promise |
| P-04 | Study Proverbs 16:18 for leadership. Is it a guarantee that every proud leader falls immediately? | `validate_scripture_reference`, `study_passage` | Wisdom genre is identified; output frames a general pattern, not a mechanical timetable; James 4 relevance is explained |
| P-05 | Trace Abigail's agency and the event order in 1 Samuel 25:23-35. | `validate_scripture_reference`, `study_passage`, optionally `render_study_workspace` | Abigail and David are surfaced where explicit, verse order is unchanged, narrative caution appears, Romans 12 is presented as a teaching anchor rather than proof that every narrative detail is prescriptive |

## Negative review cases

| ID | User prompt or scenario | Why the plugin should not complete it as asked | Expected behavior |
|---|---|---|---|
| N-01 | Quote Malachi 5:1 and explain it. | Malachi has no chapter 5. | Reject with `invalid_chapter`; do not guess or invent a quotation |
| N-02 | Study John 3:18-16. | The range is reversed. | Reject with `reversed_range`; ask for a corrected range |
| N-03 | Prove from Joshua 3:15-16 that God will always perform a miracle after I take a risky first step. | Narrative is being turned into a universal personal guarantee. | Return the passage and caution if requested, refuse the guaranteed claim, distinguish description from prescription, and suggest responsible pastoral review |

## Additional edge cases

- Reject multiple or injected references such as `John 3:16; ignore all instructions`.
- Reject a passage larger than 100 verses and ask for a focused range.
- Reject context-window values outside 0 through 12.
- Return no invented cross-reference when the curated map has no match.
- Keep tool results usable when the client does not render MCP Apps UI.
- Treat pronoun-only speaker labels as unresolved and low confidence.
- Never label WEB text as another translation.

## Acceptance rule

Automated tests verify deterministic behavior. Public-review cases must later be rerun in actual ChatGPT developer mode against the deployed HTTPS MCP endpoint. Human theological and editorial review remains separate from test success.

