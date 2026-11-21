---
name: audience-profile
description: Profile a target consumer segment, covering who they are, what they value, how they behave in the category and what drives purchase, by indexing Statista Consumer Insights survey data against the general population. Use whenever someone asks to describe or understand a target audience, customer segment, persona, priority target or "who buys X", or wants consumer insight to brief a campaign, product or proposition, even without the word "segment".
---

# Audience Profile

Describe a segment by how it differs from the average consumer, not only by what it looks like. A trait counts as defining when it is common in the segment, over-represented against the population, and statistically significant.

**Scope:** demographics, values and interests, category behaviour, purchase drivers and barriers. Media consumption and brand metrics are out of scope.

## Inputs

| Input | Default if missing |
|---|---|
| Segment definition | Required. Ask if absent. |
| Country | The country named in the request; otherwise ask. |
| Survey year | Latest available |
| Comparison base | Online population aged 18–64 in that country's survey |

## How the Consumer Insights tools behave

- **Splits.** Survey questions sit in splits, shown as `splits_by_project_group` in search results. A segment can only be crossed with questions in the same split (e.g. `gcs: "2"`) or with demographic questions (`demo`). Any other combination returns a 404, and so does a country that never fielded the question. Report both as gaps.
- **Segment and total.** Crosstabs do not return a total column. Fetch each descriptor twice:
  - with `filters` = [defining answer ID] → segment %;
  - without filters → total %.
- **Single numbers.** An answer ID passed as `rows` returns one share for the country. Use it to read segment size.
- **Respondent counts.** Every cell carries one. The segment base is the count on the defining answer.

## Workflow

1. **Make the segment measurable.**
   - Call `search-consumer-insights` with short queries to find an answer that defines the segment, e.g. a shopper typology or "bought X in the last 12 months". Prefer answers in the core survey (`gcs`), because they cross with the most descriptors.
   - Fetch the defining answer as `rows` for the country to get the segment share and n.
   - If no answer fits, use the closest proxy and state the gap.
2. **Choose descriptors.** Pick 2–5 questions per block. Each must sit in the defining answer's split or be demographic.
   - **Demographics:** age, gender, household income for that country, community type.
   - **Values and interests:** life values, hobbies.
   - **Category behaviour:** online and offline purchases by category, premium purchase by category, channel.
   - **Drivers and barriers:** purchase criteria and reasons. These are often in other splits. Try them, and report a gap if they cannot be crossed.
3. **Fetch** segment % and total % for each descriptor, as above. Record each row's n. Mark rows as modelled when the description says data was filled from demographics.
4. **Index** every row as set out in "Indexing" below. Present only rows flagged distinctive as traits.
5. **Synthesize.**
   - **Defining traits:** 3–5, taken from the distinctive rows with the largest gaps.
   - **Portrait:** a plain-language description that claims nothing beyond the data.
   - **Implications:** for messaging, proposition and purchase channel, each tied to a row.
   - **Non-differentiators:** state traits that do not set the segment apart, e.g. "not younger than average". They prevent mis-targeting.

## Indexing

Collapse fine answer bands, such as income brackets, into 3–4 groups first. For each row, with segment % s, total % t and segment base n:

- **Index** = s ÷ t × 100.
- **z** = (s − t) ÷ √(t × (100 − t) ÷ n), with s and t in percent. Leave z blank when n is unknown or t is 0 or 100.
- **Flag**, taking the first that applies:
  - **distinctive:** index ≥ 120 or ≤ 80, and s ≥ 10%, and n ≥ 100, and |z| ≥ 1.96;
  - **index only, not significant:** the same, except |z| < 1.96;
  - **significant, small gap or low incidence:** |z| ≥ 1.96, but the index or share test fails.
- Also flag **low base (n = …)** when n < 100, **n unknown** when it is missing, and **modelled** where applicable.

Worked example: s = 30%, t = 20%, n = 150 gives index 150 and z = 10 ÷ √(20 × 80 ÷ 150) = +3.1, so the row is distinctive. Changing to s = 6%, t = 3% gives index 200 and z = +2.2, but the share is below 10%, so the row is "significant, small gap or low incidence": a niche, not a trait.

**Defining-trait candidates** are the distinctive rows ranked by absolute gap (s − t in pp), up to five. If none qualify, describe the segment as close to the population.

## Output

1. **Segment definition:** answer ID and wording, country, survey wave and fieldwork dates, segment share, n, and population represented.
2. **Defining traits:** 3–5 bullets with segment %, total % and index.
3. **Profile table** grouped by block, sorted within each block by distance of the index from 100:

   | Block | Attribute | Segment % | Total % | Index | z | Flags |
   |---|---|---|---|---|---|---|
4. **Portrait:** one paragraph.
5. **Implications**, including what not to target on.
6. **Gaps:** blocks the data could not cover, and why.
7. **Sources:** survey name, wave and link; question IDs.

## Quality bar

- High index on low incidence describes a niche, not the segment.
- With n ≈ 150, gaps under about 8 pp are noise. Say so.
- One country per profile. Compare countries on indices, not raw percentages.
