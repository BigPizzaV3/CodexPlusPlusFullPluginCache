<!-- Source book: RESOURCES_PLAYER_GUIDE_v0_1.md -->

# ForgeMaster Resources Guide

Status: **Public draft v0.1**  
Evidence cutoff: **11 September 2026**

This chapter explains what ForgeMaster resources do, how players obtain them, which resources are immediately spendable and which are limited by timers or capacity. Exact rewards can vary with progression, league, Clan War tier and Tech. Where the game displays a player-specific cost or reward, use that live value.

## Quick resource map

| Resource | Principal use | Important constraint |
|---|---|---|
| Coins | Forge upgrades; fixed 3m Forge ascension; some event payments | Forge upgrades become heavily time-gated; Personal Tech can reduce ordinary upgrade cost but does not appear to reduce the 3m ascension price |
| Hammers | Forge equipment | Forging consumes hammers but produces equipment and coins; normally plentiful compared with the other war resources |
| Skill Tickets | Summon and improve Skills | Base bundle is 200 tickets for five summons: 40 tickets per summon; Personal Tech can reduce the cost |
| Eggshells | Obtain eggs for Pets | Approximately 100 shells per egg; hatching is time-gated, so shells are not the same as immediately usable pets |
| Eggs | Hatch into Pets | Existing unhatched eggs are separate from eggshells and occupy the hatching pipeline |
| Clock Winders | Summon Mounts | Base cost is 50 per summon; Personal Tech can reduce cost and add a chance of an extra summon |
| Red Personal Tech Potions | Start Personal Tech upgrades | Cost is paid when the upgrade starts; only one Personal Tech upgrade can run or await completion at a time |
| Green Clan Tech Potions/Vials | Donate to Clan Tech and the Clan Tech Race | One ordinary donation costs two green potions; do not confuse these with red Personal Tech Potions |
| Gems | Finish a running Forge upgrade immediately and other premium uses | Finish Now charges according to remaining time; gems are not Forge coin-node funding |
| Dungeon keys | Enter Hammer Thief, Ghost Town, Invasion and Zombie Rush | Two uses per dungeon per day, eight total; unused daily capacity does not carry forward |
| War tickets | Attack rival players during the Day-6 brawl | Five per member for the brawl |
| Stepping Stones tokens | Play the recurring Stepping Stones minigame | Eight free tokens are offered daily during the event; unclaimed daily tokens expire, while claimed tokens accumulate |

Equipment, Skills, Pets and Mounts are also progression assets. Spare Pets and Mounts are resources for merging, but they must not be added to currency balances as though they were summons waiting to happen.

## Core spending conversions

| Action | Base requirement | Tech interaction |
|---|---:|---|
| One Skill summon | 40 Skill Tickets | Skill Summon cost: −1% per Personal Tech sublevel |
| Five Skill summons | 200 Skill Tickets | Same reduction applies to the displayed bundle cost |
| One Mount summon | 50 Clock Winders | Mount Summon cost: −1% per sublevel; Extra Mount Summon chance: +2% per sublevel |
| One egg | Approximately 100 Eggshells | Extra Egg chance can improve effective yield; rarity-specific Tech reduces hatching time |
| One ordinary Clan Tech donation | 2 green Clan Tech Potions | Clan Tech Race Score multipliers can increase race score credited for donations |
| One Pet merge | 1 donor egg or Pet | Donor XP transfers; donor modifiers do not; merge score may matter on Days 3 and 5 |
| One Mount merge | 1 donor Mount | Donor XP transfers; donor modifiers do not; merge score may matter on Days 2 and 4 |

Do not apply a base conversion when the player's live screen shows a reduced cost. A reduced summon cost and an extra-summon chance are different benefits and should be calculated separately.

## Where resources come from

### Dungeons

| Dungeon | Base reward |
|---|---|
| Hammer Thief | Hammers and coins |
| Ghost Town | Skill Tickets |
| Invasion | Eggshells |
| Zombie Rush | Red Personal Tech Potions |

Each dungeon progresses independently from `1-1` through `1-20`, then `2-1`, up to `20-20`. If the next level cannot be defeated, **Sweep Last** awards the reward for the last successfully completed level.

Convert displayed level `n-m` to a flat level with `L = 20 × (n − 1) + m`. The game-file base-reward fields then give:

| Dungeon reward | Base formula for one run |
|---|---:|
| Hammer Thief coins | `3,900 + 100L` |
| Hammer Thief hammers | `198 + 2L` |
| Invasion Eggshells | `59 + L` |
| Ghost Town Skill Tickets | `199.35 + 0.65L` internally |
| Zombie Rush red potions | `99 + L` |

| Level | Hammer coins | Hammer hammers | Invasion shells | Ghost tickets, internal | Zombie red potions |
|---|---:|---:|---:|---:|---:|
| `1-1` | 4,000 | 200 | 60 | 200.00 | 100 |
| `1-20` | 5,900 | 238 | 79 | 212.35 | 119 |
| `2-1` | 6,000 | 240 | 80 | 213.00 | 120 |
| `20-20` | 43,900 | 998 | 459 | 459.35 | 499 |

Ghost Town is stored fractionally in configuration. The client's final displayed/awarded rounding rule has not yet been observed directly, so calculations should preserve the internal value rather than silently choose floor or nearest-integer rounding.

Each dungeon has two daily uses. The four dungeons therefore provide up to eight daily runs. Two sweeps at the same completed level award twice its reward; two successful progression attempts instead award the two newly cleared levels. This capacity is use-it-or-lose-it rather than a hoardable reserve.

Relevant Personal Tech can increase dungeon yield. The formulas above are deliberately **base rewards before Personal Tech**, and a player's live payout is the best evidence for the adjusted amount.

### Clan missions

- Clan Missions are independent of dungeon progress.
- Six mission offers appear each day, with one refresh available.
- A player receives three Mission Tickets per day. A ticket is consumed by a successful mission, allowing up to three rewarded completions.
- Failing does not consume a Mission Ticket, but the failed mission is removed from the available list.
- Choosing a mission starts a rally lasting **1, 3 or 10 minutes**. A rally icon appears on other clan members' main game screens.
- Up to three other clan members can join and lend their power, increasing the chance that the mission succeeds. Only the player who started the mission receives its reward.
- An assisting player may leave before the rally timer ends and may assist rallies as often as desired; assisting does not use that player's Mission Tickets.
- A one-minute rally is normally suitable for an easy mission. A ten-minute rally gives clan members more time to notice and join a difficult mission.
- Each completed mission shows four reward draws; duplicate rewards combine in the displayed result.
- An unusually difficult mission should not be budgeted as routine income merely because assistance is possible.

The current planning allowance for an active player completing three missions is **provisional**: about 500 Skill Tickets, 200 Eggshells, 100 Clock Winders and 20 green potions per day. This is an expected mixed daily allowance, not a guaranteed bundle and not an amount to add three times.

### Offline rewards

The base maximum offline period is four hours. The Maximum Offline Time Personal Tech effect adds 16% of the base duration per sublevel:

| Completed sublevels | Maximum offline time |
|---:|---:|
| 0 | 4h |
| 5 | 7h 12m |
| 10 | 10h 24m |
| 15 | 13h 36m |
| 20 | 16h 48m |
| 25 | 20h |

Separate Personal Tech nodes increase offline coin and hammer rewards by 1% per sublevel. Extending maximum offline time helps only when the player would otherwise remain away beyond the existing cap.

### Clan War rewards

Clan War produces two distinct reward streams:

1. an end-of-war reward determined by the clan's tier and whether it won or lost;
2. personal milestone boxes earned from the player's cumulative war score.

A loss is not a zero-income week.

#### End-of-war reward per eligible player

| Tier | Result | Hammers | Skill Tickets | Eggshells | Red Tech Potions | Clock Winders | Green Potions |
|---|---|---:|---:|---:|---:|---:|---:|
| S++ | Win | 5,800 | 8,600 | 5,700 | 6,500 | 4,400 | 200 |
| S++ | Loss | 2,650 | 3,900 | 2,600 | 2,900 | 2,000 | 40 |
| S+ | Win | 5,500 | 8,190 | 5,500 | 6,200 | 4,200 | 50 |
| S+ | Loss | 2,650 | 3,900 | 2,600 | 2,900 | 2,000 | 20 |
| S | Win | 5,300 | 7,800 | 5,200 | 5,900 | 4,000 | 20 |
| S | Loss | 2,650 | 3,900 | 2,600 | 2,900 | 2,000 | 10 |
| A | Win | 3,750 | 3,600 | 2,500 | 2,800 | 1,900 | 15 |
| A | Loss | 1,870 | 1,800 | 1,250 | 1,400 | 1,000 | 8 |
| B | Win | 2,130 | 2,100 | 1,400 | 1,580 | 1,000 | 10 |
| B | Loss | 1,060 | 1,050 | 700 | 790 | 500 | 5 |
| C | Win | 1,060 | 1,050 | 700 | 800 | 525 | 10 |
| C | Loss | 530 | 525 | 350 | 400 | 260 | 5 |
| D | Win | 530 | 520 | 350 | 400 | 250 | 10 |
| D | Loss | 265 | 260 | 175 | 200 | 125 | 5 |
| E | Win | 265 | 260 | 170 | 200 | 125 | 10 |
| E | Loss | 130 | 130 | 85 | 100 | 65 | 5 |

The full table is supplied-table evidence. The S+ loss row was independently observed in game on 7 September 2026.

#### Personal milestone bundles

- **Bundle A:** 70 Hammers, 250 Skill Tickets and 165 Eggshells.
- **Bundle B:** 15,000 Coins, 220 red Personal Tech Potions and 140 Clock Winders.
- Later boxes award the displayed quantity of green Clan Tech Potions.

Each milestone box is awarded once per war when the player's cumulative score reaches its threshold. It must not be counted once per day or once per action.

### Clan Tech Race

Current base green-potion rewards per eligible player are **800, 300, 150, 80, 40, 20 and 10** for first through seventh. Every accumulated character ascension star adds +5% Clan Tech Potion rewards from all sources, and the Clan Tech Race Reward node can also increase the payout. Their combined stacking and rounding remain under verification, so use the amount displayed for the character. Eligibility and collection remain server-controlled.

### Ranked League

Ranked League provides another weekly resource stream, with amounts varying by league and finishing band. The current named game configuration resolves the older workbook's icon-only headings as Hammers, Coins, Skill Tickets, Eggshells, red Personal Tech Potions, Clock Winders and—in Diamond II and III—green Clan Tech Potions.

See the separate **Ranked Leagues Guide** and **League Rewards Reference** for the current eight-league ladder, promotion/demotion boundaries and complete reward table. Treat a projected League finish as expected income rather than collected stock until the weekly result is settled and the reward has been received.

### Stepping Stones

During the recurring Stepping Stones event, the shop offers eight free tokens per day. One token buys one game. Unclaimed daily shop tokens do not roll over, but tokens already claimed into the player's balance can accumulate. At 20 or more tokens, Auto ×20 can play 20 games automatically.

The visible reward ladder contains Hammers, Coins and combat-boosting skins. Random tile-8 skins display a 2%–12% Damage or Health range, and a 10.5% skin has been directly observed. Extra tokens can be purchased for real money, but free and purchased tokens should not be assigned different odds without evidence.

## Liquid, time-gated and expiring capacity

| Class | Examples | Planning consequence |
|---|---|---|
| Liquid stock | Tickets, shells, Winders, coins, red potions, green potions, hammers | Can generally be saved and spent later, subject to the action's own rules |
| Time-gated stock | Eggs waiting to hatch; Forge levels; running Personal Tech | A large currency balance does not remove the timer |
| Daily capacity | Dungeon keys; mission completions; unclaimed daily Stepping Stones shop tokens | Unused capacity is lost rather than accumulated indefinitely |
| Claimed event stock | Stepping Stones tokens already moved into the player's balance | Can accumulate for later use during the event; 20 permit Auto ×20 |
| Event-limited value | Fairy upgrades and temporary event spending | Consider the time remaining and alternative permanent uses of the resource |

This distinction prevents misleading statements such as treating 50,000 Eggshells as 500 immediately available Pets or treating eight unused dungeon runs as eight keys added permanently to stock.

## Saving and spending principles

- Keep a reserve for the next intended ascension before spending heavily for Clan War points.
- Where possible, delay ordinary progression spending until the matching Clan War scoring day, so one action serves progression and war participation.
- Do not spend merely because a resource can score. Compare the likely reward or strategic value with the permanent progression sacrificed.
- Use exact current balances and displayed costs for personal advice.
- Count a reward only after it is earned and collected, and do not add it again if it is already included in a later stock screenshot.
- Keep red and green potions separate in every calculation.
- Treat mission averages and future rewards as estimates; do not add them to an observed balance and call the result exact.

## Personal Tech effects on resources

| Effect | Per sublevel |
|---|---:|
| Forge Upgrade coin cost | −1% |
| Equipment sell return | +1% |
| Hammer Thief hammer reward | +1% |
| Hammer Thief coin reward | +1% |
| Maximum offline time | +16% of the four-hour base |
| Offline coin reward | +1% |
| Offline hammer reward | +1% |
| Mount Summon cost | −1% |
| Extra Mount Summon chance | +2% |
| Personal Tech upgrade potion cost | −2% |
| Skill Summon cost | −1% |
| Extra Egg chance | +2% |
| Ghost Town Skill Ticket reward | +1% |
| Zombie Rush red-potion reward | +2% |

Rarity-specific egg-timer nodes make hatching 10% faster per sublevel for their own rarity. The +1% Hammer Thief coin and hammer increments, +1% Ghost Town increment and +2% Extra Egg increment are confirmed by live node popups. The Zombie Rush +2% increment remains configuration/rulebook-derived rather than independently popup-confirmed in this pass. Tech percentages may interact with rounding, so use the live displayed reward, cost or timer for a particular player whenever available.

## Evidence still needed

- one collected weekly League bundle matched against the current named game configuration;
- broader live verification of the Clan War outcome table outside the confirmed S+ loss row;
- a representative current sample of mission rewards and the correct normal daily green-potion yield;
- live confirmation of Ghost Town's final ticket rounding and the adjusted payout rounding used by each dungeon Tech node;
- exact gem earning sources and ordinary availability;
- more live evidence for resource retention and asset removal across each non-Forge ascension.
- exact Stepping Stones event cadence, reward-settlement rule, skin stacking/duplicate behaviour and direct confirmation of a 12% skin.


---

<!-- Source book: DUNGEONS_AND_CLAN_MISSIONS_PLAYER_GUIDE_v0_1.md -->

# ForgeMaster Dungeons and Clan Missions

Status: **Player-facing draft v0.1**  
Evidence cutoff: **11 September 2026**

## Two separate systems

Dungeons and Clan Missions are both repeatable sources of resources, but they do not unlock, control or advance one another.

| Dungeons | Clan Missions |
|---|---|
| Four independent combat ladders | A daily choice from six mission offers |
| Two daily uses for each dungeon | Three Mission Tickets per day |
| Rewards depend mainly on the dungeon and cleared level | Rewards are drawn from the selected mission's reward pool |
| A player fights or sweeps alone | Up to three clan members can assist through a rally |
| Progress is retained separately for each dungeon | A failed mission disappears from that day's list |

## Dungeons

### The four dungeons

| Dungeon | Base reward |
|---|---|
| Hammer Thief | Coins and Hammers |
| Ghost Town | Skill Tickets |
| Invasion | Eggshells |
| Zombie Rush | Red Personal Tech Potions |

These names and rewards are the current live-game mapping. Some extracted files use internal labels that can be misleading when they are not joined through the language data correctly.

### Daily uses

Each dungeon provides **two uses per day**:

- two Hammer Thief uses;
- two Ghost Town uses;
- two Invasion uses;
- two Zombie Rush uses.

That gives eight dungeon uses in total each day. They do not accumulate for later days, so use them even when no Clan War points are available.

### Level progression

Each dungeon has its own progression ladder. Levels are displayed as `n-m`:

`1-1, 1-2, ... 1-20, 2-1, ... 20-20`

Clearing the current level unlocks the next level in that dungeon. A sufficiently powerful player can therefore advance by two levels per day in each dungeon.

For calculations, convert the displayed level to a flat level:

`L = 20 × (n − 1) + m`

Examples:

| Displayed level | Flat level `L` |
|---|---:|
| `1-1` | 1 |
| `1-20` | 20 |
| `2-1` | 21 |
| `20-20` | 400 |

### Sweep Last

If the player cannot beat the next level, **Sweep Last** awards the rewards from the last level successfully completed. This lets the player continue collecting daily resources without repeatedly attempting a level that is currently too difficult.

A sensible routine is:

1. Attempt the next level when it appears realistically beatable.
2. If progression is blocked, use Sweep Last for dependable income.
3. Try the next level again after improving the build or relevant Tech.

### Base rewards

The current extracted reward curves give these base amounts for one run:

| Reward | Base formula |
|---|---:|
| Hammer Thief Coins | `3,900 + 100L` |
| Hammer Thief Hammers | `198 + 2L` |
| Invasion Eggshells | `59 + L` |
| Ghost Town Skill Tickets | `199.35 + 0.65L` internally |
| Zombie Rush red potions | `99 + L` |

Selected examples:

| Level | Hammer Coins | Hammer Hammers | Invasion shells | Ghost tickets, internal | Zombie red potions |
|---|---:|---:|---:|---:|---:|
| `1-1` | 4,000 | 200 | 60 | 200.00 | 100 |
| `1-20` | 5,900 | 238 | 79 | 212.35 | 119 |
| `2-1` | 6,000 | 240 | 80 | 213.00 | 120 |
| `20-20` | 43,900 | 998 | 459 | 459.35 | 499 |

Ghost Town is stored with fractional values at many levels. The game's final display and award rounding has not yet been verified, so the player's live reward should take precedence over a calculated integer.

### Tech affecting dungeons

Personal Tech can improve some dungeon rewards:

| Personal Tech effect | Increase per sublevel |
|---|---:|
| Hammer Thief Hammer reward | +1% |
| Hammer Thief Coin reward | +1% |
| Ghost Town Skill Ticket reward | +1% |
| Zombie Rush red-potion reward | +2% |

There is no confirmed current Personal Tech node directly increasing Invasion Eggshell rewards. **Extra Egg Chance** applies later when Eggshells are converted into eggs; it does not increase the shells dropped by Invasion.

Clan Tech has separate Damage and Health nodes for each dungeon. These make its battles easier and may help a player progress to a higher reward level, but they do not directly multiply the base drop.

### Dungeons during Clan Wars

Using a dungeon key scores Clan War points on Days 1 and 4. The current base value is **3,000 points per use**, so all eight daily uses can produce **24,000 base points** on either scoring day before Clan Tech bonuses.

This is passive scoring in the Players' Guide sense: the daily uses cannot be hoarded, so using them does not consume a scarce saved stock. On non-scoring days, use them anyway for resources and progression.

## Clan Missions

### Daily mission choices

- Six mission offers appear each day.
- One refresh is available.
- The player receives three Mission Tickets per day.
- A successful mission consumes one ticket and awards its rewards.
- A failed mission consumes no ticket, but that failed mission is removed from the list.
- Three tickets therefore allow up to three successful rewarded missions that day.

Failure is not completely free: the ticket remains, but that particular opportunity is lost.

### Starting a rally

Selecting a mission starts a rally. The initiating player chooses a rally duration of **1, 3 or 10 minutes**. During that time, an assistance icon appears on other clan members' main game screens.

Up to three other clan members can join and lend their Power, increasing the chance of success. The exact success calculation is not yet established.

Only the player who started the mission receives the reward. Assistants lend Power; they do not receive a copy or share of the payout.

### Assisting other players

- An assistant can leave the rally before its timer expires.
- A player may assist as many rallies as desired.
- Assisting does not use that player's own three Mission Tickets.
- Joining difficult rallies is therefore helpful to the clan even when the assistant has completed their own missions.

### Choosing the rally duration

| Mission situation | Sensible rally time |
|---|---:|
| Easily beaten alone | 1 minute |
| Some assistance may help | 3 minutes |
| Difficult and likely to need several helpers | 10 minutes |

The longer timer does not itself provide more Power. It gives other clan members more time to notice the rally and join it.

### Mission rewards

A completed mission shows four reward draws. If the same resource appears more than once, the game combines those duplicates in the displayed result.

The current provisional allowance for an active player completing three routine missions is approximately:

- 500 Skill Tickets;
- 200 Eggshells;
- 100 Clock Winders;
- 20 green Clan Tech Potions;

This is a mixed **daily planning estimate**, not a guaranteed bundle and not an amount earned by every individual mission. Actual offers, choices, difficulty and Tech affect the result.

Clan Tech can improve Mission Damage, Mission Health and mission rewards. A separate node improves the green Clan Tech Potions obtained from missions.

### Choosing missions sensibly

1. Prefer missions that offer resources useful to the player's current goal.
2. Do not spend all three tickets on low-value choices merely to clear the list.
3. Use the refresh when the initial selection is poor.
4. Choose reliably completable missions for routine income.
5. Save a difficult high-value mission for a time when helpers are likely to be online.
6. Use a longer rally when assistance is genuinely needed.

## Daily checklist

- Use both attempts in all four dungeons.
- Progress where practical; otherwise Sweep Last.
- Review six mission offers before committing all three tickets.
- Use the refresh strategically.
- Complete up to three worthwhile missions.
- Watch for other members' rally icons and assist when available.
- On Clan War Days 1 and 4, remember that the same dungeon uses also score war points.

## What remains uncertain

- Whether a failed dungeon battle consumes one of the two daily uses.
- Ghost Town's final fractional reward rounding.
- Rounding when Personal Tech reward bonuses are applied.
- The exact Clan Mission success calculation and how each assistant's Power is incorporated.
- The complete current mission reward distribution and a verified normal daily average.
- The precise reset time and whether any displayed unused Mission Tickets can ever persist across it.

Where one of these details affects a decision, use the value or warning shown in the player's current game rather than assuming a hidden formula.
