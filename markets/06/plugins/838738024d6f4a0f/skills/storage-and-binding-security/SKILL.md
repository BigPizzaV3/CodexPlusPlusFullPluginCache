---
name: storage-and-binding-security
description: Assess R2, KV, Durable Objects, Queues, Vectorize, and other Cloudflare storage or data bindings.
---

# Storage and Binding Security

Inventory relevant resource bindings and identify which Worker can read, write, list, delete, or publish data. Review authorization before access, tenant/key namespace separation, validation of object names and uploads, content-type and size controls, malware/content handling, retention/deletion, backup/recovery, and sensitive metadata.

For R2, check public access domains, `r2.dev` exposure, custom-domain protections, CORS origin/method/header scope, presigned URL operation/object/expiry, and credential separation. Public buckets expose objects to the internet; CORS does not make a bucket private. Treat presigned URLs as bearer secrets and do not log or repeat them. For KV, assess assumptions about consistency and stale authorization state. For Durable Objects, review identity-to-object routing and per-object authorization. For Queues and async workflows, validate producer trust, message schemas, retries, idempotency, poison-message handling, and sensitive payload logging. Do not inspect object/table contents by default.
