# Direct save contract

Use only tools advertised for the current connection. Do not fall back to older
prepare/review/confirm tools or a panel. Host permission prompts remain controlled
by the host; the plugin does not add a second item-approval ceremony.

`get_import_context` accepts `capsule_name` or a returned `capsule_id` and supplies
silhouettes, colors, allowed/required attributes, allowance and destination. It
also returns `image_preparation` with a host-editing workflow and `flat_lay_prompt`.
Prepare every new image before saving, including existing retailer flat lays.
Show the finished image inline immediately when available, then continue saving.
Never ask original versus prepared or wait for approval of the shown image. Use the
host's visible generation experience when supported; do not promise streaming previews.
Rendering a preview does not replace handing off the actual finished file.
Standardize an existing flat lay, create one from product/on-person references if
needed, or generate a representative illustration from sufficient garment details
when no photo exists. Only an explicit keep-original request skips preparation.
The result should be sharp and truly #FFFFFF/transparent, not a gray backdrop.
Use the highest-resolution observed exact source (target at least 1024 pixels on
the long edge); transfer the full finished file, never a preview or screenshot.
Follow the returned quality targets using only capabilities the host exposes.
It contains no personal wardrobe or style data. Resolve missing tags from available
source evidence; ask only when a material required fact cannot be established.

`add_clothing_item` accepts:

- `idempotency_key`: one UUID per requested piece, retained across retries.
- `image`: actual host `file_id` and `download_url`, with MIME/name if supplied.
- `observed_details`: name, silhouette, primary color IDs, applicable required
  attributes and known optional brand/product facts using the advertised schema.
- `image_kind`: `garment_photo`, `product_photo` or `representative_illustration`.
- Optional `crop`: normalized x/y/width/height for the selected garment.
- Top-level `capsule_id` or `capsule_name`; leave the nested draft capsule empty.

For a generated flat lay, `image` must identify the actual finished file and
`image_kind` must be `representative_illustration`. Do not apply crop coordinates
from the source photo to the finished image. Keep observed product facts in
`observed_details`; editing does not establish new garment facts. White backgrounds
are preferred; transparent uploads are composited on white in the saved JPEG.
Never send a local path or a made-up URL in place of the host file handoff.

This path adds an owned item. It does not save shopping-list entries, replace an
existing garment or accept a catalog-choice ID. Keep nested catalog fields empty.
Never infer an owned purchase from a mere shopping suggestion.

`add_clothing_from_product` uses an observed `image_url` and public `product_url`
instead of the host file, with the same structured details/key/destination. Private,
account, order, tracking and signed links are not supported. Do not proxy around a
rejected URL. Use a supported host image handoff when available.
This saves the exact source picture and cannot substitute for transferring a
ChatGPT-edited flat lay. Use it only for an explicit original-photo request.
Unavailable editing/generation or file transfer does not authorize an automatic
source-photo fallback: preserve the prepared facts and explain the limitation.

A `details_needed` or capsule ambiguity response saved nothing and reserved no
allowance. Complete the facts and retry. A returned `job_id` can be checked with
`get_clothing_addition`. Only `saved: true` proves persistence; use its destination
and item receipt for the confirmation in chat.
New photo saves also verify that Cladwell's image delivery can return a valid
image before reporting success. To show an already-saved item, use its item ID
with the entitled selected-clothing context and render the returned saved photo;
do not substitute the source retailer URL or add the item a second time.

On a lost response, retry exactly the same operation/key. Keep file identity and
clothing facts stable; a renewed download link for the same file is allowed. Honor
`retryable` and server limits (up to three transfer attempts during the original
24-hour operation lifetime). Do not create new keys to evade quota or uncertainty.
Before changing a failed source, establish that the old operation cannot still save.
Never resubmit successful pieces after a partial batch failure.
