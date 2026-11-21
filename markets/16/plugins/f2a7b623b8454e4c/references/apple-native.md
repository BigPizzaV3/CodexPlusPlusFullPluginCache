# Apple-native implementation standard

Canonical sources: https://developer.apple.com/design/human-interface-guidelines/ and https://developer.apple.com/xcode/swiftui/ .

## iOS
- Prefer SwiftUI and native navigation patterns. Use UIKit bridges when needed for unsupported controls or system behavior. Respect safe areas, dynamic type, VoiceOver, Reduce Motion, localizations, dark mode and system focus.
- Separate view composition, observable state, persistence, networking and permissions. Consider transaction consistency, save/retry, navigation loss, app lifecycle and restoration.
- Use Swift Charts for appropriate native visualizations with accessible labels, units, legends, selection and truthful scales. Explore https://github.com/jordibruin/Swift-Charts-Examples for patterns only after confirming licensing and compatibility.
- Simulator UI tests or `xcodebuild` need a real macOS host with Xcode. Never claim iOS build/tests ran in Linux.

## macOS
- Native menus, commands/shortcuts, multiple windows, sidebars, split view, focus, drag/drop, document restoration and keyboard-first operation matter. Don't enlarge a phone layout.
- Where document data is involved, preserve user files; test autosave, failure recovery and undo/redo.
- Signing, entitlements, TestFlight, notarization and App Store submission require real credentials and explicit authorization.

Always check Xcode, SDK, target OS and API availability before using recently added SwiftUI frameworks.
