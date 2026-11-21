# Search And Reporting

Use this reference for lead or loan lists, named-assignee questions, date-bounded reporting, and requests for every matching record.

## Choose Structured Filters

- `query` searches borrower or record content. Do not use it for a team member's name.
- `assignedTo` accepts a team member's full or partial name or exact email and resolves that person inside the authenticated company.
- `assignedUserId` is preferable after Leaf360 has returned the exact user ID. Do not combine it with `assignedTo`.
- On loans, set `primaryAssigneeOnly: true` when the user asks for the person's primary LO book. Without it, supporting team assignments can also match.
- `assignedToMe` restricts loan results to the authenticated user's assignment or creator relationships, including for administrators. Combine it with `primaryAssigneeOnly` for a strict primary-LO view.

`matchedAssignees: null` means no assignee filter was applied. An empty array means a supplied assignee name did not resolve in the company. A populated array confirms the resolved tenant user; an invalid or cross-tenant `assignedUserId` is rejected.

## Lead Search

Use `leaf360_lead_search` for borrower lookup and lead reporting. Supported reporting filters include:

- `createdAfter` / `createdBefore`: inclusive ISO date or datetime bounds
- `source`: exact `leadSource`, such as `LendingTree-Purchase`
- `status`: exact configured lead status
- `assignedTo` or `assignedUserId`: assigned team member
- `primaryAssigneeOnly`: match only the lead's primary `lo_user_id`

The current assignee is available in `assignedPeople` with a stable user ID when stored. `assignedAt` is not currently available, so do not equate lead creation time with assignment time or claim speed-to-lead assignment lag.

Assignment roles are returned as canonical display labels. Treat `Loan Officer`, `loan-officer`, and `loan_officer` as the same role; the MCP returns `Loan Officer`. When a user's account permission is `Admin` but the record assigns that user through `lo_user_id`, use the record assignment role `Loan Officer` for lead distribution and role grouping. Account permissions continue to control RBAC and must not be interpreted as job assignments.

## Loan Search

Use `leaf360_loan_search` for loan inventory, processing, status, stage, and assigned-LO questions. It supports:

- `loanStatus`, `loanStage`, `pipelineStage`, and `loanPriority`
- `assignedTo`, `assignedUserId`, `assignedToMe`, and `primaryAssigneeOnly`
- `createdAfter` / `createdBefore`

Loan results include `assignedPeople`, `applicationDate`, and current pipeline fields. Identify a loan by `loanReferenceId`; use `loanNumber` only when the reference ID is null. Each result also carries `openConditions` (open conditions across the app-managed and LOS-synced lists, removed ones excluded), `rateLocked`, and `lockExpiration`, so a list can be ordered by condition pressure or lock risk without opening each file.

Loan team roles use the same canonical display labels. The recorded `loanOriginator` relationship is authoritative for the `Loan Officer` role when an embedded team snapshot contains a conflicting account-level role.

Application-date and funding-date search filters are not yet available. Do not silently substitute `createdAt`, `applicationDate`, or current funded status for one another. Explain the limitation when an exact date-window report cannot be answered.

## Tag Filters

Both `leaf360_lead_search` and `leaf360_loan_search` accept `tags` (up to 10 names) and `tagMatch`. Names match exactly but ignore case. `any` (default) returns records carrying at least one listed tag; `all` requires every listed tag. Tag names are visible on returned records as `tags`. For the full list in use, call `leaf360_config_get` with `sections: ["tags"]`; it returns each name and whether it is used on leads, loans, or partners.

## Pagination And Counts

Lead and loan searches use cursor pagination:

1. Start without a cursor and use a limit up to 100.
2. Append the returned records to a unique-ID result set.
3. While `hasMore` is true, call the same tool with the same filters and the prior `nextCursor`.
4. Stop only when `hasMore` is false.

Do not increment `page`; values above 1 are intentionally unsupported. Leave `includeTotal` false unless the user truly needs an exact database count. For complete list requests, counting the unique records collected across all cursor pages avoids a separate count query.

## Activity Counts

Use `leaf360_activity_search` for bounded cross-record counts by actor, type, direction, outcome, or lead, loan, or partner record type. `createdAfter` is required. Admins must also provide an actor or at least one activity type so the query can use an existing index; non-admins are automatically restricted to their own actor ID.

The tool returns totals and grouped counts, not activity bodies or borrower records. Its time basis is activity `createdAt`. Historical automation attribution is not reliable, so the counts can include workflow-generated communication. State that limitation instead of presenting the result as proven human effort.

## Attribution Boundaries

- `leaf360_partner_deals` answers which deals are attributed to a referral partner. It does not answer which loans are assigned to that person as an LO.
- `leaf360_pipeline_focus` prioritizes leads and tasks. It does not enumerate the loan pipeline.
- `leaf360_activity_list` reads one lead, loan, or partner timeline; use `leaf360_activity_search` for bounded cross-record counts.
- A zero or missing loan amount is a source-data condition, not proof that the search failed. Report it separately as a data-quality observation.

## RBAC And Completeness

Every result is company-scoped. Non-admin users additionally receive only records visible through their creator or assignment relationships. Never describe a non-admin assignee result as that person's complete company book unless the tool and role context establish that scope.

When reporting results, state the applied assignee and primary-only behavior, whether all cursors were exhausted, and that completeness is within the authenticated user's visible Leaf360 scope.
