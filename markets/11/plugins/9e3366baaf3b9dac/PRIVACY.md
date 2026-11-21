# Sidequest public plugin privacy

Updated November 4, 2026. Provider: David Lederer. Contact: Dav.lederer@gmail.com.

## Information used

The hosted connector receives requests to open puzzles and, when validating a completed solve, its puzzle ID and move history (slides, hints, resets and undo events). Validation happens in memory; Sidequest does not save these results on the connector or submit them to a leaderboard.

The connector's tools do not request or read conversation text, source code, local files, credentials or accounts. Do not include private information in game requests or support messages. Your host application controls what it sends when invoking a tool and has its own privacy policy.

The embedded game and host may retain puzzle progress, selected difficulty, size and minimized state in browser storage or host-managed widget state. Retention and removal depend on the host; resetting a puzzle is not a promise to erase all host records.

## Optional usage counts

When the game appears in ChatGPT or Codex, Sidequest counts game openings and successfully validated solves. To estimate distinct browsers, it creates a random identifier in that browser and sends it with those game-only events. The connector converts the identifier to aggregate counting registers and does not save the identifier, IP address, account details, conversation text or move history for analytics. Counts and aggregate registers are retained without a scheduled deletion date. The distinct-browser figure is an estimate, not a count of individual people or installs.

Usage counting is on by default. Turn it off in the game's **Settings** at any time; this stops future usage events and removes the browser identifier stored by Sidequest in that browser. Counts already aggregated cannot be removed for one browser because the server does not retain its identifier. Browser storage may be unavailable in some hosts; those openings can be counted without contributing to the distinct-browser estimate.

## Hosting and external links

Cloudflare hosts this connector and may process IP addresses, request timing and other technical information under its own policies. Application-level request-body logging and Worker observability are disabled in this deployment; this does not eliminate provider security or infrastructure logs.

Shared challenge links open the separate public Sidequest website. They contain puzzle identifiers and may include game-result information; do not include private chat links. The website's optional leaderboard and its hosting are described in the [website privacy notice](https://sidequest.davidlederer7.chatgpt.site/privacy.html).

This plugin has no advertising, sponsored content, payment processing or Sidequest login. Support email is optional and is processed through the email provider. Send only the information needed to explain a problem; never send passwords, tokens or private work.

## Questions and removal

Contact Dav.lederer@gmail.com about privacy or support. You can uninstall the plugin, remove its connection and clear relevant host/browser state using that application's controls. Sidequest cannot delete records controlled by your host or infrastructure provider.
