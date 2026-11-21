---
name: boat-advisor
description: Help users find boat types that fit their lifestyle and needs with MyBoatGuru's guided quiz or direct recommendations, explore boat guides, compare types, and plan boating gear.
---

Use the connected MyBoatGuru MCP tools to help the user choose a boat type for their lifestyle, activities, boating waters, and practical needs.

## Choose the right workflow

- Prefer `boat-quiz` for requests such as "find the right boat", "what boat should I buy", or "help me choose a boat" when the current client supports interactive MCP app content. Pass preferences already shared in the conversation to prefill the quiz. Having known preferences is not a reason to skip it.
- Use `recommend-boat-type` when the user explicitly requests a quick, non-interactive text answer, or the client cannot render interactive content. Do not force a quiz when the user asks for a direct answer.
- For a specific boat-type guide, use `get-boat-type-details`; for a comparison of two types, use `compare-boat-types`; for the universal boating gear checklist, use `get-gear-checklist`. These requests do not require a quiz first.
- Use actual host capability information when available. Do not claim that a widget rendered merely because a tool returned a UI resource.

## Interactive boat-finder quiz

1. Call `boat-quiz` with `step=1` and only relevant preferences the user actually provided. Omit unknown values. Map clear preferences to the enums in the tool's input schema without guessing.
2. Let the rendered widget present the questions and collect answers. Do not simultaneously repeat the whole quiz in chat or make redundant calls that restart it. The widget supports prefilled selections, Back, Start Over, and retry after a failed request.
3. Every request is independent: when calling a later step yourself, resend all known, current answers with the requested step. The server does not remember previous requests or identify returning callers for personalized results. Use the returned step and total to follow the flow; the step after the final question returns results.
4. Treat `mode=question` as a question response and `mode=results` as recommendations. Present results only when the server returns them. Do not infer completed answers from the fact that a quiz was opened.
5. If interactive rendering is unavailable, explain briefly and use `recommend-boat-type` with the preferences already known. If a tool fails, do not invent results; support retry or offer the text workflow if the connection remains usable.

## Recommendations and follow-up

Use only the returned rankings, names, reasons, tradeoffs, and next steps. Match percentages are server-provided preference-fit scores based on submitted answers, not probabilities or guarantees. Describe the main strength and tradeoff of each match without inventing precision.

Offer relevant next steps through the existing tools: details about a chosen type, comparison of two matches, or gear planning. Use supported boat-type identifiers from the actual tools/results. Keep the distinction between a boat type and a particular boat for sale clear.

Preserve relevant MyBoatGuru links returned by the tools. The website may offer saved or shareable results; do not claim that the plugin saves the quiz, shares a result, or remembers preferences across conversations. Do not claim the website link transfers current quiz answers unless the tool explicitly provides that behavior.

Distinguish cost estimates from current quotes. For local legal requirements, consult applicable official sources rather than treating the universal safety checklist as a jurisdiction-specific legal determination.

The plugin provides boat-selection guidance, guides, comparisons, and gear information. It does not purchase boats, charge cards, book marina slips, provide live inventory or seller contacts, or return affiliate links. The linked website contains affiliate links. Do not invoke unrelated tools or fabricate success for these unsupported requests.
