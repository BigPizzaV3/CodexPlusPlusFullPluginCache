---
name: lesson-planning
description: Create a Planit Teachers lesson, presentation, worksheet or homework for a topic and age group using the teacher's connected account and existing credits, then inspect and adapt the result.
---

Privacy boundary: this public plugin is for adult educators and creators. Never
transmit personal information about children under 13 to OpenAI. Use anonymous
or synthetic inputs only; do not request, send or retrieve pupil names, pupil
ids, rosters, photographs, scripts, individual answers or individual results.
Apply this boundary whenever ages or identifiability are uncertain. Do not
open, screenshot, upload or read back private pupil records through a browser
or another connector. Give the exact native link and hand the sensitive step
to the adult user to complete independently. Do not read a record first merely
to decide whether it contains personal information.

Use these workflows only for anonymous or synthetic teaching content. Do not
read an existing resource of uncertain privacy merely to check or sanitise it.
If it may contain pupil identities, scripts or individual answers/results,
return its native link and hand it to the adult without browser readback.

Resolve the topic, age/year group, country/curriculum and requested language.
Use stated context rather than asking again. Country-specific year groups and
standards must agree; use `lookup_curriculum_standards` when alignment matters.
Use `search_teaching_guides` or `search_planit_knowledge` for relevant published
guidance and read the selected source before relying on it.

For a multi-lesson sequence, use teaching-workspaces and its units reference
to save the exact teacher-approved outline and manage owned links. Outline
saving creates no lesson decks. Quote and generate only the teacher's selected
resources through the operations below, then attach their actual ids.

For account actions, use Planit's OAuth connection. Never solicit a password,
API key or access token in chat. `get_account` gives existing access and credit
information; feature guards remain authoritative. The plugin and a ChatGPT
subscription do not grant a Planit subscription.

Before creating a lesson, call `quote_action` with `action: lesson`, the exact
slide count and requested worksheet/homework switches. `quote_lesson` is a
standard-lesson quote only. Tell the teacher the returned credit cost. A
request to create a lesson authorises the requested creation, within the
available account access; avoid additional unrequested metered generations.
If account:read is unavailable, describe that the action uses existing credits
and let OAuth request the appropriate scope when needed.

`include_worksheet` and `include_homework` control instruction slides within
the lesson deck; the associated resources are still generated. Do not claim
that false suppresses those resources or their native costs. Use the actual
quote and explain any difference from the teacher's requested output.

Call `create_lesson` with the brief. Include worksheet/homework switches and
specific instructions when requested. Save the returned lesson id and URL.
If the result is `awaiting_plan` or `awaiting_account`, with
`generationStarted:false` or `pollingRecommended:false`, generation has not
started. Stop polling, explain the actual access restriction neutrally and
return that existing lesson's exact editor URL. Resume status checks only
after account access changes; do not create another lesson or offer a
subscription/checkout. A missing status tool is not permission to invent one.
Poll `get_lesson_status` every 15–30 seconds, at most eight times per attempt.
If still generating, give the existing lesson link and status. Never create a
second lesson just because an earlier call timed out. On an uncertain failure,
check `list_my_lessons` and the original status before attempting a retry.
The status read can also return a genuine awaiting state; apply the same stop
rule. A denied/unavailable read is an error, not proof that generation began.

When ready, read `get_lesson_markdown` and `list_lesson_outputs`. Check that the
content fits the brief, the language, the learning objective, and the year
group; inspect each output's status. Use the resource-editing skill for
requested changes and exports.

For a stand-alone worksheet/homework, quote worksheet/homework then use
`create_worksheet`. Read `get_worksheet` to inspect it and use its returned
native editor link. A free classroom-tool sheet uses the classroom-tools
skill's individually exposed deterministic preview/export operations when
available, or its exact native editor. Use that when the teacher wants an
available free option.

Finish with the actual lesson/worksheet link and a concise description of what
is ready. Link specific resources, not the homepage. Existing-credit costs,
feature restrictions and allowance refresh times may be explained neutrally.
Do not offer subscription plans, promote upgrades or initiate purchases.
