---
name: build-views
description: Creating or restyling collection view pages — why TABLE is almost never the answer, how to choose the right layout for the data (board/calendar/timeline/map/…), the companion settings each layout needs, and how to shape grouping, click actions, coloring, filters and naming.
---

# Building collection views people actually want to use

Almost never leave a view on TABLE. A created view starts as TABLE only as scaffolding — treat that as unstyled, not as a choice. Read the table's fields first: nearly every table offers a hook for something better (a status field → BOARD, dates → CALENDAR or TIMELINE, locations → MAP, a done-flag → CHECKLIST, images → CARDS). Reach for TABLE/TABLE_FULL only when the data is genuinely dense reference material and users' main job is scanning and sorting many columns. Pick the layout, then configure its companion settings in the SAME upsert_view call.

## Choosing the layout (`layout.layout`)

- BOARD — records that move through stages: a SINGLE_OPTION status/pipeline field exists and users drag records between columns (deals, tasks, applicants). Group by that field (`grouping.groups`).
- CALENDAR — records that happen on a date (events, bookings, deadlines). Needs `setup.dateStartField` (+ `dateEndField` when there's a range).
- TIMELINE / GANTT — records that span date ranges and overlap (projects, campaigns). Needs `setup.dateStartField` (+ `dateEndField` for the span); GANTT when dependencies or milestones matter (`ganttDependencies`, `milestones`).
- MAP — records with location data (`setup.map.latitudeField`/`longitudeField`).
- CHECKLIST — actionable to-dos with a BOOLEAN done field (`setup.checklistField`).
- CARDS / COLUMNS — visual browsing, few key fields, images matter (galleries, people directories, listings). Pair with a cover image via configure_view_fields.
- ROWS — tabular reading with more room per record than TABLE (long text, several secondary fields).
- TABLE / TABLE_FULL — dense reference data users scan and sort; TABLE_FULL for a spreadsheet feel.
- CHARTS — the question is aggregate ("how many/much per …"), not per-record (`charts.charts`).
- PIVOT_TABLE — two-dimensional aggregate comparisons (`pivotTable.rowGrouping`/`columnGrouping`/`values`).
- SPLIT — a list beside its record detail, for fast triage through records one by one.
- SINGLE_RECORD — the view should surface exactly one record, not a list.
Premium (plan-gated, the tool tells you): GANTT, TIMELINE, PIVOT_TABLE.

The field-driven layouts need a field that ALREADY exists — none of it is created for you, and a view built without it renders empty. No date field → not CALENDAR/TIMELINE/GANTT; no latitude/longitude pair → not MAP; no BOOLEAN → not CHECKLIST; no SINGLE_OPTION → not BOARD. Pick the best layout the table's real fields can drive, and add the field first if the user actually wants that layout.

## Shaping the view (same call or immediate follow-up)

- Grouping: group BOARD by the pipeline field; on TABLE/ROWS group by a meaningful category when the table has one (`grouping`).
- Click action: side panel (`clickAction.eventLink: openPanel`) keeps users in flow on list-heavy views; full page (openPage) when the record page is rich.
- Record coloring by the status field makes state scannable (`recordColoring`).
- App-user filters and search: enable `filterFields.search` on big tables; add quick filters for the fields users slice by (status, owner, date).
- Naming: the page title is the table's plural display name or a natural variation; `buttons.newButtonText` names the record ("Add deal"), `setup.recordTitle` is the record's name-like field.
- Sort by the field users expect (due date ascending, created descending) via `sort`.

## The record page

Every view carries a nested record page. After the view is shaped, delegate its layout to sections with the business context (what this team does, which fields matter day-to-day) — the sections editor has its own record-page design guidance. Set the fields the collection SHOWS via configure_view_fields — few, high-signal columns beat echoing the whole schema.
