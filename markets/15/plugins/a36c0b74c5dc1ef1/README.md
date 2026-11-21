# Exekite

Build and improve games through your connected assistant. The assistant supplies the design and game code; Exekite stores the project, runs isolated engine checks and playtests, manages game assets, and prepares releases.

Try: “Make a small keyboard-controlled arcade game with geometric art,” “Improve the controls in my Exekite game,” or “Playtest my game and explain what remains before release.”

## What you need

An Exekite account. Creating and editing games requires a plan that includes game creation, and a game change needs an available Exekite balance above zero; listing, reading and playing your existing games do not. Store submission, signing, agreements, notarization and project deletion stay with you in Exekite Studio.

## Connect and choose your games

Connect Exekite from your assistant and sign in with your Exekite account; Exekite never asks for your password or a token in chat. On the consent page you choose which games the assistant may use: all current and future games (needed to create a new game) or selected games only. You can disconnect an assistant at any time in Studio under Account → Connected assistants. A password reset or change disconnects every assistant too.

## Generated assets

When you ask for Exekite-generated art, sprites, sound, music or 3D models, the assistant gets a price quote for that exact request and generates it right away. The charge comes off your existing Exekite balance and is never more than the quoted maximum; a generation that fails costs nothing. The assistant tells you what was generated and what it cost, then wires the asset into your game and tests it. Your assistant app may show its own permission prompt before a paid generation, depending on its settings. Art and sound made in code use no paid generation.

## Play, watch and inspect

Where the assistant app renders app views, ask it to show a game's job, playable preview, model or asset: it opens the focused **Exekite visual companion** for that exact work. You can watch Blender and Game Test while the assistant works, play a prepared verified build, and inspect models, sprites, images and sounds. Opening the companion never starts a game or spends from your balance. Apps without an inline view can open the same view in your browser after you sign in to Exekite.

After building or changing a game, the assistant prepares a preview link so you can play it. A preview link is a temporary unlisted link: anyone holding it can open it until it expires (one hour by default). Publishing a game on its public exekite.games page happens only when you ask for it.

## Embedded content

The visual companion plays a prepared game in a frame served from `https://chatgpt-play.exekite.games`, Exekite's separate domain for game code. Games run there, apart from exekite.com, where your Exekite sign-in lives. The frame receives a short-lived permission for one verified build of your own game and loads nothing from other sites. Live Game Test and Blender views stream from `https://chatgpt-stream.exekite.com`. If the frame cannot be shown, a preview link or the browser companion plays the same build.

## Data and control

The assistant host sends the selected tool arguments to Exekite and receives tool results. Depending on the requested action, this includes game design, source files, uploaded assets, screenshots, runtime observations, job state, and account/project metadata. Exekite uses Cloudflare for storage and runtime processing of projects, revisions, and operation records. Explicit paid media operations can send the asset description and required source media to fal; they do not start another game-authoring model. The assistant provider handles the conversation and returned results under its own policies.

OAuth connects the user's account and selected project grants. Passwords, access tokens, signing credentials, and provider keys do not belong in chat or project files. The user can revoke a connection in Studio's Account → Connected assistants settings. Revocation removes that connection's future access and ends its unexpired preview links; it does not delete the user's projects. Previously returned results remain subject to the assistant host's own data controls.

Preview links and upload/download links expire. A preview link is a temporary unlisted link that anyone holding it can open until it expires, at most one hour; an upload link lasts 15 minutes and a download link 5 minutes. These windows limit link access; they are not promises about project-data retention. Creating a public share changes who can access those game bytes; the skill uses public sharing only within the user's request. Store agreements, signing, submission, notarization, and project deletion require an authenticated person to finish the appropriate Studio step.

See the [privacy policy](https://exekite.com/privacy), [terms](https://exekite.com/terms), and [support](https://exekite.com/contact) for the service's current policies and help. This package does not add retention promises or change those policies.

## Package contents

The package includes the `exekite-studio` workflow skill ([skills/exekite-studio/SKILL.md](skills/exekite-studio/SKILL.md)), 14 craft skills for Exekite projects, and one authenticated MCP connection at `https://mcp.exekite.com/mcp`. The workflow skill links to the relevant craft as needed: game-code syntax, source layout, signals, lifetimes, collision and movement, resources, tile maps, HUD layout, start/pause input, debugging, and generated-media wiring. The included responsive overlay example belongs to the HUD skill.
