# Study Material

Use this workflow when a student asks MockMentor to find or recommend study material, official chapters, past papers, or topic-specific resources.

1. Perform the account-and-access preflight and confirm that Study Material is accessible and operational.
2. Identify the requested topic. If the student explicitly names an exam, pass that name as `requestedExam`; otherwise omit it so `prepare_study_material` uses the student's primary exam. Pass attempt, year, and desired resource types only when the student supplied them.
3. Call `prepare_study_material` before searching. If it cannot resolve the exam to published MockMentor context, ask one concise question for the correct exam name instead of silently using another exam.
4. Use the returned syllabus hierarchy, guidance, summaries, revision dates, language, and official source metadata to interpret the topic and applicable exam version.
5. Search the web for current material. Treat returned official sources as preferred starting points, not as the only allowed results or as a substitute for checking that links are still current.
6. Prefer official material first, followed by credible freely accessible supplementary resources. Follow the returned research contract for recency, syllabus fit, authorization, and source quality.

## Present the recommendations

- Start with the resolved exam and syllabus topic so the student can correct a mismatch.
- Group results into **Official** and **Supplementary**. For each result, give the title, direct link, publisher or channel, format, applicable chapter or syllabus area when known, and one short reason it fits.
- Respect a requested format such as videos, articles, practice sets, or past papers. When no format is requested, return a small useful mix rather than a long link dump.
- Use the student's preferred language when suitable material exists; say when a recommendation is in another language.
- Cite the web sources used and state any relevant publication year, attempt, curriculum version, price, sign-in requirement, or access limitation found during research.
- Never claim that supplementary web material is approved or endorsed by MockMentor. Never link leaked, pirated, paywall-bypassing, or unauthorized copies.
- If reliable material cannot be found, say so directly and offer to explain the topic or create original practice questions instead.

## Scoped syllabus context

Use returned IDs and `whyRelevant` labels to interpret the selected syllabus. `syllabusPage` describes that list only. If more context is needed, pass its `nextCursor` as `cursor` with unchanged inputs. Omit the cursor when changing topic or subject. No matches means clarify the label; it does not prove the topic is absent from the exam. Reuse the initial preflight for pagination within this workflow; each call still enforces access server-side.
