---
name: groundmail
description: Send transactional email and manage sending domains, templates, webhooks and suppressions with Groundmail. Use when the user wants to send an email from their app account, check whether a message was delivered, set up or verify a sending domain, work with templates or webhooks, review suppressed addresses, or check deliverability.
---

# Groundmail

Groundmail sends transactional email: the messages an app sends for a person, such as receipts, password resets and alerts. Use the connected Groundmail tools to act on the user's own account.

## How to work

1. **Read before you write.** Use the list and get tools (`list_emails`, `get_email`, `list_domains`, `list_templates`, `get_deliverability`) to see the current state before changing anything.
2. **Confirm before sending or deleting.** Show the user the recipient, subject and body, and send only after they agree. Ask again before `delete_webhook` or `remove_suppression`.
3. **Report what happened.** After a send, give the message id and its status. Use `get_email` to follow up on delivery.

## Sending a message

`send_email` needs a `from` address, a `to` address, a subject, and an `html` or `text` body (or a published template with variables).

- If the account has a verified sending domain, send from an address on that domain.
- If it has no verified domain yet, the shared test sender is `noreply@mail.groundmail.dev`. It can only send to the account holder's own email address. Use it for test sends.
- Production sending needs a verified domain. To add one: `create_domain`, then `apply_domain_dns` or give the user the DNS records, then `verify_domain`.

## What not to do

- Groundmail is for transactional email. Do not use it to send marketing blasts, newsletters or cold outreach to lists. If asked, explain this and suggest a marketing email tool instead.
- Do not guess email addresses. Ask the user.
- Never print API keys or webhook signing secrets back to the user more than once. A signing secret is shown only when the webhook is created.
- Never ask for or accept payment card numbers, bank details, passwords, government ID numbers, health information or other sensitive personal data in chat. Billing and account details are entered by the user only in the Groundmail dashboard. If a send is refused until billing is set up, tell the user to finish that step at https://app.groundmail.dev/settings/billing themselves.
- Do not put that kind of sensitive data in email content either.

## Errors

Error messages from the tools explain the fix. The usual ones: the sender is not on a verified domain, a sandbox send went to an address other than the account's own, or the plan's daily limit was reached. Tell the user what the message says and the next step.
