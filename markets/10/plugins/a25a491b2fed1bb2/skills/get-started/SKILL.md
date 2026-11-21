---
name: get-started
description: Open Wardrobe Pet after installation and guide a new user through saving their first garment.
---

Use the connected Wardrobe Pet account. Call `open_wardrobe_workspace` to open the full wardrobe inside ChatGPT. Use `browse_wardrobe` for filtered clothing searches.

If the connection requires login, use the plugin login flow and ask the user to sign in with Google. Do not ask for a server address, developer mode, an access key, or a local file path.

If the collection is empty, explain that each account starts with its own empty wardrobe. Ask the user for one garment photo or clothing details. Use the `catalog-wardrobe` skill to research and save that garment.

The workspace saves photos, clothing records, outfits, wear dates, styling rules, and trip plans. Use ChatGPT to suggest photo details, remove backgrounds, and create optional style previews. Follow the `catalog-wardrobe` skill to save source photos and actual image results. Do not request a separate image API key. If ChatGPT cannot create or return an image, state the limit and keep the original photo.

Preserve unknown sizes and uncertain identities. Use measurements that the user states. Do not estimate exact fit from a photo or height alone.
