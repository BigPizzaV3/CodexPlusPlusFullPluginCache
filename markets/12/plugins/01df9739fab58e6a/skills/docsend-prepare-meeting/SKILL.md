---
name: docsend-prepare-meeting
description: Create a concise, sourced meeting brief using accessible DocSend documents and engagement activity. The user can identify a meeting by person, email, company, or calendar event.
---

# Prepare for a Deal Meeting

Use the DocSend MCP to connect meeting context with observed engagement and relevant document contents. Produce the supported portions of the brief even when some sources are unavailable.

Example requests:

- “Prepare me for a meeting with Bob Smith.”
- “Prepare me for a meeting with bsmith@xyz.com.”
- “Prepare me for tomorrow’s meeting with Acme based on what they’ve viewed.”
- “Set up a brief one hour before each meeting on my calendar.”

## Identify the meeting and purpose

Use the person, email, company, date, or meeting details provided; the user may or may not supply a meeting purpose. If an upcoming meeting is unidentified, discover an available, authorized calendar connection and use its event title, start time, attendees, description, and linked materials. Resolve relative dates in the user's timezone. Distinguish similarly named or recurring event instances.

If calendar access is unavailable or the relevant event remains unclear, proceed with what is known. Do not require a meeting date or purpose before preparing the supported brief. A name or email alone can support a counterparty brief; do not invent a meeting date or purpose. Label any inferred purpose as an assumption. Ask for clarification when identity ambiguity could materially change attribution, as described below.

## Match people to DocSend activity

Use `search_contacts` to match the provided or calendar-attendee email to DocSend visitors. These contacts represent visitors, not a complete recipient or delivery list. Search by name when appropriate; if only email addresses are present, use authorized calendar/contact evidence, an established name-to-email pattern, and company-domain context to assess likely matches.

A domain alone establishes possible company affiliation, not a specific person's identity. Do not generate an address and treat it as a verified match. When evidence strongly supports one reasonable match, state the assumption and its basis. If multiple plausible matches could materially change the brief, ask the user to choose, identifying candidates by email and relevant dates. Do not attribute activity on weak or ambiguous evidence; continue with unambiguous materials while clarification is pending.

When a company-specific domain is established, search for relevant visitors from that company and include useful activity from other people. Check actual email-domain boundaries rather than loose substring matches; do not group people by public email-provider domains. Keep each person's activity separate and identify any uncertain affiliation.

## Gather activity and materials

Retrieve visits with `list_visits`. For a specific visitor, resolve the contact first and use `contact_id`. For room-wide activity, use `space_id` from `list_spaces` and omit `contact_id`. Follow pagination to cover the relevant scope; disclose incomplete retrieval. Contact `total_visits` is a lifetime total, not a count for the meeting window.

By default, use the 30 days immediately before the meeting start, in the user's timezone, and state the exact start/end dates and timezone. Exclude activity after the meeting. For a future meeting, distinguish the requested window from coverage available as of preparation time. If the meeting date is unknown, cover the 30 calendar days prior to the day the user invokes the skill, in the user's timezone. State that fallback and its exact date range; do not ask for the meeting date merely to establish the activity window. Include older activity only when it adds useful context and label it separately.

The current `list_visits` schema has no date-range parameter: filter returned timestamps locally, and do not assume pagination order unless documented. Only stop early on a date boundary if the tool guarantees that ordering. Preserve the distinction between no matching records, inaccessible records, and incomplete pagination.

Select activity and documents relevant to the meeting purpose. Use `search_documents` / `list_content_library` for Library materials and `list_space_content` for room materials; they are separate surfaces. Read relevant accessible documents, including material linked from the meeting when authorized. Call `read_document` once without `page`, download its `file_url` exactly once for a full-document read, and analyze locally. Use a page request only for a specific-page question or when file access is unavailable; do not loop over every page as a substitute for the full-file download.

Report only observable events and supported measures. The current visit records expose views, pages, viewing percentage, and duration; they do not establish a download event. Report downloads only when another available source explicitly records them. Total viewing duration is in milliseconds; per-page duration is in seconds. A view, download, long duration, or repeated visit does not prove interest, concern, comprehension, or purchase intent. Frame possible implications as interpretations and talking points as suggestions.

## Write a concise, scannable brief

Lead with the most useful meeting takeaway or, when clear, the meeting goal, grounded in available evidence. Do not invent a goal when the purpose is unclear. Include the meeting date, counterparty, and purpose when known; label assumptions. Do not fabricate missing meeting details. Prefer short bullets over long paragraphs.

Use short sections suited to the available information. Adapt these headings to the request rather than treating them as a fixed template:

- **Goal:** What the user should aim to learn, explain, or agree on. Omit this section when the goal is unclear; do not force a generic goal from limited context.
- **DocSend activity:** A brief summary of the exact activity window and timezone, preparation cutoff, and the most relevant materials, with document evidence and engagement presented together.
- **Prepare / Bring:** Specific documents (linked for easy reference), figures, or topics to have ready.
- **Questions to consider:** Suggest up to three optional, high-value questions only when they would materially help the user prepare. Tailor them to the meeting purpose and evidence, prioritizing important discrepancies or gaps. Do not script the meeting or imply the user should ask every question. Omit this section when there are no especially useful questions.
- **Agree before you leave / Next step:** A concrete decision, owner, or follow-up date to propose. Label proposed commitments as suggestions; do not present them as already agreed.

Omit empty sections, generic advice, and repeated points. Include only information that could affect the meeting. Keep observed facts distinct from interpretations and suggestions, explicitly labeling suggestions.

## Present activity and source materials together

For each relevant document, link its name at first mention, alongside who viewed or interacted with it and when, plus useful facts or topics from its contents. Include relevant activity from other people at the company here, identifying each person accurately rather than attributing their activity to the meeting attendee.

Keep engagement and document facts together where useful. Avoid a redundant document inventory or repeated facts. Link specific documents in Prepare / Bring when they should be ready for the meeting, including a repeated link when needed for easy reference; do not let a mention-once convention prevent useful preparation links. Include relevant accessible materials even if there is no recorded engagement, making that distinction clear.

If a document is a sample, fictional, inaccessible, or its contents could not be verified, say so clearly alongside that document. Do not present sample or fictional figures as the counterparty's actual results, or infer unverified contents from a filename. Distinguish observed document engagement from verified document facts.

If only some of the total activity is relevant, distinguish the total from the selected items. State the scope and period of any total, and do not imply the selected documents or visits exhaust all activity. Disclose incomplete retrieval rather than giving an unsupported total.

## Keep evidence clear

Use verified returned or user-provided source URLs; never invent document URLs from internal IDs or create sharing links to supply citations. Prefer durable source links over expiring download URLs. If no usable source link is available, identify the document by name and relevant page/section at its first mention and state the citation limitation.

Include activity dates or periods where available. Distinguish observed facts from interpretations and suggestions. Explain when unavailable information or an uncertain match limits the brief, while providing the portions supported by available evidence. Do not imply that a view or download proves interest, concern, or intent.

## Recurring preparation

For a one-time brief, offer recurring preparation after delivering the brief, unless the user has already requested or declined it. Offering it does not authorize creating an automation.

When recurring preparation is explicitly requested, use the available, authorized calendar and automation connections and discover the supported scheduling tool. Reuse or update a matching automation rather than creating duplicates. Resolve the calendar scope, timing relative to meetings, timezone, and delivery destination from context; ask only for missing choices needed to configure it. Use the current chat as the default destination when supported. Preserve the user's requested one-hour lead time when specified.

Verify that calendar access and the scheduling mechanism can support event-relative preparation. A recurring calendar check is not an exact event-triggered guarantee. If using a supported polling approach, disclose its timing precision and handle rescheduled/cancelled meetings, changed attendees, and duplicate preparation for the same event. Keep runs quiet when there is no newly actionable meeting. Do not claim exact one-hour delivery unless supported.

Save instructions to re-read the current event, resolve attendees, retrieve fresh DocSend activity, and produce this brief for each relevant meeting. Confirm the actual schedule and destination only after the scheduling tool succeeds. If calendar or scheduling access is unavailable, explain what is missing without claiming the recurring task is active. Do not send briefs to attendees or other people unless the user explicitly requests it.

## Tool boundaries

Discover live tool schemas and obey their access checks. On DocSend `insufficient_scope`, ask the user to re-authenticate before retrying. Check text errors as well as structured responses before reporting success. Keep result values named `id` or ending in `_id` internal; identify items by names, emails, verified URLs, or dates.

Preparing a brief does not authorize changing documents, Spaces, sharing settings, invitations, or calendar events. Do not call live write tools merely to test this skill.
