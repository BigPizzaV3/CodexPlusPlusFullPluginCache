# Web and PWA quality references

- Framework selection follows project requirements and existing repo; verify current APIs from https://react.dev/, https://nextjs.org/docs and framework docs before implementation.
- Build accessible semantic HTML; keyboard navigation; labels; focus state; WCAG 2.2 contrast and motion preferences; responsive images and layout. Use performant fonts and load strategies.
- Security: separate client and server secrets, server-side access control, CSRF as relevant, safe cookie/session handling, XSS guards, secure dependencies, CSP as appropriate.
- UI states: initial, empty, loading, pending, error, retry, success, permissions, offline. Keep controls functional.
- PWA: correct web manifest, appropriate icons/start URL/display mode, HTTPS in production, service worker when needed, offline caching policy and update behavior.
- Never cache protected personal pages or auth tokens indiscriminately. Test install flows per browser/OS, offline fallback, stale-cache invalidation, out-of-date assets, reconnected writes/conflicts.
- Installation behavior, push and background sync vary widely by browser and OS. Never claim universal support.
- Tests: build/type/lint, unit, browser E2E, relevant accessibility checks, mobile/desktop renders, offline/PWA validation and performance as needed.

Official guidance: https://web.dev/learn/pwa/ ; https://developer.mozilla.org/ ; https://www.w3.org/TR/WCAG22/ .
