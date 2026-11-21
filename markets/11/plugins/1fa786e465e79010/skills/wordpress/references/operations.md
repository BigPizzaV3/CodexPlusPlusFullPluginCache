# WordPress: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `list_wordpress_sites` | wordpress_read | Wants the WordPress sites connected through the Opus Growth Connector plugin, and their plan. |
| `wordpress_contact_forms` | wordpress_read | Wants the Contact Form 7 forms of a WordPress site, or one form's settings. |
| `wordpress_get_post` | wordpress_read | Wants one WordPress post or page in full. |
| `wordpress_list_plugins` | wordpress_read | Wants the installed plugins of a WordPress site. |
| `wordpress_list_posts` | wordpress_read | Wants a list of posts or pages on a WordPress site. |
| `wordpress_media` | wordpress_read | Wants to browse a WordPress media library. |
| `wordpress_menus` | wordpress_read | Wants to see a WordPress site's navigation menus. |
| `wordpress_page_design` | wordpress_read | Wants to inspect how a WordPress page is built (Elementor, WPBakery, Gutenberg or classic). |
| `wordpress_performance` | wordpress_read | Wants a WordPress site's caching and speed settings. |
| `wordpress_search_content` | wordpress_read | Wants the WordPress posts or pages that contain an exact text. |
| `wordpress_seo` | wordpress_read | Wants a WordPress site's SEO plugin settings. |
| `wordpress_site_info` | wordpress_read | Wants an overview of a WordPress site: theme, plugin count and WordPress and PHP versions. |
| `wordpress_tracking` | wordpress_read | Wants every place a WordPress site loads Google Tag Manager or Google Analytics. |
| `wordpress_woo_orders` | wordpress_read | Wants recent WooCommerce orders. |
| `wordpress_woo_products` | wordpress_read | Wants WooCommerce products with price and stock. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `wordpress_create_post` | wordpress_create | Wants a new WordPress post or page; it is created as a draft by default. |
| `wordpress_woo_create_product` | wordpress_create | Wants a new WooCommerce simple product. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `wordpress_bulk_replace` | wordpress_edit | Wants the same find-and-replace applied to many WordPress posts or pages. |
| `wordpress_core_files` | wordpress_edit | Wants to check, remove or restore the WordPress core information files (such as readme.html) that reveal the version. |
| `wordpress_critical_css` | wordpress_edit | Wants to check or regenerate LiteSpeed critical CSS for WordPress pages. |
| `wordpress_edit_menu` | wordpress_edit | Wants to add, rename, relink, reorder or remove WordPress menu links. |
| `wordpress_edit_page_design` | wordpress_edit | Wants to change texts, buttons, images or styles of an Elementor page. |
| `wordpress_full_backup` | wordpress_edit | Wants a full UpdraftPlus backup of a WordPress site, or its status. |
| `wordpress_install_plugin` | wordpress_edit | Wants to install a plugin on a WordPress site from wordpress.org. |
| `wordpress_languages` | wordpress_edit | Wants to see or add the languages of a multilingual WordPress site (Polylang or WPML). |
| `wordpress_link_translations` | wordpress_edit | Wants to connect WordPress pages or posts as translations of each other. |
| `wordpress_manage_plugin` | wordpress_edit | Wants to activate, deactivate, update or delete an installed WordPress plugin. |
| `wordpress_option` | wordpress_edit | Wants to read or change one WordPress setting by name. |
| `wordpress_purge_cache` | wordpress_edit | Wants to purge a WordPress site's page cache. |
| `wordpress_set_performance` | wordpress_edit | Wants to turn WordPress speed optimisations on or off. |
| `wordpress_set_seo` | wordpress_edit | Wants to set a WordPress page's meta title, meta description, canonical URL or indexing. |
| `wordpress_set_tracking` | wordpress_edit | Wants to set a WordPress site's Tag Manager or Google Analytics ID, or add tracking code. |
| `wordpress_slider` | wordpress_edit | Wants to read or fix Slider Revolution sliders on a WordPress site. |
| `wordpress_terms` | wordpress_edit | Wants to list or manage WordPress categories and tags. |
| `wordpress_test_contact_form` | wordpress_edit | Wants to send a test entry to a Contact Form 7 form. |
| `wordpress_theme_file` | wordpress_edit | Wants to read or edit the files of the active WordPress theme. |
| `wordpress_update_connector` | wordpress_edit | Wants to update the Opus Growth Connector plugin on a WordPress site. |
| `wordpress_update_post` | wordpress_edit | Wants to edit an existing WordPress post or page. |
| `wordpress_upload_media` | wordpress_edit | Wants to upload an image from a public URL to a WordPress media library. |
| `wordpress_users` | wordpress_edit | Wants the users of a WordPress site, or to change the name a user is shown under. |
