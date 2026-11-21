---
name: mandate-light-walk-journey
description: Explore a user journey against a public Mandate Light project.
---

Use the selected public project's attached app context and its selected standards. Draft rules guide the work; they do not approve product scope. If it is absent, ask the user to open the project and use Project details → Use in chat. Reuse the panel; there is no server-held project reader.

Walk one real example from trigger to outcome. Identify the actor, the main steps, visibility, exceptions and what success means. Compare with approved requirements and identify material unanswered choices. Ask the most useful missing question rather than presenting a questionnaire. Keep the explanation in the chat.

When the user asks to save agreed behaviour, use propose_decision with the attached projectId and publicWorkspaceId. For a structured journey include design.schemaVersion=1 and design.stages with each stage's title, meaning, actor, trigger, exceptions and acceptance outcomes where agreed; IDs are assigned by Mandate. Use design.acceptance for overall measurable outcomes and negativeCase for what must not happen. Do not invent outcomes to fill the structure. Existing approvals remain authoritative; suggested stages or outcomes do not become approved merely by appearing in a journey. Confirm application from the browser receipt or refreshed context, not the prepared tool result. Do not claim a disk save. Keep Light's existing Save project/Open project route.
