---
name: zid-api
description: Answer Zid developer questions from the live docs at docs.zid.sa. Use when building a Zid app or integration, calling the Zid Merchant API, setting up Zid OAuth, scopes or webhooks, or reading a Zid API error.
---

# Zid API

Partners and merchants build on Zid through its public developer platform, and
its documentation at `https://docs.zid.sa` is the only source for how that
works. The docs change, so this skill holds no API facts of its own: it is the
procedure for finding them. Running store work through the Zid MCP tools, or on
a schedule, is the `zid-ops` skill.

## Ground rules

- The user's explicit instructions take precedence over this skill.
- Every endpoint, header, scope, parameter, limit, status code and event name in
  an answer comes from a docs.zid.sa page fetched in this conversation, and the
  answer links that page.
- Answer with documented endpoints only. When the user names one the docs do not
  list (seen in a browser, another tool or another integration), say it is not
  in the Zid developer docs.
- Secrets stay out of chat: client secrets, tokens and webhook credentials go
  into the app's secret store. In examples, write them as placeholders such as
  `<CLIENT_SECRET>`.

## Look it up

1. Fetch the index, `https://docs.zid.sa/llms.txt`. Each line holds a section
   path (such as `Merchant APIs > Orders`), a page title and the page's `.md`
   URL. Done when the index is loaded; if it cannot be fetched, say so and ask
   the user for the page instead of answering from memory.
2. Pick the pages. Every question needs the concept pages it touches (for
   example `Authorization`, `Rate Limiting`, `Responses`, the webhooks
   `Overview`) and the endpoint page for each call. Done when each part of the
   question has a page, or is noted as not in the index.
3. Fetch each page's `.md` URL. Endpoint pages carry the OpenAPI spec: server,
   method, path, headers, parameters, request body and responses. Some also
   list the scopes; when a page names none, say the scope is not stated there.
4. Answer from the fetched text: exact names as written, a link per page, code
   with secrets as placeholders. Where two pages disagree, give both with their
   links and say which one is the API reference.

Done when every fact in the answer links to a page fetched in step 3, and every
gap is named as not documented.

## Errors

For an error, ask for the status code and the full response body first, then
fetch `Responses` and, for sign-in and token errors, `OAuth Errors &
Troubleshooting`. Match the exact error text to the page; when it is not there,
say so and give the request and response the user would send to Zid.
