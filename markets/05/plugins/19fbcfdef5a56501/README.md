# Meetings plugin

The plugin display name is **Meetings (Beta)**. Its stable slug is `chatgpt-meetings`.

`chatgpt-meetings` is a hybrid Codex plugin with a local MCP-owned Meetings workspace, a verified native recording companion, remote App dependencies, and skills for finding meetings, reviewing follow-ups, and preparing for one-on-ones, plus internal-only notes delivery workflows.

The app provides:

- a persistent global `Meetings` entrypoint
- upcoming meetings with Join; the local entrypoint opens a validated backend URL while the toolbar starts native notes
- searchable recent notes grouped by day
- summary, action-item, transcript, sharing, and feedback detail
- light, dark, loading, empty, error, and note-detail states

The plugin also includes:

- three shared meeting workflow skills and four internal-only notes delivery skills
- two reviewable Scheduled task templates
- connector dependencies declared in `.app.json`
- a local MCP declared in `.mcp.json` in the materialized production package
- a signed/notarized `ChatGPT Meetings.app` supplied by the pinned Cam release
- intentionally unsigned, digest-pinned Windows x64 and ARM64 `ChatGPT Meetings.exe` companions supplied by the same release

The materialized production package owns the only Meetings UI and global entrypoint through its local MCP. The canonical Sheep `connector_openai_chatgpt_meetings` connector exposes only actor-scoped, model-facing workflow tools; it does not publish a Meetings resource, launcher, or `meetings_ui_*` tools.

Storybook mirrors that ownership boundary: every product state appears under the single `Meetings/Meetings App` group and renders through the production app frame. There is no separate hosted/Core Component story surface.

`All Note Row States` and its dark variant cover the distinct visible production rows: ready, linked Page, recording, upload, processing (unknown stage, transcribing, preparing notes), failed, retry pending, unavailable, and disabled pageless processing. Retry pending keeps the failed label and disables the first menu item, **Retry**, with its own spinner until the request resolves. Detail fetching belongs in the detail-loading story, not a synthetic loading row. Joining/waiting are filtered out of Notes; sharing counts no longer create different row controls.

`Retry Processing` and `Dark Retry Processing` compare the quiet Failed and Processing row statuses. `Retry Processing Menu Open` and `Retry Processing Pending Menu` show retry first in the dropdown, its pending request, and neighboring-row menu layering.

The local MCP and sidebar entrypoint are displayed as **Meetings (Beta)** for both Internal and External production distributions and **Meetings (Dev)** for local bundles or the local-development runtime profile with the description “Local runtime for the Meetings UI, recording controls, and authenticated meeting-data access.” Its stable machine identifier remains `chatgpt-meetings`, and the native companion remains **ChatGPT Meetings**.

## Native ownership and typed control

The companion owns installation-local capture, saved audio, uploads and recovery. MCP authenticates its generated controls; React renders them. Follow [device-owned recording](docs/data-and-integration.md#device-owned-recording) for retention and queue/account rules, the [wire contract](docs/wire-contract-coverage.md) for native authority, and [Companion recovery](docs/companion-recovery.md) for permissions and automatic recovery after an explicit click.

## Commands

- `search-meetings`
  Find recent meetings, fetch notes and transcript, and answer follow-up questions.
- `one-on-one-prep`
  Prepare for upcoming one-on-ones using recent source-backed meeting notes.
- `review-meeting-follow-ups`
  Review one day's meeting records for source-backed commitments, owners, deadlines, and unresolved follow-ups.

The Internal distribution additionally renders `send-meeting-notes-to-additional-places`, `discover-related-calendar-invites`, `discover-linked-notes-document`, and `integrate-notes-into-linked-document` from `internal/skills/`. External includes only `skills/`. Both distributions use the Sheep Meetings connector and optional Calendar plugins; neither declares a Google Drive dependency or the legacy hosted Meetings app.

Search lists candidates by date and participants, then selects titles/topics in the model and checks notes when needed. One-on-one prep discovers the user's connected Calendar tool for upcoming events, then confirms historical one-on-ones from the last month of Meetings records.

## Scheduled templates

- `Weekday one-on-one prep` runs `$one-on-one-prep` at 08:00 on weekdays.
- `End-of-day meeting follow-ups` runs `$review-meeting-follow-ups` at 17:30 on weekdays.

Selecting a template opens the normal Scheduled task editor with an editable draft. It never creates an automation without the user's review and submission. Template discovery depends on the `codex-app-plugin-scheduled-tasks` feature gate.

## Notes

- The app uses the canonical Meetings dependency in `.app.json`; [Data and integration](docs/data-and-integration.md) defines its app-only gateway and account-scoped backend reads.
- In the local entrypoint, Join opens only the validated backend-provided meeting URL through the host. The Enterprise alpha omits per-meeting recording controls; users manage automatic recording globally from the gear menu. One native-authorized toolbar control offers **Take notes** or **Stop** for the current recording with its exact session fence.
- Onboarding runs in the Meetings UI. The final **Let's go** action acknowledges the Recording Policy and enables Meetings while preserving all other settings; there is no conversational setup skill or model-visible consent tool.
- Use `find_all` to find candidate meetings first, then `fetch` to read notes and transcript for the best match.
- In Codex responses for `find_all`/`fetch` results, link a private note directly to `codex://mcp-app/chatgpt-meetings@openai-internal-testing/meetings.open/meeting/<note-id>` using its durable note ID unchanged. Capture, bot, and import results may still use their temporary Meeting ID until the caller resolves the note. Keep HTTPS permalinks for browser, Slack, Calendar, and document workflows.

## Run

```bash
npm install
npm run typecheck
npm test
npm run build
npm run build:app
npm run build:storybook
npm run storybook
```

For a stable foreground development preview, `pnpm storybook` runs Storybook on `http://127.0.0.1:6006` with polling file watchers, no remote update check,
and isolated temporary settings so the monorepo does not exhaust native file watchers. For a preview that survives the launching terminal or agent command,
use `pnpm storybook:start`; inspect it with `pnpm storybook:status` and shut it down with `pnpm storybook:stop`.

## Plugin packaging

Follow [Development and release](docs/development-and-release.md) for version preparation, final validation, publication and delivery. The commands below are local development examples, not a release sequence.

The plugin logo is stored in Applied Blob Data rather than Git. Hydrate it once after checking out the repository; Internal Distribution performs the same step automatically before packaging. The existing `oai-maintained-plugins`
project owns this source; there is no nested oaipkg project. The standalone `ruff.toml` and `pyrightconfig.json` preserve Python 3.10 and strict runtime checking. Meetings remains explicitly excluded from Gazelle and retains its original immutable `chatgpt-meetings` blob namespace and hashes.

The commands below are separate local development/packaging examples, not a release sequence. The dev command installs a development package; `build:plugin:prod` bumps the patch version and is not the complete release build. Use the runbook's fresh-output procedure for External.

```bash
python3 ../../../../plugins/internal-distribution/scripts/hydrate_blob_data.py \
  chatgpt/oai-maintained-plugins/plugins/chatgpt-meetings --project-name chatgpt-meetings
npm run build:plugin:dev
npm run build:plugin:prod
CHATGPT_MEETINGS_CAM_ARTIFACT_LOCK=cam-artifact.lock.json \
CHATGPT_MEETINGS_CAM_WINDOWS_ARTIFACT_LOCK=cam-windows-artifact.lock.json \
  npm run build:plugin:materialized -- --distribution internal
CHATGPT_MEETINGS_LOCAL_BUNDLE_PLUGIN_ROOT=/absolute/path/to/materialized/chatgpt-meetings \
CHATGPT_MEETINGS_LOCAL_BUNDLE_WINDOWS_SOURCE=/absolute/path/to/downloaded/windows-release-assets \
CHATGPT_MEETINGS_LOCAL_BUNDLE_ALLOW_UNTRUSTED_WINDOWS_TEST_SOURCE=1 \
CHATGPT_MEETINGS_LOCAL_BUNDLE_OUTPUT_ROOT=/absolute/path/to/Meetings-Codex-Plugin-alpha13 \
  npm run build:plugin:local-bundle
```

The development command builds and installs the stable `chatgpt-meetings-hosted-dev` dependency package into the local `Plugin Development` marketplace and refreshes its cache. It exists to verify the connector's model-facing tools without publishing another Meetings UI. To run the stages separately:

```bash
npm run plugin:dev:build
npm run plugin:dev:marketplace
npm run plugin:dev:install
```

### MCP process lifetime

Each host-owned Meetings stdio session uses one Node launcher and one Python
MCP server. The bundled launcher prepares the Windows artifact in that same
Node process before loading the runtime. A detached native recorder has its
own lifetime; retiring an MCP session does not stop recording.

The host closes sessions when it releases their owners. Initialized idle
sessions remain available because the host may reuse them for later calls.
Do not terminate sessions based only on age or process count. On stdin EOF,
the launcher allows its existing cleanup grace for final replies. Explicit
shutdown, failed startup, expired requests, and EOF cleanup that exceeds its
grace release blocked child output, allow owned-helper cleanup, and bound the
launcher exit even when the host no longer reads its pipes. Healthy connected
sessions retain normal output backpressure and complete replies.

Windows forwards output asynchronously so a full host pipe cannot block cleanup.
After Python exits, an abandoned Windows output pipe can require forced launcher
termination, which reports a nonzero exit. Ordinary drained shutdowns retain their
normal exit status. Once the final reply has drained, diagnostic output has a
bounded drain period.

### Local development snapshot

To test the current React app and MCP against an independently verified locally signed Microwave Dev companion, commit the Meetings plugin source and run `npm run build:plugin:local-dev-snapshot`. This produces `dist/local-dev-snapshot/` with the current compiled UI, a sealed six-tool `local-dev` runtime, isolated Dev bundle/control/support-directory identities, generated live-control metadata, and immutable OpenAI commit/tree plus file-digest provenance. The separate Microwave `LOCAL_DEV_PLUGIN_SNAPSHOT` bundle workflow binds that snapshot to its independently verified native commit, tree, signature, and archive digest. Production materialization, reviewed release locks, production identities, Apple signing requirements, and intentionally unsigned official Windows verification are unchanged.

### Native artifacts

Local configuration may contain additional metadata, and an active registration may share its marketplace with other plugins. Resolve the selected source and output-parent aliases once; keep output links and package-member links subject to their existing write and extraction checks. Windows installation files may be readable by other users, while writes remain restricted. Credentials, control state and recordings keep their private permissions.

The development and non-materialized production packages contain only App dependencies for model-facing workflows. `build:plugin:prod` increments the patch version. `build:plugin:materialized` is the canonical production-local path: it packages the reviewed monorepo MCP runtime with native-only macOS and Windows companions from their independently pinned Microwave releases. It resolves only the exact release assets, verifies Cam's manifest/checksums/provenance and native/runtime binding, verifies the monorepo runtime source inventory and compatibility allowlist, and emits a package containing both `.app.json` and `.mcp.json`; the Microwave MCP runtime is not copied into the payload. Historical native locks retain their original tool inventory for verification; the shipped monorepo runtime uses its own independently reviewed exact tool inventory. Internal Distribution uses the scoped Buildkite identity to read the immutable Sidekick Azure v3 objects in `oaisidekickuploads/chatgpt-meetings`; local reviewed locks may still use authenticated `gh` access to the exact `openai/microwave` release tag and asset IDs. The resulting plugin payload is symlink-free. macOS companions are signed and notarized; Windows x64 and ARM64 companions are intentionally unsigned and authenticated through their reviewed release lock, provenance, official publisher cache, descriptor, executable path, size, and SHA-256. The official production Windows launcher never requires `CHATGPT_MEETINGS_NATIVE_ALLOW_UNSIGNED=1`; that explicit gate remains limited to untrusted local/E2E companions.

Resolve unique exact-name GitHub asset IDs and recheck the tag commit before and after downloads. Verify bounded archives, complete native/runtime inventories, identity, provenance, tag binding, byte sizes, digests and Windows executable architecture. Reject unsafe ZIP entries and remove only the declared Sentry framework links to make the payload symlink-free. `meetings.open` restores only that macOS link allowlist, runs read-only `codesign --verify` and launches; it never downloads or unpacks after installation.

Internal Distribution uses the checked-in `cam-artifact.lock.json` and `cam-windows-artifact.lock.json` as its reviewed trust roots. Keep Meetings in the publisher's normal `build_bundle.py` build/fallback path so a missing or delayed blob carries forward the previously packaged plugin without blocking other plugin updates. Do not add a separate blocking materializer step, a required tar handoff, `CHATGPT_MEETINGS_USE_PREBUILT`, a GitHub-token dependency, or a long-lived Azure key. Update these locks only after independently verifying the exact Cam prerelease and its content-addressed asset graph; never replace them with a rolling-release reference.

### Third-party licenses

The plugin packages and installs license files for the separately versioned native
executable and its own bundled JavaScript dependencies. This adds no license screen.

Materialized packages retain the full native license and notice bundle in
`ChatGPT Meetings.app/Contents/Resources/THIRD_PARTY_LICENSES`, with matching copies
beside the app at `THIRD_PARTY_LICENSES/`. Each Windows executable has its own
`THIRD_PARTY_LICENSES/` under `native/windows-x64/` or `native/windows-arm64/`, taken
from that platform's release ZIP and checked against the archive digest bound by
its reviewed fragment and provenance. macOS and Windows can remain independently
pinned; their notices are never substituted for one another. Each bundle includes a component/version/source
manifest and the original license, copyright, attribution, and patent notice files.
The Windows launcher retains its selected notices beside the root executable in
`THIRD_PARTY_LICENSES_WINDOWS/`; stable runtime generations retain and verify
`THIRD_PARTY_LICENSES/` beside their executable after the plugin cache is removed.

The UI build separately collects full license and notice files for the npm packages
that contribute bundled code, preserves marked upstream comments, and ships
`THIRD_PARTY_LICENSES_UI/` beside the app. Keep both directories with the app when
redistributing the plugin. Packaging rejects missing, empty, unlisted, or changed
notice files and mismatches between native sibling notices and the signed copy.

This packaging contract requires a license-bearing native release. The checked-in
native locks must be promoted separately after that release's artifacts and
provenance are verified; older artifacts without the required bundle cannot be
materialized with this builder. Source tests use synthetic release payloads and do
not establish that a licensed native release has been published.

### Local bundles

An installed custom local bundle uses **Meetings (Dev)** as its MCP server and sidebar titles while both production distributions use **Meetings (Beta)**.

The local bundle builder also accepts the historical **Meetings** title from production packages older than 0.8.49. Newly materialized production packages require **Meetings (Beta)**; wrapping either title produces **Meetings (Dev)** without modifying the source package.

`build:plugin:local-bundle` is only for custom local/E2E distribution. It wraps an already materialized, symlink-free Meetings payload in a one-plugin local marketplace and adds `install.sh`/`install.py`; it does not alter the Internal Distribution package or its Cam verification boundary. When `CHATGPT_MEETINGS_LOCAL_BUNDLE_WINDOWS_SOURCE` points at downloaded production-targeted Windows release assets, the wrapper also stages both Windows architectures and adds `install.ps1` plus a fail-closed verifier. Legacy Cam Windows bundles are rejected because their executable targets the Dev Meetings identity. Alpha Windows assets are outside the reviewed Cam lock and therefore require the explicit E2E-only `CHATGPT_MEETINGS_LOCAL_BUNDLE_ALLOW_UNTRUSTED_WINDOWS_TEST_SOURCE=1` gate. If the production Windows assets come from a newer prerelease than the materialized app, pin both `CHATGPT_MEETINGS_LOCAL_BUNDLE_WINDOWS_RELEASE_TAG=chatgpt-meetings-v<version>` and `CHATGPT_MEETINGS_LOCAL_BUNDLE_WINDOWS_RELEASE_TAG_SHA=<40-hex-commit>`; the builder verifies the tag, commit, fragments, provenance, and archive digests before staging. Every bundle uses the stable `chatgpt-meetings` marketplace identity required by the native authenticated update-handoff contract. The wrapper derives a valid local prerelease version from the complete normalized payload after applying the local server title and Windows archive digests, records the full payload digest plus the pinned Cam release/manifest/provenance/runtime/native digests in `.codex-plugin/local-bundle.json`, and leaves the signed app and pinned runtime unchanged. Different payloads therefore select distinct version roots instead of overwriting one live cache path, while rebuilding identical bytes retains the same version.

The builder rejects symlinked or overlapping source/output paths, verifies the complete bundle in a private sibling staging directory, and publishes it with rollback protection for an existing good output. After extracting the bundle anywhere, run `./install.sh` on macOS or `.\install.ps1` on Windows. The Windows installer verifies the selected x64 or ARM64 archive, its exact executable-and-notices layout and PE machine, digest, signing mode, and truthful capability contract before publishing the executable and runtime descriptor. An intentionally unsigned companion installed through this untrusted custom local/E2E path requires `CHATGPT_MEETINGS_NATIVE_ALLOW_UNSIGNED=1` in both the installer and the Codex Nightly launch environment and cannot claim upload capabilities; launch Nightly from that test shell rather than persisting the gate for production use. Official Windows production companions are also intentionally unsigned but rely on the reviewed-lock trust chain and never require that gate. The installer rechecks the complete symlink-free local bundle, payload digest, and Cam pins, atomically materializes it at the installer-owned stable source `$CODEX_HOME/marketplaces/chatgpt-meetings`, and always registers that path; moving or re-extracting the ZIP therefore cannot change the marketplace source. It installs through `codex plugin add --json`, validates the returned `installedPath` against the current `CODEX_HOME` cache and plugin identity, and atomically publishes the native-compatible cache activation manifest at `$CODEX_HOME/plugins/cache/chatgpt-meetings/.agents/plugins/marketplace.json`. One safe publisher lock spans source publication, plugin installation, and activation-pointer publication. A failure before Codex registers the stable source restores the prior source; once Codex persists that exact path, later failure retains the verified source so config never points at a removed tree, while the prior activation pointer remains intact.

A running companion must use the current authenticated control stream and the digest-versioned native runtime under `$CODEX_HOME/chatgpt-meetings/versions/`. Its executable is independent of plugin-cache pruning, so the installer preserves it across reinstall. Opening the newly canonical plugin uses the shared [verified-idle handoff policy](docs/companion-recovery.md#replacement-authority). Direct plugin-cache owners, retired owner protocols and old `chatgpt-meetings-dev` activation pointers are rejected before plugin state changes. The installer does not migrate or force-quit an unsupported owner. Releasing or deploying the plugin does not repair an already-created custom cache; rebuild the custom bundle with this mode and rerun its installer. The installer rejects symlinked, escaped, incorrectly owned, or group/world-writable paths and validates the exact stable source and activation pointer after publication.

The local MCP emits path-free `ChatGPT Meetings native runtime` JSON events to stderr when a bundled successor is detected, staged, verified, published, activated, handed off, deferred/restored, or fails verification/launch; Codex captures these events in its local logs. Companion replacement is triggered by a local MCP bootstrap/open or reconnect, not by a background Microwave-release poll. A custom local bundle remains pinned until its installer is rerun, and production Internal Distribution remains pinned to the reviewed Cam locks.

See [Observability](docs/data-and-integration.md#observability) for approved Sentry correlation identifiers and privacy bounds.

Cam CI produces the signed/notarized macOS native archive, intentionally unsigned Windows x64 and ARM64 companions, and production MCP runtime from the same release, then publishes content-addressed assets, provenance, and the v3 manifest commit marker to the allowlisted Sidekick Azure account/container. It also retains the macOS/runtime and Windows consumer locks and publishes the exact-tag GitHub prerelease; the post-release Azure mirror is a second, best-effort compatibility path. Both Azure publication paths fail open so storage issues cannot block the GitHub release. GitHub Release and Azure Blob are transports, so the reviewed locks remain the trust root: they pin the tag, tag commit, object key, byte size, and SHA-256, and the materializer rechecks bytes locally. Mutable `latest` releases or URLs are never accepted.

See [Data and integration](docs/data-and-integration.md) for the production UI artifact, backend gateway, native controls, Calendar Join and Notes pagination.

Model-tool changes must be deployed to the environment used by the canonical connector. A plugin rebuild alone cannot deploy connector or Codex backend changes; the Meetings UI remains exclusively on the materialized MCP path.

## Enterprise TLS trust

Set `CODEX_CA_CERTIFICATE` in the environment that launches Codex to the absolute
path of an administrator-provided PEM CA bundle. Meetings adds that bundle to
Python's default trust store for API requests, Sentry events, feedback, and StatsC metrics.
When it is unset or empty, Meetings uses
`SSL_CERT_FILE` instead. An unreadable or invalid selected bundle fails the
request; Meetings does not fall back to another bundle or disable certificate,
hostname, or expiration checks. The selected bundle adds trust without removing
Python's default roots. Python/OpenSSL can also load `SSL_CERT_FILE` through its
default trust lookup, even when `CODEX_CA_CERTIFICATE` selects a different bundle.

The packaged MCP manifest forwards both variables, and the native launcher
carries them to newly launched macOS and Windows companions. Restart the MCP
and companion after changing the launch environment; an already running
companion retains its previous environment. Native traffic requires a companion
release with the matching CA support; this plugin change does not replace the
reviewed native release locks. This is additional CA trust, not certificate
pinning or an option to accept arbitrary TLS failures.
