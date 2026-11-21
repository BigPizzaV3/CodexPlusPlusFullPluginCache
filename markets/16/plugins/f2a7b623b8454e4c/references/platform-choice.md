# Platform architecture decision record

Preserve existing technology unless it is demonstrably unsuitable or user authorizes migration.

| Product requirement | Starting option | Decision notes |
| --- | --- | --- |
| Marketing/editorial/portfolio | static generator or React-based web | SEO and content authoring needs determine SSR vs static |
| Interactive browser-first app | React/Vite or Next.js if server rendering/full-stack routing is useful | choose based on actual needs, not fashion |
| Offline-capable browser install | PWA on existing web stack | browser/OS limits, sync/conflicts and sensitive caching |
| Native iOS | SwiftUI + selective UIKit | Apple HIG, signing/Xcode, persistence, iOS-only APIs |
| Native macOS | SwiftUI + selective AppKit | multi-window/menu/keyboard behavior and macOS SDK |
| Native Android | Kotlin + Jetpack Compose | Android permissions, back behavior, adaptive design |
| Shared iOS/Android | Expo/React Native or Flutter | existing stack, native modules, design fidelity, OTA/release cost |
| Web + mobile shared | evaluate Expo web or shared domain packages with separate UIs | don't force a single component tree where UX differs |

Before committing, record target platforms, required native features, offline needs, auth, likely build environment, dev skills, existing stack, performance/SEO needs, delivery route and restrictions. Do not assert Mac/Xcode available merely because user asks for iOS.
