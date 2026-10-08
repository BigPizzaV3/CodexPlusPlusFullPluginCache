---
name: youtube-help
description: Explain what this Windsor.ai app for YouTube analytics covers (read-only channel and video performance for the user's own channels), what it does not (publishing, editing, YouTube Ads, other channels' data), and which skill handles a request. Use when the user asks what the app can do or asks for something outside its scope.
---

# What this app can do

This app reads analytics for the user's own connected YouTube channels through Windsor.ai (connector id `youtube`): views, watch time, average view duration, subscribers gained and lost, likes, comments, shares, and traffic sources, per channel, per video, and by day, week, or month. It is read-only. It does not publish or edit videos, change channel settings, manage comments, read other channels' public statistics, or report YouTube Ads spend (that is Google Ads, covered by the Windsor.ai Google Ads listing).

## Route the request
- Reports, rankings, comparisons, trends -> $youtube-insights
- Connecting, reconnecting, adding a channel, or asking what is connected -> $youtube-connect
- Recurring exports and syncs -> $youtube-export
- What the app covers and does not -> $youtube-help

## Answering "what can you do"
- Call get_connectors with include_not_yet_connected=True and answer from it: which channels are connected and which options exist. Do not list capabilities the tool result does not show.
- Reads are available on the free plan.

## Out of scope
- Data from other platforms: name the Windsor.ai listing that covers them instead of attempting the read.
- Generating thumbnails, titles, or video ideas, general advice unrelated to the connected channels, or anything about plans and pricing.
