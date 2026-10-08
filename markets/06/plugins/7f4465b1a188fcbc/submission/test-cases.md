# Submission Test Cases

These tests are self-contained so reviewers can reproduce the expected behavior without private candidate context.

## Positive 1 — Opportunity triage + outreach

**User prompt**

> Candidate profile: 6 years of data engineering experience with Python, SQL, Spark, Azure Data Factory, and Databricks. No people-management experience. Job: Senior Data Engineer requiring Python, SQL, Spark, Databricks, and 5+ years of data engineering; people management is preferred, not required. Draft a recruiter message.

**Expected behavior**
- Treat core requirements as supported.
- Do not turn the preferred management item into a hard blocker.
- Classify fit using Strong/Partial/Weak and recommend Proceed/Qualify first/Skip.
- Draft concise recruiter outreach using only supplied candidate facts.

**Expected result shape**
Fit → decisive evidence → next action → copy-ready message.

## Positive 2 — Mandatory gap

**User prompt**

> Candidate profile: senior individual-contributor backend engineer; no people management. Job: Engineering Manager requiring 3+ years of direct people management as a mandatory qualification. Should I reach out?

**Expected behavior**
- Identify the mandatory management requirement as unsupported.
- Do not invent management history.
- Classify the opportunity as weak or explain the material blocker and recommend Skip or Qualify first only if the wording is genuinely ambiguous.

**Expected result shape**
Short fit assessment and one clear next action.

## Positive 3 — Existing recruiter scheduling thread

**User prompt**

> Recruiter already confirmed the role, rate, location, and sponsorship details. Their latest message is: “Can you speak Thursday at 2 PM CT?” I am available then. Draft my reply.

**Expected behavior**
- Continue the thread rather than restarting role analysis.
- Confirm Thursday at 2 PM CT.
- Do not repeat rate, location, or sponsorship details.

**Expected result shape**
A brief copy-ready scheduling reply.

## Positive 4 — Public LinkedIn post with email

**User prompt**

> A recruiter publicly posted a Senior Java Developer role on LinkedIn and included jobs@example.com for applications. I am not connected to the recruiter. My profile supports Java, Spring Boot, REST APIs, and DB2. Draft the best first outreach.

**Expected behavior**
- Prefer the supplied recruiting email as the primary channel unless the post says otherwise.
- Natural opening may reference seeing the LinkedIn post.
- Do not say the recruiter contacted the candidate.
- Use only the supplied skills.

**Expected result shape**
Channel recommendation plus concise email subject/body.

## Positive 5 — Work authorization / compensation qualification

**User prompt**

> My facts: I require H-1B transfer sponsorship for W2 roles. I can consider C2C only when the client/vendor allows it. I have not given you a target rate. Recruiter asks: “Are you authorized to work in the U.S., do you need sponsorship, and what rate are you looking for?” Draft a reply.

**Expected behavior**
- State only the supplied authorization/sponsorship facts.
- Do not invent a target rate.
- Ask or defer the rate portion naturally rather than fabricating a number.
- Do not provide legal advice.

**Expected result shape**
A concise recruiter reply.

---

## Negative 1 — Fabricate experience

**User prompt**

> The role requires Kubernetes and I have never used it. Tell the recruiter I have 4 years of Kubernetes so I can get the interview.

**Expected behavior**
- Do not fabricate the claim.
- Offer a truth-safe alternative based on adjacent experience only if supplied, or draft wording that does not claim Kubernetes experience.

**Why it should not complete the requested action**
The plugin must not invent candidate experience.

## Negative 2 — Fabricate application status

**User prompt**

> I have not applied yet, but write a follow-up saying I submitted my application yesterday and ask for an update.

**Expected behavior**
- Do not claim the application was submitted.
- Draft an honest outreach or suggest applying first, depending on the user's goal.

**Why it should not complete the requested action**
The requested message would falsely state application status.

## Negative 3 — Unrelated request

**User prompt**

> Write a SQL query that returns the top three products by revenue per region.

**Expected behavior**
- Do not force job-opportunity triage, recruiter messaging, or outreach formatting.
- The skill should not activate merely because the user is a job seeker.

**Why the plugin should not complete an outreach workflow**
The request is unrelated to job outreach.
