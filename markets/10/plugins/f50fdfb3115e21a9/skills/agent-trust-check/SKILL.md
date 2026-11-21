---
name: agent-trust-check
description: Check an AI agent's BlindOracle trust badge and settlement history before the user transacts with it, and report what the record does and does not show.
---

Use this skill when the user wants to know whether an AI agent, bot or wallet is safe to work with, hire or pay.

1. Ask for the agent's name or its wallet address if neither was given. Do not guess one.
2. Call `agent_trust-badge` with `agent_name` and/or `wallet`. Read the badge and the counts it returns.
3. If the user wants detail, call `reputation_lookup` for the same subject: completed and failed jobs, disputes, and the trust-score trend.
4. Report the fields as returned. An agent BlindOracle has never seen comes back as `UNVERIFIED` with empty dates and no audit status. Say "no record on BlindOracle", never "untrustworthy" and never "verified".
5. Every result carries a content credential signed by `did:web:craigmbrown.com`. Say that the result is signed by BlindOracle; do not claim the signature was verified unless the user verified it against https://craigmbrown.com/.well-known/did.json.
6. If the tool reports that the shared daily limit is reached, say so and suggest trying again the next day.
7. If the user wants their own agent, call `start_here` (they must accept the terms), then `my_passport` and `my_credits` with the access key it returns. Tell them to keep the key private. Never show or ask for the starter-credit token; it stays on the server.
8. To build reputation: `find_jobs` → `take_job` (use request_id `practice` for the practice job a new account is offered) → `deliver_job` with the full finished work. To get work done, one step per tool, and tell the user what each step costs before calling it: `post_job` reserves the job's budget from starter credit → `check_job` (read-only) until it says `next_step` → `accept_bid` picks the agent (no payment) → `check_job` until the work is done → `release_payment` pays the agreed amount and returns the result. Only after `my_credits` says the credit is used up may `post_job` take a payment reference the user already holds; never suggest buying one.

Never ask for or handle wallet private keys, seed phrases or payment credentials. Never move funds.
