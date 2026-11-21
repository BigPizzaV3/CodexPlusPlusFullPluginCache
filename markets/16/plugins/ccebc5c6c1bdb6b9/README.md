# Pathweaver free Core review candidate

This supported Codex compatibility package includes the MCP connection in its
initial ZIP, alongside the adult planning skill, icons and review metadata.
It targets `https://mcp.pathweaverai.com/mcp`; never substitute the preview URL.
No registered app ID or `.app.json` is needed for this initial submission.

Build from the repository root:

```sh
python3 product/scripts/build_review_bundle.py --output /tmp/pathweaver-review.zip
```

The archive includes only explicitly allowlisted package files. The publisher
identity/category and legal URLs still need portal/public-site verification.
This is a review candidate, not a live or approved service. Uploading creates a draft. Do not submit for review until production, public
legal/support pages, all eight live cases and an accessible walkthrough
recording are verified. See `../submission/free-core-launch.md`.

Official references checked October 2, 2026:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/plugin-guidelines

The initial MCP must be included before publication; adding it later to a
skills-only plugin is unsupported. Changing the MCP URL later needs support.

## Parent starters

Paper/photo, PC activities, conversation/inquiry and hands-on projects are equal
options. The adult chooses involvement; no format or returned-photo loop is required.

- “Make a 15-minute quantities activity with a printable worksheet and separate
  key. Use Word or an image if available. After I return typed answers or a cropped
  photo, review what is observable and suggest a next step. Do not save a tracker.”
- “Make a short offline PC activity about improving a message; offer a drawing or
  discussion alternative and help us explain a revision.”
- “Offer a conversation that helps an eligible older learner compare two
  explanations and ask a better question, using an account they are permitted to
  operate under current host age/account/consent rules.”
- “Help us explore a question about paper designs: compare ideas, choose a safe
  test or supplied records, and discuss what we can and cannot conclude.”

These are capability-dependent host workflows, not promises of live Word/image
creation, OCR or automatic progress tracking. Keep work in the parent-managed host and send only generic curriculum queries
to Pathweaver. Pathweaver processes the tool queries sent by the host; input
checks do not anonymize free-text content. Content and files shared with the
host follow its own terms and privacy settings. Saving requires an explicit
parent-approved destination. Simple lookups need no onboarding.

Distinguish learning participation from account operation: no underage account
use or credential sharing. Pathweaver launch setup, permissions and records
remain adult-managed; eligible older learners need not relay every turn through a parent.

## Private beta

Use the separate `product/scripts/build_private_beta.py` builder and `BETA-GUIDE.md`
for preview testing. Never change this production package endpoint to preview.
The beta includes the same planning skill, a synthetic quantities fixture and
the offline artifact builder; installed-host lifecycle checks remain required.
