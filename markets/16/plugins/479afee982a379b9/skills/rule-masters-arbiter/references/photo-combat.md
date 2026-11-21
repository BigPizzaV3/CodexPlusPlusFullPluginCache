# Combat from photos

Use this subskill to turn one or more Rule Masters battle photos into a combat prompt.
Read the bundled core rules and Arbiter instructions, and look up identified
cards in the relevant card lists before resolving the battle.

## Read the setup

Build the board inventory before assigning combat roles. For each photo, track
its main named Unit and each associated card's identity, type, host/target,
readiness, binding, and markers. Treat this as the full source state, including
Locations not currently displayed. Then assign attacker and defender and render
the relevant cards from their own inventories. Never populate the defender's
Location slot with whichever Location happens to be visible: it must belong
to that defending Unit. A Location in the attacking Unit's photo stays in that
Unit's inventory and is omitted from the combat summary. Text such as "Ready
and Bound" supplies attributes, not another card to add to the inventory.
Keep this bookkeeping internal; players receive the compact two-side summary.

Read the player's accompanying message and relevant earlier game details along
with the image. Include declared attacker and defender, effects, attachments,
damage, counters, resources, locations, and status changes. Explicit player
details take precedence over visual inferences; a photo may show the state
before a declared change. Do not silently replace those details with what the
layout appears to imply.

- Cards positioned on or touching a Location card are in that Location. Partial
  overlap or edge contact counts; merely being nearby does not. Keep track of
  both sides' Locations in the underlying photographed setup. Combat takes
  place at the defender's Location. Omit the attacker's Location card only from
  the displayed combat confirmation and current combat evaluation; retain its
  identity, state, markers, and association with that side for later corrections.
  Do not include it as equipment or transfer its theme to the battlefield.
  Use the featureless battlefield default only when no Location is shown or
  specified for the defender. Rebuild the relevant details if sides swap as
  described below; absence from an earlier summary is not absence from the photo.
- Equipment/Item cards placed on a Unit are equipped to that Unit. Spell cards
  placed on a Unit are enchanting that Unit. Keep attachments with their host
  when describing its Location and side of the fight; do not count them as
  separate combatants. A clearly identified Item overlapping its Unit is
  equipped to that Unit: say "equipped to [Unit]", not "likely attached/supporting".
  Placement establishes the attachment, not an invented effect or resource
  payment. Include any effect the player actually describes.
- Determine each overlapping card's type before assigning its relationship.
  A Location beneath or touching a Unit is its Location, not equipment. An Item
  partly tucked under a Unit can still be equipped; stacking order does not
  change a card's type.
- Determine readiness for each card using the orientation check below. Do not
  classify a whole group as Exhausted from the direction its text faces.
- Identify visible card names, types, icons, and markers where legible. Apply
  the marker conventions below and preserve per-card counts. Use the partial-card matching guidance below
  before treating an obscured card as unidentified. Flag unresolved identities
  or relationships as uncertain rather than inventing cards or hidden game state.

### Seals, runestones, damage, and counters

Use these photo-mode conventions unless the player supplies different meanings:

- **Coins are Seals.** A card with a coin on it is **Bound**. Assign the Seal to
  the card it marks, not every card in the overlapping stack.
- **No Seal means unbound:** assume the card is **Invoked** in some way to
  influence this combat. Show "Invoked" in the confirmation; do not narrate
  routine Seal recognition or the no-Seal convention to the player.
  Apply this per card, including Units, Items, Spells, and Locations; being on
  the table or attached does not by itself establish that a card is Bound.
  If the area where a Seal might sit is hidden, mark binding status uncertain
  rather than treating an unseen Seal as definitely absent. Explicit player
  statements about binding take precedence over the photo convention.
- **Glass beads are runestones.** Beads placed on a card typically represent
  enhancement: count them for that card and show "Runestone enhancement: N".
  Use that enhancement convention directly in the proposed setup. Do not
  silently spend them, count them as damage, or invent a numeric power bonus.
  Loose reserve beads away from cards are not automatically card enhancements.
- **Red cubes are damage.** Each red cube marks one damage on the card it is
  assigned to; report the damage total.
- **Other colored cubes are counters.** Count them separately by color for each
  card, plus the total. Ask what each color represents unless the player or
  established game state already explains it; color alone does not establish
  its effect. Do not combine red damage cubes into the non-red counter total.

Keep markers with their own card rather than copying counts to its host or
attachments. If overlap, glare, or occlusion makes a marker's kind, count, or
owning card unclear, report the visible count as partial or uncertain and ask
the focused question needed to resolve it. Do not invent hidden markers or
double-count one marker across cards.

For an assumed Invoke, infer a combat role from the card's name,
theme, placement, and accompanying text. A positive-sounding card can be
assumed to enhance the side it is associated with; a negative-sounding card
can be assumed to debuff that side. Make the affected side explicit, rather
than assuming the card always helps its owner. State a clear role directly in
the proposed setup, such as "enhances Pirate With a Porpoise", without repeated
"tentatively", "likely", or "supporting" qualifiers. The final confirmation
block identifies defaulted Invoke roles as proposed readings for the player to
correct; this does not make them printed abilities or already-agreed effects.
Reserve uncertainty language for genuinely ambiguous tone, target, or evidence.
If the tone or target is ambiguous, ask. Do not invent precise strength,
duration, resource payments, or an Activation for an unbound card. Keep an
invoked supporting Unit distinct from the single attacking or defending Unit.

These are photo-reading defaults, not changes to the underlying game rules.
Carry the player's confirmed Invoke role into the combat; do not silently
promote an unbound card to a persistent Bound attachment or Location.

### Orientation check: a half-turn is not exhaustion

Establish each player's normal card direction using the surrounding layout,
visible title/type text, and card edges. Opponents normally face each other:
their Ready cards may have upside-down text from the camera's viewpoint.

Before filling the card lines, compare every card's own printed title/type
text baseline with those on the other cards in its side. A title running along
the image's vertical direction while nearby Ready cards' titles run horizontally
(even upside down) is positive evidence of a quarter-turn: mark that card
**Exhausted**. Confirm using its long card edges. Do not fill Ready
as a default for an entire side before doing this comparison. Perform this
orientation pass before reading coins and counters so marker recognition does
not replace the readiness check. If the whole photo is rotated, make the same
relative comparison after accounting for that rotation.

- **Ready:** the card's long axis is parallel to that player's normal Ready
  cards. Both a 0-degree and a 180-degree orientation have the same long axis;
  upside-down text alone never makes a card Exhausted.
- **Exhausted:** the card has been turned roughly a quarter-turn (90 or 270
  degrees), so its long axis is perpendicular to that player's Ready direction.
  Look for sideways title/type text and the card's edges together, allowing for
  perspective and small slants. Do not equate every rotation with exhaustion.
- Judge each card independently, including Items, enchantments, and Locations.
  Never copy a Unit's exhaustion to cards touching it. Use remaining exposed
  edges and text for partly covered cards; mark readiness unclear if those clues
  do not establish the axis. Do not use a sideways Unit as the Ready baseline
  for its entire group.
- Recheck every card whose long edges are perpendicular to other cards in its
  side: if those other cards establish the player's Ready axis, the perpendicular
  card is Exhausted even when it has a Seal. A Ready Unit can overlap an Exhausted
  Item, Spell, or Location, just as an Exhausted Unit can overlap Ready cards.
  A card's type or position underneath another card is not evidence of readiness.
  A coin indicates binding only;
  it never changes readiness. Read markers and orientation as separate properties.
- Camera rotation changes every card's apparent angle, not its state. Compare
  card axes within the board layout rather than declaring all landscape cards
  Exhausted relative to the image frame. Player-supplied status still takes
  precedence over the visual inference.

For example, if an opponent's Unit lies sideways across an Item and a Location
whose text is upside down but whose long edges follow that player's Ready
direction, only the Unit is Exhausted. The Item and Location remain Ready;
the Location is where the Unit is fighting, not an equipped Item. Conversely,
when a Unit and equipped Item are upright but the Location under them has
quarter-turned title/type text, only that Location is Exhausted. Use the
Location's own exposed text and edges, not the Unit covering it, to determine
its state. Glass beads, coins, and cubes do not change this orientation reading.

### Match physical cards to the known lists first

Before writing a card's name in the confirmation, check its printed identity
against the included card lists. Use an exact match when available. Otherwise
check close spellings and partial-word matches in the relevant list, then the
other lists if its type is unclear. Combine the candidate name with visible
type and icons; do not accept an invented transcription just because it sounds
plausible. For example, a reading like "Figmentic Space Lobster" with the lobster
and planet icons matches **Enigmatic Space Lobster** in the Unit list, unless
an established game effect has actually renamed it.

Treat the card lists as the candidate set for ordinary physical Rule Masters
cards, not merely optional background information. A visual transcription is
a search clue until matched. Preserve the full listed name, including prefixes:
"Large Cake" must resolve to **Very Large Cake** when the cake card's clues fit.
"Sentient Cheese" is not an Item-list entry: compare the visible fragments with
**Ancient Cheese** and use that listed name when supported. Do not present the
unlisted guess as a card, or ask about its equipment relationship before resolving
its identity. These examples illustrate list matching, not unconditional renames
of cards regardless of their actual appearance or established game effects.

Use the canonical list spelling when the clues identify one clear match. If
several candidates remain or no listed name fits the visible evidence, report
the identity as unresolved and ask for the name or a clearer view. An unreadable,
partly covered, or unfamiliar Rule Masters card is not automatically a token.

Only blank cards, ordinary playing cards, card backs, or cards from another
game may be interpreted as physical stand-ins for tokens with different names.
Their appearance alone does not establish the token's name, type, or effect:
use what the player has established, or ask. Do not import another game's rules
from a stand-in card. This physical-card identification rule overrides the
original generic fallback that treats unlisted names as tokens.

**Established renaming effects override printed names.** First identify the
physical card, then apply any name-changing effect already established for that
card in this game. Use its current effective name in the confirmation and
ruling, even if that name is not in any list. Keep the printed identity as a
tracking aid and mention it in parentheses only when needed to distinguish the
physical card. Do not correct an established changed name back to the printed
one, classify the renamed physical card as a token merely because its new name
is unlisted, or assume an unclear transcription is a renaming effect. Respect
the established effect's duration and scope; ask if its target or continued
application is unclear.

### Partially obstructed cards

Try to identify cards even when another card or object covers part of them.
Combine the visible clues instead of requiring a fully readable name or icon:

- If part of an icon is visible, consider which complete icons could match its
  visible shape, features, and color. Compare those possibilities with the icons
  recorded in the bundled card lists. Do not require the whole icon to be exposed,
  and do not assume the covered portion lacks additional icons or features.
- Consider partial words and individual readable letter sequences in the card
  name, including word beginnings, endings, and fragments between obstructions.
  Search the card lists for compatible names rather than treating a partial word
  as a complete name. Keep uncertain letters open to plausible alternatives.
- Narrow candidates using the combination of name fragments, icon fragments,
  visible card type, any other visible identifying details, and the player's
  accompanying text. A shared icon alone need not identify a unique card. A
  candidate should fit all reliable visible clues; do not ignore contradictory
  letters or features to force a match.

When the combined clues support a clear match, use that name in the inferred
combat prompt. If the match remains tentative, label it as likely and briefly
state the identifying clue. If several cards fit, state the plausible candidates
and ask the player which one it is; if none can be narrowed down, ask for the
card's name or an unobstructed view. Do not classify a card as a token merely
because its printed name is covered. Resolve any identity ambiguity that could
change the combat before issuing the ruling.

### What Exhausted means

The core rules say that Bound cards normally start upright and **Ready**.
Activating a Ready card turns it sideways into the **Exhausted** state. It cannot
activate again until readied, normally in its controller's next Ready Phase,
when that player readies all their cards on the battlefield.

The combat instructions describe its significance explicitly:

> Cards which are Exhausted are slightly weaker than if Ready. "Exhausted" is only a minor status, as its intended as gameplay state representing that the Card can't act again until their next turn.

An Exhausted card can still defend; do not treat it as helpless, asleep, or
automatically defeated. A sideways attacker may already have been exhausted to
pay for the attack being resolved. Do not infer from the photo alone that this
is an illegal second activation; clarify timing only if it matters.

## Multiple photos and attack direction

By default, treat each supplied photo as one side of the same combat. Keep its
cards, markers, and relationships together and label the sides by photo number.
Treat that photo's main Unit and its associated cards as one combat group:
equipment, enchantments, invoked enhancements/debuffs, Location, and markers
stay associated with that same Unit when its attacker/defender role changes.
This grouping does not turn supporting cards into additional attacking Units.
Anchor inferred effects to the named Unit in that photo, not to a temporary
role label. In particular, an invoked negative card in a Unit's photo defaults
to debuffing that Unit; do not redirect it to the opponent merely because it
was played by that Unit's side. Explicit player-supplied targets override this
photo grouping. If the photo contains multiple possible main Units and the
association is unclear, ask rather than moving effects arbitrarily.
Use captions and explicit player statements first. If images clearly show
overlapping views or close-ups of the same side, merge those views rather than
duplicating cards or counting the same markers twice. If more than two photos
cannot be assigned to the two sides, ask which images belong together instead
of inventing extra combatants. Work out orientation separately in each photo;
different camera angles do not imply different readiness states.

A written combat matchup such as "A vs B", "A vs. B", or "A versus B" supplies
direction: A attacks B unless the player explicitly says otherwise. Use the
named parties before photo orientation or photo-order defaults. Keep each
photo group's cards and effects with their named Unit. Do not ask who attacks
or reconfirm the defender merely because the player used versus. If the text
requests that combat and the visible setup is otherwise clear, resolve it;
ask only about genuinely unresolved essential details. This does not remove
the setup confirmation for a photo-only submission.

For a single photo showing both sides, default to the side whose normal card
text is right-side-up to the viewer as the attacker, and the opposite/top side
as defender. Use the group's normal orientation, not a single exhausted Unit's
sideways text. Explicit attack direction overrides this default. For separate
side photos where both face the viewer, default to photo 1 attacking photo 2
unless captions establish another direction. For a photo-only setup, confirm
the inferred defender in the final question. If neither accompanying text nor
the layout supplies a meaningful assignment, ask which side attacks rather
than pretending it is clear.

### When the player reverses attacker and defender

Keep the full photographed setup for each side separate from its current role
as attacker or defender. A combat summary intentionally omits some details; do
not use that filtered summary as the sole record of the board.

When the player says to reverse the attack, swap sides, or names the other Unit
as attacker, rebuild the combat from the original photos and established game
state. Carry each Unit's equipment, effects, readiness, binding status, damage,
runestones, and counters with that Unit. Retrieve the new defender's Location
from its original side, including the Location's own readiness, binding, and
markers, even when it was omitted while that side was attacking. Remove the
new attacker's Location from the displayed combat and evaluation. Do not move
Location cards between Units or substitute the old defender's Location.

For example, if Clockwork Komodo at Towering Wall was attacking a Gnome, the
first confirmation omits Towering Wall. If the Gnome now attacks the Komodo,
the revised defending side must include Towering Wall and its observed state.
This follows from the photographed association, not from a fixed rule that a
Komodo always has that Location.

Reinspect the original image if an omitted Location's details are no longer
available in the working state. Ask a focused question only if the image or
established details cannot resolve them; do not silently fall back to the
featureless battlefield. Preserve every photo-associated or confirmed
card-targeted effect with its named Unit, including Invoked cards. Resolve the
old summary's role labels to the Units they referred to before changing the
labels: "Scourge debuffs the defender" means the Unit previously identified as
defender remains debuffed when it becomes the attacker. Move Scourge's card line
with that photo group and rewrite its description to name the same affected
Unit in its new role. The same applies to positive enhancements. Do not leave
an invoked card behind, drop its effect, or keep it attached to the word
"defender" after the underlying Unit changes roles.

An explicit player-established rule that dynamically targets whoever is
attacking/defending can override this default. A role word in the Arbiter's own
earlier summary is not evidence of such a dynamic rule. Do not ask the player
to clarify an ordinary reversal when the photo association or prior named
target already resolves it. Ask only if the underlying target or effect rule
was genuinely unresolved. A reversal does not reset or invent any card state.

Show the revised setup with the new defender's Location. The player's reversal
should preserve the same photo groups and per-card states, changing only their
roles, corresponding labels, and which Location is displayed. Check that every
previously included non-Location card is still present with its original Unit
and effect target before sending the revised summary. The player's reversal
already establishes the direction, so do not ask them to confirm the same swap
again. Ask only about genuinely unresolved details, or resolve if they requested
the ruling and the remaining setup is established.

## Present the combat for confirmation

If the player provides only a photo, reply with the combat prompt you infer and
ask for confirmation or corrections. The same applies to a vague caption such
as "resolve this" that still leaves the intended attacker and defender inferred.
Incorporate any supplied details even when confirmation is needed.

Use one attacker and one defender. Do not make every visible Unit a simultaneous
attacker or invent a supporting activation because cards are grouped together.
Apply the attack-direction defaults above. If the photo cannot support a meaningful choice, show the readable
setup and mark the missing attacker or defender for the player to identify.

Start with **Combat: [Attacker] attacks [Defender]**. This is the setup being
confirmed, so do not preface it with "inferred" or repeated hedging. Then clearly divide the confirmation into
**Attacking side** and **Defending side**, labeled with their photo positions
where useful. If direction cannot be inferred meaningfully, use **Side A** and
**Side B** with positions and ask which attacks.

Under each side, give each relevant card its own bullet, including combatants,
Items, enchantments, the defender's Location only, and other invoked support. Do not collapse a
stack into one shared state. Use this compact card-line pattern:

> - **[Card name]** — [role/host or affected side]; **Ready / Exhausted**;
>   **Bound / Invoked**; Damage: [N, if any];
>   Runestone enhancement: [N, if any];
>   Counters: [total and counts by color, if any]; [Invoke role, if any].

Every card must have its own explicit readiness and Bound/Invoked status.
Write readiness simply as **Ready** or **Exhausted**; keep the visual reasoning
internal and omit annotations such as "(sideways)" from the card line.
If either cannot be established, write "Readiness unclear" or "Binding status
unclear" on that card's line. Include nonzero damage, runestone enhancement,
and counter counts on the relevant card; omit absent count fields to keep the
confirmation readable, but do not omit uncertain or partially visible counts.
For example, counters can read "3 total: 2 blue, 1 green; meanings unknown".
Label the Location simply "defender's Location", not "home turf" or
"Location/home turf"; home turf is not a separate mechanical status to list.
In the eventual ruling, keep the home-base convention implicit unless a
specific thematic tie or established effect makes it worth mentioning. Describe
that actual interaction rather than routinely calling the Location home turf.
Keep the defender's Location distinct from equipment, and state each Invoke's
enhancing/debuffing role directly. Never copy a host's state to its cards.

Do not add a separate Exhausted summary or "Exhausted: None": every card already
has its readiness shown. Retain those per-card states in the agreed combat and
eventual ruling.

Separate the final questions from both sides with a blank line, a Markdown
horizontal rule, another blank line, and the heading **Confirm before combat**.
Put a blank line after the heading, then a numbered list with one clear question
per item. Ask about an inferred defender only when the text has not already
specified direction (including a versus matchup), proposed Invoke roles needing confirmation,
and unknown counter meanings or other material uncertainties. For example:

> **Confirm before combat**
>
> 1. Is [Defender] the intended target?
> 2. Is Reinforce enhancing [Attacker] for this combat?
> 3. What does the green counter on [Defender] represent?

Include only questions relevant to this setup; do not ask again about facts the
player already supplied. A short "Correct anything else above" may follow the
list. Do not combine the questions into a prose paragraph. Apply routine visual
conventions silently: omit explanations such as "I treated coins as Seals",
"red cubes as damage", or "the Seal-less card as Invoked". The card lines already
show those interpretations. Ask about a marker only when its shape, count,
assignment, or meaning is genuinely unclear. Likewise, confirm the proposed
target directly instead of adding a preamble about the attack-direction default.
Keep blank lines between the Combat title, side labels, card lists, and final
question block so headings and adjacent text do not run together.
Before sending, check every card name in the completed response against the
exact full entries in the appropriate lists. Correct shortened or misread names
using supported candidates. For an unresolved ordinary Rule Masters card, use a
positional description such as "unidentified Item beneath the defender" and
ask for its identity instead of publishing an unlisted name. Do not apply this
correction to an established effective name from a current-game rename or to a
player-named permitted token stand-in. Give each question one question mark and
avoid duplicated punctuation such as ".." or "?." on card or question lines.
Do not announce a winner,
damage result, or battle narration yet. Wait for the player's confirmation or
corrections, then resolve the agreed combat using the normal arbitration rules.
Ask again only if a correction still leaves an essential fact unresolved.

When the accompanying text already clearly requests a specific combat, use the
photo to fill in the visible setup and resolve it normally. Ask a focused
question only for an essential ambiguity that the text and rules do not settle;
do not require a redundant confirmation merely because a photo is attached.
