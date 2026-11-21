# Stripo Agent Plugin — OpenAI release 1.0.6

Create and edit native, editable Stripo emails with ChatGPT Work or Codex.
The plugin uses your authenticated Stripo connection and includes the email SDK and
editor validator. It does not send emails or schedule campaigns.

## Skills

| Skill | Capabilities |
| --- | --- |
| `email-from-reference` | Create an email from a brief, website, template, HTML, screenshot or supplied images; rebuild an explicitly selected email or template; verify saved desktop/mobile previews. |
| `email-model-editor` | Edit native copy, links, images, layout, styles, document title and preheader in existing emails and templates. |

Image generation and editing use Stripo MCP. Supplied images are hosted as original assets;
requests to inspect content do not start image jobs.

## Install and connect

This package updates the OpenAI plugin `app-6ab2a4a6b6008191a57909ccabc1ddae` from
1.0.5 to 1.0.6. It is built from Stripo Agent Plugin 0.14.2 (commit `fd80078`).
Install or update Stripo through the host's plugin directory and use its OAuth sign-in.
The package declares `stripo-mcp` at `https://mcp.stripo.email/mcp` in both MCP descriptors.

Requirements include Node.js 20.18.1+ and a host with shell, file, image inspection and MCP
tools. The shell examples use POSIX syntax. Keep the entire plugin directory together so
the local commands can find the SDK and transfer helper.

Run `node scripts/doctor.mjs` from the plugin directory to check the local prerequisites.
In a new agent session, use the read-only `whoami` check to verify the account and project
before editing. For connection help, see
[How to connect your AI assistant to Stripo](https://support.stripo.email/en/articles/15921958-how-to-connect-your-ai-assistant-to-stripo).

## Signed file transfers

`scripts/transfer.mjs` starts with ordinary host permissions. It downloads authorized HTTPS
models, references and previews and stages files for Stripo using PUT. Both clients keep the
original request path and query, verify TLS, refuse redirects, bound response streams and
verify any supplied download SHA-256. The limit is 64 MiB or the smaller manifest/ticket
limit. Keep local files in the private task directory under system temp. Downloads replace
the destination atomically after verification. The JSON result includes the transport,
attempt count and HTTP status when known. See the [CLI and recovery rules](skills/email-model-editor/reference/stripo-acquisition.md#transfers).

- **Direct.** The host resolver must return only public addresses. Both clients connect to
  the same checked IP with certificate verification for the original hostname. A failed DNS
  lookup can be retried within budget. A direct transfer always needs a validated address.
- **Proxy.** The helper uses the host-configured HTTP or HTTPS proxy, including on Node 20.
  It selects `https_proxy`/`HTTPS_PROXY`, then `http_proxy`/`HTTP_PROXY`, then
  `all_proxy`/`ALL_PROXY`. Lowercase takes precedence within each pair. CGI ignores uppercase
  `HTTP_PROXY`. `no_proxy`/`NO_PROXY` supports comma-separated exact hosts, optional ports,
  `.domain` or `*.domain` for subdomains, IP literals, IP ranges/CIDR and `*`.
  Both clients use the selected route throughout the transfer.
- **Proxy destination policy.** On HTTPS port 443, GET and PUT can use the storage hosts
  `stripo-mcp-content-live.s3.eu-west-1.amazonaws.com`,
  `stripo-mcp-content-stage.s3.eu-west-1.amazonaws.com` and
  `stripo-mcp-content-dev.s3.eu-west-1.amazonaws.com`. PUT is restricted to these hosts on
  every route. Proxy GET also accepts `*.stripocdn.email` on port 443 for generated images.
  The wildcard matches one or more DNS labels below `stripocdn.email` (for example,
  `rf.stripocdn.email`). CONNECT trusts the configured proxy and its resolver to choose
  the destination IP for these Stripo names. Other reference hosts need an already-permitted
  direct route with public-IP pinning. Proxy credentials, if configured, go only to the proxy.
  Ticket headers travel inside the origin TLS connection.
- **Fallback.** Node runs first. An eligible DNS, connection, timeout or native transport
  failure can select curl once. A PUT can switch only before handing bytes to the origin.
  HTTP responses, access denials, cancellation and failed safety checks end that attempt
  path. An unavailable curl capability probe consumes no transfer attempt.
  Each attempt has a 60-second deadline covering DNS, CONNECT, TLS and the body.
  The total budget across clients and agent retries is two. If the primary entry cannot
  start, `scripts/transfer-curl.mjs` accepts the same CLI arguments and shares all guards.
  Both bundled entries require Node 20.18.1+. A host without Node needs an equivalent
  managed binding to transfer the file.
- **curl prerequisites.** curl 8.4+ enforces the byte cap even for unknown-length responses.
  HTTPS proxies also require the curl HTTPS-proxy feature. The helper disables curl's
  startup file, supplies the request target and headers through stdin, and keeps staged data
  in a private temporary directory. Node uses its configured TLS trust. curl uses its TLS
  backend defaults or the host's CA settings (`CURL_CA_BUNDLE`, `SSL_CERT_FILE`,
  `SSL_CERT_DIR`, or Node's extra CA bundle). With only `NODE_EXTRA_CA_CERTS`, curl reuses
  Node's effective roots on runtimes providing `tls.getCACertificates`. Older runtimes use
  the explicit extra PEM for that fallback, so its issuer coverage can be narrower.
  See the [curl size-limit documentation](https://curl.se/docs/manpage.html#--max-filesize).

## Examples

- "Create a Stripo email from this brief and check its saved desktop and mobile previews."
- "Change the CTA and image in this email, keeping the rest of its layout."

## Data and external services

The agent runs the bundled Node.js helpers locally and calls the authorized Stripo MCP server.
Email models, reference files, images and previews are downloaded to local task files using
short-lived URLs returned by Stripo or URLs authorized for the task. Candidate and unchanged base
models use separate upload tickets. After a write, the skill reads saved state and inspects fresh
desktop/mobile previews. Local files remain in the workspace until its owner or host removes them.

Stripo image generation/editing consumes the project's image quota. Image jobs receive the
requested prompts and authorized reference assets. Uploading or generating an image returns a
hosted URL; inserting it into an email requires a separate model write. A supplied image is not
permission to generate a substitute. The plugin carries no separate image-provider credentials.

Website references use the agent's authorized browser session. The destination receives normal
browser requests. This plugin has no hosted browser service, publisher proxy or background hook.
Host and external-provider data handling follows their own terms and settings.

See [Stripo privacy](https://stripo.email/privacy-policy/),
[terms of use](https://stripo.email/terms-of-use/) and [support](https://support.stripo.email).

## Limits and maintenance

Access depends on the selected project's permissions, available MCP tools and quotas. The plugin
cannot create templates, change external name/project/folder metadata, or rank emails by sending
performance. Missing capabilities and incomplete visual checks are reported explicitly; local
validation alone is not a successful save.

The package root is the installable plugin. `skills/` contains the two workflows.
`packages/` contains the bundled email SDK and editor validator. The SDK's `getContract()`
reports the editor revision and validator hash. Each skill's `HOST.md` explains local setup
and tool discovery. Development evals and marketplace configuration are available in the
[source repository](https://github.com/stripoinc/agent-plugin).

This package is distributed under the [Stripo Agent Plugin License, Version 1.0](LICENSE).
The pinned editor validator contains proprietary Stripo code; bundled third-party notices and
separately licensed components retain their own terms. The OpenAI plugin identifier is `app-6ab2a4a6b6008191a57909ccabc1ddae`.
