---
name: trace-across-events
description: Find the other conferences a company, speaker, exhibitor or sponsor is listed at, across Prompt Prospect's catalog and the user's workspace. Use when the user asks where else a company exhibits or sponsors, which events a person speaks at, or whether a prospect will be at another event.
---

The cross-event answer comes from two tools; both read Prompt Prospect's own index and spend nothing.

1. **A company.** Call `get_company` with `name` (or `domain` when the user gives a website). Starting from an event, pass `event_id` and the company's `company_id` from `list_event_companies` instead, which also returns its role, fit and people at that event. The answer's `other_events` lists each edition with the year, dates, place, the role the source gives (exhibitor, sponsor, partner, speaker company, attendee company) and `in_workspace_event_id` when the user already has it saved. `found: false` means the index has no such company; say so rather than guessing.
2. **A person.** Call `get_person` with `event_id` and the person's `link_id` (from `list_event_people`) as `event_person_id`. Its `other_events` lists the conferences the same person is listed at, with their role at each and `employers` as the sources recorded them. A person cannot be looked up by name alone: find them at an event first, or use `search_prospects` across the user's events.
3. **Present it as a timeline.** Sort by date, say the role at each event ("exhibiting at HLTH 2026, sponsored Money20/20 2025"), and note `year_estimated` when a year was inferred. Offer `plan-a-conference` for an event the user does not have yet (`catalog_slug` is given when the event is in the catalog).

Boundaries: a listing is a listing; say "listed as an exhibitor", not "will be there". Engaging with an event's posts is not counted as going, and the tools say so in `other_events_note`. Never pad the list with events the tools did not return.
