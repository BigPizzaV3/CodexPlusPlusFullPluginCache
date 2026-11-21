# Render the style picker

The visual picker is the first styling response in each chat. Use a category explicitly stated in this chat; otherwise show both sets immediately, with no category question first. It shows the supplied photos and all four price choices together. Do not ask for an outfit cap, photo, or dress code before showing it.

## Inline visualizations

When the host supports inline visualizations, use the bundled gallery builder. This is the preferred route in ChatGPT Work. Plain local Markdown image references can turn into file cards in that surface, and an image-inspection tool result may be visible only to the model.

1. Resolve this skill directory from its real installed path. Choose an absolute output path in the current task's writable working directory, such as its work/style-choices.html. Never assume /mnt/data exists or is writable.
2. Run the bundled Python 3 helper, using the host's available command tool. It uses only the Python standard library:

   `python3 <skill-directory>/scripts/build_gallery.py --category both --output <absolute-task-path>/style-choices.html`

   Both is the display default when the category is missing. Replace it with womenswear or menswear only when explicitly selected in this chat. Quote paths and arguments properly. Use the existing Python executable supplied by the runtime if python3 is not on PATH.
3. On a fresh request, omit `--tier`, `--style`, and `--budget-context` unless the user explicitly supplied those choices in THIS chat or explicitly asked to reuse an earlier selection. Memories, prior test chats, and usage examples are not user selections. If the current user did supply a tier, pass its exact allowed label with `--tier`. Pass an explicit current-chat cap with `--budget-context` and an explicit current-chat style ID with `--style`. These optional flags are input mechanisms, never defaults. A supplied cap permits continuation without requiring a named tier.
4. Check the command succeeded and produced the actual fragment. The helper embeds the bundled photo previews, preserves their full composition, and includes the style and price controls. Do not substitute generated imagery or rebuild it from memory.
5. In the final response, emit the inline content reference on its own line, using the real absolute path returned by the helper:

   `visualize{"path":"<absolute-task-path>/style-choices.html","title":"Style inspiration"}`

   The reference itself must be emitted as response content, not inside a code block or as a Markdown link. Do not attach the HTML as a regular file instead. One brief invitation to choose is enough; the gallery already contains the captions and all four tiers.

Each build creates a fresh gallery instance. The picker allows a style blend and one price preference. Tentative local choices stay private to that instance; only the user's explicit Continue submission sends them to the conversation. Never read a previous chat's generated gallery to initialize a new one. Its Continue button requests a follow-up only after an explicit click. If the host cannot send that follow-up, the picker shows the exact selection text the user can reply with. Do not assume that clicking a style or price alone started another turn.

The JPEG previews are resized display copies of the six supplied originals. They do not change the clothes, colors, or composition. The original full-resolution assets remain bundled for inspection or individual viewing.

For an explicitly identified developer regression test, the optional `--qa` flag marks any submitted choices as synthetic test fixtures, not personal preferences. Do not use that flag for ordinary styling requests.

## Other hosts

If inline visualizations are unavailable but the host can render original local images directly, display the three or six originals using its documented image syntax and offer the four price choices immediately below. Use only actual supported file references.

If neither presentation method works, say that inline pictures could not be displayed in this chat. Provide available image attachments as a fallback and show the four price choices, but do not claim the visual gallery appeared. A tool reading an image or a filename-only card is not a visible photo. Do not repeatedly try invented sandbox paths, public URLs, or a questionnaire to conceal this gap.
