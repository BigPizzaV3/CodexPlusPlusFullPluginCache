# Offline validation workflow

Node 22 or 24, package files only; no npm install, app account, network or repository is needed. Paths resolve relative to the shipped scripts, not the current directory.

```
node <installed-skill>/scripts/validate.mjs animation.json
node <installed-skill>/scripts/validate.mjs --import-compatible legacy-input.json
node <installed-skill>/scripts/recipe-revision.mjs recipe.json
node <installed-skill>/scripts/self-test.mjs
```

Exit 0 means the requested offline mode passes; exit 1 means validation fails; exit 2 means usage/file-read failure. JSON output reports validationMode, runtimeOk, schemaOk, authoringOk, canonicalOk, errors/schemaErrors/authoringErrors and warnings. Default canonical mode checks the entire generated DTO shape and authoring lint after the production bounded import parser. Group children in the opaque props bag are checked against the generated ObjectDTO before lint reads them; malformed children return actionable JSON-pointer diagnostics and exit 1. Opaque path entries are also guarded before DrawStep target identities are read. Import-compatible mode preserves the production normalized-import decision; it may accept raw/legacy envelopes, timing the app adjusts, or nested children the importer currently permits. `ok:true` in that mode can coexist with `canonicalOk:false` and additional authoring findings. The explicit warning makes that difference visible; it never implies canonical validity. Read the separate results rather than treating them as equivalent.

The bundle and live app use one production verdict owner. After live discovery, `template.validate_json` capability version 2 accepts `json` and `mode`; request `mode: "canonical"` for new authoring. Its omitted mode defaults to import-compatible, while this offline CLI defaults to canonical. With an older live contract, use offline canonical validation and follow the discovered schema instead of sending unsupported fields. An offline PASS does not replace live apply checks.

Bundled production checks include JSON node/depth/size/forbidden-key budgets, SVG geometry budgets, supported object types, object/track/key/draw/camera/path references, slot/assets diagnostics, track eligibility and procedural host/asset/recipe/score/palette input safety. Canonical lint adds nonnegative/scene-bounded intervals, sorting, duplicate identities and direct relationship references. Unsupported lanes remain **warnings** in production; canonical Anchor x/y conflicts are also lint errors. Repair every material warning before relying on motion.

Opaque props and unsupported/ignored DTO fields are documented in [contract scope](contract-scope.md). The parser currently normalizes timing semantics and some metadata; canonical mode checks the original input so normalization cannot disguise an authored version mismatch. It does not fetch assets, execute SVG, render every frame, prove all relationship eligibility/cycles or certify local persistence/export. Live importer/app semantic checks and permissions remain authoritative. Retained procedural workspace budgets are checked only at apply.

[Self-contained fixtures](../examples/README.md) cover project/scene/block, camera rotation, hide/hold, connectors, slots, tracks/keys/draw and procedural recipes. Negative fixtures include structurally valid semantic failures. `integrity.json` at plugin root records packaged resource SHA-256s; maintainer generation and isolated tests check deterministic drift. Do not edit generated validator/schema bytes by hand.
