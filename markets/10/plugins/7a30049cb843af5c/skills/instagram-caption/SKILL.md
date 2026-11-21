---
name: instagram-caption
description: Write an Instagram caption that works before the "… more" cut (first line, body, one call to action, search words, up to five hashtags), often with a "Comment KEYWORD" ask that a Saypage DM automation answers; check it, and publish it with Saypage when the user asks. Use for requests like "I need text for this post", "which hashtags should I use", "help me with the description of my Reel", or when a post is ready but has no caption.
---

# Instagram caption

A caption has one moment that matters: the line people see before "… more". Everything
else is for the few who tap, and for Instagram search.

## 1. Decide who speaks first

- **Video-led** (a Reel that opens on a spoken or on-screen hook): people read the caption
  after the video caught them, so it adds rather than repeats: the context, the details,
  the ask, the words people search for.
- **Caption-led** (a photo, a carousel, a product shot): the image cannot say much on its
  own, so the caption's first line does the catching.

Tell the user which case this is.

## 2. The first line

The feed shows about the first 125 characters (two lines on a phone) before "… more".
Make them stand alone, and end on something that makes people tap, not in the middle of a
word. Count the characters. Never open on a greeting, a hashtag, an @mention, "New post!"
or the brand name alone.

## 3. The body

- Short paragraphs, a blank line between them.
- Two or three phrases people would type into Instagram search, inside normal sentences
  ("sourdough for beginners", "brunch in Lyon"). Search reads the caption's words, which
  now do more than hashtags.
- The useful details: quantities, timings, prices, address, opening hours, dates. Only
  facts the user gave you.
- Rarely more than about 1,000 characters. Instagram stops at 2,200.

## 4. One ask

Pick one: save it, send it to someone, follow, open the link in bio, or comment a keyword.
Two asks split the response.

The keyword ask is the strongest when there is something to send (a recipe, a menu, a
guide, a price list, a booking link): links in captions are not clickable, and "link in
bio" loses people on the way. With Saypage, a comment-to-DM automation answers it:

- **The keyword**: one short word, no spaces, no accents, no emoji (Saypage matches
  accents and emoji exactly, so `RESA` is safer than `RÉSA`), different from the post's
  other keywords. Write it in capitals: "Comment GUIDE and I'll send you the guide by DM."
  Say it in the video too.
- **Check that something answers it**: `list_automations`. If no automation covers this
  post and keyword, offer to set one up (see "Automations" in the `saypage` skill), best
  with a page made for this post that delivers what the caption promises. Ask before
  creating it. On the Connector plan it is built as a draft and goes live with a plan
  that includes automations; on the Free plan it cannot be built, so say once that it
  needs a plan ("Plans" in the `saypage` skill).
- Promise only what the DM delivers.

## 5. Hashtags

Up to five: Instagram has capped posts at five hashtags since December 2025. They label
the topic for Instagram, they do not buy reach. Specific beats broad (`#sourdoughbaking`
over `#food`); local businesses add a place (`#lyonfood`). Skip `#explore`, `#reels`,
`#viral` and `#fyp`. Put them at the end, or use none.

## 6. Mentions, alt text, language

- @mention only people or brands that are in the post (a collaborator, a supplier).
- Write alt text for photos and carousels: one sentence on what the image shows. Saypage
  takes it as `alt_texts` in `prepare_instagram_post`.
- Write in the audience's language. For a bilingual audience, ask whether they want one
  language per post or both (the main one first).

## 7. Check before you show it

- The first 125 characters make sense alone.
- One ask, and a keyword that an automation answers (or the user knows it needs one).
- Five hashtags at most, no URL in the caption.
- Every fact comes from the user.
- The `natural-voice` pass is done.

## Output

The caption in a code block, ready to copy, then a short check:

```
First line    112 characters, ends before the cut
Ask           Comment GUIDE (no automation on this post yet: set one up?)
Search words  "sourdough starter", "beginner bread"
Hashtags      3
```

## Publishing it

Only when the user asks. If `get_account` shows `can_publish_posts`, the caption goes into
`prepare_instagram_post` (photos and carousels) or `publish_instagram_video` (Reels), as
the `saypage` skill describes: show the final caption, wait for the go-ahead, publish once.
Otherwise the user pastes it in the Instagram app. Saypage cannot change a caption after
publishing or delete a post: the user does both in the app.

After publishing, `list_instagram_posts` shows the post with its `comment_keyword`: if an
automation was meant to answer it, make sure it is active.
