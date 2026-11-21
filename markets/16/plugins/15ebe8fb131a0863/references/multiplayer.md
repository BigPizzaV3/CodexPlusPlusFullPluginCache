# Network gameplay standards

Choose the networking model: local multiplayer, asynchronous turn-based, peer-to-peer, or server-authoritative real-time. Do not start cloud services without permission.

- Authenticate any account-specific actions; do not assume trust in client-provided stats, inventories, payments or permissions.
- Design rooms, join/leave, reconnect, timeouts, version mismatches, input prediction/reconciliation only when required.
- Use bounded message sizes, rate limits, anti-cheat/abuse controls and privacy disclosures.
- Test local loopback before external infrastructure, then two-client sessions, packet loss, latency and reconnect where tools exist.
- Missing real networking or server access means prototype/network design only; not verified multiplayer.
