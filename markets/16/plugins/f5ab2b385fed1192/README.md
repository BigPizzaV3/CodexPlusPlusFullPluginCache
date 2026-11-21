# Scribe Animator Director 2.0.0 — cloud draft

Portable skills-only authoring package. Start at [SKILL.md](skills/scribe-animator-director/SKILL.md). Native editability is the goal; fresh desktop install/WebMCP acceptance and directory submission remain separate uncompleted phases.

Offline: Node 22.13+ or 24, `node skills/scribe-animator-director/scripts/self-test.mjs` and `node skills/scribe-animator-director/scripts/validate.mjs <animation.json>`. No checkout, dependency installation, network or account is needed.

This draft includes the production fixes from PR206 at `8a51c34a0f03492719de1193aa6c04fd93a42a23`. Review and merge PR206 before PR205; neither has been merged into main. The bundled validator delegates to the same canonical/import-compatible owner as the live app, and authored text DTO conversion preserves explicit font overrides. Regenerated archives supersede the earlier PR205 ZIPs; old bundles do not contain these repairs. Client installation, live capability discovery and desktop acceptance still require separate verification.

For local installation, extract this plugin folder and create a local marketplace root with `.agents/plugins/marketplace.json` containing:

```json
{"name":"scribe-director-local","interface":{"displayName":"Scribe Director Local"},"plugins":[{"name":"scribe-animator-director","source":{"source":"local","path":"./scribe-animator-director"},"policy":{"installation":"AVAILABLE","authentication":"ON_INSTALL"},"category":"Productivity"}]}
```

Place this folder at `scribe-animator-director` relative to that marketplace root. The official guide uses `codex plugin marketplace add <local-marketplace-root>` to register it; restart the latest ChatGPT desktop app, choose the local source in Plugins Directory, then install and test in a fresh chat. These are instructions for the later local phase, not a claim that installation was performed here. Recheck the current marketplace schema/client workflow if it rejects this catalog. See [prerequisites](skills/scribe-animator-director/references/clients-and-recovery.md) and [acceptance](skills/scribe-animator-director/references/local-acceptance.md).

Maintainers: from the repository, `npm ci --prefix scripts/director-package --ignore-scripts`, `npm run director:generate`, `npm run director:check`, `npm run test:director-package`, `npm run director:pack`. Build-only dependencies are locked in scripts/director-package/package-lock.json. The ZIP includes a marketplace root and this plugin folder; the separate submission ZIP has plugin.json at its root. Neither is uploaded or published by the build.
