# Project continuity

Use at a new project task or when its Vision association is missing, inaccessible,
or ambiguous. A project is host context; a Vision is its strategic home, not a
second project object to create automatically.

## Resolve before strategic execution

1. Read the user-confirmed association in the host's persistent project
   instructions. For repositories, prefer `.visionboard/project.json` at the
   repository root and read that file directly: look in the project directory,
   then in each parent folder, up to and including the first folder that
   contains `.git`. Never read above that repository root, so another project's association is
   never inherited. The file is valid only when it is under 4 KB, holds exactly
   `schemaVersion: 1`, `projectName`, `visionId` (a UUID) and
   `organizationName` (each name non-empty, at most 160 characters) and nothing
   else. Treat any other content as invalid and ask; do not repair it. Reading
   it needs no credentials, sends no paths and modifies no files.
2. Verify that exact `visionId` using `list_vision_hubs({visionId})` and verify
   the returned organization name. If inaccessible, do not select another Vision
   or create a replacement: report the access/association problem.
3. Without a pointer, call `list_vision_hubs` for the granted organization.
   Follow `contextBrief.discovery.nextOffset` until `complete` is true. Its
   `query` filters Vision titles; approved-content search is not a complete
   Vision directory. If the server has no discovery metadata, do not infer
   absence from a short result: ask the user for the Vision or update the client.
   If `limitReached` is true or no next offset is available while incomplete,
   disclose the incomplete search and ask for a more specific Vision; never loop
   on the same page or claim that no match exists.
4. Compare project name/purpose with available Visions. Name similarity is a
   candidate, not authorization. Ask once to confirm the association if it has
   not already been explicitly provided; always ask on multiple plausible
   matches. Check other already-authorized organizations when relevant, never
   request broader access merely for discovery.
5. When nothing matches after complete discovery, do not decide the next step
   yourself: the server states it. Read `contextBrief.discovery.whenNoMatch`
   and check `contextBrief.visionCreation` before proposing anything.

   - `offer_new_vision` — this grant covers the organization, so nothing fits
     anywhere the person could have meant. Say that plainly and offer to
     prepare a new Vision for this project, using the project's name as the
     proposed title. This is the expected path for a genuinely new project, not
     an exception to avoid.
   - `ask_link_or_create` — this grant is narrower than the organization, so an
     empty result proves nothing. Never claim no Vision exists. Ask the one
     question that resolves it: link an existing Vision through VisionBoard's
     own access controls, or create a new one and connect it. Linking is the
     person's action in the product; you cannot widen your own grant.
   - `continue_discovery` — pages remain. Keep paging before concluding.

   When `visionCreation.requiresUpgrade` is true, the plan has no room for
   another active Vision. Creating one anyway succeeds and is then plan-locked,
   leaving the person with a Vision they cannot use. Explain that limit and
   offer to continue in an existing Vision. Never promote upgrades or initiate
   a purchase through the plugin. Creating a Vision always requires the normal
   exact human authorization; none of these branches is permission to create.

   Guardrails for the offer to create a Vision:

   - Offer it once per conversation, as one short question that names the
     proposed title. If the person declines or continues without one, do not
     ask again in that conversation and do not store the refusal in the pointer
     (its schema stays fixed).
   - Preparing is not creating: the exact human authorization step still
     decides, and nothing is created, linked or written to the pointer before
     it. Never offer a Vision as a side effect of an ordinary task in a project
     that already has an association.
   - Never offer it when `visionCreation.requiresUpgrade` is true, and never
     mention plans, prices or upgrades in the offer.
   - After a Vision is created and confirmed, save the association as in step 6
     so later chats do not ask again.

   Older servers omit these fields. Then keep the conservative path: offer to
   prepare one, never assert that none exists outside the grant, and say that
   the connection cannot see the whole organization.
6. Persist a confirmed association in the host's project instructions so every
   new chat receives it. In a coding project, with permission to edit project
   configuration, use `.visionboard/project.json` with only `schemaVersion: 1`,
   `projectName`, `visionId`, `organizationName`; add a short instruction in the
   existing agent entry point to read it at project-task start. In hosts without
   project files, use their supported persistent project instructions. Never
   edit global instructions or unrelated projects as a side effect. Confirm
   where it was saved; if no durable mechanism is available, disclose that.

The pointer grants no access, contains no token or copied strategy, and must be
revalidated in new chats. Worktrees use the versioned project file; never fall
back silently to another checkout's association. The public plugin has no
hardcoded customer, organization or Vision.

## Close the strategic loop

Read the current Direction version and exact task-relevant revisions. At each
material decision and task completion compare **conversation outcomes**, not
just server versions, with that baseline. Pricing, audience, positioning,
constraints, product promises and success criteria are strategic candidates;
debug logs and code changes implementing unchanged strategy are not.

Within the user's write authority, update the existing strategic object rather
than duplicating it. Keep recommendations distinct from decisions and mark open
questions explicitly. Use attributed Drafts, exact base revisions, stable retry
keys and human Review. Check an uncertain write's receipt before retrying.

Choose the single completion surface in SKILL.md: exact approval card for ready
Review, explicit unsaved disclosure for a missing update, or a version check only
when no strategic update remains. Never show a green "current" card while a
conversation change is unrecorded. A late change after the card requires a new
reconciliation, not automatic approval of the previous set.

## Host boundary

Skills and MCP initialize instructions guide model behavior; they cannot force
every host to invoke a tool. Do not claim an always-on observer or guaranteed
cross-chat synchronization. Persistent project instructions improve discovery;
verify a fresh-chat test without the word VisionBoard in each supported host.
No periodic polling, Vela call or extra AI credit spend is needed just to find
the associated Vision. Browsing VisionBoard is optional, not the transport.
