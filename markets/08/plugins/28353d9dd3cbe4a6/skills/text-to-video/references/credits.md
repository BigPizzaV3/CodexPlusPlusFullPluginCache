# Credits and billing

Credit configuration is read and cached by the server from the upstream combined model list. **The
only trustworthy quote source is the `credit_cost` returned by `t2v_get_options`** and each model's
`combinations[].credit` in `t2v_list_models`. Do not rely on experience, and do not apply image-to-
video or reference-to-video prices to text-to-video--**the three modes use different model lists and
different unit prices**.

| Operation | Billing |
| --- | --- |
| `t2v_list_models` | Free |
| `t2v_get_options` | Free |
| `t2v_create_task` | **Charges credits**; the amount is `credit_cost` |
| `t2v_get_task` (polling and retrieving the finished video) | Free |

Text-to-video has no upload step, so it also never uses `create_upload_url`.

## Dimensions that affect credits

Credits are determined jointly by the parameter set "mode + quality + duration + whether audio is
enabled"; the server uses this set to locate a billing template:

- **Quality**: higher resolution costs more (for example, 1080P is clearly more expensive than 720P)
- **Duration**: text-to-video duration is an explicit parameter and usually affects credits linearly
  (10 seconds is often twice as expensive as 5 seconds)
- **Mode**: high-quality mode is usually more expensive than fast mode
- **Model**: unit prices can vary greatly between models

**Aspect ratio and prompt length do not affect credits**: `16:9` and `9:16` cost the same, and a
longer or shorter prompt costs the same. Therefore, within the length limit, writing a detailed
prompt is "free" and should be encouraged.

If any billing dimension changes, call `t2v_get_options` again to get a new quote; do not calculate
it yourself.

## Membership requirement

`t2v_create_task` requires an active membership in addition to enough credits. Check `is_member` from
`get_user_profile()` before quoting. If it is not `true`, do not quote or submit: call
`get_pricing_url` and give the user the returned `pricing_url` to purchase a membership. The server
also enforces this rule: a non-member create call is rejected before any credits are charged.

## Rules for communicating with users

1. Before starting work, use `get_user_profile()` to check the `credit` balance, and show
   "estimated cost vs. current balance" when quoting.
2. Before submitting `t2v_create_task`, you must obtain explicit user confirmation. **Do not submit
   on your own initiative**.
3. When the user is deciding between multiple models / qualities / durations, list the price
   differences directly instead of reporting only one number. Duration is especially worth pointing
   out: 10 seconds is often twice as expensive as 5 seconds.
4. When a task fails, its charged credits are refunded automatically, and retrying re-submits
   it at the normal price. State this rule once, up front, together with the initial cost
   quote--after that, a failure only needs you to report the error and ask retry-or-give-up;
   you do not need to reconfirm the price again.
5. If the prompt is too brief, **complete it before submitting**. Placing an order with a sentence
   like "generate a video" will very likely require rework, which means wasting one credit charge.
6. If the finished video is unsatisfactory, first recommend **making the prompt more specific** and
   retrying--the effect of text-to-video is almost entirely determined by the prompt. Blindly
   switching models and retrying only repeats the charge.
7. When the balance is insufficient, the upstream service reports an error directly. Relay the error
   message as-is and tell the user to recharge: call `get_pricing_url` and give the user the
   returned `pricing_url` to open in a browser, signed in with the same Wondershare account used to
   authorize this MCP, to top up credits or upgrade the plan. Do not construct the pricing link
   yourself.

## About `example`

The billing credential `example` is issued by the upstream service according to the parameter
combination; after the server selects it, the server forwards it unchanged. It is neither returned to
the model nor constructible by callers. If an error related to `example` appears, it means the
server-side model configuration has a problem. Report it to the service maintainer; do not try to
bypass it.
