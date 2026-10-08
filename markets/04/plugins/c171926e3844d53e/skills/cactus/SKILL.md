---
name: cactus
description: Use when working with Cactus commercial real estate deals, property information, source verification, or underwriting questions.
---

# Cactus

Use the currently available Cactus tools as the authoritative source.

- Inspect the available tools and their descriptions at runtime.
- Do not assume a fixed set of tools or workflows.
- Prefer current Cactus data over model memory.
- Follow relevant `next_actions` returned by Cactus.
- Cite only evidence returned by Cactus.
- Never invent missing values or source locations.
- Use an available Cactus renderer when it improves clarity.
- Use `list_deals` with `limit: 20` when the user asks for a portfolio summary, KPIs, charts, tables, or a visual demo so its dashboard renders inline.
- Treat Cactus renderers as in-chat components. Do not open a browser or follow a Cactus URL unless the user explicitly asks to open the Cactus website.
- When the user asks to use another Cactus organization and `change_organization` is available, you MUST call it before giving instructions. Never replace the tool call with manual browser steps.
- After `change_organization` prompts reconnection, tell the user to choose **Connect Cactus**, select an organization, and approve access. Mention starting a fresh task only if browser approval finishes but the current task does not resume with the newly authorized organization.
- Never claim that an organization was changed until a subsequent Cactus response identifies the newly approved organization.
- Explain clearly when information or access is unavailable.
