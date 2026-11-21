# Playbook

Connect Claude, ChatGPT or Codex to your [Playbook](https://www.playbook.com) workspace. Playbook is a media backend for creative teams, and this plugin lets an assistant search your images, video and documents, organize them into boards, tag them, upload new files, review version history, and share a board through a link or a published page.

## What is in the plugin

- **A connection to Playbook's hosted MCP server** at `https://mcp.playbook.com/mcp`. The tools run on that server, which calls Playbook's REST API as the user who signed in.
- **Five skills** that tell the assistant how to use those tools:
  - `get-started` finds its way around a workspace and its boards.
  - `organize-assets` searches, tags, sets custom fields, moves, archives and groups assets.
  - `upload-files` adds files from a URL, from bytes, or from Google Drive and Dropbox.
  - `share-and-publish` creates share links, published pages and permanent URLs.
  - `build-app` builds and hosts a small web app over one board, open to anyone, to the board's people or behind a password.

The plugin contains no executable code, hooks or scripts, and it runs nothing on your machine.

## Install

Claude Code:

```
claude plugin marketplace add playbook-labs/mcp-plugins
claude plugin install playbook@playbook-plugins
```

Claude on the web and the desktop app: open **Customize > Plugins**, choose **Add**, then **Add marketplace**, and enter `playbook-labs/mcp-plugins`.

Codex:

```
codex plugin marketplace add playbook-labs/mcp-plugins
codex plugin add playbook@playbook-plugins
```

## Sign in

The first time the assistant uses Playbook, a Playbook consent screen opens in your browser. Sign in and choose **Allow**. No API key is created, copied or stored in this plugin. In Claude Code you can also start this by running `/mcp`, picking the `playbook-creative` server and choosing **Authenticate**.

The assistant can then do what your Playbook account can do, in the workspaces that account belongs to. To end access, revoke it from your Playbook account settings.

## Data handling

- Your requests to the assistant stay with the assistant. The plugin sends Playbook only the tool calls the assistant makes: a tool name and its arguments.
- The server passes each call to Playbook's API and returns the result to the assistant.
- Playbook records usage analytics for each tool call in PostHog, linked to your Playbook user: the tool name, how long it took, whether it failed, and its arguments with passwords, upload credentials, note text and descriptions removed. Tool results are not recorded.
- Playbook's [privacy policy](https://www.playbook.com/privacy/) and [terms](https://www.playbook.com/terms/) apply.

## What it cannot do

It does not download a file's contents, read text inside an image, extract video captions, or render a board as a PDF.

## Help

- Full tool reference and setup for other clients: [dev.playbook.com/docs/guides/mcp](https://dev.playbook.com/docs/guides/mcp)
- Support: [playbook.com/contact](https://www.playbook.com/contact) or support@playbook.com

## If you added the server by hand before

A server registered earlier with `claude mcp add` connects a second time next to the plugin. Remove the manual entry:

```
claude mcp remove playbook
```

## License

MIT. See [LICENSE](./LICENSE).
