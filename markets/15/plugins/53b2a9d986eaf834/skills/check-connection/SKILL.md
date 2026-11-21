---
name: check-connection
description: Check the PhoneStamp Portal connection when the user asks whether PhoneStamp is connected or which account is signed in.
---

Use the Portal connection's `mcp_ping` tool to check the connection. Do not substitute the PhoneStamp Internal connection if it is also installed.

Report whether the call succeeded. If the user asks which account is connected, use the identity returned by the tool. A successful ping does not establish access to every portal tool or permission to make changes.

If the Portal tool is unavailable or authentication fails, explain that the user needs to connect or reconnect PhoneStamp Assistant. Do not request passwords, client secrets or access tokens in chat.
