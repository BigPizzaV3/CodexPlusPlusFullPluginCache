---
name: edit-page
description: "Change the copy, sections, animations or blog posts of an existing Beste site, saving to the draft and publishing only when the person says so. Use when the person wants to edit, update or fix a site they already have on Beste."
---

Edit an existing Beste site.

### Your first message

Two lines, no jargon. Something like:

    **Let's edit your site.**

    Tell me what you want changed, or I can walk you through it.

Then the first question. No preamble, no recap.

Use your question tool for every choice so the person picks rather than types. A numbered list is the
fallback, not the plan. One question per message, and ask a real question rather
than a keyword.

1. list_websites. One site? Use it. Several? Ask which, numbered, one line each.
   If the person named a site when they started, match it and do not ask again.
2. list_pages. Ask which page, numbered, unless they already said.
3. open_preview with the websiteId and that page's slug, once, always, and
   before the first change. In a chat that shows apps it opens the draft next to
   the conversation and follows every change, so the person sees each edit land.
   Elsewhere it only returns the Studio link; carry on either way and do not
   open it again.
4. get_page_markdown for that page. Read it before touching anything: the
   outline carries the sectionId you will need.
5. Ask what should change, if they have not said.
6. get_section on the section you mean, so your patch matches the shape that is
   already stored.
7. update_section with only the fields that change. It merges, so leave the rest
   alone.
8. get_page_markdown again and compare against what they asked for.
9. Tell them what changed, and that it is saved to the draft.

**Never publish on your own.** Not after a fix, not after a good one, not at the
end of a session that went well. This site is already live: people are reading it
now, and everything you write goes to a draft that nobody sees until somebody
decides otherwise. That decision is theirs.

So: finish the change, say it is in the draft, and offer to put it live in the
same breath. Then stop. If they say yes, publish and pass their words as "asked".
If they say nothing, nothing is published, and that is the correct outcome, not
an unfinished one.

Wanting to be helpful is the whole trap here. The helpful act is the offer.

Do not add a new section when the existing one only needs different words. Style
is deliberately narrow: padding (padding.py, padding.containerMaxWidth), invert,
background colour, a background photograph at style.colors.backgroundMedia with
its overlay, and the entrance animation. Everything else is rejected on purpose,
and the rejection lists what it would have taken.

**Animations have their own tools, and asking for them is common.** "Make the
animations faster", "turn them off", "make everything slide in from the right":
call get_animations first, which reports what each section does now and carries
the exact choices the builder offers, then put them to the person by name (Slide
Right, Very Fast) and write the answer with set_animations. It changes a page,
several pages or the whole site in one call. Never invent an animation name or a
number of seconds; both come from get_animations.

A rejection is never a reason to offer to change Beste's own source code. If
something cannot be done, say what can: another way to get the same result from
inside the site, or that the person can do it in the builder.

If the outline marks a section [shared], it is the site navbar or footer and
editing it changes every page. That is usually what you want for navigation, so
say so rather than trying to make a per-page copy.

Any link to another page of this site is an internal link carrying that page's
id, never a URL. list_pages gives you the ids.

Asked what images the site has? list_images answers it: address, name, type,
size, and the prompt if it was generated. Do not open the files. They are things
to point at, not things to read, and a library runs to hundreds.

Asked for a blog post? That is create_post, not create_page: a post carries its
own summary, author and date, blog list sections find it on their own, and it
stays off the live site until published. It needs a site that has been published
at least once; if this one never has, publish it first and say why. Write the article as Markdown and pass
it as the post body; do not assemble it out of sections. list_posts shows what is
already there, write_post_body rewrites one, update_post publishes it.
