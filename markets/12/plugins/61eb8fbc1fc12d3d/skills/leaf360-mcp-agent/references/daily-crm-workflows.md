# Daily CRM Workflows

Use this reference when the user asks what to focus on, how to prioritize, or how to manage their mortgage pipeline.

## Daily Focus Flow

1. Call `leaf360_pipeline_focus`.
2. Review stale leads, urgent tasks, and high-intent lead opportunities.
3. If the request includes the loan pipeline, call `leaf360_loan_search` with the relevant status, stage, pipeline, assignee, or created-date filters and follow its cursors.
4. Use `leaf360_loan_get` or `leaf360_activity_list` on specific high-priority records before recommending action.
5. Suggest a short ranked action plan and offer to create tasks, notes, or message drafts for the top actions.

## Priority Signals

High priority:

- New inquiries with no recent contact
- Leads with a high close probability relative to the rest of the list, medium or high confidence, and no recent contact
- Borrowers waiting on next steps
- Loans approaching closing or stuck at a gated status
- Conditions, appraisal, disclosures, or closing tasks at risk
- Partners with recent referral activity but no follow-up
- Overdue tasks attached to high-value loans or partners

Medium priority:

- Leads contacted but not advanced
- Warm partner relationships needing nurture
- Loans with upcoming milestones but no blocker
- Templates or automations that would reduce repeat work

Low priority:

- Records with recent completed activity and no open blocker
- Cold leads without intent signals
- Cosmetic CRM cleanup unless requested

## Recommended Output Shape

Keep the response practical:

- Start with the top 2-4 priorities.
- Name the record and why it matters.
- Recommend the next action.
- Offer to create the task, note, draft email/SMS, or automation.

Do not list every record if a short prioritized answer is more useful.

When the user explicitly asks for every record or an exact count, exhaust cursor pagination and state that results are complete only within the authenticated user's visible RBAC scope.

For communication cadence or per-officer activity counts, call `leaf360_activity_search` with `createdAfter`, an optional `createdBefore`, and an indexed actor or activity-type filter. Treat its time window as activity `createdAt`, and repeat its automation-attribution warning when presenting human-performance conclusions.

## Mortgage CRM Judgment

- A stale website inquiry is time-sensitive.
- A loan milestone blocker usually beats generic prospecting.
- A referral partner with active deal flow deserves fast, professional follow-up.
- A borrower-facing message should reduce uncertainty and clearly state the next step.
