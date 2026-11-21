---
name: kinetik-trends
description: Use when the user asks what is trending or new on social media or in their niche, wants ideas worth recreating or something new to make, picks a trend Kinetik showed, asks for research, or links an Instagram, TikTok or YouTube post or video to find out what is in it. Showing the trends Kinetik follows, research with links to sources, reading a linked post, and making the trend picked.
---

# Trends

A question about what is trending, general or in the user's niche, is answered with Kinetik's trends
view. Research is for when the user asks for it, wants trends looked into in depth, or links a post or
video to find out what is in it.
Which format a post the user plans should take is neither: `get_post_format_recommendations` answers it.

## What is trending

Kinetik follows the content trends taking off across social media right now: photo effects, video
formats, carousel styles. They have a view of their own, Kinetik's trends view (`kinetik-show`
documents it), and that view is the answer to "what's trending": the user sees every trend Kinetik
found, each as it looks, and picks one with a tap. Show the view rather than researching or listing
trends in text; the view fills itself with today's trends, so none are named or promised from memory.
Then a sentence is enough, offering deeper research of their niche and saying it takes a while. If
the user cannot see views, name a few from what the view returned.

## Research

When the user wants research, Kinetik researches it: posts, formats and news, each with a link
to the original so the user can see it for themselves. Give the ideas worth recreating with their links, and offer to
make the user's own version of the one they like. Each finding keeps the link Kinetik gave for it, never a
profile or home page in its place, and the post angles it returned are given too. Pass the research on as
it came, without re-checking it with your own search.

A post or video the user links (Instagram, TikTok, YouTube) and asks about goes to research, the link
in its query: Kinetik opens it, watches it and reads its caption and speech, where a web fetch is refused.

## When the user picks a trend

A pick arrives as the user's own message, in their language, naming the trend and Kinetik. It is a
new piece:

- **No confirmations.** The pick is the decision, and a photo or video the user sends of themselves
  is their consent: never ask them to confirm the effect, the credits or the use of their face.
- **New material.** It is made from the photo or topic the user gives now. Something from earlier is
  reused only when they say so.
- **What this trend needs.** Pass the pick to `create_content` as it came, less its mention of
  Kinetik (wherever it stands), which only names this app; Kinetik asks for what the
  trend needs. Pass that on as the question. When the pick itself says what to ask for first (an effect
  that redraws the face wants a head-turn video too), ask for it with the photo, in one message.
- **As the trend is made.** A video trend becomes a video, a still stays a still, unless the user asks
  otherwise. The look is the trend's own, so add no style wishes the user did not express.
