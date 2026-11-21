---
name: review-traffic
description: Screen a batch of signups, logins, orders, reviews or log lines for anonymized traffic with VPNDetection, keeping each result next to the record it came from. Use when someone shares an export, a CSV, a table or a log file and asks which entries came from VPNs, proxies, Tor or hosting, or asks for help spotting fraud, abuse or account sharing by network.
---

# Review traffic with VPNDetection

1. Find the IP address in each record, and keep whatever identifies the record (user, email, order ID, timestamp) beside it. If a record has more than one address, use the client address, not a server or proxy hop, and say which column you used.
2. Look up every distinct address with a single `lookup_ips` call. A batch needs a key on a paid plan: on any other key, a list of more than 10 addresses comes back `bad_request` on every address, so say a review that size needs a paid plan and offer to check the 10 records the person cares about most. Read `coverage` first: a category the key's plan does not include was not checked, so never report those records as clean on that category.
3. Join the results back onto the records and sort them into what they are:
   - `is_resproxy`, `is_mobproxy`: residential or mobile proxy. The address looks like a home or phone connection but is resold, which is the strongest signal of the set.
   - `is_vpn`, `is_tor`: a VPN or a Tor node. Deliberate anonymization, common among ordinary privacy-minded users too.
   - `is_dcproxy`, `is_hosting`: a datacenter proxy or a hosting range. Usually automation, scripts or servers rather than a person at a device.
   - `is_pubproxy`: a public proxy, one anyone can use for free, so read it like a datacenter proxy. Where the result carries the `pubproxy` detail, a recent `last_usable` counts for more than the match alone, since most public proxies work only some of the time.
   - `is_relay`: a privacy relay such as iCloud Private Relay, or an enterprise web gateway such as Zscaler: ordinary people with a privacy setting on, or at work behind their company's gateway. Weigh it lightly.
   - `is_cdn`: a CDN range. Usually a service fetching on someone's behalf.

   Every result from a key also carries `location` (the country, its continent and timezone) and `asn` (the network: its number, name, type and announced prefix). Neither is a verdict, but both group the records: a country that doesn't match the account's, one network behind many accounts, or an `asn.type` of `hosting` where the key's plan doesn't include `is_hosting`.
4. Report a count per category, then a table of the flagged records with the identifying fields, the address, the category, the provider where known, and the country and network. Then call out patterns that only show up across records: one provider, one network or one address behind many accounts, bursts in time, or several accounts sharing an address.
5. Offer the full joined table as CSV if the person wants to act on it.

Keep the conclusions to what the data shows. A flag says the network is anonymized, not that the person is acting in bad faith, so present the evidence and let the person asking make the call unless they ask you to recommend one.
