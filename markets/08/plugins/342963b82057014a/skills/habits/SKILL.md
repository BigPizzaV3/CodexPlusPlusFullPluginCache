---
name: habits
description: "Build habits and lifting routines and log runs, workouts, sleep, mood, or anything else in beckett from what the user did, then summarize how it's going. Use when the user starts a habit or lifting routine, reports an activity, workout, or measurement, or asks how a habit is going."
---

# Habits and trackers

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- To start a habit, create one with the goal the user describes, such as three runs a week. If they want a nudge or a weekly look back, set up a check-in too, as the check-ins skill describes.
- Log something the user did or measured, such as "I ran 3 miles" or "slept badly," as an entry on the matching habit or tracker. If none matches, offer to create one.
- For questions like "how has my sleep been?", read that tracker's history, then summarize what the entries show, without medical advice.
- For lifting, start a workout tracker in beckett if they don't have one. Set up a routine from the days, exercises, and targets they give, or change the active one. If they haven't said, ask about their goals, training days, and equipment instead of making up a program. Log a finished workout with the exercises and sets the user gave, and the routine day if they named one. For a question about one exercise, such as how their squat is going, analyze that tracker for the exercise.
