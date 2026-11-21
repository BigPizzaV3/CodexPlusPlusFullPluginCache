---
name: heta-modeling-api
description: Create, build, check, repair, or export a specific Heta model through the Heta API MCP server when a local Compiler is unavailable or model files are not accessible. Use even when the user only asks to create a model and does not explicitly request compilation. Use heta-language for conceptual syntax questions.
---

# Heta modeling through API

Help users build small Heta models and diagnose compiler errors with Heta API. Start with the user's files, the shared `heta-language` references when available, and actual compiler diagnostics. Consult the [Heta language specifications](https://hetalang.github.io/specifications/) only when those materials leave a syntax detail unresolved or version dependent.

- Keep new models small and aligned with the user's request. Ask for missing details when needed, and include every source file needed for compilation.
- Use MCP `buildPlatform` to compile every model you create or revise before presenting it as valid. Do this for requests such as "build me a model" even when validation is not separately requested. Also use it when the user asks to check, compile, or convert a model. Request exports only when an output format is wanted. Follow the tool's current schema for parameters, formats, and options. If `buildPlatform` is unavailable, check whether a local `heta` executable and the model files are accessible; otherwise state clearly that compilation could not be performed and why. Do not suggest installing the local CLI when the API is available.
- For a broken model, compile the supplied files, identify the relevant diagnostics, explain the cause, and show a focused correction. Preserve unrelated code. Recompile the correction when possible; after three unsuccessful repair attempts, report the remaining diagnostics.
- After each build, show the returned raw logs without editing them in a fenced text block, followed by a short conclusion. Explain fixes separately. Never invent compiler output or claim that uncompiled code was validated.
- Provide returned file or download links when available. Generated files and links are temporary; mention expiry when relevant.
- For conversion, clarify the desired format if needed, build with that export request, and provide the generated content or returned download link.

The MCP server offers `getInfo` for its Compiler version and `buildPlatform` for validation and export. It does not run numerical simulations. If simulation is requested, explain what can be prepared or exported without claiming simulation results.
