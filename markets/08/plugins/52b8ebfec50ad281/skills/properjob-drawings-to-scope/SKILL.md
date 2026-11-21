---
name: properjob-drawings-to-scope
description: Prepare a draft scope of works, builder pricing schedule, tender brief or room/trade work list from a verbal brief, notes, specifications or readable plans. Use for defining the work builders should price, including small jobs and requests without drawings.
---

# Prepare a scope of works

## Country and language

Reply in the requested or conversation language. Keep the actual project country,
currency, units and tax basis independent of language; do not infer them from a
translation or a shared currency symbol. Translate the schedule for the user while preserving literal drawing labels, IDs, revisions, units and page/detail references. Explain uncertain local construction terms rather than silently replacing the specification.

For international documents, number formats or jurisdiction questions, read the
[country and language rules](../properjob-building-work/references/international-workflows.md),
also available at `skill://proper-job/properjob-building-work/references/international-workflows.md`.

## Choose by the requested output

Use this skill when the user wants a scope, work description, tender brief or
pricing schedule, even for one small trade and when no plans exist. Job size and
the presence of drawings do not decide the workflow. Cite the supplied brief
when there are no drawings; do not require an attachment to start.

For a request whose main purpose is the cost of a repair or individual trade,
use `properjob-small-jobs`. When a scope request also asks for prices, prepare
the schedule here first, then follow the supported costing path below.

## Workflow

Read `properjob-building-work` before inspecting attachments. Its host-only
analysis, page access, revision, measurement and privacy rules apply in every
country. No paid extraction, raw-file transfer or saved-project access is added.

Inspect the supplied brief and readable plans, sections, elevations,
specifications and schedules. Record what was actually inspected and which
revision each fact comes from. Do not combine conflicting revisions or claim
text extraction is full visual inspection. Deliver a useful partial scope when
pages are missing, visibly listing the limitation.

Produce a draft schedule grouped by room or trade to suit the user's request.
For each item include a stable neutral ID, physical entity/location, existing
retained/demolition/repair/new status, work description, quantity/unit when
supported, source page/detail or brief reference, specification and open question.
Use stated dimensions or the core skill's calibrated measurements. Deduct
openings once and reconcile repeated views with the same physical item ID.

Distinguish explicit drawing requirements, user brief requirements and possible
coordination questions. Never convert a guessed specification or likely knock-on
into confirmed work. A brief requirement absent from drawings gets a brief
reference, not a fabricated page citation. Specialist design and statutory
requirements stay unresolved until supported by appropriate evidence.

Keep alternatives separate and mark supply/install responsibility and exclusions
where known. Check interfaces between structure, envelope, services, fittings,
finishes, protection and reinstatement. End with the material questions builders
need answered to price consistently.

A schedule-only request does not require a calculator call. If pricing is also
requested, send one reconciled set of supported neutral facts to
`calculate_building_work` following the core workflow. Respect the 25-document,
200-observation and 100-unresolved-item limits; obtain an agreed subset rather
than silently truncating a larger job. Unpriced tasks stay in the schedule.

Label the output a draft scope for review, not a certified bill of quantities,
coordinated construction specification or issued tender. Do not send it to
builders or claim it was saved to the user's Proper Job account.
