# SAP Cloud Integration code and transformation workflow

Ask runtime/processor only where needed: CPI Groovy runtime/version, permitted APIs, XSLT processor/version, mapping engine and adapter. Never assume XSLT 3.0 or specific Groovy library compatibility; confirm supported engine before syntax selection.

First analyze whether Content Modifier, XPath conditions, Router, Message Mapping, XSLT, standard adapters or Value Mapping solve the task before selecting Groovy. Content Modifier can set exchanges headers/properties and body using supported expression types, with XPath capabilities dependent on the step/expression context.

Groovy: if writing CPI scripts, use applicable SAP message interface API and supported libraries; do not hardcode credentials. Be mindful of streams vs materialized large payloads; null safety, encoding, namespace handling, logging redaction, deterministic failures. Show full snippet, imports, expected headers/properties, example payload and output.

XSLT: declare stylesheet version and namespace prefixes, avoid accidentally matching namespaces incorrectly, explain XPath context, output format and escaping, and note XSLT/XPath compatibility by processor. Static review is NOT compilation or runtime test.

REST/OData/SOAP: distinguish HTTP method, URL placeholders, Accept/Content-Type, CSRF handling where relevant, pagination, batch semantics, rate limits, OAuth scopes and retries. Do not invent endpoints or OData entities; request a metadata sample or official reference.

Testing checklist: happy path, missing keys, null/empty field, namespace variants, escaped characters, large payload, duplicate event, bad auth, expired credential, timeout, 429/5xx, target business rejection, recovery idempotency. Say 'illustrative/unexecuted' without test tools. Never print secrets or customer data in example logs.
