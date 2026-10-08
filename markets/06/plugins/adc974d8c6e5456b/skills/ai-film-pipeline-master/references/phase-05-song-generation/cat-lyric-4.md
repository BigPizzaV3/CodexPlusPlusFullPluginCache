# Lyric, Verse, Refrain and Song Structure — Part 4

Category `lyric`, continued. Parts 1 to 3 are in `cat-lyric.md`, `cat-lyric-2.md` and `cat-lyric-3.md`. Nothing here repeats them.

**Part 4 of 4.** 1 card.

These cards close gaps the database reported about itself: each was named as missing by an agent that needed it and could not cite it.

---

### The Prose Poem

**Also called:** poem in prose, prose poetry, poème en prose, the block poem, the paragraph poem, lyric prose piece
**What it is:** A poem written as one or more unbroken paragraphs, which gives up the line break — poetry's only instrument with no prose equivalent — and gives up the plot obligation prose normally carries, so the sentence becomes the unit of measure and the block on the page becomes the shape.
**Effect on the audience:** The reader arrives with prose reflexes, reading fast and expecting to be told something, and meets poetry's density at that speed. The correction is physical: they slow down without being instructed to, and usually go back to the top. A prose poem takes forty seconds and stays for a week, and readers rarely remember it as short.
**Used for and where it works best:** The short, intense, image-driven piece that has one pressure and no plot, and the passage of memory or dream where line breaks would impose a tidiness the material does not have. Baudelaire built the form for exactly this — city fragments too prosaic for verse and too charged for reportage — and it still does that job best. **The craft rule that makes it work: a prose poem earns its form by being unavailable in either neighbour.** If it would be better with line breaks, it is a poem set wrong. If it would be better with a story, it is a paragraph. Test both directions before defending it as a prose poem, because the form is the commonest hiding place for a piece that failed at line level and got justified into a block to conceal slack breaks. Four things carry the weight once the line is gone. **The sentence is the unit** — each one is a line-equivalent and gets weighed like one, so sentence length is now your only metre: a long accumulating sentence followed by a three-word one is a stanza break, and the run of lengths down the block is the poem's rhythm (`rhythm.length_as_tempo`, `rhythm.short_after_long`, `rhythm.long_breath`). **Rhythm moves inside the paragraph rather than at its edges** — repetition has to replace the line's micro-suspense, so anaphora, a mutating refrain and internal sound patterning do structural work here that they only decorate elsewhere (`rhythm.anaphora`, `rhythm.epistrophe`, `rhythm.consonant_texture`, `lyric.vowel_casting`). **Image density replaces lineation as the signal** that this is a poem: the sentences must sit closer together in image terms than any prose would, and the material should be generated from an object and the senses rather than from a feeling (`lyric.object_writing`, `rhythm.concrete_nouns`). **The block is a visual fact, not a default** — a squat grey rectangle announces before a word is read that this is short, continuous and will not let the reader rest, which is why the form suits claustrophobia, obsession and held breath, and why a prose poem broken into four airy paragraphs is usually four attempts at one poem. **How it ends, given there is no last line:** the landing is built out of sentence length collapsing — long, then short, then shorter, the diminishing close of `end.poem_landing` performed with syntax instead of lineation — out of the last sentence turning on its last word (`rhythm.last_word_turn`, `rhythm.end_weight`), and out of a final image assembled from parts already on the page (`end.final_image`). Stop on the image, never on its meaning. **Boundaries inside this database:** `rhythm.lyric_adjacent_prose` is one verse device imported into a prose work and dropped again, and it depends on the plain prose around it — here there is no around, the device runs the whole object. `lyric.rhyme_free` still has lines and a melody keeping time. `lyric.sound_texture`, `rhythm.anaphora` and `rhythm.fragment` are devices used inside this form, not the form. `rhythm.white_space` and `rhythm.paragraph_breath` are pacing diagnostics for blocks inside a long work; here the block *is* the work. **The neighbours, honestly:** the lyric essay and flash fiction sit either side and the borders are genuinely contested, not merely fuzzy. The lyric essay — named by Deborah Tall and John D'Agata at *Seneca Review* in 1997 — keeps an allegiance to fact and usually runs longer: a prose poem is rarely over a page, a lyric essay can run twenty. Flash fiction keeps the story obligation, and the editor's practical test, put well by Nancy Stohlman, is whether the piece is driven by narrative or by image and emotion; Tania Hershman's version is that a flash must feel like it is on the side of story, even if only just. Tara L. Masih is right that it is a sliding scale rather than a taxonomy, and the same piece does get published under both labels. Treat the label as a submissions decision and the craft rule above as the real one.
**Best in:** formats: Prose Poem, Poetry, Essay, Short Story, Memoir | genres: Literary, Arthouse, Surreal, Heritage, Migration
**Avoid when:** Something has to happen. The form has no mechanism for consequence, and a prose poem carrying a real event delivers it as scenery — the reader finishes knowing a thing occurred and feeling nothing about it, which is the exact failure flash fiction exists to avoid. Avoid it too when the piece must be performed to a room: it gives a listener no visible breath marks and no line to end on, so a landing that clicks on the page can pass a live audience without registering. And the form's own failure mode is `rhythm.empty_music` at full length — a block that scans beautifully, moves nowhere, and mistakes texture for a turn. The diagnostic is brutal and works: rewrite the whole thing as flat prose, one plain sentence per image, and ask whether anything is left worth saying. If the only answer is "a mood", that is a legitimate result for a prose poem and a fatal one for anything else of the same length, so make sure it was the result you wanted and not the one you settled for.
**Example:**
> **Inventory**
>
> The officer asks what is in the case and my mother says clothes, which is true, and does not say that the clothes are folded around a jar of soil the size of a fist, because that is not a thing a case contains, that is a thing a country does. She has packed it the way she packs everything, tightly, as though the journey will be graded. Somewhere over the sea the jar sweats. Later, in a flat with a boiler that knocks twice before it agrees to work, she will set the soil in a pot on the windowsill and grow nothing in it for eleven years, watering it on Sundays, and when I ask her why she waters it she will say that you water what you have. The boiler knocks. She waters it.
>
> Set as verse, the eleven-year sentence would be cut into line-units that each promise a small turn, and the one thing the piece is doing — running on the way the waiting ran on, until it simply stops — would be redistributed into a dozen little suspensions instead of one held breath.

**Yields to:** `lyric.rhyme_free` — Piece must be performed to a room.  
`lyric.prose_poem`

---

## Coverage

**1 card** in this file: `lyric.prose_poem`.

## Sources

Verified 2026-09-17.

- [Prose Poem — Academy of American Poets](https://poets.org/glossary/prose-poem)
- [Prose poetry — Wikipedia](https://en.wikipedia.org/wiki/Prose_poetry)
- [Le Spleen de Paris (Petits poèmes en prose) — Wikipedia](https://en.wikipedia.org/wiki/Le_Spleen_de_Paris)
- [What Sets Prose Poetry Apart from the Lyric? — Paul Hetherington and Cassandra Atherton, Literary Hub, from Prose Poetry: An Introduction (Princeton UP, 2020)](https://lithub.com/what-sets-prose-poetry-apart-from-the-lyric/)
- [What is a Prose Poem? Understanding Prose Poetry — Writers.com](https://writers.com/prose-poetry-definition)
- [The Lyric Essay — Seneca Review (Deborah Tall and John D'Agata, 1997)](https://senecareview.hws.edu/the-lyric-essay)
- [The Lyric Essay: Examples and Writing Techniques — Writers.com](https://writers.com/lyric-essay)
- [Ask A Flash Fiction Editor: Is this Flash Fiction or a Prose Poem? — Nancy Stohlman](https://nancystohlman.com/2013/04/28/ask-a-flash-fiction-editor-is-this-flash-fiction-or-a-prose-poem/)
- [Prose Poem or Flash Fiction – What's the Difference? — Jessica Terson, Trish Hopkinson blog (Hershman and Masih quoted)](https://trishhopkinson.com/2018/11/25/prose-poem-or-flash-fiction-whats-the-difference-guest-blog-post-by-jessica-terson/)
- [Poetic closure — Wikipedia](https://en.wikipedia.org/wiki/Poetic_closure)
