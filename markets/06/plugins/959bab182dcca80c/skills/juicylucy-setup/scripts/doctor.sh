#!/bin/sh
# JuicyLucy: report what ad production needs and what this machine has.
#
# POSIX sh on purpose. The first thing this checks is whether Node exists, so it
# cannot itself be a Node script — on a fresh machine there would be nothing to
# run it with. macOS always has /bin/sh.
#
# Read-only. It installs nothing, writes nothing, and touches no config. (The
# juicy-skill line regenerates the skill into a scratch folder to compare it,
# and deletes the folder.) Two lines reach the network, and each says so when
# it cannot: juicy-version asks the registry whether a newer juicy exists, and
# juicy-login asks the generation service whose session this machine holds.
#
#   sh doctor.sh             human-readable
#   sh doctor.sh --quiet     the STATUS lines only, for a caller to parse
#   sh doctor.sh --preflight the STATUS lines, then one `preflight` line; for
#                            the ad workflows, which run it before Step 0
#
# Exit code is the number of missing requirements, so a caller can branch on it.
#
# --preflight answers a narrower question: has setup been run on this machine?
# It counts only the toolchain lines — what install.sh puts down and whether
# PATH reaches it (node, hyperframes, hf-version, ffmpeg, ffprobe,
# ffmpeg-on-path, adspython, juicy, on-path) — and skips the registry call. The
# other lines are still printed but do not decide: chrome is fetched on the
# first render, a newer juicy is an update rather than an absence, the sign-in,
# the config file and the sandbox table each say so themselves at the step that
# needs them, and the skills line is inventory. An ad run on a machine with no
# toolchain cannot even create its project; one with a toolchain and a missing
# sign-in gets as far as generation and is told exactly what to do there.

set -u

# See install.sh: a config.toml PATH from an earlier setup left Codex's commands
# without /usr/bin. Restore the system directories so this script can run its
# own checks; the `env` line below still reports the PATH as it was found.
FOUND_PATH="$PATH"
PATH="$PATH:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export PATH

JUICYLUCY_HOME="${JUICYLUCY_HOME:-$HOME/.juicylucy}"
NODE_MIN=22
MISSING=0
QUIET=0
PREFLIGHT=0
for arg in "$@"; do
  case "$arg" in
    --quiet) QUIET=1 ;;
    --preflight) PREFLIGHT=1; QUIET=1 ;;
    *) printf 'doctor.sh: unknown option %s\n' "$arg" >&2; exit 64 ;;
  esac
done

# The lines --preflight decides on, and what it found missing among them.
PREFLIGHT_LINES=" node hyperframes hf-version ffmpeg ffprobe ffmpeg-on-path adspython juicy on-path "
PREFLIGHT_MISSING=0
PREFLIGHT_NAMES=""

say() { [ "$QUIET" -eq 1 ] || printf '%s\n' "$*"; }

# `name  ok|missing  detail` — one line per requirement, always printed.
status() {
  printf '%-12s %-8s %s\n' "$1" "$2" "$3"
  if [ "$2" = "missing" ]; then
    MISSING=$((MISSING + 1))
    case "$PREFLIGHT_LINES" in
      *" $1 "*) PREFLIGHT_MISSING=$((PREFLIGHT_MISSING + 1)); PREFLIGHT_NAMES="$PREFLIGHT_NAMES${PREFLIGHT_NAMES:+, }$1" ;;
    esac
  fi
  return 0
}

# First existing executable among the arguments, or empty.
first_exec() {
  for candidate in "$@"; do
    [ -n "$candidate" ] && [ -x "$candidate" ] && printf '%s' "$candidate" && return 0
  done
  return 0
}

resolve() { command -v "$1" 2>/dev/null || true; }

say ""
say "JuicyLucy setup — checking this machine"
say ""
status arch ok "$(uname -m) ($(uname -s))"

# ── node ──────────────────────────────────────────────────────────────────────
NODE_BIN=$(first_exec "$JUICYLUCY_HOME/node/bin/node" "$(resolve node)")
if [ -z "$NODE_BIN" ]; then
  status node missing "not found — nothing else can run without it"
else
  NODE_VER=$("$NODE_BIN" --version 2>/dev/null | tr -d 'v')
  NODE_MAJOR=${NODE_VER%%.*}
  if [ "${NODE_MAJOR:-0}" -lt "$NODE_MIN" ] 2>/dev/null; then
    status node missing "v$NODE_VER is too old — v$NODE_MIN or newer is required"
  else
    status node ok "v$NODE_VER at $NODE_BIN"
  fi
fi

# ── the hyperframes CLI ───────────────────────────────────────────────────────
# The skills were written against one CLI version (UPSTREAM.lock: cli); the
# installer pins it, and the hf-version line says whether this machine has it.
HF_EXPECTED="0.8.71"
HF_VER=""
HF_BIN=$(first_exec "$JUICYLUCY_HOME/node_modules/.bin/hyperframes" "$(resolve hyperframes)")
if [ -n "$HF_BIN" ]; then
  status hyperframes ok "$HF_BIN"
  HF_VER=$("$HF_BIN" --version 2>/dev/null | head -1 | tr -d 'v')
  if [ "$HF_VER" = "$HF_EXPECTED" ]; then
    status hf-version ok "$HF_VER"
  else
    status hf-version missing "installed ${HF_VER:-unknown}, expected $HF_EXPECTED — re-run setup's tools step"
  fi
else
  status hyperframes missing "the program that renders the video is not installed"
fi

# ── ffmpeg / ffprobe ──────────────────────────────────────────────────────────
# The env vars win, which is the whole reason a system ffmpeg is optional:
# packages/parsers reads HYPERFRAMES_FFMPEG_PATH / HYPERFRAMES_FFPROBE_PATH
# before it scans PATH.
ARCH=$(uname -m)
[ "$ARCH" = "x86_64" ] && FF_ARCH=x64 || FF_ARCH=arm64
FFMPEG_BIN=$(first_exec "${HYPERFRAMES_FFMPEG_PATH:-}" \
  "$JUICYLUCY_HOME/node_modules/ffmpeg-static/ffmpeg" "$(resolve ffmpeg)")
FFPROBE_BIN=$(first_exec "${HYPERFRAMES_FFPROBE_PATH:-}" \
  "$JUICYLUCY_HOME/node_modules/@ffprobe-installer/darwin-$FF_ARCH/ffprobe" "$(resolve ffprobe)")
[ -n "$FFMPEG_BIN" ] && status ffmpeg ok "$FFMPEG_BIN" || status ffmpeg missing "the video encoder is not installed"
[ -n "$FFPROBE_BIN" ] && status ffprobe ok "$FFPROBE_BIN" || status ffprobe missing "the video inspector is not installed"

# ── bare `ffmpeg` on PATH ─────────────────────────────────────────────────────
# Separate from the check above on purpose. Those env vars are read by
# hyperframes; the ad skills also run ffmpeg and ffprobe DIRECTLY, and a bare
# `ffmpeg` that resolves to a system build is a different program with different
# filters. Observed: Homebrew's ffmpeg has no libfreetype, so `drawtext` is
# missing, and an agent that hit it abandoned the render path entirely.
PATH_FFMPEG=$(resolve ffmpeg)
if [ -z "$PATH_FFMPEG" ]; then
  status ffmpeg-on-path missing "the skills call ffmpeg directly — add $JUICYLUCY_HOME/bin to PATH"
elif [ "$PATH_FFMPEG" = "$JUICYLUCY_HOME/bin/ffmpeg" ] || [ "$PATH_FFMPEG" = "$FFMPEG_BIN" ]; then
  status ffmpeg-on-path ok "$PATH_FFMPEG"
elif "$PATH_FFMPEG" -hide_banner -filters 2>/dev/null | grep -q ' drawtext '; then
  status ffmpeg-on-path ok "$PATH_FFMPEG (not ours, but has drawtext)"
else
  status ffmpeg-on-path missing \
    "bare ffmpeg is $PATH_FFMPEG, which lacks drawtext — put $JUICYLUCY_HOME/bin ahead of it on PATH"
fi

# ── headless Chrome ───────────────────────────────────────────────────────────
# hyperframes downloads its own, so this is only "not yet fetched", never a
# manual install.
if [ -d "$HOME/.cache/puppeteer" ] && [ -n "$(ls -A "$HOME/.cache/puppeteer" 2>/dev/null)" ]; then
  status chrome ok "cached in ~/.cache/puppeteer"
else
  status chrome missing "hyperframes will download it (hyperframes browser ensure)"
fi

# ── Python QA (statics) ──────────────────────────────────────────────────────
# The statics QA scripts run through the adspython shim — our own standalone
# CPython under JUICYLUCY_HOME with Pillow in it. install.sh --only python sets
# it up; nothing here ever runs the Mac's python3, which may be a stub that
# opens Apple's Command Line Tools installer.
ADSPY=$(first_exec "$JUICYLUCY_HOME/bin/adspython" "$(resolve adspython)")
if [ -n "$ADSPY" ] && "$ADSPY" -c "import PIL" 2>/dev/null; then
  status adspython ok "$ADSPY ($("$ADSPY" --version 2>&1))"
else
  status adspython missing "the statics QA interpreter — install.sh --only python sets it up"
fi

# ── the juicy command ─────────────────────────────────────────────────────────
# Every image, video and music generation goes through `juicy`, which setup
# installs at the NEWEST published version and the user signs in to once. The
# skill that tells the agent how to use it is generated by the installed
# binary itself into ~/.agents/skills/juicy-cli, where its name replaces the
# plugin's copy. Four lines, so "not installed", "a newer one is out", "the
# skill is not this version's" and "not signed in" each name their own fix.
# `--version` and `skill` read local files only. Two lines call out: the
# registry check, through npm, and `auth status`, which asks the generation
# service. Either being unreachable is reported as exactly that — not as a
# problem with the machine, and not as a missing sign-in.
JUICY_PKG="@juicylucy/cli"
JUICY_SKILL="$HOME/.agents/skills/juicy-cli"
# `a` is older than `b`, as x.y.z triples.
ver_lt() {
  a1=${1%%.*}; rest=${1#*.}; a2=${rest%%.*}; a3=${rest#*.}
  b1=${2%%.*}; rest=${2#*.}; b2=${rest%%.*}; b3=${rest#*.}
  [ "$a1" -lt "$b1" ] 2>/dev/null && return 0
  [ "$a1" -eq "$b1" ] 2>/dev/null && [ "$a2" -lt "$b2" ] 2>/dev/null && return 0
  [ "$a1" -eq "$b1" ] 2>/dev/null && [ "$a2" -eq "$b2" ] 2>/dev/null && [ "$a3" -lt "$b3" ] 2>/dev/null && return 0
  return 1
}
JUICY_BIN=$(first_exec "$JUICYLUCY_HOME/bin/juicy" "$JUICYLUCY_HOME/node_modules/.bin/juicy" "$(resolve juicy)")
if [ -z "$JUICY_BIN" ]; then
  status juicy missing "the command that generates images, video and music — install.sh --only juicy"
else
  status juicy ok "$JUICY_BIN"
  # Its launcher needs a node on PATH; put the one we found first.
  JUICY_PATH="${NODE_BIN:+$(dirname "$NODE_BIN"):}$PATH"
  JUICY_VER=$(PATH="$JUICY_PATH" "$JUICY_BIN" --version 2>/dev/null | sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' | head -1)
  # The npm on PATH first — the one Codex's config puts there — then the one
  # beside the node we found, for a machine whose config is not in place yet.
  NPM_BIN=$(first_exec "$(resolve npm)" "${NODE_BIN:+$(dirname "$NODE_BIN")/npm}")
  JUICY_LATEST=""
  [ "$PREFLIGHT" -eq 0 ] && [ -n "$NPM_BIN" ] && JUICY_LATEST=$(PATH="$JUICY_PATH" "$NPM_BIN" view "$JUICY_PKG" version --fetch-retries=0 --fetch-timeout=15000 2>/dev/null | tr -d '[:space:]"')
  case "$JUICY_LATEST" in [0-9]*.[0-9]*.[0-9]*) ;; *) JUICY_LATEST="" ;; esac
  if [ -z "$JUICY_VER" ]; then
    status juicy-version missing "juicy runs but prints no version — re-run setup's juicy step"
  elif [ "$PREFLIGHT" -eq 1 ]; then
    status juicy-version ok "$JUICY_VER (the registry is not asked in preflight; the full doctor checks for a newer one)"
  elif [ -z "$JUICY_LATEST" ]; then
    status juicy-version ok "$JUICY_VER (could not reach the registry to check for a newer one)"
  elif ver_lt "$JUICY_VER" "$JUICY_LATEST"; then
    status juicy-version missing "installed $JUICY_VER, newest is $JUICY_LATEST — re-run setup's juicy step"
  elif [ "$JUICY_VER" = "$JUICY_LATEST" ]; then
    status juicy-version ok "$JUICY_VER (the newest published)"
  else
    status juicy-version ok "$JUICY_VER (ahead of the registry's $JUICY_LATEST — a build installed by hand)"
  fi
  # The skill: absent, or not byte-for-byte what this binary generates, is
  # the same fix — the plugin's fallback copy and a stale local copy are both
  # some other version's description of the command.
  if [ ! -f "$JUICY_SKILL/SKILL.md" ]; then
    status juicy-skill missing "no skill describing the installed juicy at $JUICY_SKILL — re-run setup's juicy step"
  else
    JUICY_SKILL_TMP=$(mktemp -d)
    if PATH="$JUICY_PATH" "$JUICY_BIN" skill --dir "$JUICY_SKILL_TMP" >/dev/null 2>&1 \
        && diff -r "$JUICY_SKILL_TMP/juicy-cli" "$JUICY_SKILL" >/dev/null 2>&1; then
      status juicy-skill ok "$JUICY_SKILL is what juicy ${JUICY_VER:-} generates"
    else
      status juicy-skill missing "$JUICY_SKILL is not what the installed juicy ${JUICY_VER:-} generates — re-run setup's juicy step"
    fi
    rm -rf "$JUICY_SKILL_TMP"
  fi
  # The session. `auth status` asks the service (it reports the balance), so
  # inside a sandbox with the network off it fails — and a failure to ask is
  # not an answer. juicy says "no session" itself: exit 3, before any request
  # when the file is absent, or when the service refuses the one it holds. A
  # `network` error therefore means a session IS on disk and could not be
  # confirmed; it is reported as that, never as "not signed in", which sends
  # the agent to ask the user for a password this machine does not need.
  JUICY_AUTH=$(PATH="$JUICY_PATH" "$JUICY_BIN" auth status 2>&1); JUICY_AUTH_EXIT=$?
  JUICY_WHO=$(printf '%s\n' "$JUICY_AUTH" | sed -n 's/.*"email": *"\([^"]*\)".*/\1/p' | head -1)
  JUICY_AUTH_CODE=$(printf '%s\n' "$JUICY_AUTH" | sed -n 's/.*"code": *"\([^"]*\)".*/\1/p' | head -1)
  if [ "$JUICY_AUTH_EXIT" -eq 0 ] && [ -n "$JUICY_WHO" ]; then
    status juicy-login ok "signed in as $JUICY_WHO"
  elif [ "$JUICY_AUTH_EXIT" -eq 3 ]; then
    status juicy-login missing "not signed in — run juicy auth help and follow it (SKILL.md § Signing in)"
  elif [ "$JUICY_AUTH_CODE" = "network" ]; then
    # Best effort, for the account's name only; the verdict does not rest on it.
    JUICY_SAVED=$(sed -n 's/.*"email": *"\([^"]*\)".*/\1/p' "$JUICYLUCY_HOME/juicy/credentials" 2>/dev/null | head -1)
    if [ "${CODEX_SANDBOX_NETWORK_DISABLED:-}" = "1" ]; then JUICY_WHY="this command ran in a sandbox with the network off"
    else JUICY_WHY="the service could not be reached"; fi
    status juicy-login ok "a session${JUICY_SAVED:+ for $JUICY_SAVED} is on this machine, not confirmed: $JUICY_WHY — do NOT ask the user to sign in; juicy auth status run with network approval confirms it"
  else
    status juicy-login missing "could not check: juicy auth status exited $JUICY_AUTH_EXIT${JUICY_AUTH_CODE:+ ($JUICY_AUTH_CODE)} — that is not \"not signed in\"; run it and read its error before asking the user for anything"
  fi
fi

# ── the commands, bare, on PATH ───────────────────────────────────────────────
# Every line above finds its tool where setup puts it, by absolute path, so
# they all read ok on a machine whose config block was never written — or was
# written and never loaded by a restart. The skills run these commands BARE,
# so what decides whether an ad run gets past `hyperframes init` is the
# caller's PATH: each command has to resolve on it, and the renderer it
# reaches has to be the pinned one rather than a global install of some other
# version. (ffmpeg has its own line above, because a system ffmpeg is a
# different program; ffprobe is checked here.)
ON_PATH_GAPS=""
for cmd in hyperframes juicy adspython ffprobe; do
  [ -n "$(resolve "$cmd")" ] || ON_PATH_GAPS="$ON_PATH_GAPS${ON_PATH_GAPS:+, }$cmd"
done
PATH_HF=$(resolve hyperframes)
if [ -n "$PATH_HF" ]; then
  if [ "$PATH_HF" = "$HF_BIN" ]; then PATH_HF_VER="$HF_VER"
  else PATH_HF_VER=$("$PATH_HF" --version 2>/dev/null | head -1 | tr -d 'v'); fi
  [ "$PATH_HF_VER" = "$HF_EXPECTED" ] || ON_PATH_GAPS="$ON_PATH_GAPS${ON_PATH_GAPS:+, }hyperframes on PATH is ${PATH_HF_VER:-unknown} rather than $HF_EXPECTED"
fi
if [ -z "$ON_PATH_GAPS" ]; then
  status on-path ok "hyperframes $HF_EXPECTED, juicy, adspython and ffprobe all resolve on PATH"
else
  status on-path missing "$ON_PATH_GAPS — the skills run these bare; PATH in config.toml must list $JUICYLUCY_HOME/bin and $JUICYLUCY_HOME/node_modules/.bin (Step 4), then one restart"
fi

CODEX_CONFIG="${CODEX_HOME:-$HOME/.codex}/config.toml"


# ── environment ───────────────────────────────────────────────────────────────

# What the running process actually has — true only after a restart.
ENV_GAPS=""
[ "${HYPERFRAMES_SKIP_SKILLS:-}" = "1" ] || ENV_GAPS="HYPERFRAMES_SKIP_SKILLS"
[ "${HYPERFRAMES_NO_TELEMETRY:-}" = "1" ] || ENV_GAPS="$ENV_GAPS HYPERFRAMES_NO_TELEMETRY"
case ":$FOUND_PATH:" in
  *:/usr/bin:*) ;;
  *) ENV_GAPS="$ENV_GAPS PATH(no /usr/bin — curl, tar and git are unreachable)" ;;
esac
if [ -z "$ENV_GAPS" ]; then
  status env ok "skills-refresh and telemetry are both switched off; PATH is complete"
else
  status env missing "not right:$ENV_GAPS — see references/environment.md"
fi

# ── config.toml ───────────────────────────────────────────────────────────────
# The same block, read from the FILE rather than the process. This is what
# makes one restart enough: a missing key or a wrong PATH shows up here the
# moment the file is written, instead of after a restart as an `env` failure.
config_value() {
  awk -v key="$1" '
    /^\[shell_environment_policy\.set\]/ { in_table = 1; next }
    /^\[/ { in_table = 0 }
    in_table && $1 == key { sub(/^[^=]*= *"/, ""); sub(/" *$/, ""); print; exit }' "$CODEX_CONFIG"
}
CONFIG_GAPS=""
if [ -f "$CODEX_CONFIG" ]; then
  for key in HYPERFRAMES_FFMPEG_PATH HYPERFRAMES_FFPROBE_PATH HYPERFRAMES_SKIP_SKILLS HYPERFRAMES_NO_TELEMETRY; do
    [ -n "$(config_value "$key")" ] || CONFIG_GAPS="$CONFIG_GAPS $key"
  done
  CONFIG_PATH=$(config_value PATH)
  if [ -z "$CONFIG_PATH" ]; then
    CONFIG_GAPS="$CONFIG_GAPS PATH"
  else
    case "$CONFIG_PATH" in
      *'${'*|*'$PATH'*) CONFIG_GAPS="$CONFIG_GAPS PATH(contains \$PATH — Codex does not expand it; write the full list install.sh prints)" ;;
    esac
    case ":$CONFIG_PATH:" in *:/usr/bin:*) ;; *) CONFIG_GAPS="$CONFIG_GAPS PATH(no /usr/bin)" ;; esac
    case ":$CONFIG_PATH:" in *":$JUICYLUCY_HOME/bin:"*) ;; *) CONFIG_GAPS="$CONFIG_GAPS PATH(no $JUICYLUCY_HOME/bin)" ;; esac
  fi
  if [ -z "$CONFIG_GAPS" ]; then
    status config ok "config.toml carries the whole environment block"
  else
    status config missing "in config.toml:$CONFIG_GAPS"
  fi
else
  status config missing "$CODEX_CONFIG does not exist"
fi

# ── the sandbox: network, the toolchain folder, the skill folder ──────────────
# Codex's default sandbox blocks every host and every write outside the project
# folder. `juicy` needs all three: the generation service, ~/.juicylucy/juicy
# for its session and catalog cache, and ~/.agents/skills for the skill it
# writes about itself (both observed as EPERM / "Operation not permitted" from
# a workspace-write sandbox, the second measured on codex-cli 0.154.0 with a
# roots list holding only ~/.juicylucy). Setup has the user's config carry
# `network_access = true` and both folders in `writable_roots` under
# [sandbox_workspace_write]. Read from the file, like `config`, so a gap is
# caught before the restart rather than as a mysterious failure mid-ad.
sandbox_value() {
  awk -v key="$1" '
    /^\[sandbox_workspace_write\]/ { in_table = 1; next }
    /^\[/ { in_table = 0 }
    in_table && $1 == key { sub(/^[^=]*= */, ""); print; exit }' "$CODEX_CONFIG"
}
#
# The file is what setup controls, so the file decides the line. It is not the
# whole truth: a Codex client that sends its own sandbox with each thread
# (measured: Codex Desktop 0.151–0.154, every thread network-off with this
# table in place) never applies the table, and Codex marks a process whose
# network it has cut with CODEX_SANDBOX_NETWORK_DISABLED=1. When the file says
# on and the process says off, the line says both — before the restart that is
# expected; after it, juicy's calls each need the network approved.
if [ -f "$CODEX_CONFIG" ] && [ "$(sandbox_value network_access)" = "true" ]; then
  if [ "${CODEX_SANDBOX_NETWORK_DISABLED:-}" = "1" ]; then
    status network ok "[sandbox_workspace_write] network_access = true in config.toml — but this command ran with the network off: expected before the restart; after it, this Codex is not applying the table, so approve the network for juicy commands when asked (references/environment.md)"
  else
    status network ok "[sandbox_workspace_write] network_access = true in config.toml"
  fi
else
  status network missing "config.toml lacks network_access = true under [sandbox_workspace_write] — juicy cannot reach the generation service (references/environment.md)"
fi
# The config carries each folder's physical path (Codex refuses a symlinked
# root); accept a path as configured or as resolved.
JUICYLUCY_HOME_REAL=$(cd "$JUICYLUCY_HOME" 2>/dev/null && pwd -P || printf '%s' "$JUICYLUCY_HOME")
AGENT_SKILLS_DIR=$(dirname "$JUICY_SKILL")
AGENT_SKILLS_REAL=$(cd "$AGENT_SKILLS_DIR" 2>/dev/null && pwd -P || printf '%s/.agents/skills' "$(cd "$HOME" 2>/dev/null && pwd -P || printf '%s' "$HOME")")
WRITABLE_ROOTS=$( [ -f "$CODEX_CONFIG" ] && sandbox_value writable_roots )
has_root() { case "$WRITABLE_ROOTS" in *"\"$1\""*|*"\"$2\""*) return 0 ;; *) return 1 ;; esac; }
if has_root "$JUICYLUCY_HOME" "$JUICYLUCY_HOME_REAL" && has_root "$AGENT_SKILLS_DIR" "$AGENT_SKILLS_REAL"; then
  status writable ok "$JUICYLUCY_HOME and $AGENT_SKILLS_DIR are in writable_roots"
elif has_root "$JUICYLUCY_HOME" "$JUICYLUCY_HOME_REAL"; then
  status writable missing "config.toml's [sandbox_workspace_write] writable_roots lacks \"$AGENT_SKILLS_DIR\" — setup cannot write juicy's skill there from inside the sandbox (references/environment.md)"
else
  status writable missing "config.toml's [sandbox_workspace_write] writable_roots lacks \"$JUICYLUCY_HOME\" — juicy cannot keep its session or cache (references/environment.md)"
fi

# ── local skills ──────────────────────────────────────────────────────────────
# Codex reads skills from a project's .agents/skills (walked up from the working
# directory), from ~/.agents/skills and /etc/codex/skills, as well as from the
# plugin — and a copy in any of those SHADOWS the plugin's copy of the same name.
# That is how a user adds a brand or tries a change without a release
# (references/extending.md), and how setup itself puts the installed juicy's
# own description of itself ahead of the plugin's copy. It is also how a stale
# copy of a workflow skill stops receiving updates without anyone noticing, so
# intentional workflow replacements are inventory with an update reminder.
# An extra juicy-cli copy still needs checking against the installed binary.
SHIPPED_SKILLS=$(cd "$(dirname "$0")/../.." 2>/dev/null && pwd -P)
# Physical paths on both sides of the walk: a home reached through a symlink
# (/var → /private/var on a Mac) would otherwise never match and the walk
# would run past it to /.
HOME_REAL=$(cd "$HOME" 2>/dev/null && pwd -P || printf '%s' "$HOME")
skill_roots() {
  dir=$(pwd -P)
  while [ "$dir" != "$HOME_REAL" ] && [ "$dir" != "/" ]; do
    printf '%s\n' "$dir/.agents/skills"
    dir=$(dirname "$dir")
  done
  [ "$dir" = "/" ] && printf '%s\n' "/.agents/skills"
  printf '%s\n' "$HOME/.agents/skills" "/etc/codex/skills"
}
# One tab-separated line per local skill that matters: kind, name, root.
local_skills() {
  skill_roots | while IFS= read -r root; do
    # The root this doctor was shipped in is the shipped set, not a shadow of it
    # — the case when the skills are staged in a project's .agents/skills.
    [ -d "$root" ] && [ "$(cd "$root" && pwd -P)" = "$SHIPPED_SKILLS" ] && continue
    for skill in "$root"/*/; do
      [ -f "$skill/SKILL.md" ] || continue
      name=$(basename "$skill")
      short=$(printf '%s' "$root" | sed "s|^$HOME_REAL|~|; s|^$HOME|~|")
      case "$name" in
        juicylucy) printf 'replaces\t%s\t%s\n' "$name" "$short" ;;
        juicy-cli)
          # Generated where setup writes it; a copy anywhere else is a stale hand copy.
          if [ "$(cd "$root" && pwd -P)" = "$(cd "$(dirname "$JUICY_SKILL")" 2>/dev/null && pwd -P)" ]; then printf 'generated\t%s\t%s\n' "$name" "$short"
          else printf 'shadows\t%s\t%s\n' "$name" "$short"; fi ;;
        brand-*)
          if [ -d "$SHIPPED_SKILLS/$name" ]; then printf 'replaces\t%s\t%s\n' "$name" "$short"
          else printf 'added\t%s\t%s\n' "$name" "$short"; fi ;;
        *) [ -d "$SHIPPED_SKILLS/$name" ] && printf 'replaces\t%s\t%s\n' "$name" "$short" ;;
      esac
    done
  done
}
LOCAL_SKILLS=$(local_skills)
SHADOWS=$(printf '%s\n' "$LOCAL_SKILLS" | awk -F '\t' '$1 == "shadows" { printf "%s%s (in %s)", sep, $2, $3; sep = ", " }')
EXTENSIONS=$(printf '%s\n' "$LOCAL_SKILLS" | awk -F '\t' '$1 != "shadows" && NF { printf "%s%s (%s, in %s)", sep, $2, $1, $3; sep = ", " }')
if [ -n "$SHADOWS" ]; then
  status skills missing "$SHADOWS overrides the generated command reference — check it against the installed juicy version (references/extending.md)"
elif [ -n "$EXTENSIONS" ]; then
  status skills ok "local: $EXTENSIONS — local replacements do not receive plugin updates; keep intentional customizations"
else
  status skills ok "shipped skills only — no local brands or overrides"
fi

# ── the preflight verdict ─────────────────────────────────────────────────────
# One more line in the same shape, so the ad workflow reads a verdict rather
# than adding the lines up itself; the exit code says the same thing.
if [ "$PREFLIGHT" -eq 1 ]; then
  if [ "$PREFLIGHT_MISSING" -eq 0 ]; then
    if [ "$MISSING" -eq 0 ]; then
      status preflight ok "the toolchain is installed and reachable; every other line reads ok too"
    else
      status preflight ok "the toolchain is installed and reachable; $MISSING other line(s) read missing — setup's to fix, not a blocker for starting an ad"
    fi
  else
    status preflight missing "$PREFLIGHT_NAMES — setup has not been run to the end on this machine; run the juicylucy-setup skill first"
  fi
  exit "$PREFLIGHT_MISSING"
fi

say ""
if [ "$MISSING" -eq 0 ]; then
  say "Everything needed is present. Nothing to install."
else
  say "$MISSING thing(s) missing. Install what can be installed with:"
  say "  sh \"\$(dirname \"\$0\")/install.sh\""
fi
say ""
exit "$MISSING"

