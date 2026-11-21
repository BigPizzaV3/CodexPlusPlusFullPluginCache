# Authoring API usage

Read this reference when a supported, independently authorized code client can reduce model-visible
data or combine calls. Use the connected MCP tools for ordinary interactive work. This reference
supplies no credentials or client executable.

## Confirm access and selection

Use the API base URL configured for the connected Agentplace environment. Do not infer production
from a business website URL or change environments to work around an error. The API base ends in
`/api/authoring/v1`. The client's supported OAuth flow authorizes the same environment's authoring
resource. Its credential store supplies authentication to requests; keep credentials out of tool
arguments, printed output and generated app source. MCP linking alone does not establish this client.

Keep the discovered project, selected role and existing session. Encode each URL path component.
The role key is `builtin` or `configured:<roleId>`, using the actual returned role ID. The selected
session prefix is:

```text
{apiBase}/projects/{projectId}/roles/{roleKey}/sessions/{sessionId}
```

Open or refresh that session's guidance with `GET {sessionPrefix}/context`. Read the required-entry
and relevant specialist skills using their returned paths. API and MCP share this guidance and
source; changing transports is not a reason to create a new session or reload unchanged guides.

## Read and reduce data

The existing file-read operation is `POST {sessionPrefix}/files/read`. Its JSON body uses the same
`paths` and optional `viewRanges` business fields as the corresponding MCP read. Selection comes
from the URL. For example, a selected batch of paths goes in `{"paths": [...]}`. Obtain paths and
current schemas from authorized discovery; do not derive API routes from tool-name spelling.

Check HTTP status and the operation outcome. A domain success has `ok: true` and `data`; a domain
refusal has `ok: false` and `error`. Authentication and ingress failures can have a different error
shape. On a successful file read, inspect each `data.files` entry for a per-file error and incomplete
range before using its content. Consume the structured file entries; each body is returned once.

For a mechanical task, code can collect independent pages or read batches, compare digests and
return only changed paths, relevant excerpts, counts and per-item errors. Preserve coverage,
continuation and truncation information so the model can distinguish absence from an incomplete
search. For implementation, return the exact skill or file text the model needs to understand or
edit. Do not print every intermediate JSON response.

Use existing batch inputs and pagination bounds. Parallelize independent reads only. Keep dependent
edits, commands, builds and paid operations in their required order. API calls are not automatically
faster than an existing MCP batch.

## Interpret outcomes before choosing another route

Use current action definitions and results for permissions, mutation inputs and recovery. An HTTP
endpoint does not supply an action missing from the selected role. Firecrawl and Media operations
must be discovered as available before use; a planned capability is not an exposed endpoint.

After an uncertain mutation, preserve its original selection and any operation-specific retry key.
Inspect the effect through the owning operation before repeating it. A client timeout or changed
transport proves neither failure nor cancellation. Commands and paid calls may run again if repeated.
If API access is unavailable before dispatch, continue the supported task through MCP.


## Repository developer example

The Agentplace repository includes `packages/server/scripts/authoring-api/read-project.ts` and a
thin typed client. From `packages/server`, Node 24 runs it with the authoring resource URL, project
ID, existing session ID and required file paths. It starts its own OAuth/PKCE authorization and
keeps credentials in process. It emits the selected context and exact requested files. Set
`AUTHORING_BASELINE_FILE` to a prior successful read envelope to omit bodies whose digest kind,
range and digest all match; errors and incomparable observations stay visible. Read the emitted
guidance and fetch required and relevant specialist skills before authoring.

This example needs repository dependencies and a reachable callback. It is not installed as a
command by this plugin. Without that supported environment, continue through MCP.
