---
name: altodocs-start
description: Get started with AltoDocs in chat, connect an account, choose a project and the right saved file workflow. Use for setup or capability questions and onboarding; do not create sample files without a user request.
---

# Start using AltoDocs

Help the user work in chat and open a real saved result when useful. Respect
their chosen output. Prioritise standalone MathCanvas for calculation sheets,
documents for combined reports, markup for explanatory sketches, then CAD for
precision 2D drawings. Spreadsheets remain a distinct native file type.

Use the host's native AltoDocs connection flow if the account is not connected.
The user signs in and chooses project access there; do not request passwords,
API keys or tokens in chat. Existing account permissions and granted scopes
control tool availability. An installed skill does not unlock an unpublished
tool, broaden consent or bypass organisation editing access.

When the user wants to begin a concrete task, check the tools offered by the
host, then resolve an identified or unambiguous destination with `list_projects`.
Use the workspace skill for an explicitly requested new project. Do not create
a sample project/file simply because installation completed. Ask only questions
that matter for the requested outcome; sufficient supplied inputs are a reason
to proceed, not to demand another generic confirmation.

Route to the focused workflow:

- **Standalone MathCanvas:** native calculation file, inputs/formulas/units,
  saved evaluation, notes/layout, follow-up edits to the same live sheet.
- **Engineering reports:** document text, tables, embedded worksheets and
  supported beam analysis, with saved section links.
- **Markup sketches:** editable blank-background drawing blocks and saved
  previews; arbitrary image/PDF-background annotation is not exposed.
- **2D CAD:** native model geometry, annotation, blocks/layers and paper layouts.
- **Native spreadsheets:** saved values/formula source/styles/tabs; these tools
  do not recalculate spreadsheet formulas.
- **Projects and files:** discovery, project/folder creation, copies, moves,
  renaming, recoverable Trash and restore.
- **Unit-aware calculations:** evaluate supplied formulas without implying a save.

For attachments, use authorised host file-reading capabilities if present. If
the host cannot read a Word/PDF/image/spreadsheet attachment, ask for the relevant
excerpt/values. AltoDocs does not fetch or parse arbitrary attachments itself.
Keep provided facts, derived results and assumptions distinguishable.

If the host exposes only report tools, explain precisely that standalone
MathCanvas/project/CAD tools are not available in this connection yet. Do not
promise they will appear just by reconnecting; the host's published tool set can
also be the limit. Offer an available alternative only for the user to choose.

Complete work with a concise result and the real saved native URL, after the
appropriate read-back. Never describe a scratch calculation as a saved file.
Do not claim engineering certification, arbitrary code execution, external
imports, exports, email, sharing administration, or voice-mode support absent
the necessary authorised host/product capability.
