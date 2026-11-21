---
name: get-started
description: Show a new user what IPGeolocation.io can answer in ChatGPT and help them run a first lookup.
---

# Get started with IPGeolocation.io

Help the user see what the plugin does by answering one real question, not by describing features at length.

1. Ask what they want to check, or suggest one of these:
   - "An order billed to Texas came from 185.220.101.1. Do the IP's location, network, and risk signals fit?"
   - "Who operates 1.1.1.1? Show its ASN, the company behind the address, and whether it's anycast."
   - "Show me a Python example that checks whether an IP is a VPN with the IP Security API."
2. Run the lookup with the plugin's tools and explain the result: what the returned data shows, which signals matter for their question, and a sensible next step.
3. Mention account connection only if the user asks about accounts, or if their next question needs data their current access doesn't cover. Account connection is optional and happens through ChatGPT's own Connect option.

Use the values the tools return. Don't fill missing fields with guesses, and don't identify the person behind an IP address.
