# Flowers and leaf-like stitch flow / 花・葉脈風の縫い

## Confirm the intended appearance / 制作前の確認

After generating or inspecting the source, propose concrete image-specific treatments with a short reason, rather than opening with “Anything you want to change?”. Offer 2–3 meaningful alternatives and an all-auto option; develop the proposal through brief questions. Reuse decisions already made. Do not assume all flowers need a vein pattern. Read the proposal workflow in SKILL.md.

- **Appearance / 表現:** ordinary fill, or two-sided leaf-vein-like flow? Distinguish a visible sewn central vein from a central boundary formed only by contrasting stitch angles.
- **Source / 元画像:** keep the supplied artwork and use a supported region split, or regenerate/redesign a source with independently identifiable halves? Confirm source redesign before generating. Preserve petal count, silhouette and center unless changes are requested.
- **Flow / 流れ:** branches extending toward the tip from the central seam, or the opposite, toward the base? For flowers, anchor every seam at the central disk and extend it toward its own petal tip. Ask in visual terms, not only in degree numbers.
- **Method / 縫い方:** when undecided, explain broad fill versus long-and-short as appearance choices. Apply an explicit user choice to the requested regions only.

Example: 「この花は中央で左右を分けると、葉脈風の流れが出せます。①中心から先端へ流す（おすすめ） ②逆向きに流す ③すべてお任せ。左右を編集できる色分け画像を作る案をおすすめします。」 Adapt choices to the actual image and omit answered parts.

## Prepare independently editable halves / 分割用図案

1. Identify each petal’s base, tip and longitudinal centerline from the image. Bisect each petal along its own radial axis, never with one global horizontal/vertical cut.
2. For five two-sided petals, preserve ten independently editable regions. This is an example, not a universal petal count.
3. When a new image is authorized, request opaque flat fills with distinct adjacent colors, smooth boundaries, no gradients/noise and no accidental stripes. Inspect the generated image; prompt compliance is not guaranteed.
4. Keep identifying colors through segmentation and contour extraction. Change **thread colors after region creation**, so two adjacent halves can share blue thread without losing their IDs. Do not reduce to the final thread count if that merges required halves.
5. Map IDs to observed coordinates/bounds and visual positions. Exclude background and confirmed artifacts, preserve intentional detail. Treat IDs and cleanup thresholds as project-specific.

## Plan and verify direction / 角度を決めて拡大確認

- Record a pair of angles per petal relative to its own centerline. Do not copy one left/right pair across differently oriented petals.
- Verify the app’s angle convention using the actual generated stitches: mathematical coordinates and screen coordinates may have opposite vertical signs. A valid numeric setting is not proof of the desired flow.
- **A 180° numeric rotation does not reverse a parallel fill’s visible axis**: angles are equivalent modulo 180°. To reverse the vein-like appearance, mirror the two sides’ slopes about the local centerline (or exchange the two half settings when appropriate), then regenerate. Distinguish this from reversing sewing order/start–end, which requires a supported routing control.
- Zoom in on **every** petal, especially diagonals and the lower-right petal. Trace from the central disk along the seam to the tip, then from the seam outward into each half; verify that branches point in the agreed direction. Check seam gaps, center crowding, missing fill and travel lines separately.
- If one pair is reversed, repair that pair only. Never declare all petals correct after inspecting just the top petal or a whole-design thumbnail. Save/show an enlarged preview before claiming success.
- Preserve per-half colors and angles when switching Tatami to the app’s advertised long-and-short mode. Reinspect generated needle points/stitch lengths; a stored fillType or changed stitch count alone does not prove a long-and-short texture. Do not equate an app’s Brick label with every traditional long-and-short technique.
- Keep green leaves/stems separate from petal decisions. A petal vein request does not authorize adding veins or splitting the green leaves automatically.
- After repair or method changes, regenerate and export new files from the current design; older JEF/PES and project saves are stale. Verify actual files and keep the editable final project where supported.


## Five-petal angle reference / 上から時計回りの5枚花びら

Use this starting reference for the tested Jiminy angle convention: one petal vertically upward from a central disk and four surrounding petals, each bisected longitudinally. Number petals **clockwise from the top**. These are the final visually corrected settings from the blue-flower case, not universal constants. Identify halves by screen position, never old region IDs.

| Petal / 花びら | Half A / 半分A | Angle A | Half B / 半分B | Angle B |
|---|---|---:|---|---:|
| 1 Top / 上 | Screen-left / 画面左 | 135° | Screen-right / 画面右 | 45° |
| 2 Upper-right / 右上 | Above central seam / 中央線の上側 | 67° | Below central seam / 中央線の下側 | 157° |
| 3 Lower-right / 右下 | Above central seam / 中央線の上側 | 0° | Below central seam / 中央線の下側 | 90° |
| 4 Lower-left / 左下 | Upper-left side of seam / 中央線の左上側 | 0° (180° equivalent) | Lower-right side of seam / 中央線の右下側 | 90° |
| 5 Upper-left / 左上 | Above central seam / 中央線の上側 | 113° | Below central seam / 中央線の下側 | 23° |

Anchor the five seams at the yellow disk and trace them to each tip. Match the desired tipward branching, including the lower-right pair that was previously reversed. The generated source was approximately radial, not an exact regular pentagon: adapt angles to the actual seam slopes, petal rotation and shape. If the whole design rotates or the renderer changes, recalibrate using visible stitches instead of blindly reusing numbers.

**Mandatory enlarged inspection:** enlarge until individual stitch segments and the seam are clearly distinguishable; inspect all five pairs, seam joins and outer edges. Adjust affected angles, regenerate, and inspect again. Carry the corrected per-half angles into long-and-short only when the current app supports them; inspect the actual stitch texture too. A thumbnail or this reference table alone never establishes completion.
