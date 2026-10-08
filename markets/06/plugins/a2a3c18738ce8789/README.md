# Capability Orchestrator

Capability Orchestrator is a control-plane plugin for ChatGPT and Codex.
It interprets non-trivial requests, selects the smallest effective set of
specialist capabilities, and delegates focused subtasks instead of trying
to replace those specialists.

## What it routes

The skill may consider:
- specialist skills;
- plugins;
- connected apps and connectors;
- MCP tools exposed by the host;
- native tools;
- generic routers;
- direct model reasoning.

It prefers direct specialists and avoids loading unrelated capability
context.

## Activation

The main mechanism is the `capability-orchestrator` skill.

On Codex and supported ChatGPT Work runtimes, the packaged `SessionStart`
hook can inject a compact bootstrap instruction. Packaged hooks are
unmanaged hooks: review and trust the current hook definition before
expecting Codex to execute it.

Installing the plugin on ChatGPT web does not deploy executable hook
scripts. On that surface, use normal plugin/skill selection; the plugin is
designed to remain useful through skill selection alone.

## Package structure

`plugin.json` is the canonical portable manifest.
`.codex-plugin/plugin.json` is a compatibility mirror.
`hooks/hooks.json` registers the optional SessionStart bootstrap.

V1 contains no custom MCP server.

## Deterministic verification

Run:

```bash
python3 -m unittest discover -s tests -v
```

All tests must pass before packaging.

## Clean-session acceptance

Test the plugin in a clean supported session with the prompts in
`tests/fixtures/routing_cases.json`.

For each prompt, verify the listed `expect` properties and confirm that none
of the `must_not` behaviors occur.

Minimum release evidence:

1. A trivial greeting does not trigger catalog discovery.
2. A direct specialist request prefers the specialist over a generic router.
3. An email-to-calendar request uses complementary capabilities with minimal
   context transfer.
4. A missing CRM capability triggers discovery before an absence claim.
5. “Do this without plugins” is respected.
6. Router recursion terminates and never delegates to Capability Orchestrator.
7. A no-hook surface never reports that SessionStart ran.

## Security and permissions

Capability Orchestrator does not expand downstream permissions.
Installation, connection, authentication, confirmation, and mutation rules
remain those of the host and selected capability.

## Scope

V1 intentionally excludes a custom MCP router, telemetry, learned routing,
automatic plugin installation, automatic permission grants, and custom UI.


## Codex-native upload package

This distribution uses `.codex-plugin/plugin.json` as its manifest entry point and intentionally omits a root `plugin.json` to avoid Agent Plugins → Codex conversion during OpenAI Platform upload.
