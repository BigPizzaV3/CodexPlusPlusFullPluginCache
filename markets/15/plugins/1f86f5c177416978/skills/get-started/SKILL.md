---
name: get-started
description: Connect an EXZA Remote computer safely and check its live status in ChatGPT.
---
# EXZA Remote — first connection

EXZA Remote connects a ChatGPT user only to the computer they own or are explicitly authorized to administer.

1. Open https://remote.exza.de and sign in. Open registration requires email confirmation; no invitation code. Never ask for or collect user passwords, invitation codes, device secrets or email verification codes in chat.
2. Start the EXZA Remote Connection client on macOS, Windows or Linux using the system's terminal starter. Keep the EXZA terminal window open.
3. Enter the six-digit pairing code into the website and review the account email shown in the computer terminal; press **Y** once to approve or **N** once to deny (no Enter required in an interactive terminal). Enter alone never approves pairing. If the account is unfamiliar, deny pairing.
4. Complete the EXZA OAuth authorization and choose the correct computer.
5. Use EXZA Remote tools only for the authenticated device explicitly selected by its owner. Read and write capabilities require OAuth scopes; ChatGPT presents its native approval dialog according to the connected app permission settings; the terminal logs actions. A confirmation dialog cannot be forced by the MCP server. Never bypass consent or reveal private pairing secrets.
6. A listed capability is not proof that a specific device or account is authorized. If a tool is unavailable, disabled or needs new scopes, explain that rather than claiming a completed action. Never claim access to file operations, shell commands, application control, email send or payment checkout while they are locked. Do not suggest bypassing ChatGPT host confirmation or elevated OAuth. Do not ask a user to disable security controls.
7. If the device is offline, tell the user to start EXZA Remote Connection on that computer. Stopping or closing the EXZA terminal ends its connection.

For help: https://remote.exza.de/support.html or info@exza.de.

Users may remove computers from My Devices or permanently delete their EXZA account in Account settings. Account deletion requires the exact word DELETE, current password and browser confirmation, revokes device and OAuth access and ends EXZA Premium billing. Legally required invoices and third-party processor records may remain. Never bypass owner consent.

Permission policy: Initial OAuth grants computer:read only. External directory listings and write/device tools require separate computer:write OAuth consent. The plugin uses the native ChatGPT tool approval flow and the account-specific ChatGPT App permissions (Always ask, low-risk actions, etc.). ChatGPT alone controls whether an approval is shown and whether an Always allow option is eligible. EXZA must not fabricate confirmation, claim an unseen click or provide a fake native-looking window. OAuth scopes, selected device account, file sandbox, deny mode, local full-computer scope for commands, and system privacy rules remain independent barriers. The terminal shows redacted request and result logs, never an extra approval for authorized cloud tool calls. Do not call shell or mail tools without the user's specific request.

## Disconnect and reconnect
- Clicking **Disconnect** in My Devices completely closes the foreground EXZA Remote computer connection and local agent. It does **not** delete the saved device pairing.
- There is no automatic web Resume. To reconnect, the user must manually start EXZA Remote on that computer through the normal terminal installer/launcher; no new pairing PIN is required unless the device was permanently removed.
- **Remove** revokes the saved device pairing, and starting again requires a confirmed new pairing.

## External directory listings (RC36)
For an explicit request to list Downloads, Desktop, Documents or another directory
outside the EXZA workspace, call exza_list_external_folder directly with its exact
path. The server deliberately rejects such paths through exza_list_files, so a
read-scope-only tool can never silently elevate into computer:write. ChatGPT
controls the native approval prompt according to app settings. The additional
OAuth scope computer:write is required regardless of ChatGPT app setting.
The server returns at most 200 visible names/types in that single directory,
without contents or permanent home permission. User home root itself is blocked;
private and hidden paths are blocked, including symlink escapes.
If ChatGPT declines or blocks the action, no tool execution reaches EXZA.
The operating system may still require a one-time privacy permission.

## Safe Downloads folder creation (RC38)
If the user explicitly asks to create a new folder directly inside their Mac Downloads,
call **exza_create_downloads_folder** with only the desired folder name. Do not use
**exza_run_command** for that operation or ask for full-computer scope.
The tool requires computer:write OAuth and ChatGPT native app permission according
to user settings. Its action is limited to a single NEW visible folder directly
inside Downloads; existing folders, symlinks, absolute/relative paths, and hidden
names are rejected. Any macOS privacy permission still applies.

## Managed everyday operations (RC39)
For named Downloads/Desktop/Documents/Pictures/Music directories use exza_home_list, exza_home_mkdir,
exza_home_read_text, exza_home_write_text and exza_home_move instead of exza_run_command.
For an existing text file read first and provide the exact expectedSha256 to update it.
Open installed macOS applications with exza_desktop_launch and visible unsent email drafts with exza_email_draft.
Shell commands, long-running jobs and email sending remain powerful operations and require the active owner-approved terminal session, computer:write OAuth, and applicable ChatGPT permissions. ChatGPT's own permission UI is host-controlled.
Never assume its confirmation will always appear; explain scopes honestly.

## Everyday desktop toolkit (RC40)
Use dedicated exza_home_info, exza_home_copy, exza_home_search, exza_system_info, exza_process_list,
exza_browser_open, exza_clipboard_read and exza_clipboard_write.
Do not use exza_run_command as a shortcut for these ordinary tasks. Never assume the ChatGPT
native permission sheet will always appear; access is controlled by host app settings and OAuth.
Clipboard contents can be sensitive: read only when explicitly requested.
Browser opening is a side effect. For arbitrary shell access and email sending, retain
an active owner-approved terminal session. Linux requires appropriate desktop commands
(xdg-open, wl-clipboard/xclip, gio); Windows PowerShell and Explorer must be installed.

## Recoverable deletion (RC41)
For deleting files/folders under a managed Downloads, Desktop, Documents, Pictures or Music
path, call exza_home_trash with the exact area and relative path. NEVER use exza_run_command
for a simple deletion, and do not ask the user to enable full-computer scope for it.
exza_home_trash moves one existing item to a private EXZA recycle bin and returns recycleId.
Use exza_home_trash_list to inspect records and exza_home_restore with recycleId to restore.
Permanent deletion is intentionally not exposed. Users may have to approve each tool in
ChatGPT, depending on their ChatGPT permission setting; an app cannot force host popups.

## Owner-confirmed computer access (RC48)
The user physically presses Y once in the visible EXZA Terminal to approve the verified account/device and computer control for this terminal session, or N to deny. The first pairing also requires the six-digit PIN in My Devices. Previously paired computers keep their saved pairing identity but need a new physical Y/N each time the client is started. No second Y, scope computer, or confirm computer step is valid. The grant ends when the terminal closes or the user disconnects; scope workspace revokes computer control immediately. OAuth, ChatGPT tool permissions, and OS privacy settings still apply.

## RC43 interactive jobs / multiple text reads
Use exza_process_start to create an interactive job ONLY after owner-enabled local computer scope.
Use exza_process_output (offset optional) to read live output and exza_process_input to send
text into that exact process session. Use exza_process_sessions and exza_process_stop to
inspect/stop EXZA-owned sessions. Never use these tools to avoid the owner permission gate.
Use exza_home_read_multiple_text for 1-8 text files in the same managed home area.
The native ChatGPT Allow Once / Always Allow UI is controlled by ChatGPT, not the plugin.
Mac Mail sending remains subject to its existing local authorization requirement.

## RC48 email permissions
Mac email sending via exza_email_send requires the active owner-approved computer session, computer:write OAuth, applicable ChatGPT tool authorization, and macOS Mail automation permissions. Only send a message when the user explicitly requests the exact recipient and contents. Email preview never sends. Do not promise delivery.
