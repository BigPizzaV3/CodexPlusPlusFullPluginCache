---
name: get-artwork-in
description: Get a customer's image into their Creative Hub (theprintspace) library — from the picker panel, a chat attachment, a file on their machine, a cloud share link, or the upload page.
---

Use this skill when the image the customer wants to print is not yet in their Creative Hub library. Try the lanes in this order and stop at the first that works.

1. **The upload tile in the picker panel.** `choose_artwork` opens the panel with an "Upload a new image" tile; the customer drops a JPEG, PNG or TIFF (up to 200 MB) and the panel tells you when it lands. In clients without panels, skip to 2.
2. **An image attached to the chat (ChatGPT).** Pass the attachment as `upload_artwork`'s `file` parameter; ChatGPT supplies a temporary download link for it. You can see an attachment, but you cannot access its bytes yourself — never claim to have uploaded one unless `upload_artwork` succeeded.
3. **A file on the customer's own machine**, only if you can run commands there. Ask for the path and upload it yourself with the three `agent_upload` steps returned by `choose_artwork` or `create_upload_link` (init → PUT the bytes → complete).
4. **A cloud share link.** Dropbox, Google Drive, OneDrive and SharePoint share links work with `upload_artwork`'s `image_url` when shared so anyone with the link can view; the server turns the share page into the file. We never connect to their cloud account — the link is all it takes.
5. **The upload page**, last. `upload.upload_url` from `choose_artwork` (or `create_upload_link`) opens a drop page in their browser, valid one hour. Then find the image with `list_library_images` using `search` = its name, or `uploaded_after` = the session's `issued_at`.

After any upload, carry on with the print — the customer's next message usually names the file, and `list_library_images` finds it by that name.
