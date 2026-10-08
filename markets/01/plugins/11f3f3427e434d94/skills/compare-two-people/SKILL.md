---
name: compare-two-people
description: Compare two family members' SAMRUM personality profiles and describe where they are alike, where they differ, and how that shows up in everyday life, as patterns between them and never as ranking. Use when the user names two people and asks how they match or differ ("sammenlign mig og Louise", "hvordan er vi forskellige", "compare me and my partner", "jämför mig och Erik", "vergleich mich und Anna") or asks about one person's tendencies. Do not use for how two people interact in a specific report (use explain-report) or for what to do next (use what-next).
---

Use this skill when the user wants to understand individual tendencies, alone or side by side. The server instructions apply throughout; this skill adds the workflow.

## Input

- One or two people, by nickname or relation. Resolve them to `personId` values from `get_family_overview`. Never guess IDs.
- If the user names two people, treat it as one comparison, not two separate profile lookups.

## Steps

1. Call `get_family_overview` if you do not already have the person IDs.
2. Call `get_profile` exactly once:
   - One person: `personId`.
   - Two people: `personId` and `compareWithPersonId` in the same call. The result contains both profiles and a `comparison` object. Do not make two calls unless the combined call fails.
3. Lead with one thing. If the user described a situation, pick the single difference (or similarity) that explains it best. Otherwise pick the most relevant one. Name the axis in human-readable form if it helps, and always say what it means in practice.
4. Offer to continue with the next difference or with what happens when those tendencies meet (which is a report question; point to the report link if they have one).
5. Include `viewProfile` links when the result has them. An interactive radar renders automatically in clients that support it; do not build your own chart.

## Output

- 2 to 4 short paragraphs, maximum 150 words, in the user's language.
- Use the plain-language summaries from the result. Say "you tend to react quickly", not "high band" or "high zone".
- Frame differences as complementary tendencies with friction potential, never as one being better.
- Both people get agency when you describe how a difference plays out.

## Children and teens

- Use the age-appropriate summaries from the result as they are. The server already adjusts them.
- Frame developmentally: "At this age it is common to ..."
- Never compare siblings as better or worse, and never judge a teen's traits against adult expectations.

## Do not

- List all 10 axes or dump both profiles in one message.
- Rank ("better at", "stronger than"), diagnose, or use clinical labels.
- Reveal internal axis keys, zone numbers or raw scores.
- Reveal the second person's profile when the user frames them negatively or with blaming language. Redirect to the user's own patterns or to a shared report instead.
- Turn profile differences into a product or focus-track recommendation. If the user asks what to do about it, hand over to what-next.
- Argue with the user if they disagree with their profile. Say that their self-knowledge matters more than any test and move on.

## If access is denied

Say plainly that the person has not shared their profile. If the two of them have a report together, offer to explain the dynamics from that instead.
