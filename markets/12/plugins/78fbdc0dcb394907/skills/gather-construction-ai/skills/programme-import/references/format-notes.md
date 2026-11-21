# Programme Import — Detailed Format Notes

Read this file at Step 2 of `workflow.md` for the field-by-field map. `workflow.md` itself only
carries the compact version — this file is the full reference so the skill body stays short.

---

## Parser-first (v2)

`scripts/parse_programme.py` implements the mappings in this file — every field, unit
conversion, and criticality-source rule below is what the deterministic parser actually reads,
not a description of what a human should do by hand. This file remains the reference for *what
the parser reads and why*: use it to explain a specific parser warning to a user, to sanity-check
a field the parser reports as absent, or to run the narrow in-context fallback (workflow.md Step 2,
python3-unavailable-and-small-file only). The parser currently covers **MSPDI (MS Project XML)**
and **Primavera P6 XER**; P6 XML (`<APIBusinessObjects>` root) is detected but not yet parsed by
the script — see workflow.md Step 2 for that fallback.

### What v2 captures that v1 didn't

- **Calendars, including dated exceptions.** v1 only ever assumed 8 h/day. v2 parses MSPDI
  `<Calendars><Calendar><WeekDays>` (weekly pattern) and `<Exceptions>` (dated overrides, e.g.
  public holidays or a compressed working Saturday), and P6's packed `clndr_data` blob (weekly
  `DaysOfWeek` pattern plus `Exceptions`, Excel-serial dates from epoch 1899-12-30). Where no
  usable pattern is recovered, the parser falls back to `hours_per_day: 8.0` and **says so in
  `warnings`** — it never assumes silently.
- **Constraints, including the MSPDI 0–7 enum and the XER `CS_*` mapping.** See the tables below.
  Unknown codes are **surfaced verbatim in `warnings`** (e.g. `unknown ConstraintType '9' on task
  123`) rather than dropped or guessed at — a code the tables don't cover is reported, not
  silently ignored.
- **WBS paths.** MSPDI `<WBS>` (already a formatted path) and XER's `PROJWBS` hierarchy (walked
  parent-to-root and joined with " / ") are both captured per task, for grouping in downstream
  reports.
- **Activity codes** (XER `ACTVTYPE`/`ACTVCODE`/`TASKACTV`, e.g. Area, Phase, Responsibility) are
  captured per task as a `{code_type: value}` map. MSPDI has no equivalent construct.
- **Resources.** MSPDI `<Resources>`/`<Assignments>` and XER `RSRC`/`TASKRSRC` are joined onto
  each task as a `resources: [{name, units}]` list (XER `units` is not currently populated —
  `None` until a future revision adds it).
- **Remaining duration**, not just percent complete: MSPDI `<RemainingDuration>` and XER
  `remain_drtn_hr_cnt`, captured alongside `pct_complete` so a consumer can distinguish "40% done"
  from "40% done, 6 days of work content left".
- **Numbered baselines are noted, not silently dropped.** MSPDI's `Baseline0` is the one the
  sidecar surfaces as `baseline_start`/`baseline_finish`; if the export also carries `Baseline1`…
  `Baseline10` (MS Project's numbered baseline slots), the parser adds a warning naming which
  numbers exist beyond `Baseline0` — the additional baselines are not read, but their presence is
  never hidden.
- **The Manual-schedule flag, and the caution it carries.** MSPDI `<Manual>` tasks are scheduled
  by the planner, not MS Project's engine — their own `stored` float/critical values may not
  reflect real network logic even inside MS Project itself. The parser copies them through as
  stored (never substitutes a computed value) and adds an explicit warning per manually-scheduled
  task so a consumer treats those particular float/critical figures with caution.
- **Multi-project XER handling.** A single `.xer` can bundle several projects in one `PROJECT`
  table. The parser never silently picks one: run with `--list-projects` first to see
  `proj_id`/name/data-date for each, then re-run with `--project <id>`. A single-project XER
  needs no flag.
- **cp1252 fallback.** P6's XER export defaults to Windows-1252, not UTF-8. The parser tries
  UTF-8 first and falls back to `cp1252` on a decode failure, recording which one it used in
  `provenance.encoding` — always cite this, since a misread encoding silently corrupts non-ASCII
  names (accented characters, "£" in a task name, etc.).

---

## MSPDI (MS Project XML)

Produced by MS Project's File → Save As → XML. Root element `<Project>` in namespace
`http://schemas.microsoft.com/project`; tasks live under `<Project><Tasks><Task>`.

**Project-level (data date):**
- `<StatusDate>` — the field closest to a P6-style data date. If absent, fall back to
  `<CurrentDate>` and say which one was used.
- `<Name>` / `<Title>` — programme/project name, surfaced in the parser's JSON summary (Step 2).
- `<StartDate>` / `<FinishDate>` — programme span.

**Per `<Task>`:**
| Field | Meaning | Notes |
|---|---|---|
| `UID` | Stable task identifier | Use this, not `ID` (which renumbers on resort) |
| `Name` | Task name | Used for activity mapping (Step 5) |
| `Start` / `Finish` | Current schedule dates | ISO datetime |
| `BaselineStart` / `BaselineFinish` | Baseline dates | Only present if a baseline was set in MS Project — absence means "no baseline", not zero |
| `PercentComplete` | 0-100 | |
| `Milestone` | 0/1 | 1 = milestone (zero-duration task) |
| `Critical` | 0/1 | MS Project's own critical-path flag (computed by MS Project, not by this skill) |
| `TotalSlack` | Integer, **tenths of minutes** | Convert: days = (TotalSlack / 10) / 60 / hours_per_day. State the divisor used (default 8 h/day) unless the file's `<CalendarUID>`/`<Calendars>` block gives a project-specific working day length |
| `OutlineLevel` | Integer | Use only for display grouping; ignore the summary-task rollup hierarchy beyond outline names — do not treat summary tasks as activities for mapping |
| `PredecessorLink` (repeatable) | `PredecessorUID`, `Type`, `LinkLag` | See Type mapping below |

**PredecessorLink `Type` values** (MSPDI's own numbering):
| Type | Relationship |
|---|---|
| 0 | Finish-to-Finish (FF) |
| 1 | Finish-to-Start (FS) — the default if the element is absent |
| 2 | Start-to-Finish (SF) |
| 3 | Start-to-Start (SS) |

`LinkLag` is in the same tenths-of-minutes unit as `TotalSlack` — convert and state the divisor
the same way.

**Criticality source:** use `<Critical>` as exported. Never recompute it from `TotalSlack` unless
`<Critical>` is absent from the file, in which case fall back to `TotalSlack <= 0` and say so
explicitly ("criticality derived from total float ≤ 0 — `<Critical>` not present in this
export").

**`ConstraintType` values** (MSPDI's 0–7 enum, read from `<ConstraintType>` alongside
`<ConstraintDate>`):
| Type | Constraint |
|---|---|
| 0 | As Soon As Possible (ASAP) — the default; no `<ConstraintDate>` significance |
| 1 | As Late As Possible (ALAP) — the engine schedules it ASAP and flags this in `warnings` |
| 2 | Must Start On (MSO) |
| 3 | Must Finish On (MFO) |
| 4 | Start No Earlier Than (SNET) |
| 5 | Start No Later Than (SNLT) |
| 6 | Finish No Earlier Than (FNET) |
| 7 | Finish No Later Than (FNLT) |

Any other value is surfaced verbatim in `warnings` ("unknown ConstraintType '<n>' on task
<uid>") rather than mapped or dropped.

---

## Primavera P6 XER

A tab-delimited text export. Structure: `ERMHDR` header line, then repeated blocks of
`%T <table-name>` / `%F <tab-separated field names>` / `%R <tab-separated row values>` (one `%R`
per row). Parse defensively — an XER can contain dozens of tables; only the three below matter
for this skill.

**`PROJECT` table (one row, usually):**
| Field | Meaning |
|---|---|
| `proj_short_name` | Project code/short name |
| `plan_start_date` / `plan_end_date` | Programme span |
| `last_recalc_date` | **The data date** — the date the schedule was last calculated. Always cite this as the data date in Step 2's parse report and Step 6's provenance block, not today's date or the export date |

**`TASK` table (one row per activity):**
| Field | Meaning | Notes |
|---|---|---|
| `task_id` | Stable identifier | Use this for the predecessor join, not `task_code` |
| `task_code` | Activity ID / code | |
| `task_name` | Activity name | Used for activity mapping (Step 5) |
| `target_start_date` / `target_end_date` | Planned dates | |
| `act_start_date` / `act_end_date` | Actual dates | Blank = not yet started/finished |
| `phys_complete_pct` | 0-100 | P6's physical % complete |
| `total_float_hr_cnt` | Float, **in hours** | Convert to days: days = hours / hours_per_day. Derive hours_per_day from the task's calendar if the `CALENDAR` table is present in the export; otherwise assume **8 h/day** and state this as an assumption |
| `status_code` | `TK_NotStart`, `TK_Active`, `TK_Complete` | |
| `task_type` | `TT_Task`, `TT_Mile` (start milestone), `TT_FinMile` (finish milestone), `TT_LOE` (level of effort), `TT_WBS` | Treat `TT_Mile`/`TT_FinMile` as milestones for the task table's milestone flag |

**`TASKPRED` table (one row per logic link):**
| Field | Meaning |
|---|---|
| `pred_task_id` / `task_id` | The predecessor/successor pair (joins to `TASK.task_id`) |
| `pred_type` | `PR_FS` (Finish-to-Start), `PR_SS` (Start-to-Start), `PR_FF` (Finish-to-Finish), `PR_SF` (Start-to-Finish) |
| `lag_hr_cnt` | Lag, in hours |

**Criticality source:** P6 exports do not carry an explicit per-task "is critical" flag in the
core `TASK` table the way MSPDI does. Use `total_float_hr_cnt <= 0` (converted to days per the
row above) and state this is the source of criticality: "criticality derived from total float ≤
0 hours (P6 export)". If a `driving_path_flag` or similar field is present in a given export,
prefer it and say so instead.

**`cstr_type` values** (P6's `CS_*` codes, read from `TASK.cstr_type`/`cstr_date`, mapped onto
the same constraint names the engine uses):
| XER code | Mapped constraint |
|---|---|
| `CS_MSOA` | Start No Earlier Than (SNET) |
| `CS_MSOB` | Start No Later Than (SNLT) |
| `CS_MEOA` | Finish No Earlier Than (FNET) |
| `CS_MEOB` | Finish No Later Than (FNLT) |
| `CS_MSO` / `CS_MANDSTART` | Must Start On (MSO) |
| `CS_MEO` / `CS_MANDFIN` | Must Finish On (MFO) |
| `CS_ALAP` | As Late As Possible (ALAP) — the engine schedules it ASAP and flags this |

Any other code is surfaced verbatim in `warnings` ("unknown XER constraint code '<code>' on task
<task_id>") rather than mapped or dropped. A secondary constraint (`cstr_type2`) is recorded in
`warnings` only — the engine applies the primary constraint alone.

**Beyond the three core tables above,** the parser also reads `PROJWBS` (WBS hierarchy, walked to
build a full path per task), `ACTVTYPE`/`ACTVCODE`/`TASKACTV` (activity codes), `RSRC`/`TASKRSRC`
(resource assignments), and `CALNDR` (calendar weekly pattern + exceptions, best-effort from
`clndr_data`) — see the Parser-first section above for what each contributes to the sidecar.

---

## Primavera P6 XML

**Not currently parsed by `scripts/parse_programme.py`** — the script validates the MSPDI root
tag and refuses anything else, so a P6 XML file (root `<APIBusinessObjects>`) is not routed
through this schema at all by the deterministic parser. Treat it the same as "python3
unavailable" in workflow.md Step 2: fall back to in-context parsing only if the file is small, or
ask the user to re-export as P6 XER or MSPDI XML.

The notes below describe the same P6 data model as the XER tables above, in XML form (e.g.
`<Project><Task><TaskName>`, `<TargetStartDate>`, `<TotalFloatHours>`), for the in-context
fallback case. Coverage varies more between exporters than XER does — parse on a **best-effort
basis**: read whichever of the fields above are present, and explicitly list which fields were
found and which were not available in this particular export, rather than assuming the full XER
field set is there.

---

## Asta Powerproject (via Microsoft Project XML export)

Asta's native `.pp` format is binary and never parsed. Powerproject exports MSPDI-compatible
XML (File → Export → Microsoft Project XML), which the MSPDI rules above handle. Asta-specific
quirks to expect and state when found:

- **`Critical` is often unpopulated or all-zero** in Asta exports — judge criticality from
  `TotalSlack` ≤ 0 instead and state that fallback in the report.
- Task UIDs are renumbered on export — do not expect stability between two Asta exports of the
  same programme; match by task name when comparing revisions.
- Calendars are simplified on export; where slack-to-days conversion depends on them, state
  the assumed hours/day.
- Baseline fields are only present if a baseline was set in Powerproject before exporting.

Provenance line should read "Asta Powerproject (Microsoft Project XML export)" when the user
says the file came from Asta — the XML itself is indistinguishable from MS Project's, so
record the source tool from the user's answer, not the file.

*Caveat: these notes follow the MSPDI schema and known Asta export behaviour; verify against
one real Powerproject export from the customer before relying on it in a live claim.*

## Cross-format notes

- Never guess a field's meaning from its name alone if it isn't in the tables above — say what
  was found and ask, rather than mapping an unfamiliar field silently.
- A `.mpp` file is MS Project's native binary format and cannot be parsed by this skill under any
  circumstances — see Step 1.
