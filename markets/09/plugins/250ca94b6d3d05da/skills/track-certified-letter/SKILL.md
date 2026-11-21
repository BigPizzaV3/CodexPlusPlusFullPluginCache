---
name: track-certified-letter
description: Answer where a letter sent through Piloxa is and whether it was received, and explain any USPS Certified Mail tracking status in plain words. Use when the person asks "where is my letter?", "did they get it?", "what does Notice Left mean?" or says their letter was refused, unclaimed or returned. Read only. Not for tracking packages or mail not sent through Piloxa beyond explaining a status word.
license: MIT
metadata:
  author: Decentralized Publishing LLC
  version: "1.5"
---

# Track a certified letter

## Use when
- "Where is my letter?", "did they get it?", "what does 'Notice Left' mean?", "my letter was refused / unclaimed / returned".

## Steps
1. If the letter was prepared in this conversation, call `get_certified_letter_status`.
2. If it was sent from an earlier chat, call `list_my_letters`. If this chat is not connected yet, call `connect_my_letters` and give the person the link and the four-character code; they sign in on piloxa.com, check the code and press Allow. Then call `list_my_letters` again and `get_my_letter` for the one they mean.
3. For a status word the person or the tool has (from USPS or Piloxa), call `explain_certified_mail_status` for its meaning and the next step.
4. Refused, unclaimed or returned: tell them to keep the envelope sealed; whether it still counts as notice depends on the rule they follow. Offer a new mailing, and the `mail-legal-notice` skill when a deadline is involved.

## Boundaries
A missing USPS scan means not yet reported, not failed. Delivered does not mean read. Never say a signature or delivery exists until the status shows it.
