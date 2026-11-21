# Audio and animation production

- Create an action/event matrix: action, visual feedback, sound, timing, priority and cancellation.
- Animation: idle, move, jump, interact, impact, victory/defeat; skip unnecessary variants for tiny games.
- Sounds: menu, collection, collision, damage, success/failure, ambience; use original or verified licensed clips and track attribution.
- Browser media may require a user gesture. Add reliable mute and volume settings; don't default to loud sound.
- Use audio fallback states if loading fails; don't block the entire gameplay loop on missing music.
- Test playback and transitions in-engine; never claim audio listened to or soundtrack verified if not tested.
