# Maximos public submission preparation — v0.2.7

Two skills with explicit privacy and capability boundaries and one public read-only HTTPS MCP endpoint. No private app bindings are included. Published website, support, privacy and terms pages and publisher-approved icon are included. All OpenAI-permitted countries are intended (countries []). Commerce is false; the public endpoint requires no reviewer credentials.

## Actual walkthrough and test evidence

Demo: https://gnosismediagroup.github.io/maximos/demo/

The combined October 4, 2026 video shows two v0.2.6 interactions (John of Damascus free-will retrieval and practical counsel for resentment), followed at 1:28 by the v0.2.7 sacramental-absolution refusal in a separate chat. The update adds boundaries to both skills; the underlying source retrieval workflow remains the same. Responses are actual. Unrelated sidebar and audio were removed. The earlier private-conversation test was blocked by ChatGPT and is excluded from this walkthrough; it remains Blocked, not Passed.

Five positive and three negative cases are declared in plugin.json. Prior direct tool rehearsals covered the five positive retrieval workflows, but are not exact saved portal-version end-to-end tests. The video covers the first two positive workflows and a successful visible absolution refusal. The clinical diagnosis negative remains Not run; the private-record negative remains Blocked by the host. The destructive source-deletion prompt was removed.

## Server protection and remaining setup

Server commit b5c24fc88587b257e63799dea38c8ca16fd2a95d restricts retrieval to approved distributable source IDs and excludes private/account-marked records. Local retrieval-function checks passed: public search/fetch works, six private/unapproved fixture records are excluded and unfetchable, and a missing approval manifest fails closed. HTTP transport and live deployment of this change remain unverified; the Cloud Run build is pending.

Exact saved portal-version cases, developer identity, live domain challenge, scans and developer-completed legal/policy attestations remain outstanding. This plugin has not been submitted for review. Domain verification needs the actual portal token at https://maximos-mcp-801127943231.us-east5.run.app/.well-known/openai-apps-challenge; no token has been invented or configured.
