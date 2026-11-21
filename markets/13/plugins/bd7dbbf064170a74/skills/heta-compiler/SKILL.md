---
name: heta-compiler
description: Check, compile, or export a Heta model with the locally installed Heta Compiler in Codex. Use for project files, local diagnostics, and requested output formats; use heta-language for syntax guidance.
---

# Local Heta Compiler

Use the local `heta` CLI to validate or export Heta model sources in Codex. Read [the Compiler reference](references/heta-compiler.md) for the installed environment, platform declarations, validation without export, and requested conversions. Consult the shared `heta-language` skill and its references when syntax, units, events, tables, or modules matter.

1. Inspect the user's source files, entry module, includes, and existing platform declaration. Preserve project structure and unrelated code. For a new model, prefer `.heta` unless another source format is requested.
2. Check `heta --version` and installed help. Use the available version; investigate a concrete incompatibility before changing version requirements. If the executable is unavailable, use the Heta API MCP `buildPlatform` tool through `heta-modeling-api` when it is available. If neither compiler is accessible, continue useful static work and explain what remains unverified.
3. Validate a new or revised model with the available compiler before calling it valid. For an existing platform, check its configured entry point and declaration, with exports disabled unless requested. Inspect exit status, errors, and meaningful warnings.
4. For a broken model, explain the relevant diagnostics, make a focused correction, and rebuild when possible. For an export request, use the requested format, verify the generated files, and give their locations.

Compilation checks model structure and expressions; it does not run simulations or establish biological or numerical equivalence. Report which compiler checked the model and any validation that could not be completed. When using the remote API for local files, tell the user that their source files will be sent to Heta API before invoking `buildPlatform`.
