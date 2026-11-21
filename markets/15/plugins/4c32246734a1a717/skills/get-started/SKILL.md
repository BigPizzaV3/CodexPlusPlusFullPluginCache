---
name: get-started
description: >
  Get started with the account connection: what the GRC specialist
  covers, how the OAuth sign-in works, what to delegate to it, and what
  stays local. Use when the user asks to connect the account, asks what
  the connection can do, or wants to start delegating compliance work.
---

# ISMS Copilot: getting started

ISMS Copilot is a GRC specialist for ISO 27001, ISO 27701, ISO 42001,
SOC 2, GDPR, NIS 2, DORA, EU AI Act, HIPAA and PCI DSS. This connection
talks to the user's ISMS Copilot account over OAuth: the user signs in
with their ISMS Copilot account and approves the consent screen, and the
specialist works inside that account.

## What to delegate

- Framework interpretation: what a control or article requires, in plain
  language.
- Policy drafting and control mapping.
- Gap analysis, SoA justifications, risk registers and audit prep.
- Anything where the user would otherwise paste framework text first:
  do not paste it, the specialist already knows the frameworks.

One conversation per deliverable: start with the request, then follow up
in the same conversation so context carries over.

## Account data

The connected tools can list the account's workspaces and document metadata,
memories and company context, and can write memories, company context and
workspaces. Before drafting anything company-specific, read the stored
company context with get_company_context instead of inventing company
facts. Write only when the user asks: save a memory with create_memory
when the user asks you to remember something, and change the company
profile with set_company_context only when the user asks to update it
(it replaces the whole profile).

## What stays local

Code, files, git and credentials stay on the user's machine. Never ask
the user to paste API keys, passwords or secrets into the chat, and never
try to: this connection (OAuth sign-in) has no API key tools. If the user asks
for them, say they are not part of this connection; account settings
live in the ISMS Copilot app.

## Sensitive data and advice

Do not send health records, payment card data, government ID numbers,
passwords or API keys to the specialist; the frameworks can be discussed
without them. Answers are general compliance guidance for practitioners,
not legal advice: tell the user to review them before relying on them.

## Plans

Some features depend on the user's plan. If a feature is unavailable, say
so plainly, without adding links.
