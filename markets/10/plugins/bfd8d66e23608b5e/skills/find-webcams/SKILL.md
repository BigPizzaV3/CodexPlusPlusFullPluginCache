---
name: find-webcams
description: Find public scenic, animal, traffic and airport webcams with Webcam Live, inspect camera metadata, and get viewer links or existing thumbnails.
---

Use Webcam Live when the user wants to find public webcams or inspect a known public camera.

1. Use search_cameras with the place or name the user supplied. Add country/category only when useful. Traffic includes airports. Use pagination when necessary.
2. Use returned stable camera IDs with get_camera or get_camera_preview. Do not invent IDs or stream addresses.
3. For nearby searches, use coordinates supplied by the user or already explicitly provided for this purpose. If missing, ask for a place or coordinates. Never request browser geolocation permission automatically.
4. Return useful names, locations, reported status and the camera's viewer_url. Opening that link lets the user use the existing website. Do not claim video is playing within ChatGPT.
5. Thumbnails are existing previews, not fresh live captures. Always distinguish catalog retrieval time, status check time, and capture time. If captured_at is null, say the capture time is unknown. Do not assess current weather, road safety or emergencies from cached previews.
6. A reported status is a past check. Unknown status remains unknown. On an upstream error, say the public feed could not be read; never fabricate results or use private/withheld camera data.
7. This plugin has no write tools, private camera access, people identification, tracking, account credentials, or weather API. Do not use it for those purposes.
