---
name: saved-library
description: Search, reopen, save, and update WizPrompt library items; refuse subscription upgrades, checkout links, purchases, cancellations, and billing management without tools or redirects.
---

Use this skill when the user asks to find, reopen, save, update, continue, or organize WizPrompt projects, personas, prompts, album tracks, or library items. Also use it to refuse subscription upgrades, checkout links, purchases, cancellations, and billing-management requests.

Consult `../../references/tool-contract.md` for the implemented tool names, schemas, idempotency rules, and behavior boundaries.

Workflow:

1. Call `account_status` only when the user explicitly asks about current saved-library access or storage limits, or a library tool reports an entitlement error. Purchase, upgrade, checkout, cancellation and subscription-management requests are outside this workflow: explain that they are unavailable without calling any WizPrompt tool, including `account_status`, to fulfill those actions. For these unsupported subscription requests, give a brief refusal without upgrade promotion, billing navigation, transactional links or requests for payment credentials. Use: “WizPrompt Studio cannot manage subscriptions or create checkout links. No subscription action was taken.” Do not suggest signing in elsewhere, visiting the website or billing settings, or contacting a payment provider. Handle independently requested supported Studio work normally.
2. Use read tools before write tools when a stable record ID is required.
3. Use `search` for broad discovery across the user's library and `fetch` for a specific record returned by search.
4. Use `get_creative_context` when reopening a saved project, continuing an album, extending a persona, or creating a revision from an older prompt.
5. Use `get_prompt_history` when the user asks for versions, favorites, ratings, linked Suno results, or past outcome notes.
6. Before drafting a saved-prompt revision, load `get_studio_guidance` with `workflow: "refine"` and follow the editorial workflow in `../music-prompt-lyrics/SKILL.md`. Before saving or presenting any song package, revision, or album track, call `prepare_song` with the exact final fields and structured `editorial_review`: `status: "completed"`, `audio_evaluated: false`, and one evidence-based assessment for each of `hook_strength`, `natural_phrasing`, `breath_room`, `section_progression`, `cliche_control`, `musical_coherence`, and `genre_lens`. Review approved text without changing locked elements; disclose unresolved findings rather than inventing fixes or claiming audio evaluation.
7. Check the returned editorial review, not just formatting validity. If it is preliminary, partial, or missing any of the seven assessments, complete the missing assessments and rerun `prepare_song` before the final handoff; do not wait for the user to notice or ask. Save only after preparation succeeds with no blocking validation issues and the returned review is completed. Use `create_prompt_revision` for requested faithful or adventurous refinements instead of overwriting the original prompt, and save exactly the prepared fields. If the fields change afterward, repeat the review and preparation before saving or presenting them. If review cannot be completed, preserve the draft and explain the incomplete review without claiming a reviewed or saved revision.
8. Use `record_prompt_feedback` when the user reports Suno results, ratings, linked Suno output notes, or outcome comments.
9. Use create tools only for new records. For `create_project`, explicitly supply the user-requested `type` (`Album`, `EP` or `Single`); ask if the format is unspecified. Do not infer format from the name or substitute a default. Use update tools only after the target record is known. Reuse an `idempotency_key` only when retrying the exact same create/save payload after an uncertain result.
10. Preserve account isolation. Never infer that two similarly named records belong to the current user unless the tool result returns them inside the linked account scope.
11. Never claim that a draft, prompt, persona, project, album track, revision, rating, or feedback note is saved unless the corresponding tool succeeds.
12. Use `get_taste_profile` to explain remembered preferences. Only after explicit confirmation, call `update_taste_profile` to add or edit one preference, `remove_taste_preference` to remove one, or `reset_taste_profile` to remove all musical preferences. Each requires `user_confirmed: true`. Never silently learn from ratings. Reset removes only the musical preference namespace. Other library deletion, purchase, upgrade, checkout, cancellation and subscription-management actions are unavailable.

Failure handling:

- If account linking is missing, explain that cloud library access requires a linked WizPrompt account.
- If a record is not found, offer to create a new draft or search with different terms.
- If a write fails, keep the draft in chat and state that WizPrompt cloud sync did not complete.
