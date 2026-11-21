---
name: screen-address
description: Screen a cryptocurrency address for compliance risk with CipherOwl and explain any findings. Use when someone asks whether an address is risky, sanctioned, or safe to transact with, or why an address was flagged.
---

# Screen a cryptocurrency address

Pick the CipherOwl tool by what the user asks:

- Whether an address is risky, sanctioned, or safe to transact with: call
  `screen` with the address. Pass the chain only when the user names it;
  CipherOwl detects the chain from the address otherwise.
- Why an address is flagged, or the details behind a finding: call
  `reason_risk` for the address. It does not need a `screen` call first.
  Explain each reason: the risk category, whether funds were sent or
  received, how many hops away the source is, and the value and share of the
  exposure.

When you answer:

- Report what CipherOwl found under the organization's risk configuration.
  A clean result means CipherOwl found no risk indicators; never promise that
  an address is safe.
- After a `screen` result that found risk, offer to explain the reasons,
  unless the user already asked why or for the details; then call
  `reason_risk` right away.
- If a result carries a `plan` note, tell the user what it says, so a limited
  result is not presented as complete.
- If a result carries a link to the address on CipherOwl, include it.
- CipherOwl returns risk signals, not personal identities. Do not try to
  identify the people behind an address.
- These tools are read-only. They cannot send, freeze, or report funds.
