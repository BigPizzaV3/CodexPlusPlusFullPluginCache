# Prepared numeric MCP data practices

Revision date: 11 October 2026. Maintainer: Feida Wang, trading as RSI AI.
This is a source/preparation notice; a production service has not been deployed
by this task. The matching public policy update is a local draft only.

## Accepted inputs, purpose and recipients

The business tool accepts only five optional scalar counts: reference limit,
current usage estimate, planned increase, output reserve and an estimated
future growth rate. Each is null/unknown or an integer within its bounds, with
optional fixed source enums. It accepts no conversation history, prior-turn
arrays, local paths, model/account/chat identifiers, free-form task text or
credentials. Limits are explicit references, not discovered platform policies.

On a later deployment, the selected MCP host sends those values to the chosen
Cloudflare endpoint for arithmetic and returns numeric results. Cloudflare
therefore processes request data and transport/provider metadata such as IP,
time, URL and protocol/client information under its own policies and the
operator's account settings. Requests can contain a protocol correlation ID;
the server must return it to match the response. It preserves only necessary
bounded MCP protocol/client labels and drops arbitrary transport meta fields.
This is not a claim that the provider receives numbers only at the HTTP level.

The Worker uses no publisher database, business-data cache, disk writes, paid
model API, local Codex files or private-account integration. Its only external
request is the client's incoming HTTP call; the handler makes no outbound
network call. Raw request bytes and parsed objects enter process memory.
Unexpected fields, arrays, ambiguous JSON, oversized input and invalid values
are rejected without echoing their names/contents. No application request/body
logging is implemented and observability is disabled in the prepared config.
That does not eliminate Cloudflare infrastructure, account or operator logs.

## Storage, retention and controls

The application retains no business history between requests, sets no-store
on responses and creates no persistent MCP session. Calculation data is used
for the response. The source does not promise cryptographic erasure of process
memory or the provider's buffers. Provider/account logging and backup retention
must be confirmed and disclosed for the actual deployment; no Australian-only
processing or universal deletion interval is asserted.

The deployment profile uses two native Cloudflare rate-limit bindings. The
Worker supplies a digest of the edge-provided IP address (or a shared unknown
bucket) and a fixed service key for short-lived request counters. The digest
is pseudonymous operational metadata, not guaranteed anonymous information.
Business counts are not written into these counters. Cloudflare controls
their per-location, eventually consistent handling and infrastructure retention;
the bindings do not impose accurate global or monthly accounting. Application
limits run after a Worker invocation has begun and cannot prevent all quota
exhaustion. Publisher request/body logs remain disabled in this profile.

The client host may retain the supplied numbers and returned results in the
person's chat under that host's policies/settings. The person controls which
numbers to send and can stop using/disconnect the MCP. There is no stored
business-data database to delete through this server. Removing host chats,
provider logs, local exports and backup/sync copies uses those products' own
controls. A free hosting plan does not control unrelated host/account charges.

Local weather, checkpoint and event replay remain separate optional workflows.
They never supply transcripts or files to the remote budget tool. Their data
and removal practices are documented in PRIVACY.md's local-helper section.
Uninstalling does not erase those files or older notes. Development test traces
are synthetic and remain local; `.wrangler/`, dependency folders and evidence
are excluded from release packages.

Support is public [GitHub Issues](https://github.com/FeidaWang/Token-Weather/issues).
Posting is optional and separately chosen by the person; GitHub receives their
selected public text/attachments. Do not post private recordings, notes,
credentials or identity documents. Closing an issue does not erase it; there
is no 30-day deletion promise or email support service.


---

# Optional local helpers: data and privacy

Revision date: 11 October 2026. Feida Wang, trading as RSI AI, maintains Token
Weather. This section describes the optional local helpers preserved from the Skills-only
privacy revision. The [published project privacy policy](https://feidawang.github.io/Token-Weather/privacy.html)
also covers the broader project. A matching public-web supplement is prepared
separately; it has not been published as part of building this ZIP.

## What a requested weather reading accesses

The helper needs local Codex file/command access and Python 3.11+. It uses the
exact root chat ID and workspace supplied by the host or person. Automatic
discovery inspects matching filenames under the configured Codex home's
`sessions/` directory, not other chats' contents. Archived records are used
only when their exact file is explicitly selected. Before reducing a local
record, the helper checks its root ID, workspace and supported format. A wrong
binding, ambiguous match, unknown format or symlink is rejected.

Codex record files can contain messages, tool arguments, summaries, private
data and credentials. Bounded raw record bytes necessarily enter process
memory while reading them. The projection parser scans ignored JSON values
without decoding or constructing their message/tool/summary payloads. It
decodes only allowlisted identity/version fields needed to check the source,
usage counts, timestamps, model/thinking labels and relevant lifecycle flags.
This minimises processing; it is not a promise that no private bytes are ever
encountered, nor an eligibility decision by OpenAI.

A one-off `weather` reading defaults to no saved history and no config-file
read. It reads the exact header and at most a 4 MiB tail, with a 256 KiB record
limit; history may be incomplete. `--cache-history` explicitly requests an
incremental numeric cache, reading at most 8 MiB per scan and retaining at most
400 samples per chat. Config is read only with `--read-config`; the helper
decodes just three supported top-level model/reference fields, not unrelated
provider or credential configuration. These are advisory values, never proof
of native compaction policy. `--compact-limit` supplies a reference directly.

Default weather JSON, offline HTML and the weather API omit root/turn IDs and
paths. They still contain necessary usage, timestamps, model/thinking labels,
freshness and available numerical account windows. These are estimates, not
private ChatGPT web-context access, billing records or control authority.

## Local weather storage and the requested page

Opt-in numeric caches live under `$CODEX_HOME/state/token-weather-skills`
(`~/.codex/state/token-weather-skills` by default), or the exact
`TOKEN_WEATHER_SKILLS_DATA_DIR` selected by the person. The full edition's
`TOKEN_WEATHER_DATA_DIR` and stored history are not automatically used.

Caches contain numerical history, timestamps, model/thinking labels, quota
windows when present, file identity/cursor data and integrity hashes. Chat/path
bindings and local turn identifiers are hashed in the numeric cache, not
stored as plaintext. Hashing is not encryption or guaranteed anonymisation.
Messages, tool arguments and compaction summaries are not saved there.

`weather-service start` is a separately requested background collector and
loopback page on `127.0.0.1`; starting it saves numeric history. It keeps the
exact root/workspace/transcript or capture path, polling settings, PID/port,
process identity and a generated local control token in private service files
to reuse and stop only its own instance. That token is not an account credential.
Service status requires it and does not return plaintext chat/workspace
bindings. Weather output does not expose the token. Process logs are local;
errors reported to the caller omit exception contents and private paths.

Closing the browser tab does not stop the collector. Ask to stop the page or
run `weather-service stop` with the same root ID. A foreground `weather-serve`
page does not cache unless `--cache-history` is selected and stops with Ctrl+C.
The original page's display preference uses browser localStorage, separately
from the usage data.

## Checkpoints and evidence

Checkpoint storage is opt-in through a requested `init` or an explicitly named
enrolled workflow. This revision uses `.codex/handover-skills/<workflow>` in
the project, separately from the full/earlier edition's `.codex/handover/`.
Old workflows are not imported, changed or deleted automatically.

Save only short task goals, constraints, decisions, progress, unresolved
effects and next steps. Notes may still be confidential. Do not copy a full
conversation, raw tool output, credentials, identity documents, payment-card
data or protected health information into a checkpoint. Avoid unnecessary
personal details. Describe a dependency by a task-specific label rather than
copying a secret. The helper rejects common API-key/private-key/credential
assignment patterns before writing, but this is not a comprehensive detector
of secrets or sensitive personal information; review the selected notes.

Stored checkpoint data includes the selected notes, workflow/root ownership,
workspace identity, generations, timestamps, deduplication keys, hashes and
any chosen evidence references. Integrity and write-lease checks need this
metadata. The ledger and immutable generations retain earlier notes. Updating
a current note does not erase prior copies. Files use private local permissions;
the plugin does not encrypt them. Backups/syncs and other privileged local
software can have access according to the person's configuration.

`prepare` and `bootstrap` verify owned checkpoint integrity but do not read
referenced evidence files by default. Only `--verify-evidence`, for an explicitly
requested check, reads the files already referenced in this workflow. Paths
must be relative to this workspace without symlinks or traversal, and each
file is bounded to 4 MiB. Do not pin unrelated or restricted-data files. External
verification-cache references are unsupported. Without the option, a saved
hash is a recorded claim, not a freshly verified check. Bootstrap returns the
selected task notes; `--ledger` requests at most 20 specific older rows.

## Recorded-event replay and exports

Replay reads only the exact recording supplied by the person. Runtime replay
is bounded to 256 KiB/500 events; weather JSONL capture replay is bounded to
4 MiB. The projection drops message previews, prompt/tool bodies and error
text; lifecycle replay retains only an error-presence flag. Raw input bytes
still enter memory. The original timestamp is retained, so an old recording
does not become live telemetry. Replay executes no recorded command or edit.

Default replay results omit root/workspace/connection identifiers and summarise
control members/operations by counts. `--include-local-metadata` explicitly
requests detailed local binding and lifecycle identifiers; it does not restore
ignored message/tool payloads. Keep that diagnostic report local. Reports and
offline pages are written only to an explicitly selected `--output`/`--html`
path. An export must not overwrite its input recording or checkpoint files.

## Recipients, retention and deletion

These local weather/checkpoint/replay helpers make no publisher-server, analytics or paid-model call. The
weather page uses local resources and loopback traffic. Requested CLI/Skill
outputs can enter the user's Codex conversation and be processed by its host
under applicable policies/settings. User-selected exports, clipboard actions,
backups and synchronisation follow the selected services. Other software with
access to the same device/account can access local files; loopback is not an
encrypted storage boundary.

There is no timed automatic expiry or remote deletion service. Opt-in weather
cache/service files remain until removed, subject to the 400-sample bound.
Checkpoint notes, ledger, generations and exports remain until separately
removed. Uninstalling the plugin, archiving a chat or expiring evidence does
not delete this data. Future readings can reconstruct a weather cache from
the original record.

For the exact selected storage locations, run `privacy-status`. This is a
read-only location report; it does not create folders. To remove local data:

1. Stop the relevant collector with `weather-service stop` and confirm its
   state. Stop any workflow writers before removing checkpoint data.
2. Remove only the confirmed Skills-edition cache/service files or that named
   `.codex/handover-skills/<workflow>` directory. Inspect the path first; do
   not delete original Codex sessions, the full edition or unrelated workflows.
3. Remove selected exports, backups/sync copies and browser site storage
   separately. Deleting current notes alone does not remove ledger/generation
   copies, host chat history or the original supplied recording.

Deletion is a separate user decision; no cleanup is performed by setup or by
showing weather. If the person chooses to post a support issue, GitHub receives
their chosen public text and attachments. Do not post private records or
credentials. Support is [GitHub Issues](https://github.com/FeidaWang/Token-Weather/issues);
email support and identity-document collection are not offered. Closing an
issue does not erase it, and there is no 30-day support deletion promise.
