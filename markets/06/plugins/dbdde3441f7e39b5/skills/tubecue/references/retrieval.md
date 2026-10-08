# Retrieval and fallback

Read this reference when the direct helper fails, captions are unavailable, a preferred language is needed, or provenance is uncertain.

## Direct helper

Run from the skill directory or use an absolute path:

```bash
python3 scripts/fetch_transcript.py "<youtube-url-or-video-id>"
python3 scripts/fetch_transcript.py "<youtube-url-or-video-id>" --languages hi en
```

The helper uses the bundled `youtube-transcript-api` 1.2.4 package. It does not need a YouTube API key, browser, account, or video download. It uses YouTube's undocumented caption interface, so availability can change and cloud-hosted IP addresses can be blocked.

Successful output begins with provenance fields followed by `--- TRANSCRIPT ---`. Confirm `VIDEO_ID` matches the requested video. `LAST_TIMESTAMP` is the end of the final caption cue, not necessarily the exact player duration.

## Status codes

| Exit | Label | Meaning | Next action |
|---:|---|---|---|
| 2 | `INVALID_URL` or `USAGE` | Input is malformed | Ask for a valid YouTube URL or ID |
| 3 | `NO_CAPTIONS` | Captions are disabled or no track exists | State that captions are unavailable; do not invent content |
| 4 | `BLOCKED` | YouTube blocked the runtime IP | Use Tactiq |
| 5 | `VIDEO_UNAVAILABLE` | The video is unavailable or restricted | State the limitation; Tactiq may be attempted if the video is public |
| 6 | `DIRECT_RETRIEVAL_FAILED` | Network or upstream retrieval failed | Use Tactiq |
| 7 | `DEPENDENCY_MISSING` | Python `requests` is unavailable | Use Tactiq; do not install packages unless the user asks |

Keep raw errors and tracebacks internal. A shell DNS error is a route failure, not evidence that the video lacks captions.

## Tactiq fallback

For `BLOCKED`, `DIRECT_RETRIEVAL_FAILED`, or `DEPENDENCY_MISSING`:

1. Normalize the link to `https://www.youtube.com/watch?v=<video-id>`.
2. Open `https://tactiq.io/tools/youtube-transcript` in an interactive browser.
3. Paste only the public canonical YouTube URL and select **Get Video Transcript**.
4. Wait for the result page. Verify the matching video ID or title and a timestamped transcript list.
5. Select **Copy** and read the clipboard when possible; otherwise read the complete transcript from the page.
6. Confirm the copied header contains the matching title or URL and that timestamped lines reach the final cue.

A read-only page fetch cannot submit Tactiq's form. Switch to interactive browser/computer use rather than concluding that Tactiq failed. Do not use PickScribe, YTScribe, transcript-search pages, summaries, notes, or articles as substitutes for the transcript.

If neither direct retrieval nor interactive Tactiq is available, ask the user to paste or upload the transcript. Do not create an account, install an extension, buy a proxy, or request proxy credentials.
