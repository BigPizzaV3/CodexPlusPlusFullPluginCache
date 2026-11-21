---
name: check-ips
description: Check whether IP addresses belong to a VPN, a residential, datacenter, mobile or public proxy, a Tor node, a privacy relay or web gateway, a hosting provider or a CDN, using VPNDetection. Use when someone gives you one or more IP addresses, or text that contains them, and asks whether they are anonymized, risky, from a VPN or proxy, or who operates them.
---

# Check IP addresses with VPNDetection

1. Collect every IPv4 and IPv6 address in what you were given and drop duplicates. If there are none, ask for them.
2. For one address call `lookup_ip`. For more than one, call `lookup_ips` once with the whole list: it batches long lists itself, so never split it or loop over `lookup_ip`. A batch needs a key on a paid plan. On any other key, a list of up to 10 is still answered, one address at a time, and a longer one comes back `bad_request` on every address: say a list that long needs a paid plan, and offer to check the 10 the person cares about most.
3. Read `coverage` before you conclude anything. A field listed in `coverage.not_included` was not returned because of the plan behind the API key, which is not the same as "no". Say "not covered by this key's plan" for it, never "not a VPN". If the person needs those fields, `my_entitlement` shows the plan and field tier.
4. A private or reserved address comes back with `is_bogon: true`. Report it as an internal address, not as a clean one.
5. Report what came back:
   - One address: a one-line verdict, then each positive classification with its provider name when the result has one.
   - Several: a table of address, what it is (VPN, residential proxy, Tor and so on, or nothing found), provider, and notes, with flagged addresses first, then one line counting each category.
   - Quote raw JSON only when asked.
6. If `lookup_ips` returns an error in place of a result for an address, show it in that row and keep the rest. If a call is refused with `unauthorized`, the connection needs signing in again. If it is refused for going over the plan's allowance, check `my_entitlement` and say when it resets.

A positive answer describes the network the address belongs to, not the intent of the person using it. Leave judgement about what to do with a flagged user to the person asking, unless they ask for it; the `review-traffic` skill covers that case.
