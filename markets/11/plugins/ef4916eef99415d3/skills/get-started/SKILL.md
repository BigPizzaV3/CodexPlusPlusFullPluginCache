---
name: get-started
description: Set up Vinci after installing it - check the user's vault, follow the first creators they want in it, and show how to search, read and triage their own saved content.
---

# Get started with Vinci

Vinci is the user's personal knowledge vault: the videos and newsletters they choose to follow and keep, each
with notes on why it matters to them. New uploads from followed creators arrive in a daily triage, and
everything the user keeps stays searchable. Use this skill right after the user connects Vinci, to get them to
a useful vault in a few minutes.

## 1. See where the user stands

Call `get_account_overview`. Note how many channels they follow, how many items are in the vault, and how many
new videos wait in triage. Do not read the overview back verbatim - summarize it in one or two sentences.

## 2. If they follow fewer than three channels, help them pick some

Ask which creators they learn the most from (video channels, podcasts, conference channels). Offer to follow
up to three. For each one they name, call `follow_channel` with the channel's URL or @handle.

Only set `pullRecent` if the user wants the channel's recent videos brought in right away - explain that it
uses their monthly processing allowance. A good default to offer is 3-5 recent videos per channel. Processing
takes a few minutes; the videos then appear in their triage.

If a channel cannot be resolved, ask for its URL or @handle instead of guessing. If Vinci reports a plan limit,
pass the message on as it is - do not suggest buying or upgrading anything.

## 3. Show what they can do now

Briefly tell the user, in your own words:

- **Ask about what they've watched** - e.g. "What have I saved about pricing?" (uses `search_vault`; answers
  cite timestamped links).
- **Triage new uploads** - "What's new in my Vinci triage?" Then save the ones worth keeping and skip the rest
  (`list_videos` with scope `triage`, then `triage_video`).
- **Keep a video** - paste a video link and ask to save it (`save_video`).
- **Open the Vinci app** from the ChatGPT sidebar (or ask to open Vinci) to browse triage and the vault visually.

If the vault already has saved videos, end by running one real example for them: call `list_videos` with
`sort: "added"` and `limit: 3`, then offer to summarize one of them with `get_video`.

## Rules

- Only follow channels or save videos the user explicitly asked for.
- Vinci only knows what is in the user's own vault; never present general knowledge as something they saved,
  and never use Vinci as a general video search.
- Never mention prices, plans or upgrades.
