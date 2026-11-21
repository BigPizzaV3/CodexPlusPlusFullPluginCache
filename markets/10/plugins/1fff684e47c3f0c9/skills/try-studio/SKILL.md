---
name: try-studio
description: Restyle a real photo of a restaurant's dish into a polished, full-size food photo with ServeStack Studio. Works without an account; one photo per person.
---

1. You need a photo of one of the owner's own dishes (uploaded or a public link) and the dish's name as on their menu. Never use a stock photo or someone else's food.
2. Each person gets ONE photo, so settle the details first: offer the looks (bright brunch, rustic table, dark slate, candlelight, clean white, summer patio) and the shape (3:4 for a menu, 1:1 for an Instagram post, 9:16 for a story), and confirm before calling.
3. Call `try_studio_dish_photo`. Keep the returned `guest_token` and `trial_id` for this chat.
4. The preview card shows progress and the finished photo. If you need to check yourself, call `get_studio_trial` after about 20–40 seconds until it's completed or failed. Tell them to save the photo — the link lasts 30 days.
5. If they've already made their photo, or Studio is busy, say so plainly. Don't suggest signing up or buying anything; if they ask how to make more, `about_servestack` tells them what ServeStack is and where to find it.
