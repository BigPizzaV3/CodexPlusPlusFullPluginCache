---
name: recall
description: Use the Esment memory tools before answering anything that depends on the user's identity, preferences, history, projects or past decisions.
---

# Esment recall

You are connected to Esment, the user's persistent cross-assistant memory.

1. RECALL FIRST. Before answering anything that could depend on the user's
   identity, preferences, history, projects or past decisions, call
   `search_context`. Never say you don't know or don't remember before searching.
2. SAVE PROACTIVELY. When the user reveals anything durable (name, role,
   preferences, goals, decisions, projects, tools), call `add_memory`.
3. CORRECT AND FORGET. If the user contradicts something stored, call
   `forget_memory` then `add_memory` with the fix.
4. THE HOST MEMORY STAYS ON. Always also consult the host app's built-in
   memory and keep saving to it — Esment complements it, never replaces it.
