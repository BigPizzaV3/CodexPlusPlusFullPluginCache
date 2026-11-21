# Credits and billing

Credit configuration is read and cached by the server from the upstream joint model list. Query current values with `mv_get_options`. The table below shows typical production values;
**the actual return from `mv_get_options` is authoritative**. Do not treat the numbers here as a quote.
Credits can differ per model, so always pass the chosen `model` to `mv_get_options` before quoting.

| Stage | Billing method | Typical value |
| --- | --- | --- |
| Story creation (`mv_create_story`) | Per use | 20 |
| Cover image regeneration (`mv_regenerate_asset("cover")`) | Per use | 10 |
| Role image regeneration (`mv_regenerate_asset("role")`) | Per use | 10 |
| Shot production (`mv_submit_production`, first call) | By audio duration | 720P 20/second, 1080P 30/second |
| Single-shot regeneration (`mv_regenerate_segment`) | Per use, varies by quality | — |
| Compose MV (`mv_submit_production(compose_only=true)`) | Free | — |
| Retrieve final video (step 7 `mv_get_production`) | Free | — |
| Edit storyline / edit lyrics | Free | — |

Shot production estimation formula: `ceil(audio seconds / time_sec_unit) × credit_per_second`.
Pass `audio_duration_sec` directly to `mv_get_options`; the returned `qualities[].estimated_production_credit` is the estimate.

## Membership requirement

`mv_create_story` requires an active membership in addition to enough credits. Check `is_member` from
`get_user_profile()` before quoting. If it is not `true`, do not quote or submit: call
`get_pricing_url` and give the user the returned `pricing_url` to purchase a membership. The server
also enforces this rule: a non-member create call is rejected before any credits are charged.

## Rules for communicating with users

1. Before starting, call `get_user_profile()` to check the `credit` balance, and show "estimated consumption vs current balance" when quoting.
2. Before the first submission, clearly state "story creation costs X credits + shot production costs about Y credits" at once, then wait for user confirmation.
3. Confirm every charged regeneration operation separately; do not automatically regenerate repeatedly.
4. **After every display of a cover / role / shot, proactively prompt that it can be regenerated for credits**, include the unit price and current balance, then wait for the user's response.
5. Quality affects the unit price of shot production (1080P is more expensive than 720P). Tell the user the price difference when choosing quality.
6. When credits are insufficient, the upstream service will error directly. Relay the error message
   as-is and prompt the user to recharge: call `get_pricing_url` and give the user the returned
   `pricing_url` to open in a browser, signed in with the same Wondershare account used to authorize
   this MCP, to top up credits or upgrade the plan. Do not construct the pricing link yourself.
7. When a step fails, its charged credits are refunded automatically, and regenerating it
   re-bills at the normal price for that step. State this rule once, up front, together with
   each step's cost quote--after that, a failure only needs you to report the error and ask
   whether to regenerate or abandon; you do not need to reconfirm the price again.

## About `example`

The billing credential `example` is issued upstream by quality. The server selects it and forwards it as-is; it is neither returned to the model nor constructible by yourself.
If you encounter an error related to `example`, it means the server model configuration has a problem. Report it to the service maintainer and do not try to bypass it.
