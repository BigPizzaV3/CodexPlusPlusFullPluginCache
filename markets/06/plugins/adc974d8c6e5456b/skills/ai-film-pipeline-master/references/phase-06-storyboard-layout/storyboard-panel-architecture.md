# Storyboard Panel Architecture & Presentation Decks

21 cards. Master multi-panel poster grid architecture, aspect ratio conversion matrices, 6-column agency presentation layouts, visual reading flow, and closure rules for client-facing and AI-generative production boards.

---

### Decide the Sheet Before the Panel

**Also called:** the deck selector, sheet before panel, which board am I making  
**What it is:** The card at the head of the `board_arch.` shelf. It does not describe a deck. It asks the three questions the shelf's own pair graph asks — **is the question the sheet or the picture on it, who opens it, and how many shapes must it ship in** — and hands back a named shortlist for each answer. The axes were read off the shelf's `Yields to:` conditions and cross-checked against every `Avoid when:` on the shelf. **It is as much a boundary as a fork**: a quarter of this shelf's conditions leave it for another prefix, and the map says where each one goes. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen, and neither does most of what it selects — a deck is read, not watched. It exists so that the deck's shape is chosen against who opens it and what they must decide, rather than defaulting to the nine-panel poster because that is what a storyboard looks like in everyone's head.  
**Used for and where it works best:** Answer the three questions in order before you lay out a sheet. **Answer one honestly and you will often leave this shelf**, which is the point of asking it first. The only place the shelf genuinely forks is the deck shape itself — a handful of cards that really are alternatives to one another and that account for about half of everything this shelf says about itself. Almost everything else here is obligatory furniture that coexists with whatever you chose: it is applied, not selected, and the map lists it so that nothing gets forgotten rather than so that something gets picked.  
**Best in:** formats: All narrative and commercial production | genres: All  
**Avoid when:** **You want it to choose what is inside a panel.** It cannot, and the shelf says so in its own `Yields to:` fields: `board_arch.macro_detail_panel_insert` leaves for `doc.sports_master_wide`, `board_arch.split_panel_simultaneous_action` leaves for `anim_time.contemplative_held_tableau`, and `board_arch.final_story_beat_closure` leaves for `promo.end_card`. What a panel depicts belongs to the composition, framing and blocking shelves; what a sheet of panels *is* belongs here. Also **distrust axis three almost always** — the great majority of this shelf is shape-blind, so that question disqualifies four cards and nothing else, and a reader who expects it to narrow a shortlist will conclude the map is broken when it is merely honest. And avoid the whole card on a piece whose picture is barely cut: `board_arch.panel_count_runtime_formula` says in its own body that a held performance or an interview block may be two or three panels rather than eighteen, and a selector that starts from *which grid* has already assumed a grid is wanted.  
**Example:** `[Selector — produces no deck spec. It returns card ids. The chosen card carries the deck spec.]`  

---

**The axes**

**Axis 1 — Is the question the sheet, or the picture on the sheet?**
Asked first because it is the only axis that sends a reader off the shelf, and three of the shelf's conditions do exactly that. `board_arch.macro_detail_panel_insert` hands over on *"Fast sports action, the insert destroys spatial orientation"*; `board_arch.split_panel_simultaneous_action` on *"Simple contemplative solo scene, no concurrent event"*; `board_arch.final_story_beat_closure` on *"on any commissioned advert whose brief specifies the final frame"*, and that card names its successors in its own body — *"`promo.end_card` and `promo.logo_sting` govern instead."* **None of those three targets is on this shelf.** A reader who answers *the picture* has reached the edge of `board_arch.` and should keep walking.

**Axis 2 — Who opens this deck, and what are they deciding with it?**
The condition the shelf repeats most, and it is the one the shelf's only non-layout pair turns on: `board_arch.director_working_board_annotations` hands to `board_arch.client_pitch_presentation_finish` on *"Clean poster for a non-technical client"*, and gets handed back on *"Informal internal work, polish is not wanted yet."* `board_arch.six_column_agency_table_grid` asks the identical question in different words — *"Quick visual moodboard, technical columns unwanted"* — which is why the polish region and the layout region are one decision rather than two. The `Avoid when:` fields carry it again: *"non-technical clients who may find vector arrows distracting"*, *"Informal internal brainstorming where rapid unpolished doodles are more agile"*, *"Handing off a raw, rough draft sketch where color palette has not yet been selected"*.

**Axis 3 — How many shapes must this board ship in, and is one of them a phone?**
Three conditions turn on it and they are stated as delivery facts: *"Traditional theatrical 2.39:1 cinema project"* (`board_arch.vertical_reel_nine_by_sixteen_deck`), *"Tight smartphone feed where letterbox becomes a ribbon"* (`board_arch.anamorphic_scope_two_three_nine_deck`), *"One locked cinema aspect, nothing to reframe into"* (`board_arch.aspect_ratio_panel_conversion`). The `Avoid when:` fields add the reading surface — *"Mobile screen previews where excessive margins shrink the actual images"*, *"Printing physical paper copies on office laser printers"*, *"tiny 6pt body text that cannot be read on a laptop screen"*. **It is asked last and it is the weakest of the three**, because most of the shelf holds whatever rectangle you chose without caring which one it was. It earns its place only because the cards it does sort are the ones you cannot change later.

---

**The map**

**Axis 1 — the sheet, or the picture on it**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The sheet — how the board is built, dressed and delivered** (sixteen) | `board_arch.three_by_three_presentation_grid` · `board_arch.four_by_three_commercial_board` · `board_arch.six_column_agency_table_grid` · `board_arch.vertical_reel_nine_by_sixteen_deck` · `board_arch.anamorphic_scope_two_three_nine_deck` · `board_arch.aspect_ratio_panel_conversion` · `board_arch.panel_count_runtime_formula` · `board_arch.charcoal_dark_deck_contrast` · `board_arch.hairline_divider_visual_hierarchy` · `board_arch.typography_scale_hierarchy` · `board_arch.color_accent_status_coding` · `board_arch.color_palette_swatch_footer` · `board_arch.negative_space_poster_margins` · `board_arch.reading_flow_eye_gravity` · `board_arch.client_pitch_presentation_finish` · `board_arch.director_working_board_annotations` |
| **The picture — and here the shelf hands over** (four) | `board_arch.macro_detail_panel_insert` · `board_arch.split_panel_simultaneous_action` · `board_arch.graphic_match_panel_pairing` · `board_arch.final_story_beat_closure` |

**Where the shelf stops, and which shelf takes over — read off the shelf's own fields**

| From | On this condition | Goes to |
| :--- | :--- | :--- |
| `board_arch.final_story_beat_closure` | A commissioned advert whose brief specifies the final frame | `promo.end_card`, and `promo.logo_sting` named alongside it in the same card |
| `board_arch.macro_detail_panel_insert` | Fast sports action, where an insert destroys spatial orientation | `doc.sports_master_wide` |
| `board_arch.split_panel_simultaneous_action` | A contemplative solo scene with no concurrent event | `anim_time.contemplative_held_tableau` |
| `board_arch.graphic_match_panel_pairing` | *(states no alternative; `PAIR-AUDIT.md` files it `format-exclusion`)* | nothing named — a gap, recorded below |

**Axis 2 — who opens it**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A client, an investor or an agency approval chain** (seven) | `board_arch.client_pitch_presentation_finish` · `board_arch.three_by_three_presentation_grid` · `board_arch.four_by_three_commercial_board` · `board_arch.aspect_ratio_panel_conversion` · `board_arch.negative_space_poster_margins` · `board_arch.hairline_divider_visual_hierarchy` · `board_arch.color_palette_swatch_footer` |
| **A crew or a prompt engineer who has to execute it** (four) | `board_arch.six_column_agency_table_grid` · `board_arch.director_working_board_annotations` · `board_arch.panel_count_runtime_formula` · `board_arch.color_accent_status_coding` |
| **You, still deciding the film** (four) | `board_arch.macro_detail_panel_insert` · `board_arch.split_panel_simultaneous_action` · `board_arch.graphic_match_panel_pairing` · `board_arch.final_story_beat_closure` |
| **Nobody in particular — set by the delivery, or furniture every reader meets** (five) | `board_arch.vertical_reel_nine_by_sixteen_deck` · `board_arch.anamorphic_scope_two_three_nine_deck` · `board_arch.charcoal_dark_deck_contrast` · `board_arch.typography_scale_hierarchy` · `board_arch.reading_flow_eye_gravity` |

**Axis 3 — how many shapes it must ship in**

| Answer | The shortlist, by id |
| :--- | :--- |
| **One, and it is a phone** (two) | `board_arch.vertical_reel_nine_by_sixteen_deck` · `board_arch.four_by_three_commercial_board` |
| **One, and it is a cinema or a widescreen** (two) | `board_arch.anamorphic_scope_two_three_nine_deck` · `board_arch.three_by_three_presentation_grid` |
| **More than one, and the board itself must convert between them** (one) | `board_arch.aspect_ratio_panel_conversion` |
| **Shape-blind — it holds whatever rectangle you chose** (the rest) | Every other card named in the tables above. Named by complement on purpose: listing them again would make the map longer than the shelf, and their shared answer is that the question does not reach them |

*A card appears once per axis. The answer is the intersection of the three shortlists — and on this shelf the intersection is normally the whole dressing set plus one deck shape, because only the deck shape is a genuine choice.*

---

**The default, and the one against it**

**The default is `board_arch.three_by_three_presentation_grid`, and it is measured rather than assumed — but only after the trap is stepped around.** Two cards on this shelf take two inbound edges each. `board_arch.anamorphic_scope_two_three_nine_deck` is reached from `board_arch.vertical_reel_nine_by_sixteen_deck` on *"Traditional theatrical 2.39:1 cinema project"* and from `board_arch.aspect_ratio_panel_conversion` on *"One locked cinema aspect, nothing to reframe into"* — **two edges, one condition**, stated twice. That is a delivery escape hatch, not a fallback. `board_arch.three_by_three_presentation_grid` is reached from `board_arch.four_by_three_commercial_board` on *"Non-linear or open-ended experimental art film"* and from `board_arch.six_column_agency_table_grid` on *"Quick visual moodboard, technical columns unwanted"* — **two edges, two genuinely different conditions**, one about the story's shape and one about the reader's patience. Counting conditions rather than edges breaks the tie, and it breaks it the other way round from counting edges.

**The one against it is `board_arch.panel_count_runtime_formula`, delivered as `board_arch.director_working_board_annotations`.** It is the only card on this shelf that can tell you to make **less board**, and nothing routes to it or from it — `PAIR-AUDIT.md` files it as an execution note, so the pair graph cannot reach it at all. Its own body carries the argument the rest of the shelf never makes: that a piece with few cuts *"may be two or three panels rather than eighteen"*, that long form is boarded selectively, and that *"a representative board of six to twelve panels that covers the hard sequences is worth more than a complete one nobody finishes"* — with the real test named as *"which shots would be argued about on the day."* Against the grain because every other card here assumes a full sheet and then argues about its grid. Its cost is stated by the shelf around it: an annotated partial board is not something you hand a client, which is exactly why `board_arch.client_pitch_presentation_finish` sits opposite it and gets handed the job on *"Clean poster for a non-technical client."* **Choosing the best-looking deck is not the goal; a deck nobody needed is still a deck nobody needed.**

---

**The unasked**

**Fourteen of the twenty cards are the target of no `Yields to:` field anywhere on this shelf.** They can be applied but nothing ever sends you to them. By id:

`board_arch.four_by_three_commercial_board` · `board_arch.aspect_ratio_panel_conversion` · `board_arch.panel_count_runtime_formula` · `board_arch.charcoal_dark_deck_contrast` · `board_arch.hairline_divider_visual_hierarchy` · `board_arch.typography_scale_hierarchy` · `board_arch.color_accent_status_coding` · `board_arch.color_palette_swatch_footer` · `board_arch.negative_space_poster_margins` · `board_arch.reading_flow_eye_gravity` · `board_arch.graphic_match_panel_pairing` · `board_arch.macro_detail_panel_insert` · `board_arch.split_panel_simultaneous_action` · `board_arch.final_story_beat_closure`

**And the shape of that list is the finding, not its length.** It is two clean blocks and nothing else. **Every card that dresses a sheet is on it** — surface, rule, type, accent, palette, margin, reading flow — and **every card about the picture is on it too**. The only cards the pair graph can see are the ones that name a rectangle or a grid. That is not an oversight: a typographic ladder is not an alternative to a charcoal background, and `PAIR-AUDIT.md` says so in its own vocabulary, filing this block as `execution-note` and `format-exclusion`. **So the shelf has exactly one fork and a long list of things you must remember**, and a map is the wrong instrument for the second part. Reading this shelf as a menu produces a deck missing half its furniture, because nothing in the pair graph will ever remind you of the half that does not compete.

The second thing the list shows is the card this shelf wants and does not have: **nothing here decides whether to board at all, or how much of the piece to board.** The nearest thing that exists is buried in the middle of `board_arch.panel_count_runtime_formula` — a long passage saying that the rate is not the question on an uncut piece, that above a few minutes the arithmetic stops being the right question, and that the test is which shots would be argued about on the day. It is the shelf's only brake, it is filed as an execution note, and **no card routes a reader to it**. A shelf whose first question is *which grid* has already answered *whether a grid* without asking, and the one card that could have asked is the one card the graph cannot reach.

And one smaller gap, recorded: `board_arch.graphic_match_panel_pairing` is a panel-to-panel relation like the other three cards under Axis 1's second value, but unlike them it names no successor and no other shelf. Its `Avoid when:` — *"Raw, chaotic combat sequences where intellectual graphic matches feel overly precious"* — describes a scene with no card offered for it, here or elsewhere.

`board_arch.the_sheet_before_the_panel`

---

### Three-by-Three Presentation Grid

**Also called:** 9-panel poster deck, classic 3x3 storyboard, 9-cut presentation grid  
**What it is:** Arranging nine storyboard panels in a balanced 3-row by 3-column grid across a single poster layout, ideal for short-form commercials, trailers, and 30-second reels.  
**Effect on the audience:** Delivers instant visual comprehension of the complete dramatic arc at a single glance; balances breadth of story with legibility of individual stills.  
**Used for and where it works best:** 30-second commercials, cinematic trailers, high-concept music video treatments, and client pitch meetings.  
**Best in:** formats: Commercial / TVC, Music Video, Short Film, Trailer | genres: All  
**Avoid when:** Long-form narrative films with more than 25 distinct scene locations where 9 panels compress story to unintelligibility.  
**Example:** `deck_spec: 3x3 grid poster, 9 panels, 16:9 widescreen stills, hairline black borders, panel captions below with cut numbers 1-9.`  
**Yields to:** `board_arch.six_column_agency_table_grid` — Long-form narrative, more than 25 locations.  
`board_arch.three_by_three_presentation_grid`

---

### Four-by-Three Commercial Agency Board

**Also called:** 12-panel TVC board, 4x3 commercial deck, broadcast agency layout  
**What it is:** A 12-panel layout organized into four columns of three rows (or three rows of four panels), matching the classic 30s broadcast commercial structure; a 15s or 60s spot takes the count `board_arch.panel_count_runtime_formula` gives it rather than twelve by default.  
**Effect on the audience:** Maps directly to standard commercial beats: Hook (panels 1-3), Problem/Exploration (panels 4-6), Climax/Solution (panels 7-9), and Emotional Payoff/Resolution (panels 10-12).  
**Used for and where it works best:** High-end advertising agency pitches, product commercials, automotive spots, and broadcast campaign approvals.  
**Best in:** formats: Commercial / TVC, Brand Anthem, Product Video | genres: Commercial, Corporate, High-Fashion  
**Avoid when:** Atmospheric experimental art films with non-linear or open-ended structures.  
**Example:** `deck_spec: 4x3 grid poster, 12 panels, 4:5 vertical stills for mobile broadcast, deep charcoal background (#141416), cream subtitles.`  
**Source:** assumption — the package's working figure, not a published standard; the 15s/30s/60s spot lengths are the delivery lengths the client specifies, and the 12-panel mapping is a board habit.  
**Yields to:** `board_arch.three_by_three_presentation_grid` — Non-linear or open-ended experimental art film.  
`board_arch.four_by_three_commercial_board`

---

### Six-Column Agency Table Grid

**Also called:** master storyboard table, 6-column production deck, comprehensive shoot board  
**What it is:** A horizontal row-by-row table featuring six distinct technical columns: CUT & TIMECODE | IMAGE STILL | VISUAL & ACTION | CAMERA & SHOT | DIALOGUE | AUDIO & SFX.  
**Effect on the audience:** Eliminates all production ambiguity; unites the camera crew, director, sound designer, and client on a single synchronized page.  
**Used for and where it works best:** The primary technical handoff document for physical film sets and AI video generation prompts.  
**Best in:** formats: All narrative and commercial production | genres: All  
**Avoid when:** Quick visual moodboards where technical table text distracts from artistic feeling.  
**Example:** `table_row: CUT 01 [0:00-0:02.5] | [Wide Still] | King enters throne room | WIDE 40mm, slow dolly push | King: "The hunt begins" | Distant war horn, throne room reverb.`  
**Yields to:** `board_arch.three_by_three_presentation_grid` — Quick visual moodboard, technical columns unwanted.  
`board_arch.six_column_agency_table_grid`

---

### Vertical Reel Nine-by-Sixteen Deck

**Also called:** mobile storyboard board, TikTok/Reels deck, vertical 9:16 grid  
**What it is:** Storyboard decks composed entirely of 9:16 vertical panels arranged across a 4:5 or 3:2 poster sheet, formatted specifically for mobile-first content.  
**Effect on the audience:** Accurately reflects mobile screen reality, forcing the director to evaluate vertical headroom, text safe zones, and UI overlays.  
**Used for and where it works best:** TikTok videos, Instagram Reels, YouTube Shorts, and vertical mobile drama series.  
**Best in:** formats: Vertical Short-Form (Reels, TikTok), Mobile Drama | genres: Fast-Paced Lifestyle, Heritage Reel, Viral Pop  
**Avoid when:** Traditional theatrical 2.39:1 cinema projects. And a feed piece the brief delivers horizontally: Facebook and YouTube feeds carry 16:9 video as readily as vertical, so a reel or feed video is boarded at the aspect the brief states, never assumed to be 9:16.  
**Example:** `deck_spec: 6 vertical 9:16 panels arranged horizontally across a 3:2 landscape poster sheet with upper and lower UI overlay guides.`  
**Yields to:** `board_arch.anamorphic_scope_two_three_nine_deck` — Traditional theatrical 2.39:1 cinema project.  
`board_arch.vertical_reel_nine_by_sixteen_deck`

---

### Anamorphic Scope Two-Three-Nine Deck

**Also called:** 2.39:1 letterbox board, theatrical scope storyboard, widescreen cinematic deck  
**What it is:** Storyboard panels displayed in ultra-wide 2.39:1 aspect ratio with true cinematic letterboxing, highlighting negative space, wide landscapes, and peripheral blocking.  
**Effect on the audience:** Inspires Hollywood prestige, epic physical scale, and sweeping theatrical gravity.  
**Used for and where it works best:** Historical war epics, deep space sci-fi, sweeping westerns, and high-budget action trailers.  
**Best in:** formats: Feature Film, Historical Epic, Sci-Fi Trailer | genres: Epic, Heritage, Action, Sci-Fi  
**Avoid when:** Tight smartphone feed videos where 2.39 letterboxing shrinks the image to an unwatchable ribbon.  
**Example:** `panel_spec: 2.39:1 aspect ratio, anamorphic oval bokeh, wide dual-character dialogue staging at opposite frame edges.`  
**Yields to:** `board_arch.vertical_reel_nine_by_sixteen_deck` — Tight smartphone feed where letterbox becomes a ribbon.  
`board_arch.anamorphic_scope_two_three_nine_deck`

---

### Panel Aspect Ratio Conversion Matrix

**Also called:** responsive board translation, cross-format storyboard reframing  
**What it is:** The mathematical reframing of storyboard compositions when converting between 16:9 landscape, 9:16 vertical, 1:1 square, and 4:5 social portrait.  
**Effect on the audience:** Preserves narrative focal points and character eyelines across differing display formats without awkward cropping.  
**Used for and where it works best:** Multi-platform advertising campaigns where one commercial must ship in widescreen, vertical, and square formats.  
**Best in:** formats: Commercial / TVC, Cross-Platform Campaign | genres: Commercial, Promo  
**Avoid when:** Solely shooting for a single locked cinema screen.  
**Example:** `conversion_rule: 16:9 medium two-shot converts to 9:16 by reframing as an over-the-shoulder single or vertical stack with top/bottom headroom.`  
**Yields to:** `board_arch.anamorphic_scope_two_three_nine_deck` — One locked cinema aspect, nothing to reframe into.  
`board_arch.aspect_ratio_panel_conversion`

---

### Hairline Divider Visual Hierarchy

**Also called:** micro-rule dividers, 1px border aesthetics, deck separator lines  
**What it is:** Using ultra-thin, low-opacity hairline borders (1px width, 20-30% opacity, hex #FFFFFF or accent gold) between rows and columns of panels.  
**Effect on the audience:** Creates clean, sophisticated museum-grade visual separation without creating thick comic-book gutter distraction.  
**Used for and where it works best:** Premium presentation decks, luxury brand pitches, and high-end film director lookbooks.  
**Best in:** formats: Pitch Deck, Presentation Board, Director Lookbook | genres: Drama, High-Fashion, Heritage, Luxury  
**Avoid when:** Grungy graphic novel adaptations where thick, bold, chaotic comic gutters are intentionally desired.  
**Example:** `styling: 1px hairline border, 25% opacity cream line (#F0E6D2), padding between grid cells scaled to the canvas - 24px on a 1920px-wide board, the same share of the width as `board_arch.negative_space_poster_margins` gives its 3840px canvas.`  
**Source:** reference — checked 2026-09-23: no design standard sets a pixel gutter for a presentation board; Material Design's layout grid treats margins and gutters as flexible values that change with the screen size. A pixel figure only means something at a stated canvas.  
`board_arch.hairline_divider_visual_hierarchy`

---

### Deep Charcoal Dark Deck Contrast

**Also called:** dark mode storyboard, OLED black presentation, charcoal agency board  
**What it is:** Presenting storyboard panels on a deep matte charcoal background (#121214 to #18181B) with cream white text (#F0E6D2) rather than stark glaring white.  
**Effect on the audience:** Makes cinematic lighting in the stills pop with intense contrast; reduces eye strain during long boardroom or screen reviews.  
**Used for and where it works best:** The standard presentation background for dramatic films, dark thrillers, night commercials, and sci-fi lookbooks.  
**Best in:** formats: All cinematic presentation decks | genres: All  
**Avoid when:** Printing physical paper copies on office laser printers where dark backgrounds waste toner and smear.  
**Example:** `canvas: Background #141416 matte charcoal, body text #F0E6D2 cream, accent titles #D4AF37 muted gold.`  
`board_arch.charcoal_dark_deck_contrast`

---

### Style-Color Accent Status Coding

**Also called:** chromatic cue highlights, accent text coding, storyboard metadata styling  
**What it is:** Selecting one project-specific accent color (e.g., Assyrian Lapis Blue #1E3A8A, Royal Gold #D4AF37, Cyber Magenta #EC4899) for shot numbers, scene titles, and camera moves.  
**Effect on the audience:** Instantly establishes thematic brand mood while helping the reader skim technical headers effortlessly.  
**Used for and where it works best:** Professional client pitch decks, director working boards, and comprehensive commercial treatments.  
**Best in:** formats: All presentation boards | genres: All  
**Avoid when:** Using four or five competing bright rainbow colors that turn the storyboard into a chaotic circus.  
**Example:** `color_system: Primary background #121214, text #E4E4E7, accent color #C5A059 used exclusively for Cut numbers and Shot types.`  
`board_arch.color_accent_status_coding`

---

### Typography Scale Hierarchy

**Also called:** deck typographic ladder, font pairing rules, caption readability  
**What it is:** Establishing a strict three-tier typographic ladder: Tier 1 (Project Title in elegant serif caps, 24-28pt), Tier 2 (Shot/Action titles in bold sans-serif, 12-14pt), Tier 3 (Technical descriptions and audio notes in legible light sans-serif, 9-11pt).  
**Effect on the audience:** Guides the reader's eye naturally from broad concept down to minute camera execution without cognitive overwhelm.  
**Used for and where it works best:** Every client-facing and crew-facing storyboard deck.  
**Best in:** formats: All pitch decks and production boards | genres: All  
**Avoid when:** Using unreadable decorative gothic fonts or tiny 6pt body text that cannot be read on a laptop screen.  
**Example:** `typography: Header: Trajan/Cinzel 24pt caps; Section Titles: Inter Bold 12pt uppercase; Captions: Inter Regular 10pt cream.` Text treatment: typeset in the deck's layout layer, `text_owner: built`; the image generator never draws it.  
`board_arch.typography_scale_hierarchy`

---

### Panel-to-Runtime Calculation Formula

**Also called:** board density math, panel count pacing, ASL-to-panel conversion  
**What it is:** Calculating exact panel counts based on project runtime: 15s commercial = 6 to 9 panels; 30s commercial = 9 to 14 panels; 60s reel = 18 to 24 panels; feature scene = 1 panel per dramatic beat.

**A piece with few cuts does not work this way at all.** The formula converts runtime into panels through an implied cut rate, and plenty of good films do not have one: a to-camera monologue, an interview answer, a held performance, a slow observational piece, a single process filmed close, a gallery loop — so a 45-second piece may be **two or three panels** rather than eighteen, and a three-minute one **fourteen** rather than seventy — boarding either at the rate produces a stack of nearly identical drawings that nobody will look at twice. Board what actually changes: the setup, each reframe or insert, and the end state. **Count the visual events, not the seconds.** The rate below is for a piece whose picture is cut; where it is not, the rate is not the question, and the same logic governs long form further down this card.

**Between 30 and 60 seconds**, the rate the rows already imply is about one panel per 2.5 seconds, so a 45-second piece is roughly 14 to 19 panels. Read the rows as a rate rather than as a lookup: the 30-second row is 9 to 14 and the 60-second row is 18 to 24, which is the same rate stated twice, and a 45-second piece sits exactly between them rather than falling between them. This band matters because 45 seconds is a common vertical episode length and there was no row for it.

**Between 60 and 90 seconds**, carry the 60-second rate forward: about one panel per 2.5 to 3 seconds, so a 75-second piece is roughly 25 to 30 panels. The band exists because a 75-second film used to fall between the 60-second row and the feature row with nothing in between.

**Between 90 seconds and five minutes**, which is where music videos, longer ads and most kids pieces
sit, the rate is what carries over rather than the row: **roughly one panel per two-and-a-half to
four seconds**, taken from a genre card's average shot length where the piece takes one (`vlb.genre.drama`, for one, in `../phase-03-shooting-script/vlb-genres.md`), else from this band — the same rule the shot plan's table follows. A 90-second
music video at a 3 s average is about 30 panels; the same 90 seconds of a slow heritage piece is
nearer 20. Take the ASL from the shot plan, divide, and let the table be a sanity check rather than
the answer.

**Five minutes is not a threshold, and nothing changes at 5:01.** Between roughly three and eight minutes the two approaches overlap, and most pieces in that range are **partly** boarded: board the sequences that need it completely, at the rate above, and leave the rest to the shot plan. A six-minute film might be twelve panels or it might be sixty, and both are correct answers to different films — a six-minute piece built on two long interview blocks needs almost no board, and the same six minutes of wordless reconstruction needs nearly all of it. Count the sequences that need boarding, apply the rate to those, and ignore the total runtime. Reading the line below as a cliff produces a tenfold jump in the estimate for two seconds of runtime, which is a sign the arithmetic has stopped being the question rather than a real change in the film.

**Above about five minutes this arithmetic stops being the right question.** A twenty-minute documentary boarded at a panel per shot is six hundred panels, which nobody draws and nobody reads. Long form is boarded **selectively**: board the sequences whose staging is not obvious — an establishing arrival, a reveal, a transition between two worlds, anything with geography a shot list cannot carry — and leave the interview blocks, the archive runs and the straightforward narration sequences to the shot plan alone. A representative board of six to twelve panels that covers the hard sequences is worth more than a complete one nobody finishes. The test is not runtime; it is **which shots would be argued about on the day.**  
**Effect on the audience:** Guarantees that the storyboard represents actual film pacing, preventing over-boarded clutter or under-boarded pacing gaps.  
**Used for and where it works best:** Pre-production budgeting, scheduling AI image generations, and pacing checks.  
**Best in:** formats: All video production | genres: All  
**Avoid when:** Generating 50 storyboard panels for a 15-second commercial, which represents an impossible 0.3s cut rate.  
**Example:** `formula: 30s TVC @ 2.5s ASL = exactly 12 panels (4 rows of 3).`  
**Source:** assumption — the package's working figure, not a published standard; set the panel count from the shot plan's own average shot length.  
`board_arch.panel_count_runtime_formula`

---

### Western Z-Pattern and Inverted Reading Gravity

**Also called:** visual reading flow, storyboard scan path, compositional gravity  
**What it is:** Aligning panel action vectors with the natural reading direction of the target audience: left-to-right Z-pattern for Western audiences, right-to-left inverted flow for Arabic-speaking audiences.  
**Effect on the audience:** Movement across panels feels effortless, natural, and psychologically progressive.  
**Used for and where it works best:** Multi-panel poster layouts, social carousel posts, and graphic print presentations.  
**Best in:** formats: Storyboard Poster, Print Deck, Graphic Carousel | genres: All  
**Avoid when:** Staging characters moving left-to-right while panel reading flows right-to-left, creating visual friction.  
**Example:** `flow_design: In Western board, Panel 1 hero moves left-to-right, guiding viewer eye smoothly into Panel 2.`  
`board_arch.reading_flow_eye_gravity`

---

### Final Story Beat Closure Rule

**Also called:** emotional button ending, no-logo rule, dramatic panel resolution  
**What it is:** Mandating that the final panel of a storyboard deck MUST be a story or emotional beat (a held character gaze, a resolved gesture, a quiet landscape) rather than a corporate logo or brand card.  
**Effect on the audience:** Leaves the audience with lingering cinematic resonance, emotional weight, and human empathy rather than transactional commercial dryness.  
**Used for and where it works best:** All cinematic short films, trailers, heritage reels, and modern narrative commercials — anything whose last frame is the piece talking to the viewer rather than the client talking to the market.  
**Best in:** formats: All narrative and brand storytelling | genres: All  
**Avoid when:** **Any commissioned advert whose brief requires a lock-up, pack shot, price, website or legal line in the final frame.** That is not a loophole for retail broadcast only — it covers a 9:16 social commission, a product film, a campaign spot, anything a client is paying for a mark on. Where the brief names the closing frame, the brief wins and this card does not apply; `promo.end_card` and `promo.logo_sting` govern instead. This card is a rule for **story pieces**, and the failure it prevents is a film ending on a logo nobody asked for.

**Yields to:** `promo.end_card` — on any commissioned advert whose brief specifies the final frame.  
**Example:** `panel_final: Held close-up on the craftsman's weathered hands resting on the finished carving; slow fade to black. NO logo panel.` Text treatment: none; the closing panel carries no lettering, `text_owner: none`.  
`board_arch.final_story_beat_closure`

---

### Graphic Match Panel Pairing

**Also called:** shape bridge, storyboard visual rhyme, graphic transition pair  
**What it is:** Staging two consecutive panels so that a central circular, triangular, or linear shape in Panel A matches the identical geometric position in Panel B (e.g., spinning wagon wheel -> spinning celestial galaxy).  
**Effect on the audience:** Creates breathtaking visual poetry, thematic connection, and subconscious structural harmony across cuts.  
**Used for and where it works best:** Time jumps, historical flashbacks, dream sequences, and poetic commercial transitions.  
**Best in:** formats: Short Film, Music Video, Commercial, Montage | genres: Arthouse, Sci-Fi, Heritage, Fantasy  
**Avoid when:** Raw, chaotic combat sequences where intellectual graphic matches feel overly precious and artificial.  
**Example:** `pairing: Panel 4 center frame features round bronze shield; Panel 5 center frame matches with glowing full moon in identical coordinates.`  
`board_arch.graphic_match_panel_pairing`

---

### Generous Negative Space Poster Margins

**Also called:** breathing room margins, gallery deck borders, border padding ratio  
**What it is:** Allocating at least 8% to 12% of total canvas width and height to empty, clean margins around the entire panel grid.  
**Effect on the audience:** Lends an immediate aura of luxury, calm authority, and fine-art gallery curation to the presentation.  
**Used for and where it works best:** Client presentations, executive pitch meetings, and competition submissions.  
**Best in:** formats: Pitch Deck, Master Poster | genres: All  
**Avoid when:** Mobile screen previews where excessive margins shrink the actual images to microscopic sizes.  
**Example:** `canvas_setup: 3840x2160 poster resolution, 310px outer perimeter margins (8% of the width, the floor this card sets), 48px interior gutters.`  
**Source:** reference — checked 2026-09-23: no design standard sets a pixel gutter for a presentation board; Material Design's layout grid treats margins and gutters as flexible values that change with the screen size. A pixel figure only means something at a stated canvas.  
`board_arch.negative_space_poster_margins`

---

### Macro Detail Panel Insert

**Also called:** insert panel, detail beat, texture shock panel  
**What it is:** Deliberately inserting a tight, macro-detail panel (e.g., fingers trembling on a key, eye dilating, tear on cheek) in the middle of wide environmental shots.  
**Effect on the audience:** Jars the viewer's spatial awareness, spiking psychological intimacy and emotional stakes.  
**Used for and where it works best:** Critical revelation beats, pre-battle tension, emotional confessions, and thriller investigations.  
**Best in:** formats: Feature Film, Thriller, Drama, Commercial | genres: Thriller, Drama, Horror  
**Avoid when:** Fast sports action where tiny detail inserts cause spatial disorientation.  
**Example:** `sequence: Panel 1 Wide throne room -> Panel 2 Extreme Close-Up king's hand gripping sword hilt until knuckles turn white -> Panel 3 Medium reverse on assassin.`  
**Yields to:** `doc.sports_master_wide` — Fast sports action, the insert destroys spatial orientation.  
`board_arch.macro_detail_panel_insert`

---

### Split-Panel Simultaneous Action

**Also called:** dual-frame board, diptych panel, concurrent staging  
**What it is:** Dividing a single storyboard panel into two halves to illustrate two events occurring at the exact same fraction of a second (e.g., hunter releasing bow string / prey turning head).  
**Effect on the audience:** Generates immense suspense and dramatic irony by showing cause and effect simultaneously.  
**Used for and where it works best:** Heists, countdown sequences, phone conversations, and impending collisions.  
**Best in:** formats: Thriller, Action, Commercial, Dual Narrative | genres: Thriller, Action, Crime  
**Avoid when:** Simple contemplative solo scenes.  
**Example:** `panel_spec: Split panel 50/50 vertical division: Left side sniper finger squeezing trigger, Right side target stepping into crosshairs.`  
**Yields to:** `anim_time.contemplative_held_tableau` — Simple contemplative solo scene, no concurrent event.  
`board_arch.split_panel_simultaneous_action`

---

### Color Palette Swatch Footer Bar

**Also called:** palette anchor, hex color strip, 60:30:10 deck footer  
**What it is:** Embedding a horizontal strip of 5 to 8 colored swatches along the bottom footer of the storyboard deck, showing Dominant (60%), Secondary (30%), and Accent (10%) hex values.  
**Effect on the audience:** Proves chromatic discipline and visual consistency to clients and artists, ensuring all generative prompts adhere to the identical palette.  
**Used for and where it works best:** Professional production lookbooks, agency style guides, and AI generation conditioning.  
**Best in:** formats: Pitch Deck, Art Direction Guide, Master Poster | genres: All  
**Avoid when:** Handing off a raw, rough draft sketch where color palette has not yet been selected.  
**Example:** `footer_palette: Dominant #1A2421 (60% Forest Green) | Secondary #E5DCC5 (30% Parchment) | Accent #C0392B (10% Crimson).`  
`board_arch.color_palette_swatch_footer`

---

### Director's Working Board Annotations

**Also called:** blocking vectors, red-line board, camera trajectory arrows  
**What it is:** Superimposing clean graphical vectors (red or gold arrows, arc lines, field-of-view cones) onto storyboard panels to denote camera trajectories and character walking vectors.  
**Effect on the audience:** Makes kinetic motion crystal clear on static paper; ensures the video prompt engineer or camera operator knows exactly how the camera moves.  
**Used for and where it works best:** Complex choreography, stunts, multi-character party scenes, and AI video prompt handoffs.  
**Best in:** formats: Working Storyboard, Technical Breakdown | genres: Action, Dance, Musical, War  
**Avoid when:** Delivering final clean presentation posters to non-technical clients who may find vector arrows distracting.  
**Example:** `annotation: Curved yellow arrow from background left to foreground right indicating 180-degree tracking dolly camera path.`  
**Yields to:** `board_arch.client_pitch_presentation_finish` — Clean poster for a non-technical client.  
`board_arch.director_working_board_annotations`

---

### High-End Client Pitch Presentation Finish

**Also called:** agency finish, client-ready deck, executive lookbook polish  
**What it is:** The polished presentation layer wrapped around selected, already tested storyboard decisions: charcoal canvas, hairline rules, restrained headers, consistent representative stills, full metadata captions, and clean margins. It does not convert exploratory panels into final art or override the working board.  
**Effect on the audience:** Sells the project instantly; elevates a preliminary concept into an inevitable, high-value, multimillion-dollar cinematic reality.  
**Used for and where it works best:** Pitching to investors, brand CMOs, studio heads, and grant committees after the underlying framing and sequence decisions have survived the working-board pass. Use enough finish to communicate confidence and consistency; label concept frames as concept frames rather than implying final production assets already exist.  
**Best in:** formats: High-Budget Commercial, Feature Pitch, Premium Series | genres: All  
**Avoid when:** Informal internal brainstorming where rapid unpolished doodles are more agile.  
**Example:** `presentation_package: 4K 16:9 poster export, museum catalog layout, photoreal cinematic grade, complete technical audio and camera columns.`  
**Source:** reference — ITU-R, Recommendation BT.2020-2 (10/2015), Parameter values for ultra-high definition television systems for production and international programme exchange, Table 1, p. 2, https://www.itu.int/rec/R-REC-BT.2020, checked 2026-09-24; supports a 16:9 UHD picture of 3 840 × 2 160 pixels, the frame a "4K 16:9" export resolves to (the Recommendation calls it UHDTV, not 4K).  
**Yields to:** `board_arch.director_working_board_annotations` — Informal internal work, polish is not wanted yet.  
`board_arch.client_pitch_presentation_finish`
