# GPT-6 model and API compatibility

## GPT-6.2 API targets

Checked November 19, 2026: [Astra](https://developers.openai.com/api/docs/models/gpt-6.2-astra), [Sol](https://developers.openai.com/api/docs/models/gpt-6.2-sol), [migration and prompting guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra.md). Treat these as API IDs, not Chat or Codex picker values. Start a demanding quality-sensitive comparison with `gpt-6.2-astra`; compare `gpt-6.2-sol` for complex work where cost matters. Do not replace a working lower-cost extractor or an explicitly pinned model without workload evidence.

For either 6.2 model, tool calling requires Responses; a text-only Chat Completions call is a different contract. Use supported effective effort when comparing; try medium for a new integration and low instead of unsupported none/minimal. Omit temperature, top_p and logprob options (including message.output_text.logprobs in Responses include). Do not translate UI speed or intensity labels into API options.

In Responses put reusable policy in the first developer message in input. Top-level instructions are appended after input on 6.2 and apply to that request. Append changing task data and new guidance; editing earlier messages can drop reasoning items and reduce prefix cache reuse. Replay required output items in order under the applicable storage policy. Prompt caching and persisted reasoning are different; neither guarantees correctness. No Flex on these two models. Do not opt into background mode, storage changes, a new region or a faster service tier by rewriting a prompt. Check the current docs and actual adapter before proposing any such change.

## Historical targets, for explicitly pinned workloads

The following October 2, 2026 snapshot preserves older compatibility paths. It is not the latest model list or an availability guarantee. Verify current official docs for the exact model before deployment.

| API model ID | Documented use | API reasoning effort | Tool calling |
| --- | --- | --- | --- |
| `gpt-6-astra` | Demanding reasoning and professional work | `low`, `medium`, `high`, `xhigh`, `max` | Responses required |
| `gpt-6.1-sol` | Complex coding and professional work with a speed/cost balance | `low`, `medium`, `high`, `xhigh`, `max` | Responses required |
| `gpt-6-luna` | Focused, high-volume tasks | `none`, `low`, `medium`, `high`, `xhigh`, `max` | Responses; Chat Completions function tools only with `none` |
| `gpt-6-sol` | Existing Sol integrations; GPT-6.1 Sol is the newer Sol model | `none`, `low`, `medium`, `high`, `xhigh`, `max` | Responses; Chat Completions function tools only with `none` |

Sources: [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra), [6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [6 Sol](https://developers.openai.com/api/docs/models/gpt-6-sol). Model choice is a task tradeoff. Compare representative results rather than always selecting the largest model.

## API checks

This section refers to the historical API rows above. For a legacy GPT-5.6 question, check the exact slug's model guide: the historical Chat Completions function-tool path required effective effort `none`; reasoning plus function tools belonged on Responses. Do not reuse that exception for GPT-6.2 Astra or Sol.

- Astra and 6.1 Sol reject `none` and `minimal`. The migration guide recommends `low` as the starting comparison for these older settings, with evaluation. Preserve an already supported effective effort before tuning it separately.
- Use `reasoning.effort` in Responses and `reasoning_effort` in Chat Completions. When effort is not `none`, omit `temperature`, `top_p` and `top_logprobs`; also omit Chat Completions `logprobs` and Responses `include: ["message.output_text.logprobs"]`.
- Product reasoning labels are not API enum values. Do not send a UI label such as `ultra` or a processing-speed label as API reasoning effort.
- Async tools, steering, compaction and cache controls require application support. A prompt cannot implement their event or state handling. Check the actual adapter contract before recommending them.
- Model support does not establish account availability, tool authorization, regional eligibility or a successful call. Do not change data residency or storage settings while improving a prompt.

Source: [current model and migration guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#migration-quickstart).

## Freshness and conflicts

For exact settings, consult the selected model page and current family guide together. Use the model-specific guide ahead of generic or older examples. If current official pages disagree, cite the conflict and leave the disputed setting unresolved. If web access is unavailable, name the date of the applicable section and avoid claiming a fresh check.

For Hermes and OpenClaw, ask for the relevant redacted runtime description only when needed. Verify provider, actual selected model, endpoint, supported parameters, available tools and approval configuration. Do not infer them from the agent's name or from this plugin.
