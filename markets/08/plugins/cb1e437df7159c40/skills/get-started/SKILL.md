---
name: get-started
description: Connect or reconnect Instagram to Buzzfy, or fix a connection that fails. Use when the user wants to connect their Instagram, asks what Buzzfy can see or do on their account, or says connecting failed, got stuck, connected the wrong account, or a Buzzfy tool asked them to reconnect.
---

# Get connected

1. Call `ig_connection_status` first. It says whether Instagram is connected, which permissions are granted, which plan the account is on and which tools that plan includes.
2. If Instagram is connected and the user only wanted to know what works, answer from that result in a few plain lines: what they can do now, and what needs a paid plan or MAX. Stop there.
3. If Instagram is not connected, needs a reconnect, or the user reports a problem, call `ig_connect`:
   - Pass `problem` with the exact error text the user saw, in any language, when there is one.
   - Pass `want: "dms"` if they want help with DMs, `want: "comments"` for comments only, otherwise leave it out.
4. Lead with the `diagnosis` in plain sentences, then give the `next_steps` in order, with their links. Don't add steps of your own.
5. Once they say it worked, call `ig_connection_status` again and confirm which account is connected.

Instagram needs a professional account (creator or business) to connect. If the diagnosis says the account is personal, explain how to switch in the Instagram app before anything else.
