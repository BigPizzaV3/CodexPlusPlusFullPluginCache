# AI Server websites: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `hosting_list_servers` | ai_server_read | Wants the websites they can edit: Opus Growth hosting servers and connected WordPress sites. |
| `hosting_list_sites` | ai_server_read | Wants the websites hosted on their Opus Growth server. |
| `site_csp_reports` | ai_server_read | Wants the Content-Security-Policy violation reports of their hosted website. |
| `site_design_guide` | ai_server_read | Is building a site on the hosting server and needs the design-system playbook. |
| `site_form_submissions` | ai_server_read | Wants the contact form submissions of their hosted website. |
| `site_info` | ai_server_read | Wants a hosting server's web address, status and disk usage. |
| `site_list_files` | ai_server_read | Wants the files of their hosted website. |
| `site_preview` | ai_server_read | Wants a screenshot of a page of their hosted website. |
| `site_read_file` | ai_server_read | Wants to read a file of their hosted website. |
| `site_read_url` | ai_server_read | Wants to read any live web page as a browser receives it: status, headers and HTML. |
| `site_release_status` | ai_server_read | Wants the release safety state of their hosted website. |
| `site_seo_guide` | ai_server_read | Is building a site on the hosting server and needs the SEO and structured data playbook. |
| `site_versions` | ai_server_read | Wants the automatic version snapshots of their hosted website. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `hosting_add_site` | ai_server_create | Wants another website on their existing Opus Growth hosting server, on its own domain. |
| `site_create_release_tag` | ai_server_create | Wants an immutable release tag of their hosted website's source. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `hosting_configure_site_smtp` | ai_server_edit | Wants to set up the email relay that sends their hosted website's contact-form messages, or to see its current setup. Called with only the server it changes nothing; called with mail credentials it saves them at once (there is no preview step) and, unless send_test=false, sends one test email. |
| `hosting_create_trial_site` | ai_server_edit | Wants a temporary free trial website on an isolated hosting server. |
| `hosting_deploy_site_zip` | ai_server_edit | Wants to publish a whole website from a .zip file to their hosting server. |
| `hosting_install_site_starter` | ai_server_edit | Wants to install the site starter toolkit (Tailwind, GSAP and components) on a hosting server. |
| `hosting_remove_site` | ai_server_edit | Wants to remove an extra website from their hosting server. |
| `site_block_paths` | ai_server_edit | Wants to list or change blocked paths on their hosted website. |
| `site_db_backup` | ai_server_edit | Wants a backup of their hosted website's database. |
| `site_db_restore` | ai_server_edit | Wants to restore their hosted website's database from a backup. |
| `site_dns_records` | ai_server_edit | Wants to list or edit DNS records of a domain whose DNS is hosted on Opus Growth. |
| `site_edit_file` | ai_server_edit | Wants a small exact-text edit in a file of their hosted website. |
| `site_fetch` | ai_server_edit | Wants to download a file from a public URL onto their hosted website, optionally resizing or converting images. |
| `site_headers` | ai_server_edit | Wants to list or change the HTTP response headers of their hosted website. |
| `site_rebuild` | ai_server_edit | Wants to rebuild and republish a Next.js, Vite or CRA site from the source kept on the server. |
| `site_redirects` | ai_server_edit | Wants to manage 301 redirects on their hosted website. |
| `site_restore` | ai_server_edit | Wants to restore their hosted website, or one file or folder, from an automatic snapshot. |
| `site_tag_gateway` | ai_server_edit | Wants to read, enable or remove a first-party Google tag gateway on their hosted website. |
| `site_write_file` | ai_server_edit | Wants to create or overwrite a text file on their hosted website. |
