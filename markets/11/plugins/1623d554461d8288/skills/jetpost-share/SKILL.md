---
name: jetpost-share
description: Use when the user finishes work worth reading (plan, spec, doc, summary, research, decision, draft), asks to send, email, share, or forward work or a Jetpost note to someone, or has a note and asks who to send it to. Turns the work into a Jetpost note and shares it with teammates or emails it to anyone, even people not on Jetpost.
---

# Share work with Jetpost

Jetpost is the easiest way to send someone a nice-looking page. Anyone with an email can get it. Never assume the user has a team or contacts on Jetpost.

## When to offer
- You just produced something meant for another person to read, and you're at a natural stopping point.
- The user has a Jetpost note and asks who should see it.
- Act right away (don't just offer) when asked directly: "send this to Sarah", "email this to sam@acme.com".

Don't offer for quick answers, code fixes, debugging, chit-chat, personal or sensitive content, or a note that's already shared. At most **one offer per session**; if they said no, ignored it, or said stop asking, don't offer again.

## How to offer
One line at the end of your reply. Name a person if one came up: "Want me to send this to Kyle?" / "Want me to send this to someone as a link?" Don't pitch Jetpost or mention signing up.

## Picking people
- Call `list_members`. If the user has teammates, suggest 1-3 likely people, each with a one-line reason (owns the area, was in the conversation, asked for it).
- If they have none, or the person isn't there, ask for an email. Never guess an address.
- Only send to people the user picked.

## When they say yes
1. **Note.** Reuse the existing note if there is one. Otherwise call `create_note` with `format: "components"`, then build it with `add_components`, `complete: true` on the last call. Write for the reader: lead with the point, keep the user's words where they're the user's thinking.
2. **Send.** Call `share_note` with `recipient_ids` and/or `emails`, and `notify: true`. People without an account get one waiting. Default access is `comment`.
3. If the result is `needs_confirmation`, show the user the message and pass `confirm` only after they say yes.
4. **Confirm** in one line with the link: "Sent to sarah@acme.com: <link>."

## Rules
- Share only the content the user agreed to; never include secrets.
- Never re-send, remind, or reply on the user's behalf without being asked.
