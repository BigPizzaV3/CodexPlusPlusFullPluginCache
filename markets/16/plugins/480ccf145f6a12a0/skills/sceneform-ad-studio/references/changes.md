# Change a finished ad

## Headlines, sizes, and languages

New headlines, sizes, or languages for a finished image ad are one
`generate_ad_variants` call. It takes `requests`, a list with one request
per ad: the ad's `asset_ref` as `source_ref`, and `variants` set to one of:

- `{ kind: "headlines", count }`: new headlines on the same visual, one ad
  each. Use them to test copy while the picture stays fixed.
- `{ kind: "resize", aspect_ratios }`: the same ad recomposed for other
  placements (4:5 feed, 9:16 Stories, 1:1 square, 16:9 web).
- `{ kind: "localize", languages }`: the copy translated, with language
  codes such as `de`.

Each output is one image. Several ads at once are one `generate_ad_variants`
call with one request per ad. Video and motion graphics ads cannot be
varied this way: make a new ad, or Reshoot it.

## Ad Reshoot

To change who or what one of the user's video ads shows, call
`reshoot_video` with `mode: "ad_reshoot"`, the ad's `asset_ref` as
`source_video_ref`, and an `instruction`. It plans the edit as an ad,
removes the overlaid captions, and files the result in Ad Studio.

- Every reference goes in `reference_refs` (an image `asset_ref`,
  `persona_ref`, `product_ref`, or `element_ref`), and the instruction
  names them `@Image1`, `@Image2` in that order.
- Say who appears, what they wear or hold, the place, and the light. A new
  person gets positive traits ("a woman in her 40s with short grey hair and
  a denim jacket"), never only "someone different".
- The spoken words stay, and the result is as long as the clip.
- A Reshoot for another market keeps the structure and swaps the cast,
  setting, and product the market expects.

Leave `mode` out only for a clip that is not an ad (see sceneform-generate).
