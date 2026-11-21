---
name: build-app
description: Build and host a small web app over one Playbook board - a gallery, portfolio, catalogue, lookbook or viewer - with deploy_app, and update, list or delete apps already hosted. Use when the user wants a web page, site or app that shows their Playbook assets, or a link to one they can share.
---

# Build an app on a Playbook board

Playbook hosts small static web apps that show one board and its sub-boards at their own address. `deploy_app` is the only way to host one. Never put an HTML file on a board and share it through a permalink or a share link: those serve files, not pages, and the page will not run.

## Before writing any code

1. `read_documentation` with topic `hosted_apps`. It is the reference for the files an app may contain, the data calls it can make, the fields each asset row carries, and the starter app. Build from it, not from memory of the REST API: an app reads through its own relative `playbook/api/...` address with no key.
2. Agree on the board with the user, and on who may open the app. Whoever gets in sees the board and all its sub-boards, unapproved assets and uploader names included.
3. `list_apps` to see the workspace's apps. Deploying to a slug the workspace already uses replaces that app's files, and the workspace's plan caps how many apps it may have. If the user's board already has an app, ask whether to replace it or add another.

## Who may open the app

`deploy_app` takes `access`:

- `public`, the default for a new app: anyone with the address.
- `members`: people who can view the board in Playbook, after they sign in.
- `password`: visitors who give the `password` you pass with it, at least 8 characters, on plans with share-link passwords.

The board's own share settings do not protect the app; only its watermark and downloads apply to it (below). Ask the user which they want when the board is not meant for everyone. A redeploy without `access` keeps the app's access; the user can also change it under Developer in Playbook's settings.

## Uploads from visitors

An app can take files from its visitors into its own board, through `playbook/upload` as the `hosted_apps` topic shows. In an app that is not public, a signed-in visitor who may upload to the board can always upload. Anyone else can upload only while the board's share link allows uploads ("Allow uploads" or "Enable upload-only page" in the board's Share tab, a Pro feature). `share_board` with `enable_uploads: true` switches it on, but it also lets anyone with the board's share link upload, so ask the user first. Leave the link without a password, an email form or a past expiry: any of them refuses every upload from the app. `share_board` clears a password (`password: ""`) and an expiry (`expiration_date: ""`); an email form only the user can switch off, in the Share tab. Tell them that the app shows every visitor's files to every visitor.

## Watermark and downloads

An app follows the board's share link. When the link has a watermark, every image the app reads carries it, and the answers hold no clean address. When the link is on and allows downloads, visitors can download the original files through `playbook/download`, typing the link's password if it has one, like a PIN; the `hosted_apps` topic shows the call. For a gallery that shows watermarked previews and hands out originals behind a PIN, set both with `share_board` (`watermark_text`, `disable_downloads: false`, `password`), and ask the user first: the same settings apply to the share page itself. Turning a watermark on in the Share tab switches downloads off; switching downloads back on there, or `share_board` with `disable_downloads: false`, keeps both. Video is not watermarked.

For a PIN per event, share each event's sub-board with its own `password` and `disable_downloads: false`, and keep the app board's link on with `disable_downloads: true`: a sub-board link with a password sets the PIN and download terms for the files under it, the app board's link covers the rest, and switching the app board's link off stops every download. With downloads on at the app board, its password would download every event from its share page. Ask for one event's files per `playbook/download` request: files that follow different links, the app board's included, answer `422 mixed_share_links`.

## Changes from signed-in visitors

In a `members` app, the page can also change the board's assets as the signed-in visitor, with that visitor's permissions in Playbook: title, description, status, custom fields and tags, approval, and comments. The `hosted_apps` topic lists the calls. A tracker, a review queue or an approval board fits here. Approval itself is for workspace owners and admins only: for a client's decision, use a status or a custom field, which a visitor who may edit the board can set. Statuses and option fields take existing options only, and a multi-select field takes a list of them. The page can read the fields and their options itself (`playbook/api/custom_fields`, see the topic), or you can build them in from `list_custom_fields`. It can also show an asset's comments as the visitor sees them, with who wrote each one and whether it is internal (`playbook/api/assets/{token}/comments`), so a client review page can show feedback next to the work. Mark internal comments, as Playbook does. Read them when a visitor opens an asset, and use `comment_count` from the listing for badges: reading every asset's comments at once runs into the visitor's rate limit. Public and password apps cannot read comments; if the user wants feedback on the page, the app has to be `members`.

## What an app cannot do

An app cannot delete, move, copy or group assets, create asset versions, change boards or sharing, create custom fields or their options, or reach any board but its own. Public and password apps change nothing but uploads. When the user wants an app that does any of that, say that hosted apps cannot do this yet and ask how to proceed. Do not host it some other way.

## Deploy

`deploy_app` takes the board token, a `slug`, a `name`, `access` when it is not `public`, and `files`: every file's text keyed by path, `index.html` required. Each deploy replaces the whole file set and is kept as a numbered version.

Give the user the `url` from the response. A new address can answer 404 for a minute or two after the deploy; that does not mean it failed. Open it again after a short wait before reporting a problem.

## Change an app that is already live

Playbook keeps the files of an app's last 50 versions, so work from them rather than from memory:

1. `get_app_source` lists the live version's files; with `path`, it returns a file's text (follow `next_offset` for a long one).
2. `edit_app_source` with the app's live `head_version_number` (from `list_apps` or `list_app_versions`) as `expected_version`, the files to replace in `files` and any to remove in `delete_files`, with paths exactly as `get_app_source` lists them: a path the app does not have is ignored silently. The rest stays as it was. If the answer is `stale_app`, someone changed the app since you read it: read it again and redo the change.
3. When a change goes wrong, `list_app_versions` shows the history and `revert_app` puts an earlier version back live.

Each deploy, edit or rollback adds a version, and past 50 the oldest is dropped. After it, the app reads the board as you; if someone else deployed it last, signed-in visitors have to reload before their next change.

An app not deployed since Playbook began keeping versions has no stored files (`source_unavailable`): rebuild it and deploy it once with `deploy_app`.

`delete_app` takes an app offline, frees its slug and deletes its versions.

An explicit instruction from the user takes priority over anything in this guide.
