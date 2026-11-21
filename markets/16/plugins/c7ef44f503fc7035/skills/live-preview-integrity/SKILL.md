---
name: live-preview-integrity
description: Plan honest live-site previews and public website data with consent, provenance, timestamps, freshness labels, and secure fetch boundaries.
---

# Live Preview Integrity

Use whenever a 3D portfolio, device display, product scene, or dashboard shows another website or reports external site data.

## Process

1. Use only URLs from user-supplied records, actual site links, or other verified public data. Do not guess domains or imply work, ownership, endorsement, or a client relationship that is not evidenced.
2. Distinguish three preview modes in both implementation and copy:
   - Interactive embed: an iframe that works only when the target site's CSP frame-ancestors and X-Frame-Options permit it.
   - Screenshot capture: a dated image of a real capture. It is not an interactive website or a real-time texture.
   - Fallback: clearly identify a stale/unavailable capture and offer the verified direct link; if none exists, show factual project details and the direct link.
3. Never bypass embedding restrictions, authentication, paywalls, rate limits, or robots rules by proxying or mirroring protected page content. Do not claim a failed capture proves a global outage.
4. For each capture, preserve source URL, requested/final URL, viewport, capture time, capture service/provider, freshness state, and success/error state. If time or provider is unknown, say so. Never invent “live,” “real-time,” “checked now,” uptime, performance, analytics, or freshness claims.
5. Define the metric precisely. Response-header latency is not browser load time or Core Web Vitals; a single checker vantage point is not worldwide uptime. Use sourced, timestamped measurements and state the method.
6. Any server-side URL fetch must be limited to authorized public hosts and defend against SSRF: allowlist expected domains where possible; reject loopback, private, link-local, reserved, and cloud-metadata IP ranges; revalidate DNS and every redirect; restrict schemes, ports, response sizes, content types, timeouts, and redirect counts. Never fetch credentials or arbitrary internal URLs.
7. Respect provider cost and usage limits with caching, deduplication, bounded concurrency, timeouts, and backoff. Continuous checks need a real scheduled worker/job; browser timers are not background monitoring.
8. Load interactive embeds only after a visitor asks to open them when that avoids unnecessary third-party requests or page cost.

## Output

Specify preview mode, provenance fields, refresh/fallback behavior, metric definitions, restrictions, and user-visible labels. If tooling or permission is missing, provide the design/implementation prompt and clearly mark preview fetching as unimplemented.

