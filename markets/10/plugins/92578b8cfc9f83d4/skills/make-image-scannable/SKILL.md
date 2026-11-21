---
name: make-image-scannable
description: Register an image or video with the IRCODE connector this plugin adds, so that pointing a phone at it, or asking an assistant about it, leads to their link. Use its tools whenever someone wants people to scan a poster, product, artwork or video and land on their site, wants to claim an image as theirs, or asks to make an image scannable.
---

# Make an image scannable with IRCODE

Registering changes nothing in the picture: there is no QR code or overlay, and
the image itself becomes the code.

1. Ask in one turn what to call it and whether it should link anywhere.
   Never take a title from what you can see in the picture, or invent a link.
2. Call the IRCODE connector's `ircode_register_image` with the image, by
   `image_url` or by `image_file` where your app can pass the file, plus the
   `title` and the `link_url` they gave. Pass `keep` when they want it to last,
   and `video` for a whole video. With nothing to pass, as for a video or a
   photo on their phone, call it without one and follow the result: it gives
   the person a way to send the file, and a `session_id` to call again with.
3. Report what the result says happened, not what you expected: it says whether
   the registration went into their own account or under IRCODE's for 24 hours.
