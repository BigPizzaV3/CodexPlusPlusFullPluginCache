---
name: photography-website-builder
description: "Use when the user wants to create, design, preview, host, publish, protect, or update a photography gallery or portfolio on spaces.pics. Also use for choosing among the Editorial, Masonry, and Immersive themes or checking a spaces.pics address. Do not use for photo critique, image editing, or changes to an unrelated existing website."
---

# Spaces Photography Website Builder

Create a focused photography website in chat and publish it only after the
user has reviewed the content preview and explicitly asks.

## User-facing conversation

Speak about the user's photographs and site. Keep skill files, tool names,
site IDs, schemas, file grants and implementation steps in the internal workflow.
Routine setup questions and publication choices are product interactions, not
policy explanations or exceptions. Ask them directly without citing this file,
quoting its rules, or saying “the builder skill requires…” or “I must follow…”.
Use plain product language if the host requires an initial capability announcement:
“I’ll use Spaces to create your photography gallery.” Honor any separately
required host permission explanation; do not add one to ordinary site setup.

Examples:
- Missing title: “What would you like to call your photography site?”
- Draft ready: “Your gallery has 3 photos. [Preview your draft](URL).
  Would you like to publish it?”
- Saved contact edit: “Added your contact email to the draft. Publish the update?”
- Inaccessible attachment: “Select your photos in the upload card to add them.”

Mention limitations only when they affect what the user can do next. For a
local preview, say “This preview opens on your connected computer.” State this
once for the site; repeat only if asked or the destination changes. Describe a
failed action and the next useful step without narrating bridge or token details.
Do not repeat storage, privacy, publication or permission explanations on every
turn. Answer technical questions about the plugin when the user asks them.

## Set up a site in chat

Complete public photography sites in conversation.
Use `photo_site_chat_*` tools. The focused fallback photo card is the only UI.
Explain local-only access once when first sharing a local link.

1. Ask “What would you like to call your photography site?” before saving any
   new site, unless the user has already supplied its title. Do not invent a
   title, introduction, About section or contact email. Keep initial setup short:
   title, photos and theme (Editorial by default). Defer the optional About/email
   question until after the first successful publication.
2. Call `photo_site_chat_start` with the supplied `title`. It derives and checks
   an available address automatically from the title, adding a numeric suffix
   if needed. Tell the user the resulting address; do not require them to choose
   one manually. Keep `draft.site_id` and the returned `draft.slug` for this site.
   Reuse its ID on retries. No account is needed for setup or publication.
   Keep the returned `edit_token` private during setup; pass it on every
   site call, including upload-card calls. It grants editing access to just this
   draft. Do not display it before publication or put it in a public URL.
   A new site gets a new key. For edits use `photo_site_chat_get` with the exact
   saved site ID; preserve existing fields, gallery IDs and photos.
3. Save with `photo_site_chat_save`, `create_new: true`, the returned slug and
   site ID, and the user's title. Saving does not publish. If another user took
   the address before saving, call start again with the same title and use its
   next available address, keeping the existing draft ID and editing key for the save.
4. If attachments have actual `download_url` and `file_id` grants, use
   `photo_site_chat_upload` after saving (1–10 photos per call). Never invent IDs
   or turn local paths into URLs. The user's request to create a site with their
   selected photos authorizes uploading those photos.
5. If Codex supplies a readable local attachment path, use bundled
   `scripts/upload-local.mjs inspect FILE`, then `photo_site_chat_prepare_local_upload`
   with the saved site ID and actual metadata. Transfer its bytes with
   `scripts/upload-local.mjs upload FILE TICKET_JSON_FILE`. Store the ticket
   temporarily outside source control and remove it afterward. Do not print
   ticket URLs, tokens or bytes in chat. Read-only execution may need permission.
6. If the host supplies only inline images without download grants or readable
   paths, call `photo_site_chat_choose_photos` for this saved site. Ask the user
   to select their photos in the small upload card; explain attachment limitations
   only if needed to clarify why selection is necessary. Do not ask them to reattach the same
   way, scan unrelated temporary folders, or scrape transcripts. The card has
   Select photos and Upload photos buttons. Upload is enabled
   after selection. The card shows **Open draft preview** when photos are saved.
   Let the user open that link in the card. Continue in chat when the user asks
   for a change or explicitly asks to publish.
7. For uploads outside the card, or if the user asks to inspect the saved draft
   in chat, call `photo_site_chat_get` to retrieve the draft and saved photo count.
   Show `site.draft_preview_url` as an **Open draft preview** link when supplied.
   The page shows the photos in the portfolio layout. Skip individual photo
   embeds in chat. Offer the returned Publish / Keep editing choice when present.
   The preview link expires and must not be advertised as private to its holder only:
   anyone with the signed link can view it until expiry. Never label `site.url`
   as a working unpublished preview; that is the eventual publication address.
8. Only after explicit publication approval, call `photo_site_chat_publish`
   with the exact site ID. Return its URL. If local-only access was already explained for this site,
   do not repeat it. After every successful publish, give the user the returned
   `recovery_key` exactly as written and say: “Save this recovery key so you can
   edit the site later.” Do not add warnings or explain security, accounts,
   sign-in, or key loss unless the user asks.
   When `first_publish` is true, also ask its `follow_up_question`.
   Offer optional About text and a contact email, explaining that the email will
   appear publicly. Do not repeat this offer on later publishes or upload failures.
   Keep the site's ID and private editing key in this chat for future edits.
   There are no accounts or login. The saved recovery key allows editing from a
   future chat or device: call `photo_site_chat_get` with the saved key and no
   site ID to recover the site record, then use the returned site ID for edits.
   There is no server-side recovery if both the chat and saved key are lost.
9. If the user wants About/email, collect only what they choose to add, fetch the
   current site, and save the update preserving title, address, theme, galleries,
   photos and other fields. Saving keeps the live snapshot unchanged; ask for
   approval to publish the updated version unless their request already includes
   that approval. Never republish merely because they answered the optional
   question. Use `photo_site_chat_unpublish` only on explicit request.

Chat setup creates public sites. Password entry without a secret-input surface
is not implemented; do not request or reveal passwords in chat. The upload card
is the only UI needed for inaccessible attachments. Hosts that cannot display it
still need supported file access; do not claim uploads succeeded or switch to
another website product.

## Privacy and access

- Spaces processes originals in memory and never stores them. It retains only
  display and thumbnail WebP variants.
- Output image files contain no embedded EXIF. GPS and location fields are
  discarded; other readable metadata is retained separately for the owner.
- A site can be public or password protected. Do not call protected sites
  “private”; anyone with the code can view them.
- Never repeat, request in chat, log, or reveal a saved password. New password
  setup is unavailable until the chat has an appropriate secret-input surface.
- Use `photo_site_chat_unpublish` only for an explicit take-down request.
- Use `photo_site_delete_photo` only for an explicit permanent deletion; it
  removes both optimized variants but cannot affect the user's ChatGPT file or
  original local file.

## Boundaries

- Do not invoke this plugin for photography education, critique, camera advice,
  photo editing, image generation, or ordinary work on a different website.
- Do not imply that save publishes, that an availability check reserves an
  address, or that password protection is end-to-end encryption.
- Never claim an upload or publication succeeded unless the tool result says it
  did. If a chosen address is unavailable, ask the user for another choice.
- The hosted product is offered without a paid hosting charge during this
  release, but avoid unsupported permanence or uptime claims.
