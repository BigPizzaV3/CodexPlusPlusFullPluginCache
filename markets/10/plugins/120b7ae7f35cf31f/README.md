# iwantmyname Domain Search

Check domain name availability without leaving the chat, in ChatGPT, Codex,
Claude or Claude Code. Answers come live from iwantmyname's domain search, and
every available domain comes with a link to it on iwantmyname.

Ask in plain language, for example "Is sunnybakery.com available?", "Compare
mybrand.com, mybrand.net and mybrand.org" or "Suggest 5 names for a coffee shop
and check which .com domains are free". You get one clear answer per domain
(available, taken, or couldn't be checked right now) and a Continue link for
each available name that opens it on iwantmyname. International names
such as café.de work too. In Claude Code, `/iwantmyname:check <domain>` runs the
same check directly.

## What this plugin contains

- **A connector** to iwantmyname's hosted server at
  `https://mcp.iwantmyname.com/mcp`, which provides one read-only tool,
  `domain_availability_check`.
- **A skill**, `check`, that tells the assistant how to run the check and
  present the results.

Nothing runs on your machine: the plugin has no scripts, hooks or local
servers, and needs no account, API key or configuration.

## Data handling

- **Sent:** only the domain names you ask about, to
  `https://mcp.iwantmyname.com/mcp`, which is operated by iwantmyname. Your
  conversation, prompts and account details are never sent.
- **Stored:** nothing is saved or linked to you. Results may be held in server
  memory for a few minutes so a repeat check answers quickly. The server is
  hosted on Cloudflare.
- **Read-only:** the tool never changes, transfers or orders a domain. Anything
  further happens on iwantmyname.com, by you.

Privacy policy: https://iwantmyname.com/en/privacy

## Support

https://new.help.iwantmyname.com/hc/en-gb/requests/new

More: https://iwantmyname.com/mcp
