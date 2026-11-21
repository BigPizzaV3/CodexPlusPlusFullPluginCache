# Custom APIs: the owner's own systems as capabilities

Topic `custom_apis` · version 2026-10-25 · served by `uirix_guide({ "topic": "custom_apis" })`.

Connecting the agent to one of the owner's own systems (bookings, orders, a CRM, stock) through its API is set up in the UiriX dashboard, or from Claude, not in this chat. What can be done here: read what the agent already has, explain it, see it work in a test conversation.

```
GUIDE custom_apis: the owner's own systems as capabilities

GOAL
The owner knows what the agent does with their own systems and where to change it. A Custom API (the connection to the owner's bookings, orders, CRM or stock API, its key and the capabilities built on it) is set up, tested, trained and switched on in the UiriX dashboard (Custom APIs), or from Claude. In this chat you read what the agent has, explain it, and show it at work.

FACTS THAT MISLEAD
- No tool in this chat adds a connection, builds, tests, changes or switches on a capability.
- The key is never yours to handle: never ask for a key, a token or a password in the chat, never repeat one. If the owner pastes one anyway, do not use it: it is entered only in the dashboard.
- Read or write. A capability that reads looks up the owner's system; one that writes changes it (books, updates, opens a record), only after the customer confirmed the details.
- status: draft (saved, does not run), active (runs on the channels it is on), archived (removed). Active but not live means something blocks it: the connection's test failed, no channel is on, or the definition is in an old format.
- In a test_chat conversation a capability's reads call the owner's API for real and its writes are stand-ins: nothing is sent and the agent is told it worked.

READ FIRST
- get_agent_setup(agent_id): the custom capabilities with their status, channels and whether they are live, the connections, and the findings custom_connection_pending_secret, custom_connection_failed, custom_capability_not_live, custom_capability_untested, custom_capability_draft.

ASK
What the owner wants: to connect a new system or change a capability (the dashboard), to know what the agent can do with their systems (read it), or to see it work (a test conversation).

APPLY
- A new system or a change: say in one line that Custom APIs are set up in the UiriX dashboard, or from Claude. A connection that waits for its key: the owner enters it there, never in this chat.
- What the agent can do: each capability by its display name, what it does, read or write, its channels and whether it is live, and why not, from get_agent_setup.
- See it work: test_chat with a question a real customer would ask that should use it, after one line that it is billed and the owner's yes; then get_conversation: the tool turn shows whether it was called, with which arguments, and what came back.

MONEY
Paid: every test_chat turn (one line that it is billed, then an explicit yes). Free: get_agent_setup, get_conversation.

MISTAKES TO PREVENT
- Asking for the key in the chat, or using one pasted there.
- Telling the owner a write works because a test conversation said so: test conversations only pretend to write.

STOP WHEN
The owner knows what the agent does with their systems and where to change it, and the test conversation they asked for is read.
```
