---
name: find-people-at-an-event
description: Show who is going to a researched conference and why, filtered by role, company, fit or relationship (speaker, sponsor, exhibitor, engaged attendee). Use when the user asks who will be at an event, who there matches their target customer, wants a list of people or companies from it, or asks why someone is on the list.
---

Work from evidence the workspace already holds. Nothing here spends anything.

1. **Resolve the event.** Call `list_my_events` and match the user's words to a saved event. If it is not saved, hand over to the `plan-a-conference` skill. If research has not finished (`event_overview` shows `research.status` other than complete or partial), say what has been found so far and when to check back.
2. **Filter, do not dump.** Call `list_event_people` with the narrowest useful filters: `q` for a role, company or name; `relationship` for speakers, sponsors, exhibitors or engaged attendees; `category` for sponsor, exhibitor or speaker companies; `fit` for STRONG and PLAUSIBLE when the user wants the people who match their target customer; `edition` for a past year. Default `limit` is 40; page with `offset` only when the user asks for more.
3. **No target customer yet?** When the answer carries a `note` saying no target customer is set, nobody has a fit verdict: tell the user that in one line, give the settings link from the note (the target customer is set in the Prompt Prospect app, not here), and answer with the unfiltered list instead. Do not guess who matches.
4. **Present people with their evidence.** For each person give name, headline, company and the one-line reason they are on the list (the evidence excerpt and source); when they were checked, add their fit and the reason. Group by relationship when the list mixes them. Companies come from `list_event_companies` with their role, fit and how many of their people are in the event.
5. **Go deeper on request.** `get_person` returns one person's profile, every observation and the other conferences they are listed at; use it when the user asks "why is this person here", doubts an entry, or asks where else they speak. `search_prospects` searches across every saved event when the user asks about a person or company rather than one event.
6. **Save decisions.** When the user says they want to meet someone, call `set_people_status` with `pursue` (or `watch` for later, `dismiss` to drop), passing the people's `link_id` values from `list_event_people` as `link_ids`. Notes, meetings and outcomes are the `keep-track-of-people` skill.

Boundaries: attendance is only ever what the evidence shows; say "listed as a speaker" or "engaged with the event's posts", never "will attend". A fit verdict is Prompt Prospect's judgment against the saved target customer, so present it as "judged a strong fit", not as fact about the person. Do not fabricate contact details; the tools return LinkedIn profile URLs, not emails or phone numbers.
