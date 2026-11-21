---
name: repurpose-content
description: Turn one long piece (a YouTube video, podcast, blog post, newsletter, workshop, recipe collection or menu) into a week of Instagram Reels, carousels and stories that each stand alone, plus one Saypage page holding the full version that every post sends by keyword DM. Use for requests like "get Instagram posts out of my podcast", "reuse my YouTube video", "turn my article into content", or when the user pastes something long.
---

# Repurpose content

A long video, episode or article usually hides several Instagram posts, and the full
version deserves a home too. This skill finds the posts inside it, and puts the whole
thing on a Saypage page that every one of those posts can send by DM.

## 1. Take in the whole source

Work from the full text: a transcript, the article, the newsletter, the recipes, the
workshop notes. A link you cannot open: ask the user to paste it. Go through all of it
before choosing anything. If the user filmed the source themselves, ask for the file as
well, since clips of the real footage feel more alive than a re-shoot.

## 2. Inventory what can stand alone

Do not shrink the source into a summary: look for pieces that make sense to someone who
never saw it. Count them by kind, and show the counts before drafting:

| Find | What it is | Best as |
|---|---|---|
| **Moments** | a scene with a person and a turn: what went wrong, what changed | Reel |
| **How-tos** | steps someone can follow today | carousel or Reel |
| **Numbers** | a cost, a time, a quantity, a result | Reel hook or carousel cover |
| **Opinions** | a claim someone could argue with | Reel |
| **Fixes** | a mistake and how to avoid it | Reel |
| **Lines** | a sentence quotable as it is | story frame |
| **Questions** | what it answers that people ask | carousel or a reply Reel |

When the inventory is short (two or three finds), tell the user honestly: one strong post
from it is better than four weak ones.

## 3. The page behind the posts

Put the complete version on one Saypage page: the whole recipe, the full guide, the
checklist, the episode notes with their links. Offer to build it with the `saypage` skill
(`get_page_guide` first, then a private preview; publish only with the user's agreement).
Each post then closes on a keyword ("Comment GUIDE and I'll send you the full guide"),
and an automation sends the page.

Look at the plan's limits in `get_account` before offering an automation on every post.
A good start is one automation on the strongest post, and the same page in the bio link.
On the Connector plan the page and the automation are built and previewed, and go live
with a plan that includes them: say so once. On the Free plan neither can be built: say
once that they need a plan ("Plans" in the `saypage` skill).

## 4. Lay out the week

- Write each post for a stranger: no reference to the source ("in my podcast…"), and
  everything it needs to make sense inside the post itself.
- Change the hook type from one post to the next (types in `reel-script`), so the week does
  not feel produced on a template.
- Open the week with the post most likely to travel, and keep the most useful one (the
  how-to that sends the page) for when the first posts have brought new followers in.
- Clips from the user's footage: start and stop at the edges of a sentence, and keep their
  natural reactions.

## Output

```
SOURCE  "Why I stopped buying bread" (podcast, 38 min)
FOUND   3 moments, 4 how-tos, 6 numbers, 2 opinions, 3 fixes, 5 lines

PAGE    "Sourdough starter guide": the full method + the timings sheet  (to build)

TUE  REEL      Opinion   "Supermarket sourdough isn't sourdough."        clip at 12:40
THU  REEL      Moment    The starter I killed twice, and what saved the third
SAT  CAROUSEL  How-to    Your starter in 7 days                          ask: Comment STARTER -> page
DAILY STORIES  the 5 lines, one a day, link sticker to the page
```

Then draft the posts one by one when the user asks, with `reel-script`, `carousel-post` or
`instagram-caption`, so each gets its own angle and voice.
