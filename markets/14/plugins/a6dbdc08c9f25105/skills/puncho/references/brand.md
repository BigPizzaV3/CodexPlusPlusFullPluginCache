## Palettes: pick one per concept

A brand can have several named palettes ("Main", "Hot", "Warm"), each with a
note on when to use it. `get_generation_context` lists them under
`brandKit.palettes`. For every concept, name one in `palette`, **exactly as
written**, chosen by its note for that concept's moment and reader. Leave it
out to draw in the default. The design is made in the one you name.

Spread a batch across palettes when the notes allow it: a palette is a test
dimension like shape, and five concepts in one palette test nothing about
colour. **Never name a palette that is not in the list.** A name that is not in
the list is dropped, the concept is drawn in the default, and `store_specs`
warns you.

**Making palettes.** You may make or change one with `save_palette`, the same
way as the website's colours: propose, wait for a yes, then save exactly what
was agreed. Claude Code asks the human again before it runs.

- **Colours come from evidence, never taste:** `product_colours` on a product
  shot (a palette per product is the usual reason), `read_site_brand`, or the
  human's own words. Say where each colour came from, and flag any you had to
  adjust for contrast.
- **Every palette gets a `usage` line** saying when to use it. That line is how
  you pick one for each concept later.
- **A new palette needs accent, ink and paper.** Never leave one out to be
  filled for you.
- Choosing the default palette and deleting one stay on the board.

## The brand's look, from its website

A project's colours, fonts and logo can be read off the brand's website. It is
an option, not a step: use it when the brand kit is empty or the human asks.

1. `read_site_brand` reads the site (the project's landing page unless the
   human names another) and **writes nothing**. It returns the site's title and
   address, the colours it leans on with their CSS names, fonts matched to the
   library, and logo candidates.
2. **Show the human what it found and ask.** Lead with the title and address:
   some sites are not the brand's, and `mentionsProject: false` is a reason to
   ask before anything else. Then the suggested accent, ink and paper, the fonts,
   and which logo candidate looks like theirs. Sponsors' logos are often named
   "logo" too.
3. Only after they answer, `apply_site_brand` with exactly what they chose.
   Claude Code asks them again before it runs. It sets the **default**
   palette's colours; the other palettes are left alone. If they say "not this site" or
   "not those colours", stop; do not try the next candidate on your own.

Never apply a suggestion because it looks right. A model choosing a brand's
colours is inventing its identity, the same reason no tool answers the voice
setup. Fonts marked `own-file` or `google` cannot be installed from here: the
human uploads the brand's licensed files on the board.

## Starting a project from its website

"We're starting a new project, here's the link" is a request to do the
setting-up work a human would otherwise do by hand. Do all of the reading at
once, then ask once.

1. `create_project` with the name and the website. If the name is not said,
   take it from the site's title after reading, and ask only if that is unclear.
   If a project with that name or website exists, it is refused: ask whether
   they meant that one.
2. `read_site_brand` and `read_site_content` for the new project. Then **look at
   every image** you might propose, and the product photos, with
   `view_site_image` (the logo candidates too). Nothing is stored by looking.
   Drop what is not the brand's own: stock filler, a sponsor's or partner's
   material, people photographed for something else, near-duplicates.
3. **One proposal, one message.** Lead with the site's title and address (is it
   theirs?). Then, numbered so they can answer by number:
   - colours: the suggested accent, ink, paper and secondary, with the CSS names
     that justify each;
   - fonts: heading and body, and any the site uses that need their own files;
   - the logo candidate that looks like theirs;
   - key visuals worth keeping, each described in a few words;
   - products, with name and price as the store gives them;
   - the pages whose words are the brand talking (about, story, the home page's
     own copy, a programme or product description), and who each addresses;
   - what the brand sells, PRODUCT or EVENT, if it is not already said.
   Recommend; never decide. "All of it" is a fine answer for them to give.
4. After they answer: `apply_site_brand` with exactly the colours, fonts, logo
   and `images` they kept (Claude Code asks them again), and
   `add_site_voice_samples` with the pages they kept. Copy products' names,
   prices, pages and details from the reading unchanged. Never retype page copy
   into `add_voice_samples`: a sample a model rewrote is the model's voice.
5. **Then say what is left for them**, plainly, because none of it is yours:
   - check the palette on the board and anything `look.missing` still lists;
   - the **voice setup** in the Voice frame, about five minutes (set what it
     sells first, in Settings, if you did not), **only when no voice samples
     were kept**. If they kept pages from the site, the voice is read from the
     brand's own words; do not ask for the setup, now or in later reports;
   - the Facebook Page, Instagram account and ad account in Settings;
   - product shots the site did not offer, uploaded on the board.

**Fixing and checking the brand's material:**

- **Pasted SVG markup** (a logo copied from the site's code) goes in with
  `add_brand_asset`'s `svg`, exactly as pasted. Never retype, shorten or
  recolour it. If they want a white version for dark grounds, ask them to paste
  that version.
- **A wrong asset** (an icon saved as the logo, a duplicate, the wrong product)
  is removed with `remove_brand_asset`. Name the asset in your message, get a
  yes, then remove it. Claude Code asks them again.
- **"Is everything in place?"** gets `get_project_status`. It needs no brief.
  Report what is missing and whose job each piece is; never guess at a state
  you did not read.

A thin reading is a reading, not a failure: some sites draw everything with
scripts or keep products off structured data. Say what was missing and that it
can be added on the board. Do not try other sites on your own.
