# Lahjty ads reference

## Platform specs

| Placement | aspect_ratio | Caption length | Notes |
| --- | --- | --- | --- |
| Instagram feed | 4:5 (or 1:1) | 1 to 3 short lines, then hashtags if the user wants them | The first line must work without "more". |
| Instagram or Facebook story, reel | 9:16 | Very short; the image carries the message | Keep the product in the middle; the top and bottom 15% are covered by app UI. |
| TikTok | 9:16 | One punchy line | Pair with a voiceover (`delivery: "reel_voiceover"`). |
| Snapchat | 9:16 | One line | Casual dialect works best. |
| Facebook feed | 1:1 or 4:5 | 2 to 4 lines | Clear call to action. |
| WhatsApp status | 9:16 | One line | Pass `platform: "whatsapp"`. |
| X (Twitter) | 16:9 or 1:1 | Under 280 characters | Pass `platform: "twitter"`. |

## Dialect defaults by market

| Market hint | Default dialect |
| --- | --- |
| SA | saudi |
| AE | emirati |
| KW, QA, BH, OM | gulf |
| EG | egyptian |
| JO, LB, SY, PS | levantine |
| IQ | iraqi |
| Other Arabic or unknown | ask; classical (Modern Standard Arabic) for formal or pan-Arab brands |

English output takes no dialect. "Arabic and English" means two separate captions, one per language.

## Image prompt recipes by product type

Describe the scene in plain words. The product photo keeps the real product accurate; the prompt sets everything around it.

- **Perfume, oud, cosmetics**: dark marble or warm stone surface, soft side light, gold or deep amber accents, subtle smoke or petals. Luxurious tone.
- **Coffee, tea, dates, food packs**: wooden table, morning light, a cup or serving dish beside the pack, a few beans or dates scattered. Warm, inviting tone.
- **Fashion, abayas, shoes**: clean studio backdrop in a brand color, or an urban lifestyle scene; product large and centered.
- **Electronics, accessories**: minimal desk setup, cool clean light, strong shadow, lots of empty space.
- **Home, candles, decor**: cozy living room corner, soft evening light, plants or textiles in brand colors.
- **Kids and gifts**: bright pastel background, playful props, gift ribbon.
- **Offers and seasons** (Ramadan, Eid, National Day, White Friday): `type: "offer_announcement"`, seasonal props (lanterns, crescents, green and white for Saudi National Day), and the confirmed offer as `overlay_text` only if the user wants text in the image.

Brand colors from the website (`brand_colors`) go into the prompt as plain color names, for example "deep coffee brown and cream".

## Caption formulas

- **Hook, benefit, call to action** for most feed posts.
- **Problem, solution** (`framework: "pas"`) for practical products.
- **Story** (`framework: "story"`) for gifts and heritage brands.
- Put exact must-have phrases (product name, price, code) in `required_keywords`.

## Edit phrasing that works

Pass the user's words directly as `instruction`, adding detail only when it is clearly implied:

- "Make the background plain white and keep the product exactly the same."
- "Make the product larger and centered."
- "Use warmer, softer light."
- "Make a 9:16 story version" (also set `aspect_ratio: "9:16"`).
- "Add our logo in the bottom corner" (upload the logo first and pass `logo_storage_id`).
