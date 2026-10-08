# Lightweight app guide

Last reviewed against the product specification on 2026-09-05.

## What Lightweight is

Lightweight is a workout logger and training companion for people who train
across routines and gyms. It combines fast workout logging, reusable routines,
gym-aware records, progress views, gym discovery, a Passport of completed gym
visits, and privacy-controlled social features.

People sign in with Apple or Google. Lightweight does not expose an email-and-
password sign-in flow to consumers.

## Main navigation

The app has five bottom destinations:

1. **Feed** — completed workouts, achievements, and friends who are training.
2. **Discover** — gym search, maps, and gym filters.
3. **Logger** — the prominent center `+`, which opens Start workout.
4. **Routines** — routine folders, training plans, and saved-gym management.
5. **Profile** — identity, history, rank, featured statistics, Passport, and
   Settings.

Passport is opened from its globe card on Profile; it is not a bottom tab.

## Start and log a workout

1. Tap the center `+`.
2. Choose a recent routine, **Empty workout**, or **Log without exercises**.
   If a workout is already active, resume it from the top of this sheet.
3. Check the compact gym selector. Lightweight normally preselects a useful gym
   automatically, so gym choice does not block starting.
4. In the logger, add or reorder exercises and enter each set's relevant values,
   such as load and reps, time, distance, or count. A routine copies its exercise
   order and targets into the workout.
5. Complete sets as training progresses. Previous values and personal-record
   context use the selected gym where machine history is gym-specific.
6. Finish the workout, review the summary, and save it. If saving is still
   syncing, the workout remains visibly pending rather than disappearing.

The compact active-workout control returns to a minimized workout. Rest timing
uses remembered per-exercise preferences rather than a fixed routine value.

## Routines and plans

Open **Routines**.

- Tap **New routine** to build one manually.
- Tap **Explore** for **Smart Trainer**, **Build with ChatGPT**, and
  Lightweight's curated plans. Before the public ChatGPT listing is available
  in the installed app, Build with ChatGPT shows **Coming soon**.
- Use folders to group routines. Folders can be collapsed, renamed, reordered,
  and deleted without deleting the routines inside them.
- A routine can be started from the Start workout sheet, its Routines row, or
  its detail page.
- A routine's overflow menu supports editing, moving, copying, sharing, and
  deleting it.
- The shared **All gyms** routine is portable. Eligible saved gyms can also have
  gym-specific variants without changing the shared base.

Starting a routine copies its structure into a new workout. It does not edit
the routine when set values change during that workout. After an
exercise-backed session that started from **Empty workout** is saved,
Lightweight shows **Save this workout as a routine?** Choose **Save** to create
an unfiled routine from the completed exercises under the workout's finished
title, or **Not now** to continue to the recap without creating one. This offer
does not appear for routine-backed sessions, copied workouts, exercise-free
logs, sessions without a completed exercise, or joint workouts. A full Core
routine library follows the ordinary routine-capacity flow before creation.

## ChatGPT connection

The public Lightweight connection combines two separate capabilities:

- this static guide answers general questions about using Lightweight without
  accessing an account; and
- the permissioned MCP connection can analyze complete training history—including
  completed workouts and exercise-free gym check-ins—and current saved routines through
  bounded server-side aggregates, page through exact history when a focused
  drill-down is needed, search the exercise catalogue, and create or update
  saved routines behind explicit confirmation.

Connect Lightweight in ChatGPT, sign in with Apple or Google, and approve only
the requested read-training and/or routine-write permissions. ChatGPT can use
all eligible completed workouts and exercise-free check-ins, plus current saved
routines, for server-side aggregate
analysis, including training trends, exercise progression and plateau evidence,
personal records, and weekly muscle-group set attribution. Complete history is
not returned as one unbounded raw payload; exact workouts and routines are
available through cursor-bounded pages when the question needs them.

For OAuth identity and workspace-domain controls, ChatGPT receives an opaque
Lightweight account subject identifier, the account's verified email, and its
verification status. It never receives the Apple or Google password or
provider tokens.

The connection may read whether the account is Core or Pro, how many saved
routines it has, its applicable routine limit, and how many routine slots
remain. It uses that entitlement context to explain whether a requested routine
can be saved, but it cannot read payment methods, receipts, renewal details, or
other billing data.

To create a routine, ask ChatGPT to consider the available training context and
your goals, schedule, equipment, preferences, and relevant limitations. It must
show the exact name, folder, exercise order, and every set target, then wait for
an explicit request to save that exact proposal. To update an existing routine,
it must show the complete before/after diff and receive a separate explicit
confirmation. ChatGPT cannot delete a routine, start a workout, or create,
edit, or delete workout history. It also cannot delete routine folders. A
confirmed routine may be placed in an existing private folder, or in a named
private folder that the connection creates or reuses.

The public MCP no longer creates routine drafts. A real draft created by an
older connection can still be opened in Lightweight and **Approved** or
**Rejected** until it expires after seven days. Approval saves one ordinary
routine; rejection changes nothing.

There is no separate ChatGPT paywall. Complete-history aggregates, core
analysis, and bounded exact-history drill-down are available to every owner.
The ordinary app entitlements still apply: Core can retain four routines while
Pro has unlimited routine capacity, and gym- or routine-specific analysis
scopes keep their existing Core/Pro availability.

Connection management and revocation live in
**Settings → Data & integrations → ChatGPT**. Ordinary users never need
ChatGPT Developer mode or an MCP URL. Adding a permission to an existing
connection requires disconnecting it in that screen, reconnecting from
ChatGPT, and selecting the additional permission during consent.

## Gyms and Discover

Open **Discover** to browse nearby or searched gyms, open the full map, and
filter results by useful training details. A selected gym page can show public
facts, equipment evidence, and visit context when available.

Open **Routines**, then tap **Gyms** to manage saved gyms. The home gym appears
first and supplies useful default context, but every workout still keeps its
own gym. Missing gyms can be added through the app's gym contribution flow.

Location is used only for nearby suggestions and visit verification. It is not
continuous tracking. Nearby suggestions can be controlled in **Settings →
Location**. Raw location samples used for selection or verification are
discarded after producing the result.

## Passport and gym-aware records

Open **Profile** and tap the Passport globe card to see gyms and countries where
completed workouts have been recorded. Verification state affects visit
evidence; an approximate map pin alone cannot verify a visit.

Records follow the equipment:

- standardized portable equipment, such as barbells, dumbbells, kettlebells,
  and bodyweight, compares globally; and
- machine exercises compare performances at the same gym, because machines can
  differ substantially between locations.

## Progress and profile

Open **Profile**, then use **Statistics**, **Calendar**, **Leaderboard**, or
**Measurements** below the featured-stat area. These views cover personal
training analysis, workout history by date, eligible comparisons, and body
measurements.

Profile contains the person's identity, workout history, rank, featured
statistics, Passport preview, and settings entry. A completed authorized
workout produces one calm Feed card; individual sets do not become separate
posts.

## Privacy and social controls

New profiles default to private until the person chooses otherwise during
onboarding. Profile privacy is the main workout-audience control:

- a private profile shares workouts with accepted friends; and
- a public profile may share workouts publicly.

Active-workout presence is off until the person opts in and is visible only to
accepted friends. It can show gym identity and start time, never raw
coordinates. Blocking removes profile, Feed, comment, and presence visibility
in both directions.

The ChatGPT data surface can include completed workouts and exercise-free gym
check-ins; workout, routine, and folder names; session and routine-update times;
exercise names and identifiers; set metrics; routine structure; technical IDs
needed to select the exact workout, gym, routine, or folder; a canonical gym
name or user-entered one-off place label exactly as saved; aggregate training
measures; and the plan label and routine-slot counts needed to explain routine
capacity. It excludes separate address, coordinate, and other location fields,
notes, media, social data, wearable-health data, payment and billing details,
and credentials. Its training read is a bounded server-side aggregate over
complete eligible history, with cursor-bounded pages for exact drill-down
rather than unrestricted bulk history access.

Complete-history aggregates and cursor-bounded exact-history pages are
available to Core and Pro owners. Existing gym- and routine-specific analysis
eligibility still applies where Lightweight's ordinary plan rules require it;
routine creation also respects the owner's saved-routine capacity.

## Settings and support

Open **Profile**, then the Settings control. Settings organizes account and app
controls including Appearance, Notifications, Training, Location, Privacy,
ChatGPT, integrations, data management, and support/legal information.

- **Settings → Privacy** keeps usage analytics and crash diagnostics separate
  and off by default.
- **Settings → Location** controls nearby suggestions and supported reminder
  permissions; there is no master location switch.
- **Settings → Data & integrations → ChatGPT** shows active connections,
  granted categories, any real legacy drafts that still remain, and revocation
  controls when the integration is available.
- For an account-specific problem, a missing workflow, or an issue not covered
  here, use `https://getlightweight.com/support`.

Some integrations and operating-system capabilities are platform-specific. Do
not promise an iOS-only permission or health integration on Android.
