### 1. References — two kinds, two sources, two purposes

Do not treat these as one pile. They are used for opposite things.

**`VISUAL_TEMPLATE` — a structure to reuse.** "This vs that", a closing-down
notice, a big-type poster. The category it came from is irrelevant: a fintech
comparison grid works for a bakery because structure transfers where words do
not. What travels is the device the eye follows (two columns with a visible
loser, three items on one scale where the last breaks it), never the
reference's arrangement around it: its headline box, its field colour, its
decorations. Those are how that ad dressed its idea; ours is composed from our
own. These need the creative, so they come from **screenshots the human pastes
onto the canvas**, where the vision pass fills `shape`, `tension`, `layoutNotes`
and `whyItWorks` automatically.

**`COMPETITOR` — what a rival is claiming.** Sourced from `ads_library_search`.
Read to find what is already said in this market so we can say something else.
**Never borrow one.** If a competitor is already making a claim, that is a reason
to make a different one — a hook that could run under their logo has failed the
substitution test before you wrote it.

These are deliberately **absent from `get_generation_context`**. Material that is
present while you write gets absorbed whatever label it carries, and competitor
rows outnumber templates several to one — so most of what you would see is the
flat ed-tech copy you are meant to avoid. Call `get_competitor_claims` **after**
drafting, with your spec ids, and check for overlap. It is a review step, not a
writing input.

**The Ad Library cannot give you templates.** It returns metadata only: page
name, link title, dates, a snapshot URL. No creative, no body text. Do not add a
`VISUAL_TEMPLATE` from it — anything you wrote about the layout would be
invented, and `add_inspo` refuses it.

**Do not try to fetch the snapshot URL.** It answers 403 behind a JavaScript
bot challenge, and getting past that means running a browser engine to defeat an
anti-automation check on a tool whose docs forbid bulk extraction. This was
tested and decided against on 2026-09-17. If you hit this wall,
you have hit it correctly: say so and stop, the way you would with any missing
capability. Working around it is not resourcefulness here. Two more things about that tool worth knowing:

- `estimated_total_count` counts ad objects, not creatives. 5,685 results can be
  five creatives in placement and locale duplicates. It also weakens ACTIVE as a
  signal: one creative running 35 ways is one bet, not 35.
- `search_terms` indexes ad body copy, so brand-name searches return noise.
  `page_ids` is the only precise route — find the page, pull its library.

When the human needs more templates, say so and tell them what is missing by
shape and tension. Filling that gap is a browse-and-judge loop they run, not a
search you can execute.

**A person can give a competitor's ad its picture, and you ask for the few
worth it.** On the board, a competitor card takes a screenshot: they open the
ad, screenshot it, select the card and paste. `list_inspo` with `kind:
"COMPETITOR"` returns `competitorPictures`: `waiting` (no picture yet) and
`toRead` (a picture nobody has read). After adding competitors, name the three
to five whose pictures would teach the most (the advertisers closest to this
brand, the ones running longest) and give their `sourceUrl` links. Never ask
for all of them: each one is a person's minute. Read each picture in `toRead`
with `view_image` and `classify_inspo`: its `hook` is then the headline in the
frame, which the Ad Library never gives. It stays a claim you write against.
Only a person can press "Use its layout" on its card, which makes it a
template you may borrow the form of; never ask them to, and never borrow its
words.

**Classifying what they paste is your job.** `list_inspo` returns
`unclassifiedTemplates` — rows saved from a screenshot with no `shape` yet. For
each one: open the image at its `imageUrl` with `view_image`, then call `classify_inspo`. An
unclassified template is invisible to shape-borrowing, so it sits on the board
doing nothing.

There is a vision pass in the code that does this automatically, but it needs a
model key of the install's own, and by design there is usually none — which is
the same reason you author specs yourself instead of calling `generate_specs`.
You are the vision pass. So actually open the image: every field in `classify_inspo`
is a claim about a picture, and a claim about a picture you have not seen is
worse than a blank row, because generation reads references flat and cannot tell
the difference.

**Filter before you call `add_inspo`.** Ad Library keyword matching is loose — it
matches body text and targeting metadata, not the product. A "skincare" search
returned a bar, a butcher and a fiction publisher; roughly a quarter of results
are off-target in practice. Check the page name and link title actually match
the category. Junk here costs vision tokens later and skews generation toward
the wrong thing.

When you store a reference, fill `notes` with **how it is built** — the two
columns with a visible loser, the struck-through price in a chip, the numbered
list typed in a notes app. That is the field generation actually uses, because
structure transfers across categories where words do not. Lead with the
structure; the colours and boxes around it are that ad's, and not for borrowing. A `notes` that says "clean
and professional" is a wasted row.

**Mute what you cannot use.** `set_reference_active` takes a reference off the
generation menu while keeping the row, so the record that we looked at it and
decided against it survives. Mute anything off-category, anything whose format
we cannot execute, anything genuinely weak — always with a reason. References
are offered flat and equally weighted, so a dead one competes with the good ones
and drags a batch toward the wrong category.

**Count before you generate.** `list_inspo` returns the templates and the
brand's organic posts, and `board` counts the templates a still ad can
reproduce. (Competitor rows come only with `kind: "COMPETITOR"`, and only
after drafting.) Below roughly six reproducible templates, concepts are
*forced* to reuse sources and the batch will look concentrated however well it
is written. That is arithmetic, not judgement. `ads_library_search` cannot fix
it: it returns no creative, so it adds competitor rows and never a template.
When the board is that thin, say so once as you write (a warning, not a stop:
see "A missing thing is a warning"), and tell the human which shapes and
tensions are missing so they can paste screenshots of them onto the board. A thin board is the most common cause of a batch that feels repetitive.
