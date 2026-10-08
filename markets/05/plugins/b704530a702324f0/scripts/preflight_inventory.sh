#!/usr/bin/env bash
set -eu

target_dir="${1:-.}"
if [ ! -d "$target_dir" ]; then
  echo "Target is not a directory: $target_dir" >&2
  exit 2
fi

cd "$target_dir"
printf '%s\n' "Mavixx Forge project inventory"
printf 'Directory: %s\n' "$(pwd)"

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf '%s\n' "Git: yes"
  printf 'Branch: %s\n' "$(git branch --show-current 2>/dev/null || true)"
  printf '%s\n' "Working tree:"
  git status --short
else
  printf '%s\n' "Git: no"
fi

printf '%s\n' "Detected project files:"
for item in AGENTS.md PROJECT_BRIEF.md DESIGN.md README.md package.json pnpm-lock.yaml yarn.lock package-lock.json bun.lockb pyproject.toml requirements.txt uv.lock Cargo.toml go.mod Gemfile composer.json index.html Dockerfile docker-compose.yml compose.yml .openai/hosting.json; do
  if [ -e "$item" ]; then
    printf 'Found: %s\n' "$item"
  fi
done

if [ -f package.json ]; then
  node -e 'const p=require("./package.json"); const d={...(p.dependencies||{}),...(p.devDependencies||{})}; const known=["next","react","vue","nuxt","svelte","@sveltejs/kit","astro","vite","tailwindcss","@angular/core","remix"]; console.log("Package:",p.name||"(unnamed)"); console.log("Package manager:",p.packageManager||"not declared"); console.log("Scripts:",Object.keys(p.scripts||{}).join(", ")||"none"); console.log("Framework/UI signals:",known.filter(k=>d[k]).map(k=>`${k}@${d[k]}`).join(", ")||"none detected")' 2>/dev/null || true
fi

printf '%s\n' "Application directories:"
for item in app src/app pages src/pages src components src/components styles src/styles public static tests test e2e; do
  if [ -d "$item" ]; then
    printf 'Found: %s/\n' "$item"
  fi
done

printf '%s\n' "UI and build configuration:"
for item in next.config.js next.config.mjs next.config.ts vite.config.js vite.config.ts astro.config.mjs nuxt.config.ts svelte.config.js tailwind.config.js tailwind.config.ts postcss.config.js tsconfig.json jsconfig.json eslint.config.js eslint.config.mjs; do
  if [ -e "$item" ]; then
    printf 'Found: %s\n' "$item"
  fi
done

printf '%s\n' "Environment templates and local env filenames (values are not read):"
for item in .env.example .env.sample .env.local .env.development .env.production; do
  if [ -e "$item" ]; then
    printf 'Found: %s\n' "$item"
  fi
done
