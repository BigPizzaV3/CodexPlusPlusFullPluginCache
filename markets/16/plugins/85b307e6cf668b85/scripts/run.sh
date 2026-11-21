#!/usr/bin/env bash
# Compatibility entrypoint. Legacy deploy/MDM helpers are not invoked.
set -euo pipefail
exec node "$(cd "$(dirname "$0")" && pwd)/run.mjs" "$@"
