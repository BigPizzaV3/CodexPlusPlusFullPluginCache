---
name: build-partner-documents
description: Draft an Excellent Partner document — a pro forma for a new location, a pitch deck or a quarterly investor update — from the narrative ChatGPT writes and the figures Excellent traces from the group's own records, for a person to review and publish in Excellent; and add an investor to the Partner registry. Use for "draft a pro forma for a second location", "build a pitch deck for the Scottsdale raise", "write the Q3 investor update", "add Sam Lee from Ridge Capital to our investors".
---

# Build Partner documents

This skill stages drafts, and can add an investor contact (an undoable change). You write the words;
Excellent computes every figure from the group's own records and places its tables around them, so a number
in your narrative never becomes a figure in a table. Nothing is published, shared or sent to an investor until
a person does it in Excellent. The drafts need the Partner module and the Partner permission in Excellent
(adding an investor, the Partner module and the Events permission); without them the tool says so.

## 1. Read the story first

1. `report` with `period: "quarter"`, and again with `period: "year"` — booked, collected and outstanding
   revenue, pace against goal, pipeline and win rate, and the per-venue rollup. This is what the tables will
   show, so the narrative should agree with it. Read `dataBasis`: say so if the figures are sample data.
2. `overview` — the group's venues.
3. Ask what the document is for and who will read it.

## 2. Write the narrative

Plain text: a line starting `#` or `##` is a section heading, `###` a sub-heading, a line of `---` a page or
slide break, and every other run of lines a paragraph. Leave the figures to Excellent's tables; if a sentence
needs one, use the report's figure as given, never your own. Show the narrative and wait for a yes. A Spanish
version (`narrative_es`) is optional and keeps the same headings, paragraphs and breaks in the same order.

A deck or update leads with a `focus`, one of `booking_momentum`, `collections_discipline`, `margin_quality`,
`event_value` or `expansion_footprint`. Pick one the report's figures support; one they don't is refused.

## 3. Draft

- **Pro forma:** `draft_pro_forma` with `prospect_name`, `narrative`, `steady_state_events_per_month`,
  `ramp_curve` (1 to 24 shares of steady state from 0 to 1.5, e.g. `"0.4, 0.6, 0.8, 1"`),
  `build_out_cost_minor` and `monthly_fixed_cost_minor` in cents, and `horizon_months` (12 to 60). Ask the
  person for every assumption; never invent one. If the group's records trace no average event value or
  margin, the answer says so: ask for `avg_event_value_minor` or `gross_margin_ratio` and draft again.
- **Pitch deck:** `draft_pitch_deck` with `deck_name`, `narrative` (`---` starts a new slide), an optional
  `focus`, and optionally `pro_forma_id` — one of the group's pro formas (`list_documents` or `search` with
  `kind: "document"`) whose tables the deck carries. A group with no completed events or invoices has no
  track record to show yet.
- **Investor update:** `draft_investor_update` with `period` (`YYYY-Qn`, e.g. `2026-Q3`), `focus` and
  `narrative`. Excellent adds that quarter's figures with the quarter before beside them; a quarter with no
  events or invoices is refused.

If the answer says the group's records could not be read in full, nothing was drafted: try again in a moment.

## 4. Add an investor (if asked)

Say who you will add and wait for a yes, then `add_investor_contact` with `full_name` and optional `email` and
`organization`. Give back the `change_id` and say it can be undone. It adds a contact to the Partner registry
only; nothing is sent to them.

## 5. Hand off

End with the link and one line: "This is a draft. Open it in Excellent to check the figures and the words, then
publish it there; nothing is shared with an investor until you do."

Safety: the documents are drafts behind their review link; adding an investor happens only on the person's yes
and returns a `change_id` that `undo` puts back, once, for 30 days. Nothing is published or sent to an investor
from ChatGPT, and nothing is deleted.
