---
name: nowistay-guest-records
description: Review and maintain privacy-minimized Nowistay guest records. Use when a host asks to find a returning guest, review a guest's stay history, or add a guest to the customer base. Do not use merely because another booking or messaging workflow mentions a guest.
---

# Nowistay Guest Records

Use the minimum personal data needed for the host's explicit request.

## Find and review

1. Use `list_guests` with a known name, a contact value already supplied by the user, or a property filter. Do not ask for email or phone merely to search.
2. Present the privacy-minimized list result. Do not imply that contact details are missing; they are intentionally omitted by default.
3. Use `get_guest` with `include_contact_details=false` for booking totals and recent stays.
4. Set `include_contact_details=true` only when the user explicitly asks for that guest's email or phone for a legitimate rental operation.

Never expose postal addresses, private notes, owner identifiers, or implementation fields. Keep internal guest IDs out of conversational responses unless needed to disambiguate records.

## Add a guest

1. Search by the supplied name first. If an existing record may be the same person, ask the user to disambiguate instead of creating a likely duplicate.
2. Collect only the fields the user wants to store. A name alone is sufficient; email, phone, and language are optional.
3. Never request payment-card or bank data, government identifiers, medical or biometric data, postal addresses, account passwords, access tokens, private notes, or unrelated personal information.
4. Call `create_guest_preview`. If it returns `duplicate=true`, use the existing privacy-minimized guest record and do not create another one.
5. Summarize exactly which fields will be stored. If the user asked only for a proposal, stop at the preview. If the user explicitly asked to add the guest, continue through platform confirmation with `create_guest_confirm` and only the approval token.

There is no guest update or delete tool in this workflow. Do not simulate those actions with booking tools.
