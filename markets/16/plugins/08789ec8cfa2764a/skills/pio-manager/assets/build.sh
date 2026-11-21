#!/bin/bash
# Retired raw-build fallback: project code must run through PIO Agent policy.
printf '%s\n' 'PIO Agent build fallback is disabled. Use the guarded pio-agent CLI or an existing PlatformIO MCP session with an explicit project and environment. If neither is available, stop and restore PIO Agent before retrying.' >&2
exit 1
