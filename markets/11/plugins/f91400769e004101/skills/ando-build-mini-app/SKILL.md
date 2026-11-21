---
name: ando-build-mini-app
description: Build or refine an Ando miniapp for a team workflow, such as triage, structured input, or a shared interactive view. Use to design, validate, and publish a miniapp to the intended audience.
---

# Build a mini app

Read [Ando basics](../../references/ando-basics.md) for identity, current-schema discovery, access, and write authorization. Discover only tools needed for this request.

Clarify the user task, intended audience, input data, primary action, and desired output. Reuse answers already given. Determine whether the user wants a draft, published release, installed instance, or a working interaction in a conversation; these are distinct outcomes.

Inspect current miniapp discovery, read, update, and publication schemas. Read existing apps and instances before deciding to create another. Reuse a suitable app or instance when it serves the task. Inspect command/instance contracts, revisions, permissions, and current supported rendering surfaces. Do not invent command names, unsupported fields, or a revision argument on a legacy command read that does not accept it.

For connected data, verify the actual account and grants independently of Ando identity. Use current app-tool discovery to obtain provider schemas before execution. Keep secrets in supported storage and respect the audience of source data. An app must not expose personal provider data to a broader group.

Build the smallest useful interaction with a clear primary action and visible loading, empty, error, and permission states. Follow [Ando's current miniapp guide](https://docs.ando.so/docs/ando-mcp/publish-miniapps) and supported contracts. Read-only queries must remain read-only. Controls that change Ando or a provider need supported authorization/confirmation behavior and clear consequences. Do not use decorative buttons or invented handlers as proof of functionality.

Validate the implementation using the available miniapp validation/preview path and representative permitted data. Verify meaningful actions against their persisted results. A mocked preview establishes presentation only. Handle stale revisions and denied access with an actionable recovery path.

Publish only within the user's authorized scope and intended audience. Verify the published revision, then installation and provider grants separately when requested. Read back the instance and test its intended interaction when authorized. Report which of draft, validated, published, installed, and verified working is actually complete, with links and remaining setup.

See [optional capabilities](../../references/optional-capabilities.md). For provider alert feeds use [Set up an alert channel](../ando-alert-channel/SKILL.md); for ongoing agent execution use [Set up a looped channel](../ando-looped-channel/SKILL.md). A published miniapp alone creates neither.
