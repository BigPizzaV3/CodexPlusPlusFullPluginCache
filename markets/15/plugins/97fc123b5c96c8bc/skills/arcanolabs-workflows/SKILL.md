---
name: arcanolabs-workflows
description: How to drive ArcanoLabs from a conversation — read before the first ArcanoLabs tool call. Covers which tool to reach for in Scrybe, blog content, images, SEO and CRM, what costs credits, and the three things that always ask first.
---

# ArcanoLabs workflows

ArcanoLabs acts on the signed-in person's own account. Reads are free and can be
made freely. Generation spends credits from their balance, and three kinds of
call change something they cannot quietly undo. Orient first, then act.

## Orient before you act

Start from a list, not a guess. `list_story_books`, `list_posts`,
`list_mini_lessons`, `list_decks`, `list_crm_records` and `list_images` each
return ids; almost every other tool needs one of those ids and will fail on an
invented one. When the person names a book, a post or a contact in words, find
it in a list first and use the id you got back.

`check_credits` with no arguments returns their balance and the full price
list. Call it before proposing anything that generates, so the cost is on the
table before the spend.

## Scrybe — books

Scrybe is the writing studio. It was called StoryForge, and some tool names
still read `story` for backward compatibility; say Scrybe to the person.

A book has a Story Bible (characters, places, lore — `get_story_bible`,
`upsert_story_entity`), chapters (`list_chapters`, `create_chapters`,
`arrange_chapters`) and fragments, which are the paragraphs and scenes inside a
chapter (`get_chapter_fragments`, `create_fragments`, `rewrite_fragments`,
`move_fragment`). `read_book` gives the manuscript; `get_story_stats` gives
word counts and progress.

Before rewriting anything, read the surrounding fragments. Scrybe keeps
history (`get_fragment_history`, `revert_fragments`), and `restore_fragments`
brings deleted ones back — but a rewrite that ignores the voice of the chapter
around it is work the writer has to undo by hand.

## Scripts, voices and the Acting Studio

A chapter can be set down as a screenplay (`set_down_screenplay`) and prose can
be turned into speakable lines (`convert_prose_to_lines`); `list_character_lines`
reads back who says what. A manuscript that already exists comes in through
`import_manuscript` rather than being retyped.

The studio itself is a scene at a time: `open_studio_project`,
`prepare_studio_scene`, `list_scenes` and `update_scene`, with
`export_actor_packet` for what a performer needs. Casting is
`search_studio_voice_library` across the provider's whole catalogue,
`add_studio_library_voice` to keep one, then `cast_studio_character`.

**You cannot authorize a voice.** `list_studio_voice_authorizations` reads them
and there is deliberately no tool to grant one: a person listens inside
ArcanoLabs and approves it there. Do not offer to do it from the conversation.

Scene art comes in the way uploads do — `open_scene_art_kit` returns a link the
person opens in a browser, `check_scene_art_kit` says which slots are filled,
`list_scene_art_kits` shows the kits already open. No image bytes pass through
the conversation.

## Blog content

The honest order is plan, draft, score, then publish:
`plan_posts` stores a brief, `generate_blog_post` drafts against it,
`score_article_draft` checks it against the account's Brand Wizard voice for
free, and `publish_to_wordpress` puts it on the live site.

`get_brand_wizard` and `get_brand_profile` tell you how this account's brand
actually speaks. Read one before drafting; the alternative is content in a
voice the person then has to rewrite. An account can hold several brands, so
confirm which one a post is for rather than assuming the default.

## Images

ArcanoLabs cannot receive file bytes through ChatGPT — no MCP client can pass
them. So there are two paths and neither is "send me the picture":

- Reuse what they have: `search_images` / `list_images`, then `get_image_url`.
  Prefer this. It is free and it keeps a brand looking like itself.
- Generate: `generate_image_prompt` then `generate_images`. Both cost credits.
- Let them upload: `create_image_handoff` returns a short-lived link they open
  in a browser; `check_image_handoff` tells you when the file arrived.

## SEO and CRM

`list_search_opportunities` finds underserved searches for a domain the account
has connected through Google Search Console; `check_ranking_watch` reports
drops against that site's own baseline. Both are free and both only cover
domains the person owns.

CRM tools take an `entity` argument — contact, company, deal, activity, note or
pipeline — rather than one tool per kind. `search_crm` and `list_crm_records`
read; `create_crm_record`, `update_crm_record` and `move_crm_deal` write.

## Funnels and automations

`list_funnels`, `get_funnel` and `get_funnel_report` read; `create_funnel`,
`draft_funnel_copy`, `set_funnel_sequence` and `preview_funnel_sequence` build
one. A campaign stays a draft until `publish_funnel`, and `enable_automation` /
`enable_funnel_sequence` start something that will send on its own schedule —
all three belong in the list below.

## What costs credits

Anything that generates: articles, outlines, image prompts, images, voice
samples, mini lessons and video renders. Each tool's description names its
price, `check_credits` is authoritative, and many accept `dryRun: true` to
return the projected cost without charging. Nothing is charged unless the work
is delivered. Credits are bought in ArcanoLabs; there is nothing to buy here.

## What always asks first

Say what will happen and wait for a plain yes, every time, even when the person
has been saying yes all conversation:

- **Publishing.** `publish_to_wordpress` puts words on a live site under their
  name. `publish_mini_lesson_to_archive` and
  `publish_mini_lesson_to_youtube` make something public, and the YouTube one
  also deletes the copy ArcanoLabs was hosting.
- **Scheduling.** `schedule_posts` commits a run of articles to be written,
  charged and published on dates nobody will be watching.
- **Anything that starts sending.** `publish_funnel`, `enable_funnel_sequence`
  and `enable_automation` put a campaign in front of a real audience on a
  schedule. Consent for that audience is the person's responsibility, not a
  thing to assume.
- **Deletes with no way back.** `delete_crm_record` (the CRM has no trash),
  `delete_image`, `delete_book_template`, `delete_console_preset`,
  `remove_story_entity`, `discard_mini_lesson_plan`.

Never batch one of these behind another action. If a request would trigger
several, name them all and get one answer per publish or delete.

## When a call fails

The errors are written to be read: an expired sign-in says to reconnect, and
running out of credits says what the call needed. Pass that along as it is
rather than retrying. A tool that returns `PROVIDER_NOT_CONFIGURED` needs
something switched on in the person's ArcanoLabs account — tell them which
feature, and stop.

## Links in anything you write

An article, a Mini Lesson or a funnel email links only to pages that exist. Do
not write a URL that did not come back from a tool or from the person. A
confident invented link is the one mistake readers always catch.
