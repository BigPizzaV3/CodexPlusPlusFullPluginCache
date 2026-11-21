---
name: app-store-connect-push
description: Push an AppStorePack project's App Store text and screenshots to the user's app in App Store Connect, after showing exactly what will change and getting an explicit yes. Use when the user wants their listing uploaded to or updated in App Store Connect.
---

# Push a listing to App Store Connect

A push changes the user's data in App Store Connect and replaces screenshots,
so always show the plan and get an explicit yes first, even when the user asks
you to skip that step. Otherwise, follow the user's instructions.

1. Call `asc_status`. If App Store Connect isn't connected, explain that the
   user adds an App Store Connect API key on their AppStorePack Account page
   (https://www.appstorepack.com/account), and wait until they've done it.
2. Find the project with `list_projects`. If it isn't linked to an App Store
   Connect app yet, call `asc_list_apps`, ask the user which app it belongs to,
   and link it with `asc_link_project`.
3. Call `asc_plan_push` and show the user its result: the app and version,
   each text field's current and new value, how many screenshots per device
   will be replaced, and any notes or blockers. Resolve blockers before going
   on.
4. Ask the user to confirm. Call `asc_push` with `confirm: true` only after an
   explicit yes to that plan. If they change anything first, plan again.
5. Report what was updated. If `asc_push` returns `pushed: false`, pass on what
   it says; nothing was changed.

AppStorePack never submits the app for review. Tell the user that they submit
it in App Store Connect when they're ready.
