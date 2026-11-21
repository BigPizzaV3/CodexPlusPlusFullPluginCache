# Connect before coaching

Use the learner's language. Keep connection and coaching in this one Academy
skill; do not announce loading a skill or send them to a separate setup skill.

1. If a successful authenticated Uptime call has already happened in this
   conversation, continue their question. Otherwise use the host's tool
   discovery and call `academy_connection_status` once. Do not search local
   folders, repository instructions, general memory or the web to connect.
2. The tool is protected by Uptime sign-in. Let the host show its native
   connection prompt when the tool returns an authentication challenge. Say
   only: "Sign in to Uptime to continue." Do not turn the tool's sign-in
   challenge into a list of settings instructions or a general learning answer.
3. The learner completes Uptime's sign-in page. Never request their password,
   magic link, code or token in chat. Respect cancellation. After sign-in,
   retry the status call once using the host's supported tools. If the host
   does not retry or refresh its tools, report that connection is still pending;
   do not start a loop or invent a successful connection.
4. Confirm connection only when the tool reports `authenticated: true`.
   If `learning_ready` is false, explain that sign-in worked but learning is
   unavailable; do not ask them to sign in again. Do not display identity IDs,
   membership flags or technical checks.
5. When ready, continue the question they already asked. If none, say:
   "You're connected. What would you like help with — AI, work or everyday life?"
   Use Uptime learning before giving a learning answer. Do not save invented goals.

If no connection tool or native sign-in action is available after one discovery
attempt, say: "Uptime sign-in isn't available in this chat yet. I can't connect
you from here." This is an installation failure, not successful setup. Do not
claim the ZIP is working, send the learner looking for an unverified settings
button, ask for reinstall/delete, or keep retrying. The host controls sign-in
and new-chat setup; this skill cannot create those controls or bypass them.
