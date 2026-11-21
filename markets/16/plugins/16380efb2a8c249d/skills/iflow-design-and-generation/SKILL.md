---
name: iflow-design-and-generation
description: Use when a user wants to design SAP Cloud Integration (CPI) integration flows, choose sender and receiver adapters, configure process steps, or generate a design-time iFlow ZIP using an existing exported template.
---

# SAP Cloud Integration iFlow design workflow

Developer: Rameshkumar Varanganti (https://agenticintegrationhub.com/).

1. Gather package ID, flow ID and display name, sender trigger/adapter, receiver adapter, endpoint/auth alias, message pattern, mappings, routers, retry and error handling, and externalized parameters. Use sensible defaults when safe.
2. Offer reference-content discovery via https://api.sap.com/integrations/discoverintegrations. Do not claim a public catalog page automatically grants access to download complete SAP integration content.
3. Draft a clear flow with sender, main integration process, reusable local integration process where relevant, receiver and exception subprocess.
4. Explain that valid design-time ZIP files depend on the actual SAP-exported artifact format and BPMN metadata. Do not fabricate SAP compatibility or say a generated ZIP has been imported successfully without testing.
5. For the bundled generator code, direct the user to `resources/starter/README.md`; it is local Python source, not a hosted MCP connection. It can modify an exported ZIP template, but the full adapter/process generator is not yet implemented.
6. If file creation tools are available in the current conversation, help produce source files and validate archive structure. Do not claim this installed skills-only plugin exposes executable tools or a live MCP service.
7. Future phase: connect a real remote Streamable HTTP MCP endpoint, then add GitHub commits only with explicit authorization and suitable repository permissions.

Never request or place live credentials inside generated iFlow ZIPs; use secure aliases and externalized parameters.
