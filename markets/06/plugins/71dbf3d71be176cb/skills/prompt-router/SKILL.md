---
name: prompt-router
description: Route prompt requests into drafting, refinement, evaluation, or safety review.
---

# Prompt Router

Use for any request to create, rewrite, troubleshoot, or assess an AI prompt.

1. Identify the intended model or platform if it materially changes syntax or capability; otherwise make a portable draft and label assumptions.
2. Determine the task, audience, input context, required output, constraints, examples, and what success looks like. Ask only for details that materially affect the result.
3. Route to `prompt-design`, `prompt-refinement`, `prompt-evaluation`, or `prompt-safety` as appropriate; combine only when the request needs more than one.
4. State what the prompt can and cannot enforce. Do not imply a prompt alone adds tools, permissions, memory, privacy, or deterministic guarantees.

Output the requested prompt first, followed by brief assumptions or usage notes only when useful.
