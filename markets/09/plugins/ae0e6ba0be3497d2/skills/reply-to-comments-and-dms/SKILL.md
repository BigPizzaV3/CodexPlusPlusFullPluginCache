---
name: reply-to-comments-and-dms
description: Read and answer the comments, reviews, mentions and direct messages people send the user's brand, and set up automatic replies. Use when the user asks what they need to reply to, about new comments, DMs or reviews, wants to answer one, or wants an automatic reply or DM when someone comments or messages a keyword.
---

# Reply to comments and DMs

Use this skill to show the user what people said to their brand, answer it in the brand's voice, and set up
automatic replies. Nothing is sent without the user's yes. Explicit instructions from the user always take
priority over this skill, including the wording, tone and channels they name.

## What came in (read only)
Call `list_inbox`. It returns comments, replies, mentions, reviews and direct messages from every connected
channel in one list. A channel that is not connected is left out; a channel that could not be read is named in its
notes, so say which. Group what came in by channel, newest first, and point out the items that need an answer:
questions, complaints and people ready to buy. If nothing is connected, say that accounts are connected in the
Hermoso app under Connectors, in the sidebar.

## Answer one
1. Draft the reply in the brand's voice and show the exact text. Say whether it is public (comments, replies,
   mentions and reviews) or private (direct messages).
2. After the user's yes, call `reply_to_inbox_item` with the item's `id` from `list_inbox` and the text. Report
   what the tool read back.

## Support conversations
Intercom support conversations: `list_intercom_conversations` lists them, `read_intercom_conversation` reads one, and
`reply_to_intercom_conversation` sends a reply only with `confirm` set to true after the user approved the exact
words. Never leave a placeholder such as [Your name] in a reply; ask the user for any fact you do not have.

## Automatic replies
1. Call `list_dm_automations` to see the rules the brand already has.
2. Agree the keyword, the channel, which posts it watches and the message. Call `test_dm_automation` with a sample
   comment or message: it shows exactly what would be sent, and how, and sends nothing.
3. Call `save_dm_automation` after the user agrees the text. Offer `dryRun` first: it logs what it would send and
   sends nothing. On Instagram and Facebook a keyword comment gets a private message; on TikTok, Threads, YouTube
   and LinkedIn Pages it gets a public reply under the comment, because those platforms do not let an app message
   a commenter.

## Credits
Reading and answering is free on every channel except X, which uses credits for each item read or sent.

## Do not
- Do not send a reply or turn on an automation without the user's yes to the exact text.
- Do not promise refunds, prices, dates or anything else for the brand that the user did not give you.
