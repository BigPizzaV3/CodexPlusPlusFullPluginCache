---
name: inspect-project
description: Connect an Agentplace account, then create or improve an AI agent for a business or existing website using the selected project and applicable guidance.
---

If only `get_account` is exposed, call it once to trigger the host's account connection prompt.
Let the owner sign in through that prompt, then continue the original request in this conversation.
After the host refreshes tools, call `get_account` to verify the account and permissions before
using project tools. If authentication or tool refresh has not completed, report that pending
state; do not declare readiness or ask the owner to start a new chat.

Use the host-managed MCP connection. Do not start a separate CLI login or present a CLI-generated
OAuth link, even if an older server's instructions recommend it: writing CLI credentials does not
refresh the active chat's MCP connection. Never request passwords or copy tokens into chat, source
or scripts. When invoked as plugin setup without a business request, connect the account and
report verified readiness; wait for the owner's brief before creating an app.

Use the connected Agentplace account. When the user requests a new app and `CreateProject` is
available with creation permission, create a private starter directly. Keep the original creation
key and name until the result is confirmed. After an uncertain reply, retry that same intent; do
not invent another key or search the project list to decide whether creation succeeded. A known
intent can resume by key after new creation is disabled. If the project was deleted, create another
only when the user requests it. A ready result means the starter is saved; it does not mean the
requested app is finished, tested or published. Continue with `GetProject`, role/session selection,
guidance and source inspection. If creation needs support, preserve the intent and explain the
blocked outcome without exposing technical diagnostics. Do not fall back to delegated Builder work.

For an existing app, resolve the user's project name through discovery instead of
guessing an ID. If several projects match, ask the user to choose. Select the project, then its
built-in authoring role or a configured role, then an existing session. Keep that selection for
subsequent reads and edits. A chat in this host is not an Agentplace session.

Read the guidance returned when opening the session. Skills explain how to build the app; MCP
and HTTP API are ways to perform the same permitted operations. Use the guidance's skill names,
descriptions and paths to select what to read. Load required-entry skills first. Before each kind
of work, read the matching specialist skill and only the supporting references that work needs.
For example, read website-migration guidance for website collection, then component and styling
guidance when implementing the response. A small text edit does not need the entire skill catalogue.
Reuse guidance already read in the current context; refresh it when the selected role, template or
reported guidance provenance changes. Finish incomplete required reads before relying on them.

The selected role's instruction and current available actions define this inspection's scope.
Skills may describe future actions or actions available elsewhere; they cannot grant tools that
this connection does not expose. Agentplace's role policy does not govern unrelated host tools.

Choose the transport from the current operation and available access:

| Situation | Method |
|---|---|
| Interactive discovery, reading applicable skills, a few source edits, a command or build check | Use the connected MCP tools by default. |
| An authorized code client can reduce a large result, page through an inventory, compare many digests or combine independent reads | Use the HTTP API when that saves model-visible data or round trips. Read [API usage](references/authoring-api.md) first. |
| No supported API client, credential or network access, or API setup would cost more than this small task | Continue through MCP with targeted reads and existing batch inputs. |
| A failed or uncertain mutation, paid call or command | Reconcile the original effect before retrying; switching transports does not make a retry safe. |

Both transports use the same project, role, session and applicable skills. API access does not skip
required guidance, grant broader actions or start a Builder model. Preserve exact skill text and
source needed for design or edits. Filter mechanical inventories and diagnostics before returning
them to the model; do not replace necessary instructions or editable source with a lossy summary.

Inspect the relevant source and connect conclusions to observed files and content. Use search and
line ranges to narrow large reads. Respect incomplete guidance, pagination, partial search coverage,
and source that changes while you read. To see what the app did when it ran in Preview, read its
read-only Preview logs under `logs/` as the guidance describes. Do not present incomplete evidence
as a full audit or a runtime test.
Explain findings using the app's purpose, users and accepted business behavior.

Create an empty session when a new app needs its first authoring session, or the user asks for a new
one, and the connection has that permission.
Use the returned `newSessionKey` exactly. After a lost response, retry the same selection and key.
An incomplete-guidance response still selected or created the returned session: reopen that existing
session to refresh guidance. Do not silently create another session after deletion or expiry.

When source editing is available and authorized, read a file before you change it. An edit applies
to the app's current saved text, and a save to another file never blocks it. To change part of an
existing file, use `SearchReplace`. Use `UpdateFile` for a new file or a full rewrite, right after
reading the file, because it replaces whatever is saved now.

Every edit is saved when its call returns. Call `Checkpoint` when the app reaches a state worth
returning to, such as a finished change that builds, and before a large or risky change. Describe
that state in a few words. Do not call it after every edit. All edits since the last checkpoint form
one version in the app's history.

After a conflict, read the file again and make a new edit. After a failed or unconfirmed call, read
the file to see whether the change is there before you edit again. Report confirmed saving
separately from Preview, build or runtime checks.

To review the app, obtain its private Preview URL from `GetProject`. When the URL is available and
the host provides a browser, open it and check the visible behavior requested by the user. Share
the Preview link for owner review. After editing, use `CheckBuildStatus` for the saved change when available before testing the app. A saved
file or successful compilation does not prove that the customer flow works. Finish the current
save/build group before checking its Preview, and reuse that Preview tab through the bounded tests.
For visual checks, verify rendered content: images have decoded pixels, fonts have loaded, and the
layout works in the tested viewport. Image URLs, file existence and HTTP success alone do not prove
that an image is visible; an HTML fallback can also return HTTP 200. A blocked, timed-out or incomplete
browser check stays unverified in the final report. Use the host browser's documented recovery path
for tab failures. App actions such as sending messages or making purchases still require the user's
authority.

Connecting Agentplace through MCP does not sign the browser in. If Preview asks for login or denies
access, let the owner sign in to the owning Agentplace account in that browser, then continue.
Never collect their credentials or transfer tokens into the browser. If the host has no browser or
cannot complete sign-in, offer the review link and say which behavior remains untested. If the URL
is null, say that Preview access is unavailable for this project. Do not guess a URL, start Builder
or call `PresentAgent` as a fallback. Preserve confirmed save outcomes in each case. Keep recovery
and technical diagnostics with the model; tell the owner what was saved, what was checked, and any
action they need to take. Describe app checks in everyday language. Leave build diagnostics in tool
results.

When `ExecuteCommand` is available and authorized, use it for dependency work or checks that need
shell execution. It runs on the app's saved source, waits for the result for up to `timeoutSeconds`
(30 by default, at most 45) and saves supported file changes automatically. Repeating a call runs
the command again, so after a lost reply read the affected files before you repeat it. A command
that exits nonzero or times out may still have saved file changes. Report execution and saved
changes separately. `not_started` means nothing ran; its message says why. A `failed` result has an
unknown outcome: tell the owner its message and read the source again before deciding what to do
next.

When website research or Media actions are exposed, follow the website-migration guidance and
current schemas. Research uses Agentplace wallet credits with separate consent. Keep collection
status separate from billing status; an unknown paid outcome must not be automatically repeated.
Import selected public images through Media and use only confirmed canonical asset URLs.

This pilot supports bounded source edits with write consent, commands with additional execute
consent, and publishing with publish consent. Application tabs belong to later capabilities. When
the owner asks to publish or check a publish, read [publishing](references/publishing.md) first.
An MCP connection does not give scripts or UI components access to its bearer token.
An API client needs its own authorized connection; never ask the user to paste a host token into a
tool argument or source file.

Platform orientation is returned by the shared guidance owner, reviewed from Agentplace's
`agentplace-platform` skill. Project-specific skill bodies and role instructions stay on the platform
and are retrieved only after authorized selection.

When shared project connection tools are available, load `mcp-integration` guidance before setup.
Prefer suitable host connections for authoring when they already use the intended account. Agentplace
connections supply missing host access or the app's separate access; they do not inherit host grants.
Discover providers and native actions before selecting an exact linked account. For a new account,
call `configure_agent_connections` with `newAccount`, a stable `requestKey` and selected actions.
Use the returned field requirements to ask only for missing non-secret setup in chat; pass validated
answers as `configuration`. Show the returned **Connect service** link. Provider login and keys stay
on that secure access page, never in chat or source. Do not send owners to Connections or ask them
to create, name or attach a record manually.

Keep the original task active while access is approved. Call `resume` with the same `authorizationId`
and a bounded `waitSeconds`, respect returned expiry/retry advice, and continue until setup is ready
or a specific blocker requires action. Do not ask the owner to type “done” or open a new chat.
After an uncertain reply inspect the same authorization; do not start another provider login.
An expired exact account uses `reconnect` with its `connectionId`. After readiness, refresh native
tool discovery and verify the requested context. A stored binding alone does not prove live Preview
access. Perform a bounded read only when the user's task permits it; never test by sending mail or
modifying data. ManageMcpServers owns special configuration files.

Native MCP calls use `selection`, `source`, and nested `arguments`; authenticated API calls
use the selected-session/source route and a native arguments body. Unknown write outcomes require
inspection before retrying. A saved grant does not prove private Preview access.
