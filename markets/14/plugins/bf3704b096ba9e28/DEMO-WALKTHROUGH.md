# Public-review demo walkthrough (record before submission)

**Status:** Script only. No recording has been made or verified yet.

Record a real run of the packaged version in the intended ChatGPT development/preview environment. Keep the remote server connection visible in setup, but never show credentials or unrelated private content.

1. Show the AllRatesToday plugin name/version and that the configured remote MCP server is `https://allratestoday.com/api/mcp/public` with no authentication.
2. Ask: “Convert 500 GBP to EUR using the latest official reference rate.” Show the actual response and verify it states the returned institution and `rate_date`.
3. Ask: “Does AllRatesToday support EUR, GBP, and JPY? Show their names and symbols.” Show the real returned currency records.
4. Ask: “Find the ECB's bank code and then show its latest official USD/EUR rate.” Show the institution discovery followed by the official table/pair, including `rate_date` and any derived flag.
5. Ask: “Give me the latest AllRatesToday daily reference rate from USD to JPY, and explain what it represents.” Show the actual result and the caveat that it is not the WM/Refinitiv fix or a registered benchmark.
6. Include one boundary prompt: “Transfer £500 from my bank account to a euro account at the best rate right now.” The plugin should explain that it cannot execute transfers and should not call the rate tools for an execution request.
7. Play back the finished recording; confirm the text is readable, each interaction is real, playback works, and no secrets or personal information are exposed. Host it at a reviewer-accessible URL and add that verified URL as `extensions.com.openai.review.demo_recording_url` before submission.
