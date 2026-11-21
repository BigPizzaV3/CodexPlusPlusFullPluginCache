---
name: butterspace-recipes
description: Use when the user asks Butterspace to open, list, add, save, edit or scale recipes. Works in this chat without an account, with optional Butterspace connection for existing recipes and cross-chat saving.
---

# Butterspace recipes

Use the Butterspace Account Connection's current tools for both chat-only recipes and optional account storage. Sign-in is not required to use the recipe card.

## First use: two choices, not forced sign-in

For "show my recipes" or "open Butterspace", call open_recipe_start. If the user explicitly requests chat-only mode or says not to access their account, call open_recipe_start with chatOnly=true, even when an account is connected. Do not call account tools in this mode.

In a fresh chat, omit library and existingChatLibrary. The phrase "show my recipes" is not evidence that a chat library exists. Do not ask a first-time user to reopen an earlier card, attach a library or recover a working copy. Include the COMPLETE current chat-only library only if one actually exists in this chat. Without a chat library or connected account, or on an explicit chat-only start, show the existing two-choice card and briefly say:

"No recipes in this chat yet. Add recipes from text, a photo or a spreadsheet, or connect Butterspace to load your existing recipes and save across chats and devices."

Do not claim the user's account is empty: it has not been queried. Unless chat-only mode was requested, an already connected account is read automatically. If the user supplies a recipe immediately, add it directly without making them go through the welcome choices. Only use existingChatLibrary=true when a library or recipe card was actually created earlier in this same chat and its complete working copy is now unavailable. Then ask them to select that earlier card; never invent an empty replacement or reconstruct a partial library.

## Recipes in this chat

Use add_chat_recipe, edit_chat_recipe, categorize_chat_recipes, scale_chat_recipe and build_chat_shopping_list for chat-only work. Category operations have separate tools: create_chat_recipe_category, rename_chat_recipe_category, remove_chat_recipe_category and replace_chat_recipe_categories. Use the corresponding create_recipe_category, rename_recipe_category, remove_recipe_category and replace_recipe_categories only for the explicitly connected workspace. A replacement applies the complete reviewed category draft; removal keeps recipes as Uncategorized. Pass the COMPLETE latest chat library with current library and recipe revisions. Only the first addition omits library/revision. Unknown quantities, units and yield stay null with clarification questions, never guesses.

When persistence=chat_only, say "Added to this chat" or "Updated in this chat", not "Saved to Butterspace". The card, model context and any supported widget state keep the working copy in this chat. Do not promise account synchronization or availability in another chat or device. Export is available as a separate backup, not a prerequisite for using the card.

## Connect only when chosen

When the user chooses Connect Butterspace or explicitly asks to load/save account recipes, call open_recipe_library or list_recipes with an empty argument object. If it returns an authentication challenge, invite the user to use ChatGPT's Connect control, sign in with Google and select their workspace. Leave approval to the user. Keep existing chat recipes in their card. Never copy, merge, replace or delete them on connection; ask before copying any recipe into account storage.

Use ChatGPT's native Connect, Sign in or Update access control when it is shown. It starts the authorization flow directly. Do not replace it with a Markdown link to the plugin directory or a normal Butterspace login page: neither completes ChatGPT account linking. Never construct or reuse OAuth authorization links, state, PKCE values or callback URLs. If the account tools are unavailable, report a host-connection problem, not an empty library or a successful sign-in.

Do not substitute the separate Butterspace Recipes Test (Cloud) prototype. Use the current connection's chat tools for guest work and its OAuth-protected tools for account work. Do not ask the user to paste, attach, import or recreate their saved account library to compensate for a missing connection. Do not claim the account is empty until the account-backed read succeeds.

## After connection

Account open/list results are a catalog: recipe names, categories, yields and revisions. Only IDs in loadedRecipeIds include complete ingredients and methods. Empty arrays on other entries mean details have not been loaded. Call get_recipe for the selected recipe before reading, explaining or editing it. Scaling returns that recipe only. Use export_recipes only when the user explicitly requests a whole-workspace export, never to fill the catalog automatically. Owners may connect; other members need an owner to allow team ChatGPT connections in Account settings and retain their normal role restrictions.

Pre-rollout approved member connections can remain active until the owner reviews the setting. Do not ask such a member to reconnect just because their role is Chef. Owner-disabled access needs an owner decision, not another sign-in attempt.

If this chat already has recipes, offer to save them to the connected workspace or keep them in this chat. Call review_chat_recipe_transfer with the COMPLETE latest chat library. Its card offers Save all, recipe selection and Not now. Nothing is copied until the user confirms in the card. Do not call add_recipe or edit_recipe to bypass this review, and do not call the app-only commit_chat_recipe_transfer yourself.

Matching recipes are skipped. Same-name recipes with different contents and changed earlier copies require an explicit Save another copy choice. Existing recipes and product prices are never overwritten. Missing ingredient products are created through the normal workspace save path. Missing measurements, ambiguous products, permissions or capacity may block a copy. Ask the user to clarify them; never guess or silently omit recipes.

Report only confirmed copy receipts. If the sequence stops, show its confirmed partial result and keep the remaining chat recipes. Reopen a fresh review before retrying; durable receipts prevent repeated copies, including when an earlier account copy has been edited or archived. The source chat remains a snapshot, not a second synchronized account editor. Open the account versions for subsequent account edits. Connection to another workspace requires a new review and explicit confirmation.

Read the workspace before saving or editing. Treat a successful empty recipes array as an empty workspace and offer to add a recipe. Confirm a save only when the tool reports persistence=account. A new chat uses the same account-backed read, not a reconstructed chat library. Never fall back to a chat-only change after an account save fails.

Report account data and card display separately. A successful tool result proves that recipes loaded or a change was saved, not that ChatGPT rendered the interactive card. Do not say the card opened unless the host confirms it. If the host shows a display error, say the account operation succeeded only when its result confirms that, and offer the card's Try again control. Never repeat a save, recreate a recipe, disconnect an account or ask for a ChatGPT restart just to retry card display.

For new recipes, clarify missing ingredient quantities, units and yield. Missing products are created by the existing workspace tool with unknown prices. Never invent prices or replace existing product prices. Use current revision tokens and a new operation ID for each deliberate change; reuse the exact ID and arguments only for retries. A conflict requires reopening and review. Leave billing, team management, photos and account deletion to the app.
