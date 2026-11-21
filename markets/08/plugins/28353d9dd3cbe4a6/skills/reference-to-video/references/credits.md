# Credits and Billing

Credit configuration is read and cached by the server from the upstream combined model list. **The only
trustworthy quote source is the `credit_cost` returned by `i2v_get_options(kind="reference")`**, and each
model's `combinations[].credit` in `i2v_list_models(kind="reference")`. Do not rely on experience, and do
not apply image-to-video prices to reference-image-to-video--**they are different model lists with
different unit prices**.

| Operation | Billing |
| --- | --- |
| `i2v_list_models(kind="reference")` | Free |
| `i2v_get_options(kind="reference")` | Free |
| `create_upload_url` + upload (once per reference image) | Free |
| `i2v_create_task(kind="reference")` | **Charges credits**, amount equals `credit_cost` |
| `i2v_get_task` (polling, retrieving the finished video) | Free |

## Dimensions That Affect Credits

Credits are determined jointly by the parameter set "mode + quality + duration + whether audio is
included". The server uses that set to locate a billing template:

- **Quality**: higher resolution is more expensive (for example, 1080P is clearly more expensive than 720P)
- **Duration**: some templates bill linearly by duration, `ceil(duration / time_sec_unit) x unit price`
- **Mode**: high-quality mode is usually more expensive than fast mode
- **Model**: unit prices can differ greatly across models

**The number of reference images does not affect credits**: passing 2 images or 3 images costs the same as
long as the parameter combination is identical. Therefore, within the allowed image-count range, providing
one more reference image is "free"; you can suggest that the user add optional reference images to improve
results.

If any billing dimension changes, call `i2v_get_options` again for a new quote. Do not calculate it yourself.

## Membership requirement

`i2v_create_task` requires an active membership in addition to enough credits. Check `is_member` from
`get_user_profile()` before quoting. If it is not `true`, do not quote or submit: call
`get_pricing_url` and give the user the returned `pricing_url` to purchase a membership. The server
also enforces this rule: a non-member create call is rejected before any credits are charged.

## Rules for Communicating with the User

1. Before starting, use `get_user_profile()` to check the `credit` balance, and when quoting show
   "estimated cost vs current balance".
2. Before submitting `i2v_create_task`, you must obtain explicit user confirmation. **Do not submit on your own initiative**.
3. When the user hesitates between multiple models/qualities, list the price differences directly for comparison; do not report only one number.
4. When a task fails, its charged credits are refunded automatically, and retrying re-submits
   it at the normal price. State this rule once, up front, together with the initial cost
   quote--after that, a failure only needs you to report the error and ask retry-or-give-up;
   you do not need to reconfirm the price again.
5. If the finished video is unsatisfactory, first suggest **rewriting the prompt** before retrying--the effect
   of reference-image-to-video depends heavily on the prompt, while blindly switching models just repeats the charge.
6. If the balance is insufficient, the upstream service will error directly. Relay the error message
   as-is and prompt the user to recharge: call `get_pricing_url` and give the user the returned
   `pricing_url` to open in a browser, signed in with the same Wondershare account used to authorize
   this MCP, to top up credits or upgrade the plan. Do not construct the pricing link yourself.

## About `example`

The billing credential `example` is issued upstream according to the parameter combination; the server
selects it and passes it through unchanged. It is neither returned to the model nor constructible by the
caller. If you encounter an error related to `example`, it means the server-side model configuration has a
problem; report it to the service maintainer and do not attempt to bypass it.
