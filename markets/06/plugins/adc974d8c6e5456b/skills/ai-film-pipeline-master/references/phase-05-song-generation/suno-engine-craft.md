# Tag-and-Style Song Engine Craft

19 cards. Section tags, the Styles field, exclusions, vocal direction and hallucination prevention for Suno, the tag-and-style song engine directed by a lyric sheet and a style field. These cards are where Suno's syntax and vendor facts live: every fact carries its official source and the date it was read. The Suno adapter in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §7 records when these facts were checked and points back here.

**How to read the tags on these cards.** A bracket tag is presented as documented only where an official Suno page names it. Every other bracket tag is marked *community practice that Suno does not document*. It comes from user-made cheat sheets, not from Suno, and a take that uses one is a test, not a control.

---

### Final-Fidelity Song Render

**Also called:** Suno v6, Suno flagship audio model, broadcast fidelity music engine, release render  
**What it is:** Rendering the release take on Suno's flagship model, v6, rather than on the lighter drafting tier, once the lyric, the section map and the style description are settled. The v6 family launched on 2026-09-09 in three variants: v6 (the flagship, "reliable, precise"), v6-wild (experimental, "less predictable and more varied", suited to genre-blending) and v6-mini (faster and lighter; the drafting tier, `suno.v55_fast_iteration`). Suno says "All models prior to v6 have been retired, but your songs will still be in your library and remain unchanged". Continuing work on an old song produces a new v6 generation, and Custom Models were upgraded to v6 automatically. The model picker is at the top right of the Create form, and the choice sticks until you change it. The help centre calls v6 "Recommended for most songs", but no page names the default model. **Plans:** the help centre says v6 and v6-wild are on Pro and Premier. The pricing page lists "Advanced models (v6 and v6-wild)" under Premier and gives Pro only "Access to our best models". The two pages disagree, so a Pro user checks the model picker. The owner's plan is Premier, which both pages include; he reports that a new Suno model reaches Premier first and the other plans later (2026-09-23). On client work, name in the song engine record whose plan the work runs on — model access and downloads follow that plan; where the brief does not say, take the owner's plan, record it under `decisions`, and continue. **Max Mode** (v6) costs more credits. Suno recommends it for songs over 2 minutes, for covers that should stay close to the original, for style transfer, and for keeping vocals and style consistent. No exact credit figure is published. **What comes back:** Suno publishes no sample rate or bit depth for generation. The model returns a stereo mix, not stems; stems are a separate paid feature (`song_handoff.stem_separation_protocol`). **Downloads:** MP3 on all plans; WAV on Pro and Premier, web only; MIDI on Premier, only for songs made in Studio. Studio (Premier) exports the full song, a selected range or the multitrack "in 32-bit WAV or MP3 format". Download quotas are 20 songs a month on Pro and 60 on Premier; one song counts as one download whatever the formats. **Rights:** on Pro and Premier, Suno assigns the output to you, and commercial use requires a permitted download. On Free, use is personal and non-commercial only.  
**Effect on the audience:** The track reads as a finished record rather than a sketch: acoustic instruments, the vocal and the stereo picture carry the detail a release is judged on. The take is still mastered in the edit, and a generated acoustic timbre is not a recording of live musicians.  
**Used for and where it works best:** Final release singles, theatrical cinematic scores, authentic acoustic folk, and professional commercial anthems. Use v6-wild instead when the brief is a deliberate genre blend and the take will be auditioned before it is trusted.  
**Best in:** formats: Pop Single, Epic Anthem, Film Score, Heritage Folk | genres: All  
**Avoid when:** Ultra-fast rough idea drafting where generation speed is prioritized over raw acoustic fidelity.  
**Example:** `Model: v6 (Max Mode on, the song runs over 2 minutes) | Styles: Epic Mesopotamian folk orchestral, 92 BPM, live acoustic oud, frame drums, wide stereo image | Lyrics: the approved sheet with its section tags, unchanged from the draft | Delivery: WAV download, then the project master`  
**Source:** reference — Suno official pages, read 2026-09-23: Introducing v6, https://suno.com/blog/introducing-v6 ; What's new in v6, https://help.suno.com/en/articles/13924801 ; v6 FAQ, https://help.suno.com/en/articles/13924481 ; How do I change models, https://help.suno.com/en/articles/13924993 ; Current Models: v6, https://help.suno.com/en/articles/13924737 ; Pricing, https://suno.com/pricing ; What types of files can I download, https://help.suno.com/en/articles/13926081 ; How do downloads work, https://help.suno.com/en/articles/13876865 ; What counts as one download, https://help.suno.com/en/articles/13926145 ; Introducing Suno Studio 2.0, https://help.suno.com/en/articles/13670529 ; Terms of Service, https://suno.com/terms ; What rights do I have with the free plan, https://help.suno.com/en/articles/9601601 .  
**Shelf life:** dated — Suno's models, plans, downloads and rights as read on 2026-09-23. Re-verify on the official pages before execution and at least every 30 days. No paid call runs without the project spend gate (ENGINE-CHECK.md §2).  
**Yields to:** `suno.v55_fast_iteration` — Rough drafting where speed beats fidelity.  
`suno.v6_engine_architecture`

---

### Fast Drafting Pass for Hooks

**Also called:** Suno v6-mini, Suno fast-iteration model, rapid melodic sketch engine, draft tier  
**What it is:** A deliberate drafting pass on v6-mini, the "faster, lighter" member of Suno's v6 family. It is the one model on every plan, Free included, and it is used to sketch and compare several hooks, genres and melodic ideas before the release render. The Free plan runs v6-mini only and carries no commercial use. The card id keeps "v55" only so existing routes do not break. v5.5 (released 2026-03-26) was retired with every model before v6 and cannot be selected for new generations. As history, Suno described v5.5 as "our best and most expressive model yet"; it was never presented as a speed tier.  
**Effect on the audience:** The hook that reaches the listener is the one chosen by ear from several sketches, not the first one the engine returned.  
**Used for and where it works best:** Rapid melodic sketching, testing multiple lyrical hooks, and generating high-velocity social media audio tracks.  
**Best in:** formats: Social Reel Audio, Pop Hook Sketch, Viral Short | genres: Pop, Electronic, Upbeat Folk  
**Avoid when:** Intricate acoustic chamber music requiring subtle microtonal quarter-tone precision.  
**Example:** `Model: v6-mini | Styles: Catchy Middle Eastern pop hook, 124 BPM, bright synth strings, male energetic vocal | run several generations, choose the hook by ear, then carry that lyric and style unchanged to v6 for the release render`  
**Source:** reference — Suno official pages, read 2026-09-23: What's new in v6, https://help.suno.com/en/articles/13924801 ; Current Models: v6, https://help.suno.com/en/articles/13924737 ; v6 FAQ, https://help.suno.com/en/articles/13924481 ; Release Notes, https://suno.com/release-notes ; Pricing, https://suno.com/pricing ; the v5.5 quote from https://about.suno.com/blog/v5-5 (checked 2026-09-23).  
**Shelf life:** dated — the model list as read on 2026-09-23. Recheck the live picker before execution and at least every 30 days.  
**Yields to:** `score.microtonal_quarter_tone_tension` — Intricate acoustic work needing quarter-tone precision; no Suno page documents quarter-tone output, and that card says what Lyria documents.  
`suno.v55_fast_iteration`

---

### Structural Section Markers

**Also called:** song architecture brackets, song map tags, Suno syntax, section tags, structure tags  
**What it is:** Translating the approved song map into Suno's bracketed section tags in the Lyrics field (Custom Mode), one tag on its own line above the lines it heads. Suno's guide "How to Make a Song" (updated 2026-08-12) names [Intro], [Verse], [Verse 1], [Pre-Chorus], [Chorus], [Bridge] and [Outro], and says structure tags "help guide Suno to produce a structured song". Later verses follow the documented numbered form ([Verse 2]). Suno's Music Glossary also lists Hook, Refrain, Break and Drop as structure terms, but it presents them as vocabulary to use in prompts, not as bracket syntax. The tags are prompt hints, not forced state-machine transitions. In v6 the Song Editor also lets you insert, rename, move and recolour sections on the waveform, so a returned structure can be corrected after generation as well as steered by tags. **Language of the brackets:** every section tag and every direction inside square brackets is written in English, whatever language the song is sung in; only the sung lines under the tags are in the song's own language and script, and words in parentheses are sung, so they follow the lyric's language (the owner's working practice on Suno, reported 2026-09-23; Suno's pages do not state it).  
**Effect on the audience:** Makes the musical progression the writer planned far more likely. A take that meanders into endless verses, brings the hook back too early, or skips, repeats or invents a section is caught against the map and re-rolled.  
**Used for and where it works best:** Every lyric sheet sent to Suno, after the song form is decided. The section map is the writer's plan, and a returned take can be checked against it section by section. Test the current model with a short audition before relying on custom modifiers, meaning any tag beyond the documented list.  
**Best in:** formats: All song generation | genres: All  
**Avoid when:** Writing raw lyrics without bracketed section headers, which causes the AI to guess randomly and produce chaotic forms, and leaves nothing to check the take against. That is the working observation behind this card; Suno's own pages say only that the tags help guide the structure.  
**Example:** `[Intro] -> [Verse 1] -> [Pre-Chorus] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Chorus] -> [Outro]` — each tag on its own line in the Lyrics field, above the lines it heads.  
**Source:** reference — Suno official pages, read 2026-09-23: How to Make a Song with Suno, https://suno.com/hub/how-to-make-a-song ; Music Glossary for Suno, https://help.suno.com/en/articles/9010177 ; How to Use: Song Editor, https://help.suno.com/en/articles/6141505 . Lyria 3.5's own section tags: https://ai.google.dev/gemini-api/docs/music-generation (read 2026-09-23).  
**Shelf life:** dated — the documented tag list as read on 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `lyria.dynamic_energy_progression` — The song goes to Lyria 3.5, which also documents section tags but is directed by describing the energy arc in prose; that card holds Lyria's syntax.  
`suno.structural_metatags`

---

### Chorus Energy Lift

**Also called:** chorus lift tag, climax marker, power chorus  
**What it is:** Directing the later choruses to be bigger than the first: more instruments, fuller drums, a wider stereo image, a higher and stronger vocal. The direction is written on those chorus sections and the take is then auditioned, because the direction asks for the lift and does not guarantee it. Suno documents [Chorus] as the section tag (`suno.structural_metatags`). Lift modifiers such as [Power Chorus] or [Soaring Chorus], or a description written inside the chorus tag, are community practice that Suno does not document, so each one is a test, not a control. The documented vocabulary for the lift is the glossary's dynamics words (Crescendo, Forte) and Suno's advice to "use dynamics to shape emotional intensity" in the style description.  
**Effect on the audience:** The song climbs: each return of the hook lands harder than the last instead of repeating at the same size. A successful take increases density or register at the chorus; the tag does not guarantee loudness, instrumentation, stereo width or octave.  
**Used for and where it works best:** The second and third chorus of epic anthems, rock tracks, and emotional ballads.  
**Best in:** formats: Epic Anthem, Rock Ballad, Pop Single | genres: Epic, Pop, Rock  
**Avoid when:** Intimate acoustic lullabies or quiet folk laments.  
**Example:** Community form, to audition: `[Power Chorus, full orchestra explodes, driving percussion, heroic vocal delivery]`. Documented form: `[Chorus]` over the final chorus lyric, with the lift in Styles: `crescendo into the final chorus, full orchestra, driving percussion, heroic vocal delivery`  
**Source:** reference — Suno official pages, read 2026-09-23: How to Make a Song with Suno, https://suno.com/hub/how-to-make-a-song ; Music Glossary for Suno, https://help.suno.com/en/articles/9010177 . The lift modifiers are on no official page.  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `suno.whispered_vocal_directing` — An intimate lullaby or a quiet folk lament.  
`suno.dynamic_energy_chorus`

---

### Vocal Casting & Harmony Direction

**Also called:** vocal casting tags, multi-part harmony, backing choir  
**What it is:** Stating the lead voice's gender and register and the backing layers for each section, for example a deep baritone lead over a female choir in fifths. Suno's documented controls are the **Vocal Gender** dropdown (Male or Female) under Custom Mode > Advanced Options, or the words in the prompt in Simple Mode ("female vocals"), plus qualities such as "gritty" or "soft" in the Styles field. Suno frames this as guidance, not a guarantee. The glossary's vocal-technique words are documented vocabulary: Falsetto, Belt, Melisma, Vocal Run, Harmonization, A Cappella, Call and Response, Scat, Crooning, Rapping. Bracket casting tags such as [Male Baritone Lead], [Female Belting Soprano], [Harmonized Chorus] and [Backing Choir] are community practice that Suno does not document.  
**Effect on the audience:** The song keeps one cast from the first verse to the last, with harmonies that are designed rather than accidental. Casting tags and the dropdown aim to stop the lead switching gender between verses; neither is a lock, so a take where the lead changes voice is caught against the written casting.  
**Used for and where it works best:** Multi-part vocal arrangements, call-and-response anthems, and operatic choruses.  
**Best in:** formats: All vocal songs | genres: All  
**Avoid when:** Over-specifying conflicting vocal directions in the same section, for example a deep baritone and soprano screams on one line.  
**Example:** Documented: `Vocal Gender: Male | Styles: deep baritone lead, lush female backing choir, harmonization in fifths`. Community form in the Lyrics field, to audition: `[Lead Vocal: Deep Baritone] / [Backing Vocals: Lush Female Choir harmonies in fifths]`  
**Source:** reference — Suno official pages, read 2026-09-23: Can I choose the gender of the singer, https://help.suno.com/en/articles/10153473 ; Music Glossary for Suno, https://help.suno.com/en/articles/9010177 ; Release Notes (gender selection on mobile, 2026-05-14), https://suno.com/release-notes . The bracket casting tags are on no official page.  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
`suno.vocal_arrangement_tags`

---

### Instrumental Solo & Acoustic Break Placement

**Also called:** solo prompt tag, instrumental interlude, feature break  
**What it is:** Writing a dedicated instrumental spotlight section into the lyric sheet: an oud solo, a ney flute interlude, a santur cadenza, a drum break, an acoustic guitar solo. Suno's glossary lists Break as a structure term, defined as "a section where some instruments drop out, creating contrast", a word to use in prompts rather than a bracket tag. Checked again on 2026-09-24: no official Suno page names an [Instrumental], [Break], [Interlude] or solo bracket tag, or any way to write an instrumental or silent bar inside a lyric. "How to Make a Song" (updated 2026-08-12) brackets only [Intro], [Verse], [Verse 1], [Chorus] and [Bridge], and its only instrumental control is the Instrumental toggle, which applies to the whole song. So [Instrumental], [Break] and [Interlude] written as a line in the lyric are community practice too. Spotlight tags such as [Oud Solo], [Ney Flute Interlude], [Santur Cadenza], [Drum Break], [Acoustic Guitar Solo] and [Instrumental Break: ...] are community practice that Suno does not document, so the first take is an audition.  
**Effect on the audience:** Gives the listener's ear room to breathe and appreciate virtuosic musicianship before the final vocal onslaught.  
**Used for and where it works best:** Immediately following the second chorus or bridge to build organic human musical credibility.  
**Best in:** formats: Folk Ballad, Heritage Epic, Rock, Jazz | genres: All  
**Avoid when:** Short 30-second commercial jingles where every second must carry marketing lyrics.  
**Example:** `[Instrumental Break: Virtuosic Acoustic Oud Solo with tremolo, rising microtonal tension]` on its own line after the second chorus, with no lyric under it (community tag, audition it).  
**Source:** reference — Suno official pages, read 2026-09-23 and again 2026-09-24: Music Glossary for Suno, https://help.suno.com/en/articles/9010177 ; How to Make a Song with Suno, https://suno.com/hub/how-to-make-a-song ; iOS Create: Custom Mode (the Instrumental toggle), https://help.suno.com/en/articles/3197377 ; How to Use: Song Editor, https://help.suno.com/en/articles/6141505 . The spotlight tags, and [Instrumental], [Break] and [Interlude] as lyric lines, are on no official page.  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `sync.instrumental_break_dialogue_window` — A 30s spot where words must carry every second.  
`suno.instrumental_solo_tags`

---

### Style Description Formula

**Also called:** music style box prompt, genre descriptor string, Styles field  
**What it is:** One concise ordering for Suno's **Styles** field: primary genre, era or sub-genre, tempo and metre, lead instruments, vocal character, then production feel. It is an adapter template, not the song's creative authority. **Where it goes:** Custom Mode (the hub also calls it Advanced mode) has separate Lyrics, Styles and Title fields, an Instrumental toggle and Advanced Options, which hold Exclude and Vocal Gender. Simple Mode takes one description instead, for example "A synth pop song about having fun all night". **Suno's own advice:** be specific about genre, mood, BPM, vocal character and instrumentation. Its example sets "happy pop song" against "Bright pop track, 110 BPM, female vocals, chorus with big synth hook". The glossary says to "combine tempo terms with genres", "use dynamics to shape emotional intensity", "specify instrumentation", "layer production effects" and "blend genres creatively". The Style Influence slider (Loose to Strong) sets how closely a take follows the description. **Limits:** no official page states a character limit for the Styles, Lyrics or Exclude fields or for the Simple Mode description. The figures that circulate (240 characters for styles, 3000 for lyrics) come from user song titles on suno.com, not from Suno.  
**Effect on the audience:** Improves the odds that the generated take follows the intended palette, leaving less room for generic synthesizer filler and clichéd auto-tune tropes. It cannot eliminate unwanted elements by itself, which is the job of `suno.negative_style_tags`.  
**Used for and where it works best:** The Styles field of every Suno generation in Custom Mode, after the field names and behaviour are verified in the live interface.  
**Best in:** formats: All styles | genres: All  
**Avoid when:** Writing vague story prose in the style box, for example "a song about a sad king who lost his kingdom"; the style box only parses musical terms. That is the working rule; Suno does not state it, and its own advice lists mood beside genre, BPM, vocal character and instrumentation. The story belongs in the lyric.  
**Example:** `Styles: Mesopotamian folk metal, 110 BPM 4/4, heavy distorted guitars, live acoustic oud, aggressive growls and soaring clean tenor, cavernous reverb`  
**Source:** reference — Suno official pages, read 2026-09-23: How to Make a Song with Suno, https://suno.com/hub/how-to-make-a-song ; Make a song in Simple Mode, https://help.suno.com/en/articles/2462273 ; iOS Create: Custom Mode, https://help.suno.com/en/articles/3197377 ; Music Glossary for Suno, https://help.suno.com/en/articles/9010177 ; How to Use: Creative Sliders, https://help.suno.com/en/articles/6141377 .  
**Shelf life:** dated — the fields and advice as read on 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `lyria.semantic_natural_prompting` — The direction is narrative prose, not musical terms.  
`suno.style_prompt_formula`

---

### Negative Style Constraints

**Also called:** negative music prompting, anti-trope tags, Exclude field  
**What it is:** Naming what the track must not contain (electronic synths, auto-tune, trap drums, plastic production) instead of hoping the positive description implies it. Suno's documented route is the **Exclude** field under Custom Mode > Advanced Options, where you enter the "instruments, etc" you don't want: genres, instruments, voice styles. A 2024 release note showed exclusions written with a "-" prefix, for example -piano. Exclusions can also be stated in the Styles field. Bracketed forms there are examples, not a negative-prompt grammar Suno documents. Whether a take honours the list is tested on each take, not assumed.  
**Effect on the audience:** A take that honours the list strips away modern unwanted clichés (like 808 trap hi-hat rolls or plastic EDM bass) from ancient historical pieces. A take that ignores it is rejected and re-rolled, and stays part of the audit rather than being passed as constrained.  
**Used for and where it works best:** Historical, acoustic, orchestral, and traditional heritage music.  
**Best in:** formats: Heritage Music, Historical Film, Traditional Folk | genres: Heritage (civilisation-focused), Classical, Folk  
**Avoid when:** Electronic dance music or modern trap tracks where those elements are intended.  
**Example:** Documented: `Exclude: electronic synths, trap drums, auto-tune`. Also in Styles, bracketed form undocumented: `Acoustic Ancient Heritage, [No electronic synths, no trap drums, natural acoustic resonance only]`  
**Source:** reference — Suno official pages, read 2026-09-23: How do I exclude elements of a song, https://help.suno.com/en/articles/3161921 ; Release Notes (the "-" prefix, 2024), https://suno.com/release-notes .  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `suno.drop_and_bass_impact` — The modern electronic elements are wanted.  
`suno.negative_style_tags`

---

### Whispered & Sub-Vocal Delivery Direction

**Also called:** whisper hook, intimate sub-vocal tag, spoken bridge  
**What it is:** Directing an intimate section to be delivered as a whisper, as close-mic spoken word, as a low murmur or as a breathy intimate vocal. The documented route for vocal description is descriptive words in the Styles field (`suno.vocal_arrangement_tags`). Tags such as [Whispered Vocals], [Close-Mic Spoken Word], [Low Murmur], [Breathy Intimate Delivery], or a description inside a section tag, are community practice that Suno does not document.  
**Effect on the audience:** Drops dynamic volume suddenly, forcing the listener to lean in and creating intense psychological intimacy.  
**Used for and where it works best:** Secret confessions, sinister villain bridges, and contemplative intros.  
**Best in:** formats: Pop Ballad, Dark Drama, Noir Song | genres: Drama, Noir, Pop  
**Avoid when:** Roaring stadium anthems during full drum sections.  
**Example:** `[Bridge: Whispered close to microphone, no drums, solo cello drone] The river took the secret...` (community form, audition it)  
**Source:** reference — Suno official pages, read 2026-09-23: Can I choose the gender of the singer (vocal qualities in Styles), https://help.suno.com/en/articles/10153473 ; How to Make a Song with Suno, https://suno.com/hub/how-to-make-a-song . The whisper tags are on no official page.  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `suno.dynamic_energy_chorus` — A roaring stadium chorus over full drums.  
`suno.whispered_vocal_directing`

---

### Call-and-Response Vocal Structure

**Also called:** antiphonal singing, leader and choir, responsive chant  
**What it is:** Alternating lyric lines between a lead soloist and an answering chorus, each line labelled with who sings it. Suno's glossary lists Call and Response as a vocal-technique term. The speaker labels [Lead:] / [Response:], [Priest:] / [Temple Choir:] or [Leader] / [Choir], and parentheses for backing vocals, are community practice that Suno does not document.  
**Effect on the audience:** Generates powerful ritualistic, communal, and tribal energy; makes the song feel like an ancient communal event.  
**Used for and where it works best:** Modern antiphonal songs, stadium anthems, and heritage songs written as a modern interpretation. An ancient temple liturgy or a labour song on the Euphrates canals needs a named source before it is presented as one; it cannot be inferred from the call-and-response form.  
**Best in:** formats: Cultural Anthem, Heritage Hymn, Choral Epic | genres: Heritage (civilisation-focused), Folk, Religious  
**Avoid when:** Intimate, private solo diary songs.  
**Example:** `[Leader] Who built the great wall? / [Choir] We laid the black stone! / [Leader] Who holds the iron gate? / [Choir] We stand alone!` (community labels, audition them)  
**Source:** reference — Suno official page, read 2026-09-23: Music Glossary for Suno, https://help.suno.com/en/articles/9010177 . The speaker labels are on no official page.  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `suno.whispered_vocal_directing` — An intimate, private solo song.  
`suno.call_and_response_tags`

---

### Guttural & Battle Vocal Direction

**Also called:** war chant, growl tag, warrior roar  
**What it is:** Directing a visceral vocal intensity for a section: a guttural war cry, a rhythmic battle chant, a raw raspy delivery, primal screams. The documented route is descriptive words in the Styles field (`suno.vocal_arrangement_tags`). Tags such as [Guttural War Cry], [Rhythmic Battle Chant], [Raw Raspy Delivery] and [Primal Screams] are community practice that Suno does not document.  
**Effect on the audience:** Infuses the music with ferocious, blood-pumping warrior adrenaline suitable for epic warfare scenes.  
**Used for and where it works best:** Modern metal, trailer and fantasy battle scoring, and battle sequences of ancient empires (Assyrian conquests, Bronze Age clashes) as modern dramatic scoring. Do not present a generated growl or chant as authentic Assyrian, Akkadian or Bronze Age performance.  
**Best in:** formats: Epic Action, Metal, War Soundtrack | genres: War, Epic, Metal  
**Avoid when:** Children's songs or romantic serenades.  
**Example:** `[Verse: guttural rhythmic fantasy-war chant, pounding drums]` (community form, audition it) — historical authenticity claim: none.  
**Source:** reference — Suno official page, read 2026-09-23: Can I choose the gender of the singer (vocal qualities in Styles), https://help.suno.com/en/articles/10153473 . The battle tags are on no official page.  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
`suno.guttural_battle_directing`

---

### The Drop: Pause Before the Bass Release

**Also called:** the drop, bass drop tag, EDM climax, power release  
**What it is:** Engineering an acoustic pause followed by an explosive rhythmic release: a pre-chorus build, a beat of stopped sound, then the bass drop. Suno's glossary lists Drop and Break as structure terms, as vocabulary for the prompt. The bracket sequence [Pre-Chorus Build] -> [Silence / Beat Stop] -> [BASS DROP] is community practice that Suno does not document. [Pre-Chorus] on its own is a documented tag (`suno.structural_metatags`).  
**Effect on the audience:** Delivers a massive dopamine release and physical adrenaline rush on dance floors and short-form video hooks.  
**Used for and where it works best:** Modern electronic fusion, festival bangers, and high-energy TikTok / Reel edits.  
**Best in:** formats: Modern Social Reel, Electronic Pop, Trailer | genres: Electronic, Pop, Action  
**Avoid when:** Traditional historical acoustic purist documentaries.  
**Example:** `[Build up, rising snare roll] -> [Beat Stop: 1 beat] -> [MASSIVE DROP, heavy distorted sub-bass, 128 BPM]` (community form, audition it)  
**Source:** reference — Suno official page, read 2026-09-23: Music Glossary for Suno, https://help.suno.com/en/articles/9010177 . The drop sequence is on no official page.  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `suno.negative_style_tags` — An acoustic-purist historical documentary.  
`suno.drop_and_bass_impact`

---

### Song Extension at a Phrase End

**Also called:** Suno extend feature, seamless bar extension, track stitching  
**What it is:** When a song is continued from a chosen point of a returned take, setting that point at the exact end of a 4-bar or 8-bar musical phrase. **Length:** Suno makes up to 8 minutes per generation on v6, v6-wild and v6-mini, so Extend is for a longer piece or for continuing from a chosen point, not for reaching an ordinary song length. **Extend:** open the "..." menu, then Remix/Edit, then Extend. Drag the white arrow to choose how much of the original to keep, add lyrics and style, then use "Get Whole Song" to join the parts. **Replace Section** (Pro and Premier): highlight a span, edit its lyrics and click Recreate Section. You get two options, then a new full song. The current page gives no minimum or maximum span; a 2024 release note said 10-30 s, which is history. **Song Editor:** fades, crop and remove, extend, move and insert sections, and a tempo adjustment control.  
**Effect on the audience:** When the join works it has no seam: tempo, pitch and key carry over, and the listener hears one song. Check the join by ear, and reject or edit a take where tempo, pitch, key, lyric or timbre slips.  
**Used for and where it works best:** Long-form narrative concept songs, cinematic multi-movement suites, and replacing a weak later section while keeping a strong opening.  
**Best in:** formats: Concept Album, Extended Epic, Film Suite | genres: All  
**Avoid when:** Extending mid-word or in the middle of a complex drum fill, which causes jarring rhythmic hiccups.  
**Example:** `Extend from 02:14.500 (end of chorus bar 8) | Styles: same as the previous section | Lyrics: [Bridge] then the bridge lines` — then Get Whole Song.  
**Source:** reference — Suno official pages, read 2026-09-23: How long will my song be, https://help.suno.com/en/articles/13924929 ; How do I make my song longer, https://help.suno.com/en/articles/2409601 ; Can I replace a section of a song, https://help.suno.com/en/articles/3271873 ; How to Use: Song Editor, https://help.suno.com/en/articles/6141505 ; Release Notes, https://suno.com/release-notes .  
**Shelf life:** dated — the length limit and the editing tools as read on 2026-09-23. Re-verify extension availability and duration limits before execution and at least every 30 days.  
**Yields to:** `song_handoff.extended_suite_linking` — The long form is two tracks stitched, not one continued.  
`suno.extension_continuity`

---

### Hallucination & Truncation Prevention

**Also called:** lyric drift prevention, loop fix, clean enunciation  
**What it is:** Structuring lyrics into clear 4-line stanzas with balanced syllable counts so Suno is less likely to loop phrases or mumble garbled syllables. It is the project's working rule for lyric layout, not a documented engine behaviour. Suno publishes no limit for the Lyrics field (`suno.style_prompt_formula`).  
**Effect on the audience:** Every line has room to be sung, so each word has a better chance of landing clearly. Every take is still checked word by word against the lyric sheet, and a failed line is regenerated or replaced.  
**Used for and where it works best:** Every Suno lyric sheet. Keep stanzas to 4-6 lines maximum; never feed massive unbroken walls of text.  
**Best in:** formats: All songs | genres: All  
**Avoid when:** Dumping 500 words of prose into a single verse block, which invites the engine to mumble or invent phantom words.  
**Example:** `rule: Stanzas capped at 4 lines; a consistent syllable count per line (8-10 in an adult pop verse); punctuation marks at line ends to dictate phrasing.`  
**Source:** reference — the stanza rule is the project's own; no Suno page states it (Suno pages read 2026-09-23, https://suno.com/hub/how-to-make-a-song).  
**Yields to:** `suno.multilingual_phonetic_spacing` — The lyrics are Arabic, Sumerian or Akkadian: that card sets each line's spelling, spacing and syllable guidance in place of the figures here; the short-stanza layout still holds.  
`suno.hallucination_prevention`

---

### Definitive Outro & Ending Direction

**Also called:** song landing tag, fade out vs cold stop, big finish  
**What it is:** Choosing the exact ending and writing it on the last section: a cold stop, a big finish on a sustained final chord, a fade-out, or an acoustic outro that decays into room silence. [Outro] is a documented section tag (`suno.structural_metatags`). Ending tags such as [Cold Stop], [Big Finish: Sustained Final Chord], [Fade Out], [Acoustic Outro Decay] and [End] are community practice that Suno does not document. The documented way to fix an ending after generation is the Song Editor, which has fades, crop and remove.  
**Effect on the audience:** Provides psychological closure. The chosen ending is what the take is checked against, so a take that cuts off mid-measure or loops is caught and re-rolled, or its ending is fixed in the Song Editor.  
**Used for and where it works best:** The planned ending section of any track, its length set by the composition rather than by a fixed band.  
**Best in:** formats: All songs | genres: All  
**Avoid when:** Leaving the end of the lyrics open with no ending direction, such as an [End] or [Fade Out] tag (community tags) or a written outro.  
**Example:** `[Outro: Solo Oud softly plays the opening motif, decaying into natural room silence] [Cold Stop] [End]` (the description and the last two tags are community practice, audition them)  
**Source:** reference — Suno official pages, read 2026-09-23: How to Make a Song with Suno, https://suno.com/hub/how-to-make-a-song ; How to Use: Song Editor, https://help.suno.com/en/articles/6141505 . The ending tags are on no official page.  
**Shelf life:** dated — read 2026-09-23. Re-verify at least every 30 days.  
`suno.outro_and_ending_tags`

---

### Consistent Artist Persona Across Songs

**Also called:** Suno persona locking, vocal identity persistence, Voices, Style Personas, Custom Models  
**What it is:** Using Suno's current identity features, when available, plus one locked written voice-and-style brief pasted word for word on every song. Reusing text alone does not preserve vocal identity. **Voices** replaced the Personas button in Create, and "Style Personas remain available within Voices". A Persona saves "vocals, style, etc.", is public by default, and auto-fills the Style of Music field. A Voice is your own voice: 18 and over only, not available in every country, and only the owner can use it. The Terms forbid making a voice model of another person. Suno's pages disagree on the plan: the v5.5 blog says Pro and Premier, and the release note of 2026-08-07 says Voices is "available on free plans with expanded capabilities on paid plans". Both include Premier, the owner's plan. The Voices FAQ still says "the v5.5 model must be selected to use Voices", which the v6 FAQ's retirement of every pre-v6 model contradicts, so one of those pages is out of date. **Custom Models:** Pro and Premier, up to 3, trained on at least 6 of your own tracks whose rights you own, private, 2-5 minutes to process, and upgraded to v6 automatically. Suno's moderation blocks "names of well known artists or people".  
**Effect on the audience:** Helps a disclosed fictional act feel like one artist or band releasing a cohesive body of work, without claiming that prompt reuse guarantees one singer.  
**Used for and where it works best:** Serial concept albums, artist branding, and recurring musical theatre characters.  
**Best in:** formats: Concept Album, Musical Series, Brand Artist | genres: All  
**Avoid when:** Changing style descriptors randomly between songs on the same project album. And a persona built on a real singer's voice, whoever's it is: that is the voice-cloning case, and it stops at the same gate (`elevenlabs.voice_cloning_hygiene`, root SKILL.md §0) until that person has agreed.  
**Example:** `Styles: Band: The Babylonians | Mesopotamian folk rock, raspy male tenor, live acoustic oud and heavy bass` — pasted unchanged on every track, with the same Style Persona or Custom Model selected each time.  
**Source:** reference — Suno official pages, read 2026-09-23: What are Personas, https://help.suno.com/en/articles/3484161 ; Voices FAQ, https://help.suno.com/en/articles/11362433 ; Suno v5.5 blog, https://suno.com/blog/v5-5 ; Release Notes, https://suno.com/release-notes ; Using Custom Models, https://help.suno.com/en/articles/11362497 ; v6 FAQ, https://help.suno.com/en/articles/13924481 ; Terms of Service, https://suno.com/terms ; Does Suno moderate songs, https://help.suno.com/en/articles/3198209 .  
**Shelf life:** dated — the identity features as read on 2026-09-23, with two unresolved page conflicts. Re-verify in the app before execution and at least every 30 days.  
`suno.consistent_artist_persona`

---

### Instrumental Scratch Track Auditioning

**Also called:** instrumental mode, melody discovery, scratch backing  
**What it is:** Generating the backing track first with Suno's **Instrumental** toggle (Custom Mode) turned on, and auditioning harmonic arrangements before committing lyrics. Once a melody is chosen, **Add Vocals** puts vocals on an uploaded or generated instrumental, with an Audio Strength slider. The help page puts Add Vocals on Pro and Premier; the pricing page lists "Add vocals/instrumentals to existing songs" under Premier only. The two pages disagree on Pro; both include Premier, the owner's plan.  
**Effect on the audience:** Allows rapid discovery of breathtaking melodic themes and chord progressions without being locked to flawed AI vocal performances.  
**Used for and where it works best:** Pre-production songwriting: finding the perfect melody, then writing bespoke lyrics to fit its exact phrasing.  
**Best in:** formats: Songwriting Pre-Production, Film Underscore | genres: All  
**Avoid when:** Wanting rapid, all-in-one instant complete songs in a single click.  
**Example:** `Instrumental: ON -> generate 4 backing tracks (two generations) -> select best melody -> write lyrics to its exact phrasing -> Add Vocals on that track; where Add Vocals is not on the plan, regenerate with the lyric and the same Styles`  
**Source:** reference — Suno official pages, read 2026-09-23: iOS Create: Custom Mode, https://help.suno.com/en/articles/3197377 ; Add Vocals, https://help.suno.com/en/articles/6882817 ; Pricing, https://suno.com/pricing .  
**Shelf life:** dated — read 2026-09-23, with one unresolved page conflict. Re-verify at least every 30 days.  
**Yields to:** `suno.v55_fast_iteration` — You want a complete song in one click.  
`suno.instrumental_scratch_audition`

---

### Re-Roll & Variation Management

**Also called:** seed variation, generation iterations, prompt steering  
**What it is:** Methodically generating 4 to 6 takes of one prompt, noting what altered between them (tempo, energy, vocal inflection), and refining one keyword at a time. **Suno's facts:** "Each time you generate, you make two songs with a total cost of 10 credits". Suno documents no seed; the method works either way, because it compares takes, not seeds. The sliders are **Weirdness** (Safe to Chaos, default 50%), **Style Influence** (Loose to Strong) and **Audio Influence** (only with an audio upload). v6 adds **Variety**, which varies outputs "by adjusting and updating your style prompts"; at 0 you keep full control of the prompt. Hold every slider still while comparing, with Variety at 0, so the one keyword you changed is the only thing that changed.  
**Effect on the audience:** Prevents settling for a mediocre generic take. The finished song is the best of a compared set, not the first return, and there is a noted reason for the pick; it makes no percentile guarantee.  
**Used for and where it works best:** Quality control protocol on all hero project releases.  
**Best in:** formats: Hero Singles, Master Releases | genres: All  
**Avoid when:** Modifying 10 prompt variables simultaneously between takes, making it impossible to know which change caused the improvement.  
**Example:** `protocol: Variety 0, Weirdness 50% | 2 generations (4 takes) on an identical prompt; if vocals are too pop, add "raw acoustic, raspy" to Styles; 1 more generation (2 takes)`  
**Source:** reference — Suno official pages, read 2026-09-23: v6 FAQ, https://help.suno.com/en/articles/13924481 ; How to Use: Creative Sliders, https://help.suno.com/en/articles/6141377 .  
**Shelf life:** dated — the credit cost and sliders as read on 2026-09-23. Re-verify before any paid run and at least every 30 days.  
**Yields to:** `lyria.api_batch_synthesis` — Variations auditioned programmatically, not by hand; that card says what Lyria 3.5 documents about batches and seeds.  
`suno.reroll_variation_control`

---

### Multilingual Phonetic Spacing for a Song Engine

**Also called:** non-English phonetic pacing, Arabic lyric spacing, Arabic lyrics in Arabic script  
**What it is:** Writing non-English lyrics for Suno in the language's own script (Arabic in Arabic letters, with vowel marks on any word that could be misread), keeping every square-bracket tag and direction in English, then checking the first take line by line by ear. A language with no script Suno can take, such as Sumerian or Akkadian, is written in Latin transliteration. Extra spacing, hyphenation or Latin-letter respelling is the repair for one word a take mispronounces, applied to that line only and re-rolled, not a first step. The English-brackets rule and Arabic in its own script are the owner's working practice on Suno Premier (reported 2026-09-23); the respelling repair is the project's own method, to test. **What Suno states about languages:** only that "Suno works with multiple languages, including English". No official page lists supported languages or says anything specific about Arabic; the Arabic tracks on suno.com's Arabic style page are user-made and are not a statement of support. An inline direction inside the lyric line, such as [slow cadence], is community practice that Suno does not document; Suno's v4.5 article on prompting in the lyrics now returns 404.  
**Effect on the audience:** Reduces mangled non-Latin pronunciation and keeps an authentic cultural singing cadence.  
**Used for and where it works best:** Writing Arabic, Sumerian, Akkadian, or Latin lyrics for Suno.  
**Best in:** formats: Heritage Music, World Music | genres: Heritage (civilisation-focused), Arabic, World  
**Avoid when:** Writing a direction inside the brackets in Arabic or any language other than English; or rewriting a whole Arabic lyric in Latin letters before any take has shown a word going wrong.  
**Example:** `[Verse 1]` above the verse lines in Arabic script, vowel-marked where a word could be misread, then `[Chorus]` above the chorus lines; every bracket in English. If a take mispronounces one word, that word alone is respelled (hyphenated, or in Latin letters) on that line and the line is re-rolled.  
**Source:** reference — Suno official pages, read 2026-09-23: How to Make a Song with Suno, https://suno.com/hub/how-to-make-a-song ; Create in V4.5: Better Prompts in Lyrics (404), https://help.suno.com/en/articles/5782977 . The owner's working practice on Suno Premier, reported 2026-09-23 (English brackets, lyrics in their own script). The respelling repair is the project's own.  
**Shelf life:** dated — the language statement as read on 2026-09-23. Re-verify at least every 30 days.  
**Yields to:** `lyria.syllable_timing_sync` — Classical metre that must land on the downbeat; that card says what Lyria 3.5 documents about timing and languages.  
`suno.multilingual_phonetic_spacing`

---

