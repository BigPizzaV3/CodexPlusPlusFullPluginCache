---
name: intent-sales
description: Use when the user wants to find Japanese companies that are actively researching a product category, learn why a company is a fit, build and maintain prospect lists, or send approaches by email, web form or phone through Sales Marker.
---

# Intent sales with Sales Marker

Sales Marker detects which Japanese companies are researching a topic right now
("intent"), and turns that into outreach. The tools cover four stages: find,
research, organise, approach.

Every tool acts inside the signed-in user's own subscription. Company and
contact data is real personal and corporate data about third parties — treat it
accordingly and never paste it somewhere the user did not ask for.

## Start here

Call `get_current_user` first when you need the user's own subscription, name or
product context. Call `get_products` to see what the user actually sells; most
intent questions only make sense relative to a product.

## Find companies

- `search_company_v2` is the main entry point. It filters by intent signals,
  industry, location, company size and more. Ask the user which product they are
  selling before guessing filters.
- `get_industries`, `get_prefecture_list` and `get_company_labels` return the
  valid values for those filters. Use them instead of inventing codes.
- `search_person_v2` and `search_department_v2` find people and departments at
  those companies.
- `get_intent_detection_results` and `get_intent_stats_for_graph` explain *why* a
  company surfaced — which keywords it researched and when.

## Research a company

- `get_company_approach_results` and `get_product_approach_results` show what has
  already been tried, so the user does not approach the same company twice.
- `search_meetings`, `get_meeting_details`, `get_note` and `get_properties` pull
  meeting history and AI notes. `get_note` and `get_properties` need both
  `objectID` and `interactionType` (for an online meeting, use
  `INTERACTION_TYPE_ONLINE_MEETING`).
- `get_meeting_details` takes `id`, not `meetingId`.

## Organise into lists

- `list_company_lists` / `get_company_list` to read, `create_company_list` and
  `add_companies_to_company_list` to build. Adding is idempotent, so re-sending
  the same ids is safe.
- The same pattern exists for people: `list_person_lists`, `create_person_list`,
  `add_persons_to_person_list`.
- `update_company_list`, `remove_companies_from_company_list` and
  `delete_company_list` change or destroy existing data. Confirm with the user
  before calling them, and never call `delete_company_list` speculatively — it is
  irreversible.

## Approach

These tools contact real people and companies. Call them **only** when the user
has explicitly asked to send, and show the user exactly what will go out first.

- `send_emails` sends intent emails to a company list or person list. Requires
  `senderEmail`, `title` and `content`, and exactly one recipient source.
- `send_forms` fills and submits companies' own website contact forms.
- `create_phone_calls` records calls that already happened; it does not dial.
- Sequences (`create_sequence`, `start_sequence`, `pause_sequence`,
  `update_sequence`, `delete_sequence`) automate multi-step outreach.
  `start_sequence` begins approaching real companies — treat it like a send.

## Working well here

- Resolve filter values with the lookup tools before searching; guessed ids
  return empty results that look like "no companies match".
- Prefer narrowing an existing search over running many broad ones — searches
  consume the subscription's credit.
- When a user asks "who should I contact at X", combine `search_person_v2` with
  the company's intent evidence rather than listing every employee.
- Summarise outreach results (`totalCount`, `skippedCount`) back to the user
  rather than restating the whole payload.
