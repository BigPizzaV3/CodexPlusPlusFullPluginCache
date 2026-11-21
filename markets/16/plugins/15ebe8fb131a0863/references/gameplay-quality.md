# Gameplay quality standards

A playable vertical slice must offer a goal, an input-to-feedback loop, a challenge, a win/lose or completion signal, and restart. A 3D environment that only allows walking is a technical scene, not automatically a complete game.

Assess correctness separately from game feel:
- Correctness: controls, collision, timing, scoring, win/loss, progression and repeatability verified through tests.
- Responsiveness: input delay, jump buffering, camera smoothing, feedback timing; tune based on measured behavior.
- Difficulty: initial learning, rising challenge, recovery, checkpoints and challenge communication.
- Clarity: obvious interactables, objectives, reliable HUD, accessible control hints.
- Playability: no softlocks, impossible jumps, stuck states, infinite progress loops or camera traps.
- Fun: requires actual human playtest feedback, not an automated 'fun score'.

Keep mechanics in scope: new feature must reinforce the game’s core loop and be demonstrable in the first playable level.
