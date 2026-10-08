# Responses API prompt cache diagnostics

Use this reference only for API-level cache diagnostics. The local Cache Stats runtime cannot add options to ChatGPT/Codex requests and cannot compare two finished responses retroactively.

## Request a comparison

Diagnostics are available in the Responses API for GPT-5.6 and later supported models.

1. Choose a recent completed response from the same organization whose prefix should be reusable.
2. On a new request, set `prompt_cache_options.comparison_response_id` to that response's `id`. Omit it on the baseline request.
3. Read `prompt_cache_diagnostics` on the new response. For streaming, read it from `event.response` in the `response.completed` event.
4. Read `usage.input_tokens_details.cached_tokens` for actual reuse. `cache_write_tokens`, when returned, reports input written for later reuse.

Setting a comparison response requests diagnostics only. It does not load the earlier conversation, alter generation, or limit cache reuse to that response.

```python
baseline = client.responses.create(model=model, input=baseline_input)

current = client.responses.create(
    model=model,
    input=current_input,
    prompt_cache_options={"comparison_response_id": baseline.id},
)

diagnostics = current.prompt_cache_diagnostics
usage = current.usage.input_tokens_details
```

The reusable prefix must meet the model's minimum cacheable length; the official guide states 1,024 tokens for GPT-5.6 and later.

## Interpret the result

| Type | Meaning | Next step |
| --- | --- | --- |
| `cache_hit` | No miss was detected relative to the comparison. | Measure actual reuse with `cached_tokens`; later input may still be fresh. |
| `cache_miss` | A difference prevented expected prefix reuse. | Explain the single returned `reason`, apply its fix, and compare again. |
| `comparison_response_not_found` | The baseline diagnostic record is missing, expired, or unusable. | Choose another recent completed response from the same organization. |
| `unavailable` | The comparison was inconclusive, not ready, or unsupported. | Confirm model support and retry with another recent baseline; do not call it a hit or miss. |

For `cache_miss`, `comparison_reusable_tokens` is the raw size of the baseline's reusable prefix when present. `cache_missed_tokens` estimates how much of that prefix was not reused. These are diagnostic estimates, not billing fields.

## Cache-miss reasons

| Reason | Suggested fix |
| --- | --- |
| `model_changed` | Keep model selection stable for requests meant to share a prefix. |
| `prompt_cache_key_changed` | Omit the key unless separate accounting is needed, or keep it stable within the intended group. |
| `service_tier_changed` | Keep the returned service tier consistent. |
| `tools_changed` | Keep tool definitions and order stable; restrict execution without changing the supplied list. |
| `text_format_changed` | Keep `text.format` and its schema stable. |
| `reasoning_effort_changed` | Keep top-level `reasoning.effort` stable. On supported GPT-6 and later models, append a `configuration_update` to change effort while preserving the earlier prefix; see below. |
| `verbosity_changed` | Keep `text.verbosity` stable. |
| `context_compacted` | Preserve stable instructions and evaluate total input cost; compaction may still be beneficial. |
| `input_changed` | Keep the early prefix unchanged, move volatile data later, and append conversation turns. |

Diagnostics report only the first classified reason, are best effort, and expire after a short period. Fix the reported reason and repeat the comparison to reveal another possible cause. The diagnostics operation has no separate cost or rate-limit charge, but any baseline or retry API request is billed normally.

## Change reasoning effort on GPT-6

On supported GPT-6 and later models, keep the original top-level `reasoning.effort` and append this item to the existing Responses API `input` history:

```json
{
  "type": "configuration_update",
  "reasoning": { "effort": "high" }
}
```

The latest configuration update controls subsequent responses while preserving the earlier prefix. Keep the previous history and updates in subsequent requests. This helps preserve reuse eligibility; it does not guarantee a cache hit. Use it only when the selected model supports it, and preserve the user's requested effort. The local Cache Stats runtime cannot apply this option to ChatGPT/Codex requests.

## Interpret reuse and cost separately

The GPT-6 caching improvements operate in the API. Cache Stats reports the host's recorded usage and does not need a model-specific cache-hit adjustment.

- Reuse percentage is `cached_tokens / input_tokens * 100`, aggregated across calls by summing both token counts first.
- Non-cached input is `input_tokens - cached_tokens` and includes cache writes. The local runtime retains `freshInputTokens` as the field name for this count.
- For API billing, ordinary input is `input_tokens - cached_tokens - cache_write_tokens`. Apply each category's model-specific rate once; do not add cache writes to non-cached input again.
- Current guidance for GPT-5.6 and later gives cache reads a 0.1x input rate and cache writes a 1.25x input rate. A high reuse percentage does not by itself establish net savings. Check current pricing before estimating cost; do not apply API prices to a ChatGPT subscription.

Sources: [official Prompt cache diagnostics guide](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics), [GPT-6 reasoning updates](https://developers.openai.com/api/docs/guides/prompt-caching#change-reasoning-effort-without-rewriting-the-prefix), [usage and cost calculations](https://developers.openai.com/api/docs/guides/prompt-caching#monitor-cache-performance), and [API pricing](https://developers.openai.com/api/docs/pricing).
