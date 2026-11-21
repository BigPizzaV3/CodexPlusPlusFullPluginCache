---
name: setup
description: "Use right after ChefBear is installed, or when the user asks to set up, connect or check ChefBear. Checks the connection with connection_status and shows how to use ChefBear to choose what to order."
---

# Set up ChefBear

Keep the whole reply under ten short lines, in the user's language.

1. Call `connection_status` once.
2. **Connected:** say so in one line, then say in plain words what ChefBear may do: save menus they show in the chat (at once, without using their scan allowance, or with a ChefBear scan when they ask), read their saved menus, show their order as a card for the staff, find saved menus by name (only when the scopes include menus:list), share or turn off menu links when they ask, and, only when the scopes include taste:read and taste:write, read and save their food tastes (likes, dislikes, allergies, diets) so its picks fit them: it reads them when food comes up, offers to save food tastes they mention and saves them only when they say yes, and says what it saved. If menus:list is missing, add one line: to ask about a menu they saved, open it in the ChefBear app and tap ⋯ › Ask ChatGPT about this menu. Don't tell them to update or reconnect for it.
3. Suggest three things to try:
   - attach a menu photo and ask "What should I order? Save it to ChefBear and show my order for the waiter.";
   - only when the scopes include menus:list: "What should I order from the last menu I saved in ChefBear?"; otherwise: open a saved menu in the ChefBear app and tap ⋯ › Ask ChatGPT about this menu;
   - only when the scopes include taste:write: "I don't eat cilantro and I'm allergic to peanuts. Remember that for next time."; otherwise: paste a ChefBear menu link a friend sent and ask what's worth trying.
4. **Not connected** (the tool asks to connect or can't authorize): tell them to tap Connect. ChefBear's page lists what ChatGPT may do, and they sign in there with Apple or Google. That creates their ChefBear account if they don't have one, so they don't need the ChefBear iPhone app and you never tell them to install it first. Only if they say they already use the app: they can tap Open ChefBear on that page instead (on a computer, scan the QR code with the iPhone camera), then tap Allow in the app. Accounts in the mainland China service region can't connect. When they say they're done, call `connection_status` again.
5. **Connected without the app:** when `connection_status` returns `scansLeftToday`, the account has never used the ChefBear app and gets that many ChefBear scans (`import_menu`) today; saving a menu you read (`save_menu`) and everything else is not limited. Say so in one line. You may add once that the ChefBear app scans menus with the camera and keeps the same account (the `app` link in the result); never present the app as required.
6. Never ask the user to paste a password, a token or a code into the chat.
