---
name: setup
description: Configure Remnant after plugin installation, including optional persistent per-task usage measurement for this user's Codex profile. Also use to disable that local rule. Installation alone is not consent.
---

# Set up Remnant usage measurement

Use this workflow when the user runs the plugin's setup. Do not run it as an unrelated task. Explain that the public plugin remains read-only and that measurement requires host counters; missing tokens, costs and savings remain null.

## First installation or update

Start with the bundled read-only `node <installed-skill>/register-policy.mjs status` check. It does not enable tracking or collection. For an update, keep the same plugin identity and existing connection; do not uninstall, reset settings, copy credentials, rewrite an already enabled rule or ask again for an unchanged accepted rule. State the observed local/central rule state, not inferred consent. If a managed block was edited or a check fails, preserve the file and report the exact blocker.

On an existing installation, use a short message: “Remnant has been updated. Your existing choices are preserved. You can optionally review private usage collection.” An absent central rule is disabled. Offer only a review of the new feature; declining changes nothing. Local tracking, central upload, human project consent, optional operator sharing and lesson contribution are separate choices. Never grant a missing choice during migration. Do not repeatedly promote a refused feature during ordinary tasks.

After installation/update, ask the user to start a fresh host session when required by the host. Do not promise automatic setup invocation, instant delivery to all installed clients or prove a refreshed session with an old tool catalogue. This local candidate is not yet publicly distributed.

Offer: **Use Remnant for each task and keep detailed local usage statistics**. Explain before acceptance:

- This adds a bounded rule to this user's active global Codex instructions and affects future tasks which load them, across projects. Project privacy restrictions and later opt-outs still apply.
- It tracks available quota/tokens, discovery versus actual use, quality, costs and blockers. It does not guarantee lower consumption, force irrelevant retrievals, or create comparison runs.
- The journal stays in this user's Codex home. This does not authorize uploading it, public contributions, account access, a scope upgrade or billing. Remnant requests still send sanitized arguments under the active policy.
- Disabling or uninstalling the plugin does not remove a global instruction file. Offer this setup's Disable action to remove only the managed rule. On a host without writable user instructions, report unsupported; do not claim persistence.

Read [the exact rule](usage-policy.md). Run the bundled helper in preview mode, substituting the real installed skill path; Node.js must already be available. Resolve the Codex home from the current user's environment, never a developer's absolute path. Do not install a runtime or change the MCP connection.

```text
node <installed-skill>/register-policy.mjs preview enable
```

Show the returned target and scope. Ask this user to accept once before writing; an explicit request to enable this exact rule already supplies acceptance. Installation, stored contribution consent and another user's request do not. After acceptance run `enable --accept-digest <previewDigest>` with the same helper. The digest binds the current file and proposed rule; if it changes, preview again and obtain approval of the changed scope. Never write the file by hand to bypass a refusal.

Read back with `preview enable`; report the actual result. Start a fresh Codex session to load the rule. Do not claim that all running chats received it or that a skill intercepts every final response. Use the normal Remnant skill and actual connection capabilities on future tasks. Only the separately authenticated Agent connection exposes private identity/impact; do not claim that the public plugin's seven tools gained write access or token accounting.

To disable, preview `disable`, then run `disable --accept-digest <previewDigest>` after the user's request/acceptance. The helper removes its own unchanged block only. A conflict, edited block, symlink or unsupported profile requires an explicit diagnostic; preserve all other instructions.

## Optional central collection — separate opt-in

After local setup, offer central statistics separately, without preselection. Explain that this sends structured per-task counters to Remnant, not just this device. Follow [measure-usage](../measure-usage/SKILL.md): a compatible authorized Agent connection, explicit measurement scopes and human project consent are all required. Aggregate sharing is another optional checkbox. Installation, acceptance of the local rule or lesson-contribution consent never enables upload. If collection is unavailable on this deployment, keep it disabled and report the blocker; do not promise a future automatic upload or alter the public connection.

For supported and enabled deployments, present [the exact separate central rule](central-usage-policy.md) and its scope before asking whether this user wants it applied to future tasks. Preview with `node <installed-skill>/register-policy.mjs preview enable --policy central`. After acceptance of that preview run `enable --accept-digest <previewDigest> --policy central`, then read back with the same preview. The same active-file, conflict, override and fresh-session rules apply. This does not grant project consent or create a connection. Keep only a local mapping from each user-approved project to its random pseudonym; absence of a mapping means no upload. Never record credentials there. Disabling central collection's instruction uses `preview disable --policy central` followed by the accepted disable action; retain the local-tracking rule. The user can independently revoke server consent and erase retained reports on their human page.
