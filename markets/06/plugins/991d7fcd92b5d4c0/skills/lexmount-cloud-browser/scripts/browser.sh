#!/bin/sh
set -eu
. "$(dirname -- "$0")/runtime.sh"
if [ ! -f "$binary" ]; then
  echo "CLI is not installed at $binary. Run this Skill's scripts/bootstrap.sh." >&2
  exit 127
fi
exec "$binary" "$@"
