# CrumbPass menu tools

All tools act on the one restaurant the owner authorized. Names are matched case-insensitively.

| Tool | Use it to | Key arguments |
|---|---|---|
| `get_menu` | Read categories and active dishes with prices, labels and `hasPhoto` | none |
| `create_category` | Add an empty category | `name` |
| `create_menu_item` | Add one dish (creates the category if needed) | `categoryName`, `name`, `price`, `isVegetarian`, optional labels |
| `bulk_import_menu` | Add many categories and dishes at once | `categories: [{ name, items: [{ name, price, isVegetarian, description?, ...labels }] }]` |
| `update_menu_item` | Change one dish; only the fields you send change | `itemName`, `confirm: true` after exact change approval, optional `currentCategoryName`, `newName`, `price`, `description`, `isVegetarian`, `isActive`, `categoryName`, labels |
| `delete_menu_item` | Permanently delete one dish | `itemName`, `confirm: true` after showing the exact dish and receiving approval |
| `delete_category` | Permanently delete a category and its dishes | `categoryName`, `confirm: true` after showing category and impact and receiving approval |
| `clear_menu` | Permanently delete the whole menu | `confirm: true` (only after explicit owner confirmation) |
| `reorder_menu` | Set the order guests see | `categoryOrder`, and/or `categoryName` + `itemOrder` |
| `set_menu_item_photo` | Add or replace a dish photo | `itemName`, `aiGenerated`, `confirm: true` after exact image approval, and `image` (conversation file) or `imageUrl` (https) |
| `remove_menu_item_photo` | Remove a dish photo | `itemName`, `confirm: true` after owner approval |

## Labels (optional on create, import and update)

| Field | Values | Notes |
|---|---|---|
| `diet` | `veg`, `egg`, `nonveg` | Shown as the Indian food-label mark. Egg is not vegetarian. |
| `spiceLevel` | `0`–`3` | 0 not spicy, 1 mild, 2 medium, 3 hot. `0` clears. |
| `temperature` | `hot`, `cold` | How the dish is served. |
| `highlights` | `chefs_special`, `todays_special`, `special` | `[]` clears. |
| `offerNote` | text, under 80 characters | Shown behind an "Offer" label. `""` clears. |
| `note` | text, under 280 characters | Shown behind the dish's info button. `""` clears. |

On `update_menu_item`, labels you leave out keep their current values.
