# Kiosk: an interactive page on a touch screen

Everything in `references/web-app.md` still applies (memory, never-reload, fit the viewport, never a
blank frame). What a touch screen on a signage player adds:

- **Touch only.** No hover, keyboard, right-click or system keyboard. Disable text selection and the
  long-press menu (`user-select: none`, `-webkit-touch-callout: none`).
- **Never leave the page:** no external links, no new windows, no browser bar.
- **Idle reset:** after 60–90 s with no touch, return to the attract screen and clear half-finished
  answers, with your own state, not `location.reload()`.
- **Offline-tolerant:** all screens ship inside the page; results to send wait in a queue and retry,
  never blocking the next visitor.
- **State:** per-visitor progress in memory (wiped on idle reset); per-device settings or a local tally
  in `localStorage` wrapped in try/catch. Shared results (sign-ups, answers across screens) depend on
  the host's web-page tool; see `references/host-tools.md`. No secrets or personal data in the page.
