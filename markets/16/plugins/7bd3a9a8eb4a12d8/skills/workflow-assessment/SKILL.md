---
name: workflow-assessment
description: Assess an existing workflow, map its human decision points and bottlenecks, and evaluate where the public Hashmedo capabilities fit.
---

Check what the user is asking for before any tool call:

- If they ask you to approve, pay, write records, bypass review or run a live workflow, make no tool calls. Explain that the plugin provides assessments and offer to map the process. Wait for them to request an assessment before starting one.
- If they ask you to send workflow data or Mermaid to Hashmedo, make no tool calls. Explain that the chat can show a native visual and the optional viewer can render Mermaid pasted locally. If they later ask to open the viewer, call it with `{}`.
- If they request an assessment without a workflow, make no tool calls. Ask for a short, redacted description with a trigger, main steps and any known decision owner. A fictional example is sufficient.

Use the workflow already in the conversation. Avoid requesting credentials, payment data, protected health information, government identifiers or personal records.

For an assessment with sufficient detail, call `open_hashmedo_mermaid_viewer` once with `{}` for the public catalog and optional branded viewer. Keep workflow text, identifiers, decision data, findings, Mermaid and SVG out of external calls. If the catalog is unavailable, give the workflow assessment and leave Hashmedo fit unverified.

- **Current flow** — Use a native in-chat diagram when supported. Include only the described trigger, roles, decisions, rework and outcomes. Mark unknown coverage, timeouts and next steps as unknown. A Hashmedo heading is a brand label. Show a Hashmedo step in the current flow only if the user says it is already in use. Use a simple step list if the host cannot render a diagram.
- **Human checkpoints** — Identify who decides, what evidence they need, what they can choose and what happens next. Call out missing ownership or escalation as open questions.
- **Bottleneck and change** — Tie the likely bottleneck to observed evidence or label it as a hypothesis. Propose one or two concrete changes, an owner or role and a measure for validating the improvement. Avoid estimating savings without data.
- **Hashmedo fit** — Give a fit, partial fit or no-fit judgment with reasons. The catalog supports sending human decision requests, receiving and recording answers, and retrieving the recorded answer. Source systems, business rules and downstream actions remain with the workflow owner. Describe the agent key and object grants required for a live integration. Cite the public source links from the catalog.
- **Limits and assumptions** — State material gaps. Keep current state separate from proposed changes.

Use a Hashmedo label on the native visual where the host supports it. When helpful, provide the same flow as copyable Mermaid for the optional viewer. The viewer renders on user paste. Keep the assessment readable in the conversation without requiring the viewer or an account.
