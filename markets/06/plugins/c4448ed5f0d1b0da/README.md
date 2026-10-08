# Soulware by Honorary Human

**Version 0.3.0 · A voice of its own.**

Compare, use, and tune original Soul Kit personalities in ChatGPT or Codex. This release is prepared locally; it has not been uploaded to or published through the public directory.

## Try it

Ask:

> Use Soulware to compare Flint and Lantern on this: should I rebuild my whole website because one page is confusing?

The plugin bundles three complete kits:

- **Flint:** gives a recommendation early and names what could change it.
- **Lantern:** explains a difficult relationship through one concrete example.
- **Moss:** offers a measured opinion with occasional dry humor.

Use your own question or text for a comparison. Previews leave an existing selection intact; choose a voice to activate it. You can also attach a kit from the [gallery](https://honoraryhuman.com/gallery) or [builder](https://honoraryhuman.com/build):

> Use Soulware to apply this attached Soul Kit to this conversation.

## Adjust it as you work

| Ask | Result |
| --- | --- |
| “Less humor” or “more concise” | Adjusts the selected voice for this conversation. |
| “For this answer, be more formal” | Applies once, then returns to the conversation settings. |
| “Only use it for writing” | Applies the voice to prose artifacts, with ordinary surrounding conversation. |
| “Which Soulware voice is active?” | Reports the selection, version, effective scope, and temporary adjustments. |
| “Pause” / “resume the voice” | Suspends and restores the selection and adjustments. |
| “Reset my adjustments” | Restores the original kit and scope; a paused voice stays paused. |
| “Switch to Lantern” | Replaces the previous voice and clears its voice-specific adjustments. |
| “Stop using Soulware” | Clears the conversation selection without removing installed files. |
| “Save my adjusted Soul Kit” | Prepares a revised portable kit, without installing it or changing defaults. |

Conversation state depends on available context. A kit does not change ChatGPT account preferences or automatically carry into new chats. Reattach a saved kit to use it elsewhere. Facts, explicit user instructions, and requested formats always take precedence over personality guidance.

## What works where

| Environment | Intended behavior |
| --- | --- |
| ChatGPT with this Soulware skill and accessible attachments | Compare, apply, and tune voices in the current conversation. Create a revised file when file tools are available, or provide complete manually inspected JSON. |
| Execution environment with Python 3.10+ | Automatically validate kits and save versioned revisions. A temporary cloud file is a download, not an installation on the user's computer. |
| Local Codex with Python 3.10+ | Also export, install, update, inspect, and remove reusable voice skills. Default setup is optional and explicit. |

The bundled helper uses Python's standard library. There is no Soulware API key, sign-in, background service, or per-message network request. The host AI service processes the content you supply under its own policies.

## Save and install

The plugin translates requested lasting adjustments into the existing v1 format. Its `revise` helper validates and increments the kit version, preserves its ID/name and original file, and refuses to overwrite an output. It does not establish semantic compliance by itself: the consuming assistant must also review the changed guidance and examples.

For local Codex, ask:

> Install this Soul Kit for my Codex user, but only use it when I select it.

Or explicitly select a default:

> Install this Soul Kit and make it my default voice in Codex.

Existing user edits are preserved. A saved revision is not installed automatically. Installation scope (user/project) and voice scope (conversation/writing/both) are separate.

## Development and release

- `skills/soulware/`: self-contained instructions, collection, and runtime.
- `schemas/soul-kit.schema.json`: unchanged v1 exchange contract.
- `examples/`: canonical copies of all three bundled kits.
- `docs/bundled-kits.md`: kit versions, sources, and hashes.
- `docs/listing-fields.md`: prepared directory copy.
- `docs/verification.md`: executed checks and evidence limits.
- `docs/chatgpt-acceptance.md`: bounded host trial, pending installation and a live-test budget.
- `tests/`: isolated local regression and release-package checks.

Run `python3 -m unittest discover -s tests -v`. Package with `python3 scripts/package_plugin.py --manifest-format codex` for the directory upload, or omit the flag for the portable manifest variant. The packager verifies manifest parity, all bundled kits, and self-contained copies. Public release versions remain plain semantic versions. Prior release archives are retained.

The plugin is registered in the personal local marketplace. After updating the local installation, start a new Codex task to load its new instructions. A local update does not update the ChatGPT directory listing or prove behavior inside ChatGPT web.
