# Adaptyv Bio

This OpenAI-authored plugin uses Adaptyv Bio's hosted MCP server to prepare, estimate, submit, and monitor protein experiments while keeping privacy, cost, and real-world actions visible to the user.

## Capability surface

- Discover available targets and inspect experiments, updates, quotes, invoices, sequences, and results.
- Estimate experiment cost without creating an experiment.
- Prepare and create a reviewable Draft after explicit user approval.
- Submit a Draft for Adaptyv review, confirm a quote to create an unpaid invoice, and settle an invoice only through separate approval-gated steps.
- Track experiment lifecycle, updates, and returned results without inventing missing measurements or completion state.

The live MCP tool schema is authoritative. The documented experiment types currently include affinity, screening, thermostability, fluorescence, expression, epitope binning, and enzyme activity; availability and required fields must be checked at runtime.

## Runtime and authentication

The packaged connector targets the production streamable HTTP endpoint at `https://mcp.adaptyvbio.com/mcp/`. The trailing slash is intentional and required by Adaptyv's OAuth resource configuration.

Authentication is configured at runtime through the MCP client using Adaptyv OAuth or an API token. Never add credentials to this repository, paste tokens into prompts, or persist them in skill files.

Adaptyv also documents an isolated testing endpoint at `https://mcp.testing.adaptyvbio.com/mcp/` with separate accounts and tokens. Use it only when a user explicitly requests sandbox testing and has configured sandbox credentials; the packaged production endpoint is never silently replaced.

## Safety and real-world actions

Protein sequences, custom-target details, sample metadata, and experiment parameters may be confidential and are sent to an external service when a tool is called. The skills require a disclosure summary and explicit confirmation before transmitting proprietary or undisclosed material.

Cost estimation is read-only with respect to experiment creation. Creating a Draft writes external state but does not submit the experiment. Draft submission, quote confirmation, and invoice settlement are distinct actions with separate user approvals. The plugin does not enable `skip_draft` or automatic quote acceptance, and it does not treat a quote confirmation as payment.

No real experiment is submitted during plugin validation. Source and installed-copy checks validate packaging, configuration, and instruction quality only.

## Official references

- [Adaptyv Bio API](https://www.adaptyvbio.com/api)
- [MCP server](https://docs.adaptyvbio.com/api-reference/mcp-server)
- [API introduction](https://docs.adaptyvbio.com/api-reference/api-introduction)
- [Create experiment](https://docs.adaptyvbio.com/api-reference/experiments/create-experiment)
