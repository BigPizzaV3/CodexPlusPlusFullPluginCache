# Presenting FifthRow results

LCM stands for Large Consulting Model, FifthRow's consulting-agent platform.

Answer in the user's language. Give a useful summary, dates, units and limitations. Include the exact returned platform detail/result link. Cards may be hidden inside a trace, so important state, links, findings and problems must also appear in normal chat text.

## Background status in chat

After acceptance briefly say what is running and that you are waiting for its result, using actual returned status and `display_summary`. Before a long host-held call, explain pending work when the duration is known. When native MCP Tasks, a host monitor or an automatic card notification delivers completion, update the chat with the outcome and useful findings. Do not require another user status phrase, narrate unchanged polls, or claim a card is visible. Silent card context does not wake the model; automatic delivery needs native tasks, host monitoring or a mounted card with supported host messaging.

Acceptance is not completion. Follow the existing IDs and read-only `next_step` through native tasks or a supported background monitor. Native tracking has a 24-hour limit and 48-hour task/result retention; a limit response resumes through the same status ID, never a new run. Foreground/card reads are snapshots. No sleep/poll loops in the main chat. Keep stages and measured Flow counts separate from labelled time estimates. An Agent step commonly takes ten minutes and a multi-step App can take more than thirty minutes. Output availability or all members ending may precede overall finalization; use the actual terminal status. Failed/stopped work can have useful partial output; label it honestly.

## Exact platform links

Use returned `url`, `result_url`, `autopilot_url`, `execution.link` or an authorized builder template link. Label App workflow, App result and Autopilot schedule separately. Preserve the environment and company origin. Never use a dashboard link for a detail page. Template pages use the returned slug; execution pages use the execution UUID. An Autopilot schedule UUID differs from its invocation UUID. LCM Answers execution/stored-answer IDs are incompatible with the platform's Pathfinder `/answers/{conversation_id}` route; present the answer and sources without fabricating that URL. See `get_lcm_guidance(topic="platform-links")` for the complete route table.

## Source references and full outputs

Cite original sources near every material claim, statistic, date, comparison and table row. Use multiple independent references when relevant; include a Source column for comparisons. Preserve original Markdown links, source labels and footnote definitions. The App/report link opens the deliverable and does not replace its underlying evidence. Never invent citations or strengthen an automated relevance/quality/claim-support score into a correctness guarantee. Report potential hallucination flags and important evaluator feedback when they affect the conclusion.

`get_app_run(detail_level="full")` returns visible output references and small reports inline. Follow `outputs_next_page` for further visible members, then `output_ref` and `read_run_output` pages. `read_document` has the same lossless page contract. Keep `expected_version` and restart from zero on conflict. Content pages preserve original text and citations; they are not summaries or complete reports until all requested pages are read. For very large reports select relevant sections and disclose coverage. Content paging starts no new work and needs no sleep.

## Follow-up scope

Medium/large analyses, including TAM/SAM/SOM, start with App discovery; create an App when none fits. Answers serves requested simple, narrow, one-off questions. After a lightweight answer offer deeper App research only when it adds relevant value. Present at most two related actions, honor prior authorization, respect declined offers and never automatically execute suggestions. A direct authorized Stop run click stops only the existing App/standalone Flow; schedule settings stay unchanged. Never expose internal reasoning, prompts, credentials or raw configuration.
