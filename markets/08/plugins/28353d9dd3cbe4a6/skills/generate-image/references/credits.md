# Credits and Billing

Credit configuration is read and cached by the server from the upstream combined model list. **The
only trustworthy pricing source is the `credit_cost` returned by `any2i_get_options`**, together with
`credits[].credit` for each model in `any2i_list_models`. Do not rely on experience, and do not apply
video prices to image generation--**image generation has an independent model list, and its unit
prices are not comparable with video at all**.

| Operation | Billing |
| --- | --- |
| `any2i_list_models` | Free |
| `any2i_get_options` | Free |
| `create_upload_url` + upload (once for each input image) | Free |
| `any2i_create_task` | **Charges credits**, in the amount of `credit_cost` |
| `any2i_get_task` (polling and fetching artifacts) | Free |

## The only dimension that affects credits: quality

The image-generation billing template is **tiered only by quality** (1K / 2K / 4K, etc.). This is the
biggest difference from video: video depends on four dimensions--"mode + quality + duration + whether
there is audio"--while image generation has only one.

**None of the following affects credits**:

- **Aspect ratio**: `9:16` and `1:1` cost the same, and choosing `free` costs the same too
- **Number of input images**: passing 1 image and passing 3 images cost the same. Therefore, within
  the count limit, adding one more reference image is "free"; you can suggest that the user provide
  enough reference material to improve the result
- **Prompt length**: within `prompt_limit_length`, a more detailed prompt costs the same; encourage
  specificity
- **Text-to-image or image-to-image**: for the same model and quality, the price is the same

When changing quality, call `any2i_get_options` again to get a new quote; do not calculate it
manually.

## Membership requirement

`any2i_create_task` requires an active membership in addition to enough credits. Check `is_member` from
`get_user_profile()` before quoting. If it is not `true`, do not quote or submit: call
`get_pricing_url` and give the user the returned `pricing_url` to purchase a membership. The server
also enforces this rule: a non-member create call is rejected before any credits are charged.

## Rules for communicating with the user

1. Before starting, call `get_user_profile()` to check the `credit` balance, and show "estimated
   consumption vs current balance" when quoting.
2. Before submitting `any2i_create_task`, you must get explicit confirmation from the user; **do not
   submit on your own initiative**.
3. When the user thinks it is expensive, **first suggest lowering quality**--this is the only knob that
   saves money. List the price differences between quality tiers directly.
4. When the user is hesitating between multiple models, list the unit prices at the same quality for
   comparison instead of quoting only one number.
5. When a task fails, its charged credits are refunded automatically, and retrying re-submits
   it at the normal price. State this rule once, up front, together with the initial cost
   quote--after that, a failure only needs you to report the error and ask retry-or-give-up;
   you do not need to reconfirm the price again.
6. When the prompt is too brief, **complete it before submitting**. Placing an order directly with a
   phrase like "draw a dog" will very likely require rework, which means wasting the user's credits.
7. When the finished image is unsatisfactory, first suggest **making the prompt more specific** before
   retrying--blindly switching models is just repeated charging.
8. When the balance is insufficient, upstream will return an error directly. Pass the error message
   through verbatim and prompt the user to recharge: call `get_pricing_url` and give the user the
   returned `pricing_url` to open in a browser, signed in with the same Wondershare account used to
   authorize this MCP, to top up credits or upgrade the plan. Do not construct the pricing link
   yourself.

## Set expectations that one task usually produces only one image

`image_urls` from `any2i_get_task` is an array, but **one task usually returns only one image**. If the
user wants "several images to choose from", that means **submitting multiple tasks and paying multiple
charges**. Explain the total cost before executing, and do not silently submit several orders in a row.

## About `example`

The billing credential `example` is delivered by upstream according to quality; after the server
selects it, the server passes it through as-is. It is neither returned to the model nor something you
can construct yourself. If an error related to `example` occurs, it indicates a server-side model
configuration problem. Report it to the service maintainers; do not try to bypass it.
