#!/usr/bin/env bash

script_dir=$(cd -- "$(dirname -- "$0")" && pwd) || exit 0
source "$script_dir/cli-install-common.sh"
minimum=$(cat "$script_dir/../cli-min-version" 2>/dev/null)
message=
if ! clay_valid_version "$minimum"; then
  message='Clay plugin compatibility metadata is missing or invalid. Refresh the Clay plugin before using its CLI.'
else
  executable=$(command -v clay || true)
  if [ -z "$executable" ]; then
    message="Clay CLI setup required: no clay command is on PATH. Do not run clay directly. Read the clay entry skill for access and setup instructions."
  else
    method=$(clay_install_method "$executable")
    case "$method" in
      legacy|legacy-npm)
        message="Clay CLI setup required: the clay command on PATH is a legacy plugin launcher or npm installation. Do not run clay directly, even if it works. Read the clay entry skill for access and setup instructions."
        ;;
      *)
        version=$(clay_read_version "$executable" || true)
        if ! clay_version_at_least "$version" "$minimum"; then
          message="Clay CLI setup required: the clay command on PATH is outdated or cannot run. Do not run clay directly. Read the clay entry skill for access and setup instructions."
        fi
        ;;
    esac
  fi
fi
[ -n "$message" ] || exit 0
message="For CLI access only: $message Read the clay entry skill to determine whether CLI access is needed for this task."
case "${1:-plain}" in
  claude|codex) printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' "$message" ;;
  cursor) printf '{"additional_context":"%s"}\n' "$message" ;;
  *) printf '%s\n' "$message" ;;
esac
exit 0
