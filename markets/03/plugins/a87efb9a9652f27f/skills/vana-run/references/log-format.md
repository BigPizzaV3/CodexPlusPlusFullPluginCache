# Log format

Use one log file per day at `protocols/<slug>/log/<YYYY-MM-DD>.md`. Use the date as the H1. Give each entry an H2 with the time and the action name from the protocol.

Use the time when the work happened. Ask for the time only when it affects the protocol. Use the user's local time and include the timezone only when the user changes it during the run.

Derive every field from the protocol's `# Tracking & Review`. Use one bold-label bullet for each field. Keep the same labels and units across entries when the protocol compares them.

Record only the details that the protocol uses to determine progress or the next action. Preserve relevant context that the user reports in the closest matching field.

Keep one entry per report. Append new entries. A review reads the log without rewriting earlier entries.

For example, a writing protocol might define these fields:

```md
# 2026-08-07

## 09:00 First draft

- **Planned:** Outline the introduction and write 300 words
- **Done:** Finished the outline and wrote 340 words
- **Next:** Draft the first example
```
