---
name: token-tally-setup
description: Get Token Tally ready to create your card. Checks your computer and helps set up the drawing tool if needed; no extra plugin is required.
---

# Set up Token Tally

Token Tally uses the Tesseract graphics CLI (`tsrct`, not the OCR package) to render PNG cards on the execution host. Installing the plugin does not itself install this CLI. For a card request, complete necessary setup within that workflow; do not turn it into a separate user task.

1. Check Python 3.10+, the signed-in Codex CLI, bundled Inter Display font files (or installed SF Pro Display fonts), and Tesseract CLI 0.3.1. Do not fetch account usage during setup alone or read credentials.
2. Use the main helper’s renderer discovery, including the dedicated Token Tally runtime, default install paths, PATH, and any user-supplied renderer path. Run `--version` and reuse a matching renderer. Defaults: macOS `~/Library/Application Support/Tesseract/bin/tsrct`; Linux `${XDG_DATA_HOME:-$HOME/.local/share}/Tesseract/bin/tsrct`; Windows `%LOCALAPPDATA%\Tesseract\bin\tsrct.cmd`.
3. If missing or mismatched during a card or setup request, briefly state that you are preparing the required renderer and proceed with routine setup. Do not ask an extra conversational permission question or offer manual steps by default. Use normal host network/filesystem approvals and honor user restrictions; never bypass system protections. If declined or blocked, retain any existing stats snapshot and report the actual blocker.
4. Follow [Install Tesseract](references/install-tesseract.md). Check the installed CLI version. Do not mark setup complete on download alone.
5. Run the main helper's `doctor --tsrct <absolute-path>` command. Fonts ship in `../token-tally/assets/fonts/` with their open license. Installed SF Pro Display fonts are used when available; otherwise the renderer automatically uses bundled Inter Display. Do not download proprietary fonts. Report missing bundle files as an incomplete plugin install. The complete workflow has only been tested on macOS; do not promise support on other hosts without testing.
6. Resume an existing card request using the resolved absolute renderer/font paths and a new output directory. If a snapshot was already saved, re-render it rather than retrieving stats again. Inspect the PNG. If the user requested setup only, report the checked paths and remaining blockers without collecting personal stats.

Keep downloads outside the installed plugin cache. On macOS, use the dedicated Token Tally prefix described in the installation reference to preserve any existing Tesseract version. Do not modify unrelated packages. On other hosts, explain if the official installer will switch the active Tesseract command before proceeding through normal host approvals.
