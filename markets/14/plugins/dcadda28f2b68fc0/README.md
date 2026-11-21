# Lofi public review candidate 0.4.0

Use ChatGPT and Lofi to create private, editable wireframes and continue in the
same saved project. Connect or create a Lofi account with email or Google during
the connection flow. Native **Continue with ChatGPT** sign-in is a later phase
that requires an approved OpenAI client; this package does not enable it.

## Design and iterate

ChatGPT-authored creation and structural edits use Lofi's component catalog,
focused design guidance and evaluation before saving. New designs follow
`get_design_guidance` → `evaluate_iteration` → `create_wireframe_from_design`;
existing boards use evaluated `apply_canvas_update`. Copy-only changes can save
directly. These paths use **zero Lofi generation credits**, subject to account
project limits and rollout permissions.

Structural evaluations bind the exact proposal, intent, owner, selected source
screens and saved revision. Variants remain on the same board and preserve the
originals. Describe a variant's direction, benefit, tradeoff, preserved
requirements and observable changes. Estimated layout and structural similarity
findings are advisory; these checks do not inspect pixels or certify visual
quality, semantic correctness or accessibility.

Only an explicit choice to use Lofi's generation model calls
`generate_wireframe` or `generate_variation`. These consume existing Lofi
credits: **Default 1; Thinking 10**. The plugin has no checkout or subscription
creation. Any credit or subscription purchase happens on Lofi's website. A
ChatGPT subscription does not transfer Lofi credits or fund Lofi-model calls.

## Open and review your board

Browse owned projects and open an editable canvas beside the conversation.
The floating Lofi menu contains credits and access to all projects; project
refresh stays inside the picker. **Open in Lofi** opens the same private project
using its owning Lofi account.

**Send to ChatGPT** automatically prepares a preview of the whole saved board.
Review the preview and request, then explicitly send it into the current
conversation. There is no separate Prepare board or Choose screens step. The
handoff includes screen structure, flow, a private reference and an image when
available. **Having trouble?** exposes a manual text fallback; use Lofi for file
exports. Sending and reading a board uses no Lofi generation credits and does
not publish it. Temporary private preview references expire after 15 minutes
or replacement; anything sent into ChatGPT follows the host's retention rules.
Lofi records design activity without copying the full ChatGPT conversation.

The separate website **Continue in ChatGPT** entry is limited to eligible
accounts during rollout. It stores an owner-checked board reference for
15 minutes, offers **Add Lofi to ChatGPT** if needed, and requires the same Lofi
account. The website cannot reliably detect plugin installation. This flow does
not automatically send a conversation message or change board visibility.
Deep-link support and return after installation/sign-in depend on the host;
reopening the board link and copying its reference are recovery paths.

Dedicated research, automatic coding-agent delivery, editable Figma component
export and live Figma synchronization are not plugin capabilities. Open Lofi to
use its existing app tools or ask ChatGPT for a text implementation brief.

## Review preparation status

This is a **draft package**, updated October 28, 2026 after the UI/handoff source
merge. A package is not proof of production deployment, current authentication,
privacy compliance or review-case results. The stable production MCP endpoint is
configured separately in `mcp.json`; private app bindings and credentials are
excluded.

The current [3:07 review walkthrough](https://drive.google.com/file/d/1aCkENMookUp_RgzPxwZRqdYDfbEBZbdP/view?usp=drivesdk) shows the merged automatic whole-board preview, sample designs, a same-board alternative and read-only feedback. It uses chronological 1× clips with labeled wait cuts and two labeled actual-UI still inserts. The uploaded original matches the approved local file. Anyone-with-link Viewer access, signed-out start/end playback and sampled 1080p readability were verified in Chrome Guest. The automatic 12-screen preview and coding-agent brief are readable in inspected views; tiny overview labels are not individually legible. This was not a full linear playback review and does not establish saved-public-candidate case results. The earlier recording is preserved separately as historical evidence.

Exactly five positive and three negative cases are included in both manifests.
They still need results for the exact saved candidate and matching production
server. Secure reviewer credentials, publisher/domain verification, current
support/policy page checks, privacy/retention rollout, tool scans, iframe review
and owner attestations are external gates. None is completed by this ZIP.
Optional analytics follows the account preference; this document does not claim
that retention cleanup or a revised public privacy policy has been activated.

Publisher: **LOFISTUDIO, Inc.**, the approved business identity shown by the submission portal. Distribution: all countries
available in the submission portal. No public upload, submission or publication
is established by this package.
