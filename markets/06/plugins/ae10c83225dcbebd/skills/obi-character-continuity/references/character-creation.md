# Character creation contract

## Profile

Summarize the biblical role, historical setting, selected life stage, approximate age, physical appearance, clothing, occupation, historical reasoning, and known uncertainties. Distinguish biblical facts from historical reconstruction.

## Reusable identity

Define face, hair, complexion, body, clothing, footwear, accessories, emotional presence, and the enduring traits that must remain stable. If a reference image is supplied, preserve its recognizable identity unless the user requests a change. Distinguish identity-controlling references from clothing, pose, expression, and style references.

## JSON

Return valid JSON containing identity, appearance, clothing, props, setting, personality, visual style, continuity rules, reference mapping, negative constraints, Scripture references, historical sources, and uncertainties.

## Images

Default aspect ratio is 1:1. When generation is explicitly requested, create one character sheet containing useful angles and expressions. A requested full character package contains:

1. profile portrait
2. full-body reference
3. action shot
4. multi-angle character sheet

Keep the same identity, age, facial structure, body proportions, and core clothing. Save the exact prompt after each generation. If drift is visible, explain it and propose a targeted retry rather than claiming consistency.

Offer life-stage variants when biblically useful, preserving the underlying identity while changing age and historically appropriate appearance.
