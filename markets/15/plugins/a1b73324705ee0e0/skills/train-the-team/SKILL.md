---
name: train-the-team
description: Onboard and train a restaurant group's team in Excellent — add a new hire to the training roster, build a training course from the group's own lessons and SOPs, define and assign on-the-floor competencies, assign courses and correct a team member's details — each change undoable and each course a draft for a person to publish. Use for "add Maria as a server at the Mission venue", "build a wine-service course from our SOPs", "assign the allergen course to the new bartenders", "add a decanting competency for the bar team", "who's on the training roster?", "put bar opening on Sam's plate".
---

# Train the team

This skill reads the training roster, makes changes in Excellent (each undoable) and drafts courses. It never
publishes a course, signs off a competency or tells staff anything: those stay with a manager in Excellent.

**Before every change,** say exactly what you will change and wait for a yes, unless the person already asked
for that exact change. **After every change,** give the `change_id` it returned and say it can be undone.

## 1. Read the roster

`training_roster` (with `match` to narrow by name) lists the active team members (id, name, role, home venue,
status), the published courses and the competencies, with the ids the steps below take. For course material,
`list_documents` with `type` `lesson`, `sop` or `knowledge`; only finalized ones can join a course. The roster
does not show course progress or scores: for those, send the person to the roster in Excellent rather than
guessing.

## 2. Onboard someone

1. `add_staff_member` with `full_name` and what the person gives: `email`, `phone`, `employee_ref`,
   `started_on`, `role` (server, bartender, host, busser, runner, line_cook, prep_cook, dishwasher, sous_chef,
   chef or manager), home venue `location` (from `overview`) and a free-text `position`. The courses the
   group's standing rules give that role or venue are assigned at once: say which ones came back.
2. Anything else: agree who gets what and by when, and read the list back (each person, the course or
   competency, the due date). Then `assign_course` with the `staff_id`, a published `course_id` and an
   optional `due_on`; `assign_competency` the same way with a `competency_id`. One they already have answers
   that assignment and changes nothing.

For a whole staff list at once, stage it as a roster import with the `import-a-list` skill.

## 3. Build a course

Propose an outline first: a title, what it covers, and the finalized documents in order. Then `draft_course`
with `title`, an optional `description`, `passing_score` (a percent) and Spanish `title_es` /
`description_es`, and `items` — 1 to 20 `{ document_id, required }` in order. A document not finalized yet is
refused: a person finalizes it in Excellent first. Give back the review link. The course stays a draft that
nobody is assigned; once a person publishes it in Excellent, it can be assigned (`assign_course`).

## 4. Competencies

A skill a manager signs off in person ("decanting wine"): `create_competency` with `name`, optional `name_es`
and `category` ("Bar"), then `assign_competency` to each person, with an optional `due_on`. The sign-off
happens in Excellent.

## 5. Correct someone's details

`set_staff_details` with the `staff_id` and only the fields that change (`full_name`, `email`, `phone`,
`role`, `location`). A new role or venue can assign the courses its standing rules give: say so before.
Moving an email or phone off a verified sign-in address retires that proof and cannot be undone here: say so
and ask again first.

## 6. Wrap up

List each change with its `change_id`, and each course's review link. End with: "Each change can be undone
(ask me, or say undo); a course reaches staff only once it is published in Excellent and assigned."

Safety: no change is made without the person's yes, and each returns a `change_id` that `undo` puts back, once,
for 30 days unless the record has changed since (`recent_changes` lists them). A course waits behind its review
link. Nobody is messaged from ChatGPT, no sign-off is recorded and nothing is deleted.
