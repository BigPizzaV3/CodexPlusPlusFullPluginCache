# Sound intent planning

## Contents

1. Evidence boundary
2. Sound jobs
3. Planning workflow
4. Density and silence
5. Hook, Body, proof, and CTA patterns
6. Handoff requirements

## Evidence boundary

Platform evidence supports sound-on creative, not indiscriminate SFX density. TikTok's Creative Codes describes music, narration, and sound effects as separate creative tools and says SFX can add surprise; Meta reports better Reels outcomes for a bundle of 9:16 video, audio, and safe-zone compliance. Neither establishes that “more SFX” alone improves conversion.

Audiovisual research supports two planning principles:

- temporally synchronous sound can facilitate processing of the visual event it matches;
- semantically congruent sound can improve memory for audiovisual scenes.

HIKAKIN is useful as an editing reference, not performance-ad proof. In an official interview he connects satisfying sound effects with action speed and framing, and a Japanese content analysis describes frequent short and long SFX as a way to add modulation to otherwise static talk. Transfer the function—rhythm, emphasis, causal clarity—not the entertainer's raw density.

Sources:

- [TikTok Creative Codes](https://ads.tiktok.com/business/en/creative-codes)
- [Meta Reels ads guidance](https://www.facebook.com/business/ads/facebook-instagram-reels-ads)
- [HIKAKIN interview on speed and sound](https://en.dragon-ball-official.com/news/01_888.html)
- [Audio-visual synchrony and visual processing](https://pubmed.ncbi.nlm.nih.gov/28802870/)
- [Semantic congruency and audiovisual memory](https://pubmed.ncbi.nlm.nih.gov/26620810/)
- [HIKAKIN content analysis](https://rikkyo.repo.nii.ac.jp/record/22711/files/AA12607699_10_06.pdf)

Keep claims calibrated: a sound design is a response hypothesis until a controlled campaign or retention analysis measures it.

## Sound jobs

Assign one primary job to every planned sound:

| Role | Job | Typical examples |
| --- | --- | --- |
| `causal` | Make a visible physical event feel real and correctly timed | impact, rupture, landing, object contact |
| `informational` | Confirm a work or UI event | notification, comment arrival, calendar tick, button confirmation |
| `structural` | Mark a meaningful section change | hard-cut accent, short transition, reveal onset |
| `rhythmic` | Make repeated information readable as a pattern | month sequence, checklist, report-page cadence |
| `emotional` | Change felt state without adding a factual claim | tension sting, relief lift, brief low pulse |
| `brand` | Create a reusable sonic signature | short end-card motif |
| `ambience` | Keep a place or surface believable | office room tone, device bed |
| intentional silence | Create contrast and protect meaning | breath before Aha, audio vacuum before impact |

Reject a cue when its only rationale is “the edit felt empty.” Empty space may be intentional.

## Planning workflow

1. Read the approved Beat sheet, Hook handoff, Animatic, and expression profile.
2. Mark every visible causal event and work-native information event.
3. Mark semantic changes that may need structural or emotional support.
4. Mark narration spans and important Japanese consonant-heavy phrases.
5. Decide the first sound and the role it plays. It may be speech, not an SFX.
6. Select a density profile independent from visual intensity.
7. Create repeated motifs before selecting individual assets.
8. Insert negative-space windows before major reveals when contrast improves comprehension.
9. Write `sound-intent-map.json`; do not select library filenames in planning.
10. Test the Animatic sound-on and muted. Sound may strengthen meaning but may not carry the only copy of the claim.

## Density and silence

Use role coverage before cue counts. Default limits are guardrails, not performance claims.

- `restrained`: work-native micro-cues, at most one editorial accent per Beat, one or two simultaneous layers, and a clear silence or room-tone floor.
- `balanced`: micro-cues plus one bounded high-energy transition or proof burst; at most two layers under narration and three without it.
- `entertainment_high`: a named experiment or entertainment format; allow dense clusters only with an explicit purpose, speech-masking plan, and separate control creative.

Do not create a cue for every word, text animation, zoom, or cut. Group related actions into a motif or cluster. A three-item repetition may use one sound family with subtle pitch or tail changes. A major break may use an attack/body/material layer group at one causal frame.

Keep at least one of these contrast devices when the timeline is continuously active:

- 150–400 ms of SFX negative space before an Aha or impact;
- a room-tone-only inner-thought Beat;
- a short tail reset before the CTA sonic tag.

## Hook, Body, proof, and CTA patterns

### Hook

- Synchronize notifications and UI changes to the exact visible onset.
- For repeated explanations, reuse one motif; increase pace only after the first item is understood.
- Let speech be the first sound when the spoken contradiction is stronger than an alert.

### Bridge and reveal

- Use silence or a low bed to create contrast before a major reveal.
- For a physical impact, plan attack, body, and material/tail as one layer group rather than three unrelated events.

### Proof

- Accent the first readable proof anchor.
- Use a bounded rhythm cluster for quantity, not one loud whoosh per page.
- Settle before the payoff so the main sentence remains intelligible.

### CTA

- Use one short repeatable brand motif after the CTA begins, not before the service name is understandable.
- Keep the motif consistent across Hook variants unless sound is the declared test variable.

## Handoff requirements

`sound-intent-map.json` must contain:

- platform, expression profile, fps, and final duration;
- narration windows copied from the approved timeline, so asset tails—not only trigger frames—can be checked for speech overlap;
- first-sound strategy and mute-legibility lock;
- density limits and any declared high-density clusters;
- cue intent, viewer job, trigger frame, sound family, narration-overlap rule, and maximum offset;
- motif reuse rules and intentional silence windows;
- asset-rights policy;
- evidence-calibrated checks.

The production handoff should include the map path and SHA-256. Production may select assets and mix treatments but must return a blocker before changing a required cue, silence window, or emotional function.
