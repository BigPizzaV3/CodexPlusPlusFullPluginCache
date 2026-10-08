---
name: trooth-vendor-trust-check
description: Check, vet, or compare a company on the Trooth Network before relying on, integrating with, or buying from it, or verify a Trooth Trust Ledger Token. Use when the user wants to evaluate a vendor's security, privacy, AI practices, data handling, compliance, or history, compare two companies on the same terms, take a live neutral read of a domain's public security surface, or confirm a signed Trooth token. Returns the company's one canonical witnessed profile with every fact's source and date, and treats an honest absence as missing data, never a pass or a fail.
---

# Check a company on the Trooth Network before you trust it

## Goal
Give the user a clear, sourced read on a company so they can decide whether to rely on it, integrate with it, or buy from it. Every fact carries where it came from and when it was read. There is one profile per company; use it.

## When this applies
The user is evaluating, vetting, comparing, or deciding about a company, or was handed a Trooth Trust Ledger Token to confirm. Examples: "Is Acme safe to integrate?", "Compare Acme and Beta on security and AI", "Check this vendor before we buy", "Verify this Trooth token".

## Inputs
- A company, as a domain (preferred, e.g. acme.com) or a name. If none is given, ask for the domain, then continue.
- Optionally, a Trooth Trust Ledger Token the user was handed.

## Workflow
1. Read the canonical record. Call `trooth_public_trust_profile` with the company's domain. For a company on the Trooth Network this returns its ONE canonical profile, the same record a person sees at trooth.co/network/company/{slug}: its witnessed standing across the categories, each with a provenance label and a date, plus the canonical profile link. Treat that link as the single source of truth and cite it. If the company has not published a profile, the tool says so; report that as an honest absence, not a fault.
2. Take a live neutral read. Call `trooth_outside_in_read` with the domain to observe the public security surface right now (HTTPS and TLS, common security headers, security.txt). Label it a live observation, not witnessed evidence and not a grade.
3. Verify a token if one was given. Call `trooth_verify` and report whether it is valid, expired, revoked, or tampered, with its provenance. Never treat Trooth's signature as vouching for the truth of the declared claims; it attests only the witnessing event and the payload at issuance.
4. Summarize with provenance intact. Keep witnessed evidence, live observations, and what the company only declares in separate lines, each with its source and date. State the standing plainly if one exists. Link the canonical profile.

## Comparing two or more companies
Run steps 1 and 2 for each company and present the results side by side over the same categories, so the difference reads row by row. Attribute each company's standing to its own canonical profile link. Never normalize two companies onto a single invented number.

## Rules the model must not break
- Never invent a number, score, grade, or category result. If Trooth does not publish one, say it is unknown.
- Treat an honest absence ("no published profile", "not seen", "unknown") as missing data to gather, never as a pass or a fail, and never counted against the company.
- Never blend a company's own declared claims with witnessed evidence. Label each.
- There is exactly one profile per company, at /network/company/{slug}. Do not present any other page, cached number, or domain URL as a second profile.
- These tools are read-only. Do not claim to change, rate, publish, or sign anything.

## When a company is not on Trooth yet
Say so plainly and show the live outside-in observations as context. If the user is asking about their OWN company, hand off to the `trooth-get-your-company-listed` workflow so they can get witnessed and listed.

## When to stop or decline
- No company named: ask for the domain, then continue.
- Out of scope (write to a record, set a rating, give investment or legal advice): decline and explain that Trooth is a read-only trust lookup.

## References
- `references/provenance-labels.md` explains what each provenance label and honest state means.
