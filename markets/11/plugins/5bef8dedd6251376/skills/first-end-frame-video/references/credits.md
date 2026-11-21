# Credits and Billing

Credit configuration is read and cached by the server from the upstream unified model list. **The only trustworthy
quote sources are the `credit_cost` returned by `i2v_get_options`** and each model's `combinations[].credit` in
`i2v_list_models`. Do not quote users based on experience or numbers from historical conversations.

| Operation | Billing |
| --- | --- |
| `i2v_list_models` | Free |
| `i2v_get_options` | Free |
| `create_upload_url` + upload | Free |
| `i2v_create_task` | **Charges credits**; the amount is `credit_cost` |
| `i2v_get_task` (polling, retrieving the finished video) | Free |

## Dimensions That Affect Credits

Credits are determined jointly by the parameter group "mode + quality + duration + whether audio is included".
The server uses this group to locate the billing template:

- **Quality**: higher resolution costs more (for example, 1080P is significantly more expensive than 720P)
- **Duration**: some templates bill linearly by duration, `ceil(duration / time_sec_unit) x unit price`
- **Mode**: high-quality mode is usually more expensive than fast mode
- **Model**: unit prices can vary greatly across models

Therefore, if any dimension changes, call `i2v_get_options` again to obtain a new quote; do not calculate it yourself.

## Membership requirement

`i2v_create_task` is available to accounts with an active membership and enough credits. Check
`is_member` from `get_user_profile()` before quoting. If it is not `true`, do not quote or submit;
tell the user that this feature is not included in their current account. Only if the user asks
about plans, call `get_pricing_url` (when that tool is
available) and share the returned informational `pricing_url`. The server
also enforces this rule: a non-member create call is rejected before any task is created or any
credits are charged.

## Rules for Communicating with Users

1. Before starting, call `get_user_profile()` to check the `credit` balance, and show "estimated cost vs current balance" when quoting.
2. Before submitting `i2v_create_task`, you must obtain explicit confirmation from the user. **Do not submit on your own initiative**.
3. When the user is choosing among multiple models/quality levels, list the price differences directly for comparison; do not report only one number.
4. When a task fails, its charged credits are refunded automatically, and retrying re-submits
   it at the normal price. State this rule once, up front, together with the initial cost
   quote--after that, a failure only needs you to report the error and ask retry-or-give-up;
   you do not need to reconfirm the price again.
5. If the balance is insufficient, the upstream service will directly report an error. Relay the
   error message verbatim and tell the user the required credits and the current balance.
   If the user asks about plans or credit options, call `get_pricing_url` (when that tool is
available) and share the returned informational `pricing_url`; do not construct the link yourself.

## About `example`

The billing credential `example` is issued upstream by parameter combination. The server selects it and forwards it
verbatim; it is neither returned to the model nor constructible by you. If an error related to `example` occurs,
it means the server-side model configuration is problematic. Report it to the service maintainer; do not try to bypass it.
