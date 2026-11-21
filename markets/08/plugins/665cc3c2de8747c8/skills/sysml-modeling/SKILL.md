---
name: sysml-modeling
description: Draft, revise, validate, or show a SysML v2 model with the BusbySim MCP tools. Use for a request about SysML v2 syntax or a BusbySim diagram.
---

# SysML v2 modeling with BusbySim

1. Before drafting SysML v2 in this conversation, call `get_sysml_syntax_guide` and follow the supported syntax in its result.
2. Draft a complete model. Preserve the user's design intent and existing model content when revising it. Keep the text within the tool's 50,000-character input limit.
3. Call `validate_sysml_model` with the complete text. Repair every reported syntax error and repeat until `valid` is true. Explain any remaining error if a valid model cannot be produced.
4. If the user wants to see or explore the model, call `render_sysml_model` only after successful validation. Show the diagram and the returned BusbySim link when useful.
5. Describe validation accurately: the parser checks syntax, not undefined references, engineering meaning, safety, or certification. The public tools cannot read, modify, or delete a user's saved BusbySim projects.
