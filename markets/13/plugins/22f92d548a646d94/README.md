# FounderBrain

FounderBrain analyses how one person talked in a meeting and compares it with 773 public interviews of founders and operators. You give your AI app a transcript of a pitch, an investor call, a sales call or an interview. FounderBrain returns the speaker's type, where they sit on four speaking styles, the well-known founder they sound most like, the habits that stand out, two things to try next time and one to keep. The app then coaches from it, using moments from the meeting.

The analysis describes one conversation, not a personality. Neither end of a style is better.

## What is in this plugin

- **The FounderBrain MCP server.** A remote server at `https://mcp.thinkreasonlearn.com/mcp`. It has no sign in.
- **The `coach-meeting` skill.** How to run an analysis of a transcript the user attaches or pastes, and how to coach from the result.
- **The `prepare-transcript` skill.** How to turn meeting transcript exports or caption files into one speaker turn per line, preserving speech except for the restricted details removed before transfer.

## Tools

| Tool | What it does |
|---|---|
| `check_transcript` | Lists the speakers in a transcript and how many words each said. Nothing is scored. |
| `analyse_transcript` | Analyses one speaker and returns the report as data. Supported chat apps also display the full visual report. The analysis usually takes under a minute. |
| `get_transcript_upload_command` | For terminal clients that run commands on the user's computer: returns a `curl` command for uploading a prepared temporary `.txt` copy of the speaker turns. The app reads and prepares the original locally first, leaving the original unchanged. It runs nothing itself. Chat apps use the direct analysis tool. |

None of them changes anything anywhere. The first two only read the transcript they are sent. `get_transcript_upload_command` reads nothing itself: the command it returns sends the file to FounderBrain when the app runs it.

## Try it

A made-up pitch to try it on, with Ana Ruiz, founder of Harbourline, and an investor called Tom: https://raw.githubusercontent.com/Vela-Research/founderbrain-plugin/main/examples/sample-transcript.txt

- "I'm Ana Ruiz. Here's the transcript of my seed pitch yesterday. Run it through FounderBrain and tell me how I came across."
- "I'm Ana Ruiz. I have a Series A meeting tomorrow. Run this last pitch through FounderBrain. What should I keep doing?"
- "I'm Ana Ruiz. Use FounderBrain on this investor call and tell me what to work on before the next one."

## Limits

- One transcript of up to 15,000 words.
- The person analysed needs at least 300 words of their own. Around 3,000 words gives a settled result.
- Each line should be one speaker turn, such as `Ana: We started in 2024 ...`. The `prepare-transcript` skill handles most exports.
- The service has usage limits, so at very busy times it may ask the user to try again a little later.

## Where your data goes

- Use transcripts you have the right to share. Self-coaching is the default; analysing someone else requires their knowledge and agreement.
- Before transfer, the agent is instructed to remove isolated restricted details such as passwords, payment-card data and government identifiers, and to ask for another excerpt when sensitive information cannot be separated. This is not a guarantee of complete detection. Reports describe the prepared text, so removals may affect scores.
- The transcript goes from the app to the FounderBrain server at `https://mcp.thinkreasonlearn.com/mcp` and nowhere else.
- It is scored on that server by our own model and deleted when the analysis finishes. We do not keep transcripts or reports, and we do not train on them.
- The report in the chat loads its script and fonts from the same server.
- Our logs hold word counts, timings and error types, never transcript text or names.
- The user's conversation in their AI app, including the transcript, is kept by the app's provider under its own terms.

The full privacy policy is at https://thinkreasonlearn.com/privacy and the terms of service at https://thinkreasonlearn.com/terms.

## Troubleshooting

- **"No speaker turns were found."** The transcript is not one speaker per line. Ask the app to prepare the transcript first.
- **"Only N words were found."** The person picked spoke too little. Try a longer meeting.
- **"Very high demand today".** The day's capacity is used up. Try again after midnight UTC.
- **"Busy".** The service is at capacity for now. Try again a little later.

## Support

Email support@thinkreasonlearn.com, or see https://thinkreasonlearn.com/founderbrain.

## Licence

See LICENSE.
