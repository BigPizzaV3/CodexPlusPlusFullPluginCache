---
name: completion-report
description: Use right after a Recomaze write, save, publish or job (a product written to the store, an article or post saved, a lead or step saved, the AI chatbot changed, a scan started) and when the merchant asks "did it save?", "is it ready?" or "what happened?". Reads the result back and answers in one or two sentences, with the blocker when there is one.
---

# What happened, in one line

A write is reported only after it is read back. The tool's answer is the claim; the read is the proof.

## After a write

1. The call that did it answered `needs_confirmation` first and ran with `confirmed: true` on the merchant's yes; `apply_product_content` runs on its `change_id`, `set_chatbot_voice` on its `change_id` alone, without the voice fields sent again.
2. Read the thing back with its own read of the very fields that changed: the product (`get_product`), the article or a saved post (`get_article`, by the article id the save answered), the lead (`get_lead_detail`), the chatbot's voice, tone and rules (`get_chatbot_voice`), its look, words and visibility (`get_popup_settings`), the routine's weekly budget and the kinds that run on their own (`get_daily_routine` with `preview: true`, its credits section), lead capture (`get_setup_status`, `plugin_setup.lead_capture`), the job (`scan_run_status`). Another tool's read is no proof of the change.
3. Answer in one sentence: what is saved, where it landed and, when there is one, the link. A second sentence only for a blocker or something the merchant must do. No list of ids, no restating of the approval, no cost unless it differs from the quote.

## A job still running

Say what runs and when to look again; do not poll it in a loop and do not start it a second time. A started job is not a finished one, and a saved draft is not a published one: say which it is.

## A failure

Name what did not happen and why, in the merchant's words, and what would make it work. Never report a save that only happened in the chat.
