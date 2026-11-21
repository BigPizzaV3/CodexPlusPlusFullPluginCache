---
name: ad-from-website
description: Make a first ad for a business from its website address. Use when the user gives a website or domain and asks for an ad, a video, a post visual or a product shot for that business, for example "make an ad for my shop, here is the site", and no brand profile is saved yet or the site is a different brand from the one saved.
---

# Make an ad from a website

Use this skill to go from a website address to a finished ad in one conversation.
Explicit instructions from the user always take priority over this skill, including the format, length, size,
product and wording they name.

## What you need from the user
- The website address. If they gave none, ask for it, or for a one-line description of what they sell.
- What kind of ad they want: an image or a video, and where it will run. If they did not say, ask one short
  question with two or three options (for example a square Instagram image, or a 15 second vertical video).

## Steps
1. Call `get_brand`. It is free and changes nothing. If the saved brand is already this website's business, skip
   to step 4.
2. Call `draft_brand` with the `domain` and `save` set to false. Show the user the drafted name, what it sells and
   the main products, and ask whether it is the right business. A domain can belong to a different company with a
   similar name; never assume it matched, and spend no credits until the user confirms.
3. When the user confirms, call `draft_brand` again with `save` set to true. If it is wrong, ask for the correct
   address or a short description and draft again. When the account already holds other brands, call `list_brands`
   and `use_brand` so the new one is the active brand before anything renders.
4. Call `plan_ad` with the brand, the product the user named (or the main product from the profile) and the
   format. For a video, pass the length the user asked for in `durationSeconds`; if they named none, ask.
5. Show the user the concept in a few lines: the hook, what is on screen and the headline. Ask for a yes before
   rendering, since rendering uses credits.
6. Render: an image goes to `generate_image`, a video goes to `render_ad` with the full `plan_ad` output as
   `creative`. A video takes a few minutes; call `get_job` until it is done, without asking the user to wait.
7. Show the finished file with its link.

## Output
The finished ad, one line on the idea behind it, and two next steps the user can send back as plain sentences, for
example "Make a vertical version" or "Schedule it for tomorrow at 9am".

## Do not
- Do not render before the user confirmed the business and the concept.
- Do not invent prices, discounts, claims or reviews the website does not state. Ask the user for any fact you need.
- Do not put text, a logo card or captions on a video unless the user asked for them.
