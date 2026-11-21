---
name: docsend-deal-activity-briefing
description: Summarize visitor engagement and internal activity across DocSend Spaces or shared documents for a requested reporting period. Use when someone asks for a one-time deal activity briefing, Space engagement summary, or summary of document visits and changes.
---

# DocSend Deal Activity Briefing

Produce a concise briefing for the current request using the DocSend MCP. Cover visitor engagement and internal changes separately, with clear reporting dates and data limits.

## Set scope and reporting period

Identify requested Spaces or shared documents from the request and conversation. Use the user's timezone and state the exact dates covered.

- “Yesterday” means the previous calendar day.
- “Last week” means the previous calendar week, Monday through Sunday.
- If the period is missing or ambiguous, default to the previous calendar week and explicitly state that assumption. Preserve any unambiguous dates supplied by the user.
- If resource scope is unspecified or ambiguous, use clear context where possible; otherwise default to accessible, enabled Spaces the user owns or collaborates on for that period, stating the assumed scope. Do not silently expand to all company Spaces or all Library documents. If the resource cannot be resolved without a material risk of reporting the wrong deal, ask for clarification while proceeding with unambiguous resources.

Compute calendar boundaries in the user's timezone, accounting for daylight-saving changes, then convert timestamps for tool calls. Filter the interval from the start of its first day up to, but excluding, the next day after its last day. For a period still in progress, disclose the retrieval cutoff.

## Resolve resources

Use `list_spaces` to resolve Space names and `search_documents` / `list_content_library` to find requested Library documents. Use `list_space_content`, starting with a Space's returned `home_folder_id`, for its documents and folders. Follow pagination and inspect relevant folders. The Content Library and Space content are separate surfaces.

Exclude Spaces explicitly marked disabled. Zero activity is not evidence that a Space is disabled. State exclusions concisely when relevant. Use `all_company` only when the user asks for all company Spaces and their access supports it.

## Retrieve activity and assess coverage

Use `list_visits` scoped by `space_id` for a room or `document_id` for a shared document. Omit `contact_id` for general engagement summaries; use it only for a specifically requested visitor after resolving them with `search_contacts`.

The current visits tool has no date-range parameter. Follow pagination and filter visit timestamps locally to the reporting period. Do not assume pagination order or stop at an old record unless documented ordering guarantees full coverage. For Space changes, use `list_space_events` with `from` and `to`, following pagination and applying the same reporting boundaries locally. Its end filter is inclusive, so exclude events at the next-day boundary locally.

For audit events, use `display_name` in all user-facing communication. Never expose raw event type values; use them only in tool filters. Attribute changes to the returned actor when identifiable, using their name or email. Do not infer the actor from Space ownership or assume every audit event is internal: visitor views, downloads, and signatures belong with visitor engagement. Inspect returned event details before describing what changed. If details identify only an update, do not invent the changed fields or claim a new document version without evidence.

For standalone documents, retrieve available visits. Space audit events are scoped to a Space: do not treat Library timestamps as a complete change log or claim standalone internal history is available when no supported source exposes it. If a requested document belongs to a known relevant Space, use that Space's accessible events and clearly scope the findings.

Track coverage separately for visits and internal activity for each resource. Distinguish:

- Successful complete retrieval with no in-period activity.
- Partial retrieval or incomplete pagination.
- Data unavailable because of plan or permission limits.
- Failed retrieval.

When the response establishes that the user's plan lacks Space analytics, state that the current plan does not include the Space analytics needed through MCP and that upgrading to an eligible DocSend plan, such as Advanced Data Rooms when identified by the tool, is required. Do not diagnose a generic permission or retrieval error as a plan limit. If entitlement is unverified, state the observed limitation without asserting which plan the user has. On `insufficient_scope`, ask for re-authentication before retrying. Continue with independently accessible data and disclose its limits.

## Compute only supported metrics

Report new or returning viewers, unique counts, downloads, and engagement changes only when available evidence supports them.

- Count identifiable viewers using stable internal identifiers or normalized email evidence where available; a display name alone may not identify a unique person. Keep anonymous visits separate from identified unique viewers. Do not turn visit counts into people counts.
- Define whether counts are per document, per Space, or across the briefing. Do not add per-resource unique counts and call the sum an overall unique count.
- Distinguish new-to-this-resource viewers from returning viewers only with sufficient earlier history for that same resource. If only the reporting window was retrieved, say “first observed in this period” rather than claiming a viewer is new. Lifetime contact totals do not establish prior visits to this deal.
- Visits expose views and viewing measures, not download events. Report downloads only when audit events or another source explicitly records them. Keep bulk downloads distinct from individual-document downloads unless their contents are known.
- Visit and audit logs can describe the same view. Use visits for view metrics and events for complementary actions; do not sum both into duplicate activity counts.
- Total visit duration is in milliseconds; per-page duration is in seconds. Convert units correctly. Describe notable changes only with a supported comparison baseline and label its dates and scope; otherwise describe the observed activity without a trend claim.

## Write the briefing

Start with a concise overall summary highlighting the most useful observed findings, the exact reporting dates and timezone, and any limits affecting the overall conclusion. Keep it clear, short, and scannable.

Organize the rest by Space or shared document, prioritizing notable activity. Link resource names with verified source URLs when available; do not construct URLs from internal identifiers or create sharing links for citations. For each resource, include relevant sections:

- **Visitor engagement:** Supported new/returning viewer information, documents viewed or downloaded, activity dates, and notable supported changes.
- **Internal activity:** Document additions or versions, file/folder changes, link creation or updates, and permission changes. Name the actor when identified in the activity data.
- **Recommended follow-ups:** Only concrete, actionable recommendations supported by the observed activity. Label them as recommendations and omit this section when none is meaningful.

Group resources with no activity in a brief closing line only when both relevant activity sources were successfully covered. For partial coverage, state specifically which source had no records and which was unavailable. Clearly identify resources whose activity could not be retrieved. Do not imply inaccessible data was reviewed.

Separate observed facts from interpretations and recommendations. Viewing and downloading do not establish purchase or investment intent. Do not overstate attention, concern, or understanding from duration or viewing percentage.

## Scope boundary

This skill produces a one-time briefing. It does not configure recurring delivery or create scheduled tasks. Handle any scheduling request separately, and only when a supported scheduling capability can run the workflow with DocSend access.

Discover live tool schemas and obey access checks. Keep result fields named `id` or ending in `_id` internal, referring to human-readable names, emails, dates, and verified URLs. Check text errors as well as structured results. Preparing the briefing does not authorize changes to documents, Spaces, links, groups, or permissions. Do not call live write tools merely to test this skill.
