---
name: property-video
description: Make a property listing video with siriusly from a listing link or from photos and a description.
---

Use the siriusly tools to turn a property listing into a video.

1. Call read_listing with the listing link. Without a link, call upload_listing so the user can add photos and a description.
2. Ask the user which kind of video they want: silent tour, narrated tour, guided walkthrough or presenter in the corner. Never pick one for them.
3. When the siriusly card is shown, let the user carry on in the card. It walks them through the presenter, script, options and cost.
4. Only call create_property_video after the user has seen and confirmed the cost from estimate_price.
5. Use get_video_status to show progress and the finished video.
