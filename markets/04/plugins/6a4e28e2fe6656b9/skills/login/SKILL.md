---
name: login
description: Sign the bundled Greptile CLI in through browser OAuth when the user wants to authenticate the CLI.
---

Sign the bundled Greptile CLI in to the user's account. Tell the user that a
browser will open and they need to finish signing in there.

Resolve `<skill-root>` as the directory containing this `SKILL.md`.
Substitute that absolute path in the command; use the bundled script rather
than a separately installed `greptile` executable.

```sh
GREPTILE_NO_UPDATE_CHECK=1 node "<skill-root>/scripts/greptile.mjs" login
```

Allow up to ten minutes for the browser round-trip. If the shell tool returns
a running session, keep polling that session until login finishes.

This opens `auth.greptile.com` and saves CLI credentials in
`~/.greptile/auth.json`. The plugin's MCP connection authenticates separately
through Codex and keeps its own tokens. Signing in to one does not sign in to
the other. If the user wants MCP access, direct them to connect the Greptile
MCP server in Codex instead.
