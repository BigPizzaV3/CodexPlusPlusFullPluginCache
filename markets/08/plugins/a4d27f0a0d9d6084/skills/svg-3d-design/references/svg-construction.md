# Build the contours and surfaces, then their shading

Preserve the reference's appearance with a small set of editable surfaces. First establish what each visible part is and how it overlaps its neighbors; then choose contours and color fields that explain its form.

Build with economical paths, shapes, strokes, gradients and meaningful groups. Reuse geometry where the design repeats. Keep the result editable: do not embed the reference, simulate pixels with dense tiles or default to a dense full-image trace. Direct curves and selective contour fitting are both useful; fragmented shading usually needs a few designed surfaces and fields.

Carry the main light/dark and warm/cool relationships into the first construction. Preserve broad gradients and selective highlights when they define volume, material or atmosphere. Resolve each surface's contour and overlaps before fitting its interior shading. Simplify incidental texture and quiet regions before sacrificing focal character or distinctive variation.

## Put contour detail where it belongs

Separate long, quiet curves from local clusters of meaningful turns. Fit an arm, torso or product edge with a few broad curves and aligned tangents at smooth joins. Reserve tighter segments and intentional corners for knuckles, hair tufts, folds or other visible changes. Preserve genuine asymmetry and bends; smoothing should not inflate the silhouette or erase its character.

When fitting from pixels, anchor the intended boundary at extrema, inflections and junctions. Avoid following every edge fluctuation: grain, compression and antialiasing can turn a clean outline into ripples. Refine the responsible span rather than retracing the whole silhouette at a higher point density. Preserve its endpoints and the direction of the adjoining curves.

Distinguish a geometric kink from enlarged raster stair-steps by rendering the SVG afresh at higher resolution. Judge the repaired curve at intended size too. Repair the geometry; global blur softens otherwise crisp artwork without fixing a wrong contour or malformed grip.

## Read the surfaces

In the focal region, identify the physical parts, their visible contours and the important changes within each surface. One part may contain several differently lit faces, while similarly colored shapes may be separate overlapping parts.

For a small constructed prop, establish the body, visible thickness, inset panels or controls, and connection points in a shared local frame. Keep their axes, proportions and perspective consistent when positioning the group. Compare side-face widths, panel insets and control placement at a few landmarks, including what remains visible around a grip. Match this construction before adding highlights; shading cannot replace a missing rim or misplaced connector.

| Reference cue | Economical construction |
| --- | --- |
| Outer silhouette or cut edge | A clean closed contour. |
| One part overlapping another | Correct paint order, with a local shadow on the receiving part when visible. |
| Internal ridge, fold or crease | Two shaded faces sharing a curved boundary and a common outer silhouette. |
| Smooth rounded surface | A broad linear or elliptical gradient, with additional fields only where visibly needed. |
| Deliberate curved color region | A shaped region with its own fill; extra stops do not bend a linear gradient. |
| Incidental fine texture | Retain its collective effect when it defines material or style; otherwise simplify it. |

Anchor tips, joins, inflections and the route between them. Follow a suspected fold to its ends and identify the part on each side before splitting the surface; an overlap can resemble an internal crease. A ridge may curve off-center, fade near a tip or change contrast along its length. Preserve that behavior rather than replacing it with a dark outline.

## Establish a representative construction

Work through an important part before repeating its treatment. Include another instance when its orientation, overlap or material differs substantially.

For a folded surface, keep the outer contour and broad illumination. Use the shared ridge as the boundary of a second face, clipped to that contour, and introduce the observed difference between faces. Preserve the rounded shading and overlap shadows around it; uniform face colors can clarify a crease while flattening the object.

Start with the simplest field that reproduces the visible color progression. A long form can vary along its length and across its width, so a restrained second field may be useful. Keep real plane boundaries sharp and broad shading smooth. Taper a transition's contrast where it appears or disappears gradually.

Render the part in its final clipping and overlap context beside the same reference region. Compare the whole surface and a few useful cross-sections, including an exposed edge or tip. Check the ridge's route, transition positions and light/mid/dark values on each face. A correct crease alone does not establish convincing volume.

Inspect what remains visible after other shapes cover the field. A strong center-to-edge gradient can leave a nearly uniform exposed rim; a shared vertical field can clamp on a rising curved part. Fit the field's position and direction to the visible surface, not automatically to its bounding box. Keep a nearly constant reference region nearly constant. Reuse the construction principle while preserving differences in geometry.

## Finish lines and narrow fields

Follow veins, seams, ridges and highlights to both ends. Match how each joins, tapers, fades, reaches an edge or disappears beneath an overlap. Preserve intentional blunt stops. Where a line continues beneath another part, extend the hidden geometry far enough to prevent an accidental gap.

At exposed tips, taper width or contrast when the reference does. Inspect the tangent and junction as well as the endpoint. A narrow highlight or shadow can follow the correct curve but end in an unsupported luminous wedge or dark pit. Compare the ends at intended size and enlarged, then check that the repair preserves the middle and surrounding surface.

## Refine color within the correct structure

Use samples or fitting to diagnose a visible mismatch, respecting each surface's boundary and later occluders. Check both sides of important boundaries, including edges and tips; interior-only sampling can miss most of a narrow feature. A large quiet region should not outweigh a small defining highlight or join.

Bound fitted colors and inspect the entire visible field, including areas outside the sampled interior. Extreme gradient endpoints can create bands and pits. Lower pixel error does not justify a wrong contour, dissolved plane boundary or lost material cue.

Keep shadow ownership clear: identify the casting edge and receiving surface. A fitted fill may already contain the overlap shadow, so adding it again can create an artificial dark border. Confine softness to the relevant paint or shadow while preserving the outer contour.

After combining parts, recheck overlaps and newly exposed fields in the whole composition. Use the fidelity rubric to choose the next visible repair, then verify editability and the SVG/PNG size constraint on the final render.

## SVG export and editability checks

Choose delivery dimensions and pixel density from the intended use before construction. **The final uncompressed SVG must be no larger than the actual PNG rendered from it at those dimensions**, and must honor any smaller user limit. Use normal lossless PNG compression with matching background/transparency. Do not enlarge or inflate the PNG to pass.

Re-render after edits, then run `python scripts/check_svg_budget.py final.svg final.png --width WIDTH --height HEIGHT` with resolved absolute asset paths, or an equivalent check. The helper validates the PNG export but cannot establish that it depicts the current SVG.

When over budget, remove redundant geometry, merge incidental marks, reuse repeated shapes and simplify quieter regions. Retain visible contour nuance, broad shading and distinctive secondary forms when space allows. If fidelity and the ceiling conflict, report the conflict rather than silently degrading the design or claiming success.

Check the `viewBox`, unique IDs and resolved references. Inspect small and large renders, and composite cutouts on contrasting backgrounds to check transparency. Use [the alpha helper](../scripts/review_alpha.py) or an equivalent scan to investigate unintended gaps. A group move or recolor should keep its constituent shapes, shading and masks together. Report the SVG and PNG bytes and PNG dimensions; these practical checks remain separate from visual acceptance.

Resolve bundled paths relative to the skill's root directory. Command examples assume the skill directory is the working directory; both image-checking helpers require Pillow.
