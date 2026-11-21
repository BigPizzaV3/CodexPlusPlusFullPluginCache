---
name: setup
description: Verify the Gather plugin works — checks MCP connection/auth, lists projects,
  reports configured dashboard reports. Use when starting out, after install, or a
  skill reports missing data/tools.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Setup Health Check

A one-shot pre-flight check for the Gather plugin. Confirms the MCP connection is authorised, lists the projects you can see, and reports which dashboard reports are configured in your workspace — so you know upfront which skills will run at full capability and which will degrade. This skill is entirely read-only, makes no changes, and takes no arguments.

---

## Step 1: Connection Check

Attempt `getMyProjects`.

**If Gather tools are unavailable:** discover connected tools by provider and operation, not a fixed prefix. If still absent, explain that Gather must be connected in ChatGPT Plugins and authorised with the user's Gather account. Refer to `../../docs/install.md`. Stop the live-data check here; do not invent projects.

**If authentication fails:** ask the user to reconnect Gather through its connection settings and complete the browser login. Do not ask for a password or access token in chat. Stop until a read succeeds.

If the call succeeds, continue to Step 2.

---

## Step 2: Your Projects

From the `getMyProjects` result, present the user's assigned projects:

| Project Name | Status | Role |
|---|---|---|
| Example Project Alpha | Active | Project Manager |

- If `getMyProjects` returns no projects, call `getProjects` (all workspace projects). If that returns results, tell the user they have workspace access but no project assignments — an admin will need to assign them to a project before project-scoped skills will work.
- If both `getMyProjects` and `getProjects` return nothing, suggest the user check their Gather account and permissions with their workspace admin — the connection itself works, but no projects are visible to it.

---

## Step 3: Report Availability

Call `getReportSchemas` and compare the reports it returns against the 11 supported dashboard reports the plugin's skills rely on:

`dashboardShiftTable`, `dashboardResourceLabour`, `dashboardResourceMaterial`, `dashboardResourcePlant`, `dashboardNarrative`, `dashboardProgress`, `dashboardAllocation`, `dashboardAccessPossession`, `dashboardAccessNonPossession`, `dashboardAccessOverview`, `dashboardWorklogEvents`

A named report with an empty fields list is **advertised but schema unavailable**, not verified as usable. Separate these from reports with populated schemas and reports absent from the result. Do not claim full capability from name presence alone.

Present the comparison as a table of report, schema status and affected capability:

| Available | Not Configured |
|---|---|
| dashboardShiftTable | dashboardProgress (example if absent) |
| dashboardResourceLabour | dashboardNarrative (example if absent) |
| ... | ... |

If every report is available, say so plainly and skip the "Not Configured" column content.

---

## Step 4: Capability Summary

For each report listed as "Not Configured" in Step 3, tell the user which skills will be affected — per **Pattern 12 (Schema Verification and Graceful Degradation)** in `../../shared/patterns/12-schema-verification.md`:

| Missing Report | Affected Skills |
|---|---|
| `dashboardProgress` | progress, programme, estimator, measured-mile, cost-to-complete, progress-report |
| `dashboardNarrative` | narrative-search, events, delay-analysis, commercial-report |
| `dashboardAccessPossession` / `dashboardAccessOverview` | access, programme, delay-analysis |
| `dashboardResourcePlant` | resource-analysis, plant-report |
| `dashboardResourceMaterial` | resource-analysis, delivery-notes |
| `dashboardAllocation` | resource-analysis, benchmark, estimator |
| `dashboardWorklogEvents` | events |

State clearly: affected skills degrade gracefully — they will say what data is missing rather than fabricate a result — but full capability needs the report configured in Gather. This is a heads-up, not a blocker.

---

## Step 5: Next Steps

Suggest the user try:
- `$project` — for a project overview
- `$diary <project> yesterday` — to see recent shift activity
- `docs/SKILL_REFERENCE.md` in the plugin repo — for the full skill catalogue

---

## Related Skills

- `$project` — project overview, once the connection is confirmed working
- `$diary` — review recent shift records for a project
- `$data-quality` — audits data *content* completeness (missing narratives, recording gaps) for a project; this skill checks *connection and configuration*, not the data itself
