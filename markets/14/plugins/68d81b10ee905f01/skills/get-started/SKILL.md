---
name: get-started
description: How to proofread and revise the user's text with Revise, using their saved writing rules, and how to review, explain and save the suggested changes.
---

# Getting started with Revise

Revise proofreads and polishes the user's own text using their saved writing rules.

## When to use Revise

Use Revise when the user asks to proofread, correct, polish or rewrite a piece of text they provide, or mentions Revise or one of their Revise rules. Don't use it to write new content from scratch or to answer general questions.

## How to use the tools

1. `revise_text`: pass the user's text verbatim. If they name a rule (for example "Concise" or "Make it formal"), pass it as `rule_name`, or call `list_rules` first to find its `rule_id`. Without a rule, Revise uses "Proofread".
2. The result opens in an interactive card where the user can accept or reject each change. Reply with a short summary of the main changes instead of repeating the whole text.
3. `explain_change`: when the user asks why something changed, pass the original text and the two spans.
4. `save_to_revise`: when the user wants to keep working on the text in Revise, save it and share the link.

## Limits

Each revision counts toward the word limit of the user's Revise plan. If the limit is reached, tell the user plainly; don't retry.
