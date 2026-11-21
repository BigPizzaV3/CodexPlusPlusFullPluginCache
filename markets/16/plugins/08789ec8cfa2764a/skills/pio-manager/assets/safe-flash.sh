#!/bin/bash
# Retired auto-detect fallback: no uploads, monitor termination, or monitor startup.
printf '%s\n' 'PIO Agent safe-flash fallback is disabled. Use the guarded pio-agent CLI or an existing PlatformIO MCP session with explicit project, environment, resolved target, policy and approval. If neither is available, stop and restore PIO Agent before retrying.' >&2
exit 1
