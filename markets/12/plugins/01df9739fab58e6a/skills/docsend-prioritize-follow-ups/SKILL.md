---
name: docsend-prioritize-follow-ups
description: Use DocSend engagement activity to recommend which investors, buyers, or prospects to follow up with. Use for prioritizing outreach, reviewing engagement changes, and drafting personalized follow-ups.
---

# Prioritize Deal Follow-Ups

Example: “Which investors should I follow up with this week, and what should I say?”

Use the DocSend MCP to recommend a short outreach priority list grounded in observed engagement. Draft messages when requested; sending is a separate action requiring explicit authorization and an available messaging capability.

## Resolve scope and period

Identify relevant Spaces or shared documents from the request and context. Use `list_spaces` for Spaces, `list_space_content` for room documents and folders, and `search_documents` / `list_content_library` for Library documents. Follow relevant pagination. Keep Space content distinct from the Content Library. If resource scope is missing, use the relevant context or accessible Spaces the user owns or collaborates on and state the assumed scope; ask only when a materially ambiguous deal cannot be resolved. Do not silently expand to all company resources.

If no reporting period is specified, use the last 30 days up to preparation time and state that assumption, exact start/end dates, cutoff, and the user's timezone. Distinguish a requested outreach timeframe, such as “this week,” from the historical engagement window. Preserve explicitly requested reporting dates.

## Retrieve contact and viewing evidence

Retrieve `list_visits` scoped by Space or document. Use `search_contacts` to resolve a specific person before using `contact_id`; omit it for general resource-wide queries. Contacts represent observed visitors, not a complete recipient or delivery list. Resolve ambiguous same-named people using email and context, asking when the ambiguity could change attribution. Do not guess a recipient address.

The current visits schema has no date filter. Follow pagination and filter returned timestamps locally. Do not assume pagination order or stop at an older record unless documented ordering guarantees coverage. Keep relevant resource and reporting-window filters when gathering contact-specific history. Do not use a contact's lifetime visit total as their activity for this deal or period.

Gather supported evidence such as:

- Most recent visit and its date.
- Repeat visits and whether they occurred on distinct days.
- Documents or pages viewed, viewing percentage, and coverage of relevant materials.
- Viewing duration, with total visit milliseconds converted correctly and per-page seconds treated separately.
- Downloads only when explicitly recorded by available audit events or another supported source. Views alone do not establish downloads.

Use `list_space_events` when needed for available Space download evidence. Use event `display_name` values in user-facing text, never raw event type values. Do not count audit views and visit records as separate visits when they describe the same activity. Keep bulk downloads separate from individual-document downloads unless contents are known.

Retrieve comparison history only when needed to support claims about engagement changes, and state the baseline dates and scope. Separate anonymous activity from identifiable contacts; do not assign an anonymous or shared-link visit to the intended recipient without evidence. Disclose retrieval failures, plan/permission limits, and incomplete coverage. Lack of records is different from unavailable data.

## Compare contacts and prioritize

Explain the factors used instead of inventing a DocSend engagement score. Weigh available signals in context: recency, repeat visits, breadth of relevant document coverage, supported changes over time, and explicit downloads may support different next actions. Do not let a long viewing duration alone dominate the ranking or imply that the document was actively read throughout.

Use known deal purpose, stage, and user-provided relationship context when available. A contact opening more documents may simply have received more materials; avoid presenting unequal access or missing data as a fair engagement comparison. Do not claim someone is an investor, buyer, or decision-maker unless context supports that role. Qualify close rankings or state when evidence does not meaningfully distinguish contacts. Do not manufacture a priority order when no identifiable, usable evidence is available.

When grouping by company, use verified company information or label domain-based affiliation as an assumption. Match actual company-specific domain boundaries, not loose substrings. Do not group public email-provider domains as one company. Keep individual contributors identifiable within a company summary; do not imply a colleague's activity belongs to the primary contact.

Describe inactivity as “no observed activity in this period,” not proof of lost interest. Viewing, repeated visits, downloads, duration, and coverage do not prove purchase or investment intent. Keep observed facts distinct from possible interpretations and recommendations.

## Return a short prioritized list

Start with the reporting window, scope, and a brief explanation of the comparison factors. For each recommended contact or company, include:

- **Contact or company:** A human-readable identity, with affiliation assumptions when needed.
- **Observed engagement:** Relevant dates, materials, and supported measures.
- **Why follow up:** Why a follow-up may be useful, framed as a recommendation rather than a conclusion about intent.
- **Next action:** A concrete, proportionate suggestion tailored to the evidence and known context.

Link relevant documents or Spaces with verified source URLs where available; never construct URLs from internal identifiers or create sharing links merely for citations. Flag limited evidence and comparisons based on partial data. If there is no defensible outreach recommendation, say so and identify what would help resolve it.

## Draft personalized follow-ups when requested

Use document topics and verified contents to make each requested draft relevant. When contents are needed, call `read_document` once without `page`, download its `file_url` once, and analyze locally. Do not loop over all pages when full-file access is available. If content is inaccessible, do not invent details from the filename.

Keep drafts concise with a useful next step. Avoid unnecessarily exposing detailed tracking information, such as exact viewing time, visit count, or page-by-page behavior, to the recipient. Do not claim prior discussions, unanswered outreach, concerns, or commitments without supporting context. Include only verified, appropriate source links already available; do not create new access permissions to complete a draft.

Deliver requested reusable drafts in the appropriate writing-block format. Preparing or displaying a draft does not authorize sending it or saving it into an external messaging account.

## Boundaries and tool handling

Do not send outreach without explicit authorization and an available messaging capability. If sending is authorized, resolve the intended recipient and message from that authorization and obey the messaging tool's requirements. Report send failures or uncertain outcomes accurately; inspect available status before retrying an uncertain send to avoid duplicates.

Discover live schemas and obey access checks. On DocSend `insufficient_scope`, ask the user to re-authenticate before retrying. Check text errors as well as structured responses. Keep result fields named `id` or ending in `_id` internal. Prioritizing follow-ups does not authorize document changes, access changes, invitations, or scheduling. Do not call live write tools merely to test this skill.
