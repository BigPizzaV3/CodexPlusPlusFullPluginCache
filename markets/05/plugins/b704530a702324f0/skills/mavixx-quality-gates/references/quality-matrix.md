# Quality matrix

Select checks based on project type and change risk.

| Area | Minimum evidence | Apply when |
| --- | --- | --- |
| Build | Production build or repository equivalent | Buildable software |
| Static quality | Formatter/linter/type checker configured by repo | Tool exists or change justifies it |
| Functional | Critical journeys plus relevant error paths | Behavior changed |
| Visual | Rendered desktop/mobile inspection and interaction; compare with the pre-change baseline when available | User interface changed |
| Accessibility | Keyboard, focus, semantics, labels, contrast, reduced motion | User interface changed |
| Security | Secrets, authz, input/data boundaries, dependency exposure | Relevant attack/data surface exists |
| Performance | Load/render/bundle/query/media/animation evidence | Change can affect performance |
| Data | Migration, compatibility, backup/rollback | Persistent state changes |
| Release | Environment, deployment, observability, rollback notes | Handoff or deployment |

Do not add heavyweight tooling solely to create a passing report. Prefer project-native checks; recommend missing infrastructure separately when adding it is outside scope.
