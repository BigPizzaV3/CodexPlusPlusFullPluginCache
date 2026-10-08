# In-Frame Text and Typography

16 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Read, or Only Seen

**Also called:** the in-frame text selector, the two questions before the words, who is going to read this  
**What it is:** The card at the head of the `textimg.` shelf. It asks the three questions this shelf's own cards keep asking — **will these words be read or only seen, is the lettering generated or set afterwards, and whose writing system is it** — and hands back a named shortlist for each answer. The axes come from the shelf's `Avoid when:` lines and from the conditions its cards use to send a reader elsewhere. Every card named here is named by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the words in the frame were sized against the device they will be watched on, rather than against the monitor they were designed on.  
**Used for and where it works best:** Answer question one **before you write the prompt and before you open a design tool**, out loud, in one sentence: *these words will be read*, or *these words will only be seen*. That answer decides the whole shelf, because the cards that make lettering survive generation and the cards that make lettering readable are two different populations with almost nothing in common. Question two decides who renders it. Question three decides whether it can be rendered at all. **If the answer to one is "read", the size question is not optional and it is not yours to defer to the edit** — the accessibility rule that owns it is `access.legible_at_size`, it sits in the same file as this shelf, and it is a rule you obey rather than a card you pick.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The text is delivered as a track the platform renders rather than burned into the picture.** There the player owns the size, the shape and the safe area, this card's first axis has no consequence, and `textimg.subtitle_size_in_frame` says so in its own words. Also avoid it where the lettering is the only content — a piece that is entirely type is a design job and this map's second axis will send you out of the shelf on its first answer, which is not guidance, it is a shrug. And **distrust this card most where it is most confident**: its first axis is the question this shelf demonstrably never asks itself, so the map is imposing a discipline on the cards rather than reading one off them, and a reader who finds a card sorted oddly should trust the card.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — Will these words be read, or only seen?**
It is an axis and not a footnote, and the shelf's own shape is the argument for it. Ten cards here specify text in a frame without ever saying how large it is against that frame, and three promise accurate rendered lettering — *exactly as it must appear, including capitalisation* (`textimg.quote_the_string`), *letterforms that hold their shape* (`textimg.carved_not_text`), *lettering that could have existed in the period* (`textimg.period_lettering`) — without saying how the result is checked or by whom. Only two cards in the file carry a size at all, and one of them belongs to the accessibility rules rather than to this shelf. The rule that owns the question states the split in its own `Avoid when:`: it does not apply to *a main title that is meant to be seen rather than read*, and it sends that case to `textimg.typography_as_subject`. **A design object and a caption fail in opposite directions, and nothing else on this shelf separates them.**

**Axis 2 — Is the lettering generated inside the picture, or set afterwards over a clean plate?**
Every internal argument on this shelf is this one, and it only ever runs in one direction: out of generation. *"Passage longer than a few words"* (`textimg.carved_not_text`). *"The design's whole idea is dense text"* (`textimg.short_text_rule`). *"Letterform precision needed; generate only the field"* (`textimg.typography_as_subject`). *"The figures must appear and be verifiable"* (`textimg.numbers_and_dates`). *"Set the wording as a layer, never reroll"* — which arrives from the image-repair procedures, not from this shelf. The governing rule stated elsewhere in this phase is blunter than any of them: **the type is never generated.**

**The `[Edit Overlay Instruction]` label.** A `Prompt:` field that opens with it is never sent to an
image engine as written. On a pure overlay — a caption track, a chart, a lower third — the whole field
is the instruction for the edit and nothing is generated. On a card that also needs a picture under the
text, the words after the label describe the generated plate, and those words, without the label and
without the text to be set, are what the engine receives; the lettering is set in the edit over the
space the plate leaves.

**Axis 3 — Whose writing system is it?**
The condition the shelf repeats most and the one it routes on hardest. *"The exact string is a non-Latin script"* (`textimg.quote_the_string`). *"The period letterform is a script the model cannot spell"* (`textimg.period_lettering`). *"Never generate either script as image content"* (`textimg.two_scripts_one_surface`). *"The glyph itself is never generated"* — cited by id from the kids-content shelf. And `textimg.invented_script` is the mirror of all three: a system built to be **unmistakably not** a real script, because an invented script that resembles a real one is read by people who know that one as a statement about it. Asked last, because it can only be answered once you know whether the words are being read and who is setting them.

---

**The map**

**Axis 1 — read, or only seen**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Read — the words carry information and somebody can check them** (eight) | `textimg.short_text_rule` · `textimg.quote_the_string` · `textimg.numbers_and_dates` · `textimg.repair_not_regenerate` · `textimg.two_scripts_one_surface` · `textimg.subtitle_size_in_frame` · `textimg.subtitling_a_sung_line` · `textimg.text_safe_zone` |
| **Seen — the lettering is a surface, a period, a texture, a composition** (five) | `textimg.carved_not_text` · `textimg.period_lettering` · `textimg.non_latin_script` · `textimg.invented_script` · `textimg.typography_as_subject` |
| **Neither — no words may appear in the generated frame at all** (two) | `textimg.no_watermark_clause` · `textimg.text_safe_zone` |

**Axis 2 — who renders the lettering**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The generator, and it has to survive generation** (four) | `textimg.carved_not_text` · `textimg.quote_the_string` · `textimg.period_lettering` · `textimg.invented_script` |
| **The edit, over a plate composed to receive it** (nine) | `textimg.short_text_rule` · `textimg.text_safe_zone` · `textimg.typography_as_subject` · `textimg.repair_not_regenerate` · `textimg.numbers_and_dates` · `textimg.subtitle_size_in_frame` · `textimg.subtitling_a_sung_line` · `textimg.two_scripts_one_surface` · `textimg.no_watermark_clause` |
| **Neither — rendered as marks with no legible content** (one) | `textimg.non_latin_script` |

**Axis 3 — whose writing system**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Latin, and short enough to come back right** (five) | `textimg.short_text_rule` · `textimg.quote_the_string` · `textimg.numbers_and_dates` · `textimg.typography_as_subject` · `textimg.text_safe_zone` |
| **A real script the model cannot spell** (eight) | `textimg.non_latin_script` · `textimg.two_scripts_one_surface` · `textimg.period_lettering` · `textimg.carved_not_text` · `textimg.subtitle_size_in_frame` · `textimg.subtitling_a_sung_line` · `textimg.text_safe_zone` · `textimg.repair_not_regenerate` |
| **A system that is not a real script at all** (one) | `textimg.invented_script` |
| **None — the frame comes back clean, or goes back to the edit** (two) | `textimg.no_watermark_clause` · `textimg.repair_not_regenerate` |

*A card appears once per axis, except a card that does not depend on that axis's answer: `textimg.text_safe_zone` and `textimg.repair_not_regenerate` work the same in any script and serve words that are read, so each is listed under every answer it serves. The answer is the intersection of the three shortlists, and on this shelf it is normally one or two cards wide.*

---

**The default, and the one against it**

**The most-reached card on this shelf is `textimg.non_latin_script`, and it is not the default.** Four cards send a reader there — the exact-string card, the period-letterform card, the bilingual card, and a kids-content card citing it as an authority. Counted as conditions rather than as edges, those four collapse into one: *the glyphs are not Latin*. **It is the door out of generation, not the thing generation falls back on** — a card reached four times for one reason is an exit.

**The argued default is `textimg.short_text_rule`, with `textimg.no_watermark_clause` on every frame that is not deliberately carrying words.** `textimg.short_text_rule` is the card the generated-lettering block falls to first and by name, and its own text calls it the standard working rule for any image that must carry words. `textimg.no_watermark_clause` earns its place on a stranger ground: it is the only card on this shelf whose `Avoid when:` concedes that the card almost never fails — *it usually costs nothing, which is why it belongs in almost every prompt*. **A card whose own boundary line cannot find a boundary is either a default or a rule wearing a card's clothes**, and this one is a default, because the register where a printed mark is authentic genuinely exists and the card names it.

**The stated runner-up, so the ranking is not silent:** `textimg.text_safe_zone`, and it is the closest thing here to a measured default — three conditions reach it, from three different shelves, and they are genuinely three: *letterform precision is needed so generate only the field*, *compose the quiet area instead of darkening the image afterwards*, and *the frame is composed with title space from the start*. It is second only because it presumes there will be type, which the default does not.

**The one against it is `textimg.invented_script`.** Nothing routes to it. It is the only card on the shelf that treats writing as a system to be designed rather than as a risk to be managed, and it inverts the shelf's entire premise: every other card here is work to make real text survive a model that cannot spell, and this one makes the model's inability into the medium, by building a script that has no correct spelling to fail against. Its cost is stated and it is a real one — it is not a stand-in for a real script the audience should read; a real script is set correctly in the edit layer (`textimg.non_latin_script`). **Its near cousin is `textimg.two_scripts_one_surface`**, which is against the grain in the opposite direction: it doubles the risk deliberately, on the argument that a bilingual audience reading one line and inferring the other is being told which of them the piece is for.

---

**The unasked**

**Eight of the fourteen cards are the target of no pair condition anywhere in the package.** By id:

`textimg.carved_not_text` · `textimg.quote_the_string` · `textimg.period_lettering` · `textimg.numbers_and_dates` · `textimg.no_watermark_clause` · `textimg.two_scripts_one_surface` · `textimg.subtitle_size_in_frame` · `textimg.invented_script`

**And the shape of that list is the finding, twice over.**

First: **every one of the four cards under axis two's first value is on it.** `textimg.carved_not_text`, `textimg.quote_the_string`, `textimg.period_lettering` and `textimg.invented_script` are the whole population of *generate the lettering and make it survive*, and nothing in the package sends a reader to any of them. Every edge on this shelf runs the other way — out of generation, into the edit. **The shelf is a one-way street, and the direction is away from its own craft.** A reader who arrives here by following a pair field will never be told to generate lettering; they will only ever be told to stop. That is probably correct as advice and it is certainly incomplete as a map, because the four cards exist and somebody has to reach them.

Second, and this is the one that matters: **the card that states a size is on the list, and the rule that states the other size is not on this shelf at all.** `textimg.subtitle_size_in_frame` is the only card here carrying a cap height, nothing points at it, and its own `Yields to:` does not point at a card either — it names an authority, the platform's own subtitle renderer. The other half of the question lives in the accessibility rules, in the same file, on a shelf this one cannot route to. So **there is no edge anywhere in the package that carries a size**, and ten cards specify text in a frame without one. That is not ten separate oversights. It is one missing axis, and the pair graph could not have caught it, because the readers who wrote these fields were each holding a still frame and a size question needs a viewing distance.

The card this shelf wants and does not have is the one that says **the frame has a physical size at the far end**: the same two words are a title on a cinema screen and an illegible smudge on a phone in a moving car, and nothing on this shelf changes its advice between those two cases. The nearest thing that exists, `access.legible_at_size`, says it plainly — *judge type on the smallest screen the piece will play on, at arm's length, not on the edit monitor* — and it is a rule on another shelf, so no card here is obliged to have read it.

`textimg.read_or_seen`

---

### Describe Text as Carved Geometry

**Also called:** text as object, lettering as relief, physical lettering  
**What it is:** Describing lettering as a physical thing cut, painted, moulded or stitched into a surface, with depth, tool marks and its own shadow, rather than as text to be read. It controls how the lettering behaves as material; it is not a spelling guarantee.  
**Effect on the audience:** Letterforms that hold their shape. Text described as text drifts into approximate glyphs, while text described as carved stone behaves like stone.  
**Used for and where it works best:** Heritage reconstruction with inscriptions (a non-Latin one carved as texture with no legible signs, per `textimg.non_latin_script`), signage in any period setting, and any image where lettering must survive at large size — surviving generation, which is not being read: where the words must also be read, their size on the screen they are watched on is `access.legible_at_size`'s check. Best in heritage documentary, posters and location plates.  
**Best in:** formats: all — any format that puts a non-Latin script in frame | genres: all
**Avoid when:** It usually still fails for long passages, because the failure scales with character count regardless of how the text is described. The exception is a short inscription of a few words, where the physical description is usually enough — and the returned letters are still read back against the intended ones, with a wrong word set as a layer per `textimg.repair_not_regenerate` rather than rerolled, as `rescue.text_garble` requires.  
**Prompt:** `the word cut into the limestone lintel in deep square-sectioned strokes, chisel marks visible inside the cuts, hard shadow filling each stroke from the light above`  
**Yields to:** `textimg.short_text_rule` — Passage longer than a few words; and `textimg.non_latin_script` — the lettering is a non-Latin script, carved as texture and never as legible signs.  
`textimg.carved_not_text`

### Keep In-Frame Text Short

**Also called:** character budget, word count discipline  
**What it is:** Limiting the text placed inside an image to a few words, and moving anything longer to a layer added afterwards rather than asking the model to render it.  
**Effect on the audience:** Text that comes back correct. Accuracy falls sharply with length, and one wrong letter costs the whole image.  
**Used for and where it works best:** Posters and covers, signage, packaging, and social cards. The standard working rule for any image that must carry words. Short is half of it; the size those words need on the screen they are watched on is `access.legible_at_size`'s check. Best in posters, thumbnails and product work.  
**Best in:** formats: Poster / Static Design, Thumbnail / Social Card, Product Still / Packshot, Commercial / TVC, Title Sequence / Opening Credits, Editorial / Magazine Image, Generated Keyframe Feeding Video, Fine Art Photography, Architectural Photography, Still Life Photography, Travel Photography, Documentary Photography, Abstract Photography, Photojournalism | genres: all  
**Avoid when:** It usually loses a design whose whole idea is dense text. The exception is generating the image without the text and setting the typography afterwards, which is faster than fighting the model and gives full control.  
**Prompt:** `only two words appear in the frame, set large and clear enough to read on the smallest screen the piece will play on; all other copy will be added as a separate layer afterwards`  
**Yields to:** `textimg.typography_as_subject` — The design's whole idea is dense text.  
`textimg.short_text_rule`

### Quote the Exact String

**Also called:** literal text, quoted lettering  
**What it is:** Placing the required text in quotation marks in the prompt, exactly as it must appear, including capitalisation, rather than describing what the sign says.  
**Effect on the audience:** Far higher accuracy. Describing the content produces invented wording; quoting the string gives the model a target to match.  
**Used for and where it works best:** All signage, packaging, titles and any brand-critical lettering. Best in product stills, posters and title design. Quoting governs the spelling, not the size: where the string will be read, it is sized against the smallest screen the piece plays on, per `access.legible_at_size`.  
**Best in:** formats: Poster / Static Design, Product Still / Packshot, Thumbnail / Social Card, Commercial / TVC, Title Sequence / Opening Credits, Editorial / Magazine Image, Generated Keyframe Feeding Video, Fine Art Photography, Architectural Photography, Still Life Photography, Travel Photography, Documentary Photography, Abstract Photography, Photojournalism | genres: all  
**Avoid when:** It usually still drifts on unusual scripts or long strings even when quoted. The exception is a short common-script string, where quoting is reliable enough to trust once the returned string has been read back letter by letter; a wrong one is set as a layer per `textimg.repair_not_regenerate`, never rerolled, as `rescue.text_garble` requires.  
**Prompt:** `the carved sign reads exactly "NINEVEH", in capital letters, nothing else written anywhere in the frame`  
**Yields to:** `textimg.non_latin_script` — The exact string is a non-Latin script.  
`textimg.quote_the_string`

### Non-Latin Script Handling

**Also called:** Arabic, Syriac and cuneiform lettering, script risk  
**What it is:** Treating any non-Latin script as high risk in generated images, and either rendering it as texture without legible content or adding it as a typeset layer afterwards.  
**Effect on the audience:** Avoids the specific failure of plausible-looking but meaningless characters, which is worse than no text because a reader of that script sees nonsense.  
**Used for and where it works best:** **Any frame with a non-Latin script in it, on any subject and any period.** This is a fact about how generators render glyphs, not a fact about heritage: a modern shop sign, a national flag with script on it, a stadium banner, a book cover and a seventh-century BC inscription all fail the same way and take the same remedy. It was tagged for heritage work alone, which meant the advice never surfaced on the modern briefs that need it most. Best in heritage documentary and regional campaign work, and equally in an advert, an anthem or a title card that carries Arabic, Syriac, Aramaic, Hebrew, Persian, Cyrillic, Greek or cuneiform.
**Best in:** formats: **all — any format that puts a non-Latin script in frame**, and that explicitly includes Kids Content, Educational, Explainer, Animated Series, Commercial / TVC, Music Video, Vertical Short-Form and Museum Installation alongside the heritage formats | genres: all
> *This field used to list heritage formats only — the exact mis-tagging the card's own prose describes having fixed. The prose was corrected and the field was not, so the advice still failed to surface on a children's alphabet piece, which is the single brief most likely to put a non-Latin glyph on screen as its subject.*  
**Avoid when:** It usually costs authenticity to leave the script out of a frame that would really have carried it. The exception is showing the inscription as eroded or partly obscured, which is period-truthful and removes the legibility problem.  
**Prompt:** `the tablet carries cuneiform impressions as surface texture, eroded and partly broken, not legible as specific signs; any readable text will be set afterwards`  
`textimg.non_latin_script`

### Text Safe Zone Planned in the Image

**Also called:** copy space, headline zone, clear area  
**What it is:** Composing the image with a deliberately quiet area where type will later be set, correct in size and contrast for the words it must hold on the smallest screen the piece will play on, which `access.legible_at_size` decides.  
**Effect on the audience:** Layouts that work without compromise. A great image with no place for the headline forces either a crop or a text box that damages it.  
**Used for and where it works best:** All poster, cover, thumbnail and advertising work where copy will be added. Best in posters, social cards and campaign work.  
**Best in:** formats: Poster / Static Design, Thumbnail / Social Card, Commercial / TVC, Editorial / Magazine Image, Title Sequence / Opening Credits, Brand Film, Product Still / Packshot, Fine Art Photography, Architectural Photography, Still Life Photography, Travel Photography, Documentary Photography, Abstract Photography, Photojournalism | genres: all  
**Avoid when:** It usually weakens the picture when the quiet area is so large the composition becomes an illustration with a hole in it. The exception is using an existing dark or out-of-focus region as the zone rather than creating emptiness.  
**Prompt:** `compose with the upper third held dark and quiet, free of detail, sized to carry a two-line headline that will be set afterwards`  
`textimg.text_safe_zone`

### Typography as the Subject

**Also called:** type-led image, lettering composition  
**What it is:** Building the image around the letterforms themselves, with the type carrying the composition and the photographic or illustrated content supporting it.  
**Effect on the audience:** The word lands before the picture does. Used well the letterform becomes the image the audience remembers.  
**Used for and where it works best:** Title sequences, album and book covers, campaign key art, and any piece whose idea is verbal rather than pictorial. Best in titles, posters and music work.  
**Best in:** formats: Title Sequence / Opening Credits, Poster / Static Design, Thumbnail / Social Card, Music Video, Editorial / Magazine Image, Commercial / TVC, Brand Film, Fine Art Photography, Architectural Photography, Still Life Photography, Travel Photography, Documentary Photography, Abstract Photography, Photojournalism | genres: all  
**Avoid when:** It usually fails when generated, because type-led work depends on precise letterform control the model does not offer. The exception is generating the imagery and setting the type in a design tool, which is the normal professional route.  
**Prompt:** `generate the background field only, composed to carry large display type across the centre; the lettering itself will be set in a design tool`  
**Yields to:** `textimg.text_safe_zone` — Letterform precision needed; generate only the field.  
`textimg.typography_as_subject`

### Period-Truthful Lettering

**Also called:** era-appropriate type, historical letterform  
**What it is:** Choosing lettering that could have existed in the period and place depicted, in its correct medium, rather than applying a modern typeface to an ancient surface.  
**Effect on the audience:** Nothing breaks the period. A modern grotesque on a clay tablet undoes an otherwise careful reconstruction in one glance.  
**Used for and where it works best:** All heritage and historical work, museum and exhibition pieces, and any reconstruction that will be seen by people who know the period. Best in heritage documentary and exhibition work. Exact historical text comes from a cited, verified reference, never from a generated approximation, and a generated inscription is read back before it is trusted, and one that returns wrong characters is repaired as a layer per `textimg.repair_not_regenerate`, not rerolled (`rescue.text_garble`).  
**Best in:** formats: Heritage / Historical Documentary, Location Sheet / Master Plate, Poster / Static Design, Editorial / Magazine Image, Multi-Screen Installation, Title Sequence / Opening Credits, Generated Keyframe Feeding Video, Fine Art Photography, Architectural Photography, Still Life Photography, Travel Photography, Documentary Photography, Abstract Photography, Photojournalism | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Faith / Biblical Epic, War  
**Avoid when:** It usually reduces legibility for a modern audience, since period letterforms were not designed for today's reader. The exception is using period lettering inside the image and modern type for the caption outside it, that caption sized for the screen it is watched on per `access.legible_at_size`.  
**Prompt:** `the inscription in the letterform of its own period and cut in its own medium, no modern typeface anywhere in the frame`  
**Yields to:** `textimg.non_latin_script` — The period letterform is a script the model cannot spell.  
`textimg.period_lettering`

### Numbers, Dates and Small Detail Text

**Also called:** numerals, labels, fine print  
**What it is:** Treating numerals and small labels as the highest-risk text of all, because they are short enough to look plausible and specific enough to be checked.  
**Effect on the audience:** Prevents the quiet error. A wrong digit on a date or a price passes review and then fails in public.  
**Used for and where it works best:** Product and packaging work, historical dates and inscriptions, sports and score graphics, and any label a viewer could verify. Best in product stills and documentary work. A figure set afterwards for a viewer to verify is read like any caption, so it is sized against the screen it is watched on, per `access.legible_at_size`.  
**Best in:** formats: Product Still / Packshot, Poster / Static Design, Thumbnail / Social Card, Editorial / Magazine Image, Explainer, Heritage / Historical Documentary, Commercial / TVC, Fine Art Photography, Architectural Photography, Still Life Photography, Travel Photography, Documentary Photography, Abstract Photography, Photojournalism | genres: all  
**Avoid when:** It usually costs a little realism to leave a label blank or turned away. The exception is composing so the label is partly out of frame or obscured, which is both safe and natural.  
**Prompt:** `the label is angled away from camera so no numerals are legible; any figures required will be set afterwards`  
**Yields to:** `textimg.repair_not_regenerate` — The figures must appear and be verifiable.  
`textimg.numbers_and_dates`

### Fix Text by Layer, Not by Reroll

**Also called:** text repair, typeset over, layered correction  
**What it is:** When generated lettering comes back wrong, setting the correct text as a layer over the image rather than regenerating and hoping, because the failure repeats.  
**Effect on the audience:** The image is finished in one step instead of twenty. Rerolling for text changes everything else in the frame while rarely fixing the words.  
**Used for and where it works best:** Every time generated text fails, which is most times it is attempted at length. Best in posters, packaging and social work. The corrected layer is then text to be read like any other, sized against the screen it is watched on, per `access.legible_at_size`.  
**Best in:** formats: Poster / Static Design, Thumbnail / Social Card, Product Still / Packshot, Commercial / TVC, Editorial / Magazine Image, Title Sequence / Opening Credits, Fine Art Photography, Architectural Photography, Still Life Photography, Travel Photography, Documentary Photography, Abstract Photography, Photojournalism | genres: all  
**Avoid when:** It usually shows the join when the surface beneath the text has strong perspective or texture that the flat layer cannot follow. The exception is matching the layer to the surface with a warp and a light grain, which is quicker than any number of rerolls.  
**Prompt:** `keep this image and set the corrected wording as a layer, matched to the surface angle and given the same grain as the plate`  
`textimg.repair_not_regenerate`

### Clean Plate Clause

**Also called:** no watermark, no signature, no caption  
**What it is:** Stating explicitly that no text, watermark, signature, caption, frame or border should appear, because generated images frequently invent them from training material.  
**Effect on the audience:** A clean plate. Invented watermarks and stray signatures are among the most common artefacts and are tedious to remove afterwards.  
**Used for and where it works best:** Every generation that is not deliberately carrying text, and every reference plate and keyframe. Best across all still work.  
**Best in:** formats: Generated Keyframe Feeding Video, General Reference Plate, Character Sheet / Turnaround, Location Sheet / Master Plate, Props Sheet, Product Still / Packshot, Poster / Static Design, Thumbnail / Social Card, Editorial / Magazine Image, Fine Art Photography, Architectural Photography, Still Life Photography, Travel Photography, Documentary Photography, Abstract Photography | genres: all  
**Avoid when:** It usually costs nothing, which is why it belongs in almost every prompt. The exception is a register where a printed mark is authentic, such as a period photographic border or a stamped archive number.  
**Prompt:** `clean plate, no text, no watermark, no signature, no caption, no border or frame anywhere in the image`  
**Yields to:** `ident.render_register` — The register makes a printed mark authentic.  
`textimg.no_watermark_clause`

---

### Two Scripts on One Surface

**Also called:** bilingual caption, dual-language card, the second line problem
**What it is:** One frame carrying the same words in two writing systems at once — an exhibit label in English and Arabic, a title card in Latin and Syriac, a stadium graphic in two languages — where both have to be readable and neither may look like an afterthought.
**Effect on the audience:** The audience that reads the second script decides in about a second whether the piece was made for them or translated at them. The tell is never the translation; it is whether the second line was given the same room, the same weight and the same care as the first.
**Used for and where it works best:** Museum and exhibition work, heritage pieces for a diaspora audience, anything published in a country with two official scripts, and any piece whose subtitles are burned rather than delivered as a track. Three things decide it: **give each script its own line, never a slash between them**, because two systems sharing a line fight over baseline and reading direction. **Set the right-to-left line right-aligned and the left-to-right line left-aligned** — forcing both to one alignment is the single most common way a bilingual card reads as machine-made. And **size them for equal reading weight, not equal point size**: Arabic and Syriac carry more ink per character than Latin at the same nominal size, so matched numbers look mismatched on the wall — `textimg.subtitle_size_in_frame` carries the actual figures.

**Which language leads is a decision, and it is made by the audience, not by the designer's habit.** Put first — above, or left in a side-by-side — the language of **the people who will stand in front of this**: the local language on a local surface, the visitors' language in a visitor centre, the diaspora's language on a diaspora channel. Where the surface is genuinely for both, the language of the *place* leads, because the other one is the guest. Two things that are not reasons: the language the piece was written in, and the language of whoever is laying it out. **State the choice and why in one line in the project brief**, because the second script's readers notice the order immediately and it is the cheapest possible way to say who the piece thinks it is for. And keep it consistent across every deliverable in the campaign — a poster that leads in Arabic beside a film that leads in English reads as two organisations.
**Best in:** formats: Museum Installation, Exhibition, Heritage / Historical Documentary, Title Sequence / Opening Credits, Poster / Static Design, Commercial / TVC | genres: all
**Avoid when:** The surface is too small for two lines. A phone frame with a reserved lower band rarely holds both — there, pick the audience's script for the burned line and carry the other in the delivery layer, and say which you chose. And never generate either script as image content: `textimg.non_latin_script` governs, and a bilingual card doubles the risk rather than halving it.
**Prompt:** `clean bilingual caption plate, two separate lines, the right-to-left line right-aligned above and the left-to-right line left-aligned below, generous space between them, no slash and no shared baseline, text added as a typeset layer and not generated`
**Yields to:** `textimg.non_latin_script` — Never generate either script as image content.  
`textimg.two_scripts_one_surface`

### Subtitle Size in the Frame

**Also called:** caption cap-height, how big the subtitle actually is, the phone-in-the-hand test
**What it is:** **How large the burned text is as a fraction of the frame**, which is a different question from where it sits and from how many characters it holds. The package sizes subtitles in characters per line and places them in a band; neither of those tells anyone how big to set the type, so it gets set to whatever looked right on the editing monitor and is then unreadable on a phone.
**Effect on the audience:** A subtitle that is too small is not a subtitle. The viewer either leans in, gives up, or rewinds — and on a muted autoplay feed, where the text *is* the soundtrack, they simply scroll.
**Used for and where it works best:** Work in **cap height as a percentage of frame height**, because that is the only measure that survives every screen size. A useful set of anchors: **a burned subtitle on a vertical phone piece wants a cap height around 3.5 to 4.5% of frame height**, which on a 1920-tall frame is roughly 70 to 85 px; **a 16:9 piece watched on a laptop or television sits lower, around 2.5 to 3%**, because the screen is bigger and further away; **a cinema or large-venue piece can go to about 2%**; and **anything in a feed, where the phone is at arm's length in bright light, takes the top of the range, never the bottom.** **The screen decides the range, not the aspect**: a 16:9 piece watched in a phone feed is a phone piece, and because a horizontal frame is small on the phone it takes about 4.5% of its frame height or a little more, a working default recorded under `decisions`. Two more rules that matter as much as the number. **A second script is set larger than its point-size match, not the same**: Arabic and Syriac carry their meaning in strokes and dots that vanish before Latin does, so set them roughly **10 to 20% larger in cap height** than the Latin line to read as equal — which is what "equal reading weight, not equal point size" on `textimg.two_scripts_one_surface` means in numbers. And **the size is checked on the device, at the distance, in daylight** — not at 100% zoom on a monitor thirty inches from your face.
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Heritage / Historical Documentary, Commercial / TVC, Explainer, Music Video, Lyric Video, Museum Installation | genres: all
**Avoid when:** The piece delivers subtitles as a separate track the platform renders — there the player owns the size and this card does not apply. It applies the moment the text is burned in, and burned text cannot be made bigger later.
**Prompt:** `burned subtitle line set at roughly four percent of frame height in cap height, inside the central safe band, high contrast against a subtle shadow or scrim, the second script set slightly larger than the first for equal reading weight`
**Source:** assumption — the package's working figures (3.5 to 4.5% on a phone, 2.5 to 3% on a laptop or television, about 2% in a cinema, 10 to 20% larger for a second script), not a published standard; check them on the delivery device at its viewing distance, as the card says.
**Yields to:** AUTHORITY (not a card): the platform's own subtitle renderer — Subtitles delivered as a track, not burned.  
`textimg.subtitle_size_in_frame`

### Subtitling a Sung Line

**Also called:** lyric subtitle, translated lament, singing in one language and reading in another
**What it is:** **Subtitling a song is not subtitling speech, and the reading-speed rules do not transfer.** Every subtitle standard in this package is built on characters per second against a speaking rate. A sung line breaks that at both ends: a held refrain may occupy twelve seconds and eleven characters, far *under* any floor, sitting on screen so long it stops being read and starts being stared at; and a fast patter line packs syllables past any ceiling. The constraint that actually governs is **the musical phrase**, not the clock.
**Effect on the audience:** Done right, they stop noticing they are reading. Done by the speech rules, the words arrive out of time with the voice — and because a listener feels a musical phrase physically, a subtitle a beat late is far more wrong here than the same error over dialogue.
**Used for and where it works best:** **Cut the cues at the musical phrase, never at the character count.** One line per sung phrase, entering with the phrase and leaving with it, so the text breathes where the singer breathes. A repeated refrain is subtitled **once, on its first appearance**, and left alone after — the audience has it, and re-displaying it says the words matter more than the voice. Where a line is held, let the subtitle go early rather than holding it for the length of the note: the text has done its work in two seconds and the remaining eight belong to the singing. **Translate for sense and for the image, not for line length**, because nothing here has to fit a mouth — that constraint belongs to `rhythm.lip_sync_adaptation`, and confusing the two mangles a lyric to a length that serves nothing. And **decide once whether the song is subtitled at all**: a lament in a language the audience does not read can be left untranslated with one line of context before it, and sometimes should be, because the meaning is carried and the sound is the point. Say which you chose and why. See `lyric.singable_translation` for translating a lyric *to be sung*, which is a different job again. The type is sized as any burned subtitle is, by `textimg.subtitle_size_in_frame` and `access.legible_at_size` — a sung line changes the timing, not the size.
**Best in:** formats: Music Video, Lyric Video, Heritage / Historical Documentary, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok), Film | genres: Heritage (civilisation-focused), Musical, Drama, Historical / Biopic
**Avoid when:** The line is spoken rather than sung — `tens.subtitle_preempt` and `rhythm.subtitle_beat` govern there, with the reading-speed ceilings that genuinely apply. And avoid subtitling a wordless vocal or a hummed line at all; there is nothing to translate, and a cue reading *[singing]* tells the audience only that they have eyes. And a same-language sing-along is not this case: it shows every sung line each time it comes round, so the child can read along (`kids.singalong_text`).
**Prompt:** `one subtitle line per sung phrase, entering and leaving with the phrase, the refrain translated only on its first appearance, set in the central safe band at the size a burned subtitle needs on the phone it is watched on`
**Yields to:** `rhythm.subtitle_beat` — The line is spoken, not sung.  
`textimg.subtitling_a_sung_line`

### An Invented Script That Cannot Be Misread

**Also called:** fictional writing system, invented glyphs, the divergence rule
**What it is:** The design problem when a piece needs writing on screen that is deliberately **not** any real system. Every other card in this file is about getting real text right; this one is about making invented text unmistakable. The risk is specific: an invented script that closely resembles a real one is read by people who know that script as a *statement* about it — a bad transcription, a garbled quotation, a claim about a language — and those are the viewers most likely to be watching a piece set in a world drawn from their own culture.
**Effect on the audience:** A reader of the real script either relaxes or stops watching, and nothing in between. Given one clear structural difference they read the writing as belonging to the invented world and never test it. Given a near-miss they try to parse it, fail, and conclude the production did not know what it was doing.
**Used for and where it works best:** Any secondary world with writing in frame — tablets, seals, signage, banners, inscriptions. **Pick one structural difference from the real script and hold it absolutely.** Not a stylistic difference, a structural one: a real script built from wedge impressions gets an invented one built from straight incised strokes; an alphabet gets syllable blocks; a right-to-left system gets a vertical one. One decision, stated once, and it closes the whole problem — because the difference is legible at a glance and at any resolution the piece is watched at, where a subtle one is not — checked on its smallest screen, per `access.legible_at_size`, rather than assumed, and redesigned if the difference disappears there. **Then stop designing.** The audience needs the writing to look like a system, not to be one: consistent stroke count, consistent direction, consistent spacing, regular registers. **Generate it as geometry, never as text** — `ai.text_carved_geometry` in Phase 8 owns that technique and this card does not restate it — and never name a language, a script or a translation in the prompt.
**Best in:** formats: Animated Series, Animation Feature, Feature Film, Short Film, Game Narrative, Interactive Fiction, Comics, Vertical Micro-Drama, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Fantasy and Epic, Myth, Science Fiction, Adventure, Action
**Avoid when:** The writing is real. A real inscription is researched and reproduced, not invented, and diverging from it there is the failure rather than the rule. Do not use this to make a real script "safer" either — a wrong real script is wrong, and the answer is to get it right or to keep it out of frame.
**Yields to:** `textimg.carved_not_text` — for how the lettering is prompted in a still; and `ai.text_carved_geometry` — when it has to survive video generation, where the camera is locked. This card decides what the system looks like; those decide how it survives generation.
**Prompt:** `rows of short straight incised strokes in regular horizontal registers, some crossed, some paired, pressed at a consistent angle and depth, raking light across them`
`textimg.invented_script`

### Legible at the Size It Is Actually Watched

**Also called:** accessibility legibility, phone-size type, caption readability
**What it is:** The check that on-screen text can be read by the people watching, on the device they are watching on, including those who do not see the way the designer does. It is distinct from every composition card about where text sits: this one asks whether it can be *read* once it is there. The four things that decide it are size against the frame rather than against the monitor, the contrast between the type and whatever moves behind it, the weight and form of the letters, and how long the text is on screen.
**Effect on the audience:** A viewer who cannot read a caption does not report it — they leave, and the piece records it as a retention number with no cause attached. Roughly one viewer in twelve has a colour vision deficiency and a larger share watch with uncorrected or partially corrected sight, on a screen at arm's length, outdoors, in motion.
**Used for and where it works best:** On every piece with text in frame, and it is cheapest to fix in design and most expensive after a grade. **Judge type on the smallest screen the piece will play on, at arm's length, not on the edit monitor** — a caption that is comfortable at 27 inches can be unreadable on a phone held in a moving vehicle, which is where most vertical work is watched. **Put the text on something that does not move**: a plate, a scrim, a darkened band or a still area of frame, because contrast against a moving background is contrast that exists only in some frames. **Give it a hold, not a beat** — text that leaves as soon as an average reader finishes has already failed the slower half of the audience, and the common fix is fewer words rather than longer holds. And **do not carry information in colour alone**; that is `access.not_colour_alone`. `textimg.subtitle_size_in_frame` owns the specific sizing figures and this card does not restate them.
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Explainer, Documentary Feature, Documentary Series, Museum Installation, Corporate / Training, Commercial / TVC, Kids Content | genres: all
**Avoid when:** There is no text in frame at all. It does not apply to a title designed as a graphic element rather than as information — a main title that is meant to be *seen* rather than read is a design object, and forcing caption legibility onto it destroys it.
**Prompt:** `[Edit Overlay Instruction]: type set against a held still area or a darkened plate, weight and size judged at phone scale, held past the point the fastest reader finishes`
**Yields to:** `textimg.typography_as_subject` — A main title built as a design object, not information.  
`access.legible_at_size`

