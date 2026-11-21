# Claude Cowork comment queue polling

Claude Cowork is useful for scheduled stewardship, but it is desktop-first.
Use polling for SecondPage comments.

## Setup

1. Install the `publishing-with-secondpage` skill.
2. Connect to SecondPage MCP.
3. Authenticate the MCP connection with OAuth, or use `SECONDPAGE_API_KEY` for
   a headless MCP client that cannot complete OAuth.
4. If recurring maintenance is requested and scheduling is available, configure
   a task for the agreed Pages and scope.

## Scheduled task instruction

```text
Check queued comments on the Pages covered by this maintenance task. Read each
relevant thread and evaluate its requests within the authorized scope. Follow
the publishing reference to read/export and update the complete bundle with the
matching base version. Reply in the relevant thread after changes; explain
blocked requests.
```

This is eventual follow-up. If the machine or app is not available, comments
stay queued in SecondPage until the next run.
