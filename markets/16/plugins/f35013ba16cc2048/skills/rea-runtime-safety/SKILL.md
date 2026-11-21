---
name: rea-runtime-safety
description: Evaluate authorization and host risks before REA opens, executes, or interacts with a target, processes untrusted input, installs prerequisites, or changes client configuration.
---

# Runtime and host safety

REA is a local analysis tool, not a sandbox. A local provider can parse a supplied binary with the current user's permissions; runtime workflows can execute or interact with a selected target. Same-user malicious processes are outside the provider bridge's boundary.

Before proposing or invoking a stateful/runtime operation, enumerate:

1. Exact target identity, ownership/authorization, version, and source.
2. Whether the workflow is static, parses untrusted data, launches code, attaches to a process, uses a browser, or changes files/settings.
3. The exact action, target lifecycle, filesystem/network scope, runtime/provider, and permissions.
4. Expected effects, cleanup, time/resource limits, and a safer static alternative.

Proceed only within the user's explicit requested scope and host policy. Do not silently install a prerequisite, modify agent configuration, run a target, attach to an unrelated process, browse a discovered URL, or write over a user project. If authorization or target identity is missing, pause and ask; do not guess.

For public vulnerability disclosure, follow the upstream security policy: do not post exploit details, credentials, private binaries, Hopper/Ghidra projects, capability tokens, or sensitive local paths in public issues. Use the repository's private vulnerability-reporting channel.
