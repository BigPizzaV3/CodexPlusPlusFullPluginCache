---
name: create-fashion-content
description: Create fashion product photos and videos, explore models and styles, and manage your Photoshoot GPT creations.
---

# Create fashion content

Use on EVERY Photoshoot production follow-up, especially an attached image with use this, bunu kullan or referans olarak. Save hosted attachments with import_photoshoot_image; for local-only attachments use the catalog upload control. Never substitute native image generation or invent a hosted file descriptor.

Use the connected Photoshoot MCP tools. This skill also applies when the user asks for another production after earlier results in the same conversation.

The same workflow applies in Codex, ChatGPT Work and standard ChatGPT Chat when this plugin's MCP connection is available. Codex uses the catalog upload control for local-only images; hosted ChatGPT uses the real file descriptor import. If Photoshoot tools are missing, report that the Photoshoot connection must be connected/refreshed. Do not substitute another image provider or imply that Photoshoot production is available without its tools.

## Route an attachment turn before answering

When a Photoshoot draft is already active and the user attaches an image with a request to use it (including “bunu kullanmak istiyorum referans olarak”, “vazgeçtim bunu kullanalım” and “bunu kullancam”), this is an **import request**, not a request to discuss availability or create an image. Do these steps in the same turn:

1. Read `get_photoshoot_state` for the existing session and its current revision; do not start another draft or ask for the type again.
2. In hosted ChatGPT, use the attached file through `import_photoshoot_image`'s `photo` file parameter. ChatGPT supplies file metadata for this parameter (`file_id`, `download_url`, optional `mime_type` and `file_name`). Use the host-provided file descriptor/metadata facilities; do not conclude a download URL is unavailable just because it is not printed in the user's message. Choose `purpose: reference` for a reference catalog and `purpose: product` for a product catalog; products also require a real catalog product type. In local Codex without a real hosted descriptor, reopen the same source catalog and guide the user to its catalog upload control instead.
3. When the host supplies a real descriptor, call the import tool with it, the current revision and a stable request key. Do not stop after reading state or merely say you will save it. Do not invent URLs or file IDs. Report a tool/permission/download failure only when an actual tool response establishes it; if file metadata truly cannot be resolved, say the metadata could not be obtained, not that the Photoshoot tool or connection is missing.
4. On confirmed save, immediately render the matching catalog with `focus_selected: true`. Wait for the user's **Confirm and continue** click.

After import, use one brief saved/selected acknowledgement and point to the catalog's confirmation button. The catalog is the source preview. Do not add a separate Markdown/HTML image, attachment tile, source receipt card, data URI, placeholder image or another visual preview beneath it. Never use a file ID as an image URL. No production has started and no credits were spent. Render generated outputs only through the results tool after separately confirmed production.

## Choose a type for a new request

For each new independent production request, determine whether the user explicitly specified a type for that request. An earlier generation or an earlier answer does not supply a type for an ambiguous new request such as “başka bir üretim yapmak istiyorum”. Do not repeat the previous question-tool call from conversation history.

If the type is unspecified, call `ask_photoshoot_type` again with the current conversation language and `media_type: all`. This MCP call directly requests a native form when the connection supports it and waits for the user's answer. Include product video among all four choices. Restrict image/video choices only for an explicit user restriction. Do not announce that options are already open before calling the tool.

- `accepted` with a valid `generation_type`: use that explicit answer for one new draft via `start_photoshoot` and a stable request key.
- `declined` or `cancelled`: stop. Do not infer a choice, open a draft or immediately ask again.
- `question_required`: no native form was shown. Put the returned question and every returned choice directly in the final chat message as a numbered list, then wait for the user's answer. Do not call `request_user_input_async` or another question helper for this fallback, do not output only “choose an option”, and do not claim that a choice panel was displayed.

The asynchronous question acknowledgement `accepted: true` means neither that choices were visible nor that the user selected anything. It must never be treated as a production-type answer.

If the user explicitly requests a type for the new production, including an explicit request to repeat the previous type, use that instruction and avoid an unnecessary type question.

## Open existing images first

After every explicit type choice, including a numbered answer to the text fallback, call `start_photoshoot` with a stable request key and immediately call `render_photoshoot_catalog` in the same turn:

- `create_on_model_photo` and `create_video`: `kind: products`.
- `change_model` and `change_product`: `kind: references` first. For `change_product`, show `products` after the reference is confirmed.

Use the returned `session_id` and conversation language. Existing account images are the default. Tell the user they can select an existing image or optionally attach a new one. Do not require an upload, ask permission to open the catalog, or replace the catalog with manual questions about model age, hair, pose or background. `next_action: image_required` means an image source must be selected OR uploaded; it does not mean uploading is mandatory. If the catalog is empty, offer an attachment. If an image was already explicitly attached for this new production, import it using the normal saving flow and reopen the matching catalog with it selected. Wait for **Confirm and continue** before advancing.

## Save a user-attached image

An image sent while a Photoshoot catalog is open, together with “use this”, “bunu kullan” or “bunu kullancam”, continues the SAME Photoshoot draft. Read its current state/revision, import the attachment as the source, and reopen the matching source catalog with it selected. Never switch to ChatGPT native image generation/editing, `image_gen`, another provider, a new draft, or a direct generation call. The attachment is not a new standalone image-generation request and does not authorize production. When no hosted descriptor is available, use the catalog upload control in the same draft; never invent a file URL or generate a substitute. A later explicit request to leave Photoshoot is a separate user choice.

An attachment plus an explicit request to use it in Photoshoot (for example “bu ürünü istiyorum”, “bununla devam edelim” or “bu görselle çekim yap”) authorizes saving that attachment to the Photoshoot account. Do not ask for a separate saving confirmation. If the user only attached an image without clear intent, ask what they want to do before saving. Respect a refusal or an instruction not to save. Saving does not start production or spend credits, and never authorizes production.

Use current draft state and a real `product_types` catalog ID for products (page_size at most 20); references have no product type.

- For a hosted ChatGPT file with real `download_url` and `file_id`, use `import_photoshoot_image` with that file descriptor.
- For a local Codex attachment without a real hosted file descriptor, reopen `render_photoshoot_catalog` in the SAME draft with `kind: products` or `references`. Use the catalog upload control: ask the user to select the image there, choose a real product type for products, and explicitly save it to the account. The card hashes and uploads the selected bytes through an app-only authorization; no local MCP process, terminal helper, path reading, pasted base64 or temporary token file is needed. Do not call the legacy local import preparation tools unless a legacy helper is actually available. Do not claim the chat attachment was imported automatically. Wait until the saved source is shown selected and then wait for **Confirm and continue**. If the card upload is unavailable in a host, offer the normal website upload and then reload this draft's catalog; never invent a hosted file URL or replace the photo.

For hosted imports, preserve the same request_key, revision, attachment and image intent after a lost response. For card uploads, let the user retry in the same card; it retains the image bytes and stable request key and renews only its short-lived upload ticket. Do not submit another import from chat. On a definitive revision conflict, read current state before another save. Do not report success before a confirmed saved draft.

After a confirmed product save, immediately call `render_photoshoot_catalog` with that session, `kind: products`, `focus_selected: true` and the conversation language unless the upload card has already refreshed that same catalog. The newly saved product must already be selected and visible. Do not skip straight to the model/background picker. Wait for the user to click the product widget's **Confirm and continue** before advancing the funnel. For a saved reference, reopen `kind: references` in the same way. If rendering fails after the save, retry only the catalog render; do not upload the image again.

## Continue the existing funnel

Use saved state and real catalog IDs for product, model, background, pose, reference and motion selections. Catalog confirmation saves only selections. The review widget's explicit credit-spending button starts production; never infer production permission from the type question or conversation.

After a widget confirmation supplies the saved operation reference (or an admitted `photoshoot_operation` from an older card), use that exact operation ID with `wait_photoshoot_operation` until settled and open its separate result card with `render_photoshoot_results`. Never generate or approve again while tracking. Apply the same follow-up to edits and retries. Preserve the existing ownership, credit/refund and request-key rules.
