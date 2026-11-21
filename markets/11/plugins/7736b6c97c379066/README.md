# [<img src="https://s3.vpndetection.io/vpndetection-public/brand/mark.svg" alt="VPNDetection" height="28"/>](https://vpndetection.io/) VPNDetection Plugin for ChatGPT and Codex

[![version](https://img.shields.io/github/package-json/v/vpndetection-io/openai-plugin?filename=plugin.json)](CHANGELOG.md)
[![license](https://img.shields.io/github/license/vpndetection-io/openai-plugin)](LICENSE)

The official [VPNDetection](https://vpndetection.io) plugin for [ChatGPT](https://chatgpt.com) and [Codex](https://developers.openai.com/codex).

Ask whether an IP address belongs to a VPN, a residential, datacenter, mobile or public proxy, a Tor node, a privacy relay or web gateway, a hosting provider or a CDN, and look into any of the VPNDetection databases and which ones your organization holds.

## Getting Started

VPNDetection is in the plugin directory ChatGPT and Codex share: [add it from its listing](https://chatgpt.com/plugins/plugin_asdk_app_6accd4f290588191a74086b26d749253) and sign in when it asks. Codex also installs it from the command line:

```console
codex plugin marketplace add vpndetection-io/openai-plugin
codex plugin add vpndetection@vpndetection
codex mcp login vpndetection
```

The last line signs you in with your VPNDetection account, where you pick the API key Codex should use. Codex never sees the key: our MCP server uses it on your behalf, and requests count against that key's plan like any other API call. The database tools need a key with the `db.download` scope, which your organization's `Default` key has. The Codex CLI, its IDE extension and Codex in the ChatGPT desktop app read the same configuration, so one install covers all three. You need a VPNDetection account for this, but no paid plan: without one, every lookup returns `ip` and `is_vpn` with Tor and relay detection, where the address is and the network that announces it, and the first 100 each day return every field.

To disconnect Codex, run `codex mcp logout vpndetection`, or remove it under Connected applications at https://app.vpndetection.io/settings/account/sessions. Access ends within about a minute.

## What's in it

- The VPNDetection MCP server at `https://mcp.vpndetection.io/mcp`, with seven read-only tools: `lookup_ip`, `lookup_ips`, `my_entitlement`, `list_databases`, `database_metadata`, `database_checksum` and `list_downloads`.
- Four skills that say how to use them well:
  - `check-ips` checks one address or a list, and reads the result's `coverage` so a field your plan doesn't include is never reported as a "no".
  - `review-traffic` screens a signup, login or order export and keeps each verdict next to the record it came from.
  - `database-files` answers which databases you hold, how big they are, whether your copy is intact and why a download failed.
  - `analyze-database` explains a database's columns and sample rows, and in Codex analyzes a downloaded copy.

## Try it

- "Is 45.83.91.1 a VPN?"
- "Here's yesterday's signup export. Which accounts came from proxies or Tor?"
- "Which databases are we licensed for, and how big is the latest VPN build?"

## What it sends

The plugin runs nothing on your machine. ChatGPT or Codex sends the IP addresses and database IDs you ask about to `https://mcp.vpndetection.io/mcp`, which calls the VPNDetection API with the key you picked and returns the answer. Each request is logged against that key as any API call is. Our privacy policy is at https://vpndetection.io/privacy, and questions go to support@vpndetection.io.

## Other Libraries

There are official VPNDetection client libraries available for many languages including PHP, Python, Go, Java, Ruby, and many popular frameworks such as Django, Rails, and Laravel. See our GitHub at https://github.com/vpndetection-io for more.

## About VPNDetection

VPN Detection API: Accurate anonymity detection identifying VPNs, residential proxies, hosting servers, Tor nodes, CDNs, relays and more.

[<img src="https://s3.vpndetection.io/vpndetection-public/brand/mark.svg" alt="VPNDetection" height="64"/>](https://vpndetection.io/)

## License

This project is licensed under the [MIT License](LICENSE).
