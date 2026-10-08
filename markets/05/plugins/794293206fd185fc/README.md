# stark AI Developer

OpenAI-native adapter generated from the explicit `plugins/stark-ai-developer.source.json` allowlist.

This harness-first package contains 7 developer workflows and has no shared backend,
bundled MCP server, telemetry or analytics. Jev Capability Advisor optionally
sends supplied task text and public capability cards to TypeSafe using your own
API key; offline candidate inspection needs no network or credentials.
Canonical skill content remains maintained under
`skills/<category>/<skill>/`; this openai copy is generated and must not be edited
as a source.

Use this OpenAI-native `.codex-plugin` package only with a client that requires that native layout. It is generated at package time and is not a committed repository tree.
Standalone skill installation remains available from the repository through
`npx skills@latest`.
