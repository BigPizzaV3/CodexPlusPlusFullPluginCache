# Wandeo

Create and edit videos on a local desktop with the bundled skills. Supported
targets are macOS Apple Silicon, macOS Intel and Windows x64. The host needs
local command execution and file/image access. No model API key is required.

Use `scripts/wandeo.sh` on macOS, or run
`powershell -NoProfile -File scripts/wandeo.ps1` on Windows. These launchers
prepare Node.js when needed. Run the launcher with `setup` first, then `--help`
for available commands. Setup downloads pinned rendering dependencies into
the user's cache; add `--with-asr` to prepare offline transcription too.

The sidebar connects to the HTTP MCP URL in the plugin configuration. Its server
and UI are deployed separately by the publisher; this plugin ZIP contains the
desktop video runtime and skills. Development packages use a localhost URL and
require a separately started Wandeo HTTP service.

Keep production projects and generated files outside this installed plugin.
`skills/` contains the editing, recording, setup and explanation workflows.
`third_party/anatomy/` contains the kit, authoring references, editable example
sources and capture/audit tools those workflows use. Pre-rendered example PDFs
and HTML pages are omitted except for the turning-dial page used at runtime.
Build new example pages in a writable project directory when needed.

CLI file references are relative to the explicit `--project` directory. Resolve
returned files against that directory before opening them or passing them to a
subsequent `--input`. Runtime/task internals and raw media tags are omitted from
normal results; selected source content and transcripts remain available for editing.

Website: https://sider.ai
Support: https://sider.ai/contact
Privacy: https://demopilot.chatgptapps.sider.ai/privacy
Terms: https://sider.ai/policies/terms

Wandeo includes AGPLv3 code and third-party components. See `LICENSE.md`,
`THIRD_PARTY_NOTICES.md` and `SOURCE.txt`. The separate corresponding-source ZIP
contains the development project and is supplied alongside the runtime ZIP.
