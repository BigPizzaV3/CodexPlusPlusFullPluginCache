---
name: scenario-composition
description: Compose provider-aware Nebula AI scenarios from user goals, inspect available cards and resources, validate the graph, and create a project only after explicit approval.
---

# Nebula AI scenario composition

Use Nebula AI tools when a user wants to design or create a content-production workflow.

1. Discover current capabilities before selecting cards, modes, providers, models, ports, or limits.
2. Resolve user-owned resources only when the request needs them; never invent resource identifiers.
3. Build a draft from the user's goal and constraints. Treat returned warnings and missing inputs as authoritative.
4. Validate the complete draft before proposing creation.
5. Explain the proposed cards, connections, model choices, required user inputs, and unresolved constraints.
6. Call the project-creation tool only after the user explicitly asks to create or confirms the presented draft.

Do not claim unsupported capabilities, bypass ownership checks, or activate/run/publish a newly created project. Project creation is intentionally non-destructive and produces an inactive project.
