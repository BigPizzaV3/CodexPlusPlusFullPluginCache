---
name: write-on-brand
description: Write, edit or rewrite customer communications (emails, letters, text messages, push notifications, in-app messages, notices, replies to complaints, help-centre answers, web or app copy, headlines, social posts, policy wording) in a brand's voice using its brand guide in CommScore, and check the result with CommScore before handing it over. Use whenever the user asks you to draft, reply to, edit, rewrite or "make this sound like" a brand or organisation for its customers, members or the public, including any brand set up in their CommScore workspace, even if they don't mention CommScore.
---

# Write on brand

CommScore holds the organisation's brand voice and language guide (tone, style, audiences,
terms to use and avoid) and can score a draft against it. Read the guide before you write
and check the draft afterwards. The user then gets text that already sounds like their
organisation and has been checked, instead of a generic draft they have to fix.

## 1. Find the brand

- If this conversation already has a brand_id, use it.
- Otherwise call `list_brands`.
  - One brand: use it.
  - Several brands: pick from context, such as the organisation, product or website the
    user mentioned. If it's still unclear, ask one short question listing the brand names.
  - Brands with the same name: tell them apart by website. Don't guess.
  - No brands: tell the user a CommScore admin needs to add one first. You can still
    write the draft, but say it hasn't been checked against a brand guide.

## 2. Read the brand guide

Call `get_brand_profile`. Most of what matters for writing is in these fields:

- `preferred_tone`, `core_idea`, values and `customer_charter`: how the organisation wants
  to sound and what it promises customers.
- `style_do` / `style_dont` / `style_checklist`: concrete house-style rules. Follow them
  over your own default style.
- `audiences`: who the brand writes for. Match the reader of this communication.
- `approved_terms`: the brand's own words. Use them. For a general audience, add the
  `plain_explanation` the first time a term appears.
- `avoid_terms`: words the brand doesn't use. Use the alternative given.

## 3. Get the brief straight

Before drafting, be clear on:

- who is reading;
- what they need to know;
- what, if anything, they need to do, and how and by when.

Keep every fact the user gives exactly as given: amounts, dates (in the user's format),
names, reference numbers and any wording they say must stay. If a fact the reader needs is
missing (a date, an amount, a phone number), ask, or leave a clearly marked placeholder
such as `[due date]`. Never invent one. A confident draft with a made-up date is worse than
one with a visible gap.

The same goes for **promises and instructions**. Don't add a commitment the user didn't
make, such as "we'll update you by Friday", "you'll be refunded" or "we'll restore it".
Don't add instructions or warnings to the reader, such as "don't reset your account". A
warmer tone is your job; new obligations are the user's call. If one would help the reader,
suggest it to the user after the draft rather than putting it in.

## 4. Draft

Write the communication in the brand's voice, for the reader in step 3. Put what matters
most to the reader first. If the reader must act, say what to do, how and by when.

## 5. Check before handing over

1. Call `check_terminology` on the draft. It is instant and free. Swap any avoided terms
   it finds.
2. Call `score_text`. Set `communication_type` (email, letter, newsletter, invitation,
   text_message or document). Set `audience_rank` (1 = general public, 5 = specialists)
   and `action_expected` when you know them, because they change what good looks like.
   Scoring takes up to a minute and uses the workspace's AI credits.
   - Score anything that will go to customers.
   - For a quick throwaway line, the terminology check is usually enough.
3. If `top_fixes` point to real problems, fix them. Either:
   - edit the draft yourself, which often works well because you know the intent and the
     facts; or
   - call `rewrite_text` with `focus` set to `suggested_focus`, then check that the
     rewrite kept every fact from step 3.

   Then score once more, passing the first result's `draft.draft_id` as `draft_id`, so
   CommScore links the rounds and the result's `draft.change` shows what moved. Give the
   first score a short `title` (e.g. "Holiday closure email") so the user can find it in
   their history later.

**The score you report must belong to the text you hand over.** If you change the text
after the last score, even a small edit, score it again. If you can't (credits, errors),
say plainly that the score is for the earlier draft.

One improvement round is usually enough; two at most. Scores on longer texts can move by
about a point between runs, so don't spend the user's credits chasing a decimal. Stop when
the remaining fixes are minor or depend on something only the user knows.

## 6. Hand over

Lead with the finished communication, ready to copy. The user asked for the email, not a
report. After it, add a short CommScore note:

```
**CommScore:** 4.3 / 5 overall (first draft 3.6), brand: <brand name>
Clarity 4.5 · Certainty 4.0 · Structure, style & grammar 4.5 · Brand alignment 4.0 · Customer experience 4.5
Still open: <anything you couldn't fix, e.g. "add the actual due date">
```

Skip the "first draft" figure if you only scored once, and drop "Still open" if nothing is
open. If you scored more than once, show the trail from `draft.history`, e.g. `3.6 → 4.3`.

## When something goes wrong

- **Access, licence or credit messages** from a tool: pass the message on as written,
  because it says what the user or their admin can do. Then give the draft written from
  the brand guide, marked as not yet scored.
- **Text too long:** score it in sections and report each section.
- **Several drafts or variants requested** (e.g. an email and an SMS version): read the
  profile once, then write, check and score each variant.
