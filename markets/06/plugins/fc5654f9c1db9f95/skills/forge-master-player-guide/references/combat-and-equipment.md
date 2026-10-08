<!-- Source book: COMBAT_STATS_AND_MODIFIERS_PLAYER_GUIDE_v0_1.md -->

# ForgeMaster Combat, Stats and Modifiers Guide

Status: **Public guide draft v0.1**  
Evidence cutoff: **16 September 2026**

## The short version

A ForgeMaster character is not defined by displayed Power alone.

- **Base Damage and Base Health** determine the headline Power figure.
- **Damage, Health and weapon-type modifiers** raise the totals used in battle without directly increasing displayed Power.
- **Critical Chance, Critical Damage, Double Chance and Attack Speed** turn Total Damage into actual weapon output over time.
- **Block, Health Regen and Lifesteal** determine how long that Health lasts.
- **Skills** add separate attacks, buffs and healing effects.
- The best build usually combines several complementary mechanics rather than chasing one large number.

## How to check your full statistics

There are two current routes to the player's full statistics card:

1. From the main game screen, tap the small **`i` information button** beneath the equipment area.
2. From the PvP League screen, tap the player's own icon.

Tapping the displayed **Power** number does **not** open the statistics card.

Use the full card to check Power, Total Damage, Total Health, Forge level and ascension stars, equipped assets and the complete modifier summary. This complete summary is different from opening one individual equipment item, Pet or Mount, which shows only that asset's details. If a supported combat modifier is absent from the complete summary, treat its current total as **0%**.

## Base Damage, Base Health and Total values

The game combines the raw Damage and Health supplied by the character's developed assets. Percentage modifiers are then applied to produce the values shown as **Total Damage** and **Total Health**.

For the equipped weapon type:

```text
Total Damage = Base Damage × [1 + Damage% / 100] × [1 + matching weapon Damage% / 100]
Total Health = Base Health × [1 + Health% / 100]
```

“Matching weapon Damage” means Melee Damage when a melee weapon is equipped or Ranged Damage when a ranged weapon is equipped.

This can be reversed when the full totals and modifiers are known:

```text
Base Damage = Total Damage / {[1 + Damage% / 100] × [1 + matching weapon Damage% / 100]}
Base Health = Total Health / [1 + Health% / 100]
```

Generic Damage and matching weapon Damage are separate multiplicative stages. Do not add their percentages together. For example, +31.1% Damage and +297% Melee Damage give a total multiplier of `1.311 × 3.97`, not `1 + 3.281`.

The displayed Total Damage and Total Health already include those percentage modifiers. Do not apply the same modifiers a second time when comparing characters or equipment.

## What displayed Power measures

The current confirmed relationship is:

```text
Displayed Power = 24 × Base Damage + 3 × Base Health
```

This means displayed Power does **not** directly reward:

- Damage, Melee Damage or Ranged Damage percentages;
- Health percentage;
- Critical Chance or Critical Damage;
- Double Chance;
- Attack Speed;
- Lifesteal;
- Block Chance;
- Health Regen;
- Skill strength or cooldown.

Power is useful as a broad measure of raw progression, but it is not a complete measure of fighting ability. Two characters with the same Power can perform very differently, and a lower-Power character with a coherent build can defeat a higher-Power character.

## Melee and ranged weapons

The equipped weapon determines whether the character is currently melee or ranged.

- **Melee weapons** require the character to close into striking distance before attacking.
- **Ranged weapons** can normally begin attacking while the opponent is still approaching.
- **Melee Damage** benefits only a melee build.
- **Ranged Damage** benefits only a ranged build.

A wrong-type modifier may still be listed among the character's accumulated stats, but it provides no current benefit. It becomes relevant only if the weapon type changes.

The ranged opening advantage does not automatically make ranged superior. Melee weapons and Melee Damage modifiers can have different strengths, and the final result depends on attack rate, survival, Skills and the particular opponent.

## The main modifiers

| Modifier | Player-facing effect | Important relationship |
|---|---|---|
| Damage | Raises weapon Total Damage. Equipment-style Damage also contributes to active Skill values in the current configuration. | Multiplies separately from the matching weapon-type Damage percentage for the headline weapon total. |
| Melee Damage | Raises weapon damage while a melee weapon is equipped. | Does nothing for a ranged weapon. |
| Ranged Damage | Raises weapon damage while a ranged weapon is equipped. | Does nothing for a melee weapon. |
| Health | Raises Total Health. Equipment-style Health also contributes to health-granting active Skill values in the current configuration. | Makes percentage-based Health Regen more valuable. |
| Critical Chance | Chance that a weapon hit becomes a critical hit. | Needs Critical Damage to become a major damage engine. |
| Critical Damage | Adds damage when a critical hit occurs. | Has no effect when Critical Chance is zero. |
| Double Chance | Chance for a normal weapon attack to produce a follow-up attack. | The extra attack can independently Crit, be blocked and generate Lifesteal. |
| Attack Speed | Makes ordinary weapon attacks occur more frequently. | Improves weapon damage output and the rate at which Lifesteal can heal. |
| Block Chance | Chance to prevent an incoming hit. | Preserves Health and gives Regen/Lifesteal more time to work. |
| Health Regen | Restores a percentage of the character's underlying maximum Health continuously during battle. | Scales directly with Health. |
| Lifesteal | Heals a percentage of weapon damage actually dealt. | Scales with weapon damage, Attack Speed, Crit and Double Chance. Skills do not Lifesteal. |
| Skill Damage | Raises the active values of equipped Skills, including applicable support-Skill values. | Does not increase ordinary weapon hits. |
| Skill Cooldown | Reduces the cooldown between active Skill uses. | Does not shorten the initial charge or the Skill's active duration. |

The precise interaction of equipment-style Damage and Health with every individual Skill popup would benefit from further live captures. The current configuration establishes the targeting, but the guide should prefer the values displayed on the player's actual Skill screen when available.

## Critical Chance and Critical Damage

Every critical hit has a built-in base multiplier of **1.20×** normal damage. The displayed Critical Damage modifier is added on top.

Examples:

| Displayed Critical Damage | Damage from a critical hit |
|---:|---:|
| 0% | 1.20× normal hit |
| 50% | 1.70× normal hit |
| 100% | 2.20× normal hit |
| 150% | 2.70× normal hit |

Critical Chance controls how often this happens. A simple average weapon-hit multiplier is:

```text
1 + Critical Chance × (20% + displayed Critical Damage)
```

Use decimal forms in the calculation. For example, 25% Critical Chance and 100% displayed Critical Damage gives:

```text
1 + 0.25 × 1.20 = 1.30
```

That is approximately 30% more weapon damage on average before considering Double Chance or Attack Speed.

Critical Damage without Critical Chance is unused. Critical Chance with no displayed Critical Damage still has some value because the built-in 20% critical bonus remains.

Active Skill attacks do not currently use the attacker's Critical Chance or Critical Damage.

## Double Chance

When Double Chance activates, the character makes a second weapon attack after the first. It is a separate hit rather than simply changing the first damage number.

Consequently, the follow-up attack can:

- make its own critical roll;
- be blocked separately;
- produce Lifesteal if it deals damage;
- target the opponent still present when it resolves.

At a broad average level, 30% Double Chance means approximately 1.30 weapon hits per ordinary attack opportunity. Real timing is not perfectly captured by multiplying damage by 1.30 because the follow-up attack itself takes time.

## Attack Speed

Attack Speed shortens the variable portion of the weapon attack cycle. More attacks mean:

- more ordinary weapon damage per second;
- more opportunities to Crit;
- more opportunities to trigger a Double attack;
- more Lifesteal healing per second.

Its benefit is not perfectly linear because every attack retains some fixed animation/timing overhead. Adding 40% Attack Speed therefore does not necessarily mean exactly 40% more completed attacks in every fight.

Short battles and timing boundaries can also make two nearby Attack Speed values appear identical: both may complete the same number of attacks before the battle ends.

## Block Chance

When Block activates, the incoming hit deals no damage to the blocker. Block is therefore more than a Health percentage: it can completely prevent a large hit.

Block also indirectly improves healing. Every avoided hit:

- preserves existing Health;
- creates more time for Health Regen;
- creates more time for the character to attack and gain Lifesteal;
- reduces the chance of dying before a Skill activates.

Block is confirmed for ordinary direct attacks. Its exact interaction with every Skill type, Reflect and simultaneous lethal hits remains a research area and should not be stated more precisely than the evidence supports.

## Health Regen

Health Regen restores the displayed percentage of underlying maximum Health per second while the character remains alive, up to the current maximum.

For example, 4% Health Regen on 10 million underlying Health represents approximately 400,000 Health restored per second before any mode-specific effects.

This makes Health and Health Regen complementary:

- more Health increases the amount healed each second;
- Block gives Regen more time to accumulate;
- Regen continues even when the character is not successfully dealing damage.

Regen cannot bring a dead character back to life.

## Lifesteal

Lifesteal returns a proportion of successful weapon-hit damage as healing.

For example, a weapon hit that actually deals 1 million damage with 20% Lifesteal heals approximately 200,000 Health, subject to the character's maximum Health.

Important limits:

- a fully blocked hit deals no damage and gives no Lifesteal;
- Skill attacks do not generate Lifesteal;
- healing cannot exceed the current maximum Health;
- Lifesteal cannot resurrect a character killed by damage resolving at the same moment;
- reflected damage does not itself generate Lifesteal.

Lifesteal becomes stronger when combined with Damage, the matching weapon-type Damage, Attack Speed, Critical Chance/Critical Damage and Double Chance.

## Skill Damage and Skill Cooldown

Skill Damage applies to the active values of equipped Skills. Despite its name, the current configuration also applies it to applicable Health values on support Skills.

Skill Cooldown reduces only the cooldown after an active Skill or buff has finished. Equipped Skills begin battle with an initial charge of approximately four seconds; Skill Cooldown does not reduce that initial charge and does not shorten or extend the active effect itself.

Skills provide a separate combat layer:

- damaging Skills do not use the attacker's Crit or Lifesteal;
- timed buffs temporarily add their Skill values;
- Health-carrying buffs can restore current Health when activated;
- Skill targeting, hit counts and defensive interactions vary by Skill.

See the Skills Guide for individual Skill roles. Exact damage sequences belong in the outstanding combat research rather than being guessed here.

## Reflect Chance

Reflect currently comes from the Lora Fairy rather than an ordinary equipment modifier roll.

The confirmed core behaviour is:

- the defender still takes the incoming direct weapon hit normally;
- when Reflect activates, the attacker also takes the same resolved hit damage;
- Reflect is retaliation, not damage prevention;
- reflected damage does not recursively Reflect again;
- reflected damage does not grant Lifesteal.

**Observed correction (16 September 2026):** Block and Reflect are independent checks and can trigger on the same incoming direct weapon hit. Block protects the defender, while Reflect returns the damage that the weapon hit would otherwise have inflicted—its basis is the direct-weapon damage before Block cancels the defender's Health loss. Skill damage did not produce returned damage in the tested recordings, so do not treat Skills as Reflect-eligible. Ordinary Lifesteal remains in force, but the exact same-frame Lifesteal/Reflect ordering, mitigation details, mode eligibility and whether reflected retaliation can itself be Blocked remain **Pending**.

## Modifier slots

Only equipment, Pets and the equipped Mount provide ordinary modifier slots. Skills never provide them.

### Equipment

| Equipment tier | Modifier slots |
|---|---:|
| Primitive | 0 |
| Medieval | 0 |
| Early Modern | 0 |
| Modern | 1 |
| Space | 1 |
| Interstellar | 1 |
| Multiverse | 1 |
| Quantum | 2 |
| Underworld | 2 |
| Divine | 2 |
| Any ascended equipment | 2 |

### Pets and Mounts

| Rarity | Modifier slots |
|---|---:|
| Common | 1 |
| Rare | 1 |
| Epic | 1 |
| Legendary | 2 |
| Ultimate | 2 |
| Mythic | 2 |
| Any ascended Pet or Mount | 2 |

A complete loadout contains eight equipment items, three equipped Pets and one equipped Mount. If all twelve assets have two slots, the maximum ordinary equipped modifier capacity is **24 slots**.

## Current per-slot modifier ranges

These are the current configuration ranges for one rolled modifier. They are not whole-build caps; several slots and Tech bonuses can accumulate.

| Modifier | Minimum roll | Maximum roll |
|---|---:|---:|
| Critical Chance | 1% | 12% |
| Critical Damage | 1% | 80% |
| Block Chance | 1% | 5% |
| Health Regen | 1% | 4% |
| Lifesteal | 1% | 20% |
| Double Chance | 1% | 20% |
| Damage | 1% | 15% |
| Melee Damage | 1% | 50% |
| Ranged Damage | 1% | 15% |
| Attack Speed | 1% | 40% |
| Skill Damage | 1% | 30% |
| Skill Cooldown | −1% | −7% |
| Health | 1% | 15% |

Skill Cooldown is displayed as a negative percentage because it removes waiting time; a more negative value is the stronger reduction.

## Reading a complete combat-summary screen

When the complete current combat-summary/stat panel is visible:

> If a supported modifier is not listed, its value is 0%.

It is not an unknown value. Clarification is required only when the list is cropped, obscured or otherwise incomplete.

This prevents two common errors:

- inventing a modifier because it would make the build appear more sensible;
- repeatedly asking for a value that the complete screen has already established as zero.

## How the modifiers work together

Think of a build as three connected systems.

### Weapon pressure

Built from:

- Total Damage;
- Attack Speed;
- Critical Chance and Critical Damage;
- Double Chance;
- the melee/ranged opening and positioning.

### Survival

Built from:

- Total Health;
- Block Chance;
- Health Regen;
- Lifesteal generated by weapon pressure;
- Health-support Skills.

### Skill contribution

Built from:

- the equipped Skills and their levels/stars;
- Skill Damage;
- Skill Cooldown;
- ordinary Damage/Health modifier layers where applicable;
- surviving long enough for the Skills to activate.

A stat can therefore be strong on one character and weak on another. Lifesteal needs weapon damage; Critical Damage needs Critical Chance; Regen needs Health and time; Skill Cooldown needs Skills worth repeating.

## Practical build guidance

- Do not judge a swap from displayed Power alone.
- Preserve a working combination of stats rather than maximising one isolated percentage.
- Enforce the visible modifier-slot budget before presenting precise target ranges.
- Preserve a complete attack engine: matching weapon Damage, Critical Chance/Critical Damage, Attack Speed or Double Chance, and enough Lifesteal.
- Avoid accumulating the wrong weapon-type Damage unless a weapon change is planned.
- Do not heavily invest in Critical Damage while Critical Chance remains zero.
- Remember that increasing weapon damage also strengthens Lifesteal.
- Remember that increasing Health strengthens percentage-based Regen.
- Use Block to support both raw Health and healing-based survival.
- Compare Skill modifiers against the actual equipped Skills, not against rarity labels alone.
- Treat the full current totals and complete modifier screen as the starting point for any equipment decision.
- When no character capture or battle test is available, label the recommendation **heuristic** rather than simulated or optimised.

### Published build references

The three established reference families use 80% of the decoded maximum roll values. They are public-safe targets for comparison, not universal guarantees:

| Reference | AS | CC | CD | Double | LS | Damage | Melee | Ranged | Health |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ranged Crit-Leech | 64% | 71.4667% | 476.4444% | 32% | 39.1111% | 16% | 0% | 16% | 0% |
| Melee Durable-Tempo | 80% | 52.8% | 352% | 8% | 24% | 12% | 240% | 0% | 18% |
| Melee Burst-Double | 0% | 72% | 352% | 56% | 16% | 12% | 220% | 0% | 0% |

**Melee Durable-Tempo** is the robust general melee reference. **Melee Burst-Double** is a specialist, with viable hybrids between them.

Completed comparative testing supports two maxed-Lora, 24-slot maximum-roll Reflect references:

| Stat | Ranged Reflect | Melee Reflect |
|---|---:|---:|
| Health | 30% (2 rolls) | 90% (6 rolls) |
| Damage | 0% | 30% (2 rolls) |
| Matching weapon Damage | 15% (1 roll) | 300% (6 rolls) |
| Attack Speed | 120% (3 rolls) | 120% (3 rolls) |
| Critical Chance | 84% (7 rolls) | 0% |
| Critical Damage | 480% (6 rolls) | 0% |
| Double Chance | 60% (3 rolls) | 40% (2 rolls) |
| Lifesteal | 40% (2 rolls) | 100% (5 rolls) |
| Block, Regen and Skill modifiers | 0% | 0% |
| Lora Reflect | 30% | 30% |

For the ranged version, one generic Damage roll is combat-equivalent to the listed Ranged Damage roll. The melee version had a small tested edge over the prior conventional melee reference, but the ranged Reflect version was substantially stronger across the tested opponent mix and beat the melee Reflect version directly. Zero Block led both references; one 5% Block roll was effectively tied for melee, but heavier Block allocations trailed. These are scenario-specific comparison targets using one common base character and Skill package, not universal guarantees or easily attainable live builds. Broad simultaneous ranges must not be called an established “Excellent Reflect build” without slot arithmetic and evidence limits.

One exact 12-item pairing for the melee reference is five Melee Damage + Health items, one Melee Damage + Lifesteal item, one Health + Lifesteal item, three Attack Speed + Lifesteal items and two Damage + Double Chance items. For ranged, use six Critical Chance + Critical Damage items, one Critical Chance + Ranged Damage item, three Attack Speed + Double Chance items and two Lifesteal + Health items.

## Open questions

The guide deliberately leaves these unresolved:

- exact Skill-by-Skill hit counts and targeting rules;
- exact Reflect ordering with the attacker's own Lifesteal;
- whether returned Reflect retaliation can itself be Blocked;
- mode-specific Fairy exclusions;
- the exact player-visible timing curve and breakpoints for every weapon;
- how Move Speed affects each battle type;
- whether all player-visible Skill popups show every applicable ordinary Damage/Health layer consistently.

These are suitable for controlled tests and dated observations. Until then, player answers should distinguish the confirmed core rules from the unsettled edge cases.


---

<!-- Source book: EQUIPMENT_AND_FORGING_PLAYER_GUIDE_v0_1.md -->

# ForgeMaster Equipment and Forging Guide

Status: **Public draft v0.1**  
Evidence cutoff: **15 September 2026**

Equipment—sometimes called **items**, **gear** or **gears** in community guides—provides much of a character's headline Damage and Health and many of the modifiers that shape how the build fights. A complete loadout contains **eight equipment items**.

## The eight equipment slots

| Damage-side slots | Health-side slots |
|---|---|
| Weapon | Helmet |
| Glove | Body |
| Necklace | Shoe |
| Ring | Belt |

The weapon also determines whether the character makes **melee** or **ranged** ordinary attacks. This matters when assessing attack-type modifiers: Melee Damage does not support a ranged weapon, and Ranged Damage does not support a melee weapon.

## Equipment eras and modifier slots

Equipment tiers are called **eras**. From lowest to highest:

1. Primitive
2. Medieval
3. Early Modern
4. Modern
5. Space
6. Interstellar
7. Multiverse
8. Quantum
9. Underworld
10. Divine

| Equipment | Modifier slots |
|---|---:|
| Unascended Primitive, Medieval or Early Modern | 0 |
| Unascended Modern, Space, Interstellar or Multiverse | 1 |
| Unascended Quantum, Underworld or Divine | 2 |
| Any ascended equipment item | 2 |

A visible star identifies ascended equipment. The ascended rule overrides the ordinary era rule: even a starred low-era item has two modifier slots.

An equipment popup should be read as a whole:

- slot and item name;
- era;
- item level;
- ascension stars;
- headline Damage or Health contribution;
- every rolled modifier;
- weapon type, when the item is a weapon.

Era alone does not decide whether an item is useful. A lower-era item with a strong, relevant modifier can remain better for a particular build than a higher-era item with the wrong modifier.

## Forging equipment

**Forging** means spending Hammers to create equipment. It is different from a **Forge Upgrade**, which spends Coins on upgrade nodes and then runs a timer.

Each forge attempt:

1. consumes Hammers, subject to any relevant Personal Tech effect;
2. creates one equipment item unless a separately displayed extra/free-forge effect applies;
3. rolls the item's era using the current Forge level's probability distribution;
4. awards Coins;
5. awards Clan War points on Days 1, 3 and 5 according to the resulting era.

Higher Forge levels improve the probability distribution. They do not simply switch the Forge to one guaranteed era.

### Equipment level

An item's **level** is separate from its era. Era controls the broad equipment tier and ordinary modifier capacity; level affects the item's headline Damage or Health.

The configured base maximum is displayed as **Level 99**. Personal Tech contains a separate maximum-level node for each of the eight equipment slots. Each completed sublevel raises that slot's maximum by **2 levels**, up to **10 levels per Tech tier**. This means one slot can be advanced without raising the others.

Higher-level equipment is obtained by forging again after the relevant slot maximum has increased; an existing item is not levelled up in place. The exact random level band used for each newly forged item still needs direct in-game verification, so this guide does not yet state that every new item will appear at the maximum.

### When higher eras first enter the table

| Equipment era | First non-zero chance | Chance at first appearance |
|---|---:|---:|
| Medieval | Forge Level 2 | 1% |
| Early Modern | Forge Level 5 | 0.5% |
| Modern | Forge Level 8 | 0.2% |
| Space | Forge Level 11 | 0.1% |
| Interstellar | Forge Level 14 | 0.05% |
| Multiverse | Forge Level 17 | 0.05% |
| Quantum | Forge Level 20 | 0.05% |
| Underworld | Forge Level 24 | 0.02% |
| Divine | Forge Level 29 | 0.02% |

At Forge Level 35, the supplied base table is **60% Quantum, 36% Underworld and 4% Divine**.

The full percentage for every era at every Forge level is retained in `RARITY_PROBABILITY_REFERENCE_v0_1.md`.

## Upgrading the Forge

The Forge begins at Level 1 and can be upgraded to Level 35.

To upgrade:

1. pay Coins into every node for the target level;
2. when all nodes are filled, the upgrade timer begins;
3. wait for the timer or use **Finish Now** with Gems;
4. when ready, tap **Complete** to raise the Forge level.

The nodes within a level are equal, atomic payments. The table's **Total coins** value is already the whole cost of that level; node count divides that total and must never multiply it. Coins already placed in a node remain there, but partially funding a future Forge level does not improve current forging probabilities. Only one Forge upgrade can run at a time, and each level has one timer after all of its nodes are filled—not one timer per node.

Personal Tech can reduce ordinary Forge-upgrade Coin cost and duration. Use the values displayed in the player's own game for an exact personal forecast.

The complete base costs, node counts, timers, cumulative times and Finish Now prices are retained in `FORGE_UPGRADE_COSTS_TIMERS_REFERENCE_v0_1.md`.

### Clan War distinction

- **Forging:** spends Hammers and scores on Days 1, 3 and 5 according to the item's era.
- **Funding Forge Upgrade nodes:** spends Coins and scores on Days 2 and 4.
- **Finish Now:** spends Gems and scores on Days 2 and 4.
- **Tapping Complete:** raises the Forge level but scores no additional points by itself.
- **Forge ascension:** costs 3,000,000 Coins and scores no Clan War points.

Routine forging is normally part of passive progression because it creates equipment and Coins and Hammers are usually replaceable. Mass-forging only to alter a war result is active scoring. The established rule remains: **only spend enough active-scoring resource to win**.

## Auto Forge

Auto Forge unlocks at **battle stage 2-10**. It automates repeated forging only while ForgeMaster remains open and on screen. It does not continue while the app is closed or in the background.

The Auto Forge screen allows the player to:

- select one or more equipment eras to keep;
- turn modifier filtering on or off;
- select one or more modifier stats;
- choose how many Hammers are processed in each animation, up to the player's available Auto Forge allowance.

An item is retained when it matches at least one selected keep criterion. Items which do not match are sold automatically. A modifier match is therefore not a promise that the whole item is desirable: the same item can also carry an unwanted or irrelevant modifier.

By default, Auto Forge stops when it finds and retains a matching item, allowing the player to review it.

### Auto Forge allowance

The selectable number of Hammers per animation comes from Auto Forge bonuses rather than the current Forge level:

- the shared Clan Tech **Auto Forge** node can add Hammers for every clan member;
- each completed Personal Tech **Auto Forge** tier adds one Hammer to that player's allowance.

For example, a captured displayed maximum of **13** was fully accounted for by **+9 shared Clan Tech** and **+4 Personal Tech**. The player may select fewer than the maximum.

### Continuing after a match

At **effective Forge Level 19**, the option **Continue forging when target equipment is found** becomes available. Ascended Forge progress counts toward this condition, so the option remains available after an ascension even while the current Forge is again at a low level.

When enabled:

- Auto Forge continues after a match;
- retained matches accumulate in a hidden review stack until the stack reaches the selected Hammer allowance;
- the player then reviews the retained items one at a time, without seeing the next item in advance;
- Auto Forge can be restarted as soon as at least one stack slot has been freed.

An advanced player can leave a promising item in the stack while continuing to search—for example, when the item may require a combination swap because it improves one area but loses a critical modifier. This is useful but labour-intensive and does not remove the need to review the whole build.

### Timing

An unboosted Auto Forge animation takes approximately **2.45 seconds**. In the supplied 30-fps recording, equivalent points in successive animations were normally **73–74 frames apart**.

Shared Clan Tech has a separate **Forge Animation Speed** node. It is not the same as the **Auto Forge** node that increases the simultaneous Hammer allowance. In the current configuration, Forge Animation Speed provides **+5% speed per level**, up to Level 20, and acts as a divisor:

`animation time ≈ 2.45 seconds ÷ (1 + 0.05 × node level)`

Examples:

| Forge Animation Speed | Approximate time per animation |
|---:|---:|
| Level 0 | 2.45 seconds |
| Level 4 (+20%) | 2.04 seconds |
| Level 10 (+50%) | 1.63 seconds |
| Level 20 (+100%) | 1.23 seconds |

The selected number of Hammers changes how many items are processed by each animation. No evidence yet shows that it changes the duration of the animation itself.

## A safe equipment-review process

The in-game Auto Forge filter decides which items are automatically sold and which are held for review. It does **not** decide whether a retained item should be equipped. Use this player decision process for every retained item.

### 1. Correct slot

Compare the new item only with the currently equipped item in the same slot. Do not compare a Belt's Health directly with a Weapon's Damage.

### 2. Star and era

Record ascension stars before considering era. A star changes base scaling and guarantees two modifier slots. Era remains important, but it is not a verdict.

### 3. Headline contribution

Compare the new item's visible Damage or Health with the existing item's visible contribution. Use the displayed number rather than estimating it from era or level.

### 4. Modifier relevance

Separate **roll size** from **build usefulness**:

- an impressive Melee Damage roll is off-build for a ranged character;
- an impressive Ranged Damage roll is off-build for a melee character;
- Damage, Health, Critical Chance, Critical Damage, Block Chance, Health Regen, Lifesteal, Double Chance, Attack Speed and other supported modifiers should be judged in the context of the whole build;
- changing one item can remove a modifier the build depends on, even when the new headline number is larger.

### 5. Whole-build effect

Before equipping, consider what is lost as well as what is gained. A good comparison uses the complete current totals and subtracts the old item's contribution before adding the candidate's values. Do not apply a visible modifier twice when the displayed character total already includes it.

### 6. Keep, equip or sell

- **Equip** when the candidate improves the intended build overall.
- **Keep** when it is a strong alternative, supports another attack type or build direction, or is difficult to replace.
- **Sell** only when it is genuine surplus and its future use has been considered.

Selling is irreversible. Personal Tech can improve the Coin return from selling equipment, but extra Coins do not compensate for destroying a rare useful modifier combination.

## Filtering principles

When configuring Auto Forge:

- never discard solely because an item is below the highest available era;
- never discard a weapon before checking melee/ranged type;
- protect rare or build-defining modifier combinations;
- account for starred low-era items separately from ordinary low-era items;
- review two-slot equipment more carefully because replacing it can change two modifiers at once;
- retain plausible alternatives before a planned build change;
- after Forge ascension, remember that the old loadout is removed; compare new starred candidates against remembered or recorded pre-ascension benchmarks rather than claiming the old equipment remains equipped.

Because non-matching items are sold automatically, start with broad keep settings until you understand the consequences. Selecting a desired modifier keeps any item containing that modifier; it may still contain other stats you would not have chosen. Automatic selling is irreversible.

## Forge ascension and rebuilding equipment

At Forge Level 35, Forge ascension:

- costs **3,000,000 Coins**;
- is instantaneous;
- resets the Forge to Level 1;
- removes all existing equipment and Forge progress;
- causes subsequently forged equipment to carry the new star;
- repeats the same Level 1–35 era probability cycle for the starred items;
- awards no Clan War points.

Applicable base values scale by approximately **×50 per star, compounded**. As a practical overlap guide, a one-star Multiverse item is approximately comparable with an unascended Divine item.

This creates a genuine rebuilding period because all eight old items are gone. Forge upgrade timers soon extend into days, which gives the player time to earn new Hammers and continue forging while the Forge advances, but retained Coins and Hammers cannot preserve the old loadout or bypass the timers.

A one-star Multiverse item is only an approximate per-item orientation match for an unascended Divine item. A1 Level 22 is the 4% Multiverse planning checkpoint; A1 Level 25 is stronger at 32% Multiverse plus 4% Quantum. Neither checkpoint guarantees whole-build parity across eight slots. Any Hammer estimate must state its slot, era, item-level and modifier assumptions.

Do not save Eggshells, Skill Tickets or Clock Winders for a Forge ascension. Those resources belong to their own systems. Ordinary Hammer income continues to support equipment rebuilding.

## Clan War points from forging

Forging scores on Days **1, 3 and 5**.

| Forged equipment era | Base points per item |
|---|---:|
| Primitive, Medieval or Early Modern | 1 |
| Modern, Space or Interstellar | 2 |
| Multiverse, Quantum, Underworld or Divine | 3 |

These are base values before shared Clan Tech scoring bonuses.

## Personal Tech effects relevant to equipment

Personal Tech can affect areas including:

- ordinary Forge-upgrade Coin cost;
- Forge-upgrade duration;
- equipment selling return;
- Hammer and Coin income;
- free or automated forging effects where unlocked.

Personal Tech can improve efficiency, but it does not turn a poor modifier combination into a good fit for the build. Use the live popup for an exact increment when the node may have changed.

## Questions this chapter can answer

- What is the difference between forging and a Forge Upgrade?
- What can each equipment slot contribute?
- Which equipment eras have zero, one or two modifier slots?
- At what Forge level can a particular era first appear?
- What are my exact tier chances at this Forge level?
- How much does the next Forge level cost, and how long will it take?
- Should I equip, keep or sell this item?
- Why might a lower-era item be better for my build?
- How should I review equipment after Forge ascension?
- How many Clan War points does this forge earn?
- Should I mass-forge for Clan War?
- When does Auto Forge unlock?
- Why can I process 13 Hammers at once?
- How do tier and modifier filters interact?
- When does the continuation stack unlock?

## Evidence boundaries

- Equipment slots, era order, modifier capacity, Forge mechanics, ascension behaviour and Clan War scoring are established current rulebook/configuration facts.
- The complete Forge level probability and upgrade tables come from the user-supplied ForgeMaster workbook and are preserved in separate public reference files.
- Auto Forge controls and stack behaviour are based on the user's direct explanation and the supplied 11 September 2026 screen recording/screenshot. Unlock gates and Auto Forge bonus values are corroborated by the 8 September 2026 parsed configuration.
- The 13-Hammer explanation combines a verified 5 September Personal Tech capture with the current shared Clan Tech value; the character identity is intentionally omitted from the public guide.
- The unboosted timing is measured from repeated equivalent animation frames in the supplied 30-fps recording. Values at boosted Clan Tech levels are calculated from that observation and the current divisor configuration; a boosted run has not yet been timed directly.
- The ×50-per-star scaling is configuration-derived; the Multiverse/Divine comparison is an experienced-player approximation, not a replacement for the numbers displayed on an actual item.
- The exact random level-selection rule for newly forged equipment remains pending.
