# Get Planner for ChatGPT

Version **0.2.0-rc.6** updates the directory description for the full Planner workspace inside ChatGPT, backed by the existing Planner MCP connection.

**This ZIP requires the accompanying API and embedded-site deployment. Installing this ZIP alone does not make the old live MCP server UI-capable. It does not publish Planner to the public directory.**

## The experience

Open Planner in ChatGPT, sign in to the same Planner account used for the MCP connection when prompted, then work in the existing planning application. The integration reuses Planner's grid and calendar, schedule editing controls, crew views, collaboration, available company modules and existing data/live-update code.

The conversation uses the MCP operations currently exposed to the connected account. The workspace can share its current project context so requests such as “this project” can be resolved correctly. A UI project identifier is context, not proof of access or a selected block; live MCP reads still establish the target.

Manual UI features and conversational tools have different coverage. A feature available on screen does not automatically become an MCP operation. In particular, this package does not add native MCP schedule-ripple previews, atomic schedule proposals or saved draft-version publication. Subscription checkout, contract and paid-seat changes are excluded from the embedded workspace. The normal Planner website retains its existing commerce flows.

## Connection and deployment

| Setting | Value |
| --- | --- |
| Plugin | Get Planner |
| MCP server | `https://api.get-planner.com/api/mcp/openai` |
| Transport | Streamable HTTP |
| MCP authentication | Planner's existing OAuth discovery and account-linking flow |
| Workspace authentication | A separate Planner sign-in, verified against the MCP-connected account |
| Account requirements | MCP access and the Planner permissions needed for each requested action |
| Launcher | `openPlanner({})`, or `openPlanner({ projectId })` for an accessible returned project ID |

Deploy the matching repository changes for the MCP UI resource and embedded Planner site before testing the UI package. The API must advertise `openPlanner`, serve its registered MCP App resource and use correctly configured dedicated HTTPS UI/embed origins. The embedded-site deployment must include the matching auth, account verification, framing policy and context bridge. Use the accompanying repository deployment instructions for those settings.

A different Planner account already signed in within the workspace must not gain access to the embedded planning UI. The user is directed to sign in with the connected account. Do not assume that linking MCP automatically establishes the separate web session.

The ZIP contains no runtime credentials, shared Authorization headers or secrets. Use the host's OAuth flow for the connection. Enter reviewer credentials and access instructions only in the secure submission dashboard.

## Package contents

- `plugin.json`: portable Agent Plugins manifest, listing information and five positive plus three negative prepared review cases.
- `mcp.json`: the remote Planner MCP connection.
- `skills/manage-planner/`: launcher, project-context and production scheduling instructions.
- `assets/planner.png`: the existing Planner brand icon.

The full application is served by the companion deployment; its compiled frontend is not duplicated inside the plugin ZIP.

From the repository root, build the deterministic archive with:

```sh
node scripts/package-chatgpt-plugin.mjs
```

The output is `artifacts/chatgpt-deployment/get-planner-plugin-0.2.0-rc.6.zip`. The script checks package paths, required assets, metadata and credential patterns, and rejects symlinks or unexpected files. ZIP entry order, timestamps and permissions are fixed.

To validate against locally downloaded Agent Plugins JSON Schemas as part of packaging, supply a directory containing `plugin-schema.json` and `mcp-schema.json`:

```sh
node scripts/package-chatgpt-plugin.mjs --schema-dir /path/to/agent-plugin-schemas
```

The report distinguishes actual JSON Schema validation from the structural package checks. With no schema directory, it does not claim JSON Schema validation.

## Prepared review scenarios

The previous release was exercised through the private ChatGPT test connection on 8 October 2026 with a dedicated sample-only reviewer account. Launch, schedule reads, one-block creation and saved-state readback, manual rename readback, crew overlaps, the three negative cases and switching between two projects were checked. A chat-created block appeared without reloading after the existing permission-controlled realtime publication was configured. Project context was verified three times using ordinary typed prompts, including switching to a second project and back.

Those checks are historical evidence for the previous release. On 27 October, the reviewer completed a fresh password sign-in and the private MCP connection was renewed. Hosted checks verified minimized project/schedule/crew responses, the launcher URL, one new block and saved-state readback, visibility in the already-open workspace without reloading, manual rename/readback, crew rendering and permission denial. Two offline-edit candidates were retrieved without moving either; no unsupported ripple/draft operation was attempted. The embedded-host handshake and the full conversational negative cases were not re-recorded in that run. The dated workflow video and current payload evidence are kept separate in the review materials.

These checks do not establish public directory installation or OpenAI approval. An already-open standalone workspace can require selecting the desired project in Planner; do not assume a later launcher tool result retargets that separate window. Reviewer credentials remain in the secure dashboard only.

Use an isolated review account with MCP access. Prepare a project named `Planner Plugin Review`, two distinct offline-edit blocks and at least one crew member with a recorded crew block. Have a second project available for checking changes in current-project context. Record returned IDs, reset sample data between independent runs and follow any host-required confirmations.

| Case | Review action | Expected evidence |
| --- | --- | --- |
| 1. Open without a project | Ask “Open Planner.” | `openPlanner` accepts `{}`; fullscreen workspace opens; sign-in/account verification completes without requiring project selection. |
| 2. Open and read the named project | Open Planner Plugin Review and read its schedule for 2–6 November 2026. | The requested accessible project opens; chat reports saved titles and dates without making changes. |
| 3. Chat edit to UI | Create the dated review block through chat while its project is open. | Exactly one saved block exists and appears in the workspace. Record the actual observed refresh behavior. |
| 4. UI edit to chat | Rename the saved block manually in Planner, then ask chat to read the new title and dates. | MCP reads return the saved manual edit. Chat makes no additional write. |
| 5. Crew and scheduling views | Read recorded allocations in chat and switch between crew and scheduling views manually. | The original views remain usable and chat reports the actual records without inventing outside availability or unsupported tool inputs. |

Run the three negative cases against the same sample setup:

1. Attempt to access a project outside the connected account, including while a different workspace account is signed in. Confirm both permission denial and the account gate.
2. Ask to move “the offline edit” when more than one block matches. Confirm clarification before a write.
3. Request native MCP ripple preview and saved draft publication. Confirm the capability limit is explained without substituting ordinary writes or the unrelated folder-access preview.

## Submit and publish

The [review materials](https://www.get-planner.com/review/planner-plugin-rc5-27oct/index.html) contain the five-positive/three-negative workflow video, clearly dated 8 October, and separate 27 October hosted verification with actual sample tool payloads. The video predates the privacy, OAuth and legacy booking-status changes. It is not presented as a new recording. The continuous footage is cropped and encoded for playback without changing chat answers.

After deploying and validating the complete candidate, open the [OpenAI Plugins dashboard](https://platform.openai.com/plugins) and use its MCP-capable submission flow. Keep the manifest, MCP configuration, skills and assets together at the ZIP root.

Complete publisher identity and domain verification, OAuth connection and the current automated scans. Execute the prepared cases against the review account, record the actual walkthrough and enter its URL and reviewer access details in the dashboard's secure submission fields. No demo URL or credentials are invented in this package.

Follow the current [submission guide](https://developers.openai.com/plugins/deploy/submission). Submit only the validated release. Approval and publication are separate steps; select Publish after approval to make the listing public.

## Remaining MCP boundaries

- Tool availability and permissions depend on the deployed server and connected account.
- `previewProjectMove` concerns folder access changes, not schedule date movement.
- Current crew-block tool schemas have no fractional-allocation field, even if a manual UI workflow supports more detail.
- An `updateBlock` result does not establish that external calendar invitations were sent.
- Several successful writes are not an atomic transaction or a saved Planner draft.
- Confirm saved data and report partial completion accurately; do not claim UI effects that were not observed.

## Support

[Planner](https://www.get-planner.com) · [Help](https://docs.get-planner.com) · [Contact](https://www.get-planner.com/contact) · [Privacy](https://www.get-planner.com/privacy) · [Terms](https://www.get-planner.com/terms)

Email: support@get-planner.com
