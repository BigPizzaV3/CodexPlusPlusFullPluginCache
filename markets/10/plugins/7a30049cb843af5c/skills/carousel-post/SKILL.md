---
name: carousel-post
description: Plan and build an Instagram carousel (a cover that makes people swipe, one point per slide, a summary worth saving, one ask), check each slide's crop with Saypage's post preview, and publish it with Saypage when the user asks. Use for requests like "make slides from this", "I want a multi-image post", "carousel for my recipe", or when an idea with steps, a list or a comparison would not fit in one image.
---

# Carousel post

Pick a carousel when people will want to come back to the content: a recipe, a method in
steps, a comparison, a checklist, a before and after. Each swipe tells Instagram the post
is holding attention, and Instagram may show the post again, opening on slide 2, to
people who scrolled past it: slide 2 needs its own pull.

A single surprising claim, or anything that has to be seen moving, works better filmed:
point the user to `reel-script` instead.

## 1. Plan the slides

Aim for five to ten. Saypage publishes up to 10 images per post (the Instagram app takes
20, which very few ideas fill).

- **Slide 1, the cover**: a promise of eight words at most, big enough to read in the grid.
- **Slide 2**: the reason to care, in a sentence. Someone may see this slide first.
- **The middle**: one point each, a short headline and no more than about 30 words below
  it. When the text runs longer, give it a second slide.
- **Second to last**: everything on one slide, the version people screenshot or save.
- **Last**: a single action: save, send to a friend, or comment a keyword.

Small touches that help: a "4/8" counter so people know how far they are, and the handle
in a corner of every slide, since screenshots get shared without the caption. Use only the
quantities, prices, steps and results the user gave.

Before any image exists, show the copy as a numbered list and let the user change it.

## 2. Size and layout

- **1080×1350 px (4:5)** for every slide. It is the tallest feed format; Saypage crops feed
  images outside 4:5 to 1.91:1, and Instagram gives every slide the first one's shape.
- The profile grid shows posts in a 3:4 frame, which shaves a little off each side of a 4:5
  image: leave at least 60 px between the cover's text and its left and right edges.
- On a phone the slide shrinks to about a third: keep text at 40 px or more. One accent
  color, and the user's own fonts and colors when they have a brand.
- Prepare one alt text per slide (`alt_texts`, in slide order).

## 3. Make the images

- **With a shell** (assistants that can run commands): one HTML section per slide at 1080×1350 px,
  rendered to PNG or JPEG with headless Chrome or whatever is installed, then each file
  uploaded with `start_image_upload` and `confirm_image_upload`.
- **In chat apps**: the user designs the slides in their usual tool (or picks photos) and
  adds them through the link from `request_upload_link`; `list_images` then gives each
  one's reference.
- JPEG, PNG or WebP, up to 5 MB each.

## 4. Check, then publish if asked

1. `preview_instagram_post` with the slides in order, and look at each one as Instagram
   will receive it. A cut headline or face: change `fit`, or use `pad`.
2. Write the caption with `instagram-caption`. On a carousel the caption's first line does
   the hooking, because the cover has only a few words.
3. Publishing needs `can_publish_posts` in `get_account`; it is optional and off by
   default. With it on: `prepare_instagram_post` (`kind: "feed"`, images, caption,
   `alt_texts`), show the user the slides and final caption, and call
   `publish_instagram_post` once they say go. Otherwise the user posts from the app.
4. When the last slide asks for a keyword, set up the automation that answers it (the
   `saypage` skill), with the user's approval.

## Output

```
CAROUSEL  ·  7 slides  ·  1080×1350

1  COVER    Sourdough in 5 steps
2  WHY      No stand mixer, no fancy flour, 24 hours start to finish.
3           1. Feed the starter the night before
...
6  ALL-IN-ONE  The 5 steps on one slide
7  ASK      Comment BREAD and I'll send you the printable recipe.

Caption: hook in the first line, one ask, 3 hashtags (instagram-caption)
```
