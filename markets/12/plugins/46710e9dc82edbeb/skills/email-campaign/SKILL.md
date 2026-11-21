---
name: email-campaign
description: Plan, create, check and send an email campaign with Apsis Vega. Use when the user wants to write a marketing email, add personalisation, preview or test it, send or schedule it, send an earlier email again, or cancel a scheduled send.
---

Apsis Vega works on the user's Apsis account. The company is Apsis, with a capital A and the rest in lower case, never in all capitals, and the product is Apsis Vega. Once the user has picked an account and a section, pass the same `account` and `section` to every later call. When a tool result asks for the user's go-ahead, say what the next call would do and wait for their answer in a new message. The user's explicit instructions take priority over this skill, and a tool's own refusals and notes always apply.

## What an email's state allows

`list_email_activities` gives each email a `state`:

- `draft`: can be edited, previewed, tested and sent.
- `sent`: already sent. An email is sent only once; its content can go out again as a copy, a fresh draft made with `duplicate_email_activity` that keeps the personalisation tags intact.
- `scheduled` or `paused`: a send is booked. `cancel_scheduled_send` returns it to a draft, which is also how a send is moved to another time. A copy would leave the original booked, so both would go out.
- `queued`, `processing` or `exporting`: a send is under way.

Only an email with `isEngineManaged` true, one the assistant created, can have its HTML edited. Any other can still be previewed, tested, duplicated and sent.

## Create

1. Write the content, with the HTML following the email-html-rules skill. For personalisation, take the tags from `list_email_data_tags`; an unknown tag is refused at create.
2. If the subject or preheader came from you rather than the marketer, ask for both, together in one message. A rough answer is fine, since both stay editable.
3. Call `plan_email_activity`. It creates nothing. Tell the user what will be created and where: the account and section by name, the subject, and the preheader if there is one. If the plan's `existingWithSameSubject` names an email, mention it, since reusing it may be better than a new one. Click-tracking is on by default; mention it rather than ask.
4. After an explicit go-ahead, call `create_email_activity` with the `planToken` and exactly the same `subject`, `preheader`, `html`, `section` and `trackLinks` as the plan.
5. Changes to a draft go through `edit_email_activity`, not a second create.

## Check

- Call `preview_email_activity` straight after creating or editing, and put its `previewUrl` link in your reply: that is how the user sees what was built.
- `validate_email_activity` reports whether the email can be sent, and what would block it.
- `send_test_email_activity` sends a copy to up to 10 addresses. It writes the From address onto the email, so the sender should be settled first.

## Send

1. Call `describe_email_send` for the sending domains, subscriptions and segments of the section.
2. The sender's display name and reply-to address are the marketer's to give: every recipient sees the name, and replies go to that address. Where several domains are offered, the marketer picks one.
3. The audience is one or more subscriptions, optionally narrowed by a segment. For a new group, see the audience-building skill.
4. Call `send_email_activity` without `confirm`. Put the result to the user in their words: the sender, the audience and its `profileCount`, and for a scheduled send the local time and time zone from `willSend`.
5. A real send needs the user's explicit go-ahead in a new message, then `confirm` with the `reviewToken` and `audienceToken`. For an email the assistant wrote, set `previewReviewed` only once the user has said they looked at this version of the preview. For a scheduled send, pass `sendAtLocal` and `sendAtTimezone` back exactly as `willSend` gave them.
6. A refusal or a confirmation request from the send names its own remedy, written for the user. Relay it instead of working around it.

## Scheduling

- `sendAt` takes a concrete date and time. Which date a phrase such as "next Tuesday" means is the marketer's to say, so ask when it could mean two days.
- To find a booked send, list with `state` set to scheduled, section by section if needed. To call one off, use `cancel_scheduled_send`, which takes two calls with a go-ahead between them.
