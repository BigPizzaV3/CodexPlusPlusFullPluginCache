---
name: verifyum-proofs
description: Check, verify and anchor Verifyum proofs that exact file bytes existed at a point in time, anchored on Solana Mainnet without uploading the file. Use when the user gives a Verifyum proof ID or proof URL, asks whether a proof is genuine or what it shows, asks to anchor a Verifyum commitment, or asks how to timestamp, seal or prove a file, dataset, contract draft, log or decision record. An anchor is a permanent public transaction, so never create one during setup, tests or exploration.
license: MIT
---

# Verifyum proofs

Verifyum proves that a commitment to exact file bytes existed no later than a
Solana Mainnet block time. The file stays on the user's device. Only a
domain-separated commitment is sent, and the public proof holds nothing that
identifies the file.

## If the tools are missing

If no `verifyum_` tool is available, the Verifyum plugin is not enabled in
this conversation. Ask the user to enable it and start a new conversation.

## Which tool for what

- **Follow a proof**: `verifyum_get_proof` with `proof_id`. The status is
  `queued`, `submitted`, `finalized` or `failed`. A proof URL has the form
  `https://<proof_id>.verifyum.com/`, so take the ID from the host name.
- **Check a proof**: `verifyum_verify_public_proof` with `proof_id`. Verifyum
  checks the metadata, the exact 128-byte memo and the Ed25519 service
  signature against the published key registry, and returns the exact Solana
  RPC request under `chain_check`. Tell the user that Verifyum performed this
  check itself, and that `chain_check` lets anyone confirm the chain part
  separately.
- **Anchor a commitment**: `verifyum_anchor_commitment` with `commitment` and
  `idempotency_key`, only for a commitment the user built with Verifyum's own
  code, such as the single-file clients https://verifyum.com/clients/verifyum.py
  and https://verifyum.com/clients/verifyum.mjs. Never build the manifest or
  the commitment yourself. A wrong commitment is anchored all the same and
  will never match the file.
- **Prove a file**: this plugin never receives files. Send the user to
  https://verifyum.com/create, which hashes the file in the browser, keeps
  the private draft on the device and anchors only the commitment.
  Developers can run the clients above on their own machine. The guide is at
  https://verifyum.com/agents.

## Before anchoring

1. Make sure the user asked for a proof of that specific record.
2. Say that the anchor is a real, public and permanent Solana Mainnet
   transaction that cannot be withdrawn, and ask for confirmation.
3. Use the idempotency key the user gave. Otherwise make one of 16 to 128
   URL-safe characters and show it, so a retry can reuse it.
4. Call the tool once. Then follow the proof with `verifyum_get_proof` every
   few seconds until it is `finalized` or `failed`.

## Rules

- Never anchor while testing the connection, exploring, guessing what the
  user might want, working in bulk, or as a side effect of another task.
- Never send a file, its name, its raw hash, the nonce or the private
  manifest to Verifyum, to a URL or into a message. The tools take only a
  commitment, an idempotency key or a public proof ID.
- Retry with the same commitment and the same idempotency key. That returns
  the same proof, never a second one. Never retry in parallel. If the service
  answers that the rate limit is reached, wait as long as it says and tell
  the user.
- Verifyum cannot move funds, sell anything or delete a proof.

## What a proof shows

A finalized proof shows that a commitment to the exact file bytes existed no
later than the estimated Solana block time, and that those bytes have not
changed since. It does not prove authorship, ownership, legal signature
validity, when the file was first created, or that its contents are true. Say
this plainly when you hand over a proof URL.

## Check the connection

This check reads a public proof and never anchors anything.

1. Call `verifyum_get_proof` with proof ID `72c38s8rrqa4vjhw6dxsvmbqkq`. The
   answer is status `finalized` on network `mainnet-beta`.
2. Call `verifyum_verify_public_proof` with the same ID. The verdict is
   `valid`, and `chain_check.expect` gives slot `442907852`.

Any other answer means the call did not reach Verifyum or something is wrong.
Stop and tell the user.

Reference: https://verifyum.com/agents and https://verifyum.com/docs/agent-api.md
