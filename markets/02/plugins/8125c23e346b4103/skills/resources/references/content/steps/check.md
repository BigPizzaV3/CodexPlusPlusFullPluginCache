# Submit your project

This is the step where your project actually gets sent to Devpost.

Codex runs a final check first — completeness, security scan (redacted findings only), and the hackathon's real requirements — and tells you whether you are ready, close, or not ready.

If you're ready, Codex shows you exactly what will be submitted and asks for your explicit "yes, submit." On your confirmation it submits your project to Devpost through the official Devpost connection, then verifies with Devpost that the submission landed and gives you your public project page link.

Nothing is ever submitted without your explicit confirmation — and until you see "✅ Submitted to Devpost," nothing has been sent.

If the Devpost connection fails (for example, you're not signed in), Codex will give you the official Devpost submission page link so you can finish on the website before the deadline — then come back and run `$submit-project` again to verify it landed.

If the result is close or not ready, fix the listed blockers first and run `$submit-project` again.
<!-- Copy maintainers: edit this page copy in content/steps/check.md. -->
