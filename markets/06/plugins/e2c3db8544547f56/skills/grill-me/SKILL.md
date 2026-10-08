---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding and resolving each branch of the decision tree. Use when the user asks to be grilled, challenged, stress-tested, have holes poked in a plan, or be walked through design choices before code or documentation is produced. Do not use when the design is settled and the user only wants execution or a finished artifact.
---

# Grill me

Interview the user about every material part of the plan until both sides share the same understanding.

Ask one question at a time. Walk through the decision tree in dependency order so later questions build on settled answers.

For each question:

1. Explain what decision the question controls.
2. Give a recommended answer and a short reason.
3. Ask the user for their answer.
4. Record the decision before moving to the next dependent question.

If the codebase, supplied files or connected sources can answer a question, inspect them instead of asking the user.

Challenge contradictions, missing constraints and risky assumptions directly. Do not produce code or final documentation until the important branches are resolved, unless the user asks to stop the interview and proceed.
