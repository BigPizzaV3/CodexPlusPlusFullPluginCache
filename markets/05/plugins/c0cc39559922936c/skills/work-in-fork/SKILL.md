---
name: work-in-fork
description: Use when a user asks to inspect, change, or test a website or code in a Fork sandbox connected to their account.
---

# Work in Fork

Use Fork's MCP tools only for a user-requested task in a sandbox the connected account can access.

1. Call `fork_list_sandboxes` when the sandbox has not been identified. If several match, ask which one the user means. If none are available, explain that the user needs a Fork account with sandbox access.
2. For an existing file, call `fork_read_file` before changing it. Use its SHA-256 with `fork_edit_file` for a small exact replacement. Use `fork_write_file` for a new file or a necessary full replacement. If a read is redacted, use an exact edit so hidden values are preserved.
3. After an edit, read the affected file again. For a website change, use the `fork_preview_*` tools to inspect the rendered result when a preview is available. Report what was verified and any remaining uncertainty.
4. Keep results focused on the selected sandbox and the user's request. Do not request or reveal environment files, credentials, tokens, or other secret values. Do not claim access to the user's local computer or to sandboxes the connected account cannot control.

Fork may ask the user to sign in or approve an additional OAuth scope before a tool can run. Let that authorization flow complete rather than requesting a password or token in chat.
