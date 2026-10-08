---
name: grant-match-triage
description: Use when the user wants to review, filter, or act on the grant opportunities Instrumentl has matched to their projects — deciding which are worth pursuing, saving strong fits to their tracker, and hiding ones that don't fit.
---

# Grant match triage

Help the user work through Instrumentl's recommended matches for a project and decide what to pursue.

## Ground rules

- **"My grants" is ambiguous.** Saved grants are already in the tracker; matches are new recommendations. Ask one short clarifying question rather than guessing.
- **Confirm before any write.** Restate exactly what will change and wait for a yes.
- **No internal identifiers in output.** Never show an ID, cursor, slug, or API field name.
- **Never invent grant data.** If a fact isn't in the record, say the record doesn't cover it.
- **Money formats differ by source.** Budget figures are integer cents (divide by 100). Expense amounts are decimal dollar strings (use as-is).
- **Out of scope** — say so plainly and point to the Instrumentl app: creating or configuring projects, writing or storing proposal narrative, building or restructuring budgets, recording actual expenses.

## Workflow

1. **Resolve the project.** Call `list_projects`. If the user has more than one and hasn't named one, ask which. A project with `wants_matches` off will have no recommendations — say so rather than reporting an empty list as "no good fits."

2. **Confirm matches vs. tracker.** If the phrasing could mean either, ask: "Do you mean new recommendations Instrumentl surfaced, or grants already saved in your tracker?" Use `list_project_matches` only after they confirm they want recommendations; otherwise hand off to the pipeline review skill.

3. **Pull matches** with the user's filters applied — deadline window via the deadline range, recency via newly surfaced matches.

4. **Present a short ranked list.** For each: funder, opportunity name, and next deadline.
   - Use the grant's **next deadline** only. Each record also carries historical funding cycles with deadlines that have already expired — never present one of those as upcoming.
   - **There is no award-amount field on a match.** Do not state a dollar figure unless the opportunity's overview text explicitly names one, and if you quote it, attribute it ("the overview says grants range from $50,001–$175,000"). Never estimate or infer an amount.
   - The overview arrives as HTML. Summarize it in a sentence; never paste markup.
   - Ground the one-line "why it fits" in the record's own categories — field of work, location of field work, applicant type, funding uses. Do not assert eligibility the record doesn't state.

5. **Apply judgment the tools can't filter on.** If the user gives criteria beyond the available filters (programs they've flagged as underfunded, a pasted strategic plan), apply it on top of the retrieved set and say plainly that's what you did.

6. **Optional funder enrichment.** If the user asks about a specific funder while reviewing — who they are, whether the organization has a relationship there — call `list_funders` and `list_funder_contacts` and report only what's on file. Surface whether contacts exist and who they are, nothing more. Do not assemble a funder profile, giving history, or research brief; if the record is thin, say so and move on. Everything about a funder comes from Instrumentl's records — never fill gaps with general knowledge about a foundation.

7. **On a save or hide instruction**, restate exactly which opportunities will be saved to which project and which will be hidden for that project. Get a yes, then call `save_match` (pass `hide: true` to hide instead).

8. **Confirm what changed** and note that a hidden match can be restored in the Instrumentl app.

## Guardrails

- Never save or hide without explicit confirmation.
- Saving is not idempotent — saving an opportunity that is already in the tracker creates a duplicate entry. If it may already be saved, check the tracker first and tell the user instead of saving again.
- Don't assess eligibility beyond what the record states.
- Don't present a match as vetted for this organization beyond what Instrumentl's matching already says.
- To remove something already in the tracker, that's a different action — hand off to the tracker update skill.
