# Listing screenshots

These seven files are **previews taken from the local harness**, not from
ChatGPT. They are built from the real content libraries and the real screens,
with the fictional Amaltas Skincare answer set. Replace every one of them with a
capture from ChatGPT developer mode once the planner server is deployed.

Rebuild them with:

```bash
cd web
node reference/build-fixtures.mjs
node build.mjs
node reference/shots.mjs
```

| File | Screen | What it shows |
|---|---|---|
| `01-intake-questions.png` | Intake | The question set open, the first section, a why line under each question and the "don't know" option |
| `02-profile.png` | Intake | The confirmed profile: the stated, assumed and open counts, and a basis chip on every fact |
| `03-data-map.png` | Radial map | The whole map, all four rings, the counts strip, the assumed boxes marked, the legend and the headline finding |
| `04-legal-note.png` | Note | The first counsel questions, each with the evidence to bring, what the answer changes and its citations |
| `05-gaps-and-plan.png` | Gaps and plan | The counts strip and the Legal group of the register, each gap with its priority, owner, proof and counsel questions |
| `06-buying-guide.png` | Buying guide | Two categories, each with what it leaves out, the questions to ask, and seller rows with a source link, a capture date and the MBS partner line |
| `07-pack.png` | Pack | The saved pack: the cover with the stated and assumed counts, the contents, the profile and the embedded data map |

Shot details: light theme, device scale factor 2, screen content only, no
harness header and no mock badge.

## What the OpenAI docs ask for, read on 1 October 2026

- Screenshots are optional and no count is set.
- Supported formats: PNG, JPEG, WebP and SVG, at most 5 MiB each. Every file
  here is PNG and under 1 MiB.
- No dimensions and no aspect ratio are stated for screenshots. The square rule
  of at least 48 by 48 pixels applies to icons and logos.
- Assets belong under `./assets/` in the package.

## One known deviation

Row 5 of `listing/listing-for-approval.md` section 7 asks for the three gap
groups and the four week plan in one shot. The Amaltas answer set produces 25
gaps, so that whole screen is about 8,800 pixels tall and nothing in it stays
readable at listing size. `05-gaps-and-plan.png` carries the counts strip and
the Legal group instead. The full screen, including the four weeks, is in
`web/proof/real-gaps-plan-plan-amaltas.png`.
