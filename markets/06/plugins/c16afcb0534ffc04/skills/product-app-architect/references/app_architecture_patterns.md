# App Architecture Patterns

## Purpose

Use this file after product requirements and key nonfunctional needs are understood.

Architecture is a set of trade-offs, not a technology shopping list. Prefer the simplest viable design and state what would invalidate it.

# 1. Architecture inputs

Before selecting components, identify as relevant:
- primary user flows;
- expected traffic/scale;
- data volume;
- latency needs;
- availability/recovery needs;
- sensitive data;
- auth/authorization;
- real-time requirements;
- background processing;
- search;
- files/media;
- integrations;
- offline behavior;
- analytics;
- AI/model usage;
- team/operating constraints;
- budget.

When unknown, state assumptions rather than inventing requirements.

# 2. Simple web application

Typical starting shape:

`Browser → web app/server → relational database`

Optional only when justified:
- object storage;
- cache;
- background worker;
- search service;
- CDN.

Use when scale and workflows are straightforward and speed of delivery matters.

Do not split into microservices without a real boundary or scaling/ownership need.

# 3. Content / public website

Typical concerns:
- static/server rendering;
- CMS/content source;
- search;
- media;
- caching/CDN;
- SEO;
- analytics;
- editorial workflow.

Keep authoring/publishing requirements separate from public rendering.

# 4. SaaS application

Add explicit decisions for:
- tenant model;
- authorization;
- billing if actually required;
- audit logs;
- admin/support access;
- data isolation;
- quotas;
- lifecycle/deletion.

Do not add billing or organizations to a single-user product without a requirement.

# 5. Mobile app

Typical shape:

`Native client → API/backend → storage/services`

Decide:
- local state;
- offline/cache;
- sync;
- push notifications;
- permissions;
- secure token storage;
- platform integrations;
- version compatibility.

Do not place business-critical secrets or authoritative security rules in the client.

# 6. Real-time product

Use real-time infrastructure only when delayed updates materially harm the experience.

Possible tools:
- WebSocket/SSE;
- pub/sub;
- event stream;
- presence/state service.

Define ordering, reconnect, missed-event recovery, fan-out, backpressure, and authoritative state.

# 7. Background work

Use jobs/queues for work that is slow, retryable, scheduled, bursty, external-API dependent, or unnecessary to complete synchronously.

Define idempotency, retry policy, dead-letter/failure handling, progress/status, timeout, and duplicate execution behavior.

# 8. Search

Start with database/native search when sufficient.

Add a dedicated search engine only when advanced relevance, typo tolerance, faceting, scale, or specialized indexing justify it.

Define freshness and source of truth.

# 9. AI-enabled feature

Treat AI as a bounded subsystem.

Define:
- exact user task;
- model input/output contract;
- source data;
- deterministic vs model responsibility;
- structured outputs;
- tool permissions;
- evaluation;
- fallback;
- privacy;
- latency/cost.

Do not add RAG or agents unless the task requires them.

# 10. Security architecture

Identify:
- trust boundaries;
- identity;
- authorization;
- tenant/resource ownership;
- secrets;
- sensitive data;
- encryption needs;
- audit events;
- abuse cases;
- destructive actions.

Prefer least privilege, secure defaults, server-side authorization, validated contracts, and explicit retention.

Use current OWASP guidance for detailed verification requirements.

# 11. Reliability and operations

Define only to the level the product needs:
- health signals;
- logs/metrics/traces;
- backups;
- restore testing;
- deployment/rollback;
- dependency failure behavior;
- rate limits;
- graceful degradation;
- ownership/runbook.

Do not build mission-critical complexity for a low-risk prototype.

# 12. Architecture decision format

For a meaningful choice provide:

**Recommendation**  
**Why**  
**Trade-offs**  
**Alternatives rejected**  
**What would invalidate this choice**  
**Migration path if needs grow**
