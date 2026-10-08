---
name: find-legal-context
description: Turn an in-house legal request into a grounded Sandstone context by finding the related matter, people, companies, conversations, and documents. Use for an unstructured request or ambiguous record lookup.
---

Turn the user's request into a grounded legal-work context using read-only GraphQL operations.

1. Extract the request, urgency, requested outcome, named people, companies, matter names, and document references.
2. Use schema search or introspection only to discover the fields needed, then execute read-only GraphQL queries. Try exact names first, then narrower combinations; do not guess when multiple records match.
3. Present the best matching matter and relationship context with links or record identifiers and a short reason for each match.
4. List relevant documents and their dates. Distinguish directly matching records from nearby context.
5. Ask only for the smallest clarification needed when confidence is low. Never claim that a record exists when the search returned no match.

Do not make legal conclusions or execute mutations. Do not expose unrelated records.
