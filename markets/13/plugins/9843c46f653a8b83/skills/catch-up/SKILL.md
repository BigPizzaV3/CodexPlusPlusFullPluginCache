---
name: catch-up
description: Use when the user asks what they missed in Woosh, what is new, or what needs an answer from them - unread chats, mentions, friend requests, invitations and plans coming up. Reads only, and sums up instead of listing everything.
---

# Catch up on Woosh

1. Start with the numbers: `get_unread_counts` for unread chats, activity and notifications, and `get_feed_summary` for what is new in the feed since the user last looked.
2. Read what needs the user first. Use `list_notifications` for mentions, reactions, join requests and invitations, and `list_friend_requests` for people waiting on an answer.
3. Then the chats with something unread: find them with `list_chats` and read the busiest few with `read_chat`. Reading a chat marks it read, as opening it in the app would, so say which chats you read.
4. Look ahead with `list_events`: what is coming up in the next days, and which invitations still have no answer.
5. Answer in a few short lines, most important first: what needs a reply, then what was decided, then what is coming up. Do not paste whole conversations. Times in the results are UTC: give them in the user's time zone.
6. Offer the next step (reply, answer an invitation, accept a friend request), and only do it when the user asks. Anything other people will see waits for the user's go.
7. If a tool is refused or not available, say so and tell the user where to see it in the Woosh app (`woosh_guide` says where). Do not try another way round it.
