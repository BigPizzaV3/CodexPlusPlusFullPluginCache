# Unicycle

One voice conversation for your existing Codex tasks.

Unicycle is a local Codex desktop workflow plugin. It uses native task tools to read state changes, surface meaningful decisions and previews, and route your scoped answers to the correct owner. A small Python cache remembers cursors and delivery attempts across restarts.

## Start

Install the plugin from its configured local marketplace, then select it from the plugin listing or explicitly invoke `$unicycle:coordinate` in Codex. A truncated general skill catalog can omit it even when the native registry discovers it. Open native voice in that conversation and name the existing tasks you want to follow. The coordinator checks capabilities and registers those owners. No API key, additional speech service, or background server is required.

Setup stays inside Codex: a native question selects existing owners, then the coordinator confirms their identities and actual capability checks. There is no website-style setup. The plugin listing supplies starter prompts; this plugin does not add a custom Codex settings panel. Native task and question tools must be available in the host; CLI-only contexts can test the cache but cannot prove desktop voice behavior.

## What stays separate

- Native voice is the conversation surface. Unicycle does not provide a new voice engine or programmatically choose an accent.
- Existing tasks own execution and approvals. A completed turn does not prove the whole goal complete.
- SQLite state lives outside the package, defaults to `~/.local/state/unicycle`, and can be overridden with `--state-dir` or `UNICYCLE_STATE_DIR`.
- The cache cannot verify a speaker's identity or authenticate consent. The host agent must validate genuine user input and exact scope before dispatch.
- Preview tabs use native supported placement. A queued tab is not proof that the user saw it.
- No telemetry, remote service, automatic publication, UI scraping, or global settings changes are included.

Unicycle is the default persona with transatlantic cadence direction. Jarvis and Evie/EV are optional Easter-egg personality labels. Actual synthesized voice remains controlled by Codex. The labels imply no official character affiliation.

## Tests and distribution

Run `python3 -m unittest discover -s tests -v` from the plugin root. Tests use synthetic identities in temporary private state. Package only the manifest, skill, helper, tests and documentation. Never include runtime state, local history, user identifiers, private receipts, or host configuration backups.

This is an early local integration. Host capabilities and live user-answer/visual verification are required before a public completion or release claim. Distribution destination is configured by the publisher; none is assumed.

Plugin structure follows [OpenAI plugin packaging guidance](https://developers.openai.com/plugins/build/plugins). Local installation and native tools depend on the current Codex host.
