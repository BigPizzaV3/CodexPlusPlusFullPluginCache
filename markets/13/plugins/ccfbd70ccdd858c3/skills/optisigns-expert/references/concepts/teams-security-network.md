# Teams, security and network

## Accounts, teams and folders

- **Account:** the billing boundary. One account never sees another's data.
- **Teams** (Pro Plus): separate workspaces inside one account, each with its own members, folders,
  content and optionally its own share of screen licenses. A user can belong to several teams and
  switch. A license held by one team isn't available to another, which can look like "maximum screens
  reached".
- **Folder permissions** (Pro Plus): give a user or team Edit or View on one folder. Admin roles see
  everything. Can't be turned off once enabled.
- **Sharing across teams:** change a folder's permissions to share it. HQ can share master folders
  down, or locations can share up.
- **External share links** (Pro Plus): share a playlist or asset folder with someone outside, with
  optional password and expiry.
- **Sub-accounts:** separate accounts under a parent for franchises or clients that need their own
  billing and owners. Use teams when the goal is shared content.
- **Trash:** deleted items stay recoverable for 30 days.

https://support.optisigns.com/hc/en-us/articles/18986181635859

## Roles

| Role | Can |
|---|---|
| Owner | Everything, including billing and deleting the account |
| Super Admin | All teams; create teams; billing |
| Admin | One team: invite users, manage screens |
| User | Create and edit content, add and remove screens, in folders they can access |
| Content Proposal | Upload and propose playlist changes; can't manage screens |
| Content Approval | Like User, plus approve proposals |
| Read Only | View only |

Custom roles are Pro Plus and can't be turned off once enabled.

## Sign-in and security

- **SSO (SAML)** on Pro Plus and above: Google Workspace, Microsoft Entra ID, Okta, OneLogin,
  Shibboleth. Choose authentication-only or full authorization (groups map to roles and teams on every
  sign-in). Keep a backup admin login.
- **Enforced SSO** works on the standard portal address, not on a custom branded domain.
- **SCIM** for deprovisioning can be turned on by request for SSO accounts. It deactivates or removes
  users when the identity provider does; it doesn't create users.
- **Multi-factor sign-in:** an authenticator app on every plan; SMS codes on Pro Plus (US numbers).
- **Audit logs** (Pro Plus, Owner and Super Admin): sign-ins and changes, kept two years, exportable.
- **Regional data residency** (Engage and above, enabled by support): US, EU, UK, Canada or Australia.
- **Disk encryption** on Pro Player and ProMax, set during a factory reset.
- **Security documents** (SOC 2 Type 2 report, data processing agreement, security overview) are
  available on request. Security questions: security@optisigns.com.

## Network and firewall

Players only make **outbound HTTPS connections on port 443**. Nothing inbound, nothing to
port-forward.

- **Allow the OptiSigns domains** on 443, including the software update and download domains. If
  updates are blocked, old content keeps playing but new content and fixes stop arriving.
  Full list: https://support.optisigns.com/hc/en-us/articles/360047275934
- **Some features need third-party domains** too (uploads, Designer images, remote control, sports
  feeds); they're in the same list.
- **Proxy:** allow the same domains on the proxy.
- **Enterprise Wi-Fi / 802.1X** (PEAP, EAP-TTLS): Pro Player, ProMax, Windows and Linux. Raspberry Pi
  needs Network Manager first. OptiStick 802.1X Wi-Fi is set from the portal:
  https://support.optisigns.com/hc/en-us/articles/44890229616403
- **Internal sites:** the site must be reachable from the player, and the company's root certificate
  installed on it. Supported on Pro Player, Windows, Linux, macOS and Chrome; not Android. Pro Player
  Gen 3 and ProMax need a `.crt` file.
- **The web player can't reach internal-only addresses.**
- **Static IP** can be set on Pro Player and ProMax.
- **No pair code, or online to the TV but offline to OptiSigns:** almost always the firewall. Test on
  a phone hotspot to confirm.
