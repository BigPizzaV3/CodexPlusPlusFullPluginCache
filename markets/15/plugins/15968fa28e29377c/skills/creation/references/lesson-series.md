# Plan a connected lesson series

Use this reference when the teacher asks for a unit or several lessons that build on one another. Plan the progression, then use `create_lessons` to generate the lessons. This produces standalone Chalkie lessons, not a native series record. Keep their returned IDs and URIs in order and describe that distinction accurately.

## Plan the whole sequence

Call `get_creation_context` for teacher context and supported grades, languages, settings, and limits. Use `search_curriculum_standards` when curriculum alignment is requested. Work from the teacher's topic, grade, language, lesson count, slide budget, source material, and teaching approach. Resolve missing information only when it materially changes the plan.

Before generating, define each lesson's title, learning goal, content outline, prerequisite knowledge, and contribution to the overall sequence. Give each lesson its own scope: build on earlier knowledge, avoid re-teaching the same explanations or activities, and leave later topics for their own lessons. The final lesson consolidates the sequence. If vocabulary is requested, choose four useful terms per lesson.

Keep the structure, visual direction, and terminology consistent across lessons. Decide once whether objectives and vocabulary need to share a slide to fit the budget. Reserve space for the recap and a final understanding check; do not spend the entire budget on new content.

## Pass the context into every lesson

Each `create_lessons.items[]` entry needs its own `topic`, `grade_id`, `language`, and other supported settings. Follow the conversational writing and formatting guidance in the creation skill. Use the list below to check coverage, not as a rigid template for the brief. Short paragraphs can explain the teaching, with an ordered list for the sequence outline and brief headings where helpful. Put the following in its `additional_instructions` string:

1. The sequence topic and this lesson's position, for example "Lesson 2 of 4".
2. A compact outline of the whole sequence, marking earlier lessons, this lesson, and lessons still to come.
3. This lesson's learning goal and full content outline.
4. The concrete knowledge to retrieve from the preceding lesson, plus material to avoid repeating or introducing too early.
5. The shared slide structure, terminology, and design brief.

These standalone lessons do not receive Chalkie's native series context automatically. Supplying this information explicitly is essential, including when generating several lessons in one batch. Keep each instruction string within the tool's 15,000-character limit; summarise surrounding lessons rather than copying whole decks.

## Recap and progression

The first lesson introduces the sequence without assuming prior lessons. For every subsequent lesson, make slide 2, immediately after the cover, a recap of the previous lesson. Title it "Recap: <previous lesson title>" in the lesson language. Include three short, specific recap points followed by a retrieval question or short quiz before introducing new material. Count this slide within the requested slide budget.

If previous lessons have already completed, call `get_resource` for each lesson to ground the recap in what was actually generated. Otherwise, use the shared outline and do not claim to have checked a completed deck. Never recap only a vague topic name. Each lesson should still provide enough orientation for a student who missed the previous one.

Use consistent fixed-slide headings and task formats throughout. Build on previously introduced vocabulary, examples, and concepts rather than redefining them. End with a check for understanding, and make the final lesson consolidate the unit rather than open a new thread.

## Create and follow through

Use `create_lessons` with at most the batch size reported by `get_creation_context` (currently 10). Split longer sequences into batches without losing the overall plan or ordering. Use the same supported shared settings across batches.

Creation is asynchronous. Call `get_resource` for each returned lesson ID to check completion and inspect the resulting content. Report failures accurately. Return an ordered list of lessons and their links; do not claim the sequence is complete while any requested lesson is still generating.

Follow the creation skill's theme guidance and preserve any requested learning supports in `additional_instructions` alongside the progression, recap, and teaching requirements.
