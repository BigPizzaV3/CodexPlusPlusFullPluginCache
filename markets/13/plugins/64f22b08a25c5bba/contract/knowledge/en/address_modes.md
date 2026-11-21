# Address modes: what a coding agent sees

Each address of a project (an exact origin such as
`https://staging.example.com`) has a mode that decides what a coding agent
connected over MCP sees from it. The owner sets it in Widget → Addresses; a
new address starts from its name (local and `.test` addresses Direct, staging
and dev addresses Team, the rest Public).

- **Direct**: the agent sees every comment from the address at once. Suits
  your own working copy.
- **Team**: the agent sees a thread only after someone on the team hands it
  over in the inbox (Hand to an agent), with an optional note on what to do.
  It gets the thread as it was handed over; a message added or edited later
  stays out until someone hands the thread over again.
- **Public**: a visitor's words never reach the agent. A person hands a thread
  over with a note saying what to change; the agent gets that note and the
  place on the page, and cannot reply to or close the thread.

For the agent:

- lists, searches and counts include only threads it may see, and a text
  search looks only at what it may read;
- replies, resolutions, pin statuses and review rounds work only on threads it
  may change: Direct ones, and Team ones as they were handed over;
- `get_next_steps` counts the threads waiting for a person to hand them over
  and asks the human to do it in the inbox;
- a review round's Needs fix item is work only while the agent may change
  every thread it links; `waitingThreadIds` names the others.
