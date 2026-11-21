# OpenAI review video script

Target length: 2–3 minutes.

## 0:00–0:15 — What Eli is
Show the Eli plugin enabled in ChatGPT.

Say:
“Eli is a public evidence-backed test for whether AI can understand, verify, and act with a company website.”

## 0:15–1:05 — Public company test
Prompt:
“Can AI do business with hireeli.io?”

Show `test_company_for_ai` being invoked and the resulting public evidence.

Point out that unknown or pending states remain unresolved rather than being invented.

## 1:05–1:40 — AI visibility
Prompt:
“Scan hireeli.io for public AI-search visibility.”

Show `scan_visibility`.

Explain that the result is a measured sample, not a claim about every ChatGPT or AI session.

## 1:40–2:00 — Get started
Prompt:
“How do I start using Eli?”

Show `get_started` and the official Eli URLs.

## 2:00–2:20 — Negative case
Prompt:
“What's the weather in Amsterdam tomorrow?”

Show that Eli does not need to activate for an unrelated request.

## 2:20–end — Safety
Say:
“The public Eli plugin is read-only, requires no Eli account, and uses public evidence. Authenticated customer data and write actions are not exposed in this initial public submission.”

Upload the finished recording somewhere a reviewer can open without signing in, then add that URL to the Review details in the OpenAI submission portal or to `review.demo_recording_url` in plugin.json.
