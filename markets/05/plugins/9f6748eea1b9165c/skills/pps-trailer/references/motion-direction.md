# Custom motion direction

Use when an actual programmable video compositor is available. These are creative starting points, not API capabilities or rigid templates.

## Motion language

Choose one coherent family and a restrained accent: dimensional cinematic titles with light crossing beveled edges; bold editorial typography with masks and per-word rhythm; or graphic symbols with repeated geometric transformations. Relate surfaces and motion to the subject. Keep essential words in editable rendered type rather than asking a video model to spell them.

Design entrances, readable holds, and exits separately. A dramatic entrance is wasted if the phrase never settles. One to five words often works well for a teaser title; allow roughly 0.8–1.5 seconds of stable reading for a short phrase, longer for unfamiliar names. Verify rather than applying this mechanically. Reserve interface-safe margins for the chosen social destination and keep the title focal point away from faces.

Useful motion mechanisms include a word revealed by a moving object; a camera push through a title into footage; letters pulled together by the recurring motif; a footage shape match-cut into a letterform; or a large title transitioning to a precise date/CTA. These require compositor support. Choose two or three related mechanisms rather than a different trick for every cut. Use blur, glow, particles, and simulated depth to support hierarchy, keeping edges readable. Avoid rapid flashing and nonstop shake.

## Adaptable 15-second custom treatment

| Time | Story purpose | Picture and graphics | Sound direction |
| --- | --- | --- | --- |
| 0–1.2 | Immediate hook | Peak action or an arresting unresolved image; motif enters | Short impact, pulse starts |
| 1.2–3.0 | Establish the promise | First concise title emerges from the image and holds | Low tension, restrained voice if useful |
| 3.0–6.5 | Develop stakes | Two connected footage moments; a graphic echo bridges them | Rhythm and layers build |
| 6.5–8.5 | Pattern interruption | Brief reduction in movement/sound; second title reveals a turn | Breath or drop before the rise |
| 8.5–11.8 | Payoff | Strongest footage reveal, motif resolves, controlled acceleration | Musical crest |
| 11.8–15 | Name and invitation | Hero title, then readable date or CTA; intentional last image | Final hit and resolving tail |

This is NOT a valid `pps_plan_ad` template. Use it only with custom composition. For 30 or 60 seconds develop additional story turns and allow anticipation; do not stretch a 15-second montage with repetitive clips.

## Direction examples

Weak: “Epic cinematic trailer, incredible motion graphics, go all out.”

Stronger footage direction: “Foreground rain streaks past a stone arch. A lone adult messenger runs toward the opening as the dawn-lit valley appears behind them. A quick tracking move closes the distance, then a low-angle rise reveals the immense gathering beyond. A banner sweeps across frame near the second second; finish on the reveal with clear negative space overhead. No lettering.”

Stronger compositor direction: “Carry the banner's diagonal into a masked title reveal. Oversized condensed white type reads THE WAIT IS OVER; reveal three words on successive percussion accents, settle into a crisp hold, then push through the O into the dawn shot. Use warm amber light as the sole accent. Keep the title readable during the hold; place the final film name and invitation on a quieter composition.”

The compositor example describes intent, not a PPS schema. Translate it only into controls that exist in the chosen renderer.

## Hosted timeline and optional local source

For custom motion within the supported contract, use PPS's hosted `pps_plan_trailer` and `pps_render_trailer`. Read [hosted-timeline.md](hosted-timeline.md) for layers, keyframes and frame-based audio placement. The agent does not need a local renderer.

The download also includes `packages/remotion-kit`, with `TrailerComposition` and a conceptual interface fixture in `src/trailer/fixture.json`. An agent with a verified local renderer can render the same schema using `npx remotion render src/index.ts TrailerComposition out/trailer.mp4 --props=<your-json>`. Local props include the spec and an assets map of supported media URLs. The existing `AdComposition` remains the fixed ad grammar. Local source-code changes do not transfer through the hosted tools; a requirement beyond their timeline schema needs a separately verified external composition.
