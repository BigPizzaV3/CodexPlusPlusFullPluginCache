# Status and diagnostic values

`get_account_status` gives a compact account view. `get_onboarding_diagnostics`, where available, adds:

- the latest relevant Strava export import;
- Garmin connection detail;
- running-history availability;
- a `readiness` summary (`analysis_ready`, `reason`, `next_action`).

Explain these facts in plain words. Do not read the codes out.

## Readiness

| `reason` | Meaning | What to say or do |
|---|---|---|
| `running_data_available` | Runs are stored and visible | Go straight to the runner's question |
| `running_data_available_import_in_progress` | Runs exist; an upload is still being processed | Analyse what exists. Newer runs from the upload may not be included yet |
| `running_data_available_latest_import_failed` | Runs exist; the newest upload failed | Analyse what exists. Mention the failed upload only if relevant to the question (for example a missing period) |
| `import_in_progress` | No runs yet; an upload is queued or processing | It is still being processed. Offer to check again later. Do not promise a time |
| `import_<reason>` | No runs yet; the latest upload failed (see Import reasons) | Explain the reason and the next step |
| `garmin_reauth_required` | Garmin needs reconnecting (permission missing or revoked) | Reconnect Garmin on the Performance Signal website, then recheck |
| `garmin_sync_pending` | Garmin is connected; no Garmin activity has been received yet | Nothing has arrived yet. Suggest checking that the activity is in Garmin Connect and has finished syncing there. No delivery time or history backfill is known |
| `garmin_syncing` | Garmin activities have been received and are waiting to be processed | They have arrived and are being processed; the connection is fine. Offer to check again when they ask. The account status message may still say "waiting for delivery"; the diagnostics are more specific |
| `garmin_processing_error` | A received Garmin item could not be processed | Say plainly that Garmin delivered something that then failed to process (it did arrive). Suggest checking again later, or contacting support if it persists. Do not guess the cause and do not suggest reconnecting |
| `garmin_data_not_visible` | Garmin is connected and has delivered activities, but Garmin data is not available to this chat | Say their Garmin activities have arrived in Performance Signal but are not available in this chat at the moment. Nothing is wrong with their connection, and they do not need to connect anything else. Do not suggest connecting Strava or uploading a Strava export as a workaround. Do not promise when this will change |
| `no_running_activities` | Activities are stored, but none is a run | Their data has no runs (for example only rides). Running analysis needs a run |
| `strava_connected_no_stored_runs` | Strava is connected but no runs are stored | Recent Strava runs usually arrive automatically. A specific missing run can be retrieved on request (tool selection) |
| `no_data_source` | No connection and no imported history | Explain the options: upload a Strava export on the website, or connect Strava or Garmin there |
| `evidence_unavailable` | Some status could not be read | Say you could not confirm it right now and offer to recheck. Never conclude "no data" |
| `access_inactive`, `access_setup_incomplete`, `access_unknown` | Access does not currently allow analysis, or could not be confirmed | Relay the tool's message and dashboard link neutrally |
| `account_unknown` | The account status itself could not be read | Say you could not check the account right now and offer to try again. Do not conclude anything about access or data |
| `account_pending_deletion` | The account is being deleted | Relay the message; nothing else |

## Import reasons (`strava_export.latest.reason`)

| Reason | What to say |
|---|---|
| `invalid_archive` | The file was not a usable Strava export (damaged, not a ZIP, or an unexpected structure). Upload the original, unmodified export ZIP downloaded from Strava |
| `archive_too_large` | It exceeded the upload limits. Contact support; do not suggest editing or splitting the archive |
| `unreadable_activities_csv` | The activity list inside the export could not be read (for example, missing expected columns). Upload the original export again. **Never** tell the runner to rename or edit CSV columns |
| `language_not_enabled` | The export is in a language (`language.detected`) the importer recognises but that is not enabled yet. Say support for that language is not available yet. Do not promise a date. They could check back later |
| `no_runs_recognised` | The export was read but contained no recognisable runs. Check it is the right account's export |
| `interrupted` | Processing stopped part-way (see `interruption`). Anything saved is kept (counts). Uploading the same export again continues without duplicating saved runs |
| `account_not_eligible` | The account could not accept the import at the time. Check account access |
| `unknown` | The cause is not recorded in a form we can explain. Do not guess; suggest checking again or contacting support |

**Counts.** `activities_added`, `streams_added`, `already_imported`, `skipped` and `failed_writes` are real saved results.

- **Partial import:** when `partial` is true, say what was saved.
- **Superseded failure:** when `failure_superseded` is true, the failure is old and a later import succeeded. Do not present it as current.

**Language.** `language.enabled: null` means the language is not one the importer knows. Do not claim support either way.

## Garmin (`garmin.state`, `garmin.data_visible_in_app`)

| State | Meaning |
|---|---|
| `connected` | Connected; at least one activity has been received |
| `sync_pending` | Connected, no activity received yet |
| `syncing` | Received items waiting to be processed |
| `error` | A received item failed processing |
| `reauth_required` | Reconnect on the website (missing or revoked permission) |
| `connecting` | An authorisation was started and not finished |
| `disconnected` / `not_connected` | Not connected |
| `unavailable` | Garmin is not available for this account (it is a paid or pilot feature) |
| `unknown` | Could not be checked. Do not conclude anything |

**Visibility in this chat.** `data_visible_in_app: false` (or `garmin_data_enabled: false` in account status) means stored Garmin activities are not available to this chat, even when they were received. That is a product setting, not a fault the runner can fix, and not a reason to connect Strava.

**What Garmin cannot do here.** Garmin sends new activities to Performance Signal after they sync to Garmin Connect. There is no request from here for past Garmin history and no remote Garmin sync. Do not invent either.

## Trials and access

- **Trial state:** `trial_state` is `unused`, `active` or `expired`, with `trial_expires_at`. Quote the date as given, converted to the runner's time zone if known.
- **Expired trial without a membership:** analysis tools return an access message with a dashboard link. Status and setup help remain available.
- **Never** start, extend or reset a trial; never invent prices, discounts or upgrades.

## Sign-in

If ChatGPT asks the runner to sign in again, that is the app's own authorisation with Performance Signal. It is separate from Strava or Garmin connections. They should complete the sign-in prompt, then you can check status again. Never ask for credentials or tokens.
