---
name: get-started
description: Onboarding for the Fax.Plus plugin. Confirms the Fax.Plus account is connected, explains what the plugin can do, and suggests a first action.
---

# Get started with Fax.Plus

Use this skill the first time a user works with the Fax.Plus plugin, or when they ask what it can do.

## 1. Confirm the account is connected

Call `get-user` to confirm the Fax.Plus account is connected and to learn the account name.

- If the call succeeds, greet the user by the account name and continue.
- If it fails with an authorization error, tell the user to connect their Fax.Plus account from the plugin settings. Connecting opens a Fax.Plus login page. No API keys or tokens are needed.
- If it fails because the account is not eligible, explain that this Fax.Plus account cannot use the plugin (for example, accounts with Advanced Security Controls cannot connect) and point them to the Fax.Plus help center at https://help.alohi.com/hc/en-us.

Then call `list-numbers` so you know which sender numbers are available. If the account has no number, the user can still send faxes but cannot receive them.

## 2. Explain what the plugin can do

Keep it short. The plugin works only with the connected account's data.

- **Send a fax**: attach a document and name a recipient number or contact. The send flow is always `pipeline_start`, then `list-numbers` and `list-contacts`, then `request-file-from-user`. Never ask the user to paste file contents, and never read the file yourself.
- **Track delivery**: `list-outbox-faxes` for faxes still queued, `list-faxes` with category `sent` for history, `get-fax` for details, `get-fax-report` for the confirmation report.
- **Read the inbox**: `list-faxes` with category `inbox`, filtered by date or sender. `get-file` or `get-file-page` return a short-lived download link.
- **Manage contacts**: list, create, update, and delete contacts and groups.

Not available here: buying or releasing numbers, balance, team invitations, webhooks, and bulk deletion. Send the user to the Fax.Plus dashboard for those.

## 3. Suggest a first action

Offer one concrete next step based on what you learned, for example:

- "Want me to check whether you received any faxes today?"
- "Attach a PDF and tell me the fax number, and I'll send it."
- "I can show the delivery status of your last sent fax."

## Rules

- Any delete (`delete-fax`, `delete-outbox-fax`, `delete-contact`, `delete-contact-group`) requires explicit confirmation from the user first, one item at a time.
- Sending a fax is irreversible once transmitted. Confirm the recipient number before sending.
- Use E.164 numbers, for example `+12125550199`.
- Only act on the connected account. Never try to access another person's account.
