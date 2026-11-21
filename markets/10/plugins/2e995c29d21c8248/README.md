# ScanMalware plugin

Investigate phishing and malicious URLs with [ScanMalware](https://scanmalware.com) from
Claude Code, Codex and Gemini CLI. ScanMalware runs URLs through isolated analysis
environments, records what each page loads and runs, and keeps every public scan in a
searchable archive. This plugin connects your agent to that archive and teaches it how to
turn one phishing URL into the rest of its campaign.

No account or API key is needed.

## What it adds

- **The ScanMalware MCP server** (`https://mcp.scanmalware.com/mcp`, remote, no sign-in):
  145 tools, 143 of them read-only. Read a scan's verdict, network requests, IOCs, TLS and
  JARM details, detected technologies, hunting-rule (YARA) matches, DNS answers, OCR text and
  RDAP data; run advanced searches (SMQL) with facets and match counts; find related scans by
  domain, IP, ASN, JARM, favicon hash, screenshot hash, TLSH/ssdeep/sdhash fuzzy hash, OCR
  text, tracking key or JavaScript fingerprint; follow a name's DNS history and reverse DNS;
  list a scan's searchable values, compare up to 20 scans side by side and list the hosts
  seen for a domain; look up Certificate Transparency records; read what deobfuscating a
  page's scripts revealed and the analysis of files a page delivered; submit a new URL for
  scanning. The two write tools submit a URL for scanning and vote on a scan as safe or
  malicious. Overview: <https://mcp.scanmalware.com>.
- **The skill `pivoting-phishing-infrastructure-with-scanmalware`**: a procedure for
  expanding one phishing URL into its sibling hosts, and for avoiding the two mistakes that
  produce wrong conclusions:
  - giving a domain a verdict that belongs to someone else: a lure that only redirected to
    it (common for the brands phishing kits imitate), or another tenant's subdomain on a
    shared platform such as `github.io` or `pages.dev`;
  - blocking on a pivot that describes a hosting platform rather than an actor (shared
    IPs, ASNs and JARM fingerprints).

  Besides kit artifacts (script hashes, inline scripts included, favicon, screenshot,
  title), it pivots on the operator's own account keys, such as an analytics ID or a
  live-chat license in the page source, which follow the operator across kit rebuilds and
  hosting platforms. It counts every pivot in one request to tell a kit from a shared
  platform, turns the kept pivots into a host list, and includes a report template.

## Install

### Claude Code

```
/plugin marketplace add scanmalware/scanmalware-plugin
/plugin install scanmalware@scanmalware
```

The skill appears as `scanmalware:pivoting-phishing-infrastructure-with-scanmalware`.

### Codex

```
codex plugin marketplace add scanmalware/scanmalware-plugin
codex plugin add scanmalware@scanmalware
```

### Gemini CLI

```
gemini extensions install https://github.com/scanmalware/scanmalware-plugin
```

### Only the MCP server

In Claude, ScanMalware is also listed in the connectors directory. Any MCP client can
connect to `https://mcp.scanmalware.com/mcp` over streamable HTTP without credentials.

## What this plugin sends, and where

- **MCP tool calls** go to `mcp.scanmalware.com`, run by Triop AB. Each call sends its
  arguments (URLs, domains, IP addresses, hashes, scan IDs) there, and the server forwards
  them to the ScanMalware API at `scanmalware.com`. Requests are logged as described in the
  [MCP server privacy policy](https://github.com/scanmalware/mcp-server/blob/main/PRIVACY.md).
- **The skill's commands** call the ScanMalware REST API at
  `https://scanmalware.com/api/v1` directly, anonymously. They send the URLs, domains and
  hashes you investigate, and no credentials.
- **Submitting a URL** makes ScanMalware's scanner visit it, which the site's operator can
  see. A `public` scan lists the URL and its results in the public feed, visible to anyone
  and to search engines; an `unlisted` scan is reachable only through its link; a `private`
  scan needs a ScanMalware account. The MCP `submit_scan` tool requires you to choose; the
  REST API uses `public` when the choice is left out. Use `unlisted` for client targets and
  anything carrying a victim's email address or token.
- The plugin ships no scripts, runs no hooks, installs no packages and reads no
  environment variables.

ScanMalware's own terms and privacy policy: <https://scanmalware.com/terms>,
<https://scanmalware.com/privacy>.

## Support

Questions and bug reports: [GitHub issues](https://github.com/scanmalware/scanmalware-plugin/issues)
or <https://scanmalware.com/contact>. The MCP server's source is at
[scanmalware/mcp-server](https://github.com/scanmalware/mcp-server).

## License

[Apache-2.0](LICENSE). ScanMalware is operated by Triop AB, Sweden.
