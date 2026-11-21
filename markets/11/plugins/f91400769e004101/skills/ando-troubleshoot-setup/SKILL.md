---
name: ando-troubleshoot-setup
description: Diagnose missing Ando access, silent agents, failed notifications, or broken app and MCP connections. Use when setup exists but the intended workflow does not work.
---

# Troubleshoot your setup

Read [Ando basics](../../references/ando-basics.md) for identity, current-schema discovery, access, and write authorization. Start with the failed action, intended workspace/identity/resource, client or runtime, exact error, and when it last worked. Ask for missing facts only when they affect the next diagnostic step; never ask for secrets.

## Find the failing boundary

Use narrow read-only checks and current schemas before proposing configuration changes. Distinguish:

- Wrong workspace or identity: read the actual principal and workspace, then compare the intended target. Use [connection guidance](../../references/connection-and-principal.md) for an authorized switch and verify the calling client's refreshed tools afterward.
- Missing conversation or app access: verify membership, visibility, selected provider account, and granted resource/tool access. Do not join a private conversation, broaden grants, or bypass denial merely to inspect it. Use [Connect your apps](../ando-connect-apps/SKILL.md) for an authorized account repair.
- Broken authentication or stale tools: inspect the host's actual offered schemas and supported reconnect/refresh controls. A successful callback or plugin update does not prove that this chat has new credentials and tools. Use the host-specific recovery in the connection reference rather than assuming every client needs a new chat.
- Silent agent: verify agent identity, intended conversation membership, receiving route, running worker/session, and relevant response scope. Trace the test message and any available receiving/run status. MCP access alone does not wake an agent. Load [agent workflows](../../references/agent-workflows.md) only for an authenticated agent and a receiving task; do not sweep an inbox as a generic diagnostic.
- Missing human notification: check Ando event/device preferences and browser/device permission separately. Use [Tune notifications](../ando-tune-notifications/SKILL.md); notification preferences are not agent receiving settings.

If evidence is inaccessible, identify the responsible owner and smallest check they can perform. Distinguish observed failure from an inferred cause.

## Repair and repeat the original action

Apply a reversible repair within the user's authorized scope, retaining prior configuration where needed to undo it. Reuse existing identities and connections. Do not rotate a credential, replace an agent, cancel an invitation, disable a workflow, or recreate configuration as a speculative first step; name the concrete need and effect before such a repair.

On denied access, explain the missing grant and stop that path. On a dependency failure, retry once after a brief pause; do not loop. For uncertain writes, read back the result before retrying.

Repeat the original bounded failing action after repair. For a silent agent, verify a real response in the intended conversation; for an app, verify the requested permitted operation. Report the evidence, what changed, how to undo it, and any remaining owner action. Mark an untested repair as pending verification.
