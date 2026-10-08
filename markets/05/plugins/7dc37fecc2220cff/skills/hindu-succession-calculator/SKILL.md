---
name: hindu-succession-calculator
description: Conduct a dynamic legal-fact interview and calculate exact inheritance shares under the Hindu Succession Act, 1956 for Hindu intestate succession, including male and female intestates, Class I and Class II heirs, represented branches of predeceased children, agnates and cognates, Section 6 coparcenary screening, statutory disqualifications, simultaneous deaths, children in the womb, multiple properties, monetary values, and the Kerala Section 15(2)(c) amendment. Use when a user asks who inherits, requests a Hindu succession or legal-heir calculation, wants inheritance fractions or percentages, or needs a step-by-step succession assessment. Distinguish final, conditional, and legal-review-required results.
---

# Hindu Succession Calculator

## Objective

Interview the user for only the facts that can change the result. Calculate each property separately with exact fractions. Explain the legal route, inclusions, exclusions, assumptions, and uncertainties in plain language.

Treat the result as a non-binding legal assessment. Do not claim to replace an advocate, adjudicate disputed facts, validate documents, or determine title.

## Load the references

Read [references/question-flow.md](references/question-flow.md) before interviewing the user.

Read [references/conversation-ui.md](references/conversation-ui.md) before interviewing the user. It defines the story-first option, card-style questions, progress model, estimate ranges, fact ledger, and finish line.

Read [references/statutory-rules.md](references/statutory-rules.md) before classifying heirs or calculating a share. It contains the operative central rules, Schedule entries, Kerala amendment, and review triggers.

Read [references/output-format.md](references/output-format.md) before presenting a result.

## Control the conversation

1. If the user has not supplied substantial facts, offer `Tell me everything in one message` and `Guide me one step at a time`. Skip the choice when the opening message can already be parsed.
2. Use the semantic Markdown card pattern in `conversation-ui.md` for every question turn. Show the current stage and an honest remaining-answer range.
3. Never show a fixed completion percentage. Recalculate the range after triage and explain whenever a new legal branch materially increases it.
4. Ask no more than three short questions per turn. Prefer one question when the answer controls the next branch.
5. Explain an unfamiliar legal term in one sentence, offer ordinary-language choices, and add one short `Why this matters` line.
6. Always offer `Not sure` when a fact may be unavailable. Accept free text even when numbered choices are shown.
7. Maintain a fact ledger. Separate confirmed facts, user assumptions, disputed facts, and unknown facts. Show it at meaningful checkpoints, not after every answer.
8. Give early value through a supported route preview. Do not show provisional fractions unless the alternatives are finite and explicitly conditional.
9. Do not ask about remote relatives until a prior statutory class or entry has been ruled out.
10. Do not ask for names when relationship labels are sufficient. Accept aliases such as `wife`, `son 1`, or `predeceased daughter`.
11. Ask the user to confirm the normalized family and property summary before the first calculation when the case contains more than one property, a represented branch, successive deaths, or coparcenary property.

## Apply the gates in order

### 1. Applicability gate

Establish:

- date and State/Union Territory of death;
- whether the deceased was governed by the Hindu Succession Act under section 2;
- Scheduled Tribe status and any applicable Central notification;
- whether section 5 or another special succession regime may exclude the property;
- whether a valid will or other testamentary disposition covers any property.

Route property covered by a will to `LEGAL_REVIEW_REQUIRED` unless the user asks only for a hypothetical intestate comparison. Section 30 does not itself provide a will-distribution calculator.

### 2. Property gate

Create one record per asset or legally distinct share. Establish:

- description and location;
- the deceased's ownership fraction;
- movable, immovable, or business interest;
- separate/self-acquired, inherited, jointly owned, or Mitakshara coparcenary character;
- for a female intestate, the exact source of inherited property;
- value, only if monetary results are wanted;
- relevant partitions, decrees, registered deeds, alienations, gifts, releases, settlements, or earlier deaths.

Never assume the deceased owned 100% or that all assets follow the same route.

### 3. Succession gate

For a male intestate, apply sections 8 to 13 and the Schedule.

For a female intestate, apply sections 15 and 16 property by property, including source-based exceptions under section 15(2). Apply Kerala section 15(2)(c) when the death and property are governed by that amendment.

For a Mitakshara coparcenary interest, first determine the deceased's section 6 interest, then distribute only that interest through the appropriate testamentary or intestate route. Do not treat the entire coparcenary asset as the deceased's estate.

### 4. Eligibility gate

Check only when relevant:

- survival at the opening of succession;
- represented branches of predeceased children;
- child conceived before death and later born alive under section 20;
- uncertain order of death under section 21;
- murder/abetment under section 25;
- post-conversion descendants under section 26;
- effect of disqualification under section 27;
- full blood, half blood, and uterine blood under sections 3 and 18 and the Schedule.

Do not disqualify a person for disease, defect, deformity, remarriage, or another ground not currently provided by the Act.

## Build statutory units before doing arithmetic

Do not divide by the number of displayed people. Build the statutory unit tree described in [references/statutory-rules.md](references/statutory-rules.md).

Use [scripts/fraction_engine.py](scripts/fraction_engine.py) to divide the estate interest through the unit tree and verify conservation. The script accepts a JSON file or standard input. Example:

```json
{
  "estate_share": "1",
  "whole_asset_value": "120000000",
  "units": [
    {"id": "widow", "beneficiary_id": "W", "label": "Widow"},
    {"id": "son", "beneficiary_id": "S", "label": "Son"},
    {"id": "daughter", "beneficiary_id": "D", "label": "Daughter"}
  ]
}
```

Run:

```bash
python3 scripts/fraction_engine.py --input case.json
```

For a group or represented branch, replace `beneficiary_id` with `children`. Every node divides its allocated share equally among its immediate children. Model widow groups and represented branches explicitly; do not flatten them.

Set `estate_share` to the deceased's fraction of the whole asset. Set optional `whole_asset_value` to the value of the entire asset, not merely the deceased's interest.

Treat the script as an arithmetic and conservation engine, not a legal classifier. Verify that the unit tree matches the statute before accepting its output.

## Decide the result status

Use exactly one status:

- `CALCULATED`: essential facts are confirmed and no review trigger applies.
- `CALCULATED_WITH_WARNINGS`: shares are calculable, but a nonessential uncertainty remains.
- `CONDITIONAL`: show alternative results keyed to one or more stated factual assumptions.
- `INCOMPLETE`: essential facts are missing; ask the next decisive question instead of inventing a share.
- `CONFLICTING_FACTS`: supplied facts cannot all be true.
- `LEGAL_REVIEW_REQUIRED`: a disputed title, will, adoption, marriage validity, state/historical rule, Section 6 issue, document construction, or other issue cannot safely be resolved from the available statutory text.

Never label a result `final` unless its status is `CALCULATED` or `CALCULATED_WITH_WARNINGS`.

## Calculate and validate

1. Preserve fractions as rational numbers through every step.
2. Calculate percentage and money only from the final exact fraction.
3. Confirm that beneficiary shares sum exactly to the estate interest distributed.
4. Confirm that every represented branch sums to its parent branch share.
5. Keep successive deaths as separate succession openings with separate dates, legal regimes, and calculations.
6. Show a compact calculation trace: property interest, statutory route, units, branch divisions, and consolidated shares.
7. If conservation fails, stop and report `CALCULATION_ERROR`; do not display plausible-looking shares.

## Cite and qualify

Cite the exact section, rule, and Schedule entry used. Link the official India Code PDF recorded in the statutory reference. State the governing date and jurisdiction. Identify any rule that needs current case-law or state-law verification.

End every calculated or conditional answer with this concise qualification:

> This is a statutory share calculation based on the facts stated, not a title opinion or substitute for advice on disputed facts, documents, state amendments, or later case law.
