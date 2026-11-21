---
name: pixly-listing-text
description: Write a property's listing description, Instagram/Facebook captions and a short Reel text from its photos and Pixly results, after looking at each one with view_pixly_photo, and offer a vertical video to post with them. Use when the user wants listing copy, a property description, social media captions or a post for their listing photos.
---

# Listing text and social posts

The user's own instructions always come first. Everything below is a default.

## How to ask, and what to report

- Questions: when ChatGPT offers its `ask_user_input` tool, ask through it — every question of the round at once, each with fixed choices (and the recommended one first); otherwise one short chat message. Never more than one round.

## 1. Find the photos

- Photos attached in the chat → you can see them yourself.
- Their Pixly results (staged rooms, edits, videos) → `list_library` (or `list_listings`, then `list_library` with that `listingId` when they name the property). You cannot see Pixly results by yourself: call `view_pixly_photo` with each item's id (a video gives its first frame). Up to 8 is plenty.
- Nothing yet → ask them to attach the listing photos, or to pick them in Pixly Studio (`open_studio`).

## 2. Ask once, only what is missing

Facts you can't see in a photo and they haven't given: bedrooms and bathrooms, size, price, location, anything special (a view, a garden, parking). Offer to leave out what they don't know. Don't ask about tone — default to warm and professional, in the user's language.

## 3. Write

- **Listing description** — 120 to 180 words: an opening line on the strongest feature, then the rooms in walking order, then the area. Only what is in the photos or what they told you; never invent features, sizes or prices.
- **Instagram / Facebook caption** — 2 to 4 short lines, one or two emoji at most, 3 to 6 relevant hashtags (place, property type).
- **Reel text** — one hook line under 10 words, plus 2 or 3 short on-screen lines.

The texts are the user's own: never mention Pixly, AI or editing in them (no "made with Pixly", no #Pixly). If a photo is virtually staged, add nothing about it unless they ask — that is their call for their market.

## 4. Offer the video

In one line, offer a vertical 9:16 video for the post: `cinematic_motion` with `format` "9:16" on the strongest photo. It quotes first; run it only on their yes.

## 5. Finish

Give the three texts, each under its own short heading, ready to copy. Never show job ids or model names.
