---
name: creative-studio
description: Use when the user wants a marketing, office or e-commerce image made with Creative Studio — recruitment or event posters, sale banners, social posts, product shots, livestream or YouTube thumbnails, greeting cards, ads — or wants templates, a brand kit, or to edit or find an image they made there. Not for text-only writing (captions, slogans, post copy), video, or general illustrations unrelated to marketing or brand work.
---

# Creative Studio

Creative Studio turns a short brief into on-brand images. The user's brand kits (colours, logo, reference images),
uploads and past images live in their Creative Studio account; every tool works on the signed-in user's data only.

## Pick the right tool

| User wants | Tool |
|---|---|
| A new image from a description and/or photos | `creative_clarify` (a format they named → `use_case_id`) |
| What Creative Studio is, how it works, how to start, AI allowance — or a mention with no clear task | `creative_help` |
| Which formats or styles exist, or an id another tool needs | `creative_catalog` |
| See, search or ask for template suggestions with no image round open | `creative_templates`; "Use this template" → `creative_asks` |
| Answer the questions card in chat | `creative_generate` with the card's generate values + answers |
| The suggest step of an open `creative_clarify` round | `creative_suggest_templates`; their own template images → `creative_add_template` |
| Change part of an image (text, colors, an object) | `creative_edit` |
| Redraw a whole finished image — not a local change, that's `creative_edit` | `creative_regenerate` |
| Their images / one image | `creative_library` / `creative_image` |
| Progress of images being created (only when asked) | `creative_job_status` |
| Their brand kits | `creative_brand` |
| Set up a brand kit from a website, or by hand | `creative_brand_extract`; logos they send for the draft → `creative_brand_draft_logo` |
| Save a kit, make it the default, change its images | `creative_brand_save`, `creative_brand_default`, `creative_brand_asset` |
| Delete images / a brand kit | `creative_library_delete` / `creative_brand_delete` (first call only shows a confirm card) |
| Something only the website does | `creative_open_web` |

## Rules

- Pick the tool by what the user asks: only a request to make a new image goes to `creative_clarify` or
  `creative_asks`; never turn a question or an unrelated message into an image.
- Creative Studio only makes images. Text alone (captions, slogans, post copy), video, or general art and illustrations
  are not for its tools — answer those without calling any Creative Studio tool.
- Always call a tool for anything about formats, templates, the user's images or brand kits — never guess.
- Pass `locale` (vi or en) = the language of the user's latest message.
- Pass the user's words verbatim as `description` (and as edit or regenerate changes); don't write or expand image
  prompts. Text that should appear on the image comes from their words, in their language.
- Pass every attached photo in `images` and pasted image links in `image_urls`. A ratio, size or orientation they name
  goes in `ratio`; otherwise don't ask about style or ratio — the studio picks defaults per format.
- When the user says how many images they want, pass it as `count`. One run makes at most 4 images (more is capped at 4
  — say so); with 0–1 template that many images, with 2+ templates one image per template.
- Every created image has a short code shown on the cards (e.g. CARD-13). When the user names an image by its code, pass
  it verbatim as `image_code` (`creative_edit`, `creative_image`, `creative_regenerate`).
- The questions card asks only what is missing: let the user answer it, don't invent answers.
- Creating, redrawing or editing an image first returns a confirmation card; nothing is drawn until the user confirms it
  on the card, or agrees to it in chat after it appears (then call again with the card's values and `confirm=true`).
  Delete tools are confirmed by the card's Delete button.
- A questions, templates or confirm card from Creative Studio in this chat is an open request: when the user answers it
  or decides in chat ("create it without a template", "use this one"), continue it with the Creative Studio tool its
  button would call.
- Keep `description` about the image: leave out requests about running the tool (how many images → `count`, skipping
  confirmation, "right now").
- When a card is shown, reply in at most one short sentence; never restate the card.
- If a tool fails, say what failed and offer to try again. Never say Creative Studio made an image it did not make.
- Never ask for passwords, API keys or tokens in chat.
