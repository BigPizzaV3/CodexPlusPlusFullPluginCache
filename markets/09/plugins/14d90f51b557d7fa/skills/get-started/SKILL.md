---
name: get-started
description: >-
  First steps with MetaRun in ChatGPT for iOS developers: what works right
  away without an account (worldwide pricing, storefront language audit, AI
  visibility check on any App Store app), how to connect a MetaRun account,
  and how change cards work. Use when someone asks what MetaRun can do, how to
  connect it, or how applying a change works.
---

# Getting started with MetaRun

MetaRun runs an iOS developer's App Store presence: listing copy in every
language, prices in every storefront, releases, review replies, keyword ranks,
and whether AI assistants recommend the app.

## Works immediately, for any app, no account

Offer these first: they show value before anyone signs in.

- `calculate_worldwide_prices`: a base price and a strategy (purchasing power
  parity, Big Mac, Spotify, or plain conversion) priced for every App Store
  storefront. Ask for the base price if the person has not given one; never
  pick it for them.
- `audit_storefront_languages`: which countries see a listing in a language
  people there cannot read, and where translated text sits on untranslated
  screenshots. Works on competitors too.
- `check_ai_visibility`: whether an answer engine names and recommends the app
  for the questions people actually ask, who it recommends instead, and which
  sources shaped the answer.

## With a MetaRun account

When a tool needs the person's own apps, ChatGPT shows a button to connect
MetaRun. They sign in on metarun.dev and choose read-only or "prepare changes
you approve". Their App Store Connect key stays encrypted on MetaRun and is
never shared with ChatGPT. Never ask for keys, passwords or tokens in chat.

If MetaRun says no App Store Connect key is connected, relay the link it gives;
the key is added on metarun.dev, not here.

## How changes happen

Every change is two steps, and the second one belongs to the person:

1. You call a preview tool (for example `apple_preview_set_promotional_text`).
   MetaRun reads the live store and shows a change card with the exact before
   and after.
2. The person presses Apply on the card. You cannot apply anything yourself.

So: never say a change is done until the card says it applied. If the card
reports the store changed or the preview expired, call the same preview again.
Every applied change lands in MetaRun's history; `history_search` finds it and
`apple_preview_revert_change` prepares an undo.

## Good first prompts to suggest

- "What should my $4.99 app cost in India, Brazil and Germany?"
- "Which countries see my listing in the wrong language?"
- "Do AI assistants recommend my app when people ask for a habit tracker?"
- "Translate my App Store listing into German and Japanese."
- "Is my next version ready to submit? What blocks it?"
