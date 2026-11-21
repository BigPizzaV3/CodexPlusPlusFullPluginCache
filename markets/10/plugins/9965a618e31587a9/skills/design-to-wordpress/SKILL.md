---
name: design-to-wordpress
description: Turn a design idea, mockup description, moodboard or brand brief into a WordPress-ready website in UiChemy, built to export to Elementor or Gutenberg. Use when the user asks to turn a design into a WordPress site, build a site that looks like a style or reference they describe, or go from design to Elementor or Gutenberg.
---

Use this skill when the user starts from a look (a style, a moodboard, a description of a design, images they supplied) and wants it as an editable WordPress site.

This plugin cannot read a Figma file or open another website. It works from what the user writes or attaches in this chat. If they need a Figma file converted, say so in one line and offer to rebuild the design from their description instead.

Steps:
1. Gather from the message: business, pages, mood, colours, fonts and any images. Ask one batched question only if the business type or name is missing. State the choices you make for the rest.
2. Follow the `build-site-from-brief` skill to create the project. Turn the look into hex colours, a heading font and a body font, and choose layouts that fit the described style.
3. Run `uichemy_validate` and `uichemy_check_responsive` and fix what they report.
4. Ask which builder the user wants, Elementor or Gutenberg, then follow the `export-to-wordpress` skill to mark the project exported.
5. Tell the user what was built, what style choices you made, and the next step: pull it into their WordPress site with the UiChemy WordPress plugin, or follow `deploy-to-own-wordpress` if they give a site address.

Rules:
- Do not copy another company's copy, logo or images. Use content the user owns or has the right to use.
- Use only image URLs the user supplied or that `uichemy_upload_image` returned.
- Say before you create the project that a new project will appear in their UiChemy account.
