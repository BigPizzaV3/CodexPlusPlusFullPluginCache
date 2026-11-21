#!/usr/bin/env bash
# Usage: scripts/new-plugin.sh <slug>
# Copies the template to /workspace/plugins/<slug>, renames the worker to <slug>-stag, installs deps (hardlinked from
# the template's node_modules), and leaves src/plugin.config.ts + tests/plugin.test.mjs as the only files to write.
set -euo pipefail
slug="${1:?slug}"
[[ "$slug" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "slug must be kebab-case"; exit 2; }
T="$(cd "$(dirname "$0")/.." && pwd)"
D="/home/lauki/workspace/plugins/$slug"
[ -e "$D" ] && { echo "exists: $D"; exit 3; }
mkdir -p "$D"
rsync -a --exclude node_modules --exclude dist --exclude .wrangler --exclude .git --exclude README.md --exclude BRIEF.md --exclude plugin.json --exclude .app.json --exclude .codex-plugin --exclude mcp.json "$T/" "$D/"
cp -al "$T/node_modules" "$D/node_modules" 2>/dev/null || cp -a "$T/node_modules" "$D/node_modules"
sed -i "s/^name = \".*\"/name = \"$slug-stag\"/" "$D/wrangler.toml"
sed -i "s/\"name\": \"chatgpt-plugin-template\"/\"name\": \"$slug\"/" "$D/package.json"
printf '# %s\n\nChatGPT app built from /workspace/chatgpt-plugin-template. Edit src/plugin.config.ts and tests/plugin.test.mjs only.\n\nStaging MCP: https://%s-stag.upsurge.workers.dev/mcp\nPrivacy: https://%s-stag.upsurge.workers.dev/privacy\n' "$slug" "$slug" "$slug" > "$D/README.md"
echo "$D"
