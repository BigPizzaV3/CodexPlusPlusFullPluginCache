---
name: build-a-resume
description: Turn a user's experience into a professionally typeset resume in a chosen template. Use when the user wants to make, build, convert, reformat, or "turn this into" a resume.
---

# Building a resume

JobSprout renders resumes through a real typesetting engine (Typst) to a pixel-accurate PDF, and the finished resume lands in an editor the user keeps. The template is chosen visually.

## Workflow

1. Gather the content. Accept pasted text, an uploaded file, or details collected in the conversation. If collecting by conversation, ask section by section (contact, summary, experience, education, skills) and confirm dates and employers with the user.
2. Decide the template path:
   - If the user just wants a resume and has expressed no interest in choosing a design, skip the gallery and call `build_resume` with the content and no `template_id` (a clean default is used, and they can switch the design afterwards).
   - If the user names a design ("use Academic"), skip the gallery and pass that name as `template_id`.
   - If the user wants to choose a design, call `list_resume_templates` with their preferences (one or two columns, photo, clean vs designed). It renders a browsable gallery.
3. **If you showed the gallery, end your turn and wait for the user to choose.** Do NOT call `build_resume` in the same turn, and do NOT pick a template for them. The user chooses by clicking "Use this" on a card (which sends the choice back to you) or by naming a template. Only recommend a template if the user explicitly asks you to, and only one that appears in the gallery.
4. **The moment they choose, call `build_resume` with their choice and the content.** Do not call `list_resume_templates` again to confirm or re-show the choice. Showing the gallery a second time is a failure, not a safe default.
5. The card shows the finished resume with Open in editor and Download PDF. Do not repeat it or write out its links; say in a sentence that it is ready and offer one next step.

## Boundaries

- Never fabricate employment history, titles, or achievements. Build only from what the user provides.
- Never pad or shift dates to fill gaps.
- Recommend only templates returned by `list_resume_templates` in the current conversation.
- Never search for jobs or claim to submit applications.

## Do not trigger on

- Requests to score or critique an existing resume (use **resume-review**).
- Requests to find jobs.
