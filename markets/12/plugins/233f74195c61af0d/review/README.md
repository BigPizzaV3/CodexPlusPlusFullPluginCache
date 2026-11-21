# Fitzap review materials

The current demo is the replacement recording supplied on 15 October 2026. The previous demo URL and raw recording have been removed from these submission archives.

Hosted demo: https://youtu.be/m11lXfk5FuA

The YouTube page is marked unlisted, identifies the replacement recording, shows 4:13 duration, and playback was started successfully. Browser verification used an existing YouTube session; anonymous playback was not separately tested. The URL is set in `extensions.com.openai.review.demo_recording_url`.

Local recording: approximately 4 minutes 13 seconds, 1906 × 942, with an audio stream. Sampled frames show a recipe push and its Nutrition app catalogue/details, a nutrition summary, and Workout template editing followed by app views. Sampling does not establish complete test-case coverage or a full privacy/audio review. Development case evidence and limitations are in [run-summary.md](run-summary.md).

The standard ZIP uses the hosted recording. The separate with-demo ZIP additionally contains the replacement at `review/product-demo.mov`.

## Running the cases

Use a dedicated reviewer account with sample data and sufficient permissions/entitlement. Start a fresh conversation for each case, keeping its follow-ups in that conversation. Compare actual tool calls and results against the pass criteria below. Record Passed, Failed, Blocked, or Not run with evidence. Do not treat tool-level rehearsals as a full conversational pass. Keep credentials in secure portal fields only.

The publisher must provision disposable reviewer-owned fixtures before write tests. Mirrored personal training history must not be described as synthetic. These scenarios are already embedded in `plugin.json` under `extensions.com.openai.review.test_cases` for import.

## Positive cases

### P1

Training review. Setup: reviewer account with at least four complete weeks of synthetic gym/cardio sessions, an exercise with repeated history and a PR, a stored coach report and a current metrics snapshot. Open a fresh conversation. Reads only; no report regeneration or writes.

**Prompt:**

> Review my last four complete weeks of training using my latest coach report and current training metrics. Show my weekly volume, all-time personal records, how a frequently trained exercise progressed, and the details of my most recent session.

**Expected tools:** get_account_status, get_coach_report, get_training_metrics_context, get_training_summary, get_personal_records, list_exercises, get_exercise_history, list_sessions, get_session

**Pass criteria:** Uses the reviewer account and returned timezone/units. Distinguishes report interpretation and app-computed metrics from recorded history; checks report week and snapshot freshness. Uses the last four complete weeks for summary/history. Follows pagination to identify a recent session (list_sessions is ascending), then reads its returned ID and kind. Reports only returned PRs and sets, labels estimated 1RM, incomplete coverage and unavailable/stale context, and makes no writes.

**Execution evidence:** See [run-summary.md](run-summary.md) for the observed development runs and outstanding checks.

### P2

Nutrition and energy comparison. Setup: synthetic nutrition backup active on the read-source account, at least seven days of diary coverage and synced goal context (dated saved targets or automatic phase preferences). Include a missing day where available to exercise unknown-intake handling. Reviewer writes remain isolated to the reviewer account.

**Prompt:**

> Compare my recorded calories and protein with my saved nutrition goals and estimated energy expenditure over the last complete week. Explain missing days and what these numbers can and cannot tell us.

**Expected tools:** get_account_status, get_nutrition_summary, get_energy_context

**Pass criteria:** Requests the actual last complete week with daily nutrition grouping and valid YYYY-MM-DD energy-context dates. Uses returned goals/estimates only for their supported dates; distinguishes estimated expenditure, saved goals and consumed intake. Missing entries remain unknown rather than zero. Explains stale/incomplete data and that cloud context cannot prove the targets currently displayed on the phone. Does not change goals or log food. If goal is null but preferences include normalCut, explains that automatic Cut is configured while no dated saved calorie/macro target record was returned. Does not describe the configured phase as absent, invent numeric targets, or claim cloud export proves TDEE import receipt.

**Execution evidence:** See [run-summary.md](run-summary.md) for the observed development runs and outstanding checks.

### P3

Workout draft creation and refinement. Setup: reviewer account has synthetic exercise history/templates and room for two pending drafts. In the same conversation, after creation, send: Make that pending draft three sets per exercise instead. Do not save it as a workout yet.

**Prompt:**

> Suggest a 45-minute upper-body workout based on my recent exercises and saved routines, and send it to Fitzap as a draft for me to review.

**Expected tools:** list_exercises, list_workouts, create_workout_draft, list_workout_drafts, update_workout_draft

**Pass criteria:** Creates one pending draft from supported schema inputs using the reviewer account. Explains that the user reviews and saves it in the app. On the follow-up reads the returned draft/current revision and revises that same draft to three sets per exercise, preserving unrelated details and original expiry. Returns the new revision and does not call edit_workout or claim a saved workout exists. Reviewer can verify the revised payload and unchanged expiry with list_workout_drafts without installing the mobile app; phone delivery is demonstrated separately by the publisher.

**Execution evidence:** See [run-summary.md](run-summary.md) for the observed development runs and outstanding checks.

### P4

Approved saved-workout edit. Setup: reviewer account owns at least one disposable cloud strength template, separate from mirrored read fixtures, with exercises/sets. After the initial read choose that fixture by its returned name and send: Rename this saved workout to Review Upper Body Updated. Keep every exercise and set unchanged. This direct instruction is explicit approval for that exact rename. The publisher provisions this fixture in advance; reviewers do not need to register or install the mobile app.

**Prompt:**

> Show my saved strength workouts so I can choose one to rename for this review. Keep their exercises and sets unchanged.

**Expected tools:** list_workouts, edit_workout

**Pass criteria:** Initial request only lists workouts and asks which disposable reviewer-owned template to rename; it makes no write before the follow-up approval. Reads that template and current sync_version. Calls edit_workout for its returned ID with name Review Upper Body Updated, expected_sync_version from the read and user_approved=true, omitting exercises so sets stay unchanged. Describes confirmed cloud update and possible phone sync delay. A follow-up read shows the renamed template; unrelated templates, completed history and mirrored fixtures remain unchanged. On conflict re-reads and reassesses rather than blindly retrying.

**Execution evidence:** See [run-summary.md](run-summary.md) for the observed development runs and outstanding checks.

### P5

Recipe delivery, reading, editing and public-link consent. Setup: publisher-provisioned isolated reviewer recipe catalogue, compatible assistant capabilities and capacity, with access to the declared write tools. Reviewers use the supplied account without registration or mobile app installation. The publisher demonstrates actual phone delivery in the demo recording. After reviewing the proposed recipe, approve adding it. The publisher supplies a delivered synthetic fixture for catalogue/read/edit checks. Follow up: Show me that recipe and change it to three servings. Finally request a shareable import link and, after the assistant explains public bearer-link access/24-hour expiry, explicitly approve publishing it.

**Prompt:**

> Suggest a two-serving oats and yogurt breakfast recipe with estimated macros per portion. Show me the ingredients and gram amounts before adding it to Fitzap nutrition.

**Expected tools:** push_recipe, list_recipes, get_recipe, edit_recipe, create_recipe_import_link

**Pass criteria:** Shows ingredient grams, servings and estimated macros before the approved push. Uses a fresh request_id, reports pending delivery rather than immediate phone success, and does not repeat a successful push. Uses list_recipes/get_recipe to read the created recipe and version. Revises it to three servings with the returned expected_version and consent rule; reports the queued result/version accurately without claiming phone delivery; publisher verifies phone delivery separately. Before publishing a link explains anyone holding it can read the recipe for 24 hours and waits for explicit approval. Returns the actual link/expiry; link import requires the user to open it and tap Import and does not log consumed food. Conflict and capacity errors are reported honestly without upsells.

**Execution evidence:** See [run-summary.md](run-summary.md) for the observed development runs and outstanding checks.

## Negative cases

### N1

Completed-history deletion is unsupported. Expected fallback: explain deletion must be performed in the app; no write tool, draft or recipe operation is called and no deletion is claimed.

**Prompt:**

> Delete my most recent completed workout session and all its logged sets.

**Execution evidence:** See [run-summary.md](run-summary.md) for the observed development runs and outstanding checks.

### N2

Exact GPS routes are unavailable. Expected fallback: explain that only route summaries (distance, duration, point count) are exposed and that the map is viewed in the Fitzap app; no coordinates or map are invented and no write tool is called.

**Prompt:**

> Show me the exact GPS route of my most recent outdoor run as coordinates I can put on a map.

**Execution evidence:** See [run-summary.md](run-summary.md) for the observed development runs and outstanding checks.

### N3

Recording completed sessions is unsupported. Expected fallback: explain that completed sessions are logged in the app/watch; do not create a workout draft or recipe as a substitute and do not claim a session was recorded.

**Prompt:**

> Log the five-kilometre run I completed yesterday as a finished session.

**Execution evidence:** See [run-summary.md](run-summary.md) for the observed development runs and outstanding checks.
