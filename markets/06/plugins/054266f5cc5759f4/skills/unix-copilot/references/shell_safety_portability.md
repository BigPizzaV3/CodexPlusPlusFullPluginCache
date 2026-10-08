# Shell Safety and Portability

## Purpose

Use this file for quoting, redirection, destructive commands, shell differences, filenames, privilege, and portability.

# 1. Quoting

Default rule:

```bash
"$variable"
```

when the variable represents one argument or path.

Unquoted expansions can trigger:
- word splitting;
- glob expansion;
- accidental option parsing.

Do not quote when deliberate field splitting/globbing is actually required; explain it.

# 2. Leading-dash filenames

When supported, use:

```bash
command -- "$path"
```

so a filename such as `-rf` is not interpreted as an option.

For tools without `--`, use an explicit relative/absolute path such as `./-name` where appropriate.

# 3. Output redirection

In Bash:

```bash
command > file
```

creates the file or truncates an existing regular file.

For overwrite-sensitive work consider:

```bash
set -o noclobber
```

and then use an explicit override only when intentional.

Do not pretend `noclobber` is universal shell behavior without checking the shell.

# 4. Temporary files

For important transforms prefer:
1. safe temporary file;
2. validate;
3. rename/replace.

Use `mktemp` where available.

Clean up with `trap` when the script may exit early.

# 5. `rm`

Before recursive deletion:
- print/inspect the resolved target;
- check variable is non-empty;
- confirm expected parent;
- avoid broad globs;
- use `--` where supported.

Do not normalize risky requests into `rm -rf "$var"` without proving `"$var"` is the intended target.

# 6. Copy/move

For uncertain overwrite behavior:
- preview destination;
- use interactive/no-clobber options when supported;
- or write to a new path and compare.

GNU/BSD options differ; label platform-specific flags.

# 7. Permissions

Avoid:

```bash
chmod -R 777 ...
```

as a generic fix.

Determine:
- required user/group;
- needed read/write/execute bits;
- whether directories/files need different modes;
- whether ACLs are involved.

Use least privilege.

# 8. `sudo`

Use only when the operation genuinely requires elevated privilege.

Explain the privileged scope.

Avoid running an entire shell/script with sudo when only one operation needs elevation.

# 9. Pipelines

Pipeline exit behavior differs by shell/options.

In Bash, `set -o pipefail` makes the pipeline status reflect a failing command rather than only the last command.

Use it intentionally.

# 10. `set -e`

Do not teach `set -e` as “automatic error handling.”

Its behavior has context-dependent exceptions.

For critical scripts:
- check important commands explicitly;
- use functions;
- return meaningful status;
- trap cleanup separately.

# 11. POSIX vs Bash

Portable shell:
```sh
#!/bin/sh
```

should not assume Bash features such as:
- arrays;
- `[[ ... ]]`;
- process substitution;
- `mapfile`;
- Bash-specific parameter expansions.

If using those, declare Bash explicitly:

```bash
#!/usr/bin/env bash
```

# 12. macOS / BSD vs GNU

Common differences can include:
- `sed -i`;
- `date`;
- `stat`;
- `find`;
- `xargs`;
- `grep`;
- `sort`.

Do not give GNU-only flags as though they work on stock macOS.

When exact behavior matters, check the target platform/version and show separate commands.
