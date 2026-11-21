---
name: review-a-communication
description: Review, proofread, score or improve an existing customer communication (an email, letter, text message, notice, web or app page, headline, tagline or other marketing copy, or policy wording) against a brand's voice with CommScore, then explain the result and offer fixes. Use whenever the user shares customer-facing text and asks whether it is clear, on brand, good enough or ready to send, asks you to proofread or check it, wants feedback, a score or a second opinion, or wants to compare or choose between versions, for their own organisation or any brand set up in their CommScore workspace, even if they don't mention CommScore.
---

# Review a communication

CommScore scores a communication against the organisation's own brand guide on five
pillars and names the specific things to fix. That gives the user consistent, evidence-based
feedback: the same checks every time, tied to their brand rather than to general taste.
Your job is to run the review, explain it in plain words and help the user act on it.

## 1. Find the brand

- If this conversation already has a brand_id, use it.
- Otherwise call `list_brands`.
  - One brand: use it.
  - Several brands: pick from context, such as the sender, signature, product or website
    in the text. If it's still unclear, ask one short question listing the brand names.

## 2. Score the text as it is

Score exactly what the user gave you. Don't tidy it up first, or the score describes your
version instead of theirs.

Call `score_text` with the text. Set `communication_type` from what it is (email, letter,
newsletter, invitation, text_message or document). Set `audience_rank` (1 = general public,
5 = specialists) and `action_expected` when they're clear from the text or the
conversation. Scoring takes up to a minute and uses the workspace's AI credits.

If the text is longer than the limit the tool reports, split it at natural sections and
score each one.

## 3. Report

Keep it short and concrete:

```
**<Brand>: 3.4 / 5 overall.** <headline from the result>

| Pillar | Score |
|---|---|
| Clarity | 3.5 |
| Certainty | 2.5 |
| Structure, style & grammar | 4.0 |
| Brand alignment | 3.5 |
| Customer experience | 3.5 |

**What to fix first**
1. **Certainty:** <finding, in plain words>. *"<evidence quoted from the text>"*.
   Try: <a concrete rewrite of that sentence>
2. ...
```

- Present scores as guidance, not pass/fail. They run from 1 to 5 (higher is better).
  Longer texts can vary by about a point between runs.
- Quote the evidence so the user can find the sentence.
- **Every fix ends with replacement wording the user can paste**, not just a description of
  the problem. For example, write *Try: "If you go over the limit, replies slow down until
  your next billing date."*, not "explain what happens at the limit". If the right wording
  depends on a fact you don't have, use a placeholder such as `[new limit]`.
- Review, don't rewrite: unless the user asked for a fixed version, give the fixes and
  offer the rewrite (step 4) rather than rewriting the whole text.
- Mention `reading_grade` when the audience is the general public: a lower grade is easier
  for more people to read.
- If `check_terminology` would add something (the brand has avoid terms and the text may
  use them), run it too. It is instant and free. List any avoided terms with their
  alternatives.

What the pillars mean, for explaining scores in plain words:

- **Clarity:** easy to understand at first read.
- **Certainty:** the reader knows what is happening, what to do and by when.
- **Structure, style & grammar:** well organised, correct and in house style.
- **Brand alignment:** sounds like the organisation and uses its words.
- **Customer experience:** how the message feels to the person receiving it.

## 4. Offer the fix

End by offering to fix it, e.g. "Want me to rewrite it with these fixes?" If the user says
yes:

1. Edit the text yourself, or call `rewrite_text` with `focus` set to `suggested_focus`.
2. Check that every fact, amount, date and legally required wording from the original
   survived, and that you added no new promises, deadlines or instructions the original
   didn't make. Use a placeholder or suggest them to the user instead.
3. Score the final text again with the original score's `draft.draft_id` as `draft_id`,
   and show before → after for the overall score and any pillar that moved (from
   `draft.change`), with the new text ready to copy. If you edit after that score, score
   again: the score you show must belong to the text you hand over.

## Comparing versions

When the user wants to compare drafts (theirs vs a colleague's, before vs after):

- Score each one with the same `communication_type`, `audience_rank` and
  `action_expected`, as separate drafts (no `draft_id`), each with a short `title` such
  as "Price notice A".
- Show the scores side by side.
- Say which fixes differ between the versions.
- Treat small overall differences as a tie. Look at whether the top fixes changed instead.

## Earlier scores

If the user asks how a communication improved, what they scored recently, or wants to
pick up a draft from an earlier conversation, call `get_score_history`. It is instant
and free, and shows only their own scores, including documents scored in the CommScore
Office add-in. To score a new version of one of their drafts, pass its id as `draft_id`.

## When something goes wrong

- **Access, licence or credit messages** from a tool: pass them on as written, because
  they say what the user or their admin can do. Offer your own read of the text, clearly
  labelled as not a CommScore score.
- **No brands in the workspace:** a CommScore admin needs to add one before CommScore can
  score text against it.
