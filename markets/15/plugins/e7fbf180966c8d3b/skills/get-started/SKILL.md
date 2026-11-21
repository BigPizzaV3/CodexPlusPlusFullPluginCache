---
name: get-started
description: How to connect Riven and what to ask it about your Apple Watch strength workouts.
---

# Getting started with Riven

Riven is automatic exercise tracking and muscle failure detection on the Apple Watch. Each set is scored
0-100 % for how close it came to true muscle failure: 90 %+ reached failure, 75-89 % near failure,
50-74 % working, under 50 % stopped short.

1. The user needs the Riven app on iPhone and Apple Watch, signed in with Apple (Settings → Profile → Sign in with Apple).
2. Connect Riven and sign in with the same Apple ID, then tap Allow.
3. Pass the user's IANA time zone as `timezone` when you know it.

Good first questions: "Which muscles did I train to failure this week?", "Show me my last workout set by set",
"Compare this week with last week". To read the whole history, call `get_all_workouts` and follow
`next_cursor` until it is null. The tools are read-only; Riven never shares heart rate or personal details.
