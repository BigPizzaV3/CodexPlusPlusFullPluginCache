---
name: heta-reference
description: Answer general questions about the Heta project, its documentation, installation, and how Compiler, API, and Simulator fit together. For syntax, model compilation, or local simulation, use the corresponding skill.
---

# Heta reference

Help users find accurate, concise information about the Heta project and its tools. Distinguish the Heta language from Heta Compiler (local CLI), Heta API (remote compilation service), this plugin's MCP connection to Heta API, and HetaSimulator.jl (numerical simulation). Heta API compilation does not run numerical simulations.

Start with the user's materials and the information bundled with this plugin. For syntax, use the `heta-language` references when available. Answer routine questions from those materials without opening a website just to repeat or cite them. Use the actual Compiler or API result for questions about a model that has been checked.

Consult the relevant official page when the available material does not answer the question, conflicts with observed behavior, or a current version, installation step, supported format, or API detail matters. These links are lookup destinations, not a requirement to browse for every question:

- [Heta project](https://hetalang.github.io/) for an overview and navigation.
- [Resources](https://hetalang.github.io/resources/) for the ecosystem, learning material, cheat sheet, and version compatibility.
- [Language specifications](https://hetalang.github.io/specifications/) for syntax and language concepts.
- [Heta compiler](https://hetalang.github.io/hetacompiler/) for installation, CLI use, and export formats.
- [Heta HOW-TO](https://hetalang.github.io/how-to/) for worked examples.
- [HetaSimulator.jl documentation](https://hetalang.github.io/HetaSimulator.jl/stable/) for the separate Julia simulation package and its usage.
- [Heta GitHub organization](https://github.com/hetalang/) for source repositories, issues, and release information.

When browsing is needed, use web search or page-opening tools available in the chat. Search within `hetalang.github.io` first for documentation; use the GitHub organization for repository-specific facts. Read the page before answering and cite the specific source. A link in this skill does not grant browsing access. If access is unavailable, say what could not be checked and answer only from available material.

For questions about the running remote compiler version, use MCP `getInfo` when available. For conceptual Heta syntax questions, use `heta-language`. For creating, fixing, validating, or exporting a specific model, use `heta-compiler` when a local `heta` executable and model files are accessible; otherwise use `heta-modeling-api` when the Heta API MCP `buildPlatform` tool is available. For local numerical simulation, use `heta-simulator` in Codex when Julia is available.
