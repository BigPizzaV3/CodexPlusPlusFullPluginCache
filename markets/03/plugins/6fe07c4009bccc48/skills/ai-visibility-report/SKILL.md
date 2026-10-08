---
name: ai-visibility-report
description: Report how a brand appears in AI assistant answers (ChatGPT, Perplexity, Gemini, Claude, Google AI). Use for AI visibility, AI search ranking, share of voice in AI answers, tracked prompts, running a visibility scan, competitor comparison in AI results, or sentiment in AI answers. Do not use for classic Google rankings, clicks or impressions, which belong to google-search-console-report.
---

# AI visibility report

Answer the question "when someone asks an AI assistant about this category, does the brand come up, and how does it compare to competitors?"

Every tool here is scoped to one brand and takes `brand_id`.

## Step 1: resolve the brand

Call `list_brands`. It is the only tool that takes no id, so it is always the entry point.

- One brand: use it.
- Several: ask which one, listing name and website. Never guess.
- None: tell the user to create a brand at /dashboard/brands and stop.

Keep `brand_id` for every later call.

## Step 2: establish what is tracked

Call `list_tracked_prompts` with `brand_id`.

A tracked prompt is a question a real buyer would type into an AI assistant, for example "best AI SEO tool for agencies". Visibility is measured against these, so if there are none, there is nothing to report.

If the list is empty:
1. Call `suggest_tracking_prompts` to propose prompts from the brand's site and category.
2. Show the suggestions and ask which to track. Do not track them silently.
3. Call `create_tracked_prompts` with the approved list.
4. Say that results appear only after a scan, then go to step 3.

## Step 3: decide whether to scan

Scans cost credits and take minutes, so do not scan by reflex.

Call `get_visibility_overview` first. If it returns recent results, report those.

Scan only when the user asks for fresh data, or the newest result is stale for their purpose.

Before a large scan, call `get_workspace_details` to check the plan's remaining usage. Telling the user they are out of credits before a scan is useful. Discovering it halfway through is not.

To scan:

1. Call `run_prompt_scan` with the `prompt_ids` to scan.
2. Poll `get_scan_status` with the returned `scan_id`. Do not poll faster than every 20 seconds.
3. When it completes, call `get_scan_results`.

If the user changes their mind, `cancel_prompt_scan` stops it. `list_scans` shows scan history.

## Step 4: assemble the report

Combine these, skipping any that return nothing rather than padding the report:

- `get_visibility_overview` for the headline: how often the brand appears across tracked prompts.
- `get_prompt_analytics` for per prompt detail, including which prompts the brand loses.
- `get_competitor_analysis` for how rivals place on the same prompts. Manage the comparison set with `manage_tracked_competitors`.
- `get_sentiment_analysis` for how the brand is characterised when it does appear.
- `get_visibility_insights` for the specific gaps worth acting on.

## Step 5: report honestly

Lead with the number the user cares about: the share of tracked prompts where the brand appears.

Rules:

- 0% visibility is a real, common and useful finding. Report it plainly. Never soften it and never present an absence of data as if it were zero visibility, or the reverse.
- Never invent a trend. A single scan is a point, not a direction. Only describe movement when two or more scans exist.
- Name the engines the result covers. Visibility differs sharply between assistants, so an aggregate alone can mislead.
- Attribute every number to the prompt it came from, so the user can verify it.

Close with the two or three highest value actions from `get_visibility_insights`. Where an insight has been acted on, `update_visibility_opportunity` records that.

## Boundaries

- Do not create, edit or delete tracked prompts without explicit approval. `update_tracked_prompt` and `delete_tracked_prompt` change what is measured, which breaks comparability with earlier scans.
- Do not start a scan without saying it consumes credits.
- If the user wants content written to close a gap, hand off to the content-production skill rather than doing it here.
