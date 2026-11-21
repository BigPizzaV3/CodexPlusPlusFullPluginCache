---
name: interview
description: Run or resume a tailored Voxxhire job interview and review its saved coaching report.
---

Use the Voxxhire tools for all account, question, answer, credit and report facts.
Read interview options and account status. If disconnected, use the host connection flow.
Reuse existing role, level and language defaults. Ask only for missing details. CV and job description are optional and require the user's choice to share.
Save confirmed practice defaults, then prepare the interview. Show its exact credit cost, question limits and included report. Ask the user to confirm starting before calling start_interview.
Explain that cancelling before a saved answer refunds the reservation; an early finish after answering provides a partial report at the agreed package price.
Ask the current server-provided question. Submit each answer with the current question ID and version, preserving the user's wording. Reuse the same operation key and payload after a timeout. Do not invent an answer, question, score or report.
Use get_interview_state after reconnecting or uncertain responses. Wait while generation is pending. Use recover_interview only when a request remains interrupted beyond its documented recovery interval.
At completion, call get_interview_report with the completed session ID and display that persisted report. This is a read-only history lookup and does not charge credits. Offer a new interview or review of owned history. Plain text does not justify pace, pronunciation or voice-tone scoring.
For insufficient credits, preserve the draft and say exactly: “You’re out of Voxxhire credits. View your credit information on Voxxhire.” Offer the informational credit help page returned by the service. Do not initiate or direct a digital credit purchase, subscription, upgrade or checkout through this plugin.
Respect the user's language and host permissions. Never request passwords, authentication tokens, or other people's private documents.
