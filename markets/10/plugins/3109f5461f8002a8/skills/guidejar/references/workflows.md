# Tool workflows

The connected tool schemas are authoritative; this file covers behavior the
schemas don't spell out.

## Guide steps

Use `instruction` for ordinary steps, with `heading`, `tip`, or `warning` where
useful. For walkthrough intro or divider slides, use `chapter` with a title,
optional subtitle, and one to six buttons. Button destinations may be a URL, a
step index as a string, or `next`. Only set click markers with known image
dimensions and pixel coordinates; never guess them for an unseen screenshot.

Before calling `update_guide`, fetch the current steps and use their zero-based
indices. Updates apply first, then deletions, then additions. Update and delete
indices refer to the original guide; addition indices refer to positions after
deletions. Re-read the guide before planning another structural edit. There is
no reorder parameter; do not delete and recreate steps unless their full content
is preserved.

`faqs` replaces the entire FAQ list, and an empty array removes all FAQs. Omit
it, and any other field, unless the user asked to change it.

## Articles

`get_guide` may return an article body as serialized editor JSON. Read it as
content; never pass it to `htmlContent`, which expects HTML and replaces the
whole body. For a targeted edit, rebuild the full body with the existing content
intact. Use basic HTML: paragraphs, headings, lists, emphasis, and blockquotes.
If custom blocks can't be preserved, say so and link to the editor before
replacing the body.

## Folders

`get_team_folders` needs a team ID, so always get one first:

- For a new document or a team listing, call `get_teams` and use the chosen
  team's ID.
- To move an existing document, use the `teamId` that `get_guide` returns for
  it. Folders belong to one team, so only that team's folders are valid.

Never guess team or folder IDs. In `update_guide` and `update_article`,
`folderId: "none"` moves a document to the team root, and omitting `folderId`
keeps its current folder.

## Media

Adding images or video requires access to the actual file bytes and an HTTP PUT
upload. Browser interaction and screenshot capture are separate host
capabilities; the Guidejar tools do not supply them. Check these capabilities
before starting a request that depends on capturing and uploading screenshots.

If browsing or screenshot capture is unavailable, say so and ask for supplied
screenshots or offer a text-only guide. Supplied files still require byte access
and HTTP PUT support. If those are unavailable, explain that uploads cannot be
completed in this host and offer to create the guide without media, linking to
the editor to add it. Do not silently omit explicitly requested screenshots:
get agreement to the fallback unless the user already allowed it. Report any
omitted media clearly; do not mark a screenshot/upload test as passed.

1. Call `get_upload_url` with the destination team, the file name, and a
   supported content type: JPEG, PNG, GIF, WebP, MP4, or WebM.
2. PUT the file's bytes to the returned `uploadUrl` with the returned
   `contentType`. The URL is a temporary credential; don't show it in replies.
3. Confirm the upload succeeded, then pass `mediaUrl` to the guide step or as an
   article's `featuredImage` (images only).

Getting an upload URL does not mean the file was uploaded; never claim it was.
