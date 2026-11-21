# Review preparation — Ready4Jobs 0.1.0

The package contains five positive and three negative cases for the anonymous two-tool release. They are prepared cases, not proof that production or reviewer runs passed. Use synthetic fixtures only. No reviewer account is required for this version.

The MCP endpoint is `https://www.ready4jobs.ai/api/mcp`. The card provides final diagnosis and concrete proposals without saving or applying edits. `render_resume_analysis` is presentation of supplied data and is marked unverified. There is no OAuth, account tool, PDF export or checkout.

The V1 card retains the contextual complete-version sentence in English and French, linked to the locale homepage at `https://www.ready4jobs.ai/fr` or `/en`. Old `/chatgpt/overview` links redirect to that homepage. The ChatGPT diagnosis is not transferred to a website account; users can upload their CV again on the site, anonymously or after creating an account. The card does not open checkout or require website sign-in. This wording and destination remain review candidates; if OpenAI rejects them, revise the copy before resubmission. The privacy page is `/en/chatgpt/privacy`, support is `/en/chatgpt/support`, and terms are `/en/legal/terms`. Confirm public HTTPS availability and publisher identity before submission.

Run every review case against the stable production endpoint in ChatGPT, including original PDF/DOCX file objects, mobile card use and the negative cases. The manifest includes the owner's unlisted walkthrough URL; confirm it plays for a reviewer without sign-in. The owner must verify the domain and publisher identity and inspect portal scans. No OpenAI approval is asserted here.
