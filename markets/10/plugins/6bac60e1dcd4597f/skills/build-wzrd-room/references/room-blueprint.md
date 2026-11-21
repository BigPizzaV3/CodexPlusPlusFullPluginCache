# WZRD room blueprint

Use this structure as a decision model, not as a form that must always be shown in full.

## Room identity

- **Title:** specific, participant-facing, and never “Untitled.”
- **Purpose:** the job this room should accomplish.
- **Audience:** who will enter and what they already know.
- **Primary outcome:** the one action, decision, or understanding the room should produce.
- **Room type:** choose the closest WZRD type when known; otherwise describe the behavior instead of inventing a category.

## Source inventory

Give every included source a stable identifier:

| ID | Source | Included material | Treatment | Sensitivity |
|---|---|---|---|---|
| `C1` | Conversation | Topic or message range | summarize / quote / decision | public / room-only / private |
| `D1` | Document | Filename and relevant pages/sections | attach / extract / summarize | public / room-only / private |
| `L1` | Link | Page title and URL | cite / extract / action | public / room-only / private |

Record exclusions separately with a short reason: user excluded, superseded, duplicate, irrelevant, inaccessible, or sensitive.

## Participant-facing structure

Use only the sections the participant needs. Common patterns include:

- **Overview:** what this is and why the participant is here.
- **Brief or proposal:** the distilled argument, plan, or offer.
- **Decisions:** settled choices and their consequences.
- **Work or deliverables:** final artifacts, previews, or outputs.
- **Documents:** first-class source files and supporting evidence.
- **Timeline:** milestones, sequence, or conversation history when time matters.
- **Questions:** likely participant questions grounded in the room sources.
- **Next step:** a configured, testable action.

Do not create a section merely because source material exists. Merge thin sections and move detail into attached knowledge when that keeps the participant journey clear.

## Conversation transformation

- Convert exploration into a concise brief.
- Convert explicit agreements into decisions.
- Convert assigned work into owners and next steps only when ownership was actually stated.
- Keep unresolved branches under “Open questions” or “Options.”
- Prefer the latest explicit revision. Preserve an earlier version only when it explains a decision or the user asks for history.
- Attribute direct quotations and never fabricate consensus.

## Room intelligence

Define what the room should answer, which sources it may use, and what it must not reveal. Include fallback behavior for missing, conflicting, stale, or private information. The room must not claim a handoff or action succeeded without confirmation.

## Access and behavior

Specify draft/published state, audience, link visibility, expiry, download behavior, embedding, participant memory, and whether updates should flow into the shared room. Default to draft and least privilege when the user has not decided.

## Provenance map

Map material room content back to source IDs:

| Room item | Source IDs | Transformation | Confidence or issue |
|---|---|---|---|
| Claim, decision, section, or asset | `C2`, `D1` | quoted / summarized / proposed | verified / conflict / needs confirmation |

Proposed copy may have no factual source, but label it as proposed. Material factual claims should have a source or an explicit verification flag.

## Build-ready handoff

When direct room creation is unavailable, provide:

1. Room identity and outcome.
2. Inclusion and exclusion summary.
3. Ordered participant-facing sections with ready-to-use copy.
4. Document and knowledge attachments.
5. Room intelligence and participant questions.
6. Actions and configuration dependencies.
7. Access and sharing settings.
8. Provenance map.
9. Open decisions and blockers.

This package is the room specification. Do not call it a published or created room until WZRD confirms creation.
