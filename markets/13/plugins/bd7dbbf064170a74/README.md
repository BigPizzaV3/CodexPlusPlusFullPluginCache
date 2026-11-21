# Heta Assistant

Author: Evgeny Metelkin.

A plugin for Heta guidance and simple models in Chat and Codex. Models are validated with the local Heta Compiler when available, or through the Heta API MCP server when its tools are available. Codex can also run local HetaSimulator.jl simulations with Julia.

`plugin.json` defines the plugin, `mcp.json` connects the Heta API server, and `skills/` contains reference, language, local Compiler, API, and local simulation workflows. See the [Heta project](https://hetalang.github.io/) for documentation.
