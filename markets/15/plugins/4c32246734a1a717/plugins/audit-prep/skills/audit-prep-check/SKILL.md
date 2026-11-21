---
name: audit-prep-check
description: Use before an ISO 27001 internal audit, Stage 1 or Stage 2 audit, or before signing an SoA, risk entry, NC or OFI register, policy or other record an auditor will read. Runs the audit-prep reviewer, which has ISMS Copilot challenge the findings and returns a verified change list. Beta.
license: MIT
compatibility: Claude Code with file access to the ISMS documents and an ISMS Copilot personal access token in ISMSCOPILOT_TOKEN.
---

When the human asks to prepare an ISO 27001 audit or to check records before an auditor reads them:

1. Ask once, if it is not clear: which documents or area to review, and the audit type and date.
2. Run the audit-prep subagent. In its task, give the area to review and the review date (the date the human gave, else today).
3. Give the human its answer as it is, including any limit line at the top, the "Not checked" section and the credit line. Do not edit files unless the human asks you to apply specific changes.
