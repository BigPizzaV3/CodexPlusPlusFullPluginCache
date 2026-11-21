---
name: build-with-spark
description: Build and run a business on Spark with the Spark MCP tools. Use when the user wants to start or run a business online (a website, store, booking site or AI app with hosting, customer accounts, payments, email and marketing), or to change, check or publish one of their Spark projects, and the spark MCP server is connected.
argument-hint: [describe the site, app or change you want]
---

# Building with Spark

The `spark` MCP server works in a Spark project's chat the way the user would in Spark. A project is a whole business: its site or app, with hosting, customer accounts, payments, email and marketing built into the platform. Spark designs, writes and publishes the code, and you send the requests, follow the work and check the result. When invoked as a command, the user's request is "$ARGUMENTS".

## Examples

- `/spark:build-with-spark a booking site for my pottery classes`
- `/spark:build-with-spark add a pricing page with our three class packages to Harbor Tours`
- `/spark:build-with-spark check the Harbor Tours home page on a phone`

## Tools

| Tool | Use it for |
| --- | --- |
| `list_projects`, `get_project` | Finding the project the user means, and seeing its pages, its internal tools, what Spark is doing and any question it is waiting on. |
| `plan_project` | Starting a new project. Spark asks one question at a time and ends with a plan. Send the whole conversation every call, with Spark's replies exactly as the tool returned them. |
| `create_project` | Creating the project once the user agreed to the plan, with the plan and the conversation exactly as `plan_project` returned them. Call it once per project. |
| `send_message` | Every change to an existing project. Name the page (`page: "/pricing"`) or internal tool when the request is about one. |
| `get_turn` | Following a request. Pass `waitSeconds` (up to 50) and call again while it is still running. |
| `answer_question` | Answering Spark's question or approval with the user's choice. |
| `stop_build` | Stopping a request the user no longer wants. |
| `view_page` | Looking at the preview, one screen at a time, at `desktop` or `phone` width. |
| `attach_files` | Showing the upload card when the user wants to send files from their computer; pass the ids it gives you to `send_message` as `fileIds`. |
| `publish_project` | Publishing the newest version once Spark has finished and the user asked to publish. |
| `get_history`, `get_credits`, `whoami` | What happened lately, the plan and credits left, and which account is signed in. |

## How to work

1. **Find the project.** Use `list_projects` when the user names a project, and `get_project` to see its pages and whether Spark is busy.
2. **Send the request in the user's words.** Put the facts Spark needs in the message: names, prices, opening hours, the tone they want. Spark sees only what you send, not your conversation. Send links to files in `fileUrls`.
3. **Follow it.** Call `get_turn` with `waitSeconds: 50` until the status is `completed`, `waiting`, `failed` or `stopped`. A change usually takes a few minutes, and a new project's first build about ten. Tell the user what Spark is doing meanwhile; the result's `now` field says it.
4. **Bring questions to the user.** When the status is `waiting`, show the user Spark's question or approval and its choices, and answer with `answer_question` only with what they chose. When `get_turn` says Spark's project card shows buttons for it and the card is shown, say in one line that Spark is asking in the card instead of listing the choices again. Never approve on the user's behalf.
5. **Check the result.** After a change to the site, look at the pages it changed with `view_page`, at the width that matters (phone for most visitors), and compare them with what the user asked for before you say it is done. A finished request may also carry a picture of what changed.
6. **Publish only when asked.** Changes stay in the preview until the user publishes. Use `publish_project` when they ask.

## Good to know

- Building uses the user's Build credits. Check `get_credits` when a request fails for lack of credits, and point the user to their plan.
- Messages you send appear in the project's chat in Spark, so the user can continue there with the link each result gives.
- Spark can't delete a project or an internal tool. The user does that in Spark.
