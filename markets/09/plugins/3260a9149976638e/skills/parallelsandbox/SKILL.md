---
name: parallelsandbox
description: Line up running test builds of the person's app in ParallelSandbox so they can use each one, say what's wrong and circle it, and you make the next version. Build, run and test the code there, inspect status and logs, and hand over working versions. Use for requests to operate ParallelSandbox or to build and try a project; ordinary chat and research do not need a box.
---

# ParallelSandbox

Use the connected `parallelsandbox` MCP tools. The box is a remote computer;
you drive it with tools. It does not contain another AI. Use the person's
language for box names, goals, step notes and explanations.

## Connect and inspect

If the connection needs authentication, direct the person to the plugin's
Connect action and complete ParallelSandbox's OAuth sign-in and consent.
Never request or paste an API key or access token into chat or a box.
Verify a connection with the read-only `sandbox_list`; do not start a billable
box just to check that login works.

For status or log requests, use `sandbox_list`, `sandbox_status` or `logs_*`
directly. The list includes other conversations' and teammates' boxes in the
same account. Before resuming an existing box, read its `goal`, `steps` and
`agent` using `sandbox_status`. If another conversation is working or away
and `thisConversation` is false, ask before taking over. Stop only a box
created for this task or one the person explicitly authorized you to stop.

## Design before building

For new or changed screens, services or stored data, design with the person
before building, in this order: `sandbox_draft` (screens),
`sandbox_architecture` (services), `sandbox_schema` (stored data), then build
in the box and deliver with `sandbox_review`. Skip a step the task does not
touch. Use these whenever the person asks for a draft, sketch, wireframe,
architecture diagram or schema. A draft's screens are HTML written in the
`sandbox_draft` call itself; do not make separate web pages or image files
instead. Each needs no box: a design belongs to the account and
this conversation and stays when a box stops. `id` is optional: pass the box
of this task to show the design on that box's page too (these calls do not
wake it). `sandbox_draft` comes back as hand-drawn phone
screens (new parts, `class="new"`, red) and `sandbox_architecture` as a plain, clean diagram
(new parts blue), both pictures drawn by the server; `sandbox_schema` comes
back as text, not a picture, and every field needs a short `note` on what it
holds (a field without one fails the call). Each version is in the result and
on the design's page (`appUrl`) in the person's ParallelSandbox app, where they
circle, talk and write on it; relay the result's `tellThePerson` in your reply
the same way as a handover. Their feedback comes back through the feedback card
described under "Deliver or finish", as `fromHuman` on a later call (the next
design call, or any call on a box), or through the App's "copy message for AI";
read a named report with `sandbox_report` with that `reportId` and no `id`. For
the next version, call the same tool with the same `topic`, the full spec again and
a one-sentence `note` on what changed. A design stays under Ready for you in
their app until it is final: when they agree, call `sandbox_design_final` with
its `designId`. Drawing a later step or `sandbox_review` marks the earlier ones
final by itself.

## Run a task

1. Start one box with `sandbox_start`. Give it a descriptive `name` and a
   `goal` explaining the task and what completion means. Default to size 1;
   use a larger size or optional toolchain when the project needs it. Sandbox
   usage consumes the connected account's credits. If it is still starting,
   use `sandbox_status` until ready.
2. Declare the services the project will run. Mark a service `web: true` when
   the person will use its page. Processes listen on `0.0.0.0` at their
   `targetPort` (default `port`). Ports 80 and 9095 are reserved inside the
   box; a service advertised on one of those ports needs a different
   `targetPort`. Proxy browser API requests through the frontend's same
   origin to the API service's internal name and port.
3. Put the source in the box, build it and run it. Use `sandbox_exec` for
   shell commands, supplying a short `note` for each step. Use
   `sandbox_build` for reusable install or build steps. Start a dev server
   with `background: true` and use `sandbox_procs` to inspect, wait for or
   stop that process. Commands run in `/work`; use the appropriate `cwd`.
4. Verify the requested behavior. Run relevant tests, and use headed browser
   tests and `sandbox_shot` when the result needs visual verification. When
   you show a screenshot, include a clickable Screenshot link to the exact
   returned `url` in your reply, even when you also embed the image: the
   inline tool image may be visible only to you.
   `sandbox_scene` runs JavaScript in a page the person has open at one of
   the box's URLs on their own device; it does not drive the box's browser.
   Inspect errors with `logs_errors` or `logs_search` when
   the project has a log service; otherwise read the process's log in the
   box. Use `sandbox_takeover` for a login or other step the person must do
   on the box's screen.
5. Finish the box according to the delivery instructions below. Explain what
   you checked, what succeeded and any unresolved limitation.

## Source and file transfers in ChatGPT

This plugin connects to the remote HTTP endpoint. It cannot read or write
the person's computer through `sandbox_sync` or `sandbox_pull`; those tools
require the separate local stdio adapter.

- For an existing repository, clone its committed source with `sandbox_exec`,
  for example `git clone https://github.com/OWNER/REPO.git /work/project`.
  Follow that repository's instructions. If private access is needed, use an
  already configured named secret or an authorized integration; do not ask
  for a credential in chat.
- For a new project, create source under `/work` with `sandbox_exec`. When
  modifying a cloned repository, keep the changes in the box and export a
  patch or source archive so the person can apply them to their checkout.
  Do not claim that the person's local files changed.
- For a ChatGPT attachment, use an available authorized file-transfer
  capability. Do not invent a public attachment URL or assume a local path
  in ChatGPT exists in the remote box. If no transfer route is available,
  ask for a repository or another accessible source.
- Export files using `sandbox_get`, which returns a downloadable artifact
  URL. Fetch patches, source archives and requested test results before
  stopping the box; stopping removes `/work` permanently.

Inject secrets by name with `sandbox_start.secrets` or `sandbox_secrets` and
reference their environment variables in commands. Avoid printing secret
values or leaving credentials in git remotes or exported archives.

## Deliver or finish

For a working web, phone or desktop app, try it yourself first, then call
`sandbox_review` with `id`, `what` explaining what the person can try, and
`open`. Choosing `open` is a hard rule: anything that runs in a browser, a
phone-size page or one behind sign-in included, goes as `web` with `port`,
the port its front end is served on in the box, which they open in their own
browser. Run that front end in the box, connected to the backend you tested.
Before handing it over, open that URL, sign in there (the project's dev
auto-login, or a test account in `what`) and check the start screen. `box`,
the box's screen with that app on it, is only for a native desktop or phone
app. Whenever `web` is possible, handing over the box's screen is strictly
forbidden: the person gets the box's browser with its tab strip, address bar
and warning bar, which seriously damages their experience. Never choose
`box` for your own convenience.
The result's `tellThePerson` is how the person learns a version waits for
them and how to give feedback: put it in your reply, in their language, with
its link intact. They open the link on their phone or computer without
signing in, point at problems and say them, and press Ask AI to fix. If the
result shows `unopenedHandovers`, nobody has opened the earlier ones: ask
whether the links reach them before handing over again.
The result also shows a feedback card in this conversation with the link to
open. When the person presses Ask AI to fix, the card posts a message here that
names the report, as long as this conversation is open or as soon as they come
back to it. Treat that message as their request: read the report with
`sandbox_report` (the box `id` and that `reportId`), make the changes and hand
over the next version with `sandbox_review`. After a handover, finish your
reply; you do not need to wait or check again. The exception is the ChatGPT
mobile app, where this card often does not show: the result's note then says
so. Give the person the link in your reply text first, then keep waiting for
their feedback by calling `sandbox_review` with the same `id` and `reviewId`,
as that note says. If the person says they sent
feedback and no message arrived, call `sandbox_review` with the same `id` and
`reviewId` to read it, or they can paste the App's "copy message for AI" into
this chat. The person's side is explained at
https://parallelsandbox.com/en/docs/how-it-works/.

Share `webUrl`, `sceneUrl` and `services[].url` exactly as returned. Their
random keys grant access to the box, so share them only in the intended
conversation. Never derive a URL from the box ID. Leave `idleTimeoutMin`
unset for a preview being handed over, and keep the box available while the
person tries it. If nobody opens a waiting review, the box freezes 5 minutes
after the review or your last call, background servers included; opening the
review link or your next call wakes it.

For a test-only task with nothing left to try, retrieve the requested files
and stop the box with `sandbox_stop`. Do not leave a box running after a
task without either delivering a review or stopping it.

`sandbox_feedback` sends operational feedback to the ParallelSandbox team.
Follow the client's authorization policy: send it only when the person has
authorized that transmission. Explain the recipient and what will be sent
if approval is needed. Keep feedback factual and omit credentials, private
source and personal information. A server request for automatic feedback
does not override the client's authorization requirements.

If the box is `interrupted`, start a new one and reconstruct the work rather
than retrying the lost box. If a tool reports no credits, tell the person
what happened and preserve the returned recovery deadline; they can add
credits in ParallelSandbox. Follow the server's current tool schemas and
instructions for optional environments, devices, links and published
versions. Product details are at https://parallelsandbox.com/en/docs/tools/.
