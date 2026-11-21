# Writing a faceless storyboard (agent mode)

Use this when the user wants to decide every scene. The exact fields, limits and
the scene count for this length come from `get_creation_guide('faceless')` under
`modes.agent`. `check_plan` and `validate_plan` enforce the same rules.

## The plan

- `title` in the video's language.
- `look`: one mood, era and palette true for every scene, in English. It prefixes
  every image prompt. A place and a palette, never a plot or people.
- `scenes`: each with `text` (spoken verbatim, never rewritten) and `imagePrompt`
  (English, one complete frame). Optional per scene: `motionPrompt`, `focus`,
  `shotType`, `movementType`, `transitionType`, `beat`, `characterIds`, `people`.
- Optional: `recurringPeople`, `soundEffects`, `textOverlays`, `voice`.

## Image prompts that work

- Show what is said. A line about a person puts a person in frame, described by
  role and look. A line not about people shows no one.
- Never use names in prompts: the image model does not know them. Describe the
  person ("a gray-bearded fisherman in a yellow raincoat").
- No style words (cinematic, 4k, watercolor, epic…). The visual style is applied
  to every image, and those words are removed.
- One subject, one action, one setting per frame. Say the framing: close-up,
  wide, from above.
- Light lives on the surfaces: say how it falls on the subject (warm side light,
  pale overcast, late sun on wet stone). Don't show lamps, spotlight cones,
  beams or studio equipment, unless the scene really has the source (a candle,
  a fire, a screen).
- Every scene gets its own frame. At least 70 % of the prompts must differ, and
  no two scenes repeat the same line.

## People who come back

A person seen in two or more scenes goes in `recurringPeople` once: gender, age,
hair, build, outfit and one distinctive item, never a name. List their `key` in
`people` on each scene where they appear, and call them by a short anchor in
those prompts ("the old fisherman"). Never describe their looks again.

Saved characters work the same way through `characterIds`: describe them by
their look, never their name. Leave some scenes without them for variety.

## Pacing the scenes

- Scene 1 is the hook: the strongest image and the first line, with a hook
  text overlay if it helps.
- Vary the shots (wide, medium, close) and the camera moves. Default cuts are
  fine; use other transitions only where the story turns.
- Sound effects: at most two per scene, on real moments (a door, a crash, a
  reveal). Keep transition sounds rare. No ticking clock unless the user asks.
- The last scene lands the payoff or loops to the first.
