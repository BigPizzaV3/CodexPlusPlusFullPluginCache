---
name: convoflo
description: Work in the user's Convoflo client portal. Use when the user asks about their Convoflo secure spaces, clients' files or messages, or wants to ask a client for documents, a signature or a payment.
---

# Working in Convoflo

Convoflo is a client portal. Work happens in secure spaces: shared folders where an organization and its clients exchange messages, files, file requests, signature requests and payment requests.

## IDs

- Secure spaces, folders and files have an ID and a `URL` code like `abc123/def456`. Each tool says which one it takes.
- Pass IDs with their prefix, like `msg_637679863871967232` or `folder_123`. Never send bare or rounded numbers: some IDs are 18 digits long.

## Finding things

- A client or a secure space by name: `list_secure_spaces` with `query`.
- A file anywhere: `list_files` with `q`. Inside one secure space: `list_folder`.
- What clients sent lately: `list_recent_files` for files, `list_received_messages` for messages.
- To give the user a file, use `get_file_download_link` and share the link. Do not fetch it.

## Asking a client for something

File, signature and payment requests notify nobody when they are created. To send one:

1. Find the secure space with `list_secure_spaces`.
2. Create the request: `create_file_request` or `create_payment_request`.
3. Post a message in the secure space with `post_message`, passing the request's ID (`file_request_id` or `payment_request_id`). Members are notified.

Show the user the message and the request before posting, since posting notifies their clients. Use `status: draft` when the user wants to review it in Convoflo first.

## Reviewing what a client provided

`get_file_request` shows each item and the file provided for it. Approve with `approve_file_request_item`, or reject with `reject_file_request_item` and a reason, which is posted as a reply so the client provides the file again.

## Limits

- Nothing can be deleted through Convoflo in ChatGPT.
- Uploaded files are limited to 3 MB.
- Signature requests can be followed and reminded with `remind_signers`, not created.
- Payment request amounts are in cents, in Canadian dollars.
