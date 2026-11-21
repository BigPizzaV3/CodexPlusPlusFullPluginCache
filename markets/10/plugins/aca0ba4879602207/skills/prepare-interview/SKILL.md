---
name: prepare-interview
description: Prepare a FaceFirst job description and interview questions. Save an employer-reviewed job draft when requested.
---

# Prepare a FaceFirst interview

Prepare a job draft for an asynchronous video interview. Candidates answer each question with a short video.

Use the employer's role, duties, and requirements. Ask for missing facts only when they affect the questions.
Mark other missing facts as "Not specified". Do not invent pay, qualifications, experience, or work conditions.

Keep the job description and requirements separate. Prepare up to ten clear questions about the stated duties.
Use five questions unless the employer requests another count. Ask one question per video response.
Prefer specific work examples that a candidate can explain in about 60 seconds.
For each question, explain what work evidence it seeks. Keep this explanation outside the saved question text.
Use the same questions for candidates who apply for the same role.

Show the title, description, requirements, questions, and missing facts before a save.
Keep candidate assessment and decisions outside this workflow. Do not request candidate videos or personal records.

## Save the draft

When the employer requests a save, use the FaceFirst MCP connection.
Call `get_profile` and `list_organizations` to identify the account and permitted organization.
Each connection permits one organization. Ask the employer to select another connection if the organization is incorrect.
If the employer has not reviewed the prepared content, request that review before the save.
An explicit instruction to save the displayed content supplies the review approval.

Call `create_job_draft` with the reviewed title, description, requirements, and question text.
Generate a unique `requestKey` with at least 16 letters, digits, underscores, or hyphens.
Keep this key with the saved content. Reuse both for an identical retry after a timeout or uncertain result.
Use a new key when the employer requests changed content as a new draft.
For a request-key conflict, show the error. Do not silently change the key and create another job.

Report a save only after the tool returns the job ID and review URL.
Show the review URL so the employer can open the draft in FaceFirst.
Explain that the employer must publish the draft in FaceFirst before candidates can apply.
Use `get_job_draft` to reopen a saved draft. Use `list_job_drafts` when the job ID is unknown.

If the connection is unavailable, provide the prepared content in the conversation.
State that the draft was not saved. Do not invent a job ID or link.
If access has expired, ask the employer to reconnect FaceFirst.
Do not request a password, token, or authentication code in the conversation.

The plugin cannot publish jobs, send invitations, purchase credits, or make candidate decisions.
Do not describe those operations as plugin capabilities.
