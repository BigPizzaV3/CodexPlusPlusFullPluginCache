# Model Compass display contract

## Supported behavior

- Quiet by default.
- Explicit thread-local on and off states, plus a one-shot companion request.
- One-shot `Show Model Compass` without changing the saved thread preference.
- Inline visualizations only when the current thread state permits them.
- A narrow companion visualization that remains usable if the user manually
  pops the active chat into a separate desktop window.
- Optional user-controlled **Always on top** for that popped-out chat.
- An awake ChatGPT desktop pet can show chat activity and return the user to
  ChatGPT.

## Unsupported behavior

- Detecting when the ChatGPT desktop app or a Codex chat is minimized.
- Automatically waking, hiding, moving, or repurposing a pet.
- Hosting plugin HTML inside the pet overlay or activity tray.
- Creating a persistent plugin-owned sidebar, overlay, or floating window.
- Changing desktop window state without an explicit user action.

## Product rule

Never simulate unsupported persistence. When a user asks for a minimized-only
companion, offer the manual Companion flow and state the capability boundary in
one sentence.

Official references:

- https://learn.chatgpt.com/docs/pets
- https://learn.chatgpt.com/docs/reference/settings#pets
- https://learn.chatgpt.com/docs/hooks
