---
name: profile-review
description: Review an Instagram profile as the screen a visitor decides on in a few seconds (name field, bio, link, pinned posts, highlights, grid), say what works and what to fix first, write the new name line and bio for the user to paste, and make the bio link a Saypage page that keeps the bio's promise. Saypage cannot edit the profile itself. Use for requests like "rewrite my bio", "is my profile any good", "visitors don't follow", "what should my bio link be".
---

# Profile review

Someone who liked one post taps the name, glances at the top of the profile, and either
follows, taps the link, or leaves. Review the profile from that visitor's point of view:
what do they understand, and what can they do next?

## What Saypage can do here

Saypage **cannot edit an Instagram profile**: not the name, the bio, the highlights or the
pinned posts. When the user only wants new bio text, write it, tell them to paste it in
Instagram (Edit profile), and call no Saypage tool for that. What Saypage can do is read
the current bio and link (`get_account`: `bio` and `bio_link`; Instagram shares only the
first link), read the recent posts, and build and host the page the bio links to.

## 1. Look at it

- With Saypage connected: `get_account` for the bio and link, `list_instagram_posts` for
  the last nine to twelve posts (the top of the grid).
- Ask the user for a screenshot of their profile header for what the API does not show: the name
  field, the profile photo, the highlights, the pinned posts, the action buttons.

## 2. Review, item by item

Mark each item **works**, **fix** or **missing**, with a line explaining why. Flattering
the user helps nobody: say plainly what does not work.

1. **Name field** (the bold line, not the @handle): Instagram search matches it, so it
   should hold the words people search ("Léa · Easy vegan recipes", "Maison Lune ·
   Bakery Lyon"), not the name alone.
2. **Bio, first line**: the audience and the benefit, in plain words, rather than a title
   or a string of labels.
3. **Bio, the rest** (150 characters in all): something concrete that earns trust (a
   number, a place, opening hours), then a nudge toward the link.
4. **The link**: a single destination that delivers what the bio announces. A plain
   homepage or a generic list of buttons makes visitors hunt; a page made for them does not.
5. **Pinned posts** (up to three): the one that performed best (check `performance-review`
   or post insights), the one that shows the offer most clearly, and one about the person.
6. **Highlights**: four to six, each named for something a visitor looks for (Menu, Prices,
   Recipes, Reviews, Booking, About). Old or vague ones can go.
7. **Grid**: the first nine thumbnails, at the size of a phone screen. Reel covers chosen on
   purpose, with a few words of text when the topic does not show in the image.
8. **Action buttons** (professional accounts): Book, Order, Reserve, Contact, when they
   fit the business. Set in the app.

## 3. Rewrite, biggest win first

Start with the item that loses the most visitors, and keep the list short: the user makes
each change in the app.

- **Name field**: three options.
- **Bio**: three options, each 150 characters at most, each ending toward the link.
  Count the characters. Run them through `natural-voice`.
- **Pinned posts and highlights**: which posts to pin, which highlights to rename or drop.

## 4. The link page

When the bio link is missing, generic, or a list of links (`get_account` may already
suggest replacing a Linktree), offer to build a Saypage page made for the people the bio
speaks to: the menu and hours for a restaurant, the latest recipes and the shop for a
creator, the offer and booking for a coach. Follow the `saypage` skill (`get_page_guide`
first), publish only with the user's agreement, and remind them to put the page's address
in the bio themselves.

Afterwards, `get_page_stats` shows the visits coming from the bio (`instagram_bio`), which
Instagram's own insights do not count: check it again in a couple of weeks.

## Output

```
PROFILE  ·  @maisonlune.lyon

Name field     fix       "Maison Lune": nothing a search would match
Bio line 1     fix       "Artisan · Passion · Since 2019": no one it speaks to
Bio rest       works     hours and address are there
Link           missing   none
Pinned         fix       nothing pinned
Highlights     works     Menu, Hours, Cakes
Grid           fix       most covers are blurry frames

FIX FIRST
1. Name   "Maison Lune · Boulangerie Lyon 4e"   (2 more options below)
2. Bio    "Sourdough and pastries baked every morning on the Croix-Rousse. Tue-Sun 7am-7pm. Today's menu ↓"
3. Link   a menu and hours page on maisonlune-lyon.saypage.page (build it?)
```
