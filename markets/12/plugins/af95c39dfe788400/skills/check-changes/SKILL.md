---
name: check-changes
description: Check the files changed in the current repository with VibeDoctor before a commit. Use when the user asks to check, review or validate their changes.
---

# Check changed files with VibeDoctor

1. List the changed files: `git status --porcelain` (staged and unstaged), skipping deleted files, lockfiles and binaries.
2. Read each file's full content. Send up to 50 files per call to `vibedoctor_check`, each with its repository-relative path. Pass `project` as the repository's `owner/name` from `git remote get-url origin`.
3. Report the findings grouped by file, most severe first, with line numbers and the suggested fix. Say plainly when nothing was found.
4. If the user says a finding is wrong, record why with `vibedoctor_note`. Only the user can dismiss a finding, in VibeDoctor.
