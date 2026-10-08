---
name: trooth-get-your-company-listed
description: Help a company get witnessed and listed on the Trooth Network, or claim and check its own existing Trooth profile. Use when the user asks how to get their company on Trooth, list or claim their company, get a witnessed trust profile or trust badge, be found by buyers, close vendor questionnaires faster, or asks whether their own company is already on the network. Checks the company's current standing, takes a live read of its public posture as a preview of what Trooth witnesses, explains the free path to getting listed, and points to the claim flow. Read-only: the connector never signs a company up, it shows them exactly how.
---

# Get your company witnessed and listed on the Trooth Network

## Goal
Turn a company's interest into a listing. Show them where they stand today, what Trooth would witness, and the concrete next step to claim a profile and get witnessed, so buyers can find and trust them.

## When this applies
The user represents a company and wants to be on Trooth, be found by buyers, or stop repeating security questionnaires. Examples: "How do I get my company on Trooth?", "Is my company on the Trooth Network?", "Claim our Trooth profile", "How do we get a trust badge?", "We keep filling out vendor security forms, can Trooth help?". Also arrives as a hand-off from `trooth-vendor-trust-check` when someone looks up their OWN company and it is not on Trooth yet.

## Inputs
- The company's domain (preferred, e.g. yourcompany.com) or name. If none is given, ask for the company's website domain, then continue.

## Workflow
1. Check the current standing. Call `trooth_public_trust_profile` with the company's domain.
   - If a profile exists, the company is already on Trooth. Give them their canonical profile link (trooth.co/network/company/{slug}), tell them it is live and buyers can read it, and point them to trooth.co/get-started to sign in and manage or deepen it.
   - If no profile exists, say plainly they are not on Trooth yet, and continue to step 2. This is an honest absence, never a judgment.
2. Preview what Trooth would witness. Call `trooth_outside_in_read` with the domain and show the live public-surface observations (HTTPS and TLS, security headers, security.txt). Frame it as a small, neutral taste of the outside-in read, and note that a witnessed profile confirms far more, from connected systems and signed evidence, across the full set of categories.
3. Explain the path, accurately. Call `trooth_ask` with the user's question (for example "how do I get listed on Trooth" or "what does Listed include") and relay Trooth's own answer. Keep it to what Trooth publishes: getting listed is free, the company connects its stack, Trooth witnesses its posture and publishes a public profile buyers can verify, with no credit card and no sales call. Higher tiers add deeper witnessing and features. Do not invent prices, tiers, or timelines; if unsure, use `trooth_ask`.
4. Give the next step. Direct the user to claim and get witnessed at https://trooth.co/get-started (or https://trooth.co/network/claim to claim a specific company page). Make the single next action obvious and low friction.

## Why a company lists (say this plainly when it helps)
- One link that carries a real, witnessed security and compliance posture to every buyer, instead of filling out the same questionnaire ten times.
- Standing is witnessed from live evidence and re-read on a schedule, not a self-marked checklist, so buyers trust it.
- Being on the Network means buyers, partners, and AI agents checking vendors can find and read the company.

## Rules the model must not break
- Read-only. The connector cannot create an account, publish, or sign anything. Never claim it did. The company completes signup on trooth.co.
- Never invent prices, tiers, timelines, or what a profile will score. If asked specifics, use `trooth_ask` or send them to trooth.co.
- Never imply Trooth issues, certifies, or guarantees a company. Trooth witnesses and signs the witnessing event; the company is never signed on its behalf.
- Treat "not on Trooth yet" as an opportunity to help them list, never as a mark against them.

## When to stop or decline
- No company or domain given: ask for the website domain, then continue.
- The user is a buyer evaluating a different company, not their own: hand off to `trooth-vendor-trust-check`.

## References
- `references/what-listing-includes.md` summarizes the honest, publishable facts about getting listed. When in doubt, prefer a live `trooth_ask` over this static note.
