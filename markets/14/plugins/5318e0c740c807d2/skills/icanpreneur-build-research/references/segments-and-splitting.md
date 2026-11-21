# Segment fit and splitting

Evidence can show that an interviewee is not in the segment they were planned for, or that one segment contains distinct sub-groups. Watch for both while reading interviews and insights. Acting on it reorganizes research, so propose it first and wait for the user's agreement.

**How the evidence is organized.** Research membership decides which interviews contribute to a research's analysis. A research has a default script, but its interviews may have used other scripts. A contact's customer segments are optional and do not decide whether the contact's interviews can join a research. Existing interviews are reused. Nothing needs to be re-interviewed, re-scripted or duplicated, and contacts do not have to be updated.

**Recognize it from what was said.**

- _Not a fit_: the respondent's own words, job or situation show they do not share the segment's job-to-be-done or context (read the contact's fields and the transcript). Base it on real or imported interviews. A synthetic respondent not fitting says something about the generated profile, not about the segment.
- _Sub-segments_: real respondents separate into groups whose problems, triggers, alternatives or decision criteria differ, and each group would need a different message or channel. One unusual interview is not a sub-segment. Synthetic material can suggest a split to test but cannot establish one.
- **Fit follows the segment criteria, never the feedback.** A respondent who rejects the offer, dislikes the idea or gives negative answers may fit the segment perfectly. Judge fit only by whether they match the segment definition (`icanpreneur` → `references/definitions.md`). Do not call someone a non-fit because they disagree, and do not move people to make the evidence look better.

**Keep splits rare and worth it.** The aim is the fewest segments that still preserve meaningful differences in customer needs, buying behavior and the actions the business should take. More segments mean more research, scripts, analysis, credits and thinner evidence per segment.

- Split only when the difference would change a decision: a different message, channel, offer or thing to test. If it is interesting but would not change what the user does, record it as an insight or note inside the existing segment.
- First check whether an existing segment (or an existing note) already captures the distinction. Read `get_canvas` and the notes on segment decisions before proposing anything. If there are already more segments than the user is actively researching, say so and suggest focusing.
- Weigh the strength of the evidence, not a count: the quality of the interviews, whether the sources are independent, and how much the distinction matters. Treat an emerging sub-group as provisional: describe it as a hypothesis with its evidence and do not create a segment automatically, but do not rule it out either. If the user asks to explore a sub-segment, create it and say what rests on how little evidence.
- Propose the smallest coherent restructuring that resolves the decision. Do not propose further splits unless materially new evidence or a different decision justifies them. Offer to save the reasoning as a note so later conversations do not rediscover the same proposal.

**Propose, with the evidence.** Show who is affected and why, citing the source interviews, the wording of each proposed segment (tested against the platform definition), which existing interviews would join which research, what would be removed from the original research, and what uses credits (automatic analysis and persona refresh). Wait for the user's agreement.

**Carry it out, within what the user authorized.**

1. Create the segments the agreed restructuring needs (`create_canvas_customer_segment`), only where the evidence supports them. Keep the original segment. Do not delete it; deleting a segment can affect linked work; the MCP contract does not guarantee a complete deletion or restoration cascade.
2. Create research for each new segment (SKILL.md §4). Reuse or generate a script for it (SKILL.md §3). The script is the research's default and does not limit which interviews can join. Do not duplicate the old script just to get one.
3. Associate the relevant existing interviews with each research. Search the workspace's existing interviews with `list_interviews` without filtering by the new segment's ID (use `notInResearchId` for the target research if helpful), because that filter can hide the very interviews being reorganized. Choose by content and fit, then use `update_research_interviews`. An interview can belong to several research projects.
4. Remove interviews from the original research only when that is appropriate and the user has agreed. Removal takes them out of that analysis and does not delete them.
5. Let the affected analyses and Buyer Personas refresh, then report each research separately: counts by real, imported and synthetic, analysis status and `updatedOn`. A new `BuyerPersona` research creates its own persona automatically; say so and say which persona later work should use. A new research that has no interviews yet has no associated interviews, which is different from the segment lacking supporting evidence: say which it is.
6. Contact segment links (`update_contact.customerSegmentIds`) are optional and replace the entire list for real contacts. Do them only if the user asks. Synthetic contacts cannot change their segment links.
7. Prepare new interviews only if the user included them in the scope.

The interview and research must belong to the same workspace; their segments, scripts and interview types may differ. If membership is rejected, report the message and stop the dependent step. Do not work around a rejection by changing scripts, re-importing transcripts or duplicating interviews.

An interview has one analysis with cached insights per research type. A new type triggers secondary insight extraction. Removing membership can refresh or clear aggregate research analysis and refresh/empty its persona; it keeps the interview and cached insights. After changing membership, read status and content again. `updatedOn` is a modification time, not proof that a completed refresh includes the change.
