# Authorized Security Review 1.0.1

A skills-only plugin for ChatGPT/Codex that guides an existing tool-enabled agent through authorized security research and HackerOne report drafting.

This is an independent adaptation of the evidence-first review approach discussed in this conversation. It is NOT the original Codex Security plugin, does not reproduce all 15 original skills, and is not an OpenAI or HackerOne product. It does not bundle the proprietary Codex Security files, server, logo, or publisher identity. The original export remains a separate archive.

## What is included

One complete skill with four focused references: program scope, connected tools, investigation/validation, and report format. It covers source review and scoped live web/API investigation using tools already enabled in the chat. There is no MCP server, executable scanner, hook, or credential in this package.

## Upload and installation

The ZIP contains one plugin folder with `.codex-plugin/plugin.json` and `skills/authorized-security-review/SKILL.md`. This compatibility layout is documented as supported.

For the portal at https://platform.openai.com/plugins, choose Create plugin and Skills only when offered, then upload the ZIP without extracting it. This creates a submission draft; it is not itself proof of installation in a personal ChatGPT account. Public listing requires review and subsequent publication. Do not submit public publication attestations until you have completed the publisher fields, tested behavior, and reviewed the actual submission.

For personal development, official documentation describes installation through a local marketplace on supported surfaces. Ask plugin-creator in the ChatGPT environment that actually runs your connected tools to register this extracted directory in a personal marketplace, then install from that local source and start a new chat. Local-source support varies by surface. If that interface is unavailable, do not assume the portal supplies a private installation shortcut.

The screenshot establishes access to the upload UI, not which private installation or testing features your ChatGPT Plus account exposes. Plus-specific installation was not verified for your account.

## Use

Enable this plugin and your existing Remote Desktop Commander connection in the same task. Select the installed skill through the @ picker if available, or ask to use Authorized Security Review. Example:

Use Authorized Security Review with my existing remote tools for this authorized HackerOne program: [program URL or supplied policy]. Read the scope and rules first. My target is [asset] and my requested task is [assessment or evidence validation]. Save report drafts to [folder].

The plugin checks the actual tools available; it does not assume your remote machine is the same machine hosting skill files. A missing connector must be enabled in that task. Supply program-specific rules at use time; no real target or private program data is bundled here.

## Verification status

Local manifest/skill validation and archive/reference integrity are checked when packaging. ChatGPT installation, remote connector interoperability, and live program testing have NOT been verified. The evaluation file contains proposed acceptance scenarios, not claimed executed tests.

## Official packaging references

- https://developers.openai.com/plugins/concepts/plugins
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/connect-chatgpt
- https://developers.openai.com/plugins/deploy/submission
