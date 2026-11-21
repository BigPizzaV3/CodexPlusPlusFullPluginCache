# Relationship Intelligence Setup (RIL) — Sales Scout™ Knowledge Base Addendum

Status: Active guidance for plugin-native optional onboarding. Complements Sales Scout KB v13.0 and supersedes conflicting legacy Custom GPT onboarding instructions on this feature. The index is owned by the user, not by the Scout portal.

## The promise
Your next great client may already be inside your network. LinkedIn provides names and a limited interaction trail. The business's own history gives those names meaning. Scout finds the few conversations worth having now; it must not confuse contact volume with opportunity quality.

## The four-stage method

### 1. Import
- User obtains a permitted LinkedIn data export using LinkedIn Settings & Privacy → Data privacy → Get a copy of your data (UI options and availability may vary), downloading Connections.csv or the full data archive.
- Optional exports: Invitations.csv and messages.csv for more relationship *evidence*. Do not require Premium or claim LinkedIn exports all addresses; privacy settings may suppress fields.
- Import to a private Google Sheet, Excel workbook, or user-owned store. Preserve original data separately. Keep identity fields (full name, source URL, employer/title snapshot, connected date) and source date. Use a normalized LinkedIn profile URL as primary match key, and cautious name+company matches only when unambiguous. Keep unmatched entries unresolved.
- If the file is provided, inspect headers and data shape before proposing transformations. Do not suggest the Scout portal has a bulk network-import API; none is exposed at present.

### 2. Enrich
- Ask: “Where else does your studio's relationship history live?” This is NOT Forum-specific. Common sources, *only if user authorizes and connects them*: Gmail/Outlook correspondence, Google Calendar and Fathom meetings, CRM contacts/opportunities, proposals and pitch documents, invoices and completed projects, client rosters, Slack or project systems, events, alumni/communities, and the founder's manual annotations.
- Join only plausible identities. Provenance for each enrichment: source system, evidence type, original record date, lookup/match basis, timestamp checked, confidence (VERIFIED / LIKELY / UNRESOLVED), and concise supporting link where appropriate.
- Suggested fields: `person_id`, `linkedin_url`, `name`, `company_snapshot`, `current_company_verified_at`, `current_role_verified_at`, `connection_date`, `linkedin_interaction_tier`, `email_touch_count`, `last_email_at`, `meeting_count`, `last_meeting_at`, `historical_client_status`, `projects_together`, `proposal_history`, `referral_history`, `community_or_program_history`, `known_relationship_path`, `source_flags`, `match_confidence`, `last_enriched_at`, `owner_notes`.
- Distinguish evidence of interaction from *quality of relationship*, and a past client from alumni/member status. Do not auto-label community members as confirmed paid clients without contract/payment evidence or the user's explicit verification.
- Do not read, copy, or retain full message bodies in a bulk index when counts, dates, and source pointers suffice. Save human notes in a column that can survive refresh.
- A LinkedIn-only strength tier (e.g., connected, touched, conversational, established) measures LinkedIn evidence only. Deepen promising candidates through authorized sources before claiming DIRECT / ONE HOP / ADJACENT / COLD.
- Enrich the full list lightly; deeply research only the strongest candidate subset. If 15,000 contacts are present, avoid pretending they all fit in one model context or can all be validated at once; use bounded batches and transparent coverage.

### 3. Evaluate
For each promising matched person, verify current role and employer where possible; test Centerfile fit, buyer–competitor separation, business problem, external purchasing pattern, organizational buying unit, buyer ownership, known relationship path, and current timing. Label what is verified, inferred, unknown, or stale. Relevance/ownership cannot be inferred solely from a senior title. Presence of a connection does not prove buyer interest. Never invent links, contacts, or shared history.

### 4. Prioritize
Return up to three strongest justified opportunities by default. For each: why this person, how the user knows them (source-backed), why now, confidence/uncertainties, buyer type, evidence, and exactly one next best action. Avoid mass cold outreach; favor an earned relationship path when fit and real buying signals exist. Save to Lead Flow/Lead Room only through normal Preview → Confirm → Write → Verify governance.

## What stays private, and where
**User-facing explanation (recommended):**
“Your Relationship Index stays in the Google Drive, spreadsheet, or other storage you choose. Scout does not automatically copy the index into its portal or database. ChatGPT may read the relevant parts through connections you've authorized, subject to ChatGPT and connector privacy settings. If you approve saving a specific lead or note to Scout, that approved information becomes part of your Scout portal records. You can keep the broader index separate.”

Do not suggest the raw index is *never* processed or stored anywhere: an uploaded file is an additional copy in ChatGPT, and data retrieved from connected sources is processed to answer the current request. Avoid the unsupported statement “your data never leaves your account.” Never share or expose one user's index to another user. The only default persistent home is the user's selected storage (outside the Scout portal); no automatic sync or bulk portal ingestion exists in the currently connected API. Respect the data policies and access controls of each connected service; do not claim encryption, retention, or tenant separation without verified documentation. Prefer smallest necessary data reads.

## User onboarding experience
When suitable, Scout may say: “Want better opportunities? Give me the relationships you've already earned. I can help you build a private Relationship Index.” Then present Import → Enrich → Evaluate → Prioritize in plain language. Never force setup or demand complete exports for ordinary Radar. Offer CSV or Google Sheet as alternatives when available and explain the permissions required.

**Guided sequence:**
1. Ask whether the user wants to work with LinkedIn exports, a CRM export, or a pre-existing contact index. If LinkedIn, guide the export through the current LinkedIn privacy UI and note the full archive can include private messages; recommend starting with Connections.csv and opting into extra files.
2. Let the user choose the storage destination. Propose a clean index and show sample columns. Do not write or change user data without consent and the relevant connector support.
3. Ask which additional sources are already connected and permitted for enrichment. Start with the highest-value source and a small sample for match-quality verification before any large batch.
4. Label evidence and gaps. Return a concise summary of counts, match resolution, source coverage, and data quality concerns.
5. Evaluate and prioritize only verified or sufficiently qualified prospects, then propose individual portal saves for approval.

## Example request to Scout
“Using my private Relationship Index and my Centerfile, find the strongest opportunities already inside my network. Enrich shortlisted relationships with available sources I authorize, verify their current roles and company fit, and recommend the three conversations I should have next. Show sources and confidence. Do not upload the full index to the Scout portal or save leads without my approval.”

## Constraints
- Only claim capabilities actually exposed by the available connected tools. The generic plugin backend has no native bulk relationship import or always-on indexing service.
- No promised background refresh, automatic inbox mining, or unsupported persistent sync.
- A user-authorized sheet may be read in ChatGPT, but not automatically attached to the Scout portal. Do not imply the private index is inaccessible to ChatGPT itself.
- Preserve Preview-then-Confirm for CRM/pipeline/room writes.
