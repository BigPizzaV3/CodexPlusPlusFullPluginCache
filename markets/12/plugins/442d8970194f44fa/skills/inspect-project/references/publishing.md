# Publishing

Read this when the owner asks to publish an agent, change who can open it, or check a publish.

Publishing needs the owner's publish permission. If `publish_agent` is missing, ask the owner to
reconnect Agentplace and approve publishing. Publishing deploys the app's saved source and replaces
the live version, so finish edits and build checks first.

## Agree on the audience

Ask the owner who should open the agent. Do not choose an audience for them. Pass it as `settings`:

| Who can open it | `settings` |
|---|---|
| Anyone with the link | `{"visibility": "public", "requireLogin": false, "isAllowToRemix": false}` |
| Anyone signed in to Agentplace | `{"visibility": "public", "requireLogin": true, "isAllowToRemix": false}` |
| Only the owner | `{"visibility": "private"}` |
| Named people or email domains | `{"visibility": "restricted", "accessGroups": ["ana@example.com", "example.com"]}` |

Set `isAllowToRemix` to `true` only when the owner wants other people to copy the agent.

## Publish and follow the result

Call `publish_agent` with the project ID and `settings`, then act on the result:

| Result | What to do |
|---|---|
| `needs_confirmation` | Show each warning to the owner in plain words. Only after they agree, repeat the call with `acknowledgedWarnings` set to `warningsFingerprint`. |
| Error saying publishing is blocked | Explain what blocks it. Nothing was deployed. |
| `published` | Share `link` with the owner. |
| `publishing` | Call `get_publish_status` about every 20 seconds until the result changes. A publish usually takes a few minutes. |
| `failed` | Tell the owner the `step` and `message`. Publish again after the cause is fixed. |
| `interrupted` | The server stopped mid-publish and nothing is running. Publish again. |
| `otherRequest: true` | Another publish of this agent is running, for example from the dashboard. This call started nothing. Wait for it with `get_publish_status`, then publish again if the owner still wants these settings. |

After a lost or unclear reply, call `get_publish_status`. Repeating the same `publish_agent` call is
also safe: the same request returns the publish it started instead of starting another.
