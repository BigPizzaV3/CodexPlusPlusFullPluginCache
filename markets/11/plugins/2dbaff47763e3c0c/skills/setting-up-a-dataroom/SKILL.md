---
name: setting-up-a-dataroom
description: Use when creating a new data room and getting it ready - creating it, adding its documents, and having its reports produced. Covers the order to do it in, and the reports a room produces on its own so you don't generate them a second time.
---

# Setting up a data room

## THE SEQUENCE

1. `create_dataroom` with the company's `website_url`.
2. Upload the documents.
3. Let the room produce its reports.
4. Share it.

When `onboarding` in step 1's reply is `started`, steps 2 and 3 are linked:
the memo, business report and board deck are built only once every uploaded
document has finished processing. Uploading is what moves it forward; a room
with nothing uploaded waits indefinitely.

## WHILE THE ROOM PRODUCES ITS OWN REPORTS

While `get_dataroom`'s `onboarding_status` is `IN_PROGRESS` or
`DOCUMENTS_READY`, don't call `generate_memo`, `generate_business_report`,
`generate_data_deck` or `generate_company_profile`. Each starts a second
report alongside the one the room is already building.

Tell the user they are on the way. Once it is `COMPLETED`, they are in
`list_generated_reports`.

If `onboarding` was anything but `started`, or the status is `FAILED` or
null, nothing is coming - generate what the user asks for.
