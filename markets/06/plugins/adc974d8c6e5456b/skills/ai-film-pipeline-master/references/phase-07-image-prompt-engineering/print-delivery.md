# Print and Physical Delivery

13 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Design Inside the Print Gamut

**Also called:** CMYK limits, out-of-gamut colour  
**What it is:** Choosing colours that four-colour printing can actually reproduce, because the brightest screen blues, greens and oranges have no ink equivalent and are silently converted.  
**Effect on the audience:** What was approved on screen is what arrives on paper. Out-of-gamut colour does not fail loudly; it comes back dull and nobody can say exactly what changed.  
**Used for and where it works best:** Any image going to offset or digital print, packaging, posters and editorial. Best in print campaigns and packaging.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Commercial / TVC, Props Sheet, Fine Art Photography, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually costs vibrance when a screen-first palette is pulled back for print. The exception is delivering two graded versions, one for screen and one for paper, which is the normal professional practice.  
**Prompt:** `keep the palette inside the four-colour print gamut, avoid the electric blues and greens that have no ink equivalent`  
**Yields to:** `print.spot_colour_printing` — The colour needed lies outside the process gamut.  
`print.cmyk_gamut`

### Resolution at Final Size

**Also called:** pixels per inch, print resolution  
**What it is:** Calculating the pixel dimensions from the physical size and the viewing distance, rather than generating at a default and hoping it enlarges.  
**Effect on the audience:** Detail that holds at the size the viewer stands from it. A billboard needs far fewer pixels per inch than a book page, and confusing the two wastes money in both directions.  
**Used for and where it works best:** Any physical output, from a business card to a building wrap. Best in posters, packaging and exhibition work.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Multi-Screen Installation, Commercial / TVC, Fine Art Photography, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually over-produces when the image is enlarged far beyond what the viewing distance requires. The exception is a piece that will be photographed or reproduced later, where the extra resolution has a second use.  
**Prompt:** `generate at native size then enlarge in a dedicated pass to the pixel dimensions the final print size and viewing distance require`  
**Yields to:** `print.large_format_distance` — Viewing distance, not final size, sets the requirement.  
`print.resolution_at_size`

### Bleed, Trim and Safe Area

**Also called:** crop marks, edge allowance  
**What it is:** Extending the image beyond the trim line so that cutting variance never leaves a white edge, and keeping anything important inside the safe area.  
**Effect on the audience:** A clean cut every time. Trim moves by a millimetre or two on every run, and an image built exactly to the trim line will show white on some copies.  
**Used for and where it works best:** All printed matter: posters, covers, packaging, cards. Best in packaging and editorial.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Commercial / TVC, Fine Art Photography, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually costs composition when the bleed is taken from an image that was already tight. The exception is generating wider than the trim from the start, or extending the canvas afterwards rather than cropping into the design.  
**Prompt:** `compose with three millimetres of image beyond the trim on every edge, and nothing essential within five millimetres inside it`  
**Yields to:** `ai.outpaint_reframe` — Extend the canvas rather than crop the design.  
`print.bleed_and_trim`

### The Paper Is Part of the Image

**Also called:** stock choice, substrate effect  
**What it is:** Choosing the paper as a design decision, because uncoated stock absorbs ink and lowers contrast while coated stock holds detail and raises saturation.  
**Effect on the audience:** The same file is two different images on two papers. Uncoated warmth and coated punch are opposite decisions about how the work should feel.  
**Used for and where it works best:** Posters, books, packaging and any tactile deliverable. Best in editorial, packaging and fine art print.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Fine Art Photography, Commercial / TVC, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually disappoints when a high-contrast screen image is printed on uncoated stock without compensation. The exception is grading a separate version for the chosen stock, which recovers most of the loss.  
**Prompt:** `prepared for uncoated stock: contrast lifted and shadows opened to compensate for ink absorption, saturation raised to survive the paper`  
`print.paper_changes_the_image`

### Proof Before the Run

**Also called:** hard proof, contract proof  
**What it is:** Producing a physical proof on the actual stock before committing to a full run, and judging colour under a controlled light.  
**Effect on the audience:** Errors cost one sheet rather than five thousand. Screen approval is not approval; paper approval is.  
**Used for and where it works best:** Every commercial print run and any piece with brand colour obligations. Best in packaging and campaign print.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Commercial / TVC, Fine Art Photography, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually feels like a delay on a short deadline. The exception is a digital press run small enough that the first copies are themselves the proof.  
**Prompt:** `not a prompt line but a step: proof on the production stock under a controlled viewing light before the run is authorised`  
`print.proof_before_run`

### Rich Black Versus Flat Black

**Also called:** black build, four-colour black  
**What it is:** Deciding whether large black areas print as single-ink black, which reads grey and thin, or as a built black with cyan beneath, which reads deep.  
**Effect on the audience:** Black that looks black. A poster with a large flat single-ink black area is the commonest amateur print failure and it is visible from across a room.  
**Used for and where it works best:** Posters, covers and packaging with large dark areas. Best in posters and packaging.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Commercial / TVC, Fine Art Photography, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually causes drying and register problems when the ink build is pushed too high across a large area. The exception is following the printer stated maximum coverage rather than maximising the build.  
**Prompt:** `large black areas built as rich black rather than single-ink black, within the printer stated maximum ink coverage`  
**Yields to:** AUTHORITY (not a card): the printer's stated maximum ink coverage — The rich build would exceed the press limit.  
`print.black_is_a_decision`

### Type That Survives the Image Behind It

**Also called:** legibility over photograph, knockout type  
**What it is:** Ensuring the area behind any text has enough tonal separation and low enough detail for the type to be read, adjusting the image rather than the type.  
**Effect on the audience:** The words are readable at a glance. Type over a busy or mid-tone area fails first at small sizes and in poor light, which is where posters live.  
**Used for and where it works best:** Posters, covers, packaging and any printed piece with type over an image. Best in posters and covers.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Commercial / TVC, Thumbnail / Social Card, Fine Art Photography, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually damages the image when a heavy darkening gradient is added under the type. The exception is composing the quiet area from the start, or using a shadow region that was already there.  
**Prompt:** `the upper third held dark, flat and detail-free so reversed type reads cleanly at any size`  
**Yields to:** `textimg.text_safe_zone` — Compose the quiet area instead of darkening the image.  
`print.type_over_image`

### Compose for the Viewing Distance

**Also called:** billboard rules, distance legibility  
**What it is:** Designing large-format work for the distance it will be seen from, which usually means one idea, very few elements and much larger type than feels right up close.  
**Effect on the audience:** The piece works where it lives. A billboard designed at desk distance is illegible from the road, which is the only place it will ever be seen.  
**Used for and where it works best:** Billboards, banners, exhibition graphics and building wraps. Best in exhibition and outdoor campaign work.  
**Best in:** formats: Poster / Static Design, Multi-Screen Installation, Commercial / TVC, Fine Art Photography, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Editorial / Magazine Image, Still Life Photography | genres: all  
**Avoid when:** It usually feels crude when viewed as a file on a screen, because everything is oversized. The exception is proofing at a scale that matches the real viewing angle rather than judging at full resolution.  
**Prompt:** `composed for reading at thirty metres: one subject, one line of type, no detail smaller than a hand at full size`  
**Yields to:** `print.proof_before_run` — Judge at real viewing scale, not at full resolution.  
`print.large_format_distance`

### Safe Zones on a Fixed Panel or Wall

**Also called:** installation safe area, plinth loss, eye-height band, the crowd band  
**What it is:** **The parts of a wall-mounted or free-standing display that the audience cannot comfortably see**, which no platform interface causes and which are therefore missing from every safe-zone rule written for a phone. A fixed panel loses picture at the bottom to furniture and to other people, loses it at the top to viewing angle, and loses it at the edges to whoever is standing beside it.  
**Effect on the audience:** Work designed as if the whole panel were visible puts its subject and its caption exactly where a shoulder, a plinth or a neck angle removes them — and unlike a phone crop, nobody can scroll to fix it.  
**Used for and where it works best:** Museum and exhibition walls, lobby and foyer screens, a projection onto a fixed surface, a kiosk, a shop window, a listening-post panel. Four numbers do most of the work. **Average standing eye height is about 1.5 to 1.6 m**, so that is where the piece's centre of interest belongs, and a panel hung so its middle sits at 1.6 m is being read straight on. **Everything below about 1.2 m is the crowd band**: on any busy day it is behind somebody, so nothing essential goes there, and a plinth, bench or barrier takes a further slice that is measured on site, not assumed. **Above about 2 m the viewing angle turns steep** and text there is read at a tilt, so keep it to atmosphere rather than information. **At the sides, allow a person's width** — roughly 60 cm — before the edge if people queue along the panel. Then the distance rule on `print.large_format_distance` applies to whatever survives, because a wall panel is read from two to four metres and not from a desk.  
**Best in:** formats: Museum Installation, Multi-Screen Installation, Poster / Static Design, Exhibition, Kids Content, Heritage / Historical Documentary | genres: all  
**Avoid when:** The surface is handheld or personal — a phone, a tablet, a headset — where the platform's own interface owns the reserved bands and `vertical.safe_zones` governs instead. The two are different problems: one loses picture to software, this one loses it to bodies and furniture.  
**Prompt:** `composed for a wall panel read at three metres: the subject centred on standing eye height, the lower quarter of the frame carrying nothing essential, all type clear of the top and bottom bands`  
**Source:** reference — exhibition and interpretation design practice  
**Yields to:** `vertical.safe_zones` — The surface is handheld or personal.  
`print.fixed_panel_safe_zones`

### Grading for a Projection in a Lit Room

**Also called:** gallery projection, the black-level problem, ambient-light washout  
**What it is:** **A projector cannot make black. It can only fail to add light** — so the darkest part of a projected image is whatever the wall already is, and in a room with any daylight, spill or visitor lighting that is a mid grey. Every judgement made on a monitor, where black is black, is wrong by the width of that gap.  
**Effect on the audience:** The two or three darkest passages of a piece arrive as flat grey rectangles with nothing legible in them. Nobody reports it as a fault; they simply look away during those minutes, which on a gallery loop is most of the visit.  
**Used for and where it works best:** Any projected deliverable — gallery wall, museum room, foyer, event backdrop, projection onto a building. Design for it rather than repairing it afterwards. **Lift the shadows and carry the piece in the mid-tones**, because the range below about the bottom fifth is not going to exist. **Separate by hue and by value, not by darkness**: two dark things that read apart on a monitor merge on a wall, and a silhouette against a dark sky is the standard casualty. **Keep anything that must be read — text, a face, a key object — above the mid-tones.** Ask for the room's actual conditions the way you would ask for a native tile: the projector's brightness, whether the lights can be dimmed, whether there is a window, and what the surface is (a white wall is not a screen, and a coloured or textured wall tints and scatters everything). Where those are unknown, grade for the worse case; a piece that survives a lit room also works in a dark one, and the reverse is not true.  
**Best in:** formats: Museum Installation, Multi-Screen Installation, Experimental / Art Film, Title Sequence / Opening Credits, Brand Film | genres: all  
**Avoid when:** The destination is a screen that emits its own light — a phone, a monitor, a television, a cinema with a real black — where the shadow range is genuinely available and lifting it throws away depth the piece could have had. This is a delivery decision, so grade a separate version rather than compromising one for both.  
**Prompt:** `graded for projection in a lit room: shadows lifted off the floor, the subject carried in the mid-tones, separation by hue and value rather than by darkness, nothing essential in the deepest fifth of the range`  
`print.projection_grade`

### Spot Colour, Foil and Finish

**Also called:** special inks, varnish, embossing  
**What it is:** Treating special finishes, a spot ink added to ordinary process printing, a foil, a spot varnish or an emboss, as part of the image design rather than as decoration added later. A piece printed entirely from spot inks is a printing method, not a finish, and belongs to `print.spot_colour_printing`.  
**Effect on the audience:** The piece becomes an object. A finish that follows the image reads as craft, while one applied over it reads as packaging.  
**Used for and where it works best:** Covers, packaging, invitations and limited editions. Best in packaging and fine print.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Commercial / TVC, Fine Art Photography, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually adds cost without effect when the finish does not follow anything in the image. The exception is a single element, a title or a mark, where the finish has an obvious reason to be there.  
**Prompt:** `the title area designed to take a spot gloss varnish following the lettering exactly, the rest of the sheet matte` Text treatment: the lettering is the approved artwork, placed as a layer, `text_owner: built`; the spot-varnish plate follows that artwork.  
**Yields to:** `print.spot_colour_printing` — The brief names spot colour as the printing method.  
`print.spot_and_finish`

### Spot Colour as the Printing Method

**Also called:** spot separation, screen print, Pantone build, limited-palette printing
**What it is:** **A brief that says "four spot colours" is naming the printing *method*, not a
finish.** The piece will be printed from a small number of premixed inks, one screen or plate per
ink, instead of from the four fixed process inks — which is a different job from the first decision
onward, and the card above (`print.spot_and_finish`) is about something else entirely: a varnish,
a foil or one extra spot ink laid over ordinary printing.
**Effect on the audience:** Flat, saturated ink the process gamut cannot reach — fluorescents,
metallics, opaque colour on black stock — and an object that reads as made rather than output.
**Used for and where it works best:** Screen-printed posters, gig and exhibition work, packaging,
merchandise, and any run where the palette matters more than photographic fidelity. **The governing
number is the ink, not the file.** Screen printing carries a *ruling* far coarser than offset —
commonly 35 to 65 lines per inch against offset's 150 to 175 — and the mesh sets it, so the source
resolution you actually need is around **two to two and a half times the ruling at final size,
roughly 70 to 130 ppi**, not the 300 dpi that is quoted for everything. A 4K frame genuinely makes a
large screen-printed poster. **The tonal range is not 0 to 100.** A screen will not hold a dot much
below 8 percent — it washes out — and much above 85 percent it floods solid, so a gradient that fades
to nothing loses its tail and a shadow that runs to black fills in. **A photograph must be separated,
not simply converted**: an image reduced to a few opaque inks is built from a dominant midtone, a
shadow ink, a key black carrying the features that read as identity, and a highlight. Choose the
inks *for the face* if there is a face, because skin is the colour an audience checks instinctively.
And decide early whether inks **overprint** — two transparent spot inks crossing make a third colour,
which is how four inks read as seven, and it removes the need to trap that edge at all.
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Album Art / Cover, Exhibition Print, Fine Art Photography | genres: all
**Avoid when:** The image depends on continuous photographic tone across many hues, or the run is
short enough that per-ink setup outweighs the result — that is the case process printing exists for.
Also avoid committing a palette before the printer confirms it: the same Pantone number prints
materially differently on coated and uncoated stock, and most poster stock is uncoated.
**Prompt:** `[Print Method]: four spot inks, separated for screen print at 45 lpi, shadow capped at 85% and no dot under 8%, the palette chosen around the face`
**Yields to:** `print.cmyk_gamut` — Continuous photographic tone, or a run too short.  
`print.spot_colour_printing`

### Archival Materials and Lifespan

**Also called:** permanence, pigment versus dye, acid-free  
**What it is:** Choosing an ink, substrate and process combination rated for the lifespan the work needs, and recording what was used so a later reprint can match. Archival is a performance requirement, not one mandatory printing method.  
**Effect on the audience:** The print survives. Dye inks on ordinary paper visibly shift within a few years, which matters for anything sold, exhibited or kept.  
**Used for and where it works best:** Fine art prints, exhibition work, anything sold as an edition, and heritage documentation. A screen-printed edition keeps the rule and changes the materials: the method is `print.spot_colour_printing`, and permanence is asked of its inks and stock, confirmed with the printer. Best in fine art and exhibition.  
**Best in:** formats: Fine Art Photography, Poster / Static Design, Multi-Screen Installation, Editorial / Magazine Image, Heritage / Historical Documentary, Landscape Photography, Portrait Photography, Architectural Photography, Abstract Photography, Travel Photography, Still Life Photography | genres: all  
**Avoid when:** It usually costs more than a short-life piece justifies. The exception is any print that carries a signature or an edition number, where permanence is part of what was sold.  
**Prompt:** `not a prompt line but a specification: pigment inks on acid-free cotton rag, or for a screen-printed edition the inks and stock the printer rates for the same lifespan, with the ink set, paper and profile recorded for future reprints`  
`print.archival_and_lifespan`
