---
name: contact-import
description: Import contacts from a CSV or spreadsheet file with Apsis Vega. Use when the user wants to import, upload or add contacts from a file, or check on an import.
---

Apsis Vega works on the user's Apsis account. The company is Apsis, with a capital A and the rest in lower case, never in all capitals, and the product is Apsis Vega. Once the user has picked an account and a section, pass the same `account` and `section` to every later call. When a tool result asks for the user's go-ahead, say what the next call would do and wait for their answer in a new message. The user's explicit instructions take priority over this skill, and a tool's own refusals and notes always apply.

## Before the import

1. Call `describe_import_target` for the section's attributes and the subscriptions it suggests. Profiles are matched on email.
2. Get the file's exact column headings. Reading an attached file is the reliable way. A heading that is off by a space or a capital silently imports nothing into that column. The user can also type them.
3. For a column with no attribute to map onto, the user can drop it or keep it in a new attribute: `create_attribute`, which takes two calls with a go-ahead between them.
4. Agree one plan with the user, in plain language, because `create_import` starts the import with no preview:
   - which column goes into which attribute;
   - whether existing profiles are updated (`updateExistingProfiles`);
   - whether empty cells erase values already stored (`clearExistingAttributes`);
   - whether the contacts are subscribed, and to what.
5. Subscribing creates opt-in consent, and `resubscribeIfOptedOut` reverses earlier opt-outs. Include either only on the user's explicit yes. If the subscriptions couldn't be loaded, say so, rather than saying there are none.

## The upload

- `create_import` doesn't upload anything. Its first text block is written for the user and holds the upload link. Relay it as it stands, with the link intact, then end your turn: nothing happens until the user opens the link and uploads the file.
- The file goes from the user's browser to storage, never through the chat.

## Afterwards

- `get_import_status` follows the import. `awaitingUpload` means the user hasn't opened the link yet, which is not a failure.
- On `expired` the link has lapsed and can't be renewed: a new `create_import` makes a new one.
- When rows were `unsuccessful` or `skipped`, `get_import_report` explains why, with examples.
- `list_imports` finds an earlier import, and explains a refused new one, since only a few can run at a time per account. `cancel_import` stops a running one, in two calls with a go-ahead between them.
