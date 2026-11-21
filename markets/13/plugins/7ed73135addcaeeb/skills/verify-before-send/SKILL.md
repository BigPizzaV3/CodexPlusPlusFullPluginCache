---
name: verify-before-send
description: Verify a list of email addresses with mailfloss before sending a campaign or importing contacts. Counts the addresses, confirms the credit cost, runs one batch verification, and reports which addresses to keep, fix, review or remove.
---

# Verify a list before sending

Use this workflow when the user wants to check a list of email addresses before
they send to it or import it. For one or two addresses, call `verify_email` for
each address instead of starting a batch.

1. **Collect the addresses.** Take them from the user's message or attached
   file. Drop blank entries and exact duplicates, then tell the user how many
   unique addresses remain.
2. **Check credits.** Call `get_organization` and compare `credits.total` with
   the number of addresses. Each address uses 1 credit. If the account doesn't
   have enough credits, tell the user and stop.
3. **Confirm.** Tell the user how many addresses will be verified and how many
   credits the job will use. Start only after the user agrees.
4. **Start one job.** Call `start_batch_verification` once with all the
   addresses and keep the returned job `id`. Don't resubmit the same list to
   retry, because each submission spends credits again.
5. **Wait for the job.** Call `get_batch_status` with the job id until
   `processed` is `true`. If it takes a while, report progress as
   `emailsProcessed` of `numImported`.
6. **Read every result.** Call `get_batch_results`, passing `next` from each
   page until a page has no `next`.
7. **Report the outcome.** Lead with the count in each group, then list the
   addresses in Fix, Remove and Review:
   - **Keep:** `status` is `passed`.
   - **Fix:** the result has a `suggestion`, such as a misspelled domain. Show
     the suggested address and let the user confirm the correction. Don't
     change addresses yourself.
   - **Remove:** `status` is `undeliverable`.
   - **Review:** `status` is `risky` or `unknown`. Give the `reason` so the user
     can decide.

If the user asks for the cleaned list, return the Keep addresses plus any fixes
they confirmed, as plain text or CSV.
