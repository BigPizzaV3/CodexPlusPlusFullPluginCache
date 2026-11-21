# Representative fixtures

All examples are self-contained JSON with fictional copy and no external assets. They demonstrate offline import acceptance and canonical authoring; visual/browser QA is NOT_RUN. They are not proof the distributed skill autonomously reproduced historical films.

| Valid example | Coverage |
|---|---|
| [scene](valid/scene.json) | Editable text/shape/path, slot/roles, track/keys, Draw Step, camera rotation and explicit hide/hold. |
| [project](valid/project.json) | Two ordered scenes, scene-local timing, total duration and procedural content. |
| [block](valid/block.json) | Reusable editable label/underline and insertion anchor. |
| [relationships](valid/relationships.json) | Anchor source and Clip source IDs, self-contained SVG; runtime target eligibility still needs visual acceptance. |
| [procedural](valid/procedural.json) | Parameter/motion scalar data recipe, digest/seed/material, playback and Drawing Score. Initial maximum rise establishes a nondegenerate reference pose; the motion is remapped into its bounded range. |

Every file under `invalid/` must fail default canonical validation: schema-version, missing-owner, negative-timing, camera-time, anchor-conflict, missing-clip, procedural-digest, procedural-code, procedural-parameter, procedural-derived, score-reference, runtime-properties, timing-semantics, unsupported-video and missing-child-props. Some intentionally pass structural schema or import-compatible parsing but fail canonical lint; this demonstrates why schema alone is insufficient. The shipped self-test records all 20 outcomes.

Maintainer tests evaluate the ribbon with the actual production runtime, Drawing Score/material compiler and renderer reference transform at opening/quarter/three-quarter phases, sampled extrema and min/default/max rise. Centerlines fit the authored host box; compiled ink bounds fit the scene. These geometry checks do not establish fresh installation, pixels, playback tempo or end-to-end browser acceptance.

Change a copy, not this fixture. For procedural recipe edits, calculate a fresh canonical recipe revision with recipe-revision.mjs and validate the complete envelope. App apply revalidates retained workspace budgets.
