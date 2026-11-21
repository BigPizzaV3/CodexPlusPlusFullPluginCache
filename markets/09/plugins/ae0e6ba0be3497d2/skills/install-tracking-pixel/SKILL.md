---
name: install-tracking-pixel
description: Put the user's ad platform pixels on their website and check which ones are installed. Use when the user asks to install or add a Meta Pixel, TikTok Pixel, Google tag, LinkedIn Insight Tag, or a Reddit, Pinterest, X or Snap pixel, asks whether their pixel is installed or working, or needs a pixel before running conversion ads.
---

# Install a tracking pixel

Use this skill to get an ad platform's pixel onto the user's website and prove it is there. Explicit instructions from
the user always take priority over this skill, including the site, platform and pixel they name.

## What is on the site now (read only)
Call `list_tracking_tags`. It reads the live website the way a browser loads it and lists every pixel and Tag
Manager container it finds, with their ids. If it says the page could not be read, that is not the same as "no
pixels": say so.

## Get the pixel id
- Meta: call `list_meta_pixels`. A pixel that has never fired is not installed. If there is none, `create_meta_pixel`
  makes one; say first that Meta allows one pixel per ad account and that a pixel cannot be deleted.
- TikTok: call `list_tiktok_ads_pixels`, or `create_tiktok_ads_pixel` if there is none.
- Any other platform: ask the user for the pixel id. Never invent one.

## Install it
Call `install_tracking_tag` with the pixel. How it lands depends on the site connection:
- Google Tag Manager: the tag is staged as a draft. Publishing puts it live on the website, so show what will be
  published and get the user's yes before calling it again with `publish` set to true.
- Wix: the tag goes live straight away.
- Webflow, WordPress, Shopify, or no site connection: the reply gives the code and exactly where to paste it. Pass
  that on to the user as written.

## Check it
After it is live, call `list_tracking_tags` again and confirm the pixel id is on the page. For Meta,
`list_meta_pixels` shows when the pixel last fired once someone has visited the site.

## Credits
Installing and checking pixels uses no Hermoso credits.

## Do not
- Do not publish a Tag Manager container without the user's yes.
- Do not say a pixel is installed unless `list_tracking_tags` found it on the page.
