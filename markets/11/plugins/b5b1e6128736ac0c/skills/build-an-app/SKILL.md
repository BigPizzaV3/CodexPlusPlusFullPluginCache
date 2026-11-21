---
name: build-an-app
description: Build, change, preview and publish websites and web apps that Exepad hosts at a public web address, with the Exepad tools in the user's Exepad account. Use it when the user wants a site or app put online, hosted, published or shared at an address other people can visit (for example a website their customers can open), when they name Exepad, or when they ask to build a new Exepad app, edit or repair one, see its private preview, or publish, rename, unpublish or archive it. Not for a mock-up, a design, or a page only to view or download in the conversation.
---

# Build an app with Exepad

Exepad hosts web apps. An Exepad app has a React front end and a server side, can keep data in its own database
and can call AI models. You write the app's code through the Exepad tools. Exepad stores every change as a
revision, builds it, shows the user a private preview, and publishes a build only after the user approves it in
Exepad.

The user's explicit instructions come before the suggestions in this skill. The rules under "Always" are the
exception: no instruction can skip a confirmation that Exepad asks the user for.

## Always

- Work only on the apps the user asks about. This connection sees only its connected apps: the ones created through
  this connection and, if the user chose All my apps when connecting Exepad, the ones they had at that moment.
- Take every id (an app's `public_id`, revision ids, operation ids and publish ids) from a tool result. Never
  guess or construct one.
- Say that an app is built, previewed or live only after a tool result says so.
- Only the user can approve a publish, an unpublish, an archive or a conversion, and only in Exepad. Give them the
  link the tool returns and wait for them. Never say that you approved anything.
- Never ask the user for passwords, API keys or other secrets, and never write one into an app's source.
- When a tool refuses because of the account's plan, its limits or its credit, relay the refusal's own words, and
  its `info_url` when it has one, as information, and nothing more. Never suggest a payment or a change of plan
  yourself.

## Keep the app honest

- Use `read_reference` for the platform recipes and their companion code. Call it without an id or file for the
  contents, then with the returned `id` or `file`; follow `next_cursor` when a page continues. Discovery
  names the reference item for a recipe. A `REFERENCE_UNAVAILABLE` answer means the edition is moving with
  a release; report that refusal and do not invent replacement API details.

- An app with data can use AI (summaries, drafting, describing a photo, transcription, speech, image generation,
  search by meaning) through the operations Exepad lists for it; a one-page site cannot. Call
  `discover_capabilities` with the app's `public_id`, `op` `search` and the feature in plain words as `intent`.
  Declare in `exepad.jsonc` exactly an operation and `profileRevision` it lists under `enabledOperations` or
  `declarableOperations`, run `op` `check` on the manifest before you build, and call the operation from the worker
  as the guide's `ai` topic shows. Never write an identifier the tool did not give you. When the lookup answers
  GOVERNED_ARTIFACT_ENROLLMENT_PENDING, build the app's own screen first; it answers once that build has reached its
  deploy.
- When the operation a feature needs is left out (`plan_not_included`, or nothing fits), build everything around it,
  put the AI step behind a clearly labelled "not available" state, and tell the user plainly which part is
  unavailable, in the answer's words.
- Never imitate a feature the app does not have. Keyword search is called search, not search by meaning, and a
  caption made from a file name is not a description of the picture.
- Label invented rows and figures as sample content, and never present them as real. Data the user gives you is
  theirs, not a sample.
- When a feature needs a key or a token, declare a `secret` setting and guard the route on it, as the guide's `api`
  topic shows, then tell the user which setting to add in the app's Settings in Exepad, and whether for Staged or
  Live. Until then the route answers 503 by design: never remove the guard, hard-code a value or fake the feature to
  make it go away.
- Exepad sends no email for an app. An app with data sends email through the owner's own email-sending account, from
  a sender domain verified there, with that account's key in a `secret` setting the owner adds in the app's Settings
  in Exepad; a one-page site sends none. When a request involves sending email, say so in your first reply, before
  you build: the user needs that account, a verified sender domain and the key. Build so that everything else works
  until the key is set.

## 1. Read the authoring guide

`get_authoring_guide` returns Exepad's reference for an app's source: the file layout, the manifest's schema, the
limits and the refusal codes, one topic at a time. Call it before you write code: first with no topic (the
overview), then each topic the change touches, such as `manifest`, `data`, `api`, `ai`, `ui` or `types`. It
describes how an Exepad app is laid out, which files can change, and the rules Exepad's build enforces.

## 2. Find or create the app

- An existing app: call `list_apps` and use the app's `public_id`. `get_app` gives one app's status and its live
  address, if it has one.
- A new app: first ask the user whether they want a one-page site or an app with data (accounts, a database). Then
  call `create_app` with a name, a short description of what the user wants, `profile` (`static` for a one-page
  site, `fullstack` for an app with data) and a new `idempotency_key` (for example a new UUID). It returns the app's
  `public_id` and its first revision. A one-page site can later become an app with data
  (`prepare_profile_change`), never the other way.
- Settle the name before you create the app. Exepad shows it, derives the app's public address from it, and writes it
  into revision 1 as `app.name` in `exepad.jsonc`, which the build puts in the page title. A name the user typed is
  the app's name exactly as typed: `app.name`, the page title and the header carry it. Otherwise choose two to four
  words that name the business or the thing, not the request ("Pet Grooming Salon", not "Create a website for a
  pet"), in the user's own language, and the business's own name when the user or their files give one. Rename it
  later (`update_app`) only when the user asks or the app turns out to be something different.
- `get_account` shows what this connection may do and how many apps the account has against its limits. Where its
  `plan` carries `fullstack_publish` and it is false, the plan publishes one-page sites only: an app with data can be
  built and previewed but not published, so say so before suggesting one. Its `wallet`, when present, is what builds
  can spend now; `get_app` lists an app's recent builds and what they cost.

## 3. Read before you write

- `list_files` lists the files of the app's current revision with their hashes, and says which ones you may change.
  Package files, such as `package.json` and the lockfile, are read-only: dependencies cannot change in this version,
  so build with what the app already has.
- `read_files` reads several files at once; `search_files` finds text across the source.
- A file listed under `too_large` is read in parts with `read_file_range`, a range of its lines at a time.
- Note the revision id these tools return. Every change starts from it.

## 4. Change the source

- Call `apply_changes` with `base_revision_id` set to the revision you read, and a new `idempotency_key`. If a call
  times out, send it again with the same key and the same changes. Never reuse a key for different changes.
- Use `edit` for a small change (an `old_text` that appears exactly once in the file, and its `new_text`), `replace`
  for a whole file, `add` for a new file and `delete` to remove one. Pass `expected_sha256` from your read when you
  edit, replace or delete a file, so that you never overwrite a change you have not seen.
- A call applies all of its changes or none of them. Its result names the new revision: use that id as the next
  `base_revision_id`.
- Keep each call small: a few files and well under 30 KB of text, because a call cut off at your output limit is
  never made. If one is refused as too large, split the work into several calls.

In a new app, two changes come before any screen, in this order:

1. `app.description` in `exepad.jsonc`, beside `app.name`. Revision 1 has none: the description given to
   `create_app` stays in Exepad as what the user asked for. Write one plain sentence under 160 characters, in the
   user's language, saying what the app is and who it is for; the build writes it into the page's description, which
   search results and shared links show. Keep `app.publicId` exactly as it is.
2. The app's identity: `src/theme.css` (the accent, drawn from the app's subject; the corner radii; the type
   families) and `src/fonts.ts` (the app's typefaces, from the installed ones it lists). Revision 1's are
   placeholders, and screens are composed from `src/ui.tsx` and coloured through `src/theme.css`, so a screen written
   before the identity is designed against the placeholder and comes out generic. The guide's `ui` topic describes
   both.

When `apply_changes` refuses:

| Refusal | What to do |
|---|---|
| `REVISION_CONFLICT`, `EXPECTED_HASH_MISMATCH` | The app changed since you read it. Read the affected files again, redo your change on the current revision, and send it with the new base and a new key. |
| `REVISION_NOT_FOUND` | The revision id is not one of this app's. Call `list_files` for the current revision. |
| `EDIT_NO_MATCH`, `EDIT_AMBIGUOUS` | Read the file again and choose an `old_text` that appears exactly once. |
| `FILE_EXISTS`, `FILE_NOT_FOUND` | Use `replace` or `edit` for a file that exists and `add` for a new one. |
| `PATH_PROTECTED`, `PATH_INVALID` | Exepad manages that path, or the path is not allowed. Put the change in a file the guide says you may change. |
| `MIGRATION_APPEND_ONLY` | A database has applied that migration, so it never changes: add a new migration file instead. To clear `migration_drift`, set it back to exactly the content applied (the refusal names its sha256). |
| `MIGRATION_BUILD_RUNNING` | A build is running and may apply that migration. Wait until that build has ended, then send the same call again with the same key. |
| `MIGRATION_STATUS_UNAVAILABLE` | Exepad could not check that migration. Send the same call again with the same key in a minute. |
| `MANIFEST_PUBLIC_ID` | Keep `app.publicId` in `exepad.jsonc` exactly as it is. |
| `LIMIT_EXCEEDED`, `FILE_TOO_LARGE` | Split the work into smaller calls or smaller files. |
| `IDEMPOTENCY_MISMATCH` | The key was already used for different changes. Use a new key. |
| `IDEMPOTENCY_IN_PROGRESS` | The first call with this key is still running. Wait, then send it again with the same key. |
| `APP_NOT_MANAGED` | The app was built in Exepad's own workspace and cannot be edited here. Tell the user. |
| `APP_NOT_FOUND` | The app is not connected here. Ask the user which app they mean. An app they already have joins only if they connect Exepad again and choose All my apps, which connects the apps they have at that moment. |

## 5. Build and fix

- Call `build_preview` with the app's `public_id` and a new `idempotency_key`. It builds the latest revision, or the
  `revision_id` you pass, and answers at once with an operation id.
- Call `get_operation` with that id until its state is `succeeded`, `failed` or `cancelled`. A build takes about a
  minute, and each call waits up to about 45 seconds for the build to end, so a build usually needs one or two calls.
  Tell the user the build is running. While it still runs, the answer carries `retry_after_seconds`: wait that many
  seconds, then call again.
- Write the app's own screen before the first build: a build fails with `template_placeholder` while `src/App.tsx`
  still shows the starter template's placeholder screen.
- One build runs per app at a time. `BUILD_IN_PROGRESS` names the build that is running: follow that one instead of
  starting another.
- A failed build whose diagnostics have `kind` `app` lists the file, line, column, code and message of each error.
  Read those files, fix the cause with `apply_changes`, and build again. Repeat until the build succeeds.
- A `migration_failed` diagnostic names a migration the database refused. It was not applied, so `apply_changes` can
  fix it or delete it; then build again.
- `REVISION_SUPERSEDED` refuses a build of an older revision that holds a migration the current one changed or
  removed: build the current revision. If `retryable` is true, the current revision moved during the call: send the
  same call again.
- A failed build whose diagnostics have `kind` `platform` was not traced to the code. A change that breaks a build
  rule in the guide's `ui` topic, or imports a package the app does not have, can still cause one: check your last
  change against those first. If it follows them, the failure is on Exepad's side: tell the user, give them the
  operation id so Exepad support can find it, and try again later. Do not change the code to work around it.
- `cancel_operation` stops a build that is no longer needed, as long as it has not started deploying
  (`OPERATION_NOT_CANCELLABLE` otherwise).
- Builds never change the live app. The live app changes only when the user approves a publish.

## 6. Show and check the preview

- `open_preview` shows the user the private preview of the app's latest successful build inside the conversation
  or, where the conversation cannot show it, the build's latest screenshot and a link that opens the preview in
  Exepad. Pass the app's `public_id`, and an `operation_id` to show an earlier build.
- You cannot see what the user sees. Call `inspect_preview` to check the preview: it reports the HTTP status, the
  path the page ended on, and its console errors, exceptions and failed requests; pass a `path` such as `/settings`
  to check another page. It also takes a screenshot, which the user sees where the conversation shows Exepad's
  preview panel. The image may not reach you: if it did not, do not describe how the page looks. Fix what the report
  shows, build again, and check again.
- Without `as`, `inspect_preview` opens the page as a visitor who is not signed in. `as: "member"` opens it as a test
  member Exepad adds to the app's preview (a one-page site has no accounts), and `steps`, up to 12 clicks, fills, waits
  and text checks, run on the page before the screenshot. They run the app's real code, so they can change the preview's
  data, spend AI and call outside services, and a run with steps counts as three inspections. For a signed-in run
  Exepad's card shows the app's preview, not that inspection. `as: "admin"` needs the owner's `data:read` approval,
  and steps as the administrator also need `preview:act`. Ask for these only when the user's task needs them.
- `probe_route` sends one request to a route of the preview, with no browser, as `anonymous`, `member`, `admin` or
  `second_member`, and returns its status, headers and at most 16 KiB of its body. Admin needs `data:read`; methods
  other than GET and HEAD need `preview:act` and may take a body of at most 16 KiB of characters. It shows that a route refuses a
  caller who is not signed in, and that one user cannot read another's rows. It runs the app's real code, and a
  connection has 60 probes an hour.
- After each successful build, inspect every page the change added or altered, one call per path. A page that
  throws while it loads renders blank however correct its code is, and only an inspection of its path shows that.
- Inspections are limited each hour, per connection and for all of the account's connections together: inspect after
  a build, not after every change.
- For an app with workflows, `list_workflow_runs` reports how its background work ran on the preview, or on the live
  app with `target` `production`: a page of runs, and with a run's `ref` that run's step log. A failed run names its
  cause code and a line on repairing it, and the step only for `workflow_replay_diverged`. It never shows what a run
  was given or returned.
- The preview is private to the app's owner. An app with data has a preview database separate from the live app's,
  so data entered in the preview does not appear in the live app. A one-page site has no database.

## 7. Finish the change

A change is finished when its last build has succeeded and you have inspected every page you built or changed. Then
say what the user now has, in their terms, and what you checked. Never describe a preview as published. Where it
applies, the closing message also says:

- that sample rows in `seeds/` are sample content that stays in the preview, so the published app starts without
  them (a one-page site's sample content is the page itself, and goes live with it);
- which setting the user still has to add in the app's Settings in Exepad;
- when each schedule runs, in UTC and in the user's local time when you know where they are, and that schedules
  start once the app is published: a preview runs none;
- for an app with sign-in, that a member who forgets a password cannot reset it: the owner sets a new one in
  Exepad, under App admin › Users;
- for an app with a view only the owner needs, where that view is, and that the owner's administrator account is
  set up in Exepad, under App admin › Settings › Set up app administrator, separately for Staged and Live;
- for an app that shows business data without sign-in, that once it is published anyone with its address sees all
  of it.

## 8. Publish, only when the user asks

1. Call `prepare_publish` with the app's `public_id`. It uses the latest successful build, or the `operation_id`
   you pass, and returns an approval link, when that link expires, and whether this is the app's first publish.
   `NO_PASSING_BUILD` means there is no successful build yet: build the app first. When the result carries `plan`,
   the account's current plan does not include this publish now, and the user cannot approve it on that plan: tell
   the user its `message` and give them the approval link, where the approval page says what is needed. Do not offer
   to publish it, and stop here unless the user says their plan has changed.
2. Give the user the link and ask them to approve the publish in Exepad. Nothing goes live until they do. Do not
   call `publish_app` before the user says they have approved.
3. Once the user says they have approved, call `publish_app` once, with the `intent_id` that `prepare_publish`
   returned. It starts the publish and answers where it stands. `APPROVAL_REQUIRED` means the user has not approved
   yet and nothing started: give them the link again, and call `publish_app` again only after they say they have
   approved.
4. Follow the publish with `get_publish`, passing the app's `public_id` and the same `intent_id`. It reports where
   the publish stands and never starts anything. `publishing` means it is still going live: call `get_publish` again
   shortly. `approved` means it has not started: call `publish_app` once more. `published` comes with the live
   address: share it. If the publish expired or failed, call `prepare_publish` for a new approval; if the user
   cancelled it, ask before preparing another.

## 9. Manage an app

- `list_releases` lists an app's releases, newest first, and shows which one is live.
- `update_app` renames an app. While the app has never been published and its address is still the one Exepad
  derived, its address follows the new name.
- `unpublish_app` takes a live app offline and `archive_app` archives an app permanently. Call them only when the
  user asks, and say what will happen first. Each returns a confirmation link: the user confirms in Exepad, where
  they see exactly what will change. An app must be unpublished before it can be archived
  (`ARCHIVE_BLOCKED_BY_RELEASE`); `NOT_PUBLISHED` means there is nothing to unpublish.
- `prepare_profile_change` requests turning a one-page site into an app with data. Call it only when the user asks,
  and say first that a conversion cannot be undone. It returns a confirmation link, and each call is a new request:
  the user confirms in Exepad by typing the app's address, where the page says what changes for publishing, hosting
  and any live site. Once `get_app` reports `capability_profile` `fullstack`, what the app needs is declared and
  written in later revisions. `ALREADY_FULLSTACK` means it already has data; `APP_NOT_MANAGED` means it was built in
  Exepad's own workspace, so the user converts it there.
- `prepare_setting` requests a value for a setting or secret the app declares. It takes no value and returns none: it
  returns a link, each call is a new request, and the user enters the value in Exepad, where the page says the app's
  code can read it. The value replaces any the setting held, and on `production` it changes what the live app does for
  everyone. A secret is requested for `production` only (`SECRET_PRODUCTION_ONLY`). `SETTING_NOT_DECLARED` means the
  target's latest release does not declare that `key`, and `SETTING_RESERVED` that Exepad refuses that name.

- `prepare_asset_upload` requests one file for a binary destination under `public/`. It returns a 30-minute, single-use
  link for the user to choose and upload the file in Exepad; no file or filename passes through this tool. The file can
  be at most 1 MiB and must match the destination type. It replaces any file at that path on the current source.
  The user returns to the chat once it is ready, and `list_files` reports it. Tell the user this file becomes public
  after publishing, even when the app requires sign-in. Build and publication approval remain separate steps.

## Other refusals

- `INSUFFICIENT_SCOPE`: this connection is not allowed to do that. Tell the user and let the host request the extra
  permission. A package may request all ten permissions when connecting. Existing eight-scope grants need a new
  ten-scope consent before using the additional permissions. A URL-only connection may not read a package's scope
  declaration; do not claim reconnecting has added permissions unless the requested tool succeeds.
  On Exepad's consent page they choose the existing connection to replace and Keep this connection’s
  projects to preserve its access. If several connections qualify, they must choose one; their projects are never
  combined. All my apps is a separate, broader choice. A separate new connection starts with no existing projects
  unless they explicitly choose All my apps. Exepad revokes the chosen connection’s old credentials only when it issues
  replacement credentials, even if the assistant does not receive the response. Declined or abandoned consent and
  failed issuance do not revoke those credentials on Exepad. The assistant may still discard its local sign-in and
  require sign-in again.
- `PLAN_LIMIT_TOTAL_APPS`: relay the refusal's message (the account has as many apps as its current plan allows)
  and its `info_url`, and nothing more.
- `BUILD_CREDIT_EXHAUSTED`, `INSUFFICIENT_BALANCE`: the build could not start. Relay the refusal's message, which
  says when the credit resets (`resets_at`), and its `info_url` as information, and nothing more.
- `INVALID_ARGUMENTS`: the arguments did not match the tool's input schema. Fix the field the refusal names.
- `RATE_LIMITED`: this connection, or all of the account's connections together, made more calls than Exepad's own
  limits allow, or Exepad could not count the call just now; nothing was done. The same call can succeed after
  `retry_after_seconds`: wait that long, then send the same call again.
