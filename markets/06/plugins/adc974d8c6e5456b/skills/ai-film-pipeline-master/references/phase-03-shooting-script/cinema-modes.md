# The five live-action cinema modes

A camera grammar, picked once per sequence and then applied to every shot in it. Taken from the
owner's own production master, which is not otherwise used here: that file is a complete
nineteen-phase engine doing the same job as this skill, and two engines in one folder is the
defect this project keeps repairing. These ten sections are craft and stand on their own.

Pick the mode from the table, paste its block into the shot plan, and let it settle the movement,
the light and the grade for the whole sequence instead of deciding them shot by shot. The stacking
section at the end is for a sequence that crosses between worlds.

**The lens entries here are intent, not a lock.** The focal length, the glass and the sensor are
optical decisions and Phase 7 owns them, under its Slot 3; a mode names the *look* it wants — period
texture, clean sharpness, a long lens that separates the subject — and Phase 7 turns that into
glass. Paste the block, keep the intent, and let Phase 7 set the number. The single-ownership rule
this follows is in [HOW-PHASE-3-WORKS.md](./HOW-PHASE-3-WORKS.md#1-single-decision-ownership-the-law-of-shot-setup).

**There is a sixth mode, in two forms, and it is not in this file.** M6 Animation — drawn and M6-R Animation — rendered live in
[HOW-PHASE-3-WORKS.md §3](./HOW-PHASE-3-WORKS.md#3-the-6-cinema-modes-m1-to-m6), with M1 to M5, in
one table. It is absent here because every section below is built on things an animation piece does
not have — a camera body, a lens, a filter, a film stock — so there is no drop-in block to write for
it. If the piece is drawn or rendered rather than photographed, take the mode from that table and do
not try to fit it to one of the five here.

---

# THE 5 LIVE-ACTION CINEMA MODES (M1-M5) — Universal Camera Grammar

Five cinema modes shared across all video workflows. All five use ARRI bodies and either Panavision Ultra Vintage anamorphic or Cooke S4/i spherical glass. The differences are in **movement, filtration, grade, palette, and texture** — not in body or lens family.

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Mode-select table](#mode-select-table)
- [M1 — Narrative (canonical drop-in block)](#m1-narrative-canonical-drop-in-block)
- [M2 — Studio/Editorial (canonical drop-in block)](#m2-studioeditorial-canonical-drop-in-block)
- [M3 — Action/Combat (canonical drop-in block)](#m3-actioncombat-canonical-drop-in-block)
- [M4 — Performance/Concert (canonical drop-in block)](#m4-performanceconcert-canonical-drop-in-block)
- [M5 — Atmospheric/Empty (canonical drop-in block)](#m5-atmosphericempty-canonical-drop-in-block)
- [Lens length guide (across all modes)](#lens-length-guide-across-all-modes)
- [Lighting principles for M1, M3 and M5 (the lived-in modes)](#lighting-principles-for-m1-m3-and-m5-the-lived-in-modes)
- [60:30:10 color rule by mood](#603010-color-rule-by-mood)
- [Stacking modes (multi-world sequences)](#stacking-modes-multi-world-sequences)

<!-- /GENERATED:toc -->

## Mode-select table

| Mode | Scene type | Body | Lens | Movement | Filter | Grade |
|------|-----------|------|------|----------|--------|-------|
| **M1 Narrative** | Real-world dramatic (streets, kitchens, cars, bars, interiors, exteriors). "Lived in." | Alexa 35 | Panavision Ultra Vintage 2x anamorphic 40/55/75/100mm T2.3 | Handheld, slight breath, occasional slow dolly | Tiffen Black Pro-Mist 1/4 | Kodak Vision3 250D (EI 250), teal-amber split |
| **M2 Studio/Editorial** | White void, clean studio, hyperpop set, fashion film, editorial portrait | Alexa Mini LF | Cooke S4/i spherical 32/50/75/100mm T2 | Locked + optional 4-6 inch slow push | Tiffen Black Pro-Mist 1/2 + Glimmerglass on chrome/rhinestone | Saturated editorial, pushed magentas or pastels, warm-retained blacks, 400 ASA |
| **M3 Action/Combat** | Combat, chase, stunts, war, mech battles, alien encounters, debris, smoke, dust | Alexa 35 | Panavision Ultra Vintage 2x anamorphic 40/55/75/100mm T2.3 | Handheld + shaky throughout, NO stabilized shots, often orbital around figures | Tiffen Black Pro-Mist 1/4 | Kodak Vision3 250D (EI 250), daylight overcast or scene-appropriate palette, dusty haze |
| **M4 Performance/Concert** | Stadium, arena, stage, jumbotron, lightstick crowd, festival pit | Alexa 35 | Panavision Ultra Vintage 2x anamorphic 40/55/75/100mm T2.3 | Mixed handheld pit-photographer + shaky + orbital, hard cuts | Tiffen Black Pro-Mist 1/4 | Kodak Vision3 250D fine grain, desaturated cool tones with warm bloom, stage-lighting color cast, heavy haze, sweat sheen |
| **M5 Atmospheric/Empty** | Abandoned environments, no-humans plates, landscapes, weather plates, mood/world establishing | Alexa Mini LF | Panavision Ultra Vintage 2x anamorphic 35→85mm push range T2.3 | Locked-off or extremely slow push-in/pull-back | Tiffen Black Pro-Mist 1/4 | Kodak Vision3 250D (EI 250), palette-driven (specify hex values per scene) |

The photographic modes above default to **24fps with a 180° shutter** for cinema-standard motion
blur — a default, not a rule, and **the frame rate is not this file's to fix.** It is owned by the
`look.fps_*` cards in
[`../phase-07-image-prompt-engineering/image-format-texture.md`](../phase-07-image-prompt-engineering/image-format-texture.md),
and a piece going out over broadcast, a sports or live cut, or anything shot against screens and
mains-frequency lighting takes a different row and overrides this line without argument.

## M1 — Narrative (canonical drop-in block)

```
Shot on ARRI Alexa 35 in ProRes 4444 LogC4, Panavision Ultra Vintage 2x anamorphic [XX]mm at T2.3 with Tiffen Black Pro-Mist 1/4 filter, handheld with natural breath and slight shake, photoreal cinematic grit with oval bokeh and horizontal streak flares, warm anamorphic falloff toward frame edges, Kodak Vision3 250D film emulation grade with slight halation on highlights and its native grain structure, teal-amber color split with cool teal-blue shadows and warm amber highlights, organic lens breathing on focus racks, shallow depth of field, 24fps base shutter 180 degrees, total runtime roughly [XX] seconds.
```

Replace `[XX]` with lens length (40mm wide, 55mm medium, 75mm tight, 100mm close-up) and runtime.

## M2 — Studio/Editorial (canonical drop-in block)

```
Shot on ARRI Alexa Mini LF in ProRes 4444 LogC4, Cooke S4/i spherical prime [XX]mm at T2 with Tiffen Black Pro-Mist 1/2 filter, locked-off tripod with optional 4-to-6 inch slow push-in, photoreal editorial fashion film aesthetic with gentle halation bloom on highlights and soft warm falloff in the Cooke signature, fine 400 ASA film grain structure retaining warmth in the shadows, highlights allowed to bloom slightly around fabric and chrome surfaces, saturated editorial grade with warm-retained blacks not crushed to pure black, slight skin tone warmth from the Cooke color rendition, 24fps base shutter 180 degrees, total runtime roughly [XX] seconds. Not CGI, not plastic, shot-on-film analog aesthetic with real-world lens character.
```

For rhinestone/chrome/surface-detail close-ups, append: `Glimmerglass diffusion added to the front element to bloom highlights on reflective surfaces.`

## M3 — Action/Combat (canonical drop-in block)

```
Shot on ARRI Alexa 35 in ProRes 4444 LogC4, Panavision Ultra Vintage 2x anamorphic [XX]mm at T2.3 with Tiffen Black Pro-Mist 1/4 filter, all camera work is handheld and shaky throughout with constant operator micro-jitter, reactive movement, and chaotic shake, no stabilized or locked-off or dolly-smooth shots anywhere, gritty documentary-meets-sci-fi war film aesthetic with no stylization and everything grounded in physical realism, Kodak Vision3 250D film emulation with its native grain structure, [palette descriptor] with dusty atmospheric haze, slight halation on highlights, 24fps base shutter 180 degrees, total runtime roughly [XX] seconds.
```

Replace `[palette descriptor]` with scene-appropriate language ("daylight overcast palette," "golden hour warm palette," "blue-hour cool palette," "stormy desaturated palette").

For slow-motion impact moments, append: `intercut a 96fps high-speed slow-motion frame at the [moment], holding shutter at 180 degrees for natural motion blur even in slow motion.`

## M4 — Performance/Concert (canonical drop-in block)

```
Shot on ARRI Alexa 35 in ProRes 4444 LogC4, Panavision Ultra Vintage 2x anamorphic [XX]mm at T2.3 with Tiffen Black Pro-Mist 1/4 filter, mixed handheld pit-photographer energy with rapid handhelds and shaky low-angle operator work and orbital handheld passes around the performers, hard cuts between angles, no stabilized or locked-off shots, photoreal concert documentary aesthetic, Kodak Vision3 250D film emulation with fine grain structure overlaid throughout, slightly desaturated cool tones with warm highlight bloom and deep blacks holding shadow detail, [stage-lighting color cast descriptor], heavy volumetric haze with dust suspended in every beam, real sweat sheen on skin and real fabric darkening from exertion, gentle halation on light sources, 24fps base shutter 180 degrees, total runtime roughly [XX] seconds.
```

Replace `[stage-lighting color cast descriptor]` with scene-appropriate language ("magenta-red color cast from the LED cube above," "amber and ultraviolet wash from side rigs," "cyan and white strobe punching through warm tungsten").

## M5 — Atmospheric/Empty (canonical drop-in block)

```
Shot on ARRI Alexa Mini LF in ProRes 4444 LogC4, Panavision Ultra Vintage 2x anamorphic [XX]mm at T2.3 with Tiffen Black Pro-Mist 1/4 filter, locked-off or extremely slow push-in motion only, no handheld energy, photoreal atmospheric environment plate aesthetic, Kodak Vision3 250D film emulation with its fine native grain structure, palette-driven grade with [palette descriptor] and hex values [list 4-8 hex values from the user's palette], strong negative space, deep depth of field, light atmospheric haze with dust particles suspended in air, weathered material detail with oxidized metal and dust-covered glass and cracked paint and moisture stains, slight anamorphic flares on any directional light sources, 24fps base shutter 180 degrees, total runtime roughly [XX] seconds. No humans, no silhouettes, no living beings — the environment is the subject.
```

Replace `[palette descriptor]` with words ("cold greys, steel blues, muted greens, warm rust accents") and `[list of hex values]` with actual color codes (e.g., `#5f6468, #eaebee, #181819, #6f757a`).

## Lens length guide (across all modes)

- **32mm / 35mm / 40mm**: Wide establishing, full-body, group framing, environmental context
- **50mm / 55mm**: Medium portrait, two-shot, waist-up, dialogue framing
- **75mm**: Tight editorial portrait, single-character isolation, performance close-up
- **85mm / 100mm**: Extreme close-up — eyes, lips, jewelry, fabric texture, surface detail

When in doubt: 55mm (M1/M3/M4) or 50mm (M2) for medium framing. M5 typically uses the wider end (35→55mm).

## Lighting principles for M1, M3 and M5 (the lived-in modes)

- **Practicals first.** Lights visible in frame: lamps, windows, screens, candles, neon signage. Keep film fill, reflectors, softboxes, LED strips and overhead bounce out of these three modes — they are what makes a frame read as lit rather than found. **M2 Studio/Editorial and M4 Performance are shaped light by definition** (softbox, beauty dish, stage rig) and this bullet does not apply to them; nor does it apply to product, packshot or M6 animation work.
- **Shoot from the shadow side.** Position camera on the darker side of the subject so practicals motivate the eye-light and rim naturally.
- **Atmospheric haze.** Present by default in M1, M3, M4 and M5; light volume, no god rays, no visible light beams. **Not in M2, not in product work, and not in bright 2D/3D animation**, where haze reads as a dirty render rather than as air.
- **Forbid screen blue spill** on skin when monitors are in frame.
- **Mood-driven palette** using 60:30:10 split (main / accent / pop).

## 60:30:10 color rule by mood

| Mood | Proportion |
|------|-----------|
| Cold conflict / tension | 60% cool blue + 30% concrete grey + 10% red accent |
| Warmth / intimacy | 60% warm tungsten + 30% deep brown + 10% amber |
| Danger / panic | 60% deep red + 30% black + 10% sodium orange |
| Sci-fi / tech | 60% black + 30% cool grey + 10% accent (purple / cyan) |

## Stacking modes (multi-world sequences)

If a sequence cuts between two worlds (e.g. white void M2 intercut with kitchen M1, or action M3 intercut with performance M4), **write each shot's camera block separately according to its mode.** Don't blend the specs into one averaged grade. The cut between modes is the visual punch; collapsing them kills the contrast.

For multi-shot sequences in the same mode: one continuous prompt with hard-cut triggers in the Dynamic Description and a single shared camera block.

---

<a id="20-character-performance"></a>
