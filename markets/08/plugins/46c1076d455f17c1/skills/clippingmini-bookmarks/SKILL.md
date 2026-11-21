---
name: clippingmini-bookmarks
description: >
  Save links and supported chat attachments, and list, search, and browse bookmarks
  in the user's ClippingMini library. Use when the user wants to save a URL or
  chat attachment, find a saved link or file by topic or remembered details, list
  recent clips, or browse folders in ClippingMini.
---

# ClippingMini bookmarks

## When to use

- Save a link or URL to ClippingMini
- Save a file attached to the conversation
- Show recent bookmarks or find clips by keyword
- Browse the user's folders before saving or searching

## Tools

- `add_clip` — save a URL (optional title / folder)
- `add_file` — save one attached file to ClippingMini
- `get_file_status` — check a saved file's post-processing status
- `list_clips` — list bookmarks
- `search_clips` — fuzzy search in the user's library
- `list_folders` — list folders for browsing

## Workflows

### Choose a folder for a save

1. When the user leaves the destination open, omit `folderId` and `folderName` so ClippingMini uses its default.
2. For each new save request that names a folder, call `list_folders` to find an exact name or alias match and pass its `folderId`. Use this lookup for all items with the same destination in that request. If no folder matches, or more than one matches, ask the user to choose an existing folder. Offer My Folder if available.
3. Report the actual destination if the save result includes a different folder or a message about the destination.

### Save a link

1. If the URL is missing, ask for it before calling tools.
2. Call `add_clip` once per URL, sequentially for multiple URLs. Include a title only if the user provides it. Follow the folder workflow for a requested destination.
3. Use the tool result to confirm the outcome. If `duplicate` is `true`, tell the user the link was already saved and name the returned folder if available. Otherwise, confirm the new save only after the tool succeeds.

### Save an attachment

1. When the user asks to save an attachment, call `add_file` with the file reference provided by ChatGPT. Follow the folder workflow for a requested destination. Use `add_clip` for links. Ask the user to attach the file again if the reference is missing or expired.
2. Pass each requested attachment once and make sequential calls for multiple files. Each successful call saves a new copy.
3. If the result is `processing`, tell the user the original was saved and post-processing is pending. Use `get_file_status` with the returned `documentId` when the user asks for an update. Report `ready` as complete and `failed` as post-processing failed with the original retained.

### Find bookmarks

1. Use `search_clips` for a topic, a remembered title, or a description of something the user saved. Search the whole library unless the user asks to search a specific folder.
2. For a conversational request, put the key words or a short phrase in `query`. Keep distinctive names and quoted titles. Omit conversational phrases such as “find that thing I saved earlier.”
3. If a successful search returns no items, retry once with shorter or equivalent terms that preserve the subject and any requested folder. For “이사했는데 집주인이 월세 보증금을 안 돌려줄 때 저장한 글 찾아줘,” search `월세 보증금 반환` first and then `보증금 반환` if needed. If the requested folder could not be resolved, clarify the folder instead of expanding the search to the whole library.
4. Use `list_clips` for recent bookmarks or a folder listing without a topic. Describe only the clips returned by the tool and use their returned titles and URLs. Explain why a related clip is useful when it covers a different case. If both searches are empty, say no matching bookmarks were found for the terms tried.

### Folders

1. Call `list_folders` when the user asks which folders exist or where to save.
2. For a request to create, rename, or delete a folder, direct the user to the ClippingMini web app.

## Rules

- Only operate on the signed-in user's private ClippingMini data.
- Prefer the smallest tool call that answers the request.
- If authentication is required, tell the user to connect / sign in, then retry.
- On tool errors, report the failure clearly and suggest a next step.
