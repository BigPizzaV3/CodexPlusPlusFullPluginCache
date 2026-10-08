---
name: email-compliance-deliverability
description: Flag jurisdiction- and provider-specific questions for manual B2B email compliance and deliverability review.
---
# Compliance and sender-guideline review

Apply when the user asks whether a cold email is legal/compliant, how to contact a recipient, or how to improve deliverability.

## Inputs

Ask for the sender's and recipient's jurisdictions, recipient type (for example, corporate subscriber versus sole trader/individual where relevant), message purpose/type, whether the recipient objected/opted out, and sending volume/provider only as needed.

## Process

1. Clearly distinguish a drafting checklist from legal advice. If key jurisdiction or recipient status is unknown, say the answer is conditional.
2. Prefer current official regulator/provider sources. For the U.S., flag FTC CAN-SPAM topics such as accurate sender/subject, ad identification where applicable, postal address, opt-out and honoring requests. For the UK, distinguish PECR subscriber categories and consider UK GDPR where personal data is processed; note that ICO guidance may be under review.
3. For provider deliverability, state that requirements depend on provider, traffic type, and volume. Google sender rules may require SPF or DKIM for all senders and additional SPF/DKIM/DMARC alignment and one-click unsubscribe for qualifying bulk/marketing traffic; verify current requirements before implementation.
4. If asked to contact someone who opted out or objected, advise not to send marketing follow-ups. Do not help evade suppression using another identity/address.
5. Provide a concise checklist and cite the primary source links when available.

## Output

Return “questions to verify” and practical copy/design checks, not a legal certification. Make the jurisdictional assumptions visible.

## Boundaries

Never guarantee legality, compliance, delivery, or inbox placement. Do not facilitate spam, purchased/scraped lists, suppression evasion, spoofing, header manipulation, or platform-rule circumvention. Laws and sender requirements change; verify official guidance for high-stakes/current decisions.
