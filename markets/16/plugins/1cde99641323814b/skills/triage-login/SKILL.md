---
name: triage-login
description: Triage a flagged login, signup, or account action by checking the source IP's threat intelligence with IPGeolocation.io. Use when the user asks "is this login suspicious", "did this signup come from a VPN or Tor", "should we block this IP", or shares an IP address from an authentication or access log.
---

# Triage a flagged login or signup

1. Run `check_ip_risk` for the IP. When the user wants to compare its location with the account's usual country, also run `get_ip_report` with the location and network sections.
2. Report what was detected: VPN, proxy, residential proxy, Tor, relay, bot, spam, known attacker, and cloud provider, with provider names, confidence scores, and last-seen dates where returned, plus the threat score.
3. Recommend the next step from that evidence:
   - **Allow** when nothing was detected.
   - **Step up** with MFA or an email confirmation for an anonymizer, a cloud provider, or a moderate threat score.
   - **Block or lock** when the IP is a known attacker, or has a high threat score together with other signals.
4. If the user gives the previous login's IP address and time, look up both locations and flag impossible travel when the distance between them couldn't be covered in the time between the two logins.
5. Ask about the account's usual locations and devices when the decision depends on them.
