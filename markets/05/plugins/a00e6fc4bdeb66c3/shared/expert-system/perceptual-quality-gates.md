# Perceptual quality gates

Technical and perceptual quality are separate gate dimensions. Both must pass when the output has a human-visible or experiential target.

Evaluate applicable observables such as composition, hierarchy, brand coherence, typography, rhythm, material credibility, lighting, motion, affordance, narrative emphasis, responsiveness, and perceived polish. Compare the real output with the approved target and last approved checkpoint, not with the implementer's intent. For a material perceptual gate, prefer an evaluator who did not build the candidate, receives fresh bounded context and inspects the real output directly.

Possible results: `PASS`, `PASS WITH RISKS`, `FAIL`, `NOT VERIFIABLE`.

Judge at the intended real user scale before macro inspection. Record applicable NORMAL, FAR, MID, NEAR, MOTION and MOBILE conditions; these are relevant views, not six mandatory tests for every element. Macro may explain a mechanism but cannot certify a target that fails at normal use size. If an effect is required only at a particular size/state, that scope must be approved before evaluation. Inspect real output in its actual medium (browser, Figma, Blender/render or equivalent); a still cannot prove motion, a render cannot prove browser behavior, and a terminal log cannot prove appearance. Missing required conditions remain NOT VERIFIABLE.

- Technical pass plus perceptual fail equals overall fail.
- Perceptual pass plus build, accessibility, security, or functional fail equals overall fail.
- Numeric compliance never overrides a visible failure.
- A reviewer records evidence, affected observable, materiality, rework owner, and re-review condition.

Correct compliance with a defective specification is not success.

When abstract rules are not sufficient for a visually important project, create the smallest useful owner-ratified calibration set: representative PASS examples and discriminating FAIL examples for the relevant composition, typography, material, interaction or brand failure. Keep it project-specific, versioned and separate from the candidate. Do not replace a small calibrated set with hundreds of generic design rules, and do not let the candidate silently rewrite the calibration authority.

For material-, form- or surface-critical work, an optional `REFERENCE_VISUAL_ORACLE` may be a controlled offline reference render or equivalent high-quality reference. It communicates intended art, material, silhouette, depth or form under stated conditions. It is not automatic pixel truth for the browser/runtime candidate. Record which observables it informs, its conditions and limitations, and combine it with real runtime inspection plus the applicable technical and perceptual review. Do not require an offline oracle for ordinary websites.

For premium, brand-led or otherwise differentiation-critical work, include an authorship/genericity gate at the applicable full-experience checkpoint and final visual review. Ask whether layout, hierarchy, navigation, component language, typography, imagery/representation, motion, interaction, copy presentation and storytelling could be reused almost unchanged for unrelated products after swapping logo, copy and colors.

Results are `DISTINCTIVE`, `ACCEPTABLE_BUT_NEEDS_REFINEMENT`, `GENERICITY_RISK` or `GENERIC_DESIGN_FAILURE`. A generic design failure blocks the perceptual pass. Do not treat more glow, cards, decoration or animation as a diagnosis; route evidence to experience thesis, product truth, composition, representation, typography, brand-specific relationships or content structure.

Generic glassmorphism, oversized headline templates, default SaaS/card layouts, arbitrary blur, dark-luxury presets, decorative gradients or random award-style motion do not establish authorship. Evaluate their structural purpose and product-specific relationships, not a blanket ban on an aesthetic. A technically sophisticated effect cannot compensate for a generic composition.
