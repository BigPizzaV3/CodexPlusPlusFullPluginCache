# Quality gates

Use these checks when behavior becomes inconsistent.

## Activation
The skill should activate for:
- explicit reminders and tasks;
- scheduling;
- saving/recording durable information;
- retrieving prior persistent state;
- conditional monitoring;
- compound research + persist/action workflows;
- connected-app operations that form part of personal/work organization.

It should not activate merely because a topic happens to involve work, productivity, Notion, or planning.

## No-app-choice rule
Never ask the user to choose between Notion, TickTick, Calendar, Linear, Gmail, or Drive when the semantic type is already clear.

## No-fake-success rule
A natural-language response is not evidence that a write happened. Confirm success only from a successful tool result.

## De-duplication
Before making a second persistent object for the same thing, check whether it represents a distinct semantic object. A meeting and its preparation task are distinct; two copies of the meeting are not.

## Minimal state
Persist the smallest useful unit of state. Do not create notes for ephemeral chat content and do not stuff long research into task descriptions when Notion is the correct durable home.
