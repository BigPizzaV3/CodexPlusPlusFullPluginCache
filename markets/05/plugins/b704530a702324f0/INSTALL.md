# Mavixx Forge 1.1

Mavixx Forge sets up new software projects and upgrades existing websites and applications through implementation, rendered UI review, and release checks. Version 1.1 fixes the earlier behavior that could stop after an audit, plan, or `DESIGN.md` file without applying the upgrade to the product.

## Install directly in Codex

1. Open the Mavixx Forge plugin card from its shared Codex link.
2. Select **Install**.
3. Confirm that the plugin is enabled.
4. Start a new Codex chat so its bundled skills are loaded.

No terminal command is required. The ZIP package is only a source/backup artifact and is not the native installation method.

## Use on a new project

Open the new project folder in Codex, select Mavixx Forge, and say:

> Use $mavixx-forge. This is a new project. Set it up and build it end to end. Infer reversible implementation details, ask only about real blockers, implement the requested product, and verify it before handoff.

Mavixx Forge uses `$mavixx-project-bootstrap` for preflight and `$mavixx-design-system` for user-facing work. Preflight is the first phase of delivery, not the final result, unless you explicitly request planning only.

## Use on an existing project

Open the existing repository—not only its live URL—in Codex and say:

> Use $mavixx-forge. Upgrade this existing website end to end. Preserve working behavior, data, routes, and user changes; improve the UI and UX in the actual source code; run the site; inspect desktop and mobile states; fix in-scope issues; and complete the relevant checks. Do not stop at an audit or plan unless blocked.

The repository must be available in the active workspace. A live URL can be audited visually, but Mavixx Forge cannot change the website without its editable source. The upgrade workflow establishes a baseline, preserves project invariants, implements changes in reviewable phases, and invokes `$mavixx-quality-gates` after material work.

## Other direct commands

- Existing-project upgrade: `Use $mavixx-project-upgrade to implement and verify this upgrade; do not stop after the audit.`
- Design and UI implementation: `Use $mavixx-design-system to define and apply a coherent visual system to this interface.`
- Final verification: `Use $mavixx-quality-gates to verify, fix in-scope failures, and recheck this project before release.`

Third-party design skills are not silently installed. Mavixx Forge recommends them only when suitable and requests approval before installation.
