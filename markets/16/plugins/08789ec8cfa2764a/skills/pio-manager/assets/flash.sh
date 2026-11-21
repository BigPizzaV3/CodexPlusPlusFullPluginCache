#!/bin/bash
# Retired raw-flash fallback: preserve the path without bypassing PIO Agent gates.
printf '%s\n' 'PIO Agent flash fallback is disabled. Use the guarded pio-agent CLI or an existing PlatformIO MCP session with explicit project, environment, resolved target, policy and approval. If neither is available, stop and restore PIO Agent before retrying.' >&2
exit 1
