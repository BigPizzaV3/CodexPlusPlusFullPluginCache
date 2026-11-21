---
name: get-started
description: Use when someone asks about their Conveo studies, wants to design a new interview study, check recruitment, or analyze what participants said in Conveo interviews.
---

# Working with Conveo

Conveo runs AI-moderated video interviews. A **study** has a topic guide made of
**sections**, each holding **questions**. Participants are recruited into the
study, and every completed conversation is an **interview**.

## Find the study first

Most requests name a study loosely ("my coffee study"). `list_studies` has no
name search: it pages through studies newest first, so read the titles and
match them yourself. If more than one study matches, ask which one — never
guess between them.

## Analyzing results

- `query_study_data` takes no study ID; it always runs inside an analysis
  session. Create one with `create_analysis_session` (pass the study's ID in
  `studyIds`), then pass the returned session ID and the question to
  `query_study_data`.
- Ask follow-up questions in the same session — it keeps the conversation.
  Each query runs a full analysis, can take a few minutes, and counts as one
  analysis query for the organization.
- The answer is markdown `text`, plus `quotes`, `tables` and `charts` when the
  analyst produced them. Replace a `[ref:message:<id>]` marker with the quote
  whose `messageId` matches, and `[chart:<id>]` / `[table:<id>]` with the item
  whose `id` matches; drop a marker with no match. Never show raw markers.
- No tool counts how many participants support a single finding. Don't invent
  one — rely on what the analyst's text says.
- To resume earlier work, find the session with `list_analysis_sessions` and
  re-read it with `get_analysis_session_messages` instead of asking again.
- If the study belongs to an Always-On storyline (a wave-based program), find
  it with `list_storylines` and read its findings with
  `list_storyline_insights` before running a new analysis. Ordinary studies
  have no storyline.

## Finding clips

`search_clips` matches a literal keyword (case-insensitive) in the quotes
Conveo has already extracted from completed video interviews — not full
transcripts, and not by meaning — so try related words too (price, cost,
expensive). No results doesn't mean nobody said it: fall back to
`query_study_data`. Results carry the quoted text and interview reference, but
no link to the moment in Conveo — don't promise one.

## Designing a study

- Create it with `create_study`. Only `title` is required. It returns the
  study's ID and slug, not a link.
- Every new study is section-based. Build the interview with `add_section`,
  then add questions with `add_question`, passing the section's ID as
  `sectionId`. `type` defaults to open-ended.
- A new study comes with a "Screener" section (`type: "screener"`) and one
  empty, untitled interview section (`type: "userCreated"`). Find the untitled
  one with `get_study` and name it with `update_section` rather than leaving
  it blank. Don't rename the Screener or put interview questions in it.
- Research objectives are analytical only: they record what the analysis
  should answer and hold no questions. Don't use `add_research_objective` to
  structure the interview, and never pass an objective ID to `add_question`
  in a section-based study — the call fails. (Some older studies have
  `isSectionBased: false`; there `get_study` lists the topic guide under
  `researchObjectives`, and questions are added with that objective's ID.)
- Write questions that are open and non-leading ("Tell me about the last time
  you…" rather than "Did you like…").
- These tools cannot launch a study or recruit anyone. Tell the user to open
  the study in Conveo to review and launch it.

## Recruitment

`get_recruitment_overview` reports interview counts by status (completed,
ongoing, screened out, abandoned) and each quota group's configured targets.
It does not report how full each quota is, so describe overall progress and
the quota setup — never per-quota progress.

## What Conveo does not share

Conveo never returns participants' contact details. If asked for emails or
phone numbers, explain that and offer what is available instead.
