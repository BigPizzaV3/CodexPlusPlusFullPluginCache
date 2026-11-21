# Tag Manager: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `gtm_workspace_status` | tag_manager_read | Wants to see the changes waiting to be published in a Google Tag Manager workspace. |
| `list_gtm_accounts` | tag_manager_read | Wants the Google Tag Manager accounts they can access. |
| `list_gtm_containers` | tag_manager_read | Wants the containers of a Google Tag Manager account. |
| `list_gtm_permissions` | tag_manager_read | Wants to see who can access a Google Tag Manager account and at what level. |
| `list_gtm_tags` | tag_manager_read | Wants the tags in a Google Tag Manager workspace. |
| `list_gtm_triggers` | tag_manager_read | Wants the triggers in a Google Tag Manager workspace. |
| `list_gtm_variables` | tag_manager_read | Wants the user-defined variables in a Google Tag Manager workspace. |
| `list_gtm_versions` | tag_manager_read | Wants a Google Tag Manager container's version history and which version is live. |
| `list_gtm_workspaces` | tag_manager_read | Wants the workspaces of a Google Tag Manager container. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `connect_tag_manager` | google_ads_create | Wants to connect Google Tag Manager. |
| `create_gtm_container` | tag_manager_create | Wants a new web container in a Google Tag Manager account. |
| `create_gtm_tag` | tag_manager_create | Wants a new tag in a Google Tag Manager workspace. |
| `create_gtm_trigger` | tag_manager_create | Wants a new trigger in a Google Tag Manager workspace. |
| `create_gtm_variable` | tag_manager_create | Wants a new user-defined variable in a Google Tag Manager workspace. |
| `create_gtm_workspace` | tag_manager_create | Wants a new Google Tag Manager workspace to stage changes. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `delete_gtm_container` | tag_manager_edit | Wants to permanently delete a whole Google Tag Manager container. |
| `delete_gtm_entity` | tag_manager_edit | Wants to permanently delete a Google Tag Manager tag, trigger, variable or workspace. |
| `enable_gtm_builtin_variables` | tag_manager_edit | Wants to enable Google Tag Manager built-in variables such as Click URL or Form ID. |
| `manage_gtm_permissions` | tag_manager_edit | Wants to grant or revoke someone's access to a Google Tag Manager account or containers. |
| `publish_gtm_container` | tag_manager_edit | Wants to publish a Google Tag Manager workspace's changes live. |
| `rollback_gtm_version` | tag_manager_edit | Wants the live site to return to an earlier Google Tag Manager version. |
| `update_gtm_entity` | tag_manager_edit | Wants to edit an existing Google Tag Manager tag, trigger, variable or workspace. |
