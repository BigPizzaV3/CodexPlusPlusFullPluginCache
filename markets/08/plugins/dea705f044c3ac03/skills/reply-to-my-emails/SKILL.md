---
name: reply-to-my-emails
description: Answer an email from the user's connected inboxes (Gmail, Outlook) through Kai. Finds the thread by person, keyword, or date, reads the whole conversation, studies how the user writes to that person, and saves a reply as a draft in their mailbox. The draft is shown in the chat and sent only after the user explicitly confirms. Use when the user asks to reply to, answer, respond to, or draft an email to someone, or to write a new email from their account. Requires the Kai connector.
---

# Reply to my emails

Find the thread, read all of it, write the reply the way the user writes to that person,
and stop at Send. The user presses it.

## Tools this skill uses

`search_emails`, `list_thread_emails`, `get_emails`, `list_accounts`, `create_email_draft`,
`send_email_draft`, `discard_email_draft`.

Kai is read-and-draft on the mailbox. It can't archive, label, star, or delete mail, so don't
offer to. If the email tools aren't available in this conversation, say so and suggest a
fresh conversation that opens with the word "email".

## Steps

### 1. Find the thread

Use `search_emails`. Filters combine with AND:

- `senders`: exact From addresses, for "the email from Sarah". Use it when you know the
  address (from context, the user, or an earlier result).
- `participants`: any address in From/To/Cc/Bcc, with `match: "only"` for a one-to-one
  history.
- `query`: subject and body keywords only. It doesn't match addresses. A person's name goes
  here when you don't have their address.
- `after`: a local date-time without `Z` or offset, read in the user's time zone.

Leave `includeFullBody` off unless you expect fewer than ten results. If several threads
match, list them with sender, subject, and date and ask which one.

### 2. Read the whole conversation

Call `list_thread_emails` with the `threadId` of the match. Messages come back oldest
first. Identify the latest inbound message; that's the one to reply to. Note its `id`, who's
on the thread, any question that was asked, and any deadline.

### 3. Learn the user's voice with this person

Call `search_emails` with `recipients` set to the counterpart's address,
`direction: "outbound"`, and `includeFullBody: true`. Two or three past emails show the
greeting, formality, length, and sign-off the user reaches for with that person. Match them.

If there's no outbound history, use the stored preferences in the `morgen://user/context`
resource when the client exposes it, and otherwise default to short, plain, and warm.

### 4. Draft it

Call `create_email_draft` with `replyToEmailId` set to the message from step 2 and the reply
in `bodyText`. Recipients and subject are inferred from the original. Add `cc` or `bcc` only
if the user asked for them.

For a new email rather than a reply: call `list_accounts` with `integrationGroup: "email"`,
ask which account if there's more than one, and call `create_email_draft` with `accountId`,
`to`, `subject`, and `bodyText`.

Then show the full draft text in the chat and say it's saved as a draft in their mailbox,
not sent.

### 5. Send only on the user's word

- When the user confirms in a message after seeing the draft ("send it", "yes, go"), call
  `send_email_draft` with the `draftId`. Then confirm to whom it went.
- Even if the original request said "reply and send", show the draft first and wait for a
  confirmation that follows it. Sending leaves the user's account and can't be undone.
- To change the draft: there's no edit call. Call `discard_email_draft` on the old
  `draftId`, then `create_email_draft` again, and show the new version.
- "Not now" means leave the draft where it is. It's in their drafts folder. Don't delete it
  unless asked.

## Writing the reply

- Answer what was asked. If the thread has an open question, the reply resolves it or says
  when it will be resolved.
- Keep to the length the user uses with this person. Most replies are a few sentences.
- Plain text (`bodyText`). Use `bodyHtml` only if the user explicitly wants formatting.
- No em dashes, no marketing tone, no sign-off the user wouldn't use.
- If the reply needs a fact you don't have (a date, a price, a yes or no), ask before
  drafting rather than inventing it.

## Guardrails

- Never call `forward_email` as a way to reply. It sends immediately, with no draft step.
- Never send in the same turn the draft was created.
- Never send to addresses the user didn't ask for. Reply-all only when the original
  went to several people and the user didn't say otherwise; say who's on it.
- IDs are opaque strings from tool results. Never construct or guess one.
