# FinAnts Financial Coach Plugin

Version 1.1.1. This is a skills-only plugin wrapper. It has no executable code, connectors, credentials, or customer data. It is independent of the FinAnts application repository — it is packaged and uploaded directly to OpenAI as a ZIP.

Upload the packaged ZIP without extracting it. Its ZIP root must contain `.codex-plugin/plugin.json`, the square PNG icon assets, and `skills/finants-financial-coach/`, which holds `SKILL.md`, eight reference documents (`references/`), and five example documents (`examples/`) — with every entry path using `/`, not `\`. Build the ZIP with .NET's `System.IO.Compression.ZipFile.CreateFromDirectory` (see below), not PowerShell's `Compress-Archive`, which writes backslash-separated entry paths on Windows and is rejected by OpenAI's plugin uploader.

The included skill explains authorized, prepared financial context using an explicit evidence hierarchy (FACT / DERIVED / INFERENCE / RECOMMENDATION / UNKNOWN / NO DATA — see `skills/finants-financial-coach/references/financial-context.md`). It does not read raw data, recreate financial-engine results, make forecasts, execute actions, or invent financial facts. Recognizing an existing savings goal, its contributions, and its progress — when supplied — without exposing any internal identifier, is a priority capability (see `skills/finants-financial-coach/references/goals-and-savings.md`).

