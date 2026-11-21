# User research

A study: AI-simulated consumers are interviewed and discuss the user's question, and a report comes out with traceable sources. Use it to understand consumers, test a product or concept, or analyze a market. Results are AI simulations; say so when you present them.

Tools: `atypica_study_*`, `atypica_panel_*`, `atypica_persona_*`.

After the user confirms the plan, a study usually runs half an hour to an hour. During that time you are the user's only view of it: the user sees what you write and nothing else, so keep them in the loop the way a researcher would, without making them wait in silence or read logs.

## The loop

One question is one study. `atypica_study_create({ content })` starts it and returns its `userChatToken`; keep it for every other study tool. Then poll `atypica_study_get_messages({ userChatToken, tail: 5 })` and act on `next`:

| `next.kind`      | Do                                                                                                  |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| `running`        | Tell the user what changed in `steps` (below); poll again in 1–2 minutes                            |
| `tool_result`    | Ask the user (see "When the agent asks"), then `atypica_study_submit_tool_result` with their answer |
| `artifact_ready` | Fetch the report or podcast with `next.token` and deliver it                                        |
| `text_message`   | Relay what the agent said; send the user's reply with `atypica_study_send_text_message`             |
| `stalled`        | Send `"Please continue the research"` as a text message                                             |

Write results carry a `status`: `saved_no_ai` means the account is out of credits, tell the user; `saved_while_running` means it was saved but another write started the agent first: do not write it again, and once `next` leaves `running` send a short message to continue; `ai_failed` means write again. Writes while the agent runs are rejected; wait for `next` to leave `running`.

## Telling the user what is happening

`steps` lists what the study has done, one entry per step, each with a `state` (`running`, `done`, `failed`, `interrupted`) and a short summary when done. Interviews, a discussion and a social observation also list their `records`, one per interview, each with its own `state`. Report changes, not the list:

- **When the study starts**, say what it will do in one sentence and give `replayUrl`: the user can open it without signing in to watch the study. It shows the study as of opening; reloading brings it up to date.
- **When a step starts or finishes**, say so in a sentence or two from its summary: "Five AI consumers are ready: …", "Three of five interviews are done; the first ones point to price as the main hesitation."
- **When a long step starts** (`social_observation`, `interviews`, `discussion`), mention `replayUrl` again: that is where the user can follow the interviews and the discussion as they happen.
- **When nothing changed**, one short line ("still interviewing") or nothing. Never invent progress, counts or findings that `steps` does not show.

Personas: when a `personas` step is done, show the names and tags as a short list labeled as AI-simulated consumers. For one persona in full, `atypica_persona_get` with its `personaId` from that step's `details`.

Going deeper: when the user asks what was actually said ("what did the parents say about price?"), read the record with `atypica_study_get_step({ userChatToken, stepToken })`, the `stepToken` from that record, and quote from it. One interview or one discussion at a time; pass `after` with the previous `total` to read only what is new in a running step. Do not read steps the user has not asked about.

## When the agent asks

The agent stops twice for the user: to clarify the question (`tool-requestInteraction`) and to confirm its plan (`tool-makeStudyPlan`). By default, show the question or plan, wait, and submit what the user chose. Do not pick options or confirm a plan without the user's answer or explicit delegation of that decision. Never take silence as a yes.

Explicit delegation such as "confirm whatever plan the agent proposes without asking me" permits `atypica_study_submit_tool_result` with `{ "confirmed": true }` when the agent proposes a plan for that study. Report that you confirmed under the user's delegation. This permission covers plan confirmation, not unanswered clarification questions; ask those unless the user also delegated choosing their answers. Without delegation, show the actual plan and wait for approval.

| `next.toolType`           | Show                                                                | Submit as `output`                                                                                                     |
| ------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `tool-requestInteraction` | Each question with its options, as choices the user can pick        | `{ "answer": ["<option>"] }`; several questions `{ "answers": [{ "label", "answer": [...] }] }`; `{ "skipped": true }` |
| `tool-makeStudyPlan`      | The plan in a few lines: what is studied, with whom, what comes out | `{ "confirmed": true }`, or `{ "confirmed": false }` and send the user's changes as a text message                     |

Use the client's own way of offering choices when it has one, with no option preselected; if it requires a default selection, number the options instead and let the user reply. Do not choose exploratory defaults or describe an option as selected before the user chooses it. Option text is copied exactly; `answer` is always an array.

## Delivering

- Report: `atypica_study_get_report` with `next.token`. Give the title, a short summary in your own words and `shareUrl`.
- Podcast, when the study made one: `atypica_study_get_podcast` with `next.token`.
- Earlier studies: `atypica_study_list`; each `token` is that study's `userChatToken`.

## Who is simulated

By default the agent builds the consumers from the question. To use a group the user already has, find it with `atypica_panel_search` and pass `panelId` to `atypica_study_create`.

## Files

Upload with `atypica_get_upload_credentials` (see SKILL.md), then pass `attachments` to `atypica_study_create` or `atypica_study_send_text_message`. A study holds up to 5 images and 10 documents in all, 3 MB each.
