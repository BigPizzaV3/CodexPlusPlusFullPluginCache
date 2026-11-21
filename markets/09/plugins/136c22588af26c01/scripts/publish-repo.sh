#!/usr/bin/env bash
# Usage (inside /workspace/plugins/<slug>): scripts/publish-repo.sh
# Creates/updates PRIVATE github.com/laukiantonson/<slug> and pushes main. Never public.
set -euo pipefail
slug="$(node -e "console.log(require('./package.json').name)")"
printf 'node_modules/\n.wrangler/\ndist/\n' > .gitignore
[ -d .git ] || git init -q -b main
git add -A
git -c user.name="Lauki Antonson" -c user.email="hi@lauki.ai" commit -q -m "${1:-$slug: ChatGPT app v1 (staging)}" || true
if ! gh repo view "laukiantonson/$slug" >/dev/null 2>&1; then
  gh repo create "laukiantonson/$slug" --private --source . --push >/dev/null
else
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/laukiantonson/$slug.git"
  git push -q -u origin main
fi
vis="$(gh repo view "laukiantonson/$slug" --json visibility -q .visibility)"
[ "$vis" = "PRIVATE" ] || { echo "REPO NOT PRIVATE: $vis"; exit 1; }
echo "https://github.com/laukiantonson/$slug ($vis) $(git rev-parse --short HEAD)"
