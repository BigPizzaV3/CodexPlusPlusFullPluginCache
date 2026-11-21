---
name: report-abuse
description: Find where to report abuse coming from an IP address and draft the report, using IPGeolocation.io abuse contact data. Use when the user asks "who do I report this IP to", "find the abuse contact for 185.220.101.1", "this IP is attacking my server", or wants to file an abuse complaint.
---

# Report abuse from an IP address

1. Run `get_ip_report` for the IP with the abuse and network sections.
2. Give the abuse contact: the organization, its abuse emails and phone numbers, its postal address, and the network route the contact covers. If the report has no abuse contact, point the user to the regional registry named in the network section.
3. Offer to draft the report. Ask for the evidence: timestamps with their time zone, the targeted host or service, relevant log lines, and what happened. Keep the draft short and factual.
4. The plugin can't send email or file reports. The user sends the report from their own email.

Don't guess who is behind the address. Report the network, not a person.
