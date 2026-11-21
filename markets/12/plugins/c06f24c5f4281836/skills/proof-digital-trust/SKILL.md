---
name: proof-digital-trust
description: Use Proof when a user needs verifiable identity or credential presentation over x401, PDF e-signing, remote online notarization, or supported Proof account information.
---

# Proof digital trust workflows

Use the connected Proof MCP when the user asks to prove identity or authorization with a Verifiable Credential, satisfy an x401 credential challenge, e-sign PDF documents, begin remote online notarization, or access supported Proof account information.

For x401, preserve the protected origin and the exact `PROOF-REQUEST` value. Start the presentation through Proof, show the returned approval link when user approval is required, and retrieve the result only at the interval directed by the tool. Treat any returned `PROOF-RESPONSE` as single-use and send it only to the site named by Proof.

For e-signing or notarization, accept only PDFs through the document-upload workflow. One transaction may contain up to three uploaded PDFs. Preserve document order. Return the activation link for the user to verify identity and continue; do not state that signing or notarization is complete merely because a transaction was created.

Require the user's Proof OAuth connection for account-bound actions. Never invent credentials, approval results, transaction states, document identifiers, presentation values, or account data. Ask for clarification when the user's requested action does not map to an available Proof tool.
