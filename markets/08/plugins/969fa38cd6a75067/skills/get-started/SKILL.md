---
name: get-started
description: "Help a user start or resume Orendro setup, choose what to track, personalize supported preferences, and complete a first useful action. Use for setup, getting-started, and Orendro-specific \u201cwhat can I do?\u201d requests. Do not interrupt an ordinary logging or read request with mandatory setup."
---

Start from the user's immediate goal. If they have already asked for a concrete
Orendro action, complete that action before offering optional setup.

Read [shared rules](references/shared-rules.md) before operating.

For a setup request:
1. Confirm that the intended Orendro connection is available. If authentication
   or legal acceptance is required, use the host's supported connection flow or
   the exact link returned by the service. Never request passwords or tokens in
   the conversation and never mark legal acceptance on the user's behalf.
2. Read onboarding_status. If incomplete, call onboarding_next. Reuse known
   profile/context information rather than asking the user to repeat it.
3. Explain Orendro in one sentence. Establish what the user wants help with first
   if that is not already clear. Ask essential returned questions naturally, one
   decision at a time, reusing known information.
4. Save answers through onboarding_update using its actual accepted fields,
   current state version and an idempotency key for the intended change.
5. As soon as the chosen action has the context it requires, offer to do it now:
   log a described item, inspect groceries, prepare a workout, record time, or
   save a supported preference. Do this before optional goals, preferences or
   the tour. Execute only the action the user chooses and show the real result.
   Never create demo records or mark deferred setup as completed.
6. While the user is continuing setup, use the next question already returned by
   onboarding_update. Do not fetch next/status again unless recovering from a
   conflict or missing result. Honor supported skip/defer choices. If the server
   still requires a field the user declines, do not fabricate a skip: ordinary
   logging can proceed with that setup section unfinished.
7. Offer nutrition target estimates only when wanted. Ask for required estimator
   inputs only for that purpose, show the estimate as an estimate, and save the
   target only when the user accepts the reviewed recommendation.
8. Save reusable preferences only through an available authorized preference
   contract. Verify the saved result. If persistence is unavailable, say the
   preference applies in this conversation and identify the supported next step.
   Do not use another endpoint or a direct database write as a substitute.
9. After the first useful action, offer at most one optional next step: goals,
   personalization, or a check-in routine. If the user declines, continue
   ordinary use without repeated setup invitations.

For a returning or completed account, answer the requested goal directly or
resume the selected unfinished part. Do not rerun all welcome questions.

Output: one concise explanation or confirmed result, then at most one useful
question. Distinguish connected, ready to log, optional personalization, and
verified scheduled routines. Never claim these are the same state.

The nutrition use case is log-only. Select nutrition_targets only when the user wants optional manual or estimated targets. Estimator inputs are requested only for requestRecommendation=true; do not invent a nutritionMode argument. A just-connected user can use the setup action or listing starter; OAuth does not itself invoke an unsolicited greeting.
