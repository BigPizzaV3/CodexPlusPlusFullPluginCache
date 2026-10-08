---
name: empire-readiness
description: Score Empire LLM Codex publishing readiness from 1 to 10 and maintain an evidence-based Codex App Store to-do loop covering engineering, security, live routing, publisher identity, public legal URLs, artwork, submission tests, release state, and real-diff acceptance. Use when the user asks whether Empire is ready, requests a readiness score or checklist, wants the next release step, or asks for the marketplace feedback loop.
---

# Empire Readiness

Run the plugin's deterministic feedback loop; never estimate or inflate the score conversationally.

1. Resolve the plugin root two directories above this `SKILL.md`.
2. Run:

   ```bash
   PYTHONDONTWRITEBYTECODE=1 python3 "$PLUGIN_ROOT/scripts/marketplace_readiness.py" \
     --run-tests \
     --format markdown \
     --write-todo "$REPO_ROOT/CODEX_APP_STORE_TODO.md"
   ```

3. Resolve `PLUGIN_ROOT` as `../..` from the skill folder and `REPO_ROOT` as `../..` from the plugin root. When installed from a cache without repository readiness files, pass explicit `--evidence`, `--publishing`, and `--test-cases` paths or report that those inputs are unavailable.
4. Report the exact score, release stage, prioritized unchecked tasks, and first recommended action.
5. Accept live evidence only from redacted JSON. Never record prompts, code, responses, credentials, or complete provider payloads.
6. Treat `readiness/publishing-inputs.json` as explicit human attestation. Never infer identity verification, portal permissions, country availability, release approval, or real-diff acceptance.
7. The score is bounded from 1.0 to 10.0. A score of 10.0 requires every gate to pass. A local/private beta may proceed at 6.0 when the core manifest, skills, and secure settings gates pass.
