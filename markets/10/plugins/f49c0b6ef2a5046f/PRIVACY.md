# AdsGPT plugin privacy policy

Effective date: October 25, 2026

This policy covers the AdsGPT plugin for AI clients, such as ChatGPT, Codex, Claude and Grok, and
the AdsGPT MCP server it connects to (`https://mcp.adsgpt.dev`). AdsGPT is operated by Bee Holding SAS
("we", "us"). The plugin itself collects nothing on your device: it contains the skills the model
reads and the address of the MCP server. Everything below happens on the AdsGPT server when your AI
client calls one of its tools.

AdsGPT is a tool for advertisers to manage their own ad campaigns. It does not show ads to you or
inside your AI client, and it does not use your data for advertising.

## Personal data we collect

- **Account data:** your name, email address and the organization and role you have in AdsGPT,
  from your AdsGPT account.
- **Authorization data:** the AI client you connected, its OAuth registration, the access you
  approved (`ads:read`, `ads:write`) and the tokens we issued to it.
- **Ad platform connection data:** the credentials your organization's owner granted when
  connecting an ad platform, such as Google Ads, which we store encrypted. We never ask for or store
  your ad platform passwords.
- **Tool inputs:** what your AI client's model sends to each tool, such as ad account IDs, report
  periods, new campaigns with their budget, targeting and ads, ad texts, image URLs, YouTube links
  and landing page URLs. We never receive your conversation with the AI client.
- **Ad platform data:** the data of the ad accounts your organization connected, such as campaigns,
  ads, keywords, search terms, budgets and their performance, which we read through each platform's
  API when a tool needs it.
- **Technical data:** the IP address and the time of each request, for security and to limit abuse.

We do not ask for or collect payment card data, health data, government identifiers or passwords
of other services.

## How we use it

- To sign you in and to act only for the member, organization and access you approved.
- To run the tools your AI client calls: read reports, make the changes you approve and create the
  campaigns you approve, in the ad accounts your organization connected.
- To keep, in your organization, a log of every change made to your ad accounts: what changed,
  what it had before, the member and AI client it came from, and the tool call that made it, with
  its input.
- To keep AdsGPT secure, prevent abuse, fix errors and provide support.
- To comply with the law.

We do not sell your data, use it for advertising, or use it to train AI models. When you use
AdsGPT through an AI client, the AdsGPT server does not send your data to any AI model provider:
the model that reads the results is your AI client's.

## Google API Services

AdsGPT's use and transfer to any other app of information received from Google APIs will adhere to
the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including the Limited Use requirements. We use Google Ads data only to provide the features you
request, we do not transfer it except as needed to provide them or as the law requires, we do not
use it for advertising, and no person reads it unless you ask us to for support, for security, or
as the law requires.

## Who receives it

- **The ad platforms your organization connected,** such as Google Ads, through their APIs and with
  the access your organization granted: the reports and changes your AI client asks for, and the
  images the tools upload to the ad account.
- **Your AI client and its provider,** such as OpenAI, Anthropic or xAI, which receive the results
  of the tools they call and handle them under their own privacy policies.
- **The websites of the images and landing pages you give by URL:** we download the images to check
  them and upload them to your ad account, and open each landing page a change sends to check that
  it works, without sending them any of your data.
- **Service providers that host and run AdsGPT,** such as cloud hosting and database providers,
  which process data only on our behalf and under confidentiality and security obligations.
- **Authorities,** only when the law requires it, and a buyer or successor of our business, under
  this policy, if AdsGPT is sold or merged.

## How long we keep it

- **Authorization data:** until the tokens expire or you revoke the AI client's access.
- **Ad platform connection data:** until your organization disconnects the platform.
- **Account data:** while your AdsGPT account exists. When you delete your account, we delete it.
- **The change log:** while your organization uses AdsGPT, so its members can review what was
  done. We delete it within 30 days of your organization asking us to.
- **Technical data:** with your sign-in sessions until they end, and in server logs for up to 30
  days.
- **Ad platform data:** we read it from each platform when a tool needs it and do not keep a copy,
  except what the change log contains.

Deleted data may remain in backups for a limited time until they are replaced. We may keep data
longer only when the law requires it.

## Security

- Every connection to AdsGPT uses HTTPS (TLS).
- AI clients sign in with OAuth 2.1 and PKCE, with tokens limited to the organization and access you
  approved; AdsGPT never sees your AI client's credentials.
- Ad platform credentials are encrypted at rest and never reach your AI client.
- Each member acts with the permissions of their role in the organization, and every change to an ad
  account is recorded with the member and the AI client it came from.
- Access to production systems is limited to the people who need it.

No system is completely secure. If a breach affects your personal data, we will notify you and the
competent authorities without undue delay, as the law requires.

## Your choices and controls

- Every tool that changes an ad account tells your AI client so, and your AI client decides whether
  to ask for your approval before it runs, as its settings say. New campaigns are created paused
  unless you ask otherwise.
- Revoke an AI client's access from AdsGPT, or remove the AdsGPT plugin or server from your AI
  client, at any time.
- Disconnect an ad platform from the **Plugins** screen of AdsGPT at any time. You can also revoke
  AdsGPT's access from your Google account at
  [myaccount.google.com/permissions](https://myaccount.google.com/permissions).
- Delete your AdsGPT account from your profile settings.

## Your rights

Depending on where you live, such as in the European Economic Area, the United Kingdom or
California, you may have the right to access, correct, delete or export your personal data, to
object to or restrict how we process it, and to withdraw a consent you gave. We do not sell or share
personal data for cross-context behavioral advertising. To exercise any of these rights, write to
[hello@adsgpt.dev](mailto:hello@adsgpt.dev): we answer within 30 days and will not treat you
differently for doing so. You may also complain to your data protection authority.

We process personal data to provide the service you or your organization requested (performance of
a contract), for our legitimate interests in keeping AdsGPT secure and improving it, and to comply
with legal obligations.

## International transfers

AdsGPT runs in the United States, and our service providers may process data in other countries.
When personal data leaves the European Economic Area, the United Kingdom or Switzerland, we rely on
appropriate safeguards, such as the European Commission's Standard Contractual Clauses.

## Business customers

When an organization uses AdsGPT, it decides which ad accounts to connect and who can use them, and
we process its data on its behalf. Organizations that need a data processing agreement can request
one at [hello@adsgpt.dev](mailto:hello@adsgpt.dev).

## Children

AdsGPT is not intended for people under 18, and we do not knowingly collect their personal data. If
we learn that we have, we delete it.

## Third-party services

The ad platforms you connect, such as Google Ads, and your AI client and its provider have their own
terms and privacy policies, which govern how they handle your data. We are not responsible for
their practices.

## Changes

We will update this policy when the plugin changes what it collects or how it uses it, publish the
new version here with its effective date, and notify you by other means when the law requires it.

## Contact

Bee Holding SAS, the operator of AdsGPT: [hello@adsgpt.dev](mailto:hello@adsgpt.dev).
