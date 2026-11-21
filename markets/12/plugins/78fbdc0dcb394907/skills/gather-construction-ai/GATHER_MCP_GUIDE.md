# Gather MCP reference

This is the tool and report snapshot carried over from the supplied Gather v0.16.0 plugin. Confirm actual schemas against the connected server. Installation for this OpenAI edition is in `docs/install.md`. Authentication and live tool behaviour have not been verified during conversion.

## Available MCP Tools

This OpenAI edition supports the nine read-only tools below. The shared server may advertise additional operations; follow the exclusions in `shared/openai-runtime.md`.

| # | Tool | Params | Returns |
|---|---|---|---|
| 1 | `getProjects` | `limit`≤100, `page`, `search`, `tags`, `modifiedSince` (ISO 8601 — only projects with shift records modified since) | All active projects (admin) — UUID, name, status, tags |
| 2 | `getMyProjects` | `limit`≤100, `page` | Projects assigned to you, with your role |
| 3 | `getProjectAssignments` | `uuid` (project) | User name, job title, role per assignee (no email) |
| 4 | `getPeople` | `limit`≤100, `page` | Name, UUID, role for each labour resource |
| 5 | `getReportSchemas` | — | Name, group, field list for every dashboard report available to your workspace |
| 6 | `getCachedReport` | `uuid` (project or workspace), `reportName`, `from`, `to` (YYYY-MM-DD) | Dashboard report rows — see report table below |
| 7 | `getShiftRecords` | `uuid` (project), `from`, `to`, `supervisor`, `tags`, `page`, `limit`≤25, `modifiedSince` (ISO 8601) | Paginated shift record UUIDs + summary metadata, newest first. `modifiedSince` filters by last-modified rather than shift date — use it for incremental re-sync instead of re-pulling a whole range |
| 8 | `getShiftRecord` | `uuid` (shift record) | Full form answers and asset references for one record — no field projection; always returns everything |
| 9 | `bulkGetAssets` | `uuids` — array of asset UUIDs, ≤100 | Signed download URLs (valid 1 hour) for up to 100 assets in one call — use instead of resolving asset URLs one `getShiftRecord` at a time |

**Rate limit on `getShiftRecords`:** 2 requests per second.


### Report types available via `getCachedReport`

| Report Name | Purpose |
|---|---|
| `dashboardShiftTable` | Shift summary (dates, project, status, scores, counts) |
| `dashboardResourceLabour` | Labour hours per shift, by role and supplier |
| `dashboardResourceMaterial` | Material usage and quantities per shift |
| `dashboardResourcePlant` | Plant/equipment planned vs. actual hours |
| `dashboardNarrative` | Narrative comments per shift, with image links |
| `dashboardProgress` | Planned vs. actual output by activity, with variance reason |
| `dashboardAllocation` | Resource allocation (fields vary by workspace configuration) |
| `dashboardWorklogEvents` | Worklog comment events tied to an activity |
| `dashboardAccessPossession` | Possession access timeliness (planned vs. actual) |
| `dashboardAccessNonPossession` | Non-possession access timeliness |
| `dashboardAccessOverview` | Access working-time and delay-category summary |
| `dashboardPeopleDetail` | Per-person shift hours, travel time, supplier, role |
| `dashboardSubcontractorLabourDetail` | Per-person subcontractor labour hours and variance |

**Performance tip:** limit date ranges to 1 month for supported reports.

**Example prompts:**
- *"Show me the labour hours for Project Alpha in January 2025."*
- *"What materials were used on site last week?"*
- *"Show me the details of the most recent shift record."*
- *"What workers were on the January 15th shift and how many hours did they work?"*

---

## Cost-aware usage

- **Cached reports first.** `getCachedReport` returns pre-aggregated columns; prefer it over pulling every `getShiftRecord` and computing the aggregate yourself.
- **One-month windows.** Wider date ranges are slower and pull more rows than most questions need — page by month if a longer range is genuinely required.
- **`modifiedSince` for re-runs.** Re-checking a period you already pulled? Use `modifiedSince` on `getProjects`/`getShiftRecords` instead of re-fetching the full range.
- **Quote what you use.** `getShiftRecord` has no field projection — it always returns the full record. Extract and quote only the fields your answer needs into any onward transcript; never paste the whole JSON.
- **`bulkGetAssets` over per-record asset URLs.** Batch asset UUIDs (up to 100) into one `bulkGetAssets` call rather than resolving each one via a separate `getShiftRecord`.

---

## Data Available Through MCP

Here's a summary of all the data you can access through the MCP server:

### Workspace Level
| Data | How to Access |
|---|---|
| All projects (name, status, tags) | `getProjects` |
| All people/labour resources | `getPeople` |
| Available report schemas | `getReportSchemas` |

### User Level
| Data | How to Access |
|---|---|
| Your assigned projects with roles | `getMyProjects` |

### Project Level
| Data | How to Access |
|---|---|
| User assignments (name, job title, role) | `getProjectAssignments` |
| Shift record listings (with date/supervisor/tag filters) | `getShiftRecords` |
| Supported dashboard reports (listed above) | `getCachedReport` |

### Shift Record Level
| Data | How to Access |
|---|---|
| Full form answers (all fields) | `getShiftRecord` |
| Supervisor, location, weather, times | `getShiftRecord` |
| Worker lists with roles and hours | `getShiftRecord` |
| Attached photos and documents | `getShiftRecord` (returns asset references); `bulkGetAssets` for signed download URLs in bulk |

---

## Example Conversations

Here are examples of questions you can ask your AI assistant once the MCP server is connected:

### Project Overview
> "What projects do I have access to? Give me a summary of each."

### Team Management
> "Who is working on Project Alpha? What are their roles?"

### Shift Analysis
> "Show me all shifts from last week on Project Beta. Were there any tagged as safety issues?"

### Labour Reporting
> "How many labour hours were logged on Project Alpha in January? Break it down by person."

### Productivity Tracking
> "What does the progress report look like for this month? Are we on track?"

### Material Usage
> "What materials have been used on site this week?"

### Detailed Shift Review
> "Pull up the shift record from January 15th. What did the supervisor note? Who was on site?"

---

## Troubleshooting

If tools are absent, check the Gather connection is enabled and authorised in ChatGPT Plugins. On authentication errors reconnect through the host's browser login. Run the Gather setup skill to check project access and configured reports. See `docs/install.md`.

## Support

Contact support@gatherinsights.com or https://help.gatherinsights.com.
