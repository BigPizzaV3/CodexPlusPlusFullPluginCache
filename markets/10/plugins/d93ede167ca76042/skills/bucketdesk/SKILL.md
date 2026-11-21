---
name: bucketdesk
description: Find, read, summarize and share files stored in the user's S3 buckets through BucketDesk. Use when the user mentions BucketDesk, S3, buckets, or files stored there.
---

Use the BucketDesk tools to work with the S3 buckets connected to the user's workspace.

- To find a file by name, call `search` first, then `fetch` to read a text file.
- To explore, call `list-connections` for connection and scope ids, then `browse` folders. Keys are full S3 keys and folders end in `/`.
- For PDFs and other documents, use `ask-document` with the user's question instead of reading the whole file.
- Use `get-metadata` or `get-media-metadata` for size, dates, type and photo or video details.
- Only call `create-share-link` or `start-archive-job` when the user asks to share or archive. Tell them what the link or job will cover before calling it.
- After `start-archive-job`, poll `get-archive-job` until it finishes and report the result.
