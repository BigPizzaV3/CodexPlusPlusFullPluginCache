---
name: research-list
description: Use Leadbase for B2B lead generation, sales prospecting, company and contact research, market mapping, lead qualification and enrichment of existing sheets. Find companies, people, products or public posts with sources and credit reporting.
---

## Choose the right operation

Use the installed Leadbase MCP tools and their current schemas directly. The user determines the entity, geography, criteria, fields and requested count. Use known facts rather than paying to rediscover them. Ask only for missing information that materially changes the result.

For a new list, use sheets_research. Each requested entity is a new row: companies means companies, people means people. Do not substitute contacts at existing companies for a requested company list, or silently modify an existing customer sheet. Design typed columns for the requested fields and source URLs. Lists of products or public posts belong in sheets too. For existing rows, use sheets_enrich for the specified sheet and cells. Use enrichment_start for a direct typed answer only when the user does not need a sheet.

Read-only discovery and billing_get are free access checks. Research consumes the connected account's credits. Honor the requested scope and any budget. Never purchase credits, grant credits, expand the batch, archive customer sheets to evade plan limits, or start outreach without explicit authorization. If a sheet limit blocks creation, explain it and ask which existing sheet may be archived or let the user choose the next step.

## Execute once and show progress

Use a stable idempotency key for each logical paid request; reuse it for an explicitly requested safe recovery, not for different work. Never automatically repeat an ambiguous paid submission. Keep the returned batch/job/sheet IDs. Writes require the current revision and a stable retry key according to their schemas.

Immediately after sheets_research returns a sheetId, call view_sheet so the user can follow live progress and edit the real sheet. open_workspace opens the sidebar library; view_sheet opens a particular table. Respect the host's available display modes. Without UI, provide the sheet link and a compact result summary.

Check enrichment_get or sheets_research_status at sensible intervals until terminal execution. Do not claim the requested count was reached based on total sheet rows: manual rows and other jobs are separate. Keep confirmed count, target count, partial failure and billing state distinct. Use returned page cursors to inspect all results, never fabricate rows beyond the first page.

## Verify results and costs

Check returned source URLs support the claimed facts. An image URL is not evidence for a product price. A precise date requires matching evidence; do not turn relative dates into unsupported exact dates. Never invent contact information or label unsupported details verified. Missing or inaccessible evidence means uncertain, not proof of absence. Explain partial results candidly.

Continue checking execution and accounting separately. A terminal job can still have pending or reconciliation_pending billing. Report credits as final only after settlement. Missing usage is unknown, not zero; held credits are not final charges. Retain failed partial results and reported actual costs rather than silently rerunning the job.

If an owned terminal job reports reconciliation_pending, enrichment_reconcile can check and settle its retained financial receipts without starting research. Use its jobId and a stable key for that repair attempt. Do not loop on an unknown receipt or substitute a new paid submission. Read the returned billing status; reconciliation does not turn failed research into successful research.

Conclude with the actual number of delivered entities, the sheet, material evidence gaps and settled credits or the exact pending accounting state. Do not expose authentication, private logs, internal provider receipts or unrelated account data.
