# Research Notes — Unix Copilot

Research date: 2026-09-23

## Recommended name

Keep **Unix Copilot**.

It is short, clear, already consistent with the existing skill, and well inside OpenAI's 30-character public display-name limit.

Package: `unix-copilot`
Skill: `unix-copilot`

## Recommended architecture

Use a **skills-only plugin** for v0.1.

The current value is command translation, explanation, shell debugging, portability, data/file handling, and safety guidance. It does not need live terminal access.

A future MCP-backed version would only be appropriate if the product deliberately adds controlled actions such as:
- read-only system inspection;
- command execution inside a sandbox;
- package/version discovery;
- filesystem operations with explicit user authorization;
- process/service inspection.

Because terminal execution can have large side effects, a live-action version would need much stronger tool annotations, scope controls, authentication, approvals, sandboxing, and destructive-action review.

## Current OpenAI plugin requirements

Current public-directory validation includes:
- display name: max 30 characters;
- short description: max 30 characters;
- long description: max 4,000 characters;
- capabilities: max 20, each max 120 characters;
- starter prompts: max 3, each max 128 characters;
- skill frontmatter requires `name` and `description`;
- combined `plugin-name:skill-name`: max 64 characters;
- skills-only ZIP submissions do not need MCP configuration;
- bundled skills are scanned for safety/security;
- verified developer/business identity and policy attestations are required.

Sources:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## POSIX portability

POSIX.1-2024 remains the baseline for portable shell command-language behavior. It explicitly defines quoting, expansion, pathname expansion, and redirection semantics.

This supports the skill's existing rules:
- quote variables/paths when they represent one argument;
- do not confuse Bash/zsh extensions with POSIX `sh`;
- treat `>` as potentially truncating an existing file;
- distinguish shell parsing from utility-specific behavior.

Primary source:
https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html

## GNU deletion and filename handling

Current GNU Coreutils documentation keeps protective behavior such as `rm --preserve-root`, and GNU Findutils documents NUL-delimited `xargs -0`.

These features reinforce the skill's safety rules, but they are GNU-specific and must not be presented as universal stock-macOS behavior.

Sources:
- https://www.gnu.org/software/coreutils/manual/
- https://www.gnu.org/software/findutils/manual/

## macOS

Apple's current Terminal documentation states that zsh is the default shell for new Terminal sessions unless configured otherwise.

The plugin should still verify the actual user's shell because:
- `$SHELL` generally describes the login shell;
- a script may run under another interpreter;
- Bash/zsh/POSIX syntax differs.

Apple also documents that `>` redirects output to a file and `>>` appends, so overwrite/truncation risk remains an important safety concern.

Sources:
- https://support.apple.com/guide/terminal/change-the-default-shell-trml113/mac
- https://support.apple.com/guide/terminal/redirect-terminal-input-and-output-apd1dbe647b/mac

## ShellCheck

ShellCheck remains a useful static-analysis tool for `sh`/Bash-family scripts and identifies syntax, semantic, robustness, and portability issues.

The plugin may recommend it for validation but should never treat a clean ShellCheck run as proof that:
- runtime data is correct;
- permissions are correct;
- a destructive target is safe;
- a script behaves correctly on every target environment.

Source:
https://github.com/koalaman/shellcheck

## Core principles retained

1. Generate guidance only; never claim execution without tool/user output.
2. Prefer portable POSIX commands when practical, but label GNU/BSD/macOS/Bash/zsh differences.
3. Treat destructive, recursive, privileged, and system-state-changing commands as high risk.
4. Preview first, execute separately, validate afterward.
5. Quote paths and variables safely.
6. Handle leading-dash and unusual filenames.
7. Avoid parsing `ls`.
8. Do not use plain line tools as general CSV parsers.
9. Preserve raw input for important transforms.
10. Never embed production secrets in commands, scripts, examples, logs, or shell history.
