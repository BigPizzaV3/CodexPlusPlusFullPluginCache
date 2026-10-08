---
name: submit-project
description: Submit the project to Devpost — run the final readiness check against the hackathon requirements and the prepared draft, then, after explicit user confirmation, actually submit via the Devpost MCP and verify it landed. Use when the user is ready to submit, wants the final checklist, or asks whether they have submitted.
---

# Submit Project

## Purpose

Actually submit the participant's project to Devpost. The command runs the final readiness review and the local security scan on the way, but its job is the submission itself: confirm, call `devpost.submit_project`, verify live that it landed, and report the truth.

Chat is the primary participant interface. Keep responses text-first so they render in any Codex host; the bundled `devpost` MCP server supplies rich inline visuals on hosts that support them.

## Required Data Source

Official requirements and rules come from the `devpost` MCP server — follow **Devpost MCP Server** in `references/plugin-runtime.md` (call only what you need, never verify or set up the server, degrade in one line on failure).

Draw on these only as needed: `devpost.get_submission_requirements`, `devpost.get_hackathon_rules`, `devpost.get_judging_criteria`, `devpost.get_key_dates`. Check readiness against the real requirements; if they are unavailable, run the check against `references/preflight-checklist.md` alone, say it is provisional, and cap the result at `close` — a provisional review can never yield `ready`, because `ready` authorizes a real submit and must rest on the event's live requirements (per **Never present unofficial data as official** in `references/plugin-runtime.md`).

For submission status and the submit itself (all AUTH-REQUIRED): `devpost.list_my_projects` / `devpost.get_project` (find the project and read its real submission status), `devpost.create_project` / `devpost.update_project` (sync the prepared draft when needed), and `devpost.submit_project` (the actual submission).

For thumbnails, two upload services exist (both AUTH-REQUIRED) — pick by encoded size: `devpost.upload_project_thumbnail` sends the image inline as base64 through the conversation and is for small images only (target ≤ 50 KB encoded, e.g. a 300×300 JPEG at quality 60; pre-shrink in one step, do not iterate); `devpost.prepare_thumbnail_upload` returns an upload URL (10-minute TTL) plus the OS-specific curl/PowerShell command that streams the file from disk without putting the bytes through the conversation — use it for anything larger. Both accept JPEG/PNG/GIF up to 5 MB.

## Required References

Read before responding:

- `references/plugin-runtime.md`
- `references/preflight-checklist.md`
- `references/config/hackathon.json`
- `references/content/steps/check.md` (the page content you will present)

## Preconditions

Read `.devpost-hackathon-state.json`.

If the file does not exist, direct the user to `$start-hackathon`.

If `rules_acknowledged` is not `true`, direct the user to `$review-hackathon-rules` first.

If `devpost-submission.md` does not exist, direct the user to `$prepare-submission`.

Legacy state: older state files may use `submission` (instead of `submit-project`) in `completed_stages` or `next_command`, and may contain a `browser_handoff_ready` field. Treat `submission` as this stage and ignore `browser_handoff_ready` — but never treat a legacy `completed_stages` entry as proof of an actual submission; only the live check below proves that.

## Live Status Check (first, when reachable)

This whole command acts on Devpost, so gate it: call `devpost.whoami` (AUTH-REQUIRED) first. If it fails on auth, hard-stop per **On auth failure** in `references/plugin-runtime.md` — one-line notice, the sign-in recovery, plus the official Devpost submission page URL so the participant can still finish on the website before the deadline. Do not run the readiness review as if it could end in a submit.

Whether the project is submitted is Devpost-owned data — local state is never proof. After the gate passes, check live: call `devpost.list_my_projects` / `devpost.get_project` (AUTH-REQUIRED) and read whether this project has been submitted to this hackathon (`submitted_at` on the hackathon entry).

- **Already submitted:** lead with the ✅ status block (below) and the public project URL, skip the readiness review and confirmation, and offer the offboarding follow-up ideas instead (see **Offboarding**).
- **Not submitted:** proceed with the readiness review below, under the ⏳ status line.
- **Status tools unavailable (availability, not auth):** proceed with the review, say the live status could not be verified, and keep the ⏳ line. A signed-out participant never reaches this branch — auth failure already hard-stopped at the gate above.

## Security Scan

Before assigning the final readiness result, scan the project for exposed secrets with a
grep (no script needed). Run from the participant's project root:

```bash
grep -rInE 'sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|gh[posru]_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]+|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(api[_-]?key|secret|password|token)\s*[:=]\s*["'"'"'][^"'"'"']{8,}' . \
  --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=dist --exclude-dir=build --exclude-dir=.next --exclude-dir=venv --exclude-dir=__pycache__ 2>/dev/null
find . \( -name '.env' -o -name '*.pem' -o -name 'id_rsa' -o -name 'id_dsa' \) -not -path '*/node_modules/*' -not -path '*/.git/*' 2>/dev/null
```

Interpret the results:

- **block**: the grep matched a high-confidence secret (OpenAI/GitHub/Slack token, AWS key,
  or a private-key block). The submission cannot be marked `ready` — and you must NOT call
  `submit_project` — until it is removed.
- **review**: only risky credential-looking files (`.env`, `*.pem`, `id_rsa`) or generic
  `key=…`/`password=…` assignments turned up. The submission can be `close`, not `ready`,
  unless the participant explicitly verifies they are benign.
- **pass**: no matches.

Never paste raw secret values in chat or generated files — refer to the file and line only,
with the value redacted.

## Readiness Review

Review:

- rules acknowledgment recorded
- project brief present
- honest build description
- AI usage explained clearly
- Codex usage explained clearly
- testing instructions included
- repo link present or clearly marked TODO
- public demo link present or clearly marked TODO
- demo video plan or URL present or clearly marked TODO
- screenshot plan present
- every event requirement satisfied (cross-check against `get_submission_requirements`)
- unresolved legal or sponsor placeholders clearly labeled
- no obvious contradiction between the build and the submission copy
- no high-confidence exposed secrets from the local security scan
- no risky credential-looking files that need user review

Assign one top-line result: `ready`, `close`, or `not ready`. Missing inputs (repo URL,
demo URL, video decision) are asked for conversationally — one short question each — not
dumped as a chore list pointing at internal files.

## Submit To Devpost (MCP, auth, high-stakes)

The final submit is high-stakes, so it REQUIRES explicit user confirmation before you call the tool.

1. Only proceed when the readiness result is `ready` — which requires the live requirements check; a provisional, fallback-checklist review caps at `close` and never ends in a submit. Never submit on a `block` scan result.
2. Present a short, plain summary of exactly what will be submitted: the project title, the hackathon name, and any category or custom-question answers. State clearly that this submits the project to Devpost for real.
3. Require the user to explicitly confirm they want to submit now (an unambiguous "yes, submit"). If they do not confirm, stop and leave the project unsubmitted — do not call the tool — and keep the ⏳ status line in the response.
4. On confirmation, call the `devpost.submit_project` MCP tool (AUTH-REQUIRED) for the prepared project and hackathon. If the project does not exist on Devpost yet, create or sync it first via `create_project` / `update_project`, confirming with the user before each write.
4a. **Offer to capture a screenshot when one is missing.** If the project has no thumbnail or screenshots and it runs locally, offer — don't just note the gap: "Want me to capture a screenshot from the running app and upload it as your project thumbnail?" On yes, capture, upload via the size-appropriate thumbnail service (AUTH-REQUIRED; see **Required Data Source** — `upload_project_thumbnail` inline at ≤ 50 KB encoded, `prepare_thumbnail_upload` streaming from disk above that), and confirm per 4b. Never capture or upload without their yes.
4b. **Confirm every asset you handle.** If a screenshot or thumbnail is provided or uploaded on this turn (`prepare_thumbnail_upload` / `upload_project_thumbnail`), state explicitly what was received and where it went — uploaded as the project thumbnail, saved locally at a path, or still pending. Never handle an upload silently. On a successful thumbnail upload, add one line telling the participant what it's for: this image now represents the project — it's the picture shown on their project listing in the hackathon's submissions on Devpost.
5. **Verify, then report.** After `submit_project` returns success, confirm live via `devpost.get_project` (or `list_my_projects`) that the submission is recorded, and report the ✅ status line with the public project URL. If the readback can't run, report the tool's returned confirmation and say verification is pending.

Fallback: if `submit_project` fails on auth or availability, do NOT silently succeed — keep the ⏳ status line, report that the submit could not be completed, note that submitting requires being signed in to the Devpost MCP, and give the official Devpost submission page URL so the participant can finish on the website before the deadline. If they submit on the website, tell them to come back and run `$submit-project` again — the live status check will verify it. Leave `submission.status` as `ready` so the MCP submit can be retried.

## State Update

Edit `.devpost-hackathon-state.json` directly, only when state changes on this turn,
preserving the fields you are not touching.

`completed_stages` may gain `submit-project` in exactly one case: `submit_project`
succeeded (or the live check confirmed an existing submission). A readiness result of
`ready` is not completion — the participant has not submitted yet.

- **Submitted (verified):** add `submit-project` to `completed_stages`, set `current_stage`
  to `submit-project`, `submission.status` to `submitted`, and `next_command` to
  `hackathon-map`. A returned confirmation id/url may be recorded under `submission`.
- **Ready but not yet confirmed/submitted:** set `current_stage` to `submit-project`,
  `submission.status` to `ready`, and `next_command` to `submit-project`. Do NOT touch
  `completed_stages`.
- **Not ready:** set `current_stage` to `submit-project`, `submission.status` to
  `needs-work`, and `next_command` to the specific command that fixes the top issue (e.g.
  `prepare-submission`).

## Presentation Output

After the readiness review and the state edit, compose the response in-context per
`references/plugin-runtime.md` ("Composing the Response"): read `references/content/steps/check.md`,
strip maintainer `<!-- -->` comments, interpolate the event name, and present it. Render
the journey stepper widget first (see PLUGIN_RUNTIME). Summarize the scan + readiness
result in your own words alongside the page content.

## Chat Output

Keep chat output compact. Do not hand-write a separate progress dashboard — the stepper
widget shows progress.

**Mandatory status block.** Every response from this command must include, verbatim, near
the top, exactly one of the two blocks (⏳ or ✅) from **Submission Status Blocks** in
`references/plugin-runtime.md`. On the turn a fresh submit succeeds, the **Offboarding** response
below replaces the ✅ heading with its celebratory form — that is the one sanctioned
variant. The ✅ form may be used only after `submit_project` success or a live check
confirming the submission — never on `ready`, never from local state alone. Verb
discipline: outside the ✅ block, never say "submitted" or "submission complete" about the
participant's work.

## Offboarding (after a verified submission)

On the turn a submit succeeds (and, trimmed to the follow-up ideas, when a later run finds
the project already submitted), close the journey properly. First call
`devpost.get_key_dates` for the real submission deadline; if it is unavailable, write "the
submission deadline" and point to the hackathon page — never invent a date. Then compose
in this shape, interpolating the URL and deadline:

```markdown
### 🎉 Submitted — congratulations!

✅ **Submitted to Devpost** — verified live. Your public project page: <URL>

You did the hard part: you shipped. Now here's the part most people miss — **your
submission isn't frozen.** You can keep improving your project page until the deadline
(**<deadline>**), and judges see the final version, not the one from the moment you hit
submit. You can keep editing and polishing your submission form on the Devpost website
too — **a good idea to double-check the AI's work and make sure it looks exactly how you
want it.**

Worth an hour before the deadline:

- **Read your project page like a judge.** Open it on Devpost and ask: would a stranger
  understand what this does in 10 seconds? For example, if your gallery opens with a
  screenshot of your terminal, swap in the one where the app is actually doing the
  impressive thing.
- **Add more screenshots or a short demo video** — projects with visuals get remembered.
- **Invite your teammates** on Devpost so everyone gets credit on the project page.
- **Share your public link** — momentum and feedback beat polishing in private.

That's everything — type `$hackathon-map` anytime to see where things stand.
```

The journey is complete, so never end this response with the "Say next" callout — the
anytime-offer line above is the closer (per `references/plugin-runtime.md`).

Respond with:

- the status line
- readiness result: `ready`, `close`, or `not ready` (when a review ran)
- security scan status
- missing inputs asked conversationally, one short question each, if needed
- when ready but not yet submitted: the explicit confirmation prompt described above (what will be submitted + "yes, submit?")
- when submitted: the **Offboarding** response (see that section) — celebratory heading, live deadline, the polish ideas, and the anytime-offer closer; never the "Say next" callout
- when a submit attempt failed: the specific failure, the sign-in note, and the official website URL to finish before the deadline

If you cannot read the content file, fall back to a compact text response:

- the status line
- readiness result and security scan status
- the confirmation prompt, missing-input questions, or the submission result as appropriate
- next recommended command
