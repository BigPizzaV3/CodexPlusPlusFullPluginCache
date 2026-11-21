# Convocados: OpenAI directory submission package

This is a portable Agent Plugin bundle with an optional Codex compatibility manifest.

- `plugin.json` is the authoritative Agent Plugin manifest; listing metadata is under `extensions.com.openai.interface`.
- `mcp.json` points to the existing HTTPS MCP endpoint and configures mixed anonymous/OAuth access with DCR. No credentials are included.
- `.codex-plugin/plugin.json` and `.mcp.json` are optional compatibility entry points.
- `skills/convocados/SKILL.md` documents all 16 MCP tools and explicit approval before each mutation.
- `assets/logo.png` and `assets/icon.png` are real square PNGs included in the package.
- Five positive and three negative test cases, plus release notes, are embedded in the manifest.

## URLs

- Website (public): https://convocados.cabeda.dev/
- Privacy policy (public, confirmed through web retrieval): https://convocados.cabeda.dev/privacy
- Support (public GitHub issues): https://github.com/Cabeda/Convocados/issues
- Terms of service: https://convocados.cabeda.dev/terms **NOT VERIFIED/PUBLISHED** as of 2026-11-02. The manifest supplies the intended URL but final submission will fail until that route serves real terms. A site source file `terms.astro` is provided separately for publisher review and deployment.

## Remaining requirements outside ZIP

1. **Publish and verify the terms page** on the website at https://convocados.cabeda.dev/terms, or replace the manifest's `termsOfServiceURL` with the correct existing live HTTPS route.
2. **Record a reviewer-accessible demo video** showing main MCP use cases. Add its URL in `plugin.json` under `extensions.com.openai.review.demo_recording_url`, or in the dashboard when editable. Do not insert a fake example URL.
3. **Enter reviewer account details** and sign-in steps in the OpenAI dashboard secure review form, not in ZIP. Seed sample games to make positive review cases meaningful.
4. **Verify domain ownership**, connect OAuth and scan all 16 MCP tools in the dashboard. The ZIP has not been live-scanned by OpenAI.
5. **Set Ask before writes** in the host's permission settings. Skill instructions request confirmation but cannot independently enforce a client approval dialog.

## Tool test information

The positive reviewer tests assume the test account has at least one upcoming editable event with a player roster and a recorded past game. Write test checks explicit confirmation before an RSVP change. All other positive tests are reads. Tests are examples for reviewers and have not been executed against live credentials.

## License and image

The codebase reports FSL-1.1-ALv2 in its public repository. A newly generated icon is used in this package as a provisional visual; the publisher should replace it with the official Convocados mark if brand consistency requires it.
