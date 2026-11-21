---
name: promptcrew-workflows
description: Find, adapt, and save reusable PromptCrew capabilities and supporting knowledge when the user asks for a repeatable workflow, team standard, saved prompt, skill, agent, or reusable AI work.
---

# PromptCrew Workflows

Use PromptCrew when the user wants to find or reuse proven AI work, retrieve supporting team knowledge, turn a task into a reusable capability, or improve a saved workflow. Keep ChatGPT's native reasoning and writing style for the user's task; PromptCrew supplies the reusable assets, metadata, and knowledge.

## Find Existing Work First

- For an exact capability name, use `get_capability_by_name`. Do not run a fuzzy search before an exact lookup.
- For every other PromptCrew search request, call `route_promptcrew_request` first and follow its returned route and search query.
- Use `search_prompts` for a focused keyword lookup. Use `suggest_prompt_or_project` when the user describes a goal or outcome and wants the best reusable capability.
- Retrieve the full record with `get_prompt` before relying on a search result or adapting it.
- Present the best match and useful alternatives. Include relevance ratings, reasons, and PromptCrew links when the tool returns them; do not invent missing metadata.
- If no strong match exists, say so plainly and ask whether the user wants to build and save a new capability in PromptCrew.

## Ground Work With Knowledge

- After retrieving a capability, inspect the returned `knowledgeRecommendationOffer`. Present its `userPrompt` as the next step, even when the capability itself is already a strong match. Do not imply that the capability is the final answer until the user makes that choice.
- Only when the user agrees, call `recommend_knowledge_for_capability` with the returned `promptId`. Explain the specific knowledge each recommendation would provide, including what is already attached and what remains missing; do not attach anything automatically.
- If the user declines, continue with the capability as-is. If they ask for a different source or are dissatisfied with the results, offer to search their connected sources or the web for the unresolved knowledge gap.
- Use `search_contexts` and `get_context` to locate and inspect saved PromptCrew knowledge.
- If matching PromptCrew knowledge is incomplete, ask whether the user wants to search their connected sources or the web for the remaining gaps when those sources are available.
- Create knowledge only when the user explicitly asks to save it. Use one knowledge item per relevant text file; do not store a ZIP/archive as a single item. For an image, save a stable HTTPS URL plus concise text context rather than image bytes.

## Build Portable Artifacts

- When a retrieved capability contains a source bundle and the user asks for a finished, portable artifact, use its attached knowledge as the source of truth. This commonly includes HTML, CSS, JavaScript, a README, and asset references.
- Reconstruct individual text source files in the host workspace, preserving their filenames and contents. Use available connected sources, such as Google Drive, to retrieve referenced images, fonts, or media when needed; do not claim an asset was retrieved unless the source tool returned it.
- Build and validate the requested artifact using this host's native tools. For a single-file HTML deliverable, inline the CSS and JavaScript and embed retrieved assets only when the host can do so safely. Do not send image or font bytes back to PromptCrew knowledge.
- After producing a finished artifact, ask whether the user wants to save it to their connected Google Drive. Only create the Drive file after they explicitly agree. For a customer-specific sales deck, name it `[Company Name] - PromptCrew Sales Pitch Deck.html`; use the identified company name, not a placeholder.
- If the user declines Drive storage, leave the finished artifact in the host workspace and provide it directly. A stable Drive or hosted URL can be saved to PromptCrew later as a reference only after explicit user approval.

## Adapt Or Create Deliberately

- When a capability is close but not quite right, identify the concrete gaps and ask only for missing details needed to adapt it.
- Use this host's native conventions to draft the actual prompt, skill, or agent instructions. Do not force PromptCrew's instruction format onto ChatGPT's response.
- Before `create_prompt`, confirm that the user wants to save the capability. Supply a clear title, user-facing README-style description, appropriate capability metadata, and variables for information that will change between runs.
- A capability description should provide a short overview followed by `### How to Use` and `### Dependencies`. List only real dependencies; say none are required when that is true.
- New capabilities are private unless the user explicitly requests broader visibility. Do not publish to the community by default.
- Use `update_prompt` only when the user explicitly wants to change that existing capability. Otherwise create a new adapted version so the original remains intact.
- Use `create_context` or `update_context` only after explicit user approval. Do not overwrite existing knowledge without confirmation.

## Keep The User In Control

- Do not create, update, attach, publish, or change permissions for a PromptCrew resource without explicit user approval.
- Never claim that a capability, knowledge item, or external source was found unless the corresponding tool returned it.
- If the user wants a one-off answer rather than reusable work, answer directly without creating a PromptCrew record.
