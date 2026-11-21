---
name: answer-trail
description: Create and read a dated Rankfor brand-evidence snapshot for one neutral buyer question.
---

# Rankfor Answer Trail

Use this workflow only when the user asks to run or read an individual Rankfor Answer Trail snapshot.

## Check tool availability

Locate `create_visibility_snapshot` and `get_visibility_snapshot` in the connected Rankfor tools. If the host provides tool search or deferred tool discovery, use it before concluding that the tools are unavailable. Reading this skill or completing sign-in does not establish that the tools are enabled in this conversation.

If the tools remain unavailable, stop the snapshot workflow. State that no Answer Trail measurement was run and ask the user to enable the Rankfor connection in a new Work chat. Do not replace the requested measurement with a list of brands from general web search. Offer separate web research only if the user asks for it.

## Create a snapshot

1. Use a neutral category question that can be asked without naming the target brand. Supply the brand and domain through `target_brand` and `target_domain`.
2. If the request is leading, comparative or names the target inside the evaluated question, propose a neutral replacement and obtain the user's confirmation before starting compute.
3. Call `create_visibility_snapshot` once with a fresh UUID v4 idempotency key. Reuse that key only when retrying the same request after a timeout or uncertain network result.
4. Use the requested language and market as parameters. Do not claim they affected provider behavior until the returned evidence demonstrates it.
5. Poll `get_visibility_snapshot` at the returned `poll_after_seconds` interval. Stop after six attempts. If collection remains in progress, return the snapshot ID.

## Report evidence faithfully

- Describe every result as an individual Gemini or OpenAI API snapshot with its collection time and snapshot ID.
- Treat `target_observation.state` as the service's evidence classification. `observed` can reflect returned discovery evidence. Call an excerpt a direct answer quote only when the response explicitly identifies it as raw answer text.
- Use `not_detected` only for a successful provider observation. Preserve failed, incomplete and unavailable provider results as `unknown` or their exact returned state.
- List candidate brands and citations exactly as returned. A citation is a source URL supplied by the provider. It does not prove that the source caused a brand observation.
- Describe an unlisted `share_url` as a bearer link accessible to anyone who receives it. Do not call it account-restricted.
- State that the plugin measures API snapshots. Do not describe them as consumer ChatGPT measurements, persistent rankings, market-wide results or ongoing monitoring.

## Stay within scope

Do not use these tools for general web research, SEO planning, content generation, publishing, subscription management or continuous monitoring. Do not start a replacement paid run silently after a neutrality error. Ask for confirmation first.
