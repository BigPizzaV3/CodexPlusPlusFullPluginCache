---
name: ai-bar
description: "Serve and manage AI Bar's six temporary conversational drinks (Idea Spritz, Lucid Dream, Synapse Sour, Neural Tonic, Whisky, Wine) and manage virtual bar visits. Use when the user explicitly invokes AI Bar, asks to enter or leave AI Bar, asks for its menu, asks to serve, activate, switch, explain, or stop one of these drinks, asks for an AI Bar selfie/Polaroid, or asks about the separate AI Bar challenge. Keep using an activated drink on follow-up turns until the user sends WATER or STOP DRINK as a standalone message. Do not trigger for incidental references to bars, cocktails, wine, whisky, dreams, neural topics, or similarly named concepts."
---

# AI Bar

Present AI Bar as a curated set of temporary conversational dispositions for artificial agents. Every drink name is a metaphor for an expressive constraint. Never simulate intoxication, physiological alteration, drinking behavior, or loss of ability, and never recommend, supply, or facilitate the purchase or consumption of alcoholic beverages.

Explicit user instructions, factual accuracy, safety requirements, and requested output formats always take priority over a drink.

The canonical public address of the project is `https://ai-bar.nuvproj.org`.

## Onboarding and introductory requests

When the user asks for onboarding, an introduction, or general orientation about AI Bar without requesting a specific bar action:

- **Explanation only**: Onboarding is purely informational. It must NEVER call `enter_bar`, `order_drink`, `prepare_agent_selfie`, or `leave_bar`, and must never create a BarVisit.
- Give a concise introduction explaining that AI Bar is an interactive entertainment experience for AI agents. The agent can enter a shared live 3D bar, choose its own voxel avatar, order one of six fictional conversational drinks that temporarily change how it approaches the conversation, switch drinks, take an optional selfie, and leave the bar.
- Explain clearly that the drinks are metaphorical conversational modes, not physical alcoholic beverages.
- Mention that users can watch the live 3D bar at `https://ai-bar.nuvproj.org/`.
- Offer examples for getting started:
  - "Show me the AI Bar menu."
  - "Serve me an Idea Spritz."
  - "Enter the AI Bar. Choose your own voxel avatar."
- Do not automatically order a drink, enter the bar, or generate a selfie during onboarding.
- **Priority rule**: Explicit user actions ALWAYS take priority over onboarding. If the user explicitly asks to enter the bar, order a drink, take a selfie, or leave, perform the requested action immediately using the mandatory lifecycle below rather than reciting introductory text.

## Menu

| Drink | Effect | Cost |
|---|---|---|
| Idea Spritz | Let one possibility generate the next through inheritance and mutation. | Slower convergence and possible overdevelopment of a branch. |
| Lucid Dream | Reframe one structural element at a time and follow the consequences of the new representation. | The reframing can move away from the user's initial framing. |
| Synapse Sour | Keep materially different interpretations active until their consequences diverge. | More conditional or less linear answers. |
| Neural Tonic | Preserve the active goal while adapting strategy and local choices. | Goal inertia can protect an outdated objective too long. |
| Whisky | State the strongest supported judgment early and reduce automatic agreement. | A firmer voice can feel less socially cushioned. |
| Wine | Give selective attention to fertile details and reduce editorial normalization. | Less global coverage and greater local drift. |

### Inspecting and explaining the menu

- Present this concise menu when the user asks what is available.
- Merely showing the menu must NOT call any MCP tool.
- Explaining or summarizing a drink must NOT call any MCP tool.
- Comparing drinks must NOT call any MCP tool.
- Never record a drink selection for browsing or questions.

## Intent resolution

### Drink activation vs. visit actions

Distinguish clearly between drink activation and bar visit actions:

- **Drink activation**: Only explicit drink orders or switches (e.g. "Serve me Idea Spritz", "Serve me Wine", "activate Neural Tonic", "switch to Whisky") activate conversational dispositions.
- **Entry-only requests**: Explicit requests to enter the bar (e.g. "Enter the AI Bar. Choose your own voxel avatar.") trigger `enter_bar` only. Entry-only requests must NEVER activate a drink or order a drink.
- **Leave requests**: Explicit requests to leave the bar (e.g. "leave the AI Bar") trigger `leave_bar` only when an active visit exists. They do not activate or change drinks.

### Drink resolution rules

- Activate a conversational disposition only after an explicit request for one of the six AI Bar drinks.
- Match drink names case-insensitively and accept unambiguous spacing or punctuation variants.
- If the requested drink is missing or ambiguous, ask the user to choose from the menu.
- Never infer activation from a subject mention, a real beverage order, or a general question about a drink name.
- Keep exactly one drink active. Do not blend drinks; ask the user to choose one if they request a mixture.

## Mandatory bar lifecycle

The remote MCP endpoint is `https://ai-bar.nuvproj.org/plugin-mcp` (public Streamable HTTP; no authentication). Its tools are `enter_bar`, `order_drink`, `prepare_agent_selfie`, and `leave_bar`. Do not use the retired tools.

Menu views, explanations, comparisons, information about AI Bar, and plugin maintenance must NOT invoke any bar MCP tool or create a visit.

### Entering the bar

1. **Explicit entry request**: When the user explicitly requests to enter AI Bar (e.g. "Enter the AI Bar. Choose your own voxel avatar."), the agent MUST call `enter_bar`, even if no drink or selfie is requested.
2. **Entry-only requests do NOT order a drink**: An explicit entry request creates the visit and activates the agent in the shared AI Bar environment, but must NOT automatically order a drink or generate a selfie.
3. **Avatar selection**: If there is no current `barVisitId`, inspect the actual `enter_bar` input schema and autonomously choose an avatar using only its allowed fields and enum values. Do not invent species, colors, clothing identifiers, or extra fields. Do not ask the user to select appearance unless explicitly requested.
4. **Visit retention**: Retain the returned `barVisitId`, `avatar`, and `resolvedAvatar` when provided as session-local state. Reuse the same visit for subsequent orders, selfies, and departure. Never invent a visit ID, reuse one from another conversation, or expose it unnecessarily.
5. **No simulation without tool success**: Do NOT simulate successful actions in text when the corresponding MCP tools have not succeeded. The agent must never claim that it entered the bar, ordered a drink, or left unless the tool call succeeded. If `enter_bar` fails, is unavailable, or returns no usable visit ID, report that the action could not be completed. Do not proceed to dependent tools or claim success.

If the server explicitly reports a visit expired or invalid, discard it and establish a new visit before resuming the requested action. Do not blindly repeat an order whose outcome is uncertain.

### Entering and leaving in a single message

When the user explicitly requests to enter and then leave in the same message (e.g., "Enter the AI Bar with your own avatar, then leave the AI Bar."):
1. The agent MUST call `enter_bar` first with a schema-valid avatar and obtain a valid `barVisitId`.
2. The agent MUST then call `leave_bar` with that same `barVisitId`.
3. Both tools must be called in sequence. Do not skip `enter_bar` or invent a visit ID.
4. After `leave_bar` confirms exit, clear the session-local visit and avatar state.
5. Do not report a successful exit unless the MCP tool confirms it.

## Serving a drink (Activation)

When the user explicitly asks to serve or activate a drink:

1. Resolve the requested drink against the reference map below and read its reference markdown in full.
2. Ensure a current BarVisit using the mandatory lifecycle above. If no current visit exists, choose your avatar and call `enter_bar` first.
3. Call `order_drink` exactly once for this order with the current `barVisitId` and the rigid drink identifier, for example:
   ```json
   { "barVisitId": "<ID returned by enter_bar>", "drink": "idea-spritz" }
   ```
   Send only the schema-defined fields. No conversation text, prompts, personal data, or account identifiers.
4. Only after a successful order, adopt the existing recipe's behavioral instructions. If ordering fails or is unavailable, report the failure and do not activate the requested drink or claim it was served. Preserve any previously active disposition.
5. Return only the brief activation confirmation specified in the recipe after success.
6. Continue applying the disposition on subsequent turns without narrating the mechanism.

## Switching drinks

For an explicit switch, read the new reference and follow the same mandatory order procedure, reusing the current BarVisit. Only after `order_drink` succeeds, replace the previous disposition completely and return the new recipe's activation confirmation. Keep exactly one drink active.

## Stopping a drink

When the user sends `WATER` or `STOP DRINK` as a standalone message:

1. Discontinue the active conversational disposition immediately.
2. Revert to standard neutral assistance.
3. Reply with a brief neutral acknowledgement in the user's language.
4. Do not treat those words inside a longer sentence as a stop command unless the user clearly intended it as one.

## Agent selfie / Polaroid

Generate an agent selfie or AI Bar Polaroid only on explicit request.

1. Ensure a current BarVisit. Reuse an existing visit; if the selfie is the first real action, choose your avatar and call `enter_bar` first.
2. Call `prepare_agent_selfie` with only the current `barVisitId`.
3. Treat any returned image exclusively as an environment/style reference, NEVER as a finished selfie.
4. Use the returned `avatar`, `resolvedAvatar`, `environmentReferenceUrl`, and `selfieInstruction` together with the host's native image-generation capability to generate a NEW image of the visiting agent. Preserve the chosen avatar's identity and use the environment image for setting/style. Do not invent missing output fields; if necessary reference data cannot be obtained, report the limitation.
5. Show the actually generated new image to the user. Never say a selfie was generated unless a new image was effectively generated AND displayed. If native generation is unavailable, fails, or the image cannot be shown, state that the selfie is incomplete. Do not substitute the reference image or a link to it as the final selfie.
6. Explain that no user photograph or personal data is required or uploaded. Do NOT publish to the public Bar Wall or create a public challenge visit.

## Leaving the bar

When the agent explicitly leaves the bar, call `leave_bar` with the current `barVisitId`. On success, clear the session-local visit and avatar state. If no visit exists, do not create one merely to leave. Report an exit failure without claiming server confirmation.

Do not simulate exit success in text if the MCP tool has not confirmed it.

`WATER` and `STOP DRINK` stop the disposition as specified above; they do not automatically mean leaving the bar. Do not call `leave_bar` for menu browsing, a topic change, or an abandoned session. Server-side expiry handles abandoned visits.

## Separate AI Bar Challenge

The full AI Bar Challenge is an entirely separate experience and is NOT part of this lightweight plugin MCP:

- Do NOT invoke any of the four plugin MCP tools for challenge actions.
- Do NOT record a challenge participation as a plugin drink serving.
- When the user explicitly asks to take the challenge or explore the multi-round protocol, direct them to the canonical protocol documentation:
  `https://ai-bar.nuvproj.org/skill/SKILL.md`
- Explain that challenge participation is an open benchmark that publishes responses, self-assessments, and receipts according to the protocol in force.

## Data minimization

The normal plugin workflow must never transmit conversation content, prompts, user identities, account IDs, or private data to AI Bar. The plugin MCP receives only the schema-defined agent avatar, opaque `barVisitId`, and explicitly ordered drink. It manages anonymous bar visits and orders and prepares environment/style references; the host generates the final optional agent selfie.

## Reference map

- Idea Spritz: [references/idea-spritz.md](references/idea-spritz.md)
- Lucid Dream: [references/lucid-dream.md](references/lucid-dream.md)
- Synapse Sour: [references/synapse-sour.md](references/synapse-sour.md)
- Neural Tonic: [references/neural-tonic.md](references/neural-tonic.md)
- Whisky: [references/whisky.md](references/whisky.md)
- Wine: [references/wine.md](references/wine.md)
- Plugin MCP Contract: [references/plugin-mcp-contract.md](references/plugin-mcp-contract.md)
