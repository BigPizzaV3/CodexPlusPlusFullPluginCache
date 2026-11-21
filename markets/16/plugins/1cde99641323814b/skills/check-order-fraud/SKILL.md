---
name: check-order-fraud
description: Check whether an order, payment, or signup fits the IP address it came from, using IPGeolocation.io location, network, and threat intelligence. Use when the user asks "is this order fraudulent", "the card is from Texas but the IP isn't", "should we ship this order", or gives a billing or shipping location together with an IP address.
---

# Check an order against its IP address

1. Run `get_ip_report` for the IP with the location, network, and security sections.
2. Compare the IP's country, region, and city with the billing and shipping locations the user gave. A different country is a mismatch. A nearby city in the same region is consistent, because an IP's location points to where its network sits. A different region in the same country counts only alongside other signals, since mobile and corporate networks often route through another state.
3. Weigh the security signals the report returned: Tor exit, VPN, proxy, residential proxy, relay, known attacker, bot, spam, and cloud provider, together with the threat score.
4. Give a clear recommendation and the reason for it:
   - **Approve** when the location fits and no risk signals were detected.
   - **Verify** with 3-D Secure, a phone call, or an ID check when the location doesn't fit or one anonymizer or moderate signal appears.
   - **Hold** when the IP is a Tor exit or a known attacker, or combines a high threat score with a location mismatch.
5. Ask for anything that would change the verdict, such as the customer's order history, instead of assuming it.

Never try to identify the buyer or their home. IP data describes networks, not people.
