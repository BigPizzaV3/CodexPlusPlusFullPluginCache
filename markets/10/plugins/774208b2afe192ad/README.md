# ScoreStarling

Convert musical content across sound, pictures, documents and score files. Start
from an audio or video recording, a sheet-music image or PDF, MIDI, MusicXML, ABC,
numbered notation, a lead sheet or music written in chat. Create an editable,
playable score, review or preview changes, and export PDF, SVG/PNG images, MusicXML,
MIDI, MP3/WAV audio, ABC, MEI, parts or numbered notation.

This plugin combines the hosted ScoreStarling MCP tools with two workflow skills:
`scorestarling-score` for audio/video recordings and `scorestarling-notation` for
sheet music, score files and music written in the chat.
It is maintained by individual developer HaiyiMei.
The OpenAI listing uses the verified developer name HAIYI MEI.

## Access and use

Sign in with a ScoreStarling account and approve the MCP connection through the
client’s OAuth flow. Each account can run two transcriptions at a time.

Ask: "Turn this attached recording into a score, open it, and help me check it." or
"Make this photo of sheet music playable and give me the MIDI."
One instrument or voice, and solo piano with both hands and pedal, are free; a band uses credits.
Uploads are limited to 50 MiB, or 120 MiB as WAV, AIFF or FLAC. Each transcription covers the account’s supported excerpt, up to five minutes.
Read `get_account_usage.max_seconds` for its current limit before starting. A band's
price is shown, and agreed in the chat, before it starts. The skill checks tool results and score structure,
but listening and human review remain necessary for transcription accuracy.
Model-proposed musical edits are previews until the user accepts them.

## What connects and runs

The plugin connects only to `https://mcp.scorestarling.com/mcp`; audio uploads go to
`https://scorestarling.com`. The client's authorized MCP connection reads or changes
the signed-in user's scores and starts requested transcriptions. When the user
chooses a band transcription and agrees to its price, the service sends the recording to
Mirelo, the band transcription provider, within a limit the server sets from the recording's
length; the user sees only the price in credits.
The service's privacy policy covers Supabase/Railway storage and Sentry/PostHog
diagnostics.

ChatGPT uses its native attachment tool. For a readable local attachment, the
optional Python 3.11 upload helper requires HTTPX and network access. It receives
an explicitly prepared, one-use upload ticket on stdin, posts raw audio once to
the matching ScoreStarling origin, and reports acceptance. Status checks use the
connected host's tools. Its programmatic entry can prepare and poll through an
already-authorized tool callback. It installs nothing and reads no environment
credentials. It sends no OAuth token or cookie on the capability POST and follows
no redirects. If code or network is unavailable, use the built-in upload panel.

## Distribution and support

The portable `plugin.json` / `mcp.json` package is for ChatGPT and Codex. Claude's
`.claude-plugin/plugin.json` and `.mcp.json` reference the same skill and service.
This package does not include the backend, a local MCP server, hooks or subagents.
Actual installation and automatic skill selection must be checked in each client
before publishing. Public publication on Claude requires a public GitHub source
and a separate submission of our remote MCP connector.

A direct MCP connection receives concise initialization instructions, tool metadata and
state-dependent next steps, plus `get_workflow_guide` for recording, notation, editing, each
edit action's limits (operations) or feedback. It does not install native skills. The complete workflows remain in these two
skills; their marked MCP essentials share `apps/server/workflow_guidance.py` and are checked
by `scripts/sync_workflow_guidance.py`. After editing those shared rules, run the script with
`--write` and run `tests/mcp/check_workflow_guidance.py`.

OpenAI documents server instructions as guidance used alongside tool metadata. Its MCP
skills extension imports a static snapshot during submission through Scan Tools; it does
not fetch skills at runtime. This package does not implement that extension. See
[server instructions](https://developers.openai.com/plugins/build/mcp-server#create-the-server)
and [skill imports](https://developers.openai.com/plugins/build/skills#import-a-skill-from-mcp).

Use the hosted MCP tools for account-scoped actions and the skill for the
transcribe, review, preview, accept and export workflow. Start with an actual
chat attachment; the code upload helper and built-in upload panel are fallbacks.

- [Connection guide](https://scorestarling.com/mcp)
- [Support](https://scorestarling.com/support)
- [Privacy](https://scorestarling.com/privacy)
- [Service terms](https://scorestarling.com/terms)

The plugin files are licensed under MIT; see [LICENSE](LICENSE). This package's
license does not cover customer audio, customer scores or the hosted backend.
Support, terms and privacy pages are hosted by the website; changing this
package does not deploy them.

## Development and releases

This public repository is the canonical source of the plugin. The private product
repository pins it as a Git submodule; backend changes do not release this package.

Run `python3 tests/check_plugin_build.py` and validate both Claude manifests before
release. `python3 scripts/build_plugin.py` builds a deterministic ZIP from the Git
index; `--source working-tree` builds tracked local changes. CI files, tests and
top-level developer scripts are excluded from the ZIP.

Update both manifest versions, commit, and push a matching `v<version>` tag to
release. CI checks the tag and manifests, creates the GitHub ZIP release, and
advances the `release` branch only after checks pass. Claude directory submissions
track that branch, so ordinary commits to `main` do not publish a plugin update.
OpenAI directory uploads and review remain separate steps. Review videos and
reviewer credentials are supplied privately rather than included here.
