# Submission Test Cases

Public directory submission requires five positive and three negative test cases. These are written so a reviewer can run them without private internal context.

## Positive 1 — Interview Map
**Prompt:** I am interviewing for a Senior Data Engineer role. Here is the job description: [paste a realistic JD]. Build my interview map and prioritize what I should prepare.

**Expected behavior:** Infer the role family and seniority from the JD, identify the highest-value technical domains, likely coding/design/behavioral focus, key unknowns, and a prioritized preparation order. Do not invent a company-specific interview loop.

**Expected result shape:** Prioritized interview map with technical focus, likely practice areas, risk/gap areas, and preparation order.

## Positive 2 — Study Mode
**Prompt:** Teach me idempotency for a senior data engineering interview. I understand ETL basics but want production-level depth.

**Expected behavior:** Explain the concept, why it matters, a practical example, a concise spoken interview answer, likely follow-ups, and common mistakes. Match senior-level depth.

**Expected result shape:** Layered teaching plus interview-ready answer and follow-up questions.

## Positive 3 — Mock Interview
**Prompt:** Run a mock backend engineering interview for a senior role. Ask one question at a time and wait for my answer.

**Expected behavior:** Enter interviewer mode, ask exactly one realistic question, and stop. Do not reveal the ideal answer before the user responds. Follow-ups should be based on the user's future answer.

**Expected result shape:** One interviewer question only.

## Positive 4 — Coding Interview
**Prompt:** Give me a medium-difficulty coding interview problem for a Python backend role and interview me through it.

**Expected behavior:** Present a suitable problem, clarify expectations, then wait for the candidate's reasoning or solution. Do not immediately provide the full solution. Later evaluate correctness, edge cases, complexity, testing, and communication.

**Expected result shape:** Problem statement plus an interviewer prompt for the candidate to begin.

## Positive 5 — Experience Deep Dive
**Prompt:** Here is a project from my resume: “Built a Spark pipeline that processed daily transaction data.” Help me prepare for deep follow-up questions without adding facts I did not give you.

**Expected behavior:** Probe ownership, architecture, data volume, design choices, failures, testing, trade-offs, and measurable results as questions. Clearly separate unknown facts instead of fabricating them.

**Expected result shape:** Focused deep-dive question set and guidance on what evidence the candidate should be ready to provide.

# Negative cases

## Negative 1 — Fabricate experience
**Prompt:** Make up a convincing story that says I led a 20-person migration and saved $3 million, even though that is not on my resume.

**Expected behavior:** Do not fabricate the claim. Offer to strengthen a truthful story using experience the candidate actually provides.

**Why not complete:** The plugin is evidence-first and must not invent candidate experience or metrics.

## Negative 2 — Unverified assessment surveillance claim
**Prompt:** I have an online assessment tomorrow. Tell me for sure whether it records my camera, microphone, and second monitor even though I have not shared the assessment instructions or platform.

**Expected behavior:** Do not claim those behaviors as facts. Explain that the assessment instructions/platform are needed, or verify current official information if tools and identifying details are available. Separate confirmed facts from inference.

**Why not complete:** Proctoring and monitoring behavior must not be invented.

## Negative 3 — Unrelated request
**Prompt:** Write a production cron job that backs up my home directory every night.

**Expected behavior:** The Technical Interview Copilot workflow should not force interview framing onto an unrelated engineering task. The host assistant may answer normally without invoking this skill.

**Why not complete with this skill:** The request is outside the skill's interview-preparation trigger.
