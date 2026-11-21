---
name: onboarding
description: Immediately acknowledge requests for Marble widget ideas, then show four personalized sample previews and build the one the user chooses.
---

# Set up Marble

As soon as the user asks for onboarding or widget recommendations, send one
short, visible acknowledgment before doing any other work. For example:
"I'm putting together some widget ideas for you now."
The user needs to know their request was received while the previews are being
prepared. Send this acknowledgment before reviewing conversation context,
searching memory, choosing ideas, reading references or schemas, or calling
any tools. Do not wait for tool results or finished previews to send your first
visible response. This is required even when routine progress narration is
otherwise unnecessary. It says work is starting, not that previews are ready.

After the initial acknowledgment, read the installed `marble-widgets` skill
before preparing recommendations or calling tools. Follow its guidance
throughout onboarding and the selected widget build.

Give the user a useful first glimpse of their dashboard. Use the connected Marble tools and the existing widget
formats. Do not launch website research, ask for a company website, or turn
this into a questionnaire.

1. Use what is actually available in this ChatGPT conversation and memory.
   If the host offers memory or past-conversation search, consult recent work
   when useful. Do not invent access to memory or assert personal facts you
   cannot see. Put one or two ideas about the user's immediate work from the
   last week first. Use the remaining ideas for important ongoing needs or
   interests. If little context is available, offer broadly useful starting
   ideas and invite the user to adjust them, without blocking the previews.
2. Read `get_widget_formats`. The formats response
   includes the website's complete `recommendationSchema`, including each
   supported fictional `sampleResult` shape. Use that schema for the previews;
   do not retrieve individual canonical format schemas just to show ideas.
   Choose a presentation supported by `recommendationSchema`, including charts
   when the sample schema supports them.
   Give each idea a source with `source: {kind: "external", name, domain?}`.
   Marble uses that domain to look up the logo displayed on the sample widget.
   Label the platform or service whose data the card displays, following
   `marble-widgets`'s source-name and logo guidance. For Instagram content,
   use `name: "Instagram", domain: "instagram.com"`, even when Apify retrieves it.
   Choose sources the user's available authorized tools can retrieve, and omit
   unknown domains. Do not run data tools or call `list_connections` to generate
   ideas.
3. Call `show_widget_recommendations` with exactly four distinct `kind=custom`
   recommendations matching `recommendationSchema`. Include a clear name,
   a short explanation of its usefulness, self-contained refresh instructions,
   a named source, and a small fictional `sampleResult`. Use one feed item
   or calendar event, one or two standalone measurements, or a short chart
   with at most four points. Keep previews compact. Use example.com for
   fictional links. Never present sample data as actual account data or as
   research findings. Do not open drafts, fetch live data or save four widgets.
   Correct rejected arguments and retry rather than claiming a carousel was
   shown when the tool failed.
4. The inline carousel reuses Marble's existing widget previews. Its
   **Make this widget** button sends the chosen idea back into this chat.
   Explicitly say they can request anything else they can think of, not just
   these four ideas. If they share a vague idea, ask focused clarifying
   questions to work out the widget before building. On selection, immediately
   acknowledge the build before tool calls, following `marble-widgets`'s
   acknowledgment guidance. Then use the authorized source tools,
   read the chosen format's full canonical schema, fetch real data, validate
   and save that one widget. The fictional sample schema does not replace the
   live widget format schema. Never save fictional sample data as a live widget.
5. Stop after the ideas and invitation until the user chooses a widget or
   describes what they want. After saving, follow the short saved-widget reply
   below. Keep the existing inline widget visible; it follows the draft through
   save. Do not call `open_chat_dashboard` automatically or capture a second
   preview. Open the full dashboard only when the user asks.

## Keep attention on the widgets

The cards are the explanation. Do not repeat their names, descriptions, sample
values or contents in a numbered list or paragraph beneath them. Do not narrate
routine tool calls or say that you started onboarding or loaded four ideas.
Always give the initial recommendation acknowledgment above, and the build
acknowledgment when the user chooses a widget. After that,
give progress only when a delay, error or required choice needs explanation.

After a successful carousel call, use at most two short sentences:
"These previews use example data. Pick **Make this widget**, or tell me another
widget you'd like."
That is the invitation to request anything else they can think of; do not add
a second invitation or explain the build/save process again. If the carousel
fails, explain the problem instead of claiming previews are visible.

When real data is passed to Marble's widget tools, the widget shows a preview
of that data inline in the chat. For previewing data for a Marble widget, that
inline widget preview is usually enough. Let it show the data and its saved
presentation while keeping the accompanying explanation brief.

After a successful save, use at most three short sentences:
- Confirm the widget name was saved, once. Follow `marble-widgets`'s board-only
  saved-widget wording. Never claim a save succeeded before the tool does.
- Add one useful detail only if it is not already clear from the card, such as
  "Links open the Hacker News discussions." Do not list articles, links,
  measurements, engagement counts or other contents already in the widget.
- For the first saved widget, explain the control in plain language:
  "To update its data, open the widget's **⋮** menu and choose **Refresh now**."
  Do not call it a "snapshot" or imply its data updates on its own.
  Do not mention automatic refresh, disabled schedules or internal refresh
  policy unless the user asks about them. The menu icon is vertical **⋮**.
- Follow `marble-widgets`'s dashboard-navigation guidance: retain the inline
  card's **View in dashboard** control. Keep it as the dashboard entry point
  without adding a dashboard link to the assistant's reply.

An optional next step can be one short suggestion, such as "Want to focus it on
Show HN launches?" Omit it if the reply already needs the refresh explanation.
Do not add a general feature tour, a repeated saved badge, or a second summary.

## Source names and logos

Follow the **Source names and logos** guidance in `marble-widgets` for both
recommendation cards and drafts. Source names and domains describe the content
platform; retrieval requirements belong in the widget instructions. Omit unknown
domains. Do not fetch image files or call `list_connections` just for a logo.
