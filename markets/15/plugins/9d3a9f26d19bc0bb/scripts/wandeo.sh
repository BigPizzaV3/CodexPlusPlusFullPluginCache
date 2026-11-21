#!/bin/bash
set -euo pipefail
TASK_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TASK_NODE=""
if [[ "${WANDEO_FORCE_PORTABLE_NODE:-0}" != "1" ]] && command -v node >/dev/null 2>&1 && node -e 'process.exit(Number(process.versions.node.split(".")[0]) >= 22 ? 0 : 1)'; then
  TASK_NODE="$(command -v node)"
else
  [[ "$(uname -s)" == "Darwin" ]] || { echo 'Wandeo launcher supports macOS. Use wandeo.ps1 on Windows.' >&2; exit 1; }
  case "$(uname -m)" in
    arm64) TASK_ARCH=arm64; TASK_SHA=bed7eea5325e1108f32ce5228ddd6a5f0f08a499ee42aa7442aea583702f6057 ;;
    x86_64) TASK_ARCH=x64; TASK_SHA=1462cb3b3046b815cf8ea436d3da450ec1a9f11dac7e5a46b0ada5305d7e8097 ;;
    *) echo 'Unsupported CPU architecture.' >&2; exit 1 ;;
  esac
  TASK_CACHE="${WANDEO_CACHE_DIR:-$HOME/Library/Caches/Wandeo}"
  TASK_DIRECTORY="$TASK_CACHE/node/node-v24.21.0-darwin-$TASK_ARCH"
  TASK_NODE="$TASK_DIRECTORY/bin/node"
  if [[ ! -x "$TASK_NODE" ]]; then
    mkdir -p "$TASK_CACHE/node"
    TASK_TEMP="$(mktemp -d "$TASK_CACHE/node/bootstrap.XXXXXX")"
    trap 'rm -rf "$TASK_TEMP"' EXIT
    echo '[wandeo] Preparing pinned portable Node.js' >&2
    curl --fail --location --retry 2 --output "$TASK_TEMP/node.tar.gz" "https://nodejs.org/dist/v24.21.0/node-v24.21.0-darwin-$TASK_ARCH.tar.gz" >&2
    printf '%s  %s\n' "$TASK_SHA" "$TASK_TEMP/node.tar.gz" | shasum -a 256 -c - --status 2>/dev/null || { echo 'Portable Node checksum mismatch.' >&2; exit 1; }
    tar -xzf "$TASK_TEMP/node.tar.gz" -C "$TASK_TEMP"
    if [[ ! -d "$TASK_DIRECTORY" ]]; then mv "$TASK_TEMP/node-v24.21.0-darwin-$TASK_ARCH" "$TASK_DIRECTORY"; fi
    rm -rf "$TASK_TEMP"
    trap - EXIT
  fi
fi
exec "$TASK_NODE" "$TASK_ROOT/dist/cli.mjs" "$@"
