<!-- Source book: ASCENSION_AND_REBUILDING_PLAYER_GUIDE_v0_1.md -->

# Ascension and Rebuilding

Players' Guide draft v0.2  
Evidence reviewed: 15 September 2026

## The short version

Do not ascend merely because the button is available. Ascension removes the assets belonging to the chosen pillar and begins a rebuilding period. Your first starred assets are much stronger than equivalent unascended assets, but the first low-rarity drops may still be weaker than the high-rarity unascended assets you have just lost.

Hoarding the retained basic resource before ascension gives you more immediate chances to recover the lost Power. It shortens the weak period before the ascended pillar reaches a sufficiently high rarity.

**Evidence status:** The overlap and star-scaling principles are supported by current decoded data and player observation. The reserve targets below come from Xyphic's community *Comprehensive Ascension Guide* (posted 12 April 2026 and edited 8 May 2026). They are useful planning estimates, not yet independently verified universal requirements.

## What a star means

- No star: unascended.
- One star: ascended once.
- Two or three stars: ascended repeatedly.
- The current decoded configuration supports a maximum of three stars.

A low numerical level after ascension should not be treated as an undeveloped ordinary asset. Compare the star count, rarity, level, displayed base values and modifiers together.

For equipment, pets and mounts, an ascended asset has two modifier slots regardless of the ordinary rarity or equipment-era slot rule.

### Character-wide Clan Tech Potion bonus

Ascension stars also provide a permanent character-wide economy benefit. For **every ascension star accumulated**, the character receives **+5% Clan Tech Potion rewards from all sources**.

This counts accumulated stars across the four ascension pillars rather than the star on one currently equipped asset. For example:

| Accumulated ascension stars | Clan Tech Potion reward bonus |
|---:|---:|
| 1 | +5% |
| 3 | +15% |
| 12 | +60% |

The Ascension Bonuses screen displays twelve steps, consistent with three possible stars in each of Forge/equipment, Skills, Pets and Mounts. This personal bonus is distinct from Clan Tech nodes that increase particular green-potion sources or Tech Race rewards.

## How large is the ascension increase?

Current decoded configuration applies a compounded multiplier to the applicable base values:

| Stars | Multiplier |
|---:|---:|
| 0 | x1 |
| 1 | x50 |
| 2 | x2,500 |
| 3 | x125,000 |

This applies to the appropriate base values for equipment, mounts, pets, active skills and skill passives. It does not mean that every one-star asset is automatically better than every zero-star asset: different rarities and levels start from different base values, and modifiers still matter.

## The important overlap

Experienced-player comparisons preserved in the archive give these useful approximations:

- one-star Multiverse equipment is roughly comparable with zero-star Divine equipment;
- a one-star Legendary pet or skill is approximately comparable with a zero-star Mythic version;
- a one-star Epic mount is approximately comparable with a zero-star Mythic mount.

These are orientation guides, not exact equality rules. Always prefer the visible values when comparing two actual assets.

The practical consequence is that the first starred Common assets do not necessarily restore the Power of the Divine equipment, Mythic pets/skills or Mythic mount removed at ascension. The overlap identifies the starred rarity at which the rebuilt pillar roughly catches up with its former unascended strength.

## Why hoarding works

Ascending without stock may leave you waiting for enough new starred assets to rebuild. Saving beforehand lets you forge, summon or hatch a larger batch immediately after ascension. This matters because the old assets from that pillar are removed; they cannot be retained while replacements are found.

The relevant resource depends on the section:

| Ascension area | Useful preparation stock | Purpose |
|---|---|---|
| Forge/equipment | Coins required to ascend plus hammers for subsequent forging | Generate starred equipment candidates |
| Mounts | Clock Winders | Generate starred mount candidates |
| Skills | Skill tickets | Generate starred skill candidates |
| Pets | Eggshells | Generate and develop starred pet candidates |

## What is lost and what survives

Ascension affects only the chosen pillar; the other three pillars remain unchanged. The reset rule is:

| Pillar ascended | Assets removed | Basic resources retained |
|---|---|---|
| Forge/equipment | Forge level/progress and all existing equipment | Coins and Hammers |
| Skills | All Skills and accumulated upgrade copies/progress | Skill Tickets |
| Pets | All Pets and all unhatched eggs | Eggshells |
| Mounts | All Mounts, including equipped, spare and XP-invested Mounts | Clock Winders |

The ascended pillar returns to Level 1. Nothing in the asset/progress column carries through: there is no preserved donor, Skill, copy counter or equipment item. The player rebuilds using only the retained raw currency. These reset and retention rules are player-confirmed.

## Forge ascension: confirmed mechanics

- The Forge can ascend at Level 35.
- The ascension payment is 3,000,000 coins.
- The payment currently receives no Clan War points.
- Ascension adds one Forge star and returns the Forge to Level 1.
- Equipment forged afterward carries the Forge's accumulated star count.
- The ordinary Level 1–35 costs, timers and equipment-tier probability sequence repeat.
- Stars improve the resulting equipment but do not improve the probability of receiving a higher equipment era.

Forge recovery is not immediate. Coins and Hammers survive, but every Forge level must be rebuilt through its upgrade process. The timers soon extend to many days, so retained stock cannot instantly restore the old Forge level or equipment-era probabilities. The delay does provide time to earn more Coins and Hammers while upgrading.

That final point explains why hammers remain useful: immediately after ascension, the Forge is again at the low-level end of the equipment-era distribution.

### Exact base recovery arithmetic

Each upgrade-table row's **Total coins** is already the whole cost of that level. Node count only divides the level cost into payments, and one timer runs once per level. From post-ascension Level 1, summing each intervening row once gives:

| A1 target | Cumulative base time | Ordinary upgrade coins | Including fixed 3,000,000 ascension payment |
|---:|---:|---:|---:|
| Level 27 | 60d 14h | 20,971,100 | 23,971,100 |
| Level 28 | 66d 22h | 23,201,100 | 26,201,100 |
| Level 35 | 120d 23h 20m | 41,891,100 | 44,891,100 |

Apply ordinary Forge Timer Speed as `base time ÷ (1 + speed bonus)` and ordinary Forge-cost reduction to the ordinary upgrade coins only. Do not discount the fixed ascension payment. For example, +50% Timer Speed and −25% ordinary upgrade cost make the Level-27 result `60d 14h ÷ 1.5 = 40d 9h 20m` and `20,971,100 × 0.75 + 3,000,000 = 18,728,325 Coins`.

## How many mount keys should I save?

The mount-summon resource is properly called **Clock Winders**. “Mount keys” and the source graphic's “Key Winders” refer to the same resource.

For the **first mount ascension**, the supplied community guide recommends rebuilding to at least an ascended Epic mount. It targets mount Level 31, where it says Epic has a 7.2% summon chance, and gives this base reserve:

> **30,000 Clock Winders before Personal Tech reductions.**

The guide assumes 50-summon bundles. It combines the Mount Summon cost-reduction node with the Extra Mount Summon chance node. Current verified Personal Tech data confirms that each sublevel gives −1% summon cost and +2% extra-summon chance, with five sublevels in each tier.

The resulting first-ascension estimates are:

| Personal Tech position | Cost reduction | Extra-summon chance | Estimated Clock Winders for Epic target |
|---|---:|---:|---:|
| No relevant Tech | 0% | 0% | 30,000 |
| Tier III range | 11–15% | 22–30% | 19,615–21,885 |
| Tier IV range | 16–20% | 32–40% | 17,143–19,091 |
| Tier V complete | 25% | 50% | 15,000 |

Here **Tier III/Tier IV means the tier reached in Personal Tech for those two mount-summon nodes**. It does not mean mount rarity or mount ascension count. The source advises waiting until at least Tier III and calls Tier IV the “sweet spot” for first mount ascension.

The estimate uses:

`30,000 × (1 − summon-cost reduction) ÷ (1 + extra-summon chance)`

This gives a far better planning answer than a bare key-to-summon conversion, but the 30,000-Winder target and Level-31 rarity assumption remain community guidance pending independent verification.

For simple conversions, one ordinary mount summon costs 50 Clock Winders before Personal Tech reduction:

| Reserve | Summons |
|---:|---:|
| 500 | 10 |
| 1,000 | 20 |
| 2,500 | 50 |
| 5,000 | 100 |

Personal Tech can reduce summon cost, so use the cost shown in your own game when it differs from 50. These figures are conversions only; the community target above additionally allows for expected extra summons.

## Community rebuilding targets for the other pillars

These targets explain what the Discord guide means by saving enough resources to regain roughly the pre-ascension Power level.

| Pillar | First-ascension rebuilding target | Base reserve estimate | Estimate with stated Tech effect |
|---|---|---:|---:|
| Forge/equipment | First 4% Multiverse checkpoint at Forge Level 22 | 11,471,100 total coins including the fixed 3m ascension payment | 9,353,325 total at 25% ordinary Forge-cost reduction |
| Forge/equipment, stronger distribution | Forge Level 25: 32% Multiverse plus 4% Quantum | 16,841,100 total coins including the fixed 3m ascension payment | 13,380,825 total at 25% ordinary Forge-cost reduction |
| Skills | Legendary at Skill Level 24 (claimed 2% chance) | 49,600 tickets | 37,200 at 25% ticket-cost reduction |
| Pets | Legendary at Pet Level 37 (claimed 7.2% chance) | 48,600 eggshells | 32,400 with 50% extra-drop chance |
| Pets, cheaper fallback | Epic at Pet Level 15 (claimed 20% chance) | 7,100 eggshells | 4,733 with 50% extra-drop chance |
| Mounts | Epic at Mount Level 31 (claimed 7.2% chance) | 30,000 Clock Winders | 15,000 with 25% discount and 50% extra-summon chance |

The Forge figures include the separate fixed 3,000,000-coin ascension payment and assume the player uses gems to rush the upgrade timers. One-star Multiverse versus unascended Divine is only an approximate per-item orientation; neither checkpoint promises whole-build parity across eight slots. The pet fallback was suggested only when the old Mythic pets had poor modifiers; it is not presented as equal to a strong Mythic pet loadout.

The source's priority opinion was Forge **very high**, Skills **high**, Pets **medium** and Mounts **low**. Treat that as author advice rather than a game rule: actual order depends on the player's current assets, stocks and Personal Tech.

## Equivalent preparation conversions

- A base bundle costs 200 Skill Tickets for five skill summons: 40 tickets per summon before any player-specific reduction.
- The Skill Summon cost Personal Tech node can reduce that ticket cost, so use the price displayed in the player's game when calculating a reserve.
- One egg costs approximately 100 eggshells, but hatching capacity and time limit how quickly the stock can be used.
- One Mount merge consumes one donor Mount; the retained recipient remains. Each available donor therefore provides one merge action.

Earlier chat advice suggested roughly 20,000 eggshells as a minimum pet-rebuilding reserve and 40,000–50,000 as comfortable. The newly supplied community guide instead gives target-specific figures: 7,100 for the cheaper Epic route or 48,600 for the Legendary route before extra-drop effects. The older 20,000/40,000–50,000 bands should therefore remain under review rather than being blended with these different targets.

## Ascension and Clan War timing

Pets, Mounts and Skills need an additional scheduling decision. Their assets and accumulated progress do not survive, but they may represent active Clan War score through Pet/Mount merges or available Skill upgrades. Ascending during a savings or easy war therefore creates two bad choices: leave that potential unused and lose it in the reset, or consume it first and create a large active score in a week where it may not matter.

The better default is to protect the relevant raw-currency reserve while it accumulates, then choose a hard or competitive war. Use the old Pet/Mount merge bank or available Skill upgrades only as much as helps secure the win, following **only spend enough active scoring resource to win**. When ascension is confirmed, every remaining asset and unit of accumulated progress in that pillar is lost; none carries into the rebuild.

Saving a substantial reserve—often 20,000+ Eggshells for the Pet route selected—usually takes weeks, so the player should have several wars in which to choose a useful transition window. This is scheduling context, not a universal minimum. Skills and Mounts follow the same loss/retention logic with Skill Tickets and Clock Winders.

## Sensible preparation checklist

Before ascending:

1. Confirm exactly which pillar is ascending and what will reset.
2. Record the quality of the existing assets you need to replace.
3. Check the current displayed summon or forging costs, including Personal Tech reductions.
4. Retain enough currency to pay the ascension cost itself.
5. Build a stock of the relevant forging, summoning or hatching resource.
6. Expect the chosen pillar's old assets to be removed when ascension is confirmed.
7. Do not confuse a Clan War weekly spending allowance with an ascension reserve.

## Still being investigated

- The exact ascension activation levels for pets, skills and mounts.
- Direct current-game confirmation that pets and unhatched eggs, skills, mounts and equipment are removed exactly as the community overview states.
- Independent confirmation of the quoted rarity chances and resource totals.
- Whether the guide's expected-value estimates produce an adequate modifier mix, rather than merely the target rarity.
- Minimum, comfortable and strong reserve bands beyond the guide's single rebuild targets.

Where these details matter, the guide should say that the answer is pending rather than inventing a number.
