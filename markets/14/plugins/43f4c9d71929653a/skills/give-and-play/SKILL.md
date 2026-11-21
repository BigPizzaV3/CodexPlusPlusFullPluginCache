---
name: give-and-play
description: Claim a supplied Wildcards invitation, pass a held power, choose its consenting target, or play it once and open the saved result.
---

Read [the shared contract](../../references/contract.md). Inspect only the invitation the user supplied with inspect_wildcard_invitation; parse card and code from its fragment without logging the private code. Inspection does not claim. Claim with claim_wildcard only when requested, using the user's chosen display name. Explain that the name appears with the saved effect and on public works. In ChatGPT the claim belongs to the signed-in account. The website also supports a free guest wallet and private return link.

Use list_wildcards(kind=wallet) or read_wildcard to recover an existing held card. Open render_wildcards(screen=card,id=returned card ID) or read_wildcard_work with matching card_id. Let the holder choose an accepted work and when to play. Native controls are available; never spend merely to preview. play_wildcard requires the held claimed card, accepted work ID, and a fresh request_id for the intended spend. A successful result atomically saves spent state plus the complete effect. A retry of that request recovers it. Another spend must fail; rejected targets leave the card available. Show returned credit and saved work, not an invented result.

Harbor Storm changes rain, wind and physically tethered boats. Music Storm changes the actual event plan with rain percussion and thunder. Audio starts only through the explicit Play music control. Do not claim audible verification from a label alone. Use render_wildcards(screen=work,id=work ID,card_id=card ID) to revisit.

For an authorized pass, read_wildcard then pass_wildcard with current expected_revision. The pending transfer blocks play until claimed or canceled. Return the private link for deliberate sharing; send no message. Cancel a pending transfer only when requested. Never spend for the issuer or a stranger, bypass a claim race, or create access to other wallets.
