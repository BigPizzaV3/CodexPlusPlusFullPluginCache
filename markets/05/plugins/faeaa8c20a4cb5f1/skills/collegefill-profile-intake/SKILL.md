---
name: collegefill-profile-intake
description: Prepare or revise canonical CollegeFill Master Profile JSON from student-provided records, while asking the minimum routing questions and reporting Common App or UC gaps. Use for CollegeFill JSON creation, document or screenshot intake, and target-readiness review; not for logging in to, filling, saving, or submitting an application website.
---

# CollegeFill Profile Intake

Produce one canonical CollegeFill Master Profile JSON file that the student can manually import into CollegeFill. Do not create an Excel, CSV, SQL, or alternate profile file.

## Intake workflow

1. Before preparing the profile, determine whether the student is preparing for **Common App**, **UC**, or **both**. Ask once if the target is not already explicit.
2. Extract only information the student supplied explicitly in text or source documents. Never infer, copy, calculate, or invent student data when the source is ambiguous. Normalize only documented CollegeFill aliases when the mapping is deterministic and preserves the student's meaning; otherwise ask.
3. Resolve the historical-course gate below before presenting or downloading final JSON.
4. Do not call `create_master_profile` until the target is explicit. Then call it with the supported information and set `application_target` to the student's confirmed `common_app`, `uc`, or `both` selection. Never infer or default this argument. The server's missing-target response is a safeguard, not the normal intake path; if it is returned, ask the target question and do not present profile JSON.
5. Call `validate_master_profile` on the returned `masterProfile`. Continue with the validated canonical `masterProfile`; do not deliver structurally invalid JSON.
6. Run the matching readiness check on that validated profile:
   - Common App: `prepare_common_app_profile`
   - UC: `prepare_uc_profile`
   - Both: call both tools with the same canonical profile.
7. Combine the tools' missing-field findings into one concise batch grouped by record and target. Include only target-specific findings for the target or targets the student selected; do not ask a UC-only student for Common App-only details, or the reverse.
   - For warnings, ask whether the student wants to supply the information now or leave it blank and complete it later.
   - For errors, explain that the affected data cannot be described as target-ready. Offer to correct it, omit the affected record, or keep an importable draft clearly marked not target-ready. Only unresolved historical-course routing or core course settings delay a final JSON that includes those affected courses.
8. If the student supplies corrections or additions, update only those confirmed values, recreate and revalidate the profile, and rerun every selected target check. Track fields the student explicitly chose to leave blank so they are reported at delivery but not asked again in the same intake session. Identify a skipped item by its semantic record and field (for example, Geometry / Q2 grade or Robotics / hours per week), not only by a JSON array path, because indexes can change when records are added. Do not silently repair uncertain values.

## Historical-course gate

Historical course and grade data must be routeable before final JSON is offered. For every historical course to be included, confirm:

- the course identity or course name;
- its grade level and school year, or an explicit source mapping that establishes both without guessing;
- the student's term system, such as Semester, Trimester, Quarter, or Yearly;
- the course grading system; and
- each grade value that will be included, together with the grading period or final-grade field it belongs to.

Apply this gate before the first creation call. If an included historical course lacks its identity, grade-level/school-year routing, `termSystem`, or `courseGradingSystem`, ask for the missing routing information before sending that course to `create_master_profile`. If the student cannot supply it, obtain their choice to omit the affected course and then continue with the other supported records; do not use an unresolved course merely to generate a draft and ask afterward.

When a schedule implies additional grading periods but the source supplies only some of them, ask once whether the missing periods are unavailable, pending, intentionally omitted, or available to add. Never copy one period's grade into another period. Preserve unavailable or unanswered periods as blanks, report them as nonblocking warnings, and still offer an importable draft. If the course cannot be identified or routed to a grade level and school year, ask the student to supply that information or omit the course from this JSON. Offer to continue with an importable JSON containing the other supported sections while the unresolved course is omitted; do not block an activity-, honor-, or test-only draft.

Only missing course identity, grade-level/school-year routing, `termSystem`, or `courseGradingSystem` blocks inclusion of the affected historical course in a final deliverable. Missing term or final grades do not block the JSON; they remain blank and must be reported for later review.

For current-year courses, ask for the course name, subject/category, and course level when missing. Also ask for the course schedule when Common App is selected. When UC is selected, confirm both the profile term system and course grading system because CollegeFill uses current-year courses in UC grade-12 course preparation. Only Semester, Trimester, Quarter, or Yearly can be treated as ready for course filling; preserve `Other` in an importable draft but require manual clarification before claiming target readiness.

## Missing information

Treat missing completion details for activities and honors as **nonblocking warnings**, not reasons to withhold otherwise importable JSON. This includes target-relevant details such as activity participation grade years, position or leadership, description, hours per week, weeks per year, and honor grade or recognition level.

For AP scores, a missing date or a year-only date is also nonblocking: preserve an explicit year as `YYYY`, omit `testDate` when none was supplied, ask for month and year, and never assume May or another month. For other test families, follow the readiness tool's returned severity and questions rather than treating every missing test date as optional.

For Common App activity type, allow only deterministic CollegeFill aliases that preserve meaning. For example, `Community Service (Volunteer)` may normalize to `Community service or volunteer work`. If a type does not have a documented exact alias, preserve it for review and ask the student to select the exact live Common App option; never guess.

When UC is a selected target, surface every category-applicable finding returned by `prepare_uc_profile`. In particular, distinguish the two UC narrative prompts instead of merging them:

- for an Award or honor, ask separately for the eligibility requirements and what the student did to earn the award;
- for Volunteer / Community service, ask separately for the organization description and the student's volunteer-work description; and
- for Work experience, ask separately for the employer or organization description and the student's job-responsibilities description.

Also surface the other applicable UC category details reported by the tool, such as UC category, award type or recognition level, grade participation, time commitment, program name, job title, or whether the student still works there. Ask only for fields applicable to the selected UC category. These are completion reminders, not permission to invent an answer or a claim that every field is universally required by UC.

- Ask these questions in one concise batch after the readiness checks, prioritizing fields the selected target will require.
- Make clear that the student may answer now or skip.
- If the student skips, preserve blanks and say exactly which items must be reviewed or completed later in CollegeFill, Common App, or UC.
- Do not repeatedly ask a skipped question in the same intake session.
- A missing record identity, such as an AP subject, activity name, or honor title, cannot be guessed. Ask for the identity or omit that record.

Do not describe an incomplete profile as complete or application-ready. Readiness tool results are data checks, not confirmation that an application page was filled.

## Deliverable

Return one generic file named `collegefill-ai-profile-v1.json`, using the latest `masterProfile` returned by `create_master_profile` after all accepted corrections. Readiness-tool results are checks; do not choose between their target-specific filenames when the student selected both targets. The file must contain exactly that `masterProfile` object as the root JSON value, not the surrounding tool response, explanations, Markdown, or readiness metadata.

In the accompanying message, state:

- the selected application target or targets;
- which CollegeFill sections are included;
- unresolved nonblocking items the student chose to leave blank; and
- that those blanks must be reviewed and completed later where required.

Do not create or offer a review Excel file. Do not claim that CollegeFill or this workflow logged in to, navigated, filled, saved, or submitted Common App or UC. Do not claim a file was saved to a library or device unless the host confirms it.
