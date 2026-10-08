# Unix Installation and Environment Reference

## Purpose

Use this file for package installation, environment checks, shell selection, and common Linux/macOS differences.

Verify current package names and commands when they matter.

# 1. Identify the environment

Useful checks:

```bash
uname -s
uname -m
```

On Linux:

```bash
cat /etc/os-release
```

Shell:

```bash
printf '%s\n' "$SHELL"
```

Note: `$SHELL` is the login shell and does not always prove which shell is executing the current script.

# 2. Debian / Ubuntu

Typical package management:

```bash
sudo apt update
sudo apt install <package>
```

Do not combine unrelated system upgrades with a simple install unless needed.

# 3. Fedora / RHEL-family

Typical:

```bash
sudo dnf install <package>
```

Exact repository/package availability can vary.

# 4. Arch Linux

Typical:

```bash
sudo pacman -S <package>
```

Follow current Arch guidance when repository state or upgrades matter.

# 5. macOS

Homebrew is common for third-party Unix tools:

```bash
brew install <formula>
```

Do not assume GNU utilities replace stock BSD/macOS utilities under the same names.

Homebrew often installs GNU variants with prefixed names or separate PATH instructions.

# 6. Python CLI applications

For standalone Python command-line applications, `pipx` can provide isolated environments:

```bash
pipx install <package>
```

Use project virtual environments for project dependencies.

Avoid `sudo pip`.

# 7. Command availability

Before recommending installation, check whether the tool may already exist:

```bash
command -v toolname
```

# 8. Versions

When behavior depends on version:

```bash
toolname --version
```

or use the tool’s documented version command.

Do not assume package-manager version and runtime version are equivalent.

# 9. GNU tools on macOS

When a workflow genuinely requires GNU-specific behavior, say so explicitly and either:
- provide a BSD/macOS alternative; or
- explain the GNU package requirement.

Do not force installation merely for convenience when a portable command is reasonable.

# 10. Environment changes

For PATH, shell startup files, aliases, or environment variables:
- state which file/shell is affected;
- avoid duplicate entries;
- preserve existing config;
- explain whether a new shell/session is required.

Never ask users to paste secrets into shell startup files unless that storage model is explicitly appropriate and secure.
