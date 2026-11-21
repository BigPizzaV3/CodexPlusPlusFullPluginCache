# Rungstone for Codex

Version 0.1.8. Read-only toolkit for industrial controls engineers: understand, translate and verify PLC
code, carry the work through to HMI/SCADA, and find why equipment stopped from historian exports.

**Not for use on a production system without review and testing by a qualified engineer.**
Provided as is, without warranty (see LICENSE).

- It never connects to or writes to a controller; outputs are files for the vendor IDE.
- Safety-rated logic is detected and excluded, with a visible notice.
- Translations go through a review queue; export is blocked while high-risk items are open.
- Source-protected routines and blocks are never opened.

Codex sees your files: any file content or report Codex reads is processed by OpenAI under your plan.
Check your customer contracts, NDAs and export-control obligations first. The scripts themselves run
locally and make no network connections. Privacy: PRIVACY.md.

Full documentation: https://github.com/arunvenkatadri/rungstone
