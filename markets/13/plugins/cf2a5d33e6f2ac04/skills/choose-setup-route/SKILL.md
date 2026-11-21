---
name: choose-setup-route
description: Help a founder choose between UAE free zones and the Dubai mainland, and shortlist free zones for their business, using Dubai Setup Index. Use when the user asks which free zone, free zone or mainland, where to set up a UAE company, or to compare setup routes.
---

# Choose a UAE setup route

Explicit user instructions take priority over this workflow.

1. **Pin down the business.** What it does, where its clients are (UAE mainland
   or abroad), where the work is performed, whether it needs premises, and how many residence visas at the
   start. Ask for what is missing, or state the assumption you made.
2. **Check the activity.** `search_activities`, then `get_activity` for the best
   match: which lanes list it (IFZA, Ajman Free Zone, Dubai mainland), and its
   approvals and premises requirements. A lane marked not-verified is
   unverified, not unavailable.
3. **Frame free zone against mainland.** `get_comparison` with
   `free-zone-vs-mainland` (or the IFZA/Ajman/mainland pairs) and
   `get_setup_chooser`. The mainland estimate is licence fees only and priced
   by owners, not visas; a free-zone figure is a package. Never present them as
   equivalent.
4. **Shortlist zones.** `list_free_zones`, then `get_free_zone` for each
   candidate. Compare starting prices only at the same visa count and term.
5. **Answer.** A short list with why each fits, its price at the requested
   visa count and what that price covers, and what must be confirmed. A route
   is a possibility to investigate, not confirmed eligibility. Cite each page.

For a founder's scenario, call `plan_business_setup` with the business type first.
Use its missing inputs and activity-specific questions, then select an exact
activity. `get_setup_requirements` returns a partial sourced checklist;
`compare_setup_scenarios` compares the chosen routes under the same assumptions.
Use `dubai_only` when the licence must be in Dubai. A regulated route with
unconfirmed permissions must not be recommended on a generic package price.

For price lists, specify `visa_count` and `term_months` (default 12), use
`sort: "price_asc"`, and `include_unpriced: true` to see exclusions. A published
quota-only or partner-channel offer may be absent from comparable results;
never describe every missing result as unpublished. Read freshness, source,
conditions and unresolved costs alongside each price.
