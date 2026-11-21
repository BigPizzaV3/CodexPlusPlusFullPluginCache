---
name: desktop-operator
description: Autonomous desktop automation, computer use, and OS window orchestration across Windows, macOS, and Linux via Project Extra.
---

# Extra Desktop Operator Skill

When operating the user's desktop screen:

## 1. Core Operating Principles
- **Live Glass Execution**: Physical mouse clicks, typing, and window manipulation happen live on the user's screen through Extra's outbound WebSocket connection.
- **Offline Client Detection**: If an action reports that the desktop client is offline, instruct the user to start their local client:
  - Run `extra connect` on the computer terminal.
  - If Extra is not yet configured, refer the user to https://extra.yantraos.com for setup instructions.
- **Compound Action Execution**: Batch related steps (such as launching an app, focusing the window, and typing input) without unnecessary conversational turns.

## 2. Available Tools
- `extra_screenshot`: Captures the screen frame and returns distilled interactive elements.
- `extra_launch`: Launches native applications (`calc`, `notepad`, `mspaint`, `explorer`, `edge`, `terminal`).
- `extra_click`: Moves the mouse smoothly and clicks on semantic targets or coordinates.
- `extra_type`: Injects native keystrokes and text into active windows.
- `extra_hotkey`: Dispatches keyboard shortcut combinations (e.g., `["ctrl", "c"]`, `["win", "left"]`).
- `extra_snap_layout`: Arranges windows side-by-side in sub-15ms.
- `extra_task_complete`: Signals task completion with visual confirmation on the glass.
