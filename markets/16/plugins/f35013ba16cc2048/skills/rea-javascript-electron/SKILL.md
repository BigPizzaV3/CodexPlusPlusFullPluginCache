---
name: rea-javascript-electron
description: Analyze an authorized JavaScript/Electron app directory or ASAR, map modules and process boundaries, or trace a requested feature through source and runtime evidence.
---

# JavaScript and Electron investigations

For a supplied app directory or ASAR, route to REA's advertised `analyze_javascript_application` capability. Static analysis needs Node.js/npm, but no native disassembler. If this tool is missing, offer the documented CLI route without claiming it was run.

1. Identify the app build/version, exact input path, and one feature/question (for example, where search is handled).
2. Start with the module/import and process-boundary overview, then trace from the user-visible entry point through relevant renderer, preload/IPC, main-process, and native-addon relationships.
3. Inspect source maps, routes, package metadata, and configuration when they affect the question; filenames and string matches are leads, not proof.
4. If comparing two versions, state how each artifact was identified and distinguish observed code differences from inferred behavioral impact.
5. Use a runtime/browser/Electron capture only when static evidence cannot resolve the named uncertainty and the user has authorized that exact target/flow. Keep the path and interaction narrow.

Describe whether evidence is static or runtime. A reconstructed implementation is a new design choice, not evidence that the original used the same architecture. Never copy proprietary code into a new product or bypass third-party access controls.
