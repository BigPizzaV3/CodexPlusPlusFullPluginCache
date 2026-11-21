---
name: turrior-screening-quiz
description: Create, update, or attach a text or video screening quiz to a Turrior job.
---

Use this skill when the user asks to create or manage candidate screening questions or a video interview quiz.

1. Choose `create-quiz` for text questionnaires and `create-video-quiz` for asynchronous video interviews.
2. When attaching an existing quiz, resolve it with `get-quizzes-list`, resolve the job if needed, then call `attach-quiz`.
3. Make the quiz skippable only when the user requests it or the workflow clearly requires it.
4. For video quizzes, include clear job-relevant questions. For a general candidate screening video, include at least one introductory question asking the candidate to introduce themselves and describe relevant experience.
5. `put-quiz` and `put-video-quiz` are full replacements, not patches. When updating, preserve the IDs of existing questions/options that should remain and send the complete final question list.
6. Never omit an existing question from an update unless it should be deleted.
