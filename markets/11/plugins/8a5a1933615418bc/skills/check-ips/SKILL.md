---
name: check-ips
description: "Look up IP addresses with InternetData: where each one is, whose network it's on and who uses it, its abuse contact and reverse DNS name, whether it's a VPN, a residential, datacenter, mobile or public proxy, a Tor node, a privacy relay, a hosting provider or a CDN, and which services answer on it. Use when someone gives you one or more IP addresses, or text that contains them, and asks where they are, who owns or operates them, whether they're anonymized or risky, or where to report abuse from them."
---

# Look up IP addresses with InternetData

1. Collect every IPv4 and IPv6 address in what you were given and drop duplicates. If there are none, ask for them.
2. For one address call `lookup_ip`. For more than one, call `lookup_ips` once with the whole list: it batches long lists itself, so never split it or loop over `lookup_ip`. A batch needs a key on a paid plan. On any other key, a list of up to 10 is still answered, one address at a time, and a longer one comes back refused on every address: say a list that long needs a paid plan, and offer to look up the 10 the person cares about most.
3. Read `coverage` before you conclude anything. A field listed in `coverage.not_included` was not returned because of the plan behind the API key, which is not the same as "no". Say "not covered by this key's plan" for it, never "not a VPN". If the person needs those fields, `my_entitlement` shows the plan and what it has used. An answer with `cap_reached: true` is the exception: the plan covers those fields, but its organization's overage cap is reached, so say that, and that raising or removing the cap in Billing brings them back.
4. A private or reserved address comes back with `is_bogon: true`. Report it as an internal address, not as a clean one.
5. Report what came back:
   - One address: where it is, the network and the company behind it, then each positive classification with its provider name when the result has one, then the abuse contact if the person asked who to report to.
   - Several: a table of address, country, network or company, what it is (VPN, residential proxy, Tor, hosting and so on, or nothing found), provider, and notes, with flagged addresses first, then one line counting each category.
   - Quote raw JSON only when asked.
6. If `lookup_ips` returns an error in place of a result for an address, show it in that row and keep the rest. If a call is refused with `unauthorized`, the connection needs signing in again. If it is refused for going over the plan's allowance, check `my_entitlement` and say when it resets.

A positive answer describes the network the address belongs to, not the intent of the person using it. Leave judgement about what to do with a flagged user to the person asking, unless they ask for it; the `review-traffic` skill covers that case.
