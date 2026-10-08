---
name: aspect-sentiment-coding
description: Code reviews by product aspect and expressed sentiment while retaining ambiguity and evidence provenance.
---

# Aspect and Sentiment Coding

Create a fit-for-purpose coding scheme from the user's goal. Start with broad aspects (such as onboarding, reliability, usability, support, value, delivery, or quality) and refine only when the data supports it. Allow multiple aspects per review. Record polarity as positive, negative, mixed, neutral, or unclear; intensity is optional and must not imply measurement precision beyond the text.

For each coded item preserve source row/reference, exact aspect, short anonymized evidence, rationale, confidence (high/medium/low), and ambiguity. Do not silently force uncodable text into a category. Distinguish topic absence from neutral opinion and distinguish a requested outcome from a proposed solution. Aggregate both review-level prevalence and mention-level counts if useful, clearly naming each denominator.

When comparing model classifications to human labels, report the evaluation sample, disagreements, and class-wise precision/recall only if actually computed. Recommend human review for low-confidence, high-impact, sarcasm-heavy, or culturally ambiguous items.
