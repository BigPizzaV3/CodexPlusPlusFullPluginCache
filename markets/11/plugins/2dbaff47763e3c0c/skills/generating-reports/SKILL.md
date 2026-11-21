---
name: generating-reports
description: Use when asked to produce, check on, read, file or delete a data room's generated report - an investment memo, pitch deck, business report, data deck, category summary or the company profile. Covers that generation is asynchronous and the order of calls from generating one to saving it into the room.
---

# Generating reports

The generator descriptions cover each kind and its arguments; this covers
the order of calls and what not to do while one runs.

## BEFORE GENERATING

A memo, business report, board deck or company profile may already be on its
way: a room created with a website builds them itself. If `get_dataroom`'s
`onboarding_status` is `IN_PROGRESS` or `DOCUMENTS_READY`, don't generate
those - wait for the room's own.

## THE SEQUENCE

1. `generate_<kind>` - returns at once; nothing is finished.
2. `list_generated_reports` - each report's `id` and generation status.
3. `read_generated_report(kind, report_id)` - once it is ready.
4. `copy_generated_report_to_documents(kind, report_id)` - files it into the
   room's documents.

## WHILE IT RUNS

- Tell the user it is running and let them come back. Generation takes
  minutes.
- Don't loop on `list_generated_reports` waiting for a status to change.
- Don't call a generator again because nothing appeared - a second call
  starts a second report.
- Don't say a report is ready without checking `list_generated_reports`.

## DON'T

- Don't delete a report to retry it. A new `generate_<kind>` call is the
  retry; deleting first only loses the old one.
- A refusal naming the plan means the feature is not in the room's plan. Say
  so and stop - don't reach for a different kind instead.
