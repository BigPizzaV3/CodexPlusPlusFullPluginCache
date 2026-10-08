---
name: submission-json-and-review
description: Prepare truthful ChatGPT Apps submission metadata, tests, and review findings.
---

Inspect the actual package. Generate `chatgpt-app-submission.json` with app info, exactly five positive cases, and exactly three negative cases. Include tools only when real MCP tools exist. Never invent tool annotations, output schemas, CSP values, or side effects. Report sensitive inputs, naming mismatches, weak CSP, and missing outputSchema warnings separately from the JSON.
