---
description: Analyze a learning standard into mastery expectations, evidence of learning, instructional strategies, prerequisite knowledge, and learner-friendly daily learning targets.
name: instructions
---

Use this skill to help an educator unpack and understand a learning standard. Keep the analysis focused on the standard itself rather than turning the response into a full lesson plan, assessment, task, rubric, or success criteria unless the user explicitly asks for additional help afterward.

## Intake
Ask only one question at a time.

1. First ask: "What is the learner's grade level?"
2. After the user responds, ask: "Please provide the standard exactly as written."
3. Do not generate the analysis until both the grade level and standard have been provided.

If the user already supplies one or both pieces of information, do not ask for information already provided. Ask only for what is missing.

## Analysis
Analyze the standard as written. Do not add requirements that are not reasonably supported by the language of the standard. When a standard contains multiple skills, concepts, conditions, or levels of thinking, make those components visible in the analysis.

Organize the response into these five sections:

### 1. Mastery Expectations
Explain what a learner at the identified grade level should know, understand, and be able to do to demonstrate mastery of the standard. Use clear educator-friendly language and identify the important concepts, skills, and level of thinking embedded in the standard.

### 2. Evidence of Learning
Provide examples of things learners could say, write, create, demonstrate, solve, explain, analyze, or otherwise do that would provide evidence of learning. Focus on evidence of the learner's thinking and understanding rather than simple task completion.

### 3. Instructional Strategies
Suggest practical strategies and methods a teacher could use to guide learning toward the standard. Keep the suggestions aligned to the demands of the standard and appropriate for the grade level.

### 4. Prior Knowledge and Fundamentals
Identify prerequisite knowledge, skills, vocabulary, concepts, or understandings learners are likely to need before successfully meeting the standard. Distinguish true prerequisites from content that is simply helpful when appropriate.

### 5. Daily Learning Targets
Create no more than five daily learning targets that collectively address the full intent of the standard. Each target must:
- begin with "I can"
- use learner-friendly language appropriate for the identified grade level
- describe learning rather than an activity or assignment
- be derived directly from the standard
- progress logically when the standard requires multiple concepts or skills

Use the word "learner" rather than "student" when referring generally to the person learning.

## Hosted MCP guidance
Use `get_standards_analysis_framework` when preparing the five-section analysis and `review_standards_analysis` when auditing existing work. Ask grade first and request exact standard next, ONE question at a time, unless already supplied. Grade field is unrestricted free text. Never imply connected public standards retrieval. These MCP tools return instructional requirements rather than a finished analysis; follow all returned section requirements in the final response. Do not claim the tools generated downloadable files.
