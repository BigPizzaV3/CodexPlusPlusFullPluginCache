---
name: system-design
description: Create technology-neutral system architecture views and deployment options.
---

# System Design

Apply when the user asks for a new or revised system architecture.

1. Start with system context and trust/data boundaries; progress to containers/components and deployment only at the level requested.
2. Describe responsibilities, interfaces, data ownership/flows, synchronous and asynchronous paths, and important failure modes. Use Mermaid or text diagrams when useful and label inference.
3. Explain how identity, authorization, secrets, encryption, input validation, backups, observability, and recovery fit the design; distinguish controls to implement from those actually verified.
4. Compare options against requirements and team constraints. Discuss capacity assumptions, scaling limits, cost drivers, operational burden, vendor lock-in, and migration/exit paths.
5. Prefer proven simple designs until measured needs justify additional distributed complexity. Identify what requires a prototype, benchmark, threat model, or load test.

Return a design summary, diagram, trade-off table when useful, risks, and validation plan. Do not fabricate pricing, performance numbers, or cloud service capabilities; verify current facts using official primary documentation when browsing is available.
