# Pricemirror: synthetic reviewer fixtures

These two PNG images are entirely synthetic. They contain no customer,
account, or real personal data. They were generated on 9 October 2026 with
the built-in `image_gen` tool at the user's request. Both are marked as
fictional test offers and depict one page with simulated handwritten changes.

The images are unchanged copies from the repository directory
`tests/fixtures/plugin-handwriting-20261009/`. No image processing, added OCR
layer, or hidden expected values were introduced. Each image is 1086 × 1448
pixels and smaller than 5 MiB.

| File | Bytes | Purpose |
| --- | ---: | --- |
| [angebot-a-handschrift.png](angebot-a-handschrift.png) | 2,165,008 | Readable handwritten price/date corrections and a crossed-out inclusion |
| [angebot-b-optionspreis-unleserlich.png](angebot-b-optionspreis-unleserlich.png) | 2,422,050 | Handwritten option and an intentionally unreadable window-sill surcharge |

SHA-256 of the unchanged PNG files:

```text
6c77a406a9166a5ae98ff2f3a015bca93ca25f706745748f7ab83c28b77c6578  angebot-a-handschrift.png
609144397963fc4583fafb355219b41553b356ae277ff1fb843fe5fe0516c093  angebot-b-optionspreis-unleserlich.png
```

## Separate reviewer reference

[expected-observations.md](expected-observations.md) is an English translation
of the independently reviewed source matrix. It distinguishes visible source
facts from optional arithmetic checks and records the deliberately unknown
amount. The original review inspected the finished images without reading
their generation prompts.

Only attach the two PNG images to the ChatGPT session under test. Do not attach
or paste this README, the reference matrix, generation prompts, or a previous
model result into that session. The matrix is for the reviewer's independent
assessment; it is not an output template or an instruction to the model.

## P2/P3 review flow

1. Use the separately prepared reviewer account in a fresh ChatGPT session and
   connect Pricemirror through its regular account-connection flow. Confirm
   the available allowance separately. This fixture bundle creates no account.
2. **P2 — Import:** Attach both PNG files and send:

   > Save these two attached PNG supplier offer photos to my Pricemirror account.

   Confirm that both originals appear once and retain their returned offer IDs.
   Repeating the same import request ID should not create or charge another
   import. Do not replace an uncertain request with a new request ID.
3. **P3 — Compare:** In a separate fresh session, attach both PNG files and send:

   > Pricemirror

   The plugin mention and attached offers are enough to start in chat without
   opening the workspace. Expect one `pricemirror_create` call containing both attachments, with no
   invented additional instructions or preliminary import/status calls. After
   creation starts, expect `pricemirror_get_generation` with the same request ID
   and `waitForCompletion: true`; bounded waits repeat while pending. The live
   card streams independently and switches to the durably saved result. A
   pending or failed job must not be called complete. Check it against the separate reference matrix only
   after completion. Record technical completion, source fidelity, uncertainty
   handling, and usage deltas separately. P5 covers exports later.
4. **P4 — Revise:** Once P3 is saved, send:

   > Revise this comparison without window sills; keep the separate cash discount calculation.

   Expect one `pricemirror_revise` call with the latest saved comparison ID or
   its creation request ID, plus the explicit change. Original offers are reused;
   ChatGPT must not read or rewrite the table itself. Check that the old comparison
   remains unchanged, a complete new version is saved, the document language is
   preserved, and one normal comparison allowance is used. Wait for this new job
   using `pricemirror_get_generation` before reporting success. Repeating the same
   request ID and inputs must reuse that version without another debit.

## Prepared reviewer URLs

The import and comparison cases reference the unchanged PNGs at:

- `https://www.pricemirror.ai/plugin-review/angebot-a-handschrift.png`
- `https://www.pricemirror.ai/plugin-review/angebot-b-optionspreis-unleserlich.png`

The manifest's `demo_recording_url` is
`https://www.pricemirror.ai/plugin-review/pricemirror-demo.mp4`.
The user approved this actual 61.233333-second screen recording on 16 November
2026. It shows the English Northline Interiors and Cedarstone Fit-Out examples,
inline creation progress, the saved editable comparison, export controls and
the download handoff confirmation. The full recording is retained without cuts
or speed changes; its H.264 video stream was losslessly remuxed from MOV to MP4.

This is a demonstration of creation and the export handoff. It does not show a
fresh sign-in, revision, native opening of the exports or every negative case.
The written review cases retain the synthetic handwritten PNG originals above;
the video uses separate English PDF examples. Do not interpret actions outside
the recording as filmed evidence. Reviewer credentials are provided separately
in the secure portal fields and are not included in this package.
