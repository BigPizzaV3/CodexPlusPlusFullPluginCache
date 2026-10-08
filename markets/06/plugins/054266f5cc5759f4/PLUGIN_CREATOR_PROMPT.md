# Plugin Creator Prompt — Unix Copilot

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `unix-copilot`
- Skill: `unix-copilot`
- Display name: `Unix Copilot`
- Version: `0.1.0`
- Category: `Developer Tools`

## Architecture
Keep v0.1 skills-only.

Do **not** add:
- MCP;
- terminal execution;
- filesystem access;
- authentication;
- package installation;
- process control;
- system administration actions;
- custom UI.

The skill should generate and review commands/scripts only.

## Required behavior
Preserve the existing safety-first workflow:
- use the user's OS, shell, paths, output, script, and errors as source of truth;
- never claim to execute commands or inspect a machine without actual tool results;
- prefer portable POSIX-style solutions when practical;
- clearly label Bash, zsh, GNU, BSD/macOS, and Linux-specific behavior;
- classify risky file/system commands and provide preview/dry-run first;
- keep destructive execution separate from the preview;
- quote paths and variables safely;
- avoid unsafe parsing of filenames and leading-dash option confusion;
- avoid broad `chmod -R 777`, unverified `rm -rf`, and blind `curl | sh`;
- treat CSV as structured data and use CSV-aware parsers when quoted/multiline fields matter;
- never embed real credentials or secrets;
- verify current primary docs when shell/OS/utility/package behavior is version-sensitive.

## Preserve
- `SKILL.md`
- all reference files
- `agents/openai.yaml`
- branding
- listing material
- five positive and three negative tests

## Validate
1. ZIP root and `plugin.json`.
2. `skills: "./skills/"`.
3. Skill frontmatter.
4. Combined plugin/skill identity <= 64 characters.
5. `agents/openai.yaml`.
6. Asset paths remain inside package and do not use `..`.
7. Branding assets are valid and square.
8. Public listing field limits.
9. Starter prompts.
10. Submission tests.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
