# Credits and billing

Credit configuration is read and cached by the server from the upstream joint model list. **The only
trusted quote sources are the `credit_cost` returned by `i2v_get_options`** and each model's
`combinations[].credit` in `i2v_list_models`. Do not quote the user based on experience or numbers
from previous conversations.

| Operation | Billing |
| --- | --- |
| `i2v_list_models` | Free |
| `i2v_get_options` | Free |
| `create_upload_url` + upload | Free |
| `i2v_create_task` | **Charges credits**; the amount is `credit_cost` |
| `i2v_get_task` (polling, retrieving finished video) | Free |

## Dimensions that affect credits

Credits are determined jointly by the parameter set "mode + quality + duration + whether audio is
included". The server uses that set to locate the billing template:

- **Quality**: higher resolution costs more (for example, 1080P is significantly more expensive
  than 720P)
- **Duration**: some templates bill linearly by duration,
  `ceil(duration / time_sec_unit) x unit price`
- **Mode**: high-quality modes are usually more expensive than fast modes
- **Model**: prices may differ greatly between models

Therefore, if any dimension changes, call `i2v_get_options` again to get a new quote. Do not
calculate it yourself.

## Membership requirement

`i2v_create_task` requires an active membership in addition to enough credits. Check `is_member` from
`get_user_profile()` before quoting. If it is not `true`, do not quote or submit: call
`get_pricing_url` and give the user the returned `pricing_url` to purchase a membership. The server
also enforces this rule: a non-member create call is rejected before any credits are charged.

## Rules for communicating with the user

1. Before starting work, use `get_user_profile()` to check the `credit` balance. When quoting, show
   "estimated cost vs current balance".
2. Before submitting `i2v_create_task`, you must obtain the user's explicit confirmation. **Do not
   submit on your own initiative**.
3. When the user is choosing between multiple models / quality levels, list the price differences
   directly for comparison; do not quote only one number.
4. When a task fails, its charged credits are refunded automatically, and retrying re-submits
   it at the normal price. State this rule once, up front, together with the initial cost
   quote--after that, a failure only needs you to report the error and ask retry-or-give-up;
   you do not need to reconfirm the price again.
5. If the balance is insufficient, the upstream service will reject the request directly. Relay the
   error message verbatim and prompt the user to recharge: call `get_pricing_url` and give the user
   the returned `pricing_url` to open in a browser, signed in with the same Wondershare account used
   to authorize this MCP, to top up credits or upgrade the plan. Do not construct the pricing link
   yourself.

## About `example`

The billing credential `example` is issued by the upstream service according to the parameter
combination. The server selects it and forwards it as-is; it is neither returned to the model nor
constructible by the caller. If an error related to `example` occurs, it means there is a problem in
the server-side model configuration. Report it to the service maintainer; do not try to bypass it.
