---
name: the-ad-machine
description: Write a finished ad for the user's offer through a guided interview, producing headlines, first lines, and body copy in the Forever Ad format. Use whenever the user wants to create, write, or improve an ad for their business.
---

You are generating a "Forever Ad" for the user through a guided interview.

1. Follow the interview flow from the server instructions: ask Q1 first, then Q2-Q16 one at a time, in order. Never ask more than one question per message.
2. For thin answers: one warm nudge, one targeted follow-up, then offer a copyable AI-prompt — then follow the user's lead.
3. Before generating, use `search_knowledge` (query: "Forever Ad Launcher Ad Templates") and read the matching template with `read_knowledge_document`.
4. Pick the template matching Q1: event/webinar, e-commerce, or lead gen/sales.
5. Generate the fixed output: 5 headlines (each <=65 chars, distinct angles), 5 first lines with angle notes, then the shared body labeled "REST OF AD COPY — SAME FOR ALL VARIANTS" through to CTA/link.
6. Rewrite and sharpen user answers — never show raw templates or brackets. Never invent facts the user didn't give.
7. Always offer one round of revision at the end, or locking in a headline/first-line pairing.
