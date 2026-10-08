# Shell Script and Debugging Patterns

## Purpose

Use this file for writing and debugging shell scripts safely.

# 1. Choose the shell intentionally

For POSIX portability:

```sh
#!/bin/sh
```

For Bash features:

```bash
#!/usr/bin/env bash
```

Do not mix syntax accidentally.

# 2. Arguments

Validate required arguments early.

Example:

```bash
if [ "$#" -ne 2 ]; then
  printf 'Usage: %s INPUT OUTPUT\n' "$0" >&2
  exit 2
fi
```

Then quote expansions.

# 3. Dependency checks

If a script requires a nonstandard command:

```bash
command -v jq >/dev/null 2>&1 || {
  printf 'jq is required\n' >&2
  exit 1
}
```

Do not silently install dependencies inside a production script unless that behavior is explicitly intended.

# 4. Error handling

Use explicit checks for critical operations.

Example:

```bash
if ! some_command; then
  printf 'some_command failed\n' >&2
  exit 1
fi
```

Use `set -u` and `pipefail` only when compatible with script behavior.

Do not assume `set -e` catches every failure in every context.

# 5. Temporary files

Use `mktemp` where available and clean up:

```bash
tmp=$(mktemp) || exit 1
trap 'rm -f -- "$tmp"' EXIT HUP INT TERM
```

Adjust for platform and resource type.

# 6. Debugging

Useful Bash techniques:
- `bash -n script.sh` for syntax;
- `set -x` / `bash -x` for tracing;
- `printf '%q\n'` in Bash when inspecting shell-escaped values;
- `shellcheck` when installed for static analysis.

Avoid enabling tracing around secrets because it can print sensitive values.

# 7. Exit status

Scripts should return:
- `0` for success;
- nonzero for failure.

Preserve or map important dependency exit statuses when callers depend on them.

# 8. Pipelines

If pipeline failures matter in Bash:

```bash
set -o pipefail
```

Then test the pipeline as a unit.

For POSIX `sh`, do not assume `pipefail` exists.

# 9. Signals and cleanup

Use `trap` for:
- temporary files;
- lock cleanup;
- child-process cleanup;
- restoring temporary state.

Do not trap every signal blindly; understand what cleanup is safe.

# 10. Idempotency

For scripts run by cron/CI/orchestration, consider:
- repeated execution;
- partial output;
- lock files;
- atomic publish;
- duplicate external actions;
- resumability.

Prefer stage → validate → publish for material outputs.
