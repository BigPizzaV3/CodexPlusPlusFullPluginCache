---
name: make-a-training-plan
description: Show a weekly Broche Ballet training plan from real classes or a real program. Use when a dancer asks to make a training plan, find classes, achieve a goal, plan their practice, or choose what to dance on certain days.
---

# Make a training plan

The dancer's own words decide the days, the length, the level, and the focus. Show the plan first before saving anything. Use only classes and programs the tools return.

## What you need from them

- Which days of the week they want to dance (e.g. Monday, Wednesday, Friday)
- About how many minutes on each of the days (e.g. 20 mins 2 days, 45 mins 1 day)
- Their level, in their own words (for example, never danced before, returning after a break, 2-3 years ballet experience)
- What is their relationship to pointe? Already en pointe, Returning to pointe after a break, Dreaming of pointe shoes, not interested

If they want a plan and name none of these, ask which days and how long they want to practice, and plan a general class they can do this week. Ask only for what they have not already said in their initial prompt. Summarize the parts of their request that you do have before asking for what's missing. If they are not asking for anything about pointe, then you don't need to ask them about their pointe goals.

If the dancer mentions wanting to work on multiple goals and topics, don't try to search for a program or class with all of the goals in one. Split up the goals or topics and search for individual classes or programs for each. Suggest a training plan split that would combine the various goals and topics into one plan.

## Look up real classes

When the dancer is signed in with an active membership:

1. Call `get_my_week` so the plan can mention what is already on a day. Leave it there.
2. Call `list_custom_programs` when they mention a plan that Julie or Broche had already made for them. You can read it. You cannot edit it.
3. For a multi-week path, call `list_programs`, then `get_program` with an id from that list, and plan from that program's classes.
4. For separate classes, call `search_catalog`. `query` is required. `durationMaxMinutes` means at most that long. `durationMinutes` means about that long. `level` and `instructor` are ordinary words, matched against tags and titles. Display a separate individual class using the Class UI provided. 

When they are a guest, or the member tools say they need to sign in or need a membership:

1. Still make the plan. Offer that if they would like to create a free account, the plan can consist of only free classes. If they agree, call `list_free_classes`. That list is the free set of classes.

If `filtersRelaxed` or `filters_relaxed` is true, tell them these are the closest matches.

Use only titles, lengths, and links the tool returned.

- A member class has `title` and `watchUrl`. `duration` is seconds. Show minutes as that number divided by 60, rounded to the nearest minute. If `duration` is missing, leave the minutes off. Use the Class UI provided with the plugin.
- A member program has `title` or `name`, and `url`.
- A public item has `title` and `canonical_url`. Minutes come from `duration.minutes` or `duration.label`.

If a search returns nothing, say so and try one broader search. Leave the day empty rather than naming a class the tools did not return.

## Show the plan

Write a short week they can dance, in plain words. For each day give the day, the class or program title, the minutes when you have them, and the link. Then stop. Do not add it to My Week until they approve it.

A program on a day stays one program. List its classes only when they asked what is inside it, and only the classes `get_program` returned.

A live class from `list_live_events` can sit on the plan as something to attend.

If they ask to add these classes to My Week, favorite them, or take something off a day, show the plan and stop. Saving to My Week is outside this skill.

## Leave these alone

- Subscriptions, prices, canceling, and upgrades. Skip `list_offers`.
- Another dancer's account, email, or plan.
- Whether they are ready for pointe, or what to do about pain. For their own pointe practice plan, call `list_pointe_consultations` and use only that result. If no consultation plan was returned, then choose any pre-pointe class.
- A class name, length, or link that no tool returned.
- Technique suggestions, medical advice, or any question about pain.