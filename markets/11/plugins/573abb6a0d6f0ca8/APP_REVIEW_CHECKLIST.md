# OpenAI public-review checklist — checked 2026-10-02

Current official references: [submission guide](https://developers.openai.com/plugins/deploy/submission), [submission error reference](https://developers.openai.com/plugins/deploy/submission-errors), [plugin format](https://developers.openai.com/plugins/build/plugins), [MCP server guide](https://developers.openai.com/plugins/build/mcp-server). Recheck at actual submission time.

- [x] Production HTTPS origin chosen: `https://signalaf.com/api/plugins/sigrank/mcp`, isolated from the existing `/api/mcp` submission service.
- [x] Public V1 uses five no-auth tools; four reads and consent-gated beta email. No OAuth reviewer account needed.
- [x] Listing includes display name, description, category, icons and live website/support/privacy/terms URLs.
- [x] User choices: all available countries (`publication.countries: []`); no in-plugin purchases (`review.commerce: false`).
- [x] Root manifest includes exactly five positive and three negative draft review cases plus release notes.
- [x] PR #175 five-tool deployment and PR #177 homepage/eligibility repair were verified live with board and field smoke checks.
- [ ] Retest v0.1.22 in fresh ChatGPT and Codex chats: live board first, natural adaptation to statistical versus casual questions, and evidence-led discovery across scale, Yield, operating ratio, and compatible field context. Use held-out boards where different relationships deserve attention; confirm the plugin neither preselects a favored operator nor infers account type from names or metrics. Keep material scope notes brief. Capture exact tool calls and answers. Owner-provided v0.1.8 and v0.1.13 reviews are in `HOST_TEST_REVIEW.md` and `HOST_TEST_REVIEW_0.1.13.md`. The 20-fixture analyst scoring and manual pasted-count guidance are additional internal checks, not OpenAI publication requirements.
- [ ] Record and verify a reviewer-accessible video of the actual installed plugin, then add its real `review.demo_recording_url`. Do not invent one.
- [ ] Confirm the intended verified publisher identity; match `developerName` to it.
- [ ] Complete domain verification challenge, current portal tool scan, developer identity and legal/policy attestations in the submission portal.
- [ ] Inspect the saved draft after upload; submitting for review and publishing after approval are separate actions.

Annotation justifications: `get_leaderboard`, `get_operator`, `compare_operators`, `get_field_stats` are read-only because they fetch published data; open-world because they query live SignalAF; non-destructive because they do not alter records. `report_beta_bug` is not read-only or idempotent because it sends an email, is open-world because it delivers externally, and is non-destructive because it neither deletes nor overwrites records. The beta skill must show a redacted draft and obtain explicit approval before the tool call. Portal review may require these explanations even if the manifest stores only boolean annotations.

The ZIP has no credentials or unverified demo URL. A valid ZIP does not itself prove host behavior or public approval.
