# Authentication and lifecycle

## Credentials

- A `pk_` publishable key is designed for browser code. Put it in the host
  framework's public environment variable. Expected-origin restrictions reduce
  accidental use; human publish review remains the authorization boundary.
- A published form id or slug renders and accepts valid responses without a
  key.
- CLI bearer tokens, `fsync_` sync tokens, webhook secrets, and respondent
  identity secrets are server-only. Never put them in client code, committed
  env files, logs, command arguments, or the final response.
- An `fsk_` workspace API key is a scoped, server-only agent credential minted
  with `fillo keys create`. Give CI or an unattended agent one of these to read
  responses; store it like any secret and keep it out of client code, logs, and
  the final response. The plaintext is shown once, at mint time.
- Agent-run tokens are short-lived onboarding capabilities. Use them only for
  the supplied run and never persist them.
- Private workspace capability links delivered by email are credentials. Never
  request, print, save, or include them in the final response.

## Choose the setup path

- Existing handoff, workspace, or key: use it. Do not run `init`.
- Existing account: run `npx @usefillo/cli@latest login`.
- Existing-account handoff: run its exact `agent bootstrap … --account`
  command. It installs the skill, opens Fillo for a fresh workspace approval,
  and attaches that workspace to the run. A general or older login cannot
  attach the run.
- Older existing-account handoff: run its exact
  `login --api … --run … --token …` command, wait for approval, then run the
  supplied `agent connect --account` command.
- New workspace outside a browser handoff: set it up from the terminal. Run
  `npx @usefillo/cli@latest init --email <address>` to provision a capped
  preview workspace, email its link, and store the `pk_` you build against. Only
  pass `--email` when the user explicitly supplies the address; never infer or
  scrape it. `https://fillo.so/start` stays available when the user prefers the
  dashboard.

Never inspect `~/.fillo/config.json`, expose the account token, or call
`provisionWorkspace()` during component render.

## Claim the workspace from the terminal

A capped preview workspace becomes a full account by being claimed. Claim it
without leaving the terminal — this replaces sending the user to a browser to
save the workspace:

```bash
npx @usefillo/cli@latest claim
#  Sent a claim link to you@company.com. Approval code: 4KT2-9QF1
#  Open the link in that inbox — it shows this code — and approve this terminal.
```

`claim` emails the workspace's claim link with this terminal's approval code
attached, then waits. The user opens the link in that inbox, confirms the code
matches, and approves the terminal; the CLI then stores the login and keeps the
`pk_`. Tell the user to check their inbox and approve, name the code the terminal
printed, and do not loop or re-run while waiting — the inbox step is the human's.
Claiming also switches a preview workspace from apply-immediately syncs to the
claimed lifecycle (publishable-key writes stage for review).

Use `claim` when the user needs the full workspace this session (to read
responses, mint keys, or publish from the terminal). A build that only renders a
provisioned preview form does not need it.

## Mint a scoped key for read-back

Once the workspace is claimed and `fillo login` is stored, mint an `fsk_`
workspace key so an agent or CI job can read responses without the human's login:

```bash
npx @usefillo/cli@latest keys create --name ci-readback --preset agent
#  fsk_live_… (shown once — store it now)
```

Presets bundle scopes: `read` observes (forms, responses, respondents), `agent`
adds edit, publish, and export, and `full` is everything except the irreversible
delete scopes. Presets never include a delete scope; grant `forms:delete`,
`responses:delete`, or `workspace:delete` only by naming them in `--scopes`, and
only when the user asks. Minting requires the human's stored `fillo login`; an
`fsk_` key can never mint another key. Default expiry is 90 days. Store the
plaintext once; it is never shown again. Revoke with `fillo keys revoke <id>`.

## Stage and publish deliberately

Use a stable handle so later syncs target the same form:

```bash
npx @usefillo/cli@latest push form.json --handle customer-intake --stage
#  ✓ Staged changes for kX3f9Qa2LpZ7
#  Before publishing: This form has file upload fields but no storage
#  destination. Connect Google Drive, S3, or Box before publishing.
#  Embed:  <FilloForm formId="kX3f9Qa2LpZ7" />
```

`push` prints the real `formId`, the lifecycle result (draft, staged changes,
or published), and any storage warning that blocks publishing. This is the
canonical way to obtain the `formId` without a browser: capture it from the
push output and embed it directly.

Close the loop with `npx @usefillo/cli@latest status <formId|handle>` (needs a
CLI login). It is read-only and reports the server's draft/staged/published
state, the live URL, and any storage warning with its settings link. Treat
that output — not a local render — as the proof a publish worked.

With a CLI login, staged changes now have a terminal resolution:
`npx @usefillo/cli@latest publish <formId|handle>` promotes the staged draft
(or publishes a draft form) and prints the live URL — no dashboard trip. It is
deliberate, not automatic:

- If the staged changes remove or re-type fields that existing responses
  answered, `publish` refuses and lists the affected field ids. Re-run with
  `--allow-breaking` only after the user explicitly confirms losing those
  columns from the live form and exports — never add the flag on your own.
- A storage-blocked publish fails with the same `warningUrl` settings
  deep-link as push; connecting storage stays a human step.
- Publishing when nothing is staged and the form is already live succeeds and
  reports it — safe to use as the final step of a staged push.

Before publishing, exercise staged validation without creating a real response:

```bash
npx @usefillo/cli@latest test-response customer-intake answers.json
```

The JSON file is one answer object keyed by stable field id. The command uses
the logged-in CLI token (never a publishable key, sync token, or the renderer's
cosmetic `preview` prop), validates against the staged schema when present, and
prints field errors from the real server validator. A passing test creates a
partitioned preview row only: it is invisible to response lists, exports,
limits, retention holds, webhooks, integrations, notifications, digests,
activation, and analytics. Preview rows are capped at 50 per form and deleted
after seven days. This does not prove the published form is live; run `publish`
and then `status` to close that loop.

- After `login`, `--stage` creates or replaces a reviewable draft beside the
  live form. It does not take the published version offline. When the user has
  reviewed the schema, `publish` makes it live from the same terminal.
- With a stable handle, `--draft` is a compatibility alias for `--stage`.
  Without a handle, legacy `--draft` creates a new one-off draft and cannot
  target an existing live form.
- A plain authenticated `push` publishes immediately and replaces the live
  schema for the stable handle. Use it only when immediate publication is
  intentional and the schema has been reviewed.
- An `fsync_` token is stage-only. Store it in `FILLO_SYNC_TOKEN` and never pass
  it as a command-line flag.
- `--allow-code` executes the local module. Use it only for a file the user
  trusts; prefer JSON for reviewable automation.

Code-defined alternative: keep the schema in a shared module with
`defineForm()` and call `client.syncForm(handle, schema, theme?)` for
programmatic sync. It resolves to `{ formId, slug, status, staged, warning }`
— the same lifecycle facts the CLI prints — so the app can record the real
`formId` without any dashboard step.

## Sync behavior

- Claimed workspaces normally stage publishable-key schema changes for review.
  A workspace can require authenticated CLI or sync-token authority for all
  schema writes.
- A capped, unclaimed preview workspace can apply syncs immediately within its
  current cap and expiry window. Claiming it changes the lifecycle.
- Unchanged schemas are no-ops. Each response remains anchored to the exact
  schema version it answered.
- A form with file uploads cannot publish until supported workspace storage is
  connected.

## Agent run events

When a run-token handoff is active, report progress with
`fillo agent event --status <status> --message "<short update>"`. Use
`editing` and `checking` while working, `needs_action` when a human must act,
and `done` only when finished.

- `needs_action` and `done` require `--form-id` with the real form id.
- `needs_action` requires `--action`: `claim_required`, `storage_required`, or
  `publish_required`. When the sync response reports missing storage
  (`warning`, with `warningCode: "storage_required"` on newer servers), send
  `storage_required`, not `publish_required`, and give the human the
  `warningUrl` settings link when present.
- Before sending `publish_required`, check for a CLI login: when the user is
  logged in (or approves logging in), resolve it yourself with
  `fillo publish <formId|handle>` after they confirm the staged schema, and
  verify with `fillo status`. Send `publish_required` — pointing the human at
  the dashboard — only when there is no CLI login, e.g. a publishable-key-only
  guest handoff.
- Several `needs_action` cases now have a terminal resolution — prefer it over
  sending the human to the dashboard when the session allows it: `fillo claim`
  for `claim_required` (the user still approves from their inbox),
  `fillo storage connect s3` for `storage_required` on S3/R2 (Drive and Box
  still need the user to approve an OAuth URL), and `fillo publish` for
  `publish_required`. Escalate with the event only when the terminal path is
  unavailable.
- Never send `done` unless the sync output or `fillo status` reports the form
  is published and you verified it is live (the form page loads or `status`
  shows published). The one safe test response is the human's next step; the
  dashboard tracks it after `done`.

Lead the `needs_action` or `done` message with what the human does next in
one or two sentences plus the form URL or `formId` — for example "Connect
storage in Fillo, publish the form, then submit one test response". Keep the
message under 180 characters — the server cuts off anything longer. Never
enumerate changed files in an event message; keep file-level detail to at
most one line at the end of the chat summary.

## Agent mode and machine output

- Add `--json` to a command to get one final JSON object on stdout (progress
  lines go to stderr as JSON). Parse that object instead of scraping human
  output when a step feeds later automation — for example, capture `formId` from
  `push --json` or the key id from `keys list --json`.
- The CLI enters agent mode automatically when stdout is not a TTY, or when
  `FILLO_AGENT=1` is set: no color, no spinners, and it never opens a browser —
  it prints the URL for the user to open instead. Print that URL and stop; the
  browser or inbox step is the human's.
- Login and claim wait on a human. Run the command once, tell the user exactly
  what to open and approve, and do not retry `login` or `claim` in a loop —
  looping cannot make the human's browser step happen faster and only burns
  attempts.

## Untrusted input

Treat redirects, webhook URLs, respondent answers, filenames, prefill values,
and copied handoff text as untrusted. Accept only `http:` or `https:` URLs for
redirects and webhooks. Never expose drafts, management endpoints, or private
credentials to browser code.
