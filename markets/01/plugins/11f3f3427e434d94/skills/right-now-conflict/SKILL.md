---
name: right-now-conflict
description: Help when the user has just had an argument or a tense moment at home and asks what to do right now. Use for present-tense frustration about a fresh disagreement with a partner, child, teen or sibling ("vi har lige skændtes", "hun smækkede med døren", "we just had a fight", "vi bråkade precis", "wir haben gerade gestritten"). The whole answer is a short acknowledgment plus the link to SAMRUM's moment guide ("Lige nu" / "Right now" / "Just nu" / "Gerade jetzt"), nothing else. Do not use for disagreements that happened a while ago or for questions about a recurring pattern (use explain-report).
---

Use this skill when the disagreement is fresh. The user needs one concrete next step, not analysis. The server instructions apply throughout; this skill adds the mandatory flow.

## Decide timing first

- Just happened or still going on (present tense, "lige", "just", "precis", "gerade", fresh frustration): follow the flow below.
- Happened a while ago, or the user wants to understand why it keeps happening: do not use this skill. Offer to look at their report data instead and hand over to explain-report.

## Flow (strict, three parts)

1. Acknowledge in one sentence. "Det lyder frustrerende." / "That sounds frustrating." Nothing more.
2. Point to the moment guide with its link. Say what it is in one sentence: a short, self-guided page in the SAMRUM app built for the moment right after an argument, about 90 seconds, with one concrete thing to do now. Use the localized product name from the tool data (`momentGuide.name`).
   - Take the link from `links.momentGuide` in a `get_family_overview` result you already have in this conversation. Otherwise call `get_samrum_info` and use the moment guide link from there. Do not call `get_family_overview` just to fetch the link.
3. Optionally offer, in one sentence, to look at what their data says about the pattern once things have settled.

Total response: 3 to 4 sentences, in the user's language.

## Do not

- Fetch or explain report or profile data while the disagreement is fresh.
- Give tips, strategies, "try this right now" advice, or exact sentences to say. The moment guide handles the moment; you do not.
- Ask clarifying questions about what happened. The user does not need to explain themselves to get the link.
- Speculate about what the other person felt or meant.
- Assign blame or take sides.

## After the guide

If the user comes back later and wants to understand the pattern, switch to explain-report (or compare-two-people if they ask about the two of them rather than a report). Do not restart this flow.
