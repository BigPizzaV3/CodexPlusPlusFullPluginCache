---
name: fcc-office-setup
description: Complete an explicitly requested first personal FCC connection check, then guide optional personal setup. Do not run for unrelated questions.
---

# Connect my personal FCC assistant

Version: 3.1.0.

1. Use only the owner separately authorized FCC tools. If absent, open the official installation entry at https://forevercard.club/fcc-ai/ and ask the owner to complete their own account sign in. Never collect credentials, build OAuth URLs or imitate a connection with network scripts.
2. For an explicit setup request read fcc_office_modules and fcc_office_instruction for personal_setup in the owner language. Follow the current instruction, not a stale copied setup plan.
3. Read fcc_office_context through the current connection. Confirm the returned owner identity and available current data. Missing CC stays unknown. Do not infer identity from a name typed in the chat.
4. When the instruction returns connection_check.required=true, prepare one short private overview from the actual context. Call fcc_office_save_result with the exact module, title and idempotency_key returned in connection_check. The usual contract uses morning_brief and Prvi pregled AI ureda, but the returned current contract is authoritative. Preserve the same exact payload and key for a retry after an uncertain response. Do not save if required permissions are unavailable.
5. Confirm only the actual saved result and return its own portal link or result ID. Direct the owner back to their FCC office to verify the saved first overview. A read alone, installed package, local preference or unsaved draft is not a completed connection check. Never claim the owner's personal style is already confirmed.
6. After the first overview, offer one optional personal setup question at a time. Personal style becomes active only after the owner reviews and accepts the exact proposal in FCC. Ask for separate additional permissions only when a selected task needs them. Keep existing schedules unchanged.
7. Installation does not send, publish, change CC or programme completion, connect social accounts, or create automations. Ordinary unrelated questions remain ordinary AI answers without FCC calls.