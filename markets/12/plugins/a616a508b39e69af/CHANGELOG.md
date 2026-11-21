# Changelog

All notable changes to this plugin are documented here.

## 0.2.14 - 2026-11-05

- Updates the OpenAI listing tagline and requests all supported permissions through a new public client registration. Most requested permissions are preselected at consent; Organization Website Knowledge and Search remain opt-in. Existing grants, organization controls and write ceilings are unchanged.

## 0.2.13 - 2026-11-05

- Explains the optional Organization Website Search permission, encrypted short-lived session access, current-organization scope, and reconnection after expiry. Existing client defaults and grants stay unchanged.

## 0.2.12 - 2026-11-02

- Listing screening: get_listing adds a brochure state (extracted, gated, unavailable, failed, pending, not_selected or withheld) with a plain message, so a brochure behind a broker buyer portal or deal room is reported as one to upload to a deal, not as a missing brochure. Offering memorandum facts are described as preliminary and come from the current extraction only. They now include tenant, building and suite counts, the clear height range, office build-out, parcel numbers, and occupancy and WALT with the date the memorandum states them. In-place rent is not returned. In search results, has_documents counts only documents worth opening and is null when the links could not be read. Search results also add om_withheld, which names a field left empty because its offering memorandum figure came from a document EQUIRE could not match to the listing; get_listing shows that figure with a caveat. Listing records now report listing_contract_version 4.

## 0.2.11 - 2026-11-02

- Declares a registered public OAuth client and default Deal Intake permissions for OpenAI. Existing connections and grants stay unchanged; uploading the package alone does not prove the publisher adopted the new registration. Retains the 0.2.10 listing price-basis behavior.

## 0.2.10 - 2026-11-02

- Listing screening: price and cap rate sorts and the minimum and maximum price now count property prices only. A loan price, starting bid, raise amount or other non-property amount no longer leads a price sort or matches a price range; a sort lists such a listing last and keeps it in the result set, while a price filter excludes it. This holds while classification is on; with it switched off both use the stated amounts. Search results add excluded_by_price_basis, which counts the listings a filter excluded apart from the listings a sort listed last, and records now report listing_contract_version 3. The sale_price_usd value is unchanged.

## 0.2.9 - 2026-11-01

- Adds Deal Intake access guidance for confirmed deal creation and file attachment, preserving administrator choices and existing grants. Updates client setup and permission-upgrade instructions.

## 0.2.8 - 2026-11-01

- Adds confirmed private upload handoff guidance for sandbox files, with hash verification, short-lived completion tickets, credential handling and truthful host acceptance limits.

## 0.2.7 - 2026-11-01

- Listing screening: search and listing records now state what a listing's amount is. A loan sale, auction, capital raise or other non-property amount is labeled (Loan Price, Starting Bid, Raise Amount and so on) and never called an asking price, its price per square foot and cap rate stay withheld, and an unassessed listing makes no structure claim. A classification still pending review keeps its label and says so, a failed lookup is reported as unread, and a lease is marked not applicable. Records add an interest kind, price and size basis, structure badges, a classification state and the gates behind each ratio; sale_price_usd keeps its value beside is_property_price.
- Adds confirmed deal creation, document and property photo intake guidance, with intake status, host file-transfer limits, and explicit retry semantics.

## 0.2.6 - 2026-10-29

- Skills, README and listing copy call a prospecting mandate an Investment Mandate and prospecting results Deal Sourcing results, matching the Deal Sourcing area in EQUIRE; no tool or skill behavior change.

## 0.2.5 - 2026-10-15

- Adds the ChatGPT demo recording link to the OpenAI review metadata; no tool or skill behavior change.

## 0.2.4 - 2026-10-14

- Listing category is now Finance, which matches the plugin's commercial real estate investment purpose; no tool or skill behavior change.

## 0.2.3 - 2026-10-14

- Listing copy rewritten around the analyst's IC preparation; no tool or skill behavior change.

## 0.2.2 - 2026-10-14

- Market research skill: attaching a report now links and indexes it without reading its figures, so a linked-only result is expected. Figures come from the next research run or Continue fact review. Web pages may be turned off on a deployment, while PDF links are supported (a PDF can still be unreachable). Attaching a report that is already linked to the deal reports it as already linked without fetching it again.
- Retrying named report sources now reports skipped sources with a reason, and refuses before starting a run when none of the named sources can be retried.
- A prospect's source count now reads as unknown rather than zero when it could not be read.

## 0.2.1 - 2026-10-13

- The plugin's documentation link now opens the EQUIRE connect guide.

## 0.2.0 - 2026-10-13

- One EQUIRE plugin for Claude, ChatGPT, Codex, and Cursor, published from a single public repository with matching manifests for each host and one shared connection to `https://www.equire.ai/mcp`.
- New onboarding skill: connect EQUIRE, choose an organization, and learn what the assistant can and cannot change.
- Investment workflow skill, previously ChatGPT and Codex only, now ships to every host and covers document evidence across deals, deal notes, diligence items, review-item proposals, and the interactive EQUIRE workspace.
- Every skill now shares the same ground rules, including a confirmation step that states the exact change before any tool that writes or stages a change, no presentation of the assistant's own arithmetic as an EQUIRE figure, and rate changes reported in basis points.
- Underwriting what-if applies a basis-point change to the saved value, and market research keeps deal names, tenants, and prices out of web search requests and states when a run or attached report uses the organization's metered research allowance.
- Market research, portfolio triage, and underwriting what-if skills gained steps for metro trends, weekly activity, and proposal readback.
- 512 px PNG icon for directory listings.

## 0.1.x and earlier

- Separate packages for Claude (five workflow skills) and for ChatGPT and Codex (one investment workflow skill), each connecting to the same EQUIRE server.
