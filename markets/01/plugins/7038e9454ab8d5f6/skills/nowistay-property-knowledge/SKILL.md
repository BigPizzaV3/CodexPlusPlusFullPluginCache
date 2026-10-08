---
name: nowistay-property-knowledge
description: Maintain the private Nowistay AI co-host knowledge base for each property. Use to list, search, add, correct, or copy reusable property questions and answers such as policies, equipment details, access guidance, and local recommendations.
---

# Nowistay Property Knowledge

Manage private Q&A knowledge separately from the public welcome guide.

Store reusable property facts, not guest records. Do not add guest names, contact details, booking references, message transcripts, private notes, payment data, government identifiers, medical or biometric data, account credentials, or other guest-specific information to the knowledge base.

## Read and find

1. Resolve source and target properties once with `list_properties`.
2. Use `list_property_knowledge_questions` with `limit=100`; paginate only when needed. Use `search` to avoid loading the full knowledge base for a focused question.
3. Use `get_property_knowledge_question` only when one exact record needs verification before an update.
4. Present questions and answers conversationally. Keep internal IDs out of the response unless needed for disambiguation.

## Add or update

1. Check for an existing equivalent question before creating a new one.
2. Use `create_property_knowledge_question_preview` for new Q&A and `update_property_knowledge_question_preview` for corrections.
3. Preserve `need_host` unless the user explicitly changes whether future answers require host intervention.
4. Summarize the exact question, answer, property, and host-review setting.

## Copy between properties

1. List the source Q&As first and resolve every target property.
2. Use `copy_property_knowledge_questions_preview` with selected `question_ids`, or omit them to copy all source Q&As.
3. Explain that copying is a safe merge: matching normalized questions are skipped and target knowledge is never deleted or replaced.
4. Use one multi-target copy rather than repeating one copy per property.

If the user asked only for a proposal, stop at the preview. If the user explicitly requested the write, continue through platform confirmation with the matching confirm tool and only the approval token. Do not expose vector-store or database implementation details.
