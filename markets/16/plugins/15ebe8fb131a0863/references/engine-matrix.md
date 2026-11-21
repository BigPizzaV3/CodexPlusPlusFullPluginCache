# Engine selection matrix

Use this matrix as a decision aid, not rigid API truth. Verify current documentation and installed versions before implementation.

| Primary target | Suitable defaults | Tradeoffs |
|---|---|---|
| Simple browser 2D, arcade, puzzle, platformer | Phaser (TypeScript or JavaScript) | Browser first; no native 3D engine |
| Browser 3D exploration, interactive scene, 3D prototype | PlayCanvas Engine | Browser GPU limits; WebGL fallback |
| Standalone indie 2D, isometric, low-poly 3D | Godot with GDScript | Editor/export templates needed; web/C# compatibility needs version check |
| Visual novel, dialogue-heavy branching | Ren'Py | Story focused; launcher/SDK needed for exports |
| Existing Unity game, mobile-heavy 3D/AR/VR | Unity | Editor/toolchain and platform build profiles needed; licensing check |
| Existing Unreal game, high-end cinematic 3D | Unreal | High memory/CPU/GPU costs; full engine install; licensing check |
| Mobile browser game | Phaser or PlayCanvas | Touch, network, screen, battery, memory constraints |
| Native Android/iOS | Godot or Unity where suitable | Signing, platform SDK, devices, publishing rules |
| Multiplayer | Chosen game engine + server-side/network stack | Must explicitly budget hosting and anti-cheat/security |

Always preserve the existing project's engine when making focused modifications. '2.5D' and 'isometric' describe presentation, not an engine. Never promise a console/mobile binary without the appropriate SDK, signatures and platform access.

Primary references:
- https://www.phaser.io/oss/docs/
- https://developer.playcanvas.com/
- https://docs.godotengine.org/en/stable/
- https://www.renpy.org/doc/html/
- https://docs.unity.com/
- https://dev.epicgames.com/documentation/en-us/unreal-engine/
