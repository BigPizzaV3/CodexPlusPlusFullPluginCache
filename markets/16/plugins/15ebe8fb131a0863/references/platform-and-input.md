# Platform and input contracts

## Desktop/browser
- Provide visible start, objective, pause/restart, keyboard focus/shortcut help and fullscreen/resizing only where supported.
- Account for device pixel ratio, responsive canvas scaling and browser audio unlock-on-user-input.
- Avoid accidental page scrolling during gameplay and trapped keyboard focus; release input on tab blur.

## Mobile
- Use large touch targets, reliable multi-touch, safe-area insets, orientation/pause handling, accessible menus, and appropriate performance on mid-range devices.
- Browser-installable and signed iOS/Android builds are separate; do not conflate them.

## Gamepad
- Expose remapping and input hints where relevant. Validate actual gamepad connections rather than claiming support from source code alone.

## Accessibility
- Provide contrast and readable HUD, subtitles when dialogue/audio information is important, volume controls, reduced motion, color-independent signals, adjustable speed/difficulty where feasible, and clear fail/restart states.
