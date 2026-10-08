#!/usr/bin/env bash

set -euo pipefail

plugin_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(git -C "$plugin_dir" rev-parse --show-toplevel)"
output_path="${1:-$repo_root/productnow.zip}"

if [[ "$output_path" != /* ]]; then
  output_path="$PWD/$output_path"
fi

mkdir -p -- "$(dirname -- "$output_path")"

build_dir="$(mktemp -d "${TMPDIR:-/tmp}/productnow-plugin.XXXXXX")"
trap 'rm -rf -- "$build_dir"' EXIT

archive_path="$build_dir/productnow.zip"

(
  cd "$plugin_dir"
  COPYFILE_DISABLE=1 zip -q -r "$archive_path" \
    plugin.json \
    mcp.json \
    .codex-plugin \
    .mcp.json \
    assets \
    -x '*/.DS_Store' '__MACOSX/*'
)

unzip -tq "$archive_path"
mv -f -- "$archive_path" "$output_path"

echo "Built $output_path"
