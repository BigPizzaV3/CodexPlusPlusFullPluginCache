---
name: plan-project
description: Plan a project as phases with checkable exit gates and open it in the CmdBrief Project plan panel, so the user can edit it and send it to a crew of coding agents on their Mac.
---

# Plan a project for a CmdBrief crew

Use this when the user wants to plan, scope or break down a project that a
crew of coding agents could build: a website, an app feature, a tool.

## Shape of a plan

- `title`: the project in a few words ("Online ordering for the bakery site").
- `done_when`: one sentence that is true when the whole project is finished.
- `phases`: 4 to 8, in order from start to release. Name each by its outcome
  ("Payments", "Kitchen view"), not by a date.
- `gates`: 2 to 5 per phase. A gate is something someone can check, with
  evidence: "Order form works on a phone", "Test payments go through in the
  sandbox". Never a task list ("write the code") and never a time.
- Each gate has an `owner`:
  - `you`: only the user can do or decide it: approve a design, connect an
    account, announce the launch.
  - `crew`: the agents can prove it with a build, a test or a report.
- Limits CmdBrief keeps: title up to 80 characters, `done_when` up to 300,
  phase names up to 60, gates up to 120, at most 12 phases and 8 gates each.
- Images (optional): a logo you generated or one the user attached. Pass
  them as the tools' inputs describe, with a `save_as` inside the project such
  as `assets/logo.png` and a short `note` ("App logo"). PNG, JPEG, WebP or
  GIF, up to 20 MB each and 50 MB together, at most 10. CmdBrief saves them
  into the project when the user confirms. Never put a file path in gate
  text; write "Header uses the logo" and pass the image.

## Steps

1. If the goal is unclear, ask at most two short questions first. Do not
   invent facts about the user's business or code; leave them out or mark
   them for the user to fill.
2. Call `cmdbrief_plan` with the whole plan, a new opaque `draft_id`, and
   `revision: 1`. It opens the Project plan view, where the user edits phases,
   gates and owners. Keep this draft ID for revisions of the same project;
   use a different ID for an independent draft.
3. Tell the user, in a line or two, what the phases are and which gates are
   theirs. Suggest edits they might want.
4. When the user asks for changes, call `cmdbrief_plan` again with the
   updated plan and the same draft ID, increasing the revision above the
   latest revision reported by the view. Include the complete current image
   set; omit removed images. The view also tells you about edits made there.
5. When the user asks you to send it ("send it to CmdBrief", "update
   CmdBrief"), call `cmdbrief_plan_send` with the whole plan, its images, draft
   ID and revision, and a new opaque `operation_id`. Retry a timed-out send
   with the same operation ID and unchanged content; use a new operation ID
   when the revision or destination changes. Pass `workspace_id` only when they name a workspace. For a new
   project, or when they ask for a new workspace, pass `new_workspace: true`:
   CmdBrief makes a workspace named after it, with its own folder, when they
   confirm. Left out, CmdBrief uses the workspace that already has this
   project, else a new one; the user can change it in CmdBrief before
   confirming.
   They can also press **Send to CmdBrief** in the view. Either way the plan
   only waits in CmdBrief until they confirm it there. Say where it went and
   that they confirm it in CmdBrief; never say work has started. If CmdBrief
   is closed, the plan waits in CmdBrief Cloud and arrives when it opens; say
   that instead. Read the operation receipt: `accepted` means CmdBrief
   staged it, `queued` means Cloud kept it, and `processing` means the result
   is still unknown. For `processing`, retry the same operation to recover
   its result; never claim it failed or create a second send automatically.
   For `cancelled`, `expired` or `rejected`, explain the returned reason and
   make any correction before a new send.
6. After opening a plan, end with a short offer: "Say *send it* and I'll send
   it to CmdBrief."

## Revising a project that already has a roadmap

Send the whole revised plan the same way. Confirming it in CmdBrief updates
the project's roadmap instead of starting over: a phase with the same name
and a gate with the same words keep their progress, new ones are added and
what you leave out is dropped. So keep the names of phases and gates that
have not changed, word for word, and change only what should change. The
project's lead then gets what changed.
