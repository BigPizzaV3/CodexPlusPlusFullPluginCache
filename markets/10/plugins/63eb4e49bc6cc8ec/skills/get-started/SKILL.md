---
name: get-started
description: Turn an article link, notes or an idea into a LinkedIn carousel with SlideDrift, then export it or save it as a LinkedIn draft.
---

Use this when someone wants a LinkedIn carousel, or wants to export or schedule a carousel they made in SlideDrift.

1. Ask for the source if it's missing: a public article link, pasted notes, a transcript or a short idea.
2. If the user wants to review the structure first, plan it with `plan_carousel`. Otherwise create it with `create_carousel`. If they name a brand kit, find it with `list_brand_kits` and use it.
3. Before anything that uses credits, shares content or schedules a post, SlideDrift returns a quote or a preview. Tell the user in plain words what will happen and what it costs, and continue only after they confirm.
4. After creating a carousel, share the editor link so the user can review and edit the slides.
5. To export, use `export_carousel` for a PDF, PNG slides or image links. To post, check the connected accounts with `list_social_accounts`, then save a draft with `schedule_social_post`. A draft never publishes; scheduling a post needs the user's explicit confirmation of the account, text and time.
6. To change a carousel after it's made, read it with `get_carousel` (include edit targets), then use the tool for the kind of change: `edit_slide_text` for wording, `style_slide_text` for fonts, sizes and colours, `replace_slide_image` to swap an image for one the user has uploaded, or `arrange_slide` to change the slide's layout, spacing or element order. Each returns a preview; save it only after the user confirms.
7. If the user asks for something SlideDrift can't do, say so plainly.
