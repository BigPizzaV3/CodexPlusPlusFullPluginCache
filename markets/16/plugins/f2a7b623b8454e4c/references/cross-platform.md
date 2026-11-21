# Cross-platform mobile choices

- Expo/React Native docs: https://docs.expo.dev/ ; Flutter: https://docs.flutter.dev/ .
- Evaluate existing repo, performance, native integrations, web support, development skills, build/release pipeline, package ecosystem and UX requirements.
- The logic/data model may be shared, while navigation, typography, back behavior, safe areas, touch targets and settings/permissions require platform specificity.
- Do not assert iOS test success because Metro/Expo web preview runs or Android bundle builds.
- Expo/React Native: package compatibility with current Expo SDK, navigation, deep links, EAS builds and plugin review; avoid deprecated package APIs.
- Flutter: widget lifecycle, adaptive Cupertino/Material decisions, platform channels, configuration and real device testing.
- Reconcile platform-specific dependency installation, native permissions and signing. Document per-target evidence separately.
