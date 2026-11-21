---
name: cardshow-prepare-show-day
description: Build and optionally apply a practical private plan for one exact CardShow event. Use when a user asks for a show-day brief, checklist, seller stops, target plan, packing reminders, an event game plan, or help marking checklist items or attendance for a saved or selected show.
---

# Prepare for a CardShow event

Turn one exact event into a useful collector plan. Keep suggestions separate from stored CardShow facts and make every write deliberate.

## Resolve the exact show

1. Use `cardshow_get_my_planning` when the user refers to a saved show or existing plan.
2. Use `cardshow_find_events`, `search`, or `fetch` when the show must be identified.
3. If multiple shows remain plausible, ask the user to choose. Never guess the show ID.
4. Call `cardshow_get_show_day_brief` with the exact show UUID before proposing a plan.

## Build the brief

Organize the result into:

- event facts and timing returned by CardShow;
- current attendance and private plan;
- remaining plan items;
- relevant seller, category, and featured-item leads;
- practical reminders; and
- uncertainties the collector should verify.

When an approved HobbyWise Hunt List is available, call `cardshow_recommend_events_for_my_hunt_list` for the show's place and dates and use only the result for this exact event. Otherwise, use existing CardShow plan items, seller declarations, and targets the user states in the conversation.

Do not claim a seller will attend with a particular item unless the returned show supply says so. Even then, describe it as seller-declared and unverified, not reserved or guaranteed. Do not invent prices, appraisals, travel times, floor locations, or opening hours.

## Propose a useful checklist

Prefer a short ordered checklist over a long generic list:

1. highest-priority targets or seller stops;
2. questions or evidence to verify;
3. items to bring;
4. budget or trade guardrails only when the user supplied them; and
5. logistical reminders supported by the show record or the user's instructions.

Present the proposed plan before changing CardShow.

## Confirm and apply

1. Refresh `cardshow_get_show_day_brief` and current planning.
2. Preview the exact show, plan status, notes, every new item, and any attendance change.
3. Ask for explicit confirmation of the complete effect.
4. Use `cardshow_upsert_show_plan` only for the confirmed private plan. It preserves existing items and avoids duplicate matching items on retry.
5. Use `cardshow_set_show_attendance` only for a separately listed confirmed final attendance state.
6. Re-read the show-day brief and report the stored result.

For completion changes, refresh planning, use the exact returned item ID, preview complete or incomplete, confirm it, call `cardshow_set_show_plan_item`, and verify. Never invent an item ID or mark a target found merely because a seller declared a category.
