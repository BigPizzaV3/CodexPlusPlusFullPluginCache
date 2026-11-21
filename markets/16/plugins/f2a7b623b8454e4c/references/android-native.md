# Native Android standard

Official source: https://developer.android.com/develop/ui/compose/designsystems/material3 and https://developer.android.com/develop/ui/compose/layouts/adaptive .

- Prefer modern Kotlin + Jetpack Compose when starting new, unless user/framework requirements differ.
- Material 3 is guidance, not mandatory visual homogeneity; align color, typography, shape and motion with app identity, readable hierarchy, accessible contrasts and platform conventions.
- Handle window insets, back navigation, adaptive screen classes, permission rationale, lifecycle, offline behavior and system bars.
- Separate composables, state holder/ViewModel, data layer, network and persistence. Use stable dependency versions and avoid unnecessary experimental APIs.
- Test via Android SDK/Gradle; emulator/instrumentation tests need actual environment. No fake device test claims.
- Keep release signing keys out of repository/chat. Play Console publishing and user data disclosures require approval.
