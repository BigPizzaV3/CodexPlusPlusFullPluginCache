---
name: dm-writing
description: >-
  Write the messages and button labels of a Saypage comment-to-DM automation (opening message, link message, follow request, email request, public reply), and help answer someone who wrote first. Saypage sends DMs only to people who comment a keyword and cannot read the inbox. Use for requests like "write the messages my automation sends", "what should the DM say", "ask for their email in the DM", "how do I answer this person".
---

# DM writing

A DM lands in a personal inbox, next to messages from friends. It is welcome when the
person asked for it (they commented the keyword, replied to a story, asked a question)
and it delivers what they asked for, straight away. It is unwelcome in almost every other
case.

## What Saypage can do here

Saypage sends DMs only through **keyword automations**: someone comments the keyword under
a post and gets the automation's messages. It cannot read or summarise the inbox, send a
one-off message, or write to people who did not comment. When the user asks to read their
DMs or to message followers in bulk, say so and call no Saypage tool for that: offer to
help with messages they paste, or a keyword automation instead.

## 1. Automation messages (Saypage)

Instagram requires two steps: an opening message with a button, then the link.

- `opening_message`: thank them for the comment, say what is coming, ask for the tap.
  "Here's the croissant recipe you asked for 🥐 Tap below and I'll send you the link."
- `opening_button_label`: what the tap gets them. "Send me the recipe".
- `link_message`: deliver at once, a tip for using it, and optionally one easy
  question. "Here it is! The dough needs a night in the fridge, so start it tonight. Which
  filling are you trying first?"
- `link_button_label`: "Open the recipe".
- `extra_link_buttons` (up to 2 more): the shop, the booking page, the YouTube channel,
  only when the follower would want them.
- With `follow_gate: true`, `follow_request_message` and `follow_request_button_label`: say
  plainly that the link is for followers, without guilt. "This one's for my followers:
  follow @maisonlune.lyon, then tap below and it's yours." / "I'm following". A follow gate
  wins follows and loses some of the people who wanted the link: say so to the user.
- With `email_gate: true`, `email_request_message`: say what they get and what the address is
  for. "Where should I send the guide? Reply with your email and you'll get it, plus my recipe
  of the week." It comes after the tap and any follow gate, and they type the address in
  reply. The link goes out once a reply holds one; the request goes out 3 times at most, then
  the sequence stops. Followers who already gave this account an address get the link at once.
  An email gate builds the list and loses some of the people who wanted the link: say so to
  the user.
- `public_reply` (optional): the short public answer under the comment ("Sent you a DM!").

Rules for all of them:

- **Button labels: 20 characters at most.** Count them.
- **Every message in the user's language**, including the follow-gate and email ones when
  those gates are on: the defaults are English, and a DM that switches language looks broken.
- **No surprise conditions.** The link comes with the second message unless the user chose a
  follow or email gate. With a gate, say so in the ask ("Comment GUIDE and leave your email")
  and say what they get for it: a condition that only shows up in the DMs makes a free offer
  feel like a trap. Ask for nothing else in return, such as a story or a share.
- **Let the user choose the words.** These DMs speak in their name: offer two tones (warm,
  short) or let them write their own, and show the final texts before `create_automation`
  or `update_automation`, as the `saypage` skill describes.

To see where people stop and rewrite the step that loses them, use `funnel-review`.

## 2. Messages the user sends by hand

Saypage only helps write these; the user sends them from the app. When someone wrote first
(a story reply, a question), answer what they asked in two to four sentences, then one small
question or next step. Keep every fact true, and never automate outreach: many cold messages
in a row get accounts restricted.

## Output

Each message ready to copy, with its character count, labels with their length:

```
opening_message       "Here's the croissant recipe you asked for 🥐 Tap below..."   (81)
opening_button_label  "Send me the recipe"                                           (18/20)
link_message          "Here it is! The dough needs a night in the fridge..."         (107)
link_button_label     "Open the recipe"                                              (15/20)
```

Run every message through `natural-voice` before showing it.
