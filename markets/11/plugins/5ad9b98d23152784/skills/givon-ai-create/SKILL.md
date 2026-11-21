---
name: givon-ai-create
description: "Run the full Givon AI generation lifecycle through MCP or CLI: select an active model, build schema-valid input, upload references, launch the job and deliver the finished asset."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Givon AI Create

Create the first useful result with the smallest valid request. Keep MCP
mechanics, raw schemas, job ids and JSON internal unless the user asks for them.

## Default Route

1. Infer the modality (`image`, `video`, `music` or `voiceover`) from the user
   request. A voiceover needs a voice: list them with `givon_list_voices` (CLI:
   `givon voice list`) and pass the chosen id as `input.voice`.
2. Classify the requested result and the input media it depends on.
3. Call `givon_list_models` and choose an active model from live guidance, the
   user's priorities and the required input type.
4. Call `givon_get_model_schema` for that model before building `input`.
5. Build only schema-supported fields. Use schema defaults instead of inventing
   extra options.
6. If the request needs local/reference media, upload or import it first and
   keep the returned `assetUri`.
7. Confirm the price in the chat. Quote the exact request with
   `givon_quote_generation` (CLI: `givon generate quote`), tell the user the
   token cost and wait for their go-ahead before running. Skip the question only
   when the user said in this conversation to run without confirmations; that
   choice lasts until they take it back. Either way pass the quoted price as
   `maxTokens` (CLI: `--max-tokens`). A `price_above_limit` error means the
   price changed: re-quote and ask again. If quoting is unavailable, say the
   price is unknown and ask before running.
8. Call `givon_generate_content` with `wait: true` and a stable
   `idempotencyKey` for this exact request, then poll
   `givon_get_generation_status` until `succeeded`, `failed`, or `canceled`.
   Reuse that key after an uncertain response; do not launch a second job just
   because a wait timed out. Use a new key for a changed or intentional new request.

## CLI or MCP

Use one route for the whole task. On a computer with shell access, prefer the
`givon` CLI: if it is on PATH, run `givon whoami` once and use it when sign-in
succeeds. If the CLI is unavailable or cannot reach the service, use connected
Givon MCP tools. When neither route exists, ask the user to connect Givon MCP
through the host settings. CLI installation is a separate local setup action;
this generation skill does not download or execute an installer.

In a web chat without shell access, use MCP directly. If its tools are absent
or authentication fails, ask the user to connect or reconnect Givon through
the host's plugin/connector settings and browser sign-in. Do not ask a web user
to install a CLI or run terminal diagnostics. Both routes use the same account,
catalog, schemas, prices, assets and generation lifecycle.

## Model Selection

Live catalog guidance and schema own model availability, supported inputs,
defaults, selection guidance and cost. Match them to the user's goal and
priorities, then validate the chosen route against the live schema.

## Asset Route

- Local file with shell access: use `givon asset upload <path>
  --kind <image|video|audio>` and keep the returned `assetUri`. In ChatGPT, use
  `givon_upload_file_asset` when the host provides a native file parameter.
- Remote media: use `givon_import_asset` in MCP, or `givon asset import
<https-url|data-uri>` in CLI/API.
- Existing media: use `givon_list_assets` / `givon_get_asset`, or
  `givon asset list` / `givon asset get`.
- After upload/import, inspect the selected model schema. Pass `assetUri`,
  `https://` URL, or data URI only through fields that the schema supports
  (`sourceImage`, `referenceAssetUris`, `referenceAssets`, `assetInputs`, or
  model-specific asset slots). If the schema has no media field, the model is
  prompt-only for this request.
- Use `givon_archive_asset` or `givon asset archive` only when the user
  explicitly wants to hide an owned asset from active lists. It is a soft
  archive; audit links and existing project links remain intact.
- For image-to-video, source/start image goes into the schema-backed start image
  field; the prompt should describe motion and camera behavior.

## Prompt Craft

Preserve the user's creative facts and use the selected model's guide or the
relevant specialist skill for craft. The live schema filters fields and limits.
Keep the prompt complete, concrete and model-appropriate; never trade useful
control for brevity.

## UX Rules

- Ask only for information required to make the next action executable when it
  cannot be inferred from the current context or live schema defaults. Collect
  all such missing inputs together.
- Authentication stays in the browser or CLI credential flow; chat receives no
  API keys.
- For CLI authentication, use `givon login`; for a configured local MCP client,
  use `givon mcp doctor --client <client>`. In a web chat, reconnect through
  the host settings and browser sign-in instead.
- When using the CLI, prefer `givon generate create --wait` so the user gets
  the final asset, not only a job id.
- Prefer a host-native file parameter for chat attachments. If unavailable,
  upload actual bytes with `givon_upload_asset` only when the host can read
  them, or ask for an accessible HTTPS media link or an existing Givon asset.
  Never invent a download URL. With shell access, CLI upload is also available;
  the remote MCP server cannot read local files directly.
- Respect server polling guidance and use backoff. If the host cannot continue
  waiting, report the running job and retain its id for a status follow-up.
- Balance or entitlement failures may be explained, but do not initiate credit
  purchases, promote upgrades, or link to checkout from the plugin.

Read [references/mcp-workflow.md](references/mcp-workflow.md) when you need the
exact tool flow or error playbook.
Read [references/model-prompting.md](references/model-prompting.md) for the
universal model-guidance contract. After selecting a model, read only its family
file: [OpenAI](references/model-prompting-openai.md),
[Google](references/model-prompting-google.md),
[BytePlus](references/model-prompting-byteplus.md),
[xAI](references/model-prompting-xai.md),
[Alibaba](references/model-prompting-alibaba.md),
[Kling](references/model-prompting-kling.md),
[MiniMax](references/model-prompting-minimax.md),
[HeyGen](references/model-prompting-heygen.md), or
[Beeble](references/model-prompting-beeble.md).
Read [references/prompt-craft.md](references/prompt-craft.md) when shaping a
prompt, repairing a failed prompt, or handling image-to-video/design/brand
creative requests.
