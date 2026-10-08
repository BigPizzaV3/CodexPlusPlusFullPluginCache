# ShotPulled knowledge base — rule index

Every rule the engine can cite, by id. This is the map, not the territory:
call `get_rule` with an id for the full text before quoting it or leaning on it.

Generated from the shipped knowledge base — 47 rules.

## Principles — these override everything below

- `P1` — Taste is the verdict.
- `P2` — Yield is the primary extraction lever — *when flow is clean.
- `P3` — Coarse-first.
- `P4` — One variable per shot.
- `P5` — Pressure is a byproduct, not a target.
- `P6` — Grind is the right lever when the puck misbehaves.

## Bean categories — where to start, by roast and process

- `CAT.NORDIC` — *Light / Nordic, fresh.* Grind near or just past traditional; ratio 1:2.5–1:3; ~15–22 s; ~90–94 °C.
- `CAT.ULTRALIGHT` — *Ultra-light (e.g.
- `CAT.PROCESSED` — *Heavily processed (anaerobic / co-ferment / extended ferment).* Coarse; conservative yield ~1:2; lower temperature.
- `CAT.CLASSIC` — *Medium / traditional espresso roasts (chocolate, nut, caramel profiles).* The textbook baseline: ratio 1:1.8–1:2.2 in ~25–32 s at 92–94 °C, traditional ~9 bar.
- `CAT.DARK` — *Dark / Italian.* Grind **coarser than tradition** (brittle beans shatter into more fines) but **not** a turbo shot: tight ratio 1:1.5–1:2, real contact time, ~9 bar, sub-90 °C.
- `CAT.AGED` — *Well off-roast / degassed.* Lost CO₂ → faster flow and less resistance.

## Diagnoses — a taste symptom mapped to its likely cause

- `DX.SOUR_CLEANFLOW` — Clean, fast flow + sour/under-extracted → **push yield** (P2).
- `DX.BITTER_TAIL_FASTFLOW` — Fast/uncontrollable flow + bitter tail from yield overshoot → **grind finer** to rebuild resistance and regain control of the cut (especially for milk drinks).
- `DX.CHOKE_BLOND` — Slow flow, the puck "pushes hard," or the stream blonds mid-shot, or time is well past the category window → **grind coarser** (too much resistance → uneven over-extraction).
- `DX.ASTRINGENT_FINISH` — Normal flow but a dry / woody / astringent / "face-wrinkle" finish → **cut yield earlier / hard stop** — you collected the tail.
- `DX.TERMINAL_BEAN` — Going coarser strips sweetness *without* removing the bitterness → the bitterness is in the bean/age, not the brew.
- `DX.CHANNEL_SQUIRT` — A brief side-squirt from the puck = localized channeling → fix distribution/prep, not the grinder.
- `DX.TIGER_STRIPES` — Tiger striping in the stream = even extraction.
- `DX.PUCK_IMPRINT` — A screen/screw imprint on the **dry** puck = too much coffee (dose down).
- `DX.MILK` — Milk masks brightness/florals and *exposes* bitter tails.
- `DX.SOUR_BITTER_TOOFINE` — Sour AND bitter in the same cup (or a muddy/hollow/harsh cup) = heterogeneous extraction from grinding too fine: channels over-extract while the rest of the puck under-extracts.
- `DX.PERCEIVED_DRY` — A dry/astringent impression on a tight ratio / short yield is usually imbalance misread as astringency → nudge yield **up** slightly.
- `DX.BLONDING_LIGHT` — Light roasts blond almost immediately — blonding there is **not** an extraction cue and says nothing about under-extraction.
- `DX.SPLIT_CUP` — To preview a longer ratio without wasting a shot, don't stop the machine at target: catch the extra grams in a second cup, taste the main cup, then stir the extra back in and taste again.
- `DX.TOO_FRESH` — A bean younger than its rest window still holds CO₂ that blocks diffusion: extra puck resistance, roasty/carbony harshness, and perceived astringency that dialing cannot remove.
- `DX.TEMP_LEVER` — Temperature is a real lever when moved meaningfully (≥2 °C): cooler trims bitterness/harshness on darker, processed, and aged coffees; hotter helps a very light roast that stays under-extracted after yield and grind moves.
- `DX.DOSE_TRIM` — Keep dose constant while dialing.
- `DX.UNDERFILL` — A clearly underfilled basket brews thin, weak-textured shots even when the taste balances.

## Mechanisms — why the machine behaves as it does

- `MECH.CO2` — CO₂ is a major source of puck resistance besides grind size; it off-gasses over days after roast, so the same setting flows faster as a bag ages.
- `MECH.FINES_ROAST` — Darker / more-developed roasts are more brittle → produce more fines at the same setting → more resistance.
- `MECH.SEQUENCE` — Extraction order is roughly acids → sugars → heavy bitter/woody compounds.
- `MECH.PRESSURE_EQ` — Pressure = input flow rate × puck resistance.
- `MECH.BURRS` — Conical and flat burrs produce different particle distributions; grind settings do **not** transfer 1:1 across grinders.
- `MECH.NO_MICRONS` — A dial position is **not** a particle-size in microns.
- `MECH.MELANOIDIN` — Coffee has no tannins; astringency rides on phenolic-bearing melanoidins that extract late and slowly, so real astringency tracks *high* extraction — the remedy is less extraction: cut yield first, then temperature.
- `MECH.FLOW_DEBIT` — A machine's unperturbed water debit (~4.5–8 g/s) dictates low-resistance shot behavior: the same recipe pulls different times and pressures on different machines, so time targets are machine-relative, never absolute.
- `MECH.VOLCANO` — Grinding finer raises extraction only up to a peak; past it, channeling makes NET extraction fall while harshness rises.
- `MECH.CREMA` — Crema is CO₂/surfactant foam — a marker of roast darkness and freshness, not of quality — and it is the most bitter fraction of the cup.
- `MECH.EY_SWEETSPOT` — Pleasant aromatics peak around ~18–19% extraction yield; pushing past ~20–22% concentrates bitter/skunky compounds and mutes aroma.

## Techniques — puck prep and handling

- `TECH.WDT` — Distribute deep, not just the surface: a blind shaker/tumbler or fine-needle WDT (~0.3 mm, stirred from the basket floor up) breaks clumps through the whole bed; wedge levelers only touch the top half.
- `TECH.PAPER_BOTTOM` — A paper filter at the basket bottom speeds flow and raises extraction noticeably, removes flecking/fines from the cup, and permits a finer grind without clogging — useful against fines-driven dryness.
- `TECH.PUCK_SCREEN` — A top puck screen gives a small, consistent extraction gain: better water dispersion and no puck jump when pressure releases at the end of the shot.
- `TECH.TAMP_BINARY` — Tamping is binary: press level until the bed stops feeling squishy — pressing harder or twist-polishing changes nothing.
- `TECH.PINCH_TEST` — Pinched grounds should feel sandy and hold peaks; if your fingerprints show in the pinch, the grind is powder-fine — too fine as a starting point.
- `TECH.PURGE` — After a grind change, purge a few grams (grinder-dependent) so retained grounds at the old setting don't contaminate the test shot; low-retention single-dosers excepted.
- `TECH.PREP_SCALE` — Prep rigor matters more the finer you grind; coarse pucks are forgiving.
