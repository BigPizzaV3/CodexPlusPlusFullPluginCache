# Ten Year Journal plugin

Created by Codex GPT-5.6 Luna on 2026-10-02 14:59 PT on Jethro MBP (2).
Updated by Codex GPT-5.6 Luna on 2026-10-03 13:53 PDT on Jethro MBP (2).
Updated by Codex GPT-6 on 2026-10-05 16:00 PT on Jethro MBP (2).

This portable Agent Plugins package connects ChatGPT and Codex to Ten Year Journal at [adntbf.com](https://adntbf.com), the service also branded **A Decade Never to Be Forgotten**. It packages the journaling workflow and the remote MCP connection; account creation happens on the website, and the plugin does not create a second account or copy journal data.

This package is version `0.1.4`.

## Package contents

- `plugin.json` — portable plugin identity and OpenAI presentation metadata.
- `mcp.json` — the single streamable HTTP server at `https://adntbf.com/mcp`.
- `skills/ten-year-journal/SKILL.md` — the private journaling workflow and write-confirmation rules.
- `assets/ten-year-journal.svg` — the listing and composer icon.
- `scripts/verify_package.py` — local JSON/path validation and ZIP creation.

The MCP server uses OAuth. The read scope is `journal:read`; the write scope is `journal:write`. The backend currently exposes `get_profile`, `get_today_prompt`, `list_journal_prompts`, `get_journal_history`, `create_journal_entry`, and `update_journal_entry`. Creation refuses an existing same-prompt/year entry, and updates remain ownership-scoped.

## Install from this repository

1. Keep `.agents/plugins/marketplace.json` at the repository root and restart the ChatGPT desktop app or refresh the Codex plugin marketplace.
2. Open the Plugins Directory, choose the `ADNTBF Plugins` marketplace, and install `ten-year-journal`.
3. In ChatGPT, open the Ten Year Journal connection and continue to the `adntbf.com` OAuth page. Existing users choose **Log in**. New users choose **Sign Up**, enter the email and password directly on the website, approve the requested journal permissions on the website, then return to ChatGPT. Never enter a password in chat. See account onboarding below.
4. Start a new chat and ask for today's prompt, a bounded history view, or help preparing an entry.

The local marketplace is for development and direct distribution from this repository. A local install still needs the remote service to be reachable over HTTPS and the user to complete OAuth.

## Account onboarding

New users can create an account at the verified web form [adntbf.com/signup](https://adntbf.com/signup). The form asks for an email, password, and password confirmation. Enter the password directly on the website; never send it in chat. This plugin has no account-creation MCP tool.

Ten Year Journal and **A Decade Never to Be Forgotten** are the same service. In ChatGPT, if signup begins from the OAuth page and it offers a **Sign Up** link, use that link in the same browser so the pending connection request is preserved; after signup, approve journal permissions on the website and let the connection return to ChatGPT. For standalone signup, return to ChatGPT after signup and connect the existing account through its normal login/OAuth flow. Existing users should log in rather than create a second account.

Only report that an account is connected after an MCP call succeeds. If signup or connection fails, use the exact error shown on the site and do not collect passwords, tokens, or other credentials. The package makes no promises about verification emails, payments, notifications, or other outcomes that the site has not displayed.

After the MCP connection succeeds, welcome the user briefly: ChatGPT now reaches the same private journal data used at `adntbf.com`; they can ask for today's spiritual prompt and revisit responses to the same prompt across years. Preserve the user's words exactly, and write only after the user explicitly requests or confirms the exact save or update.

Try:

- “What is today's spiritual prompt?”
- “Show my responses to this prompt from prior years.”
- “Save this exact text for today's prompt: …”
- “Update my 2024 entry for this prompt with exactly: …”

## One-time ChatGPT server registration

For a ChatGPT developer-mode connection, register exactly `https://adntbf.com/mcp` in the Plugins/MCP settings, complete the OAuth flow, and copy the real technical ID returned by ChatGPT. It begins with `plugin_asdk_app`; do not invent one or copy an example ID.

The portable package intentionally does not contain `.app.json` or an `extensions.com.openai.apps` mapping. Those mappings are local compatibility wiring and must not be included in a public submission ZIP. After ChatGPT has returned a real ID, create a local ignored `.app.json` only if the host requires it:

```json
{
  "apps": {
    "journal_backend": {
      "id": "<paste the real plugin_asdk_app identifier returned by ChatGPT>",
      "required": true
    }
  }
}
```

Then point the local compatibility manifest's OpenAI `apps` field at `./.app.json`. Keep the file uncommitted. The portable `mcp.json` remains the source of truth for the public package.

## Validate and make a local archive

From the repository root:

```bash
python3 plugins/ten-year-journal/scripts/verify_package.py
python3 plugins/ten-year-journal/scripts/verify_package.py --zip
```

The second command writes the ignored archive `plugins/ten-year-journal/.dist/ten-year-journal-0.1.4.zip`. It includes the manifest, MCP configuration, skill, icon, and this README; it excludes the verifier, local compatibility files, and previous archives.

The validator checks JSON parsing, the stable package name, the exact MCP URL and transport, the skill and icon references, and the repository marketplace path. It does not replace an authenticated MCP smoke test.

## Public review status

Version `0.1.4` includes exactly five positive and three negative OpenAI review cases. Reviewer access uses a dedicated sample account; its credentials remain private and are entered through OpenAI's secure Review details form outside the ZIP. No real user data or password is stored in this repository.

The manifest now includes the public website, support, privacy, and terms pages: [adntbf.com](https://adntbf.com), [support](https://adntbf.com/help.html), [privacy](https://adntbf.com/privacy.html), and [terms](https://adntbf.com/terms.html). A captioned walkthrough using actual sample-account evidence is prepared at `https://adntbf.com/review/ten-year-journal-walkthrough-0.1.4.mp4`; hosting and URL verification are underway.

The final OpenAI review is still pending. No submission, approval, or publication is claimed here.

To prepare the package for review:

1. Run the validator and create the local `0.1.4` archive.
2. Connect the one declared MCP server, complete the domain-verification challenge on the `adntbf.com` origin, and wait for the tool scan.
3. Verify that the private reviewer account, five positive cases, three negative cases, and captioned walkthrough are available to the review team.
4. Submit the draft only after the hosted video and review details pass their dashboard checks. Hosted MCP tool changes are scanned separately after publication.

The package follows the portable root `plugin.json` and `mcp.json` format described in the official [plugin packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission guide](https://developers.openai.com/plugins/deploy/submission).

## Billing and access

The plugin has no billing or subscription MCP tool. It does not advertise prices, plans, or subscriptions or start checkout inside ChatGPT or Codex. If the journal MCP server reports that access needs to be managed, explain only that access is managed on the journal website. Do not claim that payment or access changed until a later MCP call returns the updated state.
