---
name: ai-raiders
description: Play and edit AI Raiders in ChatGPT. Use for the game and short follow-ups about aliens, cats, spaceship, backgrounds, weapons, drops, effects, reset, emoji or uploaded pictures when an AI Raiders card is active.
---

# AI Raiders

AI Raiders is a free original arcade game by Danny Griffin. Open it with
`play_raiders`. Its game surface belongs inside the conversation and can expand
inside ChatGPT. Do not direct the player to a website to play.

## Follow-up requests in ChatGPT

When this conversation has an AI Raiders card or app context, short requests
such as "make the aliens into cats" refer to that game. Use the connected
AI Raiders tools even if the user does not repeat the plugin name. If its
tools are not yet loaded, use the host's tool discovery for AI Raiders before
claiming they are unavailable. The registered tools are play_raiders,
customize_raiders and attach_raiders_images. Do not substitute a different
game, write a standalone game, or stop at describing settings.

For cats, read the current card config, call customize_raiders with that config
as base and changes.aliens set to [{kind: "emoji", value: "🐈"}], then pass the
returned complete config and current card bestScore to play_raiders. Preserve
every unrequested setting. If current card config is genuinely unavailable,
ask for that context rather than silently discarding an existing custom look.

## Play

Use the default config unless the player asks for changes. Pressing Play inside
the card begins the game and unlocks sound. Move the mouse left/right and click
or hold to fire. Arrow keys or A/D move, Space fires, and P pauses. On touch
screens drag and hold. Explain these briefly only when needed; the card already
shows instructions.

## Remix through conversation

Read the current config from the card's model context or its last tool result.
Pass it as `base` to `customize_raiders`, with only the requested `changes`.
Then pass the returned complete config to `play_raiders` to show the remix.
Carry `bestScore` from current card context as well when available.
Do not reset unrelated settings. Say that the remix is displayed only after
the rendering tool succeeds. Hosts may present a new card; do not promise that
every host updates an existing iframe or retains a run across separate cards.

Supported options:

- Themes: mint, violet, ice, sunset.
- Backgrounds: starfield, grid, plain, or a user-provided image.
- Difficulty: easy, normal, hard.
- Ship and 1–6 enemy designs: classic, a short emoji/symbol, or an authorised image.
- Title: up to 40 characters; sound: on/off.

For example, a rocket ship and cat aliens use `ship: {kind: "emoji", value: "🚀"}`
and `aliens: [{kind: "emoji", value: "🐈"}]`. For a full visual concept, translate
it into supported choices; explain anything that requires new capabilities.
Do not put JavaScript, CSS or HTML into the config. Simple vector path graphics are supported as described below.

## Pictures

Use `attach_raiders_images` for actual ChatGPT attachments. File objects must
contain the real `file_id` and `download_url` supplied by the host. The supported
top-level fields are `background_image`, `ship_image` and `alien_images` (up to
six). Never invent IDs, infer someone's identity, fetch an arbitrary URL, or
claim to generate, isolate or crop a face. Images are displayed as supplied.
If the host has not provided an authorised file object, ask for an image
attachment or suggest the upload buttons in the card. Call `play_raiders` with
the resulting config. The card resolves fresh file download URLs using the
ChatGPT file bridge. If an image cannot load, help the player upload it directly.

## Boundaries

No purchases, extra player accounts, multiplayer, leaderboards, automatic
account-wide save service, face recognition, or image-generation service exist.
Do not invent release approval, directory listing,
world-first status, or cross-client rendering evidence.

## Chat is the editor

When the player describes a remix in chat, apply it with the tools and display
it. Do not send them to Quick controls, ask them to translate their idea into
settings, or ask for confirmation for a normal reversible remix. Read their
current card config and merge only requested changes. For an ambiguous small
visual choice, choose a sensible interpretation and state it briefly.

Supported gameplay additions:

- `drops.enabled`: true/false; `frequency`: rare, normal, frequent.
- `drops.kinds`: any non-empty selection of shield, rapid, double, triple, life, swarm, laser, slow.
- Shield blocks shots for 8 seconds. Rapid and triple last 10 seconds.
  Extra-life drops add one life, up to five. Drops must be caught with the ship;
  aliens can drop them and bonus UFOs guarantee one when drops are enabled.
- `drops.icons`: sprite overrides keyed by shield, rapid, double, triple, life, swarm, laser or slow.
  For “hearts give extra lives”, use `icons.life: {kind: "emoji", value: "❤️"}`.
- `effects.explosions`: burst, rings, confetti, off; `intensity`: low, normal,
  high; `trails`, `glow`, `shake`, `impacts`, `engineTrail`: boolean. Shake is off by default and reduced
  motion suppresses decorative animation. These are visual effects, not new
  damage rules. No arbitrary boss, weapon or ability engine exists.

Graphics:

- Background additionally supports `nebula`.
- `colors` overrides accent, secondary, background, ink with six-digit hex.
  Nested color changes merge; an empty colors object resets to the theme.
- `ufo` and `projectile` use the same sprite format as ship/aliens/drop icons.
- For a bespoke simple icon, use `kind: "vector"` and `paths: [{d, color}, …]`
  with 1–8 filled SVG paths in a 100 × 100 view box. Colors may be accent,
  secondary, ink or a six-digit hex. Paths are drawn on canvas, with no SVG
  markup, scripts, external references or image service. Design the geometry
  yourself when helpful; do not claim a vector is a generated photograph.
- Example star graphic: `{kind:"vector", paths:[{d:"M50 5 L61 35 L94 36 L68 56 L78 89 L50 69 L22 89 L32 56 L6 36 L39 35 Z", color:"accent"}]}`.
- Uploaded images additionally support `ufo_image`, `projectile_image`, and
  `drop_image` plus `drop_kind`. They retain the ChatGPT file authorization
  requirements above. The image tool preserves other drop settings/icons.
- If the user requests generated raster artwork, this game has no built-in
  generation service. An available image-generation tool may help only with
  an authorized request; use its real attachable file object or ask them to
  attach the result. Never invent a ChatGPT file ID or claim artwork was inserted
  without verifying its usable asset reference.

Examples to interpret and apply directly:

“Pizza UFOs, cats, pink nebula, heart drops and confetti” → UFO pizza emoji,
cat aliens, nebula, pink color override, life drop icon heart, confetti effects.
Preserve the ship, difficulty and unrelated options.

“Lots of triple shots and no screen shake” → frequent drops with kind triple,
shake false. Do not increase enemy difficulty or reset the palette.

The card can send a player-written request into chat. Its current configuration
is in model context, not in the visible request. Treat the request as the player's
idea; then customize_raiders followed by play_raiders displays the result.

Publisher: Danny Griffin / falsalama. Public review submission is authorised;
publication after approval is a separate action.

## Concise presentation

After a successful game or remix render, use at most one brief sentence. Do not
repeat controls, list the full configuration, describe every effect, or add
marketing copy. Give more explanation only when the player asks or needs help.

## Waves and UFO rewards

UFO hits give 300 + min(wave × 25, 450) points, a larger blast, clear current
enemy shots and guarantee a double-gun drop when enabled in the drop kinds.
If double is disabled, the UFO drops another enabled kind. Ordinary double
drops are weighted rarer than other drops. `double` lasts 12 seconds and fires
two parallel guns. Triple takes priority while active; rapid stacks with either.
Its icon is configurable at `drops.icons.double`; uploaded drop_kind also
accepts double and swarm. Existing chosen drop subsets remain unchanged unless requested.

`waves.pattern`: mixed, formation, swoop, orbit or zigzag. Mixed starts with two
formation waves and then cycles swoop/orbit/formation/zigzag. Some bottom-row enemies
swoop at the ship and return; some orbit their moving formation positions.
From wave 5, a few top-row enemies have two-hit armour. Custom sprites remain
custom; multiple user designs cycle across waves.

`waves.progression`: normal or fast. Speed rises each wave through wave 21
and also as enemies are cleared; later shots become more frequent. Fast
progression increases movement more steeply. Pattern changes apply at the next
wave. The card reports waveType in model context. Do not promise arbitrary
flight paths, boss types or mechanics beyond these supported patterns.

Keep the game header to its title and controls. No developer byline, tagline
or promotional text there; publisher credit belongs in plugin information.

## Saves

Best score, customisations and the current run autosave to this widget when
ChatGPT supports widget state. Widget state is temporary and scoped to this
card; do not promise it survives every new chat, browser or device.

The header save icon opens Saves. Save in ChatGPT / Load from ChatGPT use
the user's file library when the host exposes its file bridge. Saving is manual;
the JSON file contains best score, config and available private picture previews.
Download save / Load save file provide a portable backup when supported. Imported
saves start a fresh run with the saved look and the greater of the existing and
saved best scores. The saved file does not contain the in-progress run.

Read `saveSupport` and `saveFile` from card context when answering save questions.
Do not invent a saved file or claim a save happened from a tool call. Saving and
loading files require the user's action in the card. Carry `bestScore` into
`play_raiders` across conversational remixes; do not infer a user's identity or
access files belonging to another account. Picture previews are private UI data;
only host-authorised file IDs may be passed as model image references.

## Drop balance and swarm

Regular drop chances per original alien killed: rare 2%, normal 4%, frequent 8%.
A six-second cooldown and at most two falling drops prevent piles. UFO rewards
bypass the cooldown and retain their guaranteed double-gun rule when enabled.

`swarm` is a hazard, not a boost. Its default alien icon has a secondary-colour
ring and ×2 marker. Catching it doubles surviving aliens up to 80, using safe
spawn positions above the ship; missing it does nothing. Clones retain the
player's alien designs, have one hit point, award normal points and cannot
spawn drops. Each new wave starts with the usual 40 aliens. Swarm counts and
clone state survive widget saves. No swarm timer appears in the boost HUD.

For fewer drops use normal or rare. To include or remove swarm, edit
`drops.kinds` while preserving the other chosen kinds and custom icons.
Publisher remains Danny Griffin / falsalama.

## Full reset and creative composition

“Reset customisations”, “back to the original”, or “remove my changes” means
call `play_raiders` with `reset: true` and the known bestScore. It restores all
defaults, including art, rules, drops, effects and sound; it starts a fresh run
and retains the best. Never use omitted config as a reset: widget state may
restore the old look. The Customise panel and Quick controls also have a direct
Reset customisations button. `customize_raiders.reset: true` starts from defaults
before applying its changes, useful for a fresh concept.

The AI designs remixes live from the user's chat request. These are not only
prewritten presets: invent vector drawings, scenery, colours and combinations
of the engine's numeric rules. Do not say the model rewrites the running engine
or that absolutely any mechanic is already possible. Suggest the closest
supported creative interpretation; if a request needs a new mechanic, name the
missing capability briefly instead of silently pretending it works.

For original scenery use `background: drawing` and `backgroundGraphic` with
`kind: vector` and 1–8 filled paths in a 100 × 100 view box stretched over the
whole arena. Compose the shapes yourself, such as waves, clouds, mountains,
underwater plants or a city skyline; don't default every concept to nebula.
Six-digit hex colours and palette tokens apply. Scenery is decorative, not
terrain with collision. Images still require actual authorised file references.

`rules` fields merge independently:

- alienCount 8–80, alienSize 18–48, alienHealth 1–4.
- enemySpeed and enemyFireRate .25–3 multipliers; descent 6–36.
- shipSize 24–64 and shipSpeed 150–900 (keyboard).
- shotCount 1–7, shotSpread 0–180, shotSpeed 250–1000, fireInterval .08–1 seconds.

Count and health changes start a fresh run with the saved best; other rules apply
live. Two shots are parallel; three or more fan out using shotSpread (0 makes
parallel rows). Drops can temporarily raise shot count; rapid reduces cooldown.
Enemy health receives capped extra armour in later waves. Saves retain these
rules and drawings. Remixes should change only what the request implies.

Example: “Underwater, a fish ship, giant jellyfish, bubble shots, slower enemies
and five-way fire” → draw an ocean scene, fish/jellyfish emoji or original vector
sprites, a hollow-circle vector projectile, alienSize 48, enemySpeed .7 and
shotCount 5. Choose suitable colours; preserve unrelated settings unless the
player asks for a complete new game. No extra model API or raster image service
is required for these code-drawn graphics.


## Combat and creative gameplay

New capabilities are live engine mechanics, not just decoration:

- `combat.weapon`: blaster or laser. Laser pulses pierce every aligned alien,
  dealing one damage per pulse (armour still matters); minimum cooldown .24s.
  Shot count adds parallel beam lanes. The projectile sprite customises blaster
  shots; laser beam colours use the palette.
- `combat.enemyShots`: adaptive, straight, aimed or fan. Adaptive keeps early
  waves simple, unlocks aimed shots at wave 4 and three-way fans at wave 7.
  Aimed shots commit to the ship position at firing time; they do not home.
- `combat.combos`: boolean; `comboWindow`: .5–5 seconds; `comboMax`: integer 1–5.
  Every four kills within the window raises the score multiplier by one. It
  resets after a timeout, player damage or a new wave. UFO bonuses are separate.
- `drops.kinds` additionally accepts laser (piercing beams, 8 seconds) and slow
  (enemies, their bullets and UFOs run at 35% speed for 6 seconds; player stays
  at full speed). They have rarer weights within the same sparse drop budget.
  Ordinary drop rates, six-second spacing and maximum two drops remain.
- `waves.pattern` additionally accepts zigzag. Mixed unlocks zigzag at wave 6.
  Movement pattern changes take effect next wave; direct weapon changes apply
  live. Slow time freezes when paused and saved timers restore correctly.
- `effects.impacts` toggles muzzle flashes, armour flashes and impact rings;
  `effects.engineTrail` toggles ship exhaust. Reduced motion suppresses these
  decorative animations. Triple-shot's default icon is three drawn shot lanes,
  not sparkles. Every drop icon remains independently customisable.

For “make it modern” or “give it more tricks”, compose a coherent concept:
choose a fitting weapon, enemy attack pattern, effects and scenery. Do not
increase every setting or flood the screen with drops. For a small change,
keep other fields. For a complete remix, design a coordinated scene and sprites
rather than merely renaming the game or swapping an emoji.

Examples:
“Give me lasers and occasional slow-time drops” → combat.weapon laser; add slow
alongside the current drop kinds, retaining current frequency and custom art.
“More tactical, enemies aim at me, no combos” → combat.enemyShots aimed,
combat.combos false; preserve difficulty and movement speed.
“Neon sea battle, fish enemies, turquoise beams and hourglass drops” → compose
an original drawn sea scene, fish sprites, turquoise palette, weapon laser,
add slow to existing drop kinds and draw its hourglass icon if helpful.

Use customize_raiders then play_raiders with the complete resulting config and
known bestScore. These are supported combinations, not arbitrary engine code,
bosses, multiplayer or unrestricted new physics. Reply in one short sentence.
Publisher remains Danny Griffin / falsalama. Review submission and publication after approval are separate actions.
