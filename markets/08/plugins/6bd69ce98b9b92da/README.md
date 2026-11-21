# Spin The Wheel 0.3.5

Guest MCP endpoint: https://chatgpt.tryspinthewheel.app/mcp
Authentication: none.
Preview: https://chatgpt.tryspinthewheel.app/preview
Privacy: https://chatgpt.tryspinthewheel.app/privacy
Review walkthrough: https://chatgpt.tryspinthewheel.app/review/spinthewheel-0.3.0.mp4

Create a wheel in ChatGPT, then use Spin and Edit wheel. Wheel menu contains
manual winner removal, undo removal, reset and Open on website. Reset restores
the last applied edit. The editor handles 2–100 choices and integer weights
1–100, with twelve wheel palettes; custom choice colors are preserved.
A weight of 2 is twice as likely as a weight of 1.

Spins are selected by the Worker and the wheel displays that exact result.
Failed network spins retry with the same UUID; deliberate new spins use a fresh
UUID. Guest browser snapshots expire after seven days where storage is supported.
Clear local data removes the current snapshot. Hosts that block storage keep
edits only while the card is open. No account, cloud saving or synchronization.

Six built-in example wheels are available. This release does not search the
live catalog and does not certify prize draws. It adds no advertising or user
analytics. Tool data and infrastructure requests are processed as explained in
the privacy policy; ChatGPT has its own retention and privacy policies.

The package includes five positive and three negative review cases and release
notes in plugin.json. Its MCP server is hosted separately; this ZIP contains
manifests, skill and icon, not server credentials or the Worker source.

0.3.1 fixes phone editor clearance and adds sticky top Done/Cancel actions. The linked recording shows the preceding 0.3.0 desktop flows.

0.3.2 follows the ChatGPT host theme and standard host colors on load and live changes.

0.3.5 sets the author and developer name to the verified owner, Tarun Maheshwari, after the review could not confirm ownership of the brand. 0.3.4 sets all four tool annotation hints explicitly after the 2026-10-18 review rejection. 0.3.3 adds declared tool output schemas. Prepared locally; 0.3.2 remains the submitted deployment until an owner-directed update.
