# Surface Adaptation

## ChatGPT web

Rely on plugin/skill discovery and skill selection.
Installing the plugin on ChatGPT web does not deploy hook scripts into a
local execution environment. Do not promise SessionStart execution there.

The orchestrator remains useful through skill selection alone.

## ChatGPT Work

Use the normal plugin skill when available.
Where the Work runtime supports the packaged hook and the script is present,
the SessionStart bootstrap may provide stronger automatic activation.

Unmanaged packaged hooks require the user or administrator to review and trust the current hook definition before execution.

## Codex

Use the portable plugin manifest as the canonical package definition.
Use `hooks/hooks.json` for SessionStart bootstrap when the hook is present
and trusted.

The hook only injects compact routing policy. It must not enumerate all
installed capabilities.

## Hosts without executable hooks

Use skill selection alone. Do not emulate a hook by claiming that a startup
script ran when it did not.

## Capability names

The core skill must remain capability-oriented rather than hard-code specific
providers. Surface-specific tooling may be used when the host exposes it,
but downstream capability names are discovered at runtime.
