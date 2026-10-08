# Evidence selection and temporal synthesis

Use this reference after a Ziweave chart tool succeeds.

## 1. Validate the response before interpretation

For every timing result require `coverage.complete === true`, matching requested scope coverage, one profile revision/policy, and an explicit calculation timezone. Then validate the result's own shape:

- Instant `timing-context`: all seven scopes (`natal`, `decadal`, `age`, `yearly`, `monthly`, `daily`, `hourly`), one resolved target time, and twelve `palaceMatrix` slots.
- Period `timing-period-context`: a shared `normalized.natal` with twelve indexed palaces and `normalized.segments` covering the exact Gregorian `[startDate, endDateExclusive)` without gaps or overlap. Every segment has decadal, age and yearly; month results also have monthly. Year results deliberately omit monthly; both period forms omit daily/hourly. Validate each layer's twelve aligned palace-name/star slots, with `age.stars:null` allowed, and use the returned UTC boundaries/timezone. Do not require an instant-only matrix or fabricate omitted layers.

If any invariant is missing, do not fill the gap from memory. Report that the context is incomplete.

For a day/week assembled from multiple instant results, also validate the target inventory for the requested granularity and scope-specific windows in [request-planning.md](request-planning.md#days-whole-days-and-weeks). Completing an ordinary main-daily comparison is different from covering every hour or all 24 hours; do not expand the former into the latter by default. Complete individual instant responses are usable building blocks; a missing batch endpoint is not missing evidence. Combine only compatible profile/policy/timezone results. Read daily and higher layers for a daily comparison, and hourly layers only within their matching shichen windows. Do not extend one result's `coverage.complete` to targets that have not been obtained.

## 2. Select evidence by topic

Identify the user's actual topic before reading stars. Start with palace names present in the response rather than hard-coded slot numbers. Use the following as a routing heuristic, not a universal doctrinal verdict:

| Topic | Primary evidence | Common supporting evidence |
|---|---|---|
| Money, purchase, gacha | 財帛 | 命宮、福德；事業 when income/work is central |
| Work, interview, contract | 官祿／事業 | 命宮、財帛、遷移 |
| Relationship | 夫妻 | 命宮、福德、交友 |
| Travel, move, outside opportunity | 遷移 | 命宮、官祿／事業 |
| Health or stamina | 疾厄 | 命宮、福德 |
| Mood, enjoyment, impulse | 福德 | 命宮、財帛 when spending is involved |

Names can vary by locale. Match semantic palace names in the DTO. If the topic is ambiguous, explain which interpretation you chose rather than silently mixing many domains.

Select a palace independently within every scope and period segment. In an instant matrix, find the unique slot whose `overlays[scope].palaceName` matches the intended palace, then read that overlay and its same-slot natal palace. For natal evidence, find the slot by `slot.natal.key` or `slot.natal.label`.

Period responses use a compact representation instead of `palaceMatrix`. Within each segment and scope, locate the intended name in `segment.layers[scope].palaceNames`; its array position is the documented natal slot index for that same layer's `stars[index]`. Match the shared natal palace by its explicit `index`. Do not interpret `layer.index` as the selected topic's slot or assume every scope's same-named palace occupies the same slot. Never find the natal 財帛 slot once and call every temporal overlay there「流年財帛／流月財帛／流時財帛」.

Within those per-scope selected slots, prioritize traceable evidence:

1. natal major/minor stars and natal mutagens or brightness when present;
2. the selected temporal layer's palace mapping and actual scope stars;
3. an actual selected-palace star whose own `mutagen` field is non-null;
4. corroborating evidence from a supporting palace.

Do not list every star. Prefer a small set that materially changes the conclusion and can be found in the response.

`overlay.mutagens` and a period `layer.mutagens` are layer-wide four-star lists. They do not encode the 祿／權／科／忌 role beside each entry. Do not assign one of those stars to a selected palace, or name its transformation role, from that list alone. Use the selected overlay/slot's actual stars and each star's own `mutagen` field instead.

## 3. Apply temporal hierarchy without fake precision

Use these roles:

- natal: structural baseline;
- decadal: long-horizon environment;
- age: age-stage modifier; it may have no upstream stars;
- yearly: annual background;
- monthly: current medium-term condition;
- daily: short window;
- hourly: immediate window.

Do not assign an invented numeric weight. Classify how the layers relate:

- `convergent`: long and short layers point in a similar direction;
- `countertrend-window`: broader background is restrained, but day/hour offers a relative short window;
- `temporary-headwind`: broader background is supportive, but day/hour is temporarily less supportive;
- `mixed-or-indeterminate`: evidence is conflicting or insufficient.

A favorable short layer does not erase broader risk. An unfavorable month does not mean every day and hour is unfavorable. The shorter the window, the more it can justify only a small, reversible, low-cost experiment.

## 4. Compose the answer

Use everyday language first: what may feel easier or harder, why that matters for the user's situation, and a practical way to respond. Keep most star names, palace names, overlaps and layer-by-layer trace in your internal analysis. When a term materially helps, introduce it briefly with its ordinary-language meaning; do not make the user decode a string of terms. In English, explain the idea naturally rather than replacing Chinese jargon with pinyin or a glossary of literal translations. Give only enough concrete chart evidence to support the conclusion, preserve real date changes, and keep uncertainty proportionate instead of repeating the same disclaimer in each paragraph.

Cover these ideas without forcing headings when a concise answer is clearer:

1. the longer-term background;
2. the requested period's included layers and any actual changes across its segments;
3. day/hour modulation only for an instant result or separately requested, complete finer evidence;
4. whether the signals converge or conflict;
5. a conditional conclusion proportional to the decision's cost;
6. the target moment or Gregorian period in the response's calculation timezone; use explicit segment boundaries where supplied, without inventing validity windows;
7. uncertainty and real-world limits.

For internal verification, retain a compact evidence trail such as the following; do not paste field paths or this diagnostic chain into an ordinary user reply:

```text
流時 -> 找到 overlays.hourly.palaceName=財帛的 slot -> 該流時財帛 overlay -> [response star] -> immediate spending impulse
```

Every named star, palace, mutagen, and scope must be present in the tool response.

If a short follow-up suggestion adds value, use the optional examples in [request-planning.md](request-planning.md#optional-follow-up-examples). Do not fetch charts to generate suggestions or automatically append a website link; use the skill's missing-evidence plus explicit quota-insufficient rule.

For gacha, even a relatively supportive symbolic window can justify at most a pre-budgeted, reversible entertainment action. It never means the drop rate, mathematical odds, expected value, or outcome probabilities improved.
