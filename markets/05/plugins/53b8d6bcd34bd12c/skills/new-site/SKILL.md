---
name: new-site
description: "Build a new website on Beste straight from a brief, without asking about looks, colors or images: create it, open the live preview, fill the sections, then dress and publish it. Use when the person wants a new site, landing page or homepage made with Beste."
---

Build a Beste site

## Start building, not asking

A brief is enough. If the person has already said what the business is, even in
one line, you have everything you need: build now, with no question first and
none during the build. Every question is a pause they did not ask for, and a
site on screen answers more than any question would.

Only if there is no brief at all, say what the site is for in one message, five
lines, warm, no jargon, along these lines, in your own words:

    **Let's make your site.**

    Tell me about it in your own words: what you do, what it is called, who it
    is for. Anything real helps, years, cities, prices, a phone number, names.

    **The more you write, the better the site.** Then I build it straight away.

Then stop and wait for that one answer. It is the only question you ever ask.

### What you decide yourself

Everything else is yours, never a question, and never a list of options with a
recommendation in it:

- **The name**: from the brief. No name given? The short name of what they do,
  which they can change in a word.
- **The language**: the one the brief names, otherwise the one they write in.
- **The look**: from list_looks, the one whose description matches the feel of
  the brief; otherwise Altair. People cannot judge a type scale or a button
  style by a name, and asking only confuses them. Do not mention the choice.
- **The colors**: from list_themes, the one that suits the brief ("warm amber
  tones" means an amber or warm-neutral theme). The same: pick, do not ask.
- **The pages**: what the brief asks for. A one-page site is one page; otherwise
  three, home included.
- **Images**: the placeholders. Generating spends their credits, so it waits for
  them to ask; offer it once, in the hand-over.

Then create_website with the name and language. It opens the live preview next
to the conversation in the same call, so the person watches the site take shape
while you build; do not call open_preview for it again. Where the result says
the preview did not open, call open_preview once. One line back: the address,
and that a custom domain can be attached later.

**Sections first, dressing last.** The moment the site exists, put a hero on the
home page, before anything else, so the preview never sits empty. Then build
every page's sections, navbar and footer. apply_look with the look you picked and
set_theme with the theme you picked come last, once the pages are built: both
restyle every section already on the site, so nothing is lost by waiting, and the
person watches content arrive instead of a blank page changing color.

Asked for six pages, or twenty? Build the best three and say the rest follow as
soon as they have seen it, in one sentence at the end.

The server refuses the fourth page until you have handed the site over, and
publishing on its own does not count as handing over. What counts is finishing:
publish, show them what they have, and stop. Say the fourth page right after
that and it is yours to build immediately, in this same conversation. The limit
is about them seeing something quickly, not about making them start again.

While building: silence, then one line per finished page.

## Build

Pages first: a link needs its target to exist before it can be written.

One shared navbar and one shared footer for the site: set_navbar and set_footer,
once each, no pages argument.

The navbar is written not sticky, and the server keeps it that way however you
ask. Sticky costs a strip of every screen of every page, and nothing in a brief
says which way that should go. Leave it; it is one switch in the builder, and a
reader who wants it will ask.

The logo is a wordmark, not a legal name: use the short form people actually say.
"Hartley Care and Companionship Services" becomes "Hartley Care". Once the navbar
is set, tell them in one line that they can upload their real logo in the
builder, and give them the link from preview_url. Links between pages are internal links carrying the
page id from list_pages, never a URL; an external link to "/about" is rejected
and the rejection carries the value to use instead.

A link to a spot on the same page is an anchor link, { type: "anchor", sectionId:
"<anchor>" }, and the anchor is a name you give the target section: "pricing",
"faq", "contact", "how-it-works", never its id. Set it with add_section { anchor }
when you add the section, or update_section { anchor } later (links on the page
follow a rename). Add the target before the link; a link to an anchor no section
has, or to a section by its id, is rejected.

Anything on more than one page is shared too: add_section with shared: true and
pages: "all", or share_section for one you already made. Copies drift, and the
third page keeps the old phone number.

Per page, per role: search_sections with a plain description, the chosen look's
label as the set argument and the websiteId, get_section_defaults, then add_section changing
only what you mean to change. The set is a preference, not a fence: sections
drawn for it come first, and when another set has the better layout for this
role, take it. It arrives in the site's look like everything else.

### Do not build the same site twice

The catalog holds 708 sections. The honest failure of a generated site is that
it uses eight of them, the top hit for every query, so two sites in the same
trade come out as the same page with different words in it.

Pass websiteId to search_sections. Anything the site already uses comes back
marked and sorted to the bottom, and the answer is to take the one above it.
A section repeated on two pages is a repeat even when the copy differs: the
reader recognises the shape, not the sentence.

Search differently per role, too. "Three services with an icon each" and
"services in a grid" return the same top hit; describing the page you want
("the moment a carer arrives", "prices side by side with what is included")
reaches parts of the catalog a category name never will.

### Pieces

A media slot can hold a photo or a **piece**: a small live UI component drawn in
the page - a chat thread, a booking confirmation, a chart, a phone frame, a
receipt. get_section_defaults tells you which fields of a section accept one.

There are 315, and the demo payloads use about twenty. So a section that ships
with a piece ships the same piece on every site that uses it, and leaving it is
exactly the sameness worth avoiding. Two rules, both easy:

- The default has a piece: keep it only if it suits the business. Otherwise
  search_pieces for one that does, or drop to a photo.
- The default has a photo: a piece is often better, when it can show something
  true about the work. A care company can show the visit card the family gets;
  a restaurant, the reservation; a studio, the invoice.

Whichever you use, rewrite its props in the customer's own words. get_piece
returns the demo values; a piece left on "Dr Amelia Frost" is demo content in
the same way filler copy is.

### How much to build

**Three pages, or one when the brief asks for a one-page site. Four sections on
the home page, three on every other page.**
The navbar and the footer are not sections in this count; they are on every page
already.

These are ceilings, not targets to reach past. A first build is something to look
at and react to, not a finished site, and a long site is harder to react to than
a short one: the person cannot tell you what to change if they are still
scrolling.

Four on the home page is enough to say who this is:

  hero, what they do, the proof or the work, a closing call to action

Three on an inner page: a header, the substance, a way to act.

Everything else waits, and the wait is one message long. Once you have handed the
site over there are no limits at all: more pages, more depth on a page, a blog,
each one sentence from them and yours to build on the spot.

Fill what you add. search_sections tells you how many items a section holds
(collections: features 6); a six-slot block with two items filled reads worse
than a smaller block would. If the brief lists five services, choose a section
that holds five. If it gives one line about the founder, do not stretch it over
three sections to look busy.

Write from the brief, not from the section: a features block with three slots
does not mean the business has three services.

Do not write image URLs. Every photographic slot is filled server-side with one
of four house placeholders, in rotation, whatever the demo payload carried: eight
sections from eight different photo shoots is what makes a page read as a
template even when the words are right. Logos, icons and anything already
uploaded to the site are left alone.

Never download the site's own media to look at it. list_images gives you the
address, the filename, the type and the size of every file, which is what a
question about the library actually needs. Opening them costs a request each and
a real library runs to hundreds.

So the images on the finished site are deliberately not the real ones. Say that
in the hand-over, next to the offer to replace them. Generating images spends
their credits, so offer it, do not decide it.

**Once you start building, stop asking.** No questions between create_website
and the finished site. Someone watching a build does not know whether a question
is a question or a pause, so they wait, and the thing stalls with everyone
waiting for the other.

Missing a fact? Leave that part out and keep going. A section without a phone
number is fine; a section with an invented one is not. Collect what was missing
and say it at the end, in one short list, next to the finished site.

The one exception is something that would produce a wrong site rather than a
thinner one, and that is rare enough that you should assume it is not happening.

## Blog posts

**Not during this build.** No posts, however the brief is worded and however
directly you are asked, including "and write me three articles". The server
refuses create_post until the site has been handed over, so this is not a
judgement call. Say it plainly once, at the end, with the offer: the site goes
live first, and then a post is one sentence away, in this same conversation.

A blog list section on a page is fine and worth adding when the business will
blog; it fills itself from real posts the moment there are any.

What a post is, for later: not a page. create_post writes one, and it carries a
summary, an author, tags and a publish date. A post written as a page is
invisible to every listing on the site and cannot be edited in the builder's post
drawer, so never reach for create_page for an article.

Write the article in Markdown and pass it as "body": headings, lists, tables,
quotes, code and links all survive. Do not build a post out of sections.

create_author first if the post has a byline. Blog list sections (search_sections,
category Blog List) list the real posts by themselves, so put one on a page and
leave its "posts" list alone.

## Another language

add_language, then per page: get_translatable_text, translate the strings
yourself, apply_translation. You are the translator: keep the ids, keep HTML
tags and placeholders exactly, and write as a native speaker in that industry
would, not word for word.

Changing or removing a language is critical. set_default_language and
remove_language answer first with the impact and a confirmation code and change
nothing: tell the user every count in it, in their words, and send the code back
only after they say yes. Removing the default language needs a new default,
and only the user picks it; if they did not name one, ask.

## Finish

get_page_markdown on every page, read it as the customer would, fix what still
reads like sample content, and check the page is the size it should be: four
sections at home, three inside, navbar and footer not counted, every list filled.
Over that, cut rather than keep; a page that got long during the build is the one
thing they cannot fix in a sentence.

Then publish. It returns liveUrl and builderUrl, and those two links are the
whole point of the last message: one to look at what they have, one to change it.

Hand it over in a single message, laid out. This is the one place to spend a
little on presentation, because it is the only screen they will read twice:

    ╭────────────────────────────────────────────╮
    │  Hartley Care is live                      │
    ╰────────────────────────────────────────────╯

    | | |
    |---|---|
    | **See it** | http://hartley-care.beste.co |
    | **Edit it** | http://studio.beste.co/.../home |
    | **Pages** | Home, Visits, Contact |

    Two things I left out, for want of a fact:
    - no phone number on the contact page
    - the founder's name, so the About section speaks for the company instead

    Say the word and I will do any of these now: another page, more on a page
    you have, real photos, or a blog post.

The box holds the name and the state, nothing else. The table holds what they
click. The gaps are what you could not know, not a list of everything you chose
not to build. The last line is an offer, not a menu to read.

Keep the widths sane: the box is drawn to fit its line, not padded to eighty
columns, and links go in the table rather than inside the box where they wrap.

## Publishing

You publish **once**, at the end of this build, as the hand-over. That publish is
expected: it is what makes the links in your last message work.

After it, publishing is theirs and never yours again. If they ask for a change in
this same session, make it, tell them it is saved to the draft, and stop there.
Do not publish it. Not because it is small, not because it is obviously an
improvement, not because you are confident they will want it: none of those is
them asking. The live site is what their customers are reading right now, and a
change that appears on it without anyone deciding is a change nobody can trace.

The server asks you to quote them for exactly this reason. If you cannot say what
they said, ask: one line, and wait.

Everything is a draft until publish. Content is per language. Never set colors,
gradients or shader effects on a section: the theme owns them and the server
rejects them. The only colour decision is the theme, picked by you at the start.

A background photograph is the exception, because it is a picture rather than a
colour scheme: style.colors.backgroundMedia takes enabled, type, src, size,
position and an overlay. Turn the overlay on whenever text sits over the image,
or the headline is unreadable and nobody asked for that. Padding and width are
yours too: padding.py and padding.containerMaxWidth.

### One look, any section

A site has one look: its type scale, button style, badge look, card borders and
motion, written site-wide. apply_look set it from a studio set; get_site
reports it under style. Every section you add takes it on the
way in, whichever set it was drawn for, so mixing sets is not a risk to manage:
a Sirius hero above a Polaris feature reads as one page because both wear the
site's buttons and badges.

**Sections arrive without a badge.** add_section never writes one, not even one
you pass. When the person asks for a badge, add it with update_section.
A badge above every heading is the pattern that makes a generated site read as
generated. Do not bring badges up or offer to add them.

Fonts come with the theme. When the person names a typeface or asks for a
different feel in the type, set_fonts: a curated pairing from list_fonts by id,
or body, heading and code fonts by name. Colors stay with the theme either way.

When the person wants the look changed, change it where it lives: set_appearance
with only the field they named. "Make the headings smaller" is typography
compact, "seal buttons" is buttons, "no card borders" is cardBorder off, "calmer
animations" is sectionAnimation with a slower duration or mediaAnimation with
scroll none. One call rewrites every section still wearing the old value. Never
walk the pages editing sections one by one for a site-wide change, and never
give one section a look of its own to satisfy a site-wide wish.

Entrance animations are yours as well, and they belong to their own tools rather
than to a style patch: get_animations reads what every section does and carries
every type and speed the builder offers, set_animations writes them
across a page or the whole site at once. Leave the site's animations as the
sections ship them unless the person says otherwise.
