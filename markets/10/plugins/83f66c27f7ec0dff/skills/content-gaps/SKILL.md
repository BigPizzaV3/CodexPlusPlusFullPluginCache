---
name: content-gaps
description: Find the questions a brand lacks content for, using 3RD's content recommendations, and what kind of page would close each gap. Use when the user asks what content to write, which questions they are missing, or where their pages fall short.
---

Use this skill to find content gaps.

1. Call `list_brands` and take the `brandId`. Ask which brand if there are several and the user named none.
2. Call `get_content_gaps` with the `brandId`. Pass `topicId` to look at one topic, and `limit` to shorten the list. The list is ordered by opportunity, highest first, as on the Content page in the 3RD app.
3. For each prompt you report, give:
   - the question;
   - how well the brand's own pages cover it (coverage % and matching pages);
   - the recommended action: optimize an existing page, create a new one, or defend;
   - the recommended content type and target URL when there is one.

Coverage describes the brand's pages as they are now; it has no date range, so do not attach another tool's period to it. If the user wants a brief for one of the prompts, `brief_content_gap` writes one with AI generation and saves it for the team, so confirm with the user before calling it.
