# Distribution and marketplace considerations

For web game: build output including index.html and all assets, correct MIME/path handling, responsive input, cache behavior and suitable hosting. Itch.io HTML ZIP must be checked against current platform instructions.

For Godot: export templates and presets are required, and appropriate device testing remains separate from headless export.
For Unity/Unreal: installed editor/toolchain licenses and resource demands must be checked; desktop/mobile signing/build target verification is mandatory.
For mobile: Android signing, iOS certificates/provisioning and app store review prerequisites apply. Never publish to accounts without user approval.
For narrative: Ren'Py distribution supports platform-specific packages; test script lint and save/load.
For all games: include license/attribution notices, gameplay controls, build/environment notes, accessibility options, content rating requirements where relevant, privacy disclosures when collecting analytics/accounts, and reproducible steps.

Export test gates: source integrity -> build/import -> launch packaged artifact -> actual interaction -> release notes. Never invent a hosted preview URL.
