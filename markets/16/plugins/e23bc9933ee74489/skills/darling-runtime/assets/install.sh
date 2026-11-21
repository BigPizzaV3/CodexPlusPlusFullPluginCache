#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [ "$(uname -m)" != "x86_64" ]; then echo "This bundle targets amd64/x86_64 only." >&2; exit 2; fi
if ! grep -qsE '(^|[[:space:]])VERSION_CODENAME=noble([[:space:]]|$)' /etc/os-release; then
  echo "Warning: bundled packages target Ubuntu 24.04 (noble)." >&2
fi
sudo apt update
sudo apt install -y "$HERE"/binaries/*.deb
