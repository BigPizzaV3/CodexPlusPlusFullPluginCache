Wandeo contains code derived from Recordly / OOVideo.

Recordly: Copyright (C) 2026 webadderall; derived from OpenScreen by Siddharth Vaddem (2025). AGPLv3; see LICENSE.md.

Renderer, motion, caption and directing modules were adapted from oovideo-desktop. HyperFrames and ShotCraft references retain their Apache-2.0 notices below. Runtime dependency licenses are included by their publishers and downloaded with those dependencies.

Three.js 0.180.0 and its GLTFLoader are bundled in `dist/spatial-runtime.mjs` under the MIT License. The license text is included at `third_party/three-LICENSE` in the generated plugin payload.

Anatomy explanatory geometry kit

The source distribution includes the complete pinned anatomy tree. Runtime packages retain geometry, turning, audit, WebGL, Canvas, editable examples, authoring references, capture/audit scripts and the React kit. Upstream tests, repository administration files and generated example outputs are excluded, except for the turning-dial HTML consumed by the renderer:
https://github.com/wheresryan22/anatomy
Commit: 1482e8469b0a9e0d8cc18ea2740a01423d29ae80
Copyright (c) 2026 Ryan
Licensed under the MIT License. The source license and per-file SHA-256 manifest are included at `third_party/anatomy/LICENSE`, `third_party/anatomy/NOTICE` and `third_party/anatomy/SOURCE.json`. Runtime manifests enumerate the shipped subset and retain the original commit and source-manifest hash. Wandeo's adapter invokes the upstream `turning`, `T.*`, `TURN.mount`, `glLayer`, audit and verification APIs through a deterministic `renderAt(time)` surface.

The complete-object verification fixtures in `scripts/authored-fixtures.mjs` reuse the pinned Anatomy dial-indicator and desk-computer geometry and styles with attribution. Wandeo supplies a deterministic teaching model and shot composition; the upstream source files remain unchanged.

Video ShotCraft curated reference library

This product includes a curated subset of video-shotcraft:
https://github.com/Vincentwei1021/video-shotcraft
Commit: c30d78438ef2e8c9cb2b620f19fecff13d982bd3
Copyright 2026 Wei Yihao
Licensed under the Apache License, Version 2.0. See LICENSE.

OOVideo packages text references and reference TypeScript source for local Agent
research. It does not package the Remotion runtime, fixed Ink Press template,
gallery preview media, product textures, third-party audio, or JianYing export.
