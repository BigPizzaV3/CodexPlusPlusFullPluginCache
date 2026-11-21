# WZRD product trust and launch readiness

Use these as review lenses for WZRD rooms and creator/participant journeys. Confirm the live behavior before reporting a defect; these principles originated in a launch-readiness audit and are not proof that a past issue remains present.

## Core journeys

A release should make these journeys dependable on desktop and mobile:

1. Create and share a trustworthy room without an account.
2. Upgrade that exact guest room without losing its link, content, settings, activity, or working context.
3. Answer a participant from current, permitted room content and show what supported the answer.
4. Complete each configured outcome—CTA, form, booking, payment, download, email, or webhook—end to end.

## Publish confidence

- Before sharing, catch trust-breaking problems: untitled rooms, misleading sample claims, unconfigured actions, incomplete forms, missing destinations, invalid generated content, and inaccessible primary paths.
- Hide or disable visible actions until they are configured and tested. Never present a no-op control as finished.
- Make draft, published, unpublished, pending-change, expiry, and last-updated states legible.
- Offer a visitor test that exercises every visible action and participant path.
- Keep the readiness check lightweight enough to preserve guest-first creation.

## Guest sharing and ownership

- Keep account-free creation and sharing. Explain link access, expiry, device/browser ownership, recovery limits, and what signup preserves or unlocks.
- Ask for signup at a value boundary—durable saving, teammates, protected sharing, response details, analytics, or integrations—not before the guest can experience the core value.
- Preserve the room ID, public URL, content, settings, visitor history, responses, conversations, and current location through upgrade.
- Use room-type-aware defaults. Sensitive rooms should default to shorter expiry, no embedding, and downloads off. State clearly when access means “anyone with the link.”
- Memory, retention, and cross-room transfer need plain-language consent and controls.

## AI answers and actions

- Ground answers in the rendered room, structured blocks, attached documents, catalogue records, and current published values that the participant is allowed to access.
- When useful, cite or deep-link to the supporting room content. State uncertainty when sources are missing, contradictory, stale, or private.
- Never claim that a person was notified, an edit succeeded, or an external action completed without confirmation.
- For content-changing actions, prefer exact proposed diffs and approval when the change is destructive or high impact. Validate both the block schema and rendered result before success.
- Use least privilege. Empty permission selections must not silently mean “everything.” Risky actions need clear grants, dry-run or test modes, idempotency where relevant, and an audit trail.

## Mobile and accessibility

- Verify participant and creator journeys at 320, 375, 390, 768, 1024, and desktop widths, or state explicitly when creator mobile is unsupported.
- Tabs, chat, narrator, cart, and primary actions must not overlap, clip without an affordance, or escape a preview frame.
- Target WCAG 2.2 AA: keyboard navigation, visible focus, useful accessible names, semantic status updates, sufficient contrast, and 44 px touch targets.
- Respect reduced motion and do not rely on color alone for important status.

## Information architecture and language

- Organize work around user jobs and normal words. A useful model is Build, Ground, Automate, Collaborate, and Measure.
- Keep the primary product category clear: WZRD creates conversational rooms or experiences; documents and widgets are capabilities inside them.
- Name AI roles consistently and make it obvious whether a conversation edits the room, reaches teammates, handles visitors, or records activity.
- Keep template selection, creation, publication, and sharing behavior consistent across entry points.

## Analytics, reliability, and recovery

- Separate business outcomes from raw interface, agent, and integration events. Present human labels instead of internal keys.
- Show enough safe aggregate value at an account gate to explain why signup matters, then return the user to the exact prior view.
- Verify event deduplication, privacy handling, and agreement between analytics and raw logs.
- Provide useful loading, empty, expired, unpublished, deleted, restricted, offline, generation-failed, and action-failed states with recovery paths.
- Track latency and errors for generation, ingestion, chat, voice, publishing, webhooks, email, booking, and payments. Avoid knowingly failing requests followed by silent fallback.

## Priority model

- **P0:** a core journey is broken, misleading, unsafe, or loses trust/data.
- **P1:** a material beta risk affects comprehension, mobile use, accessibility, AI grounding, recovery, permissions, or measurement.
- **P2:** consistency, polish, discoverability, and optimization.

Recommend the smallest sequence that clears P0 first, then reduces the largest P1 risks. Do not bury launch blockers in a long undifferentiated checklist.
