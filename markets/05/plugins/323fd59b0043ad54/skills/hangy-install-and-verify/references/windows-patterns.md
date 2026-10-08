# Windows Installation Patterns

## Project-local studio

Use this pattern for tools such as Remotion Studio:

1. Confirm Node.js and package-manager availability.
2. Verify the current minimum runtime, scaffold command, and supported flags from official documentation, package metadata, and the installed CLI's `--help`. Do not supply remembered version thresholds or flags as facts.
3. Inspect the destination and avoid mixing with unrelated files.
4. Scaffold a dedicated project.
5. Install pinned or current compatible dependencies from official registries.
6. Run formatting, type checking, and linting.
7. Start the studio with an explicit host and port when needed.
8. Poll the local URL until it returns HTTP 200.
9. Open the URL and provide the exact command for reopening.

Do not describe a browser-based project studio as a standalone desktop application.
If current requirements cannot be verified, state that limitation and withhold exact minimum versions or command flags until verification is possible.

## Mobile-only application

Use this pattern only after verifying that a supported Windows version does not exist:

1. Prefer an already installed, trusted emulator.
2. Use the official store listing inside the emulator.
3. Confirm the package identity and installed version.
4. Launch to a stable app screen, not merely the emulator home.
5. Explain that the user reopens the emulator first and then the app.

Do not install random APK files when an official store route is available.

## Native installer or package manager

- Verify publisher, URL, package ID, and architecture.
- Prefer silent flags only when their effects are understood.
- Check the installed binary's path and version.
- Launch the app once and confirm it remains running or shows a usable window.
- Record whether a restart is required.

## CLI or service

- Resolve duplicate binaries with `Get-Command -All`.
- Verify which executable PATH selects.
- Run a harmless version or help command.
- For services, verify listening port and process identity.
- Do not leave test services running unless the requested ready state requires it.
