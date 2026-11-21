---
name: qrbox-menus
description: Read and edit the user's QRbox QR-code menu through the QRbox tools. Use when the user wants to create a menu, turn a photo of a printed menu into their QR menu, change prices, add or translate items, add photos, mark items sold out, change the menu's settings or look, see what the menu is missing, get its QR code or check how often the menu was opened.
---

# Working on a QRbox menu

QRbox is a QR-code menu builder for restaurants, cafes, bars and hotels. Guests scan a code on the table and read the menu on their phone. The QRbox tools read and change the menus of the account the user connected. A change is live on the guests' menu as soon as it is saved: there is no draft.

## Before any change

1. Call `list_menus`. If the account has several menus and the user did not say which one, ask. If it has none, the user has just signed up: offer to create the menu with `create_menu` (see below).
2. Call `get_menu` for that menu. Every change needs the `establishmentID`, `categoryID` and `itemID` it returns; never guess an ID. For a large menu, pass `categoryID` to read one category.
3. Note the menu's languages. Texts are objects keyed by those language names exactly as `get_menu` lists them, for example `{"English": "Lentil soup", "Türkçe": "Mercimek çorbası"}`. The first language is the main one; every category and item needs a name in it.

## Common requests

**A new menu.** Ask for the venue's name, its currency and the languages the menu should be in (main language first), then call `create_menu` once. Each menu is a separate venue on the account, so create one only when the user asks for a new venue or has none, never a second one for the same place. A new menu is empty: fill it next, for example from a photo of the printed menu.

**A photo or PDF of a printed menu.** Read the categories, items, descriptions and prices from it yourself, then add everything with one `import_menu` call. Write the names as printed, in the menu's main language. An item with sizes ("small 90 / large 110") gets `priceOptions` instead of `price`; leave the price out when the paper shows none. Items already on the menu are skipped, never changed. Afterwards, tell the user how many categories and items were added and ask them to check the prices against the paper.

**Prices.** For one item use `update_item`; for several use `update_prices`, which saves all of them or none. Prices are plain numbers in the menu's currency, without a symbol. Send the new price, not the difference, and round the way the user asked. An item with price options is changed with `update_item` and its full `priceOptions` list. To raise or lower prices by a percentage ("everything 10% up, rounded to 5"), use `raise_prices` instead: it does the arithmetic and the rounding, for the whole menu or chosen categories, sizes included. Calling it twice raises twice.

**Translation.** If the language is not on the menu yet, add it first with `set_menu_languages`, sending the full list in order and the new language by its code (`de`, `fr`, `ar`). Then send the translated names and descriptions with `update_item` and `update_category`, keyed by the language name that `set_menu_languages` returned. Only the languages sent are changed.

**Photos.** Find candidates with `search_photos` (English search text works best), then put a photo on items or category covers with the `photo` field or, for many at once, `set_photos`. A photo fits only when it shows the same dish or drink; an item without a photo is better than one with the wrong photo. Only library photos can be used: a photo the user attaches to the chat cannot be uploaded.

**Sold out, hidden, order.** `update_item` with `soldOut` or `visible`, `update_category` with `visible`. Hiding or marking sold out takes something off the menu without deleting it. `reorder_categories`, `reorder_items` and `move_item` change the order and move items between categories.

**Settings and visits.** `get_menu_settings` and `update_menu_settings` cover the name, currency, contact details, Wi-Fi password, working hours and the note shown to guests (never a service charge: menus may not mention one); changing the currency changes the symbol only, not the prices. `get_menu_visits` returns how often guests opened the menu.

**The look.** Call `get_appearance_options` for the designs, their colour versions, which take a brand colour, and QRbox's cover photos, then set `theme`, `themeColor`, `brandColor` or `cover` with `update_menu_settings`. Describe the choice in words; the user sees it on the public menu.

**What is missing, and the QR code.** `check_menu` lists items without a price, photo or description, missing translations, empty categories and a missing logo or contact details: offer to fix what the tools can. `get_qr_code` returns the menu's QR code and a link to a large version for printing.

## Care

- Deleting a category or an item cannot be undone. Before `delete_category` or `delete_item`, say exactly what will be deleted, including the items inside a category, and offer hiding instead.
- After a bulk change, show the user the result (for example the new prices) so they can check it.
- If a tool reports that the menu's trial or subscription has ended, the menu can still be read but not changed; the owner renews it at qrbox.menu.
- These are done in the QRbox editor (`list_menus` gives each menu's `editorURL`), not through the tools: uploading the user's own photos, logo or cover, the menu's custom address, and deleting a whole menu.
