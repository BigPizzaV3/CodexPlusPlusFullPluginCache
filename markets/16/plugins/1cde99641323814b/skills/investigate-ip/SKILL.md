---
name: investigate-ip
description: Profile one IP address with IPGeolocation.io, covering where it is, which network and company operate it, its threat intelligence, and its abuse contact. Use when the user asks "where is this IP from", "who owns 8.8.8.8", "is this IP safe", or pastes an IPv4 or IPv6 address from a log.
---

# Investigate an IP address

Answer the user's question first, then show the evidence behind it.

1. If this conversation already has a report for the address, answer from it. Otherwise run `get_ip_report` once, requesting the sections the question needs, and ask for location, network, security, and abuse when the user wants the full picture.
2. Lead with the answer, then the supporting facts: city, region, and country; ASN, company, and connection type; whether the address is anycast; the threat score and every detected security signal, with provider names and last-seen dates where returned; and the abuse contact if the user wants to report misuse.
3. For an anycast address, say that the location describes the network that announces it, not the server that handled a given request.
4. For a list of addresses, check the ones the user cares about most, one lookup each. Bulk lookups aren't available in ChatGPT.

Use only the values the tools return, and say when a field wasn't returned.
